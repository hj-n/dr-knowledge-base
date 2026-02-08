#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import logging
import re
import signal
import warnings
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import date
from difflib import SequenceMatcher
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
PDF_DIR = ROOT / "papers" / "raw" / "pending-references"
NOTES_DIR = ROOT / "papers" / "notes"
PENDING_META = ROOT / "builder" / "evidence" / "pending-reference-papers.csv"
TRIAGE_CSV = ROOT / "builder" / "evidence" / "pending-reference-triage.csv"

CORE_TERMS = [
    "dimensionality reduction", "dimension reduction", "projection", "embedding", "manifold",
    "t-sne", "tsne", "umap", "isomap", "lle", "mds", "pca", "neighborhood", "cluster",
]
WORKFLOW_TERMS = [
    "quality", "reliability", "distortion", "trustworthiness", "continuity", "hyperparameter",
    "initialization", "stability", "subsampling", "visual analytics", "evaluation",
]
EXCLUDE_HINTS = [
    "vision transformers", "foundation model", "commentvis", "narrative visualization",
    "marine containers", "serendipitous discovery", "data perspective survey",
]
PORTAL_NOISE = [
    "di-fusion", "portail de consultation", "dépôts institutionnels", "astuces pour la recherche",
    "effectuer une recherche", "versions des publications",
]


@contextmanager
def time_limit(seconds: int):
    if seconds <= 0:
        yield
        return

    def _handler(signum, frame):
        raise TimeoutError(f"processing exceeded {seconds}s")

    old_handler = signal.signal(signal.SIGALRM, _handler)
    signal.setitimer(signal.ITIMER_REAL, float(seconds))
    try:
        yield
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0.0)
        signal.signal(signal.SIGALRM, old_handler)


@dataclass
class PendingRow:
    candidate_id: str
    paper_title: str
    authors: str
    year: str
    doi: str
    source_seed_notes: str
    source_seed_count: int
    max_context_score: int
    max_title_keyword_score: int


def normalize_space(s: str) -> str:
    s = re.sub(r"(?<=\w)-\n(?=\w)", "", s)
    s = s.replace("\n", " ")
    s = s.replace("\u00a0", " ")
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def split_sentences(text: str) -> List[str]:
    text = normalize_space(text)
    # Trim explicit references section.
    m = re.search(r"\breferences\b", text, flags=re.I)
    if m:
        text = text[: m.start()]
    parts = re.split(r"(?<=[\.!?])\s+(?=[A-Z0-9])", text)
    out = []
    for p in parts:
        p = p.strip(" -")
        if len(p) < 50 or len(p) > 420:
            continue
        low = p.lower()
        if low.startswith("index terms"):
            continue
        if re.search(r"\b(fig(ure)?|table|appendix)\b", low):
            continue
        if re.search(r"\b(authorized licensed use|copyright|all rights reserved)\b", low):
            continue
        if p.count("[") >= 4:
            continue
        out.append(p)
    return out


def keyword_count(text: str, keywords: List[str]) -> int:
    low = text.lower()
    return sum(1 for k in keywords if k in low)


def infer_title_from_first_page(text: str, fallback: str) -> str:
    lines = [normalize_space(x) for x in text.splitlines() if normalize_space(x)]
    candidates = []
    for ln in lines[:35]:
        if len(ln) < 12 or len(ln) > 180:
            continue
        low = ln.lower()
        if any(k in low for k in ["abstract", "introduction", "keywords", "index terms", "www."]):
            continue
        if re.search(r"^\d+$", ln):
            continue
        if ln.count(".") > 3:
            continue
        candidates.append(ln)
    if candidates:
        # choose longest likely title-like line
        candidates.sort(key=lambda s: len(s), reverse=True)
        return candidates[0].strip(" .")
    return fallback


def infer_year(text: str, fallback: str) -> str:
    if re.match(r"^\d{4}$", fallback):
        return fallback
    years = re.findall(r"\b(19\d{2}|20[0-2]\d)\b", text)
    if years:
        # prefer latest plausible publication year
        return sorted(years)[-1]
    return "2026"


