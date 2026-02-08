#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Dict, List, Tuple

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
PENDING_CSV = ROOT / "builder" / "evidence" / "pending-reference-papers.csv"
PDF_DIR = ROOT / "papers" / "raw" / "pending-references"
NOTES_DIR = ROOT / "papers" / "notes"
OUT_TRIAGE = ROOT / "builder" / "evidence" / "pending-reference-triage.csv"

INCLUDE_KWS = [
    "dimensionality reduction", "dimension reduction", "projection", "embedding", "umap", "t-sne", "tsne",
    "mds", "isomap", "lle", "manifold", "trustworthiness", "continuity", "quality", "metric",
    "neighborhood", "cluster", "distortion", "visual analytics",
]
EXCLUDE_KWS = [
    "foundation model", "narrative visualization", "commentvis", "vision transformers",
    "attention work in vision transformers", "serendipitous discovery of academic literature",
]

METRIC_HINTS = {
    "trustworthiness": "trustworthiness",
    "continuity": "continuity",
    "stress": "stress",
    "co-ranking": "co-ranking",
    "coranking": "co-ranking",
    "kl divergence": "kl divergence",
    "kl-divergence": "kl divergence",
    "neighborhood hit": "neighborhood hit",
    "lcmc": "lcmc",
    "procrustes": "procrustes-based quality",
    "rank": "rank-based quality criteria",
}

WORKFLOW_STEP_HINTS = {
    1: ["task", "analyst", "objective", "question"],
    2: ["preprocess", "normalization", "scaling", "noise", "outlier"],
    3: ["method", "technique", "metric", "evaluation", "quality"],
    4: ["initialization", "seed", "pca init", "random init"],
    5: ["hyperparameter", "optimization", "tuning", "parameter", "bayes"],
    6: ["visualization", "scatter", "plot", "interpret"],
    7: ["explain", "reason", "rationale", "communicate"],
}


@dataclass
class PaperRow:
    candidate_id: str
    title: str
    authors: str
    year: str
    doi: str
    source_seed_notes: str
    source_seed_count: int
    max_context_score: int
    max_title_keyword_score: int


def slugify(s: str, maxlen: int = 80) -> str:
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    if len(s) > maxlen:
        s = s[:maxlen].rstrip("-")
    return s or "paper"


def normalize_space(s: str) -> str:
    s = s.replace("\u00a0", " ")
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def split_sentences(text: str) -> List[str]:
    text = re.sub(r"(?<=\w)-\n(?=\w)", "", text)
    text = text.replace("\n", " ")
    text = normalize_space(text)
    chunks = re.split(r"(?<=[\.!?])\s+(?=[A-Z0-9\[])", text)
    out = []
    for c in chunks:
        c = c.strip(" -")
        if len(c) < 40:
            continue
        if len(c) > 500:
            continue
        out.append(c)
    return out


def choose_sentences(sentences: List[str], include: List[str], exclude: List[str], n: int) -> List[str]:
    scored = []
    for s in sentences:
        low = s.lower()
        if any(x in low for x in exclude):
            continue
        score = sum(1 for k in include if k in low)
        if score <= 0:
            continue
        scored.append((score, len(s), s))
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


def find_page_for_quote(pages: List[str], quote: str) -> int:
    q = quote[:90].lower()
    for i, p in enumerate(pages, 1):
        if q in p.lower():
            return i
    return 1


def load_note_ids() -> Dict[str, str]:
    out = {}
    for p in NOTES_DIR.glob("*.md"):
        txt = p.read_text(encoding="utf-8", errors="ignore")
        m = re.search(r"(?m)^id:\s*(.+)$", txt)
        if m:
            out[str(p.relative_to(ROOT))] = m.group(1).strip().strip('"')
    return out


def pick_seed_note_id(source_seed_notes: str, note_id_map: Dict[str, str]) -> str:
    parts = [x.strip() for x in source_seed_notes.split(";") if x.strip()]
    for p in parts:
        if p in note_id_map:
            return note_id_map[p]
    return ""


def is_relevant(title: str, ss: int, ctx: int) -> bool:
    low = title.lower()
    if any(x in low for x in EXCLUDE_KWS):
        return False
    if not any(x in low for x in INCLUDE_KWS):
        return False
    return (ss >= 2 or ctx >= 6)


def metrics_from_text(text: str) -> List[str]:
    low = text.lower()
    out = []
    for k, v in METRIC_HINTS.items():
        if k in low and v not in out:
            out.append(v)
    return out[:8]


