#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Dict, List, Set

ROOT = Path(__file__).resolve().parents[1]
NOTES_DIR = ROOT / "papers" / "notes"
METRICS_DIR = ROOT / "docs" / "metrics"
TECHNIQUES_DIR = ROOT / "docs" / "techniques"
CONFLICT_REGISTER = ROOT / "builder" / "evidence" / "conflict-register.md"
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
    tags: List[str]


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
        tags_raw = fm.get("tags", "")
        tags: List[str] = []
        if tags_raw.startswith("[") and tags_raw.endswith("]"):
            tags = [t.strip().strip('"').strip("'") for t in tags_raw[1:-1].split(",") if t.strip()]
        elif tags_raw:
            tags = [tags_raw.strip().strip('"').strip("'")]
        rel = str(p.relative_to(ROOT))
        out[rel] = NoteMeta(
            path=rel,
            title=fm.get("title", p.stem),
            year=str(fm.get("year", "")),
            source_pdf=fm.get("source_pdf", ""),
            evidence_level=fm.get("evidence_level", ""),
            tags=tags,
        )
    return out


def metric_tag_refs(note_meta: Dict[str, NoteMeta], metric_id: str) -> List[str]:
    refs = []
    for rel, meta in note_meta.items():
        if metric_id in meta.tags:
            refs.append(rel)
    return refs


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


def _slug(s: str) -> str:
    return re.sub(r"[^A-Z0-9]+", "_", s.upper()).strip("_")


def _claim_matches_entity(claim_id: str, entity_id: str) -> bool:
    c = f"_{_slug(claim_id)}_"
    e = _slug(entity_id)
    if not e:
        return False
    if f"_{e}_" in c:
        return True
    # handle known aliases
    aliases = {
        "T_SNE": ["TSNE"],
        "S_ISOMAP": ["SISOMAP"],
        "C_EVM": ["CEVM"],
        "CA_TNC": ["CATNC"],
        "L_TNC": ["LTNC"],
        "KL_DIV": ["KLDIV"],
        "NM_STRESS": ["NMSTRESS"],
        "SN_STRESS": ["SNSTRESS"],
        "SPECTRAL_OVERLAP": ["SPECTRALOVERLAP"],
        "RANDOM_PROJECTION": ["RP"],
    }
    for a in aliases.get(e, []):
        if f"_{a}_" in c:
            return True
    return False


def load_conflict_decisions() -> Dict[str, str]:
    if not CONFLICT_REGISTER.exists():
        return {}
    text = CONFLICT_REGISTER.read_text(encoding="utf-8")
    out: Dict[str, str] = {}
    for raw in text.splitlines():
        line = raw.strip()
        if not line.startswith("|"):
            continue
        if "claim_id" in line.lower():
            continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) < 9:
            continue
        claim_id = parts[1]
        decision = parts[7].lower()
        if not claim_id or claim_id == "---":
            continue
        if "contested" in decision:
            out[claim_id] = "contested"
        elif "accepted" in decision:
            out[claim_id] = "accepted"
        elif "insufficient" in decision:
            out[claim_id] = "insufficient"
        else:
            out[claim_id] = "unknown"
    return out


def entity_conflict_status(entity_id: str, conflict_decisions: Dict[str, str]) -> str:
    matches = []
    for claim_id, status in conflict_decisions.items():
        if _claim_matches_entity(claim_id, entity_id):
            matches.append(status)
    if not matches:
        return "unknown"
    if "contested" in matches:
        return "contested"
    if "insufficient" in matches:
        return "insufficient"
    if "accepted" in matches:
        return "accepted"
    return "unknown"