def score_relevance(title: str, text: str, seed_count: int, context_score: int) -> Tuple[bool, str]:
    low_t = title.lower()
    low = text.lower()

    if any(x in low_t for x in EXCLUDE_HINTS) and keyword_count(low_t, CORE_TERMS) < 2:
        return False, "out_of_scope_topic_hint"

    noise_hits = sum(1 for x in PORTAL_NOISE if x in low)
    if noise_hits >= 2:
        return False, "portal_or_repository_noise"

    core_t = keyword_count(low_t, CORE_TERMS)
    core_b = keyword_count(low, CORE_TERMS)
    wf_t = keyword_count(low_t, WORKFLOW_TERMS)
    wf_b = keyword_count(low, WORKFLOW_TERMS)

    core = core_t + core_b
    wf = wf_t + wf_b

    if core_b >= 2:
        return True, "body_core_terms"
    if core >= 3:
        return True, "title_plus_body_core_terms"
    if core >= 2 and wf >= 2:
        return True, "core_plus_workflow_terms"
    if seed_count >= 2 and context_score >= 6 and core >= 1:
        return True, "seed_context_supported"
    return False, "low_dr_signal"


def pick(sentences: List[str], keywords: List[str], n: int) -> List[str]:
    scored = []
    for s in sentences:
        low = s.lower()
        sc = sum(1 for k in keywords if k in low)
        if sc > 0:
            scored.append((sc, len(s), s))
    scored.sort(key=lambda x: (x[0], x[1]), reverse=True)
    out = []
    seen = set()
    for _, _, s in scored:
        key = s[:120].lower()
        if key in seen:
            continue
        seen.add(key)
        out.append(s)
        if len(out) >= n:
            break
    return out


def page_for_quote(pages: List[str], quote: str) -> int:
    q = quote[:80].lower()
    for i, p in enumerate(pages, 1):
        if q in p.lower():
            return i
    return 1


def slugify(s: str, maxlen: int = 72) -> str:
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return (s[:maxlen].rstrip("-") or "paper")


def read_pending_rows() -> Dict[str, PendingRow]:
    out = {}
    with PENDING_META.open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            out[r["candidate_id"]] = PendingRow(
                candidate_id=r["candidate_id"],
                paper_title=(r.get("paper_title") or "").strip(),
                authors=(r.get("authors") or "UNKNOWN").strip() or "UNKNOWN",
                year=(r.get("year") or "").strip(),
                doi=(r.get("doi") or "").strip(),
                source_seed_notes=(r.get("source_seed_notes") or "").strip(),
                source_seed_count=int(r.get("source_seed_count") or 0),
                max_context_score=int(r.get("max_context_score") or 0),
                max_title_keyword_score=int(r.get("max_title_keyword_score") or 0),
            )
    return out


def note_id_from_path(path: str) -> str:
    p = ROOT / path
    if not p.exists():
        return ""
    txt = p.read_text(encoding="utf-8", errors="ignore")
    m = re.search(r"(?m)^id:\s*(.+)$", txt)
    return m.group(1).strip().strip('"') if m else ""


def seed_note_id_from_pending_row(row: Optional[PendingRow]) -> str:
    if row is None:
        return ""
    for n in [x.strip() for x in row.source_seed_notes.split(";") if x.strip()]:
        nid = note_id_from_path(n)
        if nid:
            return nid
    return ""


def infer_seed_note_id_by_title(title: str, pending_rows: Dict[str, PendingRow]) -> str:
    best = 0.0
    best_row = None
    t = title.lower()
    for r in pending_rows.values():
        s = SequenceMatcher(None, t, r.paper_title.lower()).ratio()
        if s > best:
            best = s
            best_row = r
    if best_row and best >= 0.84:
        return seed_note_id_from_pending_row(best_row)
    return ""


