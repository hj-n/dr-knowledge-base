#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Dict, List

ROOT = Path(__file__).resolve().parents[1]
NOTES_DIR = ROOT / "papers" / "notes"
METRICS_DIR = ROOT / "docs" / "metrics"
TECHNIQUES_DIR = ROOT / "docs" / "techniques"
OUT_JSON = ROOT / "builder" / "evidence" / "reference-coverage.json"
OUT_MD = ROOT / "builder" / "evidence" / "reference-coverage.md"
OUT_DOCS_MD = ROOT / "docs" / "reference-coverage.md"

SOURCE_LINE_RE = re.compile(r"`(papers/notes/[^`]+\.md)`")


@dataclass
class NoteMeta:
    path: str
    title: str
    year: str
    source_pdf: str
    evidence_level: str


def parse_frontmatter(text: str) -> Dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    fm = text[4:end]
    data: Dict[str, str] = {}
    for raw in fm.splitlines():
        line = raw.strip()
        if not line or ":" not in line:
            continue
        key, val = line.split(":", 1)
        key = key.strip()
        val = val.strip().strip('"')
        data[key] = val
    return data


def load_note_meta() -> Dict[str, NoteMeta]:
    out: Dict[str, NoteMeta] = {}
    for p in sorted(NOTES_DIR.glob("*.md")):
        text = p.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        rel = str(p.relative_to(ROOT))
        out[rel] = NoteMeta(
            path=rel,
            title=fm.get("title", p.stem),
            year=str(fm.get("year", "")),
            source_pdf=fm.get("source_pdf", ""),
            evidence_level=fm.get("evidence_level", ""),
        )
    return out


def parse_source_notes(doc_path: Path) -> List[str]:
    text = doc_path.read_text(encoding="utf-8")
    marker = "\n## Source Notes\n"
    idx = text.find(marker)
    if idx == -1:
        return []
    tail = text[idx + len(marker) :]
    # Collect all note references until end of file.
    refs = SOURCE_LINE_RE.findall(tail)
    seen = set()
    ordered = []
    for r in refs:
        if r not in seen:
            seen.add(r)
            ordered.append(r)
    return ordered


def support_tier(count: int) -> str:
    if count >= 6:
        return "very_high"
    if count >= 4:
        return "high"
    if count >= 2:
        return "medium"
    if count >= 1:
        return "low"
    return "none"


def build_index(folder: Path, note_meta: Dict[str, NoteMeta], kind: str) -> List[Dict]:
    rows = []
    for p in sorted(folder.glob("*.md")):
        if p.name.lower() == "readme.md":
            continue
        entity_id = p.stem
        refs = parse_source_notes(p)
        notes = []
        pdf_notes = []
        non_pdf_notes = []
        pdfs = []
        unresolved = []
        for ref in refs:
            meta = note_meta.get(ref)
            if meta is None:
                unresolved.append(ref)
                continue
            note_obj = {
                "note_path": meta.path,
                "title": meta.title,
                "year": meta.year,
                "source_pdf": meta.source_pdf,
                "evidence_level": meta.evidence_level,
            }
            notes.append(note_obj)

            src = (meta.source_pdf or "").strip()
            is_pdf_source = src.lower().endswith(".pdf")
            if is_pdf_source:
                pdf_notes.append(note_obj)
                if src not in pdfs:
                    pdfs.append(src)
            else:
                non_pdf_notes.append(note_obj)

        rows.append(
            {
                "id": entity_id,
                "kind": kind,
                "doc_path": str(p.relative_to(ROOT)),
                "source_note_count": len(notes),
                "source_pdf_note_count": len(pdf_notes),
                "non_pdf_note_count": len(non_pdf_notes),
                "source_pdf_count": len(pdfs),
                "support_tier": support_tier(len(pdfs)),
                "source_notes": notes,
                "source_pdf_notes": pdf_notes,
                "non_pdf_notes": non_pdf_notes,
                "source_pdfs": pdfs,
                "unresolved_note_refs": unresolved,
            }
        )

    rows.sort(
        key=lambda x: (
            -x["source_pdf_count"],
            -x["source_pdf_note_count"],
            -x["source_note_count"],
            x["id"],
        )
    )
    return rows


