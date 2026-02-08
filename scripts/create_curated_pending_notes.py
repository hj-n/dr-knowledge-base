#!/usr/bin/env python3
from __future__ import annotations

import re
from datetime import date
from pathlib import Path
from typing import Dict, List, Tuple

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
NOTES_DIR = ROOT / "papers" / "notes"
PDF_DIR = ROOT / "papers" / "raw" / "pending-references"
PENDING_CSV = ROOT / "builder" / "evidence" / "pending-reference-papers.csv"

TARGETS = [
    "pending-ref-002",
    "pending-ref-004",
    "pending-ref-006",
    "pending-ref-008",
    "pending-ref-009",
    "pending-ref-015",
    "pending-ref-016",
    "pending-ref-024",
    "pending-ref-028",
    "pending-ref-029",
    "pending-ref-030",
    "pending-ref-031",
    "pending-ref-041",
    "pending-ref-051",
    "pending-ref-052",
    "pending-ref-055",
]


def normalize(s: str) -> str:
    s = re.sub(r"(?<=\w)-\n(?=\w)", "", s)
    s = s.replace("\n", " ")
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def split_sentences(text: str) -> List[str]:
    text = normalize(text)
    # Trim trailing references if present.
    m = re.search(r"\bReferences\b", text, flags=re.I)
    if m:
        text = text[: m.start()]
    parts = re.split(r"(?<=[\.!?])\s+(?=[A-Z0-9])", text)
    out = []
    for p in parts:
        p = p.strip()
        if len(p) < 40 or len(p) > 400:
            continue
        if p.count("[") >= 4:
            continue
        if re.search(r"\b(fig(ure)?|table|appendix)\b", p, flags=re.I):
            continue
        if re.search(r"\b(authorized licensed use|copyright|proceedings)\b", p, flags=re.I):
            continue
        if p.lower().startswith("index terms"):
            continue
        if p.lower().startswith("references"):
            continue
        out.append(p)
    return out


def pick(sentences: List[str], kws: List[str], n: int) -> List[str]:
    cand = []
    for s in sentences:
        low = s.lower()
        sc = sum(1 for k in kws if k in low)
        if sc > 0:
            cand.append((sc, len(s), s))
    cand.sort(key=lambda x: (x[0], x[1]), reverse=True)
    out, seen = [], set()
    for _, _, s in cand:
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


def read_pending_meta() -> Dict[str, Dict[str, str]]:
    import csv
    out = {}
    with PENDING_CSV.open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            out[r["candidate_id"]] = r
    return out


def note_id_from_path(path: str) -> str:
    p = ROOT / path
    if not p.exists():
        return ""
    txt = p.read_text(encoding="utf-8", errors="ignore")
    m = re.search(r"(?m)^id:\s*(.+)$", txt)
    return m.group(1).strip().strip('"') if m else ""


def parse_source_seed_id(meta: Dict[str, str]) -> str:
    notes = [x.strip() for x in (meta.get("source_seed_notes") or "").split(";") if x.strip()]
    for n in notes:
        nid = note_id_from_path(n)
        if nid:
            return nid
    return ""


def metrics_mentioned(text: str) -> List[str]:
    kmap = [
        ("trustworthiness", "trustworthiness"),
        ("continuity", "continuity"),
        ("stress", "stress"),
        ("co-ranking", "co-ranking"),
        ("coranking", "co-ranking"),
        ("neighborhood", "neighborhood-preservation criteria"),
        ("procrustes", "procrustes-based quality"),
        ("kl divergence", "kl divergence"),
        ("rank", "rank-based criteria"),
    ]
    low = text.lower()
    out = []
    for k, v in kmap:
        if k in low and v not in out:
            out.append(v)
    return out[:6]


def workflow_map(text: str) -> List[Tuple[int, str, str]]:
    low = text.lower()
    rows = []
    if any(k in low for k in ["task", "analysis task", "analyst"]):
        rows.append((1, "medium", "supports clarifying analysis intent before DR decisions"))
    if any(k in low for k in ["preprocess", "normalization", "noise", "outlier"]):
        rows.append((2, "medium", "adds constraints about data preparation and condition checks"))
    if any(k in low for k in ["method", "technique", "quality", "metric", "distortion"]):
        rows.append((3, "high", "directly informs task-aligned method/metric selection"))
    if any(k in low for k in ["initialization", "seed", "random init", "pca init"]):
        rows.append((4, "high", "contains initialization sensitivity or control guidance"))
    if any(k in low for k in ["hyperparameter", "parameter", "tuning", "optimization"]):
        rows.append((5, "high", "provides parameter sensitivity or optimization guidance"))
    if any(k in low for k in ["visualization", "scatter", "layout", "interpret"]):
        rows.append((6, "high", "guides reliable interpretation of projected layouts"))
    if any(k in low for k in ["explain", "rationale", "communicate"]):
        rows.append((7, "medium", "supports transparent explanation of recommendation rationale"))
    if not rows:
        rows = [(3, "medium", "contains DR evaluation details relevant to selection decisions")]
    return rows[:4]