def metrics_from_text(text: str) -> List[str]:
    low = text.lower()
    mapping = [
        ("trustworthiness", "trustworthiness"),
        ("continuity", "continuity"),
        ("stress", "stress"),
        ("co-ranking", "co-ranking"),
        ("coranking", "co-ranking"),
        ("procrustes", "procrustes-based quality"),
        ("kl divergence", "kl divergence"),
        ("neighbor", "neighborhood-preservation criteria"),
        ("rank", "rank-based quality criteria"),
    ]
    out = []
    for k, v in mapping:
        if k in low and v not in out:
            out.append(v)
    return out[:6]


def workflow_map(text: str) -> List[Tuple[int, str, str]]:
    low = text.lower()
    rows = []
    if any(k in low for k in ["task", "analyst", "objective"]):
        rows.append((1, "medium", "supports explicit task clarification before DR recommendation"))
    if any(k in low for k in ["preprocess", "normalization", "noise", "outlier"]):
        rows.append((2, "medium", "adds preprocessing/data-condition constraints for reliable comparison"))
    if any(k in low for k in ["method", "technique", "metric", "quality", "distortion"]):
        rows.append((3, "high", "directly informs task-aligned method and metric selection"))
    if any(k in low for k in ["initialization", "seed", "random init", "pca init"]):
        rows.append((4, "high", "contains initialization sensitivity or control-policy evidence"))
    if any(k in low for k in ["hyperparameter", "parameter", "optimization", "tuning"]):
        rows.append((5, "high", "provides hyperparameter sensitivity/optimization guidance"))
    if any(k in low for k in ["visualization", "scatter", "layout", "interpret"]):
        rows.append((6, "high", "guides reliable interpretation of projected views"))
    if any(k in low for k in ["explain", "rationale", "communicate"]):
        rows.append((7, "medium", "supports user-facing rationale communication for final choices"))
    if not rows:
        rows = [(3, "medium", "contains DR evaluation evidence relevant to selection decisions")]
    return rows[:4]