def to_markdown(metrics: List[Dict], techniques: List[Dict]) -> str:
    lines: List[str] = []
    today = date.today().isoformat()
    lines.append("# Reference Coverage Index")
    lines.append("")
    lines.append("This file tracks how many reference PDFs mention each metric and technique, using the `Source Notes` links in docs.")
    lines.append("Use this index for recommendation priority after task alignment and warning-gate checks.")
    lines.append("")
    lines.append(f"Updated at: `{today}`")
    lines.append("")
    lines.append("Support-tier rule (by distinct source PDFs): `very_high` >= 6, `high` 4-5, `medium` 2-3, `low` 1, `none` 0.")
    lines.append("Only PDF-backed notes contribute to support-tier and ranking counts.")
    lines.append("")

    lines.append("## Metrics Coverage")
    lines.append("")
    lines.append("| Metric | PDF Count | PDF Note Count | Total Note Count | Support Tier |")
    lines.append("|---|---:|---:|---:|---|")
    for r in metrics:
        lines.append(
            f"| `{r['id']}` | {r['source_pdf_count']} | {r['source_pdf_note_count']} | {r['source_note_count']} | `{r['support_tier']}` |"
        )
    lines.append("")

    for r in metrics:
        lines.append(f"### `{r['id']}` Sources")
        if r["source_notes"]:
            for n in r["source_notes"]:
                note = n["note_path"]
                pdf = n["source_pdf"] or "unknown"
                lvl = n["evidence_level"] or "unknown"
                lines.append(f"- `{note}` -> `{pdf}` (evidence_level: `{lvl}`)")
        else:
            lines.append("- No linked source notes.")
        if r["unresolved_note_refs"]:
            lines.append("- Unresolved references:")
            for u in r["unresolved_note_refs"]:
                lines.append(f"  - `{u}`")
        if r["non_pdf_notes"]:
            lines.append("- Non-PDF support notes (excluded from PDF count):")
            for n in r["non_pdf_notes"]:
                lines.append(f"  - `{n['note_path']}` -> `{n['source_pdf'] or 'unknown'}`")
        lines.append("")

    lines.append("## Techniques Coverage")
    lines.append("")
    lines.append("| Technique | PDF Count | PDF Note Count | Total Note Count | Support Tier |")
    lines.append("|---|---:|---:|---:|---|")
    for r in techniques:
        lines.append(
            f"| `{r['id']}` | {r['source_pdf_count']} | {r['source_pdf_note_count']} | {r['source_note_count']} | `{r['support_tier']}` |"
        )
    lines.append("")

    for r in techniques:
        lines.append(f"### `{r['id']}` Sources")
        if r["source_notes"]:
            for n in r["source_notes"]:
                note = n["note_path"]
                pdf = n["source_pdf"] or "unknown"
                lvl = n["evidence_level"] or "unknown"
                lines.append(f"- `{note}` -> `{pdf}` (evidence_level: `{lvl}`)")
        else:
            lines.append("- No linked source notes.")
        if r["unresolved_note_refs"]:
            lines.append("- Unresolved references:")
            for u in r["unresolved_note_refs"]:
                lines.append(f"  - `{u}`")
        if r["non_pdf_notes"]:
            lines.append("- Non-PDF support notes (excluded from PDF count):")
            for n in r["non_pdf_notes"]:
                lines.append(f"  - `{n['note_path']}` -> `{n['source_pdf'] or 'unknown'}`")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def to_docs_markdown(metrics: List[Dict], techniques: List[Dict]) -> str:
    lines: List[str] = []
    today = date.today().isoformat()
    lines.append("# Reference Coverage")
    lines.append("")
    lines.append("This user-facing page summarizes how frequently metrics and techniques are supported by reference PDFs.")
    lines.append("Use this for priority ranking when multiple candidates are already task-aligned.")
    lines.append("")
    lines.append("Related:")
    lines.append("- Overview: [`docs/overview.md`](./overview.md)")
    lines.append("- Workflow: [`docs/workflow/dr-analysis-workflow.md`](./workflow/dr-analysis-workflow.md)")
    lines.append("- Selection policy: [`docs/metrics-and-libraries.md`](./metrics-and-libraries.md)")
    lines.append("- Metric catalog: [`docs/metrics/README.md`](./metrics/README.md)")
    lines.append("- Technique catalog: [`docs/techniques/README.md`](./techniques/README.md)")
    lines.append("")
    lines.append(f"Updated at: `{today}`")
    lines.append("")
    lines.append("Priority rule:")
    lines.append("1. Filter by task alignment first.")
    lines.append("2. Apply warning gates (for example, label-separation-sensitive metrics).")
    lines.append("3. Prefer higher `PDF Count` among remaining candidates.")
    lines.append("4. If tied, inspect source-note list and choose the better-justified option.")
    lines.append("")
    lines.append("Support tier by distinct PDF count: `very_high` >= 6, `high` 4-5, `medium` 2-3, `low` 1, `none` 0.")
    lines.append("")

    lines.append("## Metrics Ranking")
    lines.append("")
    lines.append("| Rank | Metric | PDF Count | Support Tier |")
    lines.append("|---:|---|---:|---|")
    for i, r in enumerate(metrics, start=1):
        lines.append(f"| {i} | `{r['id']}` | {r['source_pdf_count']} | `{r['support_tier']}` |")
    lines.append("")

    lines.append("## Technique Ranking")
    lines.append("")
    lines.append("| Rank | Technique | PDF Count | Support Tier |")
    lines.append("|---:|---|---:|---|")
    for i, r in enumerate(techniques, start=1):
        lines.append(f"| {i} | `{r['id']}` | {r['source_pdf_count']} | `{r['support_tier']}` |")
    lines.append("")

    lines.append("## Metric Source Map")
    lines.append("")
    lines.append("Each item below shows where the metric is mentioned.")
    lines.append("")
    for r in metrics:
        lines.append(f"### `{r['id']}` (`{r['source_pdf_count']}` PDFs)")
        if r["source_pdf_notes"]:
            for n in r["source_pdf_notes"]:
                lines.append(f"- `{n['note_path']}`")
        else:
            lines.append("- No PDF-backed source note linked.")
        lines.append("")

    lines.append("## Technique Source Map")
    lines.append("")
    lines.append("Each item below shows where the technique is mentioned.")
    lines.append("")
    for r in techniques:
        lines.append(f"### `{r['id']}` (`{r['source_pdf_count']}` PDFs)")
        if r["source_pdf_notes"]:
            for n in r["source_pdf_notes"]:
                lines.append(f"- `{n['note_path']}`")
        else:
            lines.append("- No PDF-backed source note linked.")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    note_meta = load_note_meta()
    metrics = build_index(METRICS_DIR, note_meta, "metric")
    techniques = build_index(TECHNIQUES_DIR, note_meta, "technique")

    payload = {
        "updated_at": date.today().isoformat(),
        "source": "docs/*/Source Notes",
        "support_tier_rule": {
            "very_high": ">=6 PDFs",
            "high": "4-5 PDFs",
            "medium": "2-3 PDFs",
            "low": "1 PDF",
            "none": "0 PDFs",
        },
        "metrics": metrics,
        "techniques": techniques,
    }

    OUT_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(to_markdown(metrics, techniques), encoding="utf-8")
    OUT_DOCS_MD.write_text(to_docs_markdown(metrics, techniques), encoding="utf-8")
    print(
        "wrote "
        f"{OUT_JSON.relative_to(ROOT)}, "
        f"{OUT_MD.relative_to(ROOT)}, and "
        f"{OUT_DOCS_MD.relative_to(ROOT)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