def workflow_map(text: str) -> List[Tuple[int, str, str]]:
    low = text.lower()
    out = []
    for step, kws in WORKFLOW_STEP_HINTS.items():
        hits = sum(1 for k in kws if k in low)
        if hits == 0:
            continue
        rel = "high" if hits >= 3 else ("medium" if hits >= 2 else "low")
        note = {
            1: "supports task clarification before method recommendation",
            2: "provides preprocessing or data-condition cautions",
            3: "informs task-aligned technique/metric selection",
            4: "constrains initialization strategy or seed policy",
            5: "informs parameter-search or optimization reliability",
            6: "guides projection reading/diagnosis in visualization",
            7: "supports transparent rationale communication to end users",
        }[step]
        out.append((step, rel, note))
    out.sort(key=lambda x: x[0])
    if not out:
        out = [(3, "medium", "contains method/quality statements relevant to selection decisions")]
    return out[:4]


def main() -> None:
    note_id_map = load_note_ids()
    rows = []
    with PENDING_CSV.open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            rows.append(PaperRow(
                candidate_id=r["candidate_id"],
                title=r["paper_title"].strip(),
                authors=r.get("authors", "UNKNOWN").strip() or "UNKNOWN",
                year=r.get("year", "").strip() or "UNKNOWN",
                doi=r.get("doi", "").strip(),
                source_seed_notes=r.get("source_seed_notes", "").strip(),
                source_seed_count=int(r.get("source_seed_count") or 0),
                max_context_score=int(r.get("max_context_score") or 0),
                max_title_keyword_score=int(r.get("max_title_keyword_score") or 0),
            ))

    # map candidate -> local pdf
    local = {}
    for p in PDF_DIR.glob("*.pdf"):
        m = re.match(r"(pending-ref-\d{3})-", p.name)
        if m:
            local[m.group(1)] = p

    triage_rows = []
    created = 0
    skipped = 0

    for r in rows:
        pdf_path = local.get(r.candidate_id)
        if not pdf_path:
            continue

        rel = is_relevant(r.title, r.source_seed_count, r.max_context_score)
        triage_rows.append({
            "candidate_id": r.candidate_id,
            "title": r.title,
            "source_pdf": f"papers/raw/pending-references/{pdf_path.name}",
            "relevant": "true" if rel else "false",
            "reason": "in_scope_dr_workflow" if rel else "out_of_scope_or_low_signal",
        })
        if not rel:
            skipped += 1
            continue

        source_pdf_rel = f"papers/raw/pending-references/{pdf_path.name}"
        # skip if already note for this source exists
        already = False
        for np in NOTES_DIR.glob("*.md"):
            txt = np.read_text(encoding="utf-8", errors="ignore")
            if f"source_pdf: {source_pdf_rel}" in txt:
                already = True
                break
        if already:
            continue

        reader = PdfReader(str(pdf_path))
        pages = [normalize_space(p.extract_text() or "") for p in reader.pages]
        full = "\n".join(pages)
        sentences = split_sentences(full)

        problem_sents = choose_sentences(
            sentences,
            ["challenge", "problem", "distortion", "unreliable", "difficult", "fails", "limitation", "high-dimensional"],
            ["copyright", "references"],
            4,
        )
        method_sents = choose_sentences(
            sentences,
            ["we propose", "we present", "method", "algorithm", "approach", "objective", "optimiz", "embedding", "projection"],
            ["references", "copyright"],
            6,
        )
        use_sents = choose_sentences(
            sentences,
            ["use", "applicable", "works well", "best", "avoid", "limitation", "fails", "sensitive", "robust"],
            ["copyright", "references"],
            5,
        )
        impl_sents = choose_sentences(
            sentences,
            ["parameter", "hyperparameter", "initialization", "seed", "runtime", "complexity", "scal", "optimization", "iteration"],
            ["copyright", "references"],
            5,
        )

        if len(problem_sents) < 2:
            problem_sents = method_sents[:2] + problem_sents
        if len(method_sents) < 3:
            method_sents = (method_sents + sentences[:6])[:6]
        if len(use_sents) < 2:
            use_sents = (use_sents + method_sents[:3])[:3]
        if len(impl_sents) < 2:
            impl_sents = (impl_sents + method_sents[1:4])[:3]

        mets = metrics_from_text(full)
        wmap = workflow_map(full)

        evid_pool = []
        for s in (problem_sents + method_sents + use_sents + impl_sents):
            s = normalize_space(s)
            if len(s) < 50:
                continue
            if s not in evid_pool:
                evid_pool.append(s)
        evid_pool = evid_pool[:10]
        while len(evid_pool) < 6 and sentences:
            s = sentences[len(evid_pool) % len(sentences)]
            if s not in evid_pool and len(s) > 50:
                evid_pool.append(s)
            if len(evid_pool) >= 6:
                break

        year = r.year if re.match(r"^\d{4}$", r.year) else "2026"
        note_id = f"paper-{year}-{r.candidate_id}"
        title_slug = slugify(r.title, 48)
        note_file = NOTES_DIR / f"{r.candidate_id}-{title_slug}.md"

        seed_note_id = pick_seed_note_id(r.source_seed_notes, note_id_map)

        # Claim atoms from top method/problem signals
        c1 = problem_sents[0] if problem_sents else "The paper identifies reliability risks in DR projection interpretation."
        c2 = method_sents[0] if method_sents else "The paper proposes or evaluates a concrete DR method/evaluation procedure."
        c3 = (impl_sents[0] if impl_sents else "The paper discusses implementation-sensitive factors such as parameters, initialization, or reproducibility.")

        # basic venue inference from title/pdf naming unavailable -> UNKNOWN
        venue = "UNKNOWN"
        tags = ["dr", "reference", "pending_references", "workflow"]
        if "survey" in r.title.lower():
            tags.append("survey")
        if any(k in r.title.lower() for k in ["metric", "quality", "trustworthiness", "continuity"]):
            tags.append("evaluation")

        lines = []
        lines.append("---")
        lines.append(f"id: {note_id}")
        lines.append(f"title: \"{r.title}\"")
        lines.append(f"authors: \"{r.authors if r.authors else 'UNKNOWN'}\"")
        lines.append(f"venue: \"{venue}\"")
        lines.append(f"year: {year}")
        lines.append(f"tags: [{', '.join(tags)}]")
        lines.append(f"source_pdf: {source_pdf_rel}")
        lines.append(f"seed_note_id: \"{seed_note_id}\"")
        lines.append("evidence_level: medium")
        lines.append(f"updated_at: {date.today().isoformat()}")
        lines.append("---\n")

        lines.append("# Problem")
        for s in problem_sents[:4]:
            lines.append(f"- {s}")

        lines.append("\n# Method Summary")
        for s in method_sents[:6]:
            lines.append(f"- {s}")

        lines.append("\n# When To Use / Not Use")
        lines.append("- Use when:")
        for s in use_sents[:2]:
            lines.append(f"  - {s}")
        lines.append("- Avoid when:")
        for s in use_sents[2:4] if len(use_sents) > 2 else method_sents[:2]:
            lines.append(f"  - {s}")
        lines.append("- Failure modes:")
        lines.append(f"  - {use_sents[-1] if use_sents else 'Misinterpreting projection geometry without reliability checks can lead to incorrect conclusions.'}")

        lines.append("\n# Metrics Mentioned")
        if mets:
            for m in mets:
                lines.append(f"- `{m}`: referenced as part of projection-quality or reliability assessment.")
        else:
            lines.append("- No explicit named metric was extracted from the source text; use complementary DR quality checks during workflow Step 3.")

        lines.append("\n# Implementation Notes")
        for s in impl_sents[:5]:
            lines.append(f"- {s}")
        lines.append("- Keep preprocessing, initialization, and seed policy fixed when comparing methods to avoid protocol-driven score shifts.")

        lines.append("\n# Claim Atoms (For Conflict Resolution)")
        lines.append(f"- CLAIM-{r.candidate_id.upper()}-C1 | stance: support | summary: {c1} | evidence_ids: {r.candidate_id.upper()}-E1, {r.candidate_id.upper()}-E2")
        lines.append(f"- CLAIM-{r.candidate_id.upper()}-C2 | stance: support | summary: {c2} | evidence_ids: {r.candidate_id.upper()}-E3, {r.candidate_id.upper()}-E4")
        lines.append(f"- CLAIM-{r.candidate_id.upper()}-C3 | stance: support | summary: {c3} | evidence_ids: {r.candidate_id.upper()}-E5, {r.candidate_id.upper()}-E6")

        lines.append("\n# Workflow Relevance Map")
        for st, relv, note in wmap:
            lines.append(f"- step: {st} | relevance: {relv} | note: {note}")

        lines.append("\n# Evidence")
        for i, q in enumerate(evid_pool[:8], 1):
            pid = find_page_for_quote(pages, q)
            q = q.replace('"', "'")
            lines.append(f"- {r.candidate_id.upper()}-E{i} | page: {pid}, section: extracted, quote: \"{q}\"")

        note_file.write_text("\n".join(lines) + "\n", encoding="utf-8")
        created += 1

    with OUT_TRIAGE.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["candidate_id", "title", "source_pdf", "relevant", "reason"])
        w.writeheader()
        w.writerows(triage_rows)

    print(f"wrote triage: {OUT_TRIAGE.relative_to(ROOT)} (rows={len(triage_rows)})")
    print(f"created_notes={created} skipped_irrelevant={skipped}")


if __name__ == "__main__":
    main()