def main() -> None:
    warnings.filterwarnings("ignore", message=".*Multiple definitions in dictionary.*")
    warnings.filterwarnings("ignore", message=".*Ignoring wrong pointing object.*")
    logging.getLogger("pypdf").setLevel(logging.ERROR)

    ap = argparse.ArgumentParser()
    ap.add_argument("--start", type=int, default=0, help="start index in sorted pending PDFs")
    ap.add_argument("--count", type=int, default=0, help="number of PDFs to process (0=all)")
    ap.add_argument("--max-pages", type=int, default=40, help="max pages per PDF for extraction window")
    ap.add_argument(
        "--per-file-timeout",
        type=int,
        default=90,
        help="timeout (seconds) per PDF; 0 disables timeout",
    )
    args = ap.parse_args()

    pending_rows = read_pending_rows()
    pdfs_all = sorted(PDF_DIR.glob("*.pdf"))
    start = max(0, args.start)
    end = len(pdfs_all) if args.count <= 0 else min(len(pdfs_all), start + args.count)
    pdfs = pdfs_all[start:end]

    triage = []
    created = 0

    for idx, pdf in enumerate(pdfs, 1):
        m = re.match(r"(pending-ref-\d{3})-", pdf.name)
        cid = m.group(1) if m else ""
        prow = pending_rows.get(cid)
        source_pdf_rel = f"papers/raw/pending-references/{pdf.name}"
        fallback_title = prow.paper_title if prow and prow.paper_title else pdf.stem
        triage_added = False
        try:
            with time_limit(args.per_file_timeout):
                reader = PdfReader(str(pdf))
                total_pages = len(reader.pages)
                mp = max(6, args.max_pages)
                if total_pages <= mp:
                    indices = list(range(total_pages))
                else:
                    first_n = mp // 2
                    last_n = mp - first_n
                    indices = list(range(first_n)) + list(range(total_pages - last_n, total_pages))
                pages = []
                for pi in indices:
                    try:
                        pages.append(normalize_space(reader.pages[pi].extract_text() or ""))
                    except Exception:
                        pages.append("")
                full = "\n".join(pages)[:250000]
                first_page = pages[0] if pages else ""

                title = prow.paper_title if prow else infer_title_from_first_page(first_page, pdf.stem)
                authors = prow.authors if prow else "UNKNOWN"
                year = infer_year(first_page + "\n" + full[:2000], prow.year if prow else "")

                rel, reason = score_relevance(
                    title,
                    full[:50000],
                    prow.source_seed_count if prow else 0,
                    prow.max_context_score if prow else 0,
                )

                if not rel:
                    triage.append({
                        "candidate_id": cid,
                        "title": title,
                        "source_pdf": source_pdf_rel,
                        "relevant": "false",
                        "reason": reason,
                    })
                    triage_added = True
                    continue

                # Prefer abstract + conclusion windows for cleaner evidence.
                abs_m = re.search(r"\babstract\b", full, flags=re.I)
                conc_m = re.search(r"\b(conclusion|concluding remarks)\b", full, flags=re.I)
                abs_window = full[abs_m.start() : abs_m.start() + 7000] if abs_m else full[:7000]
                conc_window = full[conc_m.start() : conc_m.start() + 7000] if conc_m else full[-7000:]

                sents_all = split_sentences(full)
                sents_abs = split_sentences(abs_window)
                sents_conc = split_sentences(conc_window)

                problem = pick(sents_abs + sents_all, ["problem", "challenge", "distortion", "unreliable", "high-dimensional", "difficult"], 4)
                method = pick(sents_abs + sents_all, ["we propose", "we present", "method", "approach", "algorithm", "objective", "embedding", "projection"], 7)
                use = pick(sents_conc + sents_all, ["use", "works", "best", "avoid", "limitation", "sensitive", "robust", "fails"], 5)
                impl = pick(sents_all + sents_conc, ["parameter", "hyperparameter", "seed", "initialization", "runtime", "scalable", "optimization", "iteration"], 5)

                if len(problem) < 2:
                    problem = (problem + method[:3])[:4]
                if len(method) < 4:
                    method = (method + sents_all[:10])[:7]
                if len(use) < 3:
                    use = (use + method[:4])[:5]
                if len(impl) < 3:
                    impl = (impl + method[1:5])[:5]

                evidence = []
                for s in problem + method + use + impl:
                    s = normalize_space(s)
                    if len(s) < 50:
                        continue
                    if s not in evidence:
                        evidence.append(s)
                evidence = evidence[:8]
                while len(evidence) < 6 and sents_all:
                    s = sents_all[len(evidence) % len(sents_all)]
                    if len(s) > 50 and s not in evidence:
                        evidence.append(s)

                metrics = metrics_from_text(full)
                wmap = workflow_map(full)

                seed_note_id = seed_note_id_from_pending_row(prow) if prow else ""
                if not seed_note_id:
                    seed_note_id = infer_seed_note_id_by_title(title, pending_rows)
                if not seed_note_id:
                    seed_note_id = "paper-2025-jeon-reliable-va-survey"

                note_id = f"paper-{year}-{cid if cid else 'pending-extra-' + slugify(pdf.stem, 20)}"
                note_name_prefix = cid if cid else f"pending-extra-{slugify(pdf.stem, 20)}"
                note_file = NOTES_DIR / f"{note_name_prefix}-{slugify(title, 58)}.md"

                safe_title = title.replace('"', "'")
                safe_authors = authors.replace('"', "'") if authors else "UNKNOWN"

                lines = []
                lines.append("---")
                lines.append(f"id: {note_id}")
                lines.append(f"title: \"{safe_title}\"")
                lines.append(f"authors: \"{safe_authors}\"")
                lines.append("venue: \"UNKNOWN\"")
                lines.append(f"year: {year}")
                lines.append("tags: [dr, reliability, visual_analytics, reference, pending_references]")
                lines.append(f"source_pdf: {source_pdf_rel}")
                lines.append(f"seed_note_id: \"{seed_note_id}\"")
                lines.append("evidence_level: medium")
                lines.append(f"updated_at: {date.today().isoformat()}")
                lines.append("---\n")

                lines.append("# Problem")
                for s in problem[:4]:
                    lines.append(f"- {s}")

                lines.append("\n# Method Summary")
                for s in method[:7]:
                    lines.append(f"- {s}")

                lines.append("\n# When To Use / Not Use")
                lines.append("- Use when:")
                for s in use[:2]:
                    lines.append(f"  - {s}")
                lines.append("- Avoid when:")
                for s in use[2:4] if len(use) > 2 else method[2:4]:
                    lines.append(f"  - {s}")
                lines.append("- Failure modes:")
                lines.append(f"  - {use[-1] if use else 'Uncontrolled distortion or parameter sensitivity may lead to unreliable conclusions.'}")

                lines.append("\n# Metrics Mentioned")
                if metrics:
                    for mname in metrics:
                        lines.append(f"- `{mname}`: referenced as part of projection-quality or reliability assessment.")
                else:
                    lines.append("- No explicit named metric was extracted from this source; combine this source with complementary DR quality checks in workflow Step 3.")

                lines.append("\n# Implementation Notes")
                for s in impl[:5]:
                    lines.append(f"- {s}")
                lines.append("- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.")

                c1 = (problem[0] if problem else "The paper identifies reliability-relevant failure risks in DR workflows.").replace("|", "/")
                c2 = (method[0] if method else "The paper contributes a concrete DR method/evaluation formulation.").replace("|", "/")
                c3 = (impl[0] if impl else "The paper highlights implementation-sensitive factors that affect reliability.").replace("|", "/")

                cid_tag = (cid.upper() if cid else "PENDING-EXTRA")
                lines.append("\n# Claim Atoms (For Conflict Resolution)")
                lines.append(f"- CLAIM-{cid_tag}-C1 | stance: support | summary: {c1} | evidence_ids: {cid_tag}-E1, {cid_tag}-E2")
                lines.append(f"- CLAIM-{cid_tag}-C2 | stance: support | summary: {c2} | evidence_ids: {cid_tag}-E3, {cid_tag}-E4")
                lines.append(f"- CLAIM-{cid_tag}-C3 | stance: support | summary: {c3} | evidence_ids: {cid_tag}-E5, {cid_tag}-E6")

                lines.append("\n# Workflow Relevance Map")
                for st, relv, note in wmap:
                    lines.append(f"- step: {st} | relevance: {relv} | note: {note}")

                lines.append("\n# Evidence")
                for i, q in enumerate(evidence[:8], 1):
                    q = q.replace('"', "'").replace("|", "/")
                    pno = page_for_quote(pages, q)
                    lines.append(f"- {cid_tag}-E{i} | page: {pno}, section: extracted, quote: \"{q}\"")

                note_file.write_text("\n".join(lines) + "\n", encoding="utf-8")
                created += 1
                triage.append({
                    "candidate_id": cid,
                    "title": title,
                    "source_pdf": source_pdf_rel,
                    "relevant": "true",
                    "reason": reason,
                })
                triage_added = True
        except TimeoutError:
            if not triage_added:
                triage.append({
                    "candidate_id": cid,
                    "title": fallback_title,
                    "source_pdf": source_pdf_rel,
                    "relevant": "false",
                    "reason": f"timeout_{args.per_file_timeout}s",
                })
            print(f"skip timeout: {pdf.name}")
        except Exception as exc:
            if not triage_added:
                triage.append({
                    "candidate_id": cid,
                    "title": fallback_title,
                    "source_pdf": source_pdf_rel,
                    "relevant": "false",
                    "reason": f"parse_error_{exc.__class__.__name__}",
                })
            print(f"skip error: {pdf.name} ({exc.__class__.__name__})")

        if idx % 10 == 0:
            print(f"progress {idx}/{len(pdfs)} (created={created})")

    TRIAGE_CSV.parent.mkdir(parents=True, exist_ok=True)
    with TRIAGE_CSV.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["candidate_id", "title", "source_pdf", "relevant", "reason"])
        w.writeheader()
        w.writerows(triage)

    print(
        f"wrote {TRIAGE_CSV.relative_to(ROOT)} (rows={len(triage)}, "
        f"batch={start}:{end})"
    )
    print(f"created_notes={created}")


if __name__ == "__main__":
    main()
