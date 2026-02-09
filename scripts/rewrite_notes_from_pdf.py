#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import signal
import warnings
from contextlib import contextmanager
from datetime import date
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
NOTES_DIR = ROOT / "papers" / "notes"
TODAY = date.today().isoformat()

REQUIRED_HEADERS = [
    "# Problem",
    "# Method Summary",
    "# When To Use / Not Use",
    "# Metrics Mentioned",
    "# Implementation Notes",
    "# Claim Atoms (For Conflict Resolution)",
    "# Workflow Relevance Map",
    "# Evidence",
]

METRIC_HINTS: List[Tuple[str, str, str]] = [
    ("tnc", "trustworthiness", "Trustworthiness and Continuity behavior"),
    ("mrre", "mean relative rank error", "mean relative rank errors across neighborhood scales"),
    ("lcmc", "local continuity meta", "local continuity meta-criterion for neighborhood overlap"),
    ("nh", "neighborhood hit", "label-based neighborhood hit"),
    ("ca_tnc", "class-aware trustworthiness", "class-aware trustworthiness/continuity"),
    ("l_tnc", "label-trustworthiness", "label-conditioned trustworthiness/continuity"),
    ("nd", "neighbor-shape", "neighbor-shape dissimilarity or neighbor distortion"),
    ("dtm", "distance-to-measure", "distance-to-measure signal"),
    ("kl_div", "kullback", "Kullback-Leibler divergence behavior"),
    ("dsc", "distance consistency", "distance consistency for class separation"),
    ("pr", "pearson", "pairwise-distance correlation behavior"),
    ("srho", "spearman", "rank-correlation of pairwise distances"),
    ("ivm", "silhouette", "internal clustering validation behavior"),
    ("c_evm", "adjusted rand", "external clustering validation against labels"),
    ("snc", "steadiness", "Steadiness/Cohesiveness inter-cluster reliability"),
    ("topo", "topological", "topology-related structure behavior"),
    ("proc", "procrustes", "Procrustes local shape agreement"),
    ("stress", "stress", "stress-based distance distortion"),
    ("sn_stress", "scale-invariant", "scale-normalized stress"),
    ("nm_stress", "non-metric stress", "non-metric stress behavior"),
    ("qnx", "qnx", "QNX neighborhood-rank quality"),
    ("spectral_overlap", "spectral overlap", "spectral overlap consistency"),
]

NOISE_PATTERNS = [
    r"authorized licensed use",
    r"all rights reserved",
    r"copyright",
    r"received:\s*\d",
    r"accepted:\s*\d",
    r"published:\s*\d",
    r"doi:\s*",
    r"correspondence:",
    r"e-mail:",
    r"index terms",
    r"proc\.",
    r"arxiv:",
]


@contextmanager
def time_limit(seconds: int):
    if seconds <= 0:
        yield
        return

    def _handler(signum, frame):
        raise TimeoutError(f"timeout_{seconds}s")

    old = signal.signal(signal.SIGALRM, _handler)
    signal.setitimer(signal.ITIMER_REAL, float(seconds))
    try:
        yield
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0.0)
        signal.signal(signal.SIGALRM, old)