def build_index(
    folder: Path,
    note_meta: Dict[str, NoteMeta],
    kind: str,
    conflict_decisions: Dict[str, str],
) -> List[Dict]:
    rows = []
    for p in sorted(folder.glob("*.md")):
        if p.name.lower() in {"readme.md", "metric-relationships.md"}:
            continue
        entity_id = p.stem
        refs = parse_source_notes(p)
        if kind == "metric" and not refs:
            refs = metric_tag_refs(note_meta, entity_id)
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
                "conflict_status": entity_conflict_status(entity_id, conflict_decisions),
            }
        )

    def rank_pdf_count(row: Dict) -> int:
        c = int(row["source_pdf_count"])
        # Contested entities are down-ranked by one tier-equivalent count.
        if row.get("conflict_status") == "contested" and c > 0:
            return c - 1
        return c

    rows.sort(
        key=lambda x: (
            -rank_pdf_count(x),
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
    lines.append("| Metric | PDF Count | PDF Note Count | Total Note Count | Support Tier | Conflict Status |")
    lines.append("|---|---:|---:|---:|---|---|")
    for r in metrics:
        lines.append(
            f"| `{r['id']}` | {r['source_pdf_count']} | {r['source_pdf_note_count']} | {r['source_note_count']} | `{r['support_tier']}` | `{r['conflict_status']}` |"
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
    lines.append("| Technique | PDF Count | PDF Note Count | Total Note Count | Support Tier | Conflict Status |")
    lines.append("|---|---:|---:|---:|---|---|")
    for r in techniques:
        lines.append(
            f"| `{r['id']}` | {r['source_pdf_count']} | {r['source_pdf_note_count']} | {r['source_note_count']} | `{r['support_tier']}` | `{r['conflict_status']}` |"
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
    lines.append("- Task categories and subtasks: [`docs/task-taxonomy.md`](./task-taxonomy.md)")
    lines.append("- Selection policy: [`docs/metrics-and-libraries.md`](./metrics-and-libraries.md)")
    lines.append("- Grouped reliability cautions: [`docs/reliability-cautions-and-tips.md`](./reliability-cautions-and-tips.md)")
    lines.append("- Metric catalog: [`docs/metrics/README.md`](./metrics/README.md)")
    lines.append("- Technique catalog: [`docs/techniques/README.md`](./techniques/README.md)")
    lines.append("- Paper catalog: [`docs/paper-catalog.md`](./paper-catalog.md)")
    lines.append("")
    lines.append(f"Updated at: `{today}`")
    lines.append("")
    lines.append("Priority rule:")
    lines.append("1. Filter by task alignment first.")
    lines.append("2. Apply label-separation checks before class-aware interpretation.")
    lines.append("3. Prefer higher `PDF Count` among remaining candidates.")
    lines.append("4. Down-rank candidates with `contested` conflict status by one tier.")
    lines.append("5. If tied, inspect source-note list and choose the better-justified option.")
    lines.append("")
    lines.append("Support tier by distinct PDF count: `very_high` >= 6, `high` 4-5, `medium` 2-3, `low` 1, `none` 0.")
    lines.append("")

    lines.append("## Metrics Ranking")
    lines.append("")
    lines.append("| Rank | Metric | PDF Count | Support Tier | Conflict Status |")
    lines.append("|---:|---|---:|---|---|")
    for i, r in enumerate(metrics, start=1):
        lines.append(
            f"| {i} | `{r['id']}` | {r['source_pdf_count']} | `{r['support_tier']}` | `{r['conflict_status']}` |"
        )
    lines.append("")

    lines.append("## Technique Ranking")
    lines.append("")
    lines.append("| Rank | Technique | PDF Count | Support Tier | Conflict Status |")
    lines.append("|---:|---|---:|---|---|")
    for i, r in enumerate(techniques, start=1):
        lines.append(
            f"| {i} | `{r['id']}` | {r['source_pdf_count']} | `{r['support_tier']}` | `{r['conflict_status']}` |"
        )
    lines.append("")

    lines.append("## Metric Source Map")
    lines.append("")
    lines.append("Each item below shows where the metric is mentioned.")
    lines.append("")
    for r in metrics:
        lines.append(
            f"### `{r['id']}` (`{r['source_pdf_count']}` PDFs, conflict: `{r['conflict_status']}`)"
        )
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
        lines.append(
            f"### `{r['id']}` (`{r['source_pdf_count']}` PDFs, conflict: `{r['conflict_status']}`)"
        )
        if r["source_pdf_notes"]:
            for n in r["source_pdf_notes"]:
                lines.append(f"- `{n['note_path']}`")
        else:
            lines.append("- No PDF-backed source note linked.")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    note_meta = load_note_meta()
    conflict_decisions = load_conflict_decisions()
    metrics = build_index(METRICS_DIR, note_meta, "metric", conflict_decisions)
    techniques = build_index(TECHNIQUES_DIR, note_meta, "technique", conflict_decisions)

    payload = {
        "updated_at": date.today().isoformat(),
        "source": "docs/*/Source Notes",
        "conflict_source": str(CONFLICT_REGISTER.relative_to(ROOT)),
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