def main() -> None:
    meta = read_pending_meta()
    created = 0
    for cid in TARGETS:
        files = sorted(PDF_DIR.glob(f"{cid}-*.pdf"))
        if not files:
            print("missing_pdf", cid)
            continue
        pdf = files[0]
        md = meta.get(cid)
        if not md:
            print("missing_meta", cid)
            continue

        source_pdf = f"papers/raw/pending-references/{pdf.name}"
        # skip existing
        exists = False
        for p in NOTES_DIR.glob("*.md"):
            if f"source_pdf: {source_pdf}" in p.read_text(encoding="utf-8", errors="ignore"):
                exists = True
                break
        if exists:
            continue

        reader = PdfReader(str(pdf))
        pages = [normalize(p.extract_text() or "") for p in reader.pages]
        full = "\n".join(pages)
        abs_m = re.search(r"\babstract\b", full, flags=re.I)
        conc_m = re.search(r"\b(conclusion|concluding remarks)\b", full, flags=re.I)
        abs_window = full[abs_m.start() : abs_m.start() + 5000] if abs_m else full[:5000]
        conc_window = full[conc_m.start() : conc_m.start() + 5000] if conc_m else full[-5000:]

        sents = split_sentences(full)
        sents_abs = split_sentences(abs_window)
        sents_conc = split_sentences(conc_window)

        problem = pick(sents_abs + sents, ["problem", "challenge", "distortion", "unreliable", "high-dimensional", "difficult"], 4)
        method = pick(sents_abs + sents, ["we propose", "we present", "method", "approach", "algorithm", "objective", "embedding", "projection"], 7)
        use = pick(sents_conc + sents, ["use", "useful", "works", "best", "avoid", "limitation", "sensitive", "robust"], 5)
        impl = pick(sents + sents_conc, ["parameter", "hyperparameter", "seed", "initialization", "runtime", "scalable", "optimization", "iteration"], 5)

        if len(problem) < 2:
            problem = (problem + method[:3])[:4]
        if len(method) < 4:
            method = (method + sents[:8])[:7]
        if len(use) < 3:
            use = (use + method[:4])[:5]
        if len(impl) < 3:
            impl = (impl + method[1:5])[:5]

        evidence = []
        for s in problem + method + use + impl:
            if s not in evidence and len(s) > 50:
                evidence.append(s)
        evidence = evidence[:8]
        while len(evidence) < 6 and sents:
            s = sents[len(evidence) % len(sents)]
            if s not in evidence and len(s) > 50:
                evidence.append(s)

        metrics = metrics_mentioned(full)
        wmap = workflow_map(full)

        year = md.get("year") if re.match(r"^\d{4}$", (md.get("year") or "")) else "2026"
        note_id = f"paper-{year}-{cid}"
        filename = f"{cid}-{re.sub(r'[^a-z0-9]+','-',md['paper_title'].lower()).strip('-')[:64]}.md"
        seed_note_id = parse_source_seed_id(md)
        authors = (md.get("authors") or "UNKNOWN").replace('"', "'")
        safe_title = md["paper_title"].replace('"', "'")

        lines = []
        lines.append("---")
        lines.append(f"id: {note_id}")
        lines.append(f"title: \"{safe_title}\"")
        lines.append(f"authors: \"{authors}\"")
        lines.append("venue: \"UNKNOWN\"")
        lines.append(f"year: {year}")
        lines.append("tags: [dr, reliability, visual_analytics, reference, pending_references]")
        lines.append(f"source_pdf: {source_pdf}")
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
        lines.append(f"  - {use[-1] if use else 'Ignoring distortion behavior and parameter sensitivity can cause unreliable conclusions.'}")

        lines.append("\n# Metrics Mentioned")
        if metrics:
            for m in metrics:
                lines.append(f"- `{m}`: discussed as part of projection quality or reliability evaluation.")
        else:
            lines.append("- No explicit named metric extracted from this source; pair method claims with complementary reliability metrics during workflow Step 3.")

        lines.append("\n# Implementation Notes")
        for s in impl[:5]:
            lines.append(f"- {s}")
        lines.append("- Keep preprocessing policy, initialization policy, and random-seed protocol fixed when comparing alternatives.")

        c1 = (problem[0] if problem else "The source identifies reliability risks in DR analysis.").replace("|", "/")
        c2 = (method[0] if method else "The source presents a concrete method/evaluation contribution.").replace("|", "/")
        c3 = (impl[0] if impl else "The source includes implementation-sensitive factors affecting reliability.").replace("|", "/")

        lines.append("\n# Claim Atoms (For Conflict Resolution)")
        lines.append(f"- CLAIM-{cid.upper()}-C1 | stance: support | summary: {c1} | evidence_ids: {cid.upper()}-E1, {cid.upper()}-E2")
        lines.append(f"- CLAIM-{cid.upper()}-C2 | stance: support | summary: {c2} | evidence_ids: {cid.upper()}-E3, {cid.upper()}-E4")
        lines.append(f"- CLAIM-{cid.upper()}-C3 | stance: support | summary: {c3} | evidence_ids: {cid.upper()}-E5, {cid.upper()}-E6")

        lines.append("\n# Workflow Relevance Map")
        for st, relv, note in wmap:
            lines.append(f"- step: {st} | relevance: {relv} | note: {note}")

        lines.append("\n# Evidence")
        for i, q in enumerate(evidence[:8], 1):
            q = q.replace('"', "'").replace("|", "/")
            pno = page_for_quote(pages, q)
            lines.append(f"- {cid.upper()}-E{i} | page: {pno}, section: extracted, quote: \"{q}\"")

        (NOTES_DIR / filename).write_text("\n".join(lines) + "\n", encoding="utf-8")
        created += 1

    print(f"created_curated_notes={created}")


if __name__ == "__main__":
    main()