def parse_frontmatter(text: str) -> Tuple[Dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    fm_raw = text[4:end]
    body = text[end + 5 :]
    data: Dict[str, str] = {}
    for line in fm_raw.splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        data[k.strip()] = v.strip()
    return data, body


def serialize_frontmatter(data: Dict[str, str]) -> str:
    order = [
        "id",
        "title",
        "authors",
        "venue",
        "year",
        "tags",
        "source_pdf",
        "seed_note_id",
        "evidence_level",
        "updated_at",
    ]
    out = ["---"]
    for k in order:
        if k in data:
            out.append(f"{k}: {data[k]}")
    for k in data:
        if k not in order:
            out.append(f"{k}: {data[k]}")
    out.append("---")
    out.append("")
    return "\n".join(out)


def normalize_text(s: str) -> str:
    s = re.sub(r"(?<=\w)-\n(?=\w)", "", s)
    s = s.replace("\u00a0", " ")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n{2,}", "\n", s)
    return s


def likely_noise_sentence(s: str) -> bool:
    low = s.lower()
    if len(s) < 45 or len(s) > 460:
        return True
    if sum(ch.isalpha() for ch in s) < 20:
        return True
    if sum(ch.isdigit() for ch in s) > max(12, len(s) // 4):
        return True
    if low.count("@")==1 and " " not in low:
        return True
    if any(re.search(p, low) for p in NOISE_PATTERNS):
        return True
    if "|" in s or "\x00" in s:
        return True
    if re.search(r"\b(fig|figure|table)\s*\d", low):
        return True
    return False


def split_sentences(text: str) -> List[str]:
    text = normalize_text(text)
    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text).strip()
    parts = re.split(r"(?<=[\.!?])\s+(?=[A-Z0-9\(\[])", text)
    out: List[str] = []
    for p in parts:
        p = p.strip(" -")
        if likely_noise_sentence(p):
            continue
        out.append(p)
    return out


def choose(sentences: List[str], keywords: Iterable[str], n: int) -> List[str]:
    kws = [k.lower() for k in keywords]
    scored: List[Tuple[int, int, str]] = []
    for s in sentences:
        low = s.lower()
        score = sum(1 for k in kws if k in low)
        if score <= 0:
            continue
        scored.append((score, len(s), s))
    scored.sort(key=lambda x: (x[0], x[1]), reverse=True)
    out: List[str] = []
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


def get_text_windows(pages: List[str]) -> Tuple[str, str, str]:
    full = "\n".join(pages)
    low = full.lower()
    a = low.find("abstract")
    c = max(low.rfind("conclusion"), low.rfind("discussion"), low.rfind("limitations"))
    abstract = full[a : min(a + 9000, len(full))] if a != -1 else full[:9000]
    conclusion = full[c : min(c + 9000, len(full))] if c != -1 else full[-9000:]
    return full, abstract, conclusion


def find_page(pages: List[str], quote: str) -> int:
    q = re.sub(r"\s+", " ", quote).strip().lower()[:90]
    for idx, p in enumerate(pages, start=1):
        if q and q in p.lower():
            return idx
    return 1


def detect_metrics(full_text: str) -> List[Tuple[str, str]]:
    low = full_text.lower()
    found: List[Tuple[str, str]] = []
    for metric_id, hint, desc in METRIC_HINTS:
        if metric_id in low or hint in low:
            found.append((metric_id, desc))
    return found[:10]


def workflow_map(full_text: str) -> List[Tuple[int, str, str]]:
    low = full_text.lower()
    rows: List[Tuple[int, str, str]] = []
    if any(k in low for k in ["task", "analysis goal", "objective", "user study"]):
        rows.append((1, "medium", "supports task clarification before model selection"))
    if any(k in low for k in ["normalize", "normalization", "preprocess", "noise", "outlier", "scale"]):
        rows.append((2, "medium", "adds constraints for preprocessing and data-audit checks"))
    if any(k in low for k in ["metric", "measure", "evaluate", "reliability", "distortion"]):
        rows.append((3, "high", "directly informs task-aligned technique/metric selection"))
    if any(k in low for k in ["initialization", "seed", "random init", "pca init"]):
        rows.append((5, "medium", "adds initialization sensitivity guidance"))
    if any(k in low for k in ["hyperparameter", "perplexity", "n_neighbors", "optimization", "bayes"]):
        rows.append((6, "high", "adds hyperparameter sensitivity or optimization guidance"))
    if any(k in low for k in ["visualization", "scatter", "interpret", "explain"]):
        rows.append((7, "high", "supports visualization interpretation and user explanation"))
    if not rows:
        rows.append((3, "medium", "contains DR evidence relevant to reliable configuration selection"))
    return rows[:5]


def rebuild_note(note_path: Path, timeout_sec: int, max_pages: int) -> Tuple[bool, str]:
    text = note_path.read_text(encoding="utf-8", errors="ignore")
    fm, _ = parse_frontmatter(text)
    source_pdf = fm.get("source_pdf", "").strip()
    if not source_pdf.startswith("papers/raw/"):
        return False, "skip_non_local_source"

    pdf_path = ROOT / source_pdf
    if not pdf_path.exists():
        return False, "missing_source_pdf"

    with time_limit(timeout_sec):
        reader = PdfReader(str(pdf_path))
        total = len(reader.pages)
        if total <= max_pages:
            idxs = list(range(total))
        else:
            first = max_pages // 2
            last = max_pages - first
            idxs = list(range(first)) + list(range(total - last, total))

        pages: List[str] = []
        for i in idxs:
            try:
                ptxt = reader.pages[i].extract_text() or ""
            except Exception:
                ptxt = ""
            pages.append(normalize_text(ptxt))

    full, abstract, conclusion = get_text_windows(pages)
    s_all = split_sentences(full)
    s_abs = split_sentences(abstract)
    s_con = split_sentences(conclusion)

    problem = choose(s_abs + s_all, [
        "challenge", "problem", "difficult", "distortion", "unreliable", "high-dimensional", "limitation", "pitfall"
    ], 6)
    method = choose(s_abs + s_all, [
        "we propose", "we introduce", "method", "algorithm", "objective", "optimiz", "embedding", "projection", "evaluate"
    ], 8)
    use = choose(s_con + s_all, [
        "use", "when", "works", "best", "avoid", "limitation", "sensitive", "fail", "warning"
    ], 8)
    impl = choose(s_all + s_con, [
        "hyperparameter", "parameter", "perplexity", "n_neighbors", "runtime", "complexity", "scale", "seed", "initialization"
    ], 8)

    if len(problem) < 3:
        problem = (problem + method[:3] + s_abs[:3])[:6]
    if len(method) < 4:
        method = (method + s_abs[:5] + s_all[:6])[:8]
    if len(use) < 4:
        use = (use + s_con[:5] + method[:4])[:8]
    if len(impl) < 4:
        impl = (impl + method[2:8] + s_all[:6])[:8]

    metrics = detect_metrics(full)
    wmap = workflow_map(full)

    evidence_pool: List[str] = []
    for s in problem + method + use + impl:
        if s not in evidence_pool:
            evidence_pool.append(s)
    for s in s_abs + s_con + s_all:
        if len(evidence_pool) >= 12:
            break
        if s not in evidence_pool:
            evidence_pool.append(s)

    evidence = evidence_pool[:12]
    while len(evidence) < 6 and s_all:
        s = s_all[len(evidence) % len(s_all)]
        if s not in evidence:
            evidence.append(s)

    note_tag = re.sub(r"[^A-Z0-9]", "", fm.get("id", note_path.stem).upper())[:18] or "NOTE"

    # frontmatter update only
    fm["updated_at"] = TODAY

    lines: List[str] = []
    lines.append(serialize_frontmatter(fm).rstrip())

    lines.append("# Problem")
    for s in problem[:5]:
        lines.append(f"- {s}")

    lines.append("\n# Method Summary")
    for s in method[:7]:
        lines.append(f"- {s}")

    lines.append("\n# When To Use / Not Use")
    lines.append("- Use when:")
    for s in use[:3]:
        lines.append(f"  - {s}")
    lines.append("- Avoid when:")
    for s in use[3:5] if len(use) > 4 else method[:2]:
        lines.append(f"  - {s}")
    lines.append("- Failure modes:")
    for s in use[5:7] if len(use) > 6 else impl[:1]:
        lines.append(f"  - {s}")

    lines.append("\n# Metrics Mentioned")
    if metrics:
        for metric_id, desc in metrics:
            lines.append(f"- `{metric_id}`: {desc}.")
    else:
        lines.append("- No explicit named quality metric was confidently extracted from this source.")

    lines.append("\n# Implementation Notes")
    for s in impl[:6]:
        lines.append(f"- {s}")
    lines.append("- Keep preprocessing, initialization policy, and random-seed protocol fixed when comparing methods.")

    c1 = (problem[0] if problem else "This source defines a reliability-relevant DR problem setup.").replace("|", "/")
    c2 = (method[0] if method else "This source introduces a concrete DR method or evaluation mechanism.").replace("|", "/")
    c3 = (impl[0] if impl else "This source reports implementation-sensitive factors affecting reliability.").replace("|", "/")

    lines.append("\n# Claim Atoms (For Conflict Resolution)")
    lines.append(f"- CLAIM-{note_tag}-C1 | stance: support | summary: {c1} | evidence_ids: {note_tag}-E1, {note_tag}-E2")
    lines.append(f"- CLAIM-{note_tag}-C2 | stance: support | summary: {c2} | evidence_ids: {note_tag}-E3, {note_tag}-E4")
    lines.append(f"- CLAIM-{note_tag}-C3 | stance: support | summary: {c3} | evidence_ids: {note_tag}-E5, {note_tag}-E6")

    lines.append("\n# Workflow Relevance Map")
    for step, rel, note in wmap:
        lines.append(f"- step: {step} | relevance: {rel} | note: {note}")

    lines.append("\n# Evidence")
    for i, q in enumerate(evidence, start=1):
        q = q.replace('"', "'").replace("|", "/")
        pno = find_page(pages, q)
        lines.append(f"- {note_tag}-E{i} | page: {pno}, section: extracted, quote: \"{q}\"")

    new_text = "\n".join(lines).rstrip() + "\n"
    note_path.write_text(new_text, encoding="utf-8")
    return True, "rewritten"


def collect_notes(patterns: List[str]) -> List[Path]:
    out: List[Path] = []
    for pat in patterns:
        out.extend(sorted(NOTES_DIR.glob(pat)))
    # stable unique
    seen = set()
    uniq: List[Path] = []
    for p in out:
        if p in seen:
            continue
        seen.add(p)
        uniq.append(p)
    return uniq


def main() -> int:
    warnings.filterwarnings("ignore", message=r".*Multiple definitions in dictionary.*")
    warnings.filterwarnings("ignore", message=r".*Ignoring wrong pointing object.*")

    ap = argparse.ArgumentParser()
    ap.add_argument("--pattern", action="append", required=True, help="glob under papers/notes")
    ap.add_argument("--timeout", type=int, default=90)
    ap.add_argument("--max-pages", type=int, default=60)
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    notes = collect_notes(args.pattern)
    if args.limit > 0:
        notes = notes[: args.limit]

    ok = 0
    skipped = 0
    failed = 0
    for i, n in enumerate(notes, start=1):
        try:
            changed, status = rebuild_note(n, timeout_sec=args.timeout, max_pages=args.max_pages)
            if changed:
                ok += 1
            else:
                skipped += 1
            print(f"[{i}/{len(notes)}] {n.name}: {status}")
        except TimeoutError:
            failed += 1
            print(f"[{i}/{len(notes)}] {n.name}: timeout")
        except Exception as exc:
            failed += 1
            print(f"[{i}/{len(notes)}] {n.name}: error_{exc.__class__.__name__}")

    print(f"summary rewritten={ok} skipped={skipped} failed={failed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
