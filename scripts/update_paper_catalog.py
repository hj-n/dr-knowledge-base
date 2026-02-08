#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
from datetime import date
from pathlib import Path
from typing import Dict, List

ROOT = Path(__file__).resolve().parents[1]
NOTES_DIR = ROOT / "papers" / "notes"
GROUP_MAP_PATH = ROOT / "builder" / "evidence" / "reference-group-map.json"
OUT_CSV = ROOT / "docs" / "paper-catalog.csv"
OUT_JSON = ROOT / "builder" / "evidence" / "paper-catalog.json"


def parse_frontmatter(text: str) -> Dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    data: Dict[str, str] = {}
    for raw in text[4:end].splitlines():
        line = raw.strip()
        if not line or ":" not in line:
            continue
        key, val = line.split(":", 1)
        data[key.strip()] = val.strip().strip('"')
    return data


def load_group_map() -> Dict[str, str]:
    if not GROUP_MAP_PATH.exists():
        return {}
    try:
        payload = json.loads(GROUP_MAP_PATH.read_text(encoding="utf-8"))
        m = payload.get("reference_group_to_seed_note_id", {})
        if isinstance(m, dict):
            return {str(k): str(v) for k, v in m.items()}
    except Exception:
        pass
    return {}


def norm_source_path(source_pdf: str) -> str:
    return source_pdf.strip()


def classify_source(source_pdf: str):
    src = norm_source_path(source_pdf)
    is_pdf = src.lower().endswith(".pdf")
    is_local = src.startswith("papers/raw/")
    is_seed = False
    reference_group = ""

    if is_local:
        rel = src[len("papers/raw/") :]
        if "/" in rel:
            reference_group = rel.split("/", 1)[0]
            is_seed = False
        else:
            is_seed = True
            reference_group = ""

    return {
        "is_pdf": is_pdf,
        "is_local": is_local,
        "is_seed_paper": is_seed,
        "reference_group": reference_group,
    }


def main() -> int:
    group_map = load_group_map()
    notes: List[Dict[str, str]] = []

    for p in sorted(NOTES_DIR.glob("*.md")):
        if p.name == ".gitkeep":
            continue
        text = p.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        if not fm:
            continue
        notes.append(
            {
                "source_note": str(p.relative_to(ROOT)),
                "id": fm.get("id", ""),
                "paper_title": fm.get("title", p.stem),
                "authors": fm.get("authors", "UNKNOWN"),
                "venue": fm.get("venue", "UNKNOWN"),
                "year": str(fm.get("year", "")),
                "source_pdf": fm.get("source_pdf", ""),
                "evidence_level": fm.get("evidence_level", ""),
                "updated_at": fm.get("updated_at", ""),
                "seed_note_id": fm.get("seed_note_id", ""),
            }
        )

    id_to_note = {n["id"]: n["source_note"] for n in notes if n.get("id")}

    rows: List[Dict[str, str]] = []
    for n in notes:
        c = classify_source(n["source_pdf"])
        if not c["is_pdf"]:
            # Paper catalog is intentionally paper-only.
            continue

        parent_seed_note_id = n["seed_note_id"].strip()
        if (not c["is_seed_paper"]) and (not parent_seed_note_id) and c["reference_group"]:
            parent_seed_note_id = group_map.get(c["reference_group"], "")

        if c["is_seed_paper"]:
            parent_seed_source_note = n["source_note"]
        else:
            parent_seed_source_note = id_to_note.get(parent_seed_note_id, "")

        rows.append(
            {
                "source_note": n["source_note"],
                "paper_title": n["paper_title"],
                "authors": n["authors"],
                "venue": n["venue"],
                "year": n["year"],
                "source_pdf": n["source_pdf"],
                "is_seed_paper": "true" if c["is_seed_paper"] else "false",
                "reference_group": c["reference_group"],
                "parent_seed_note_id": parent_seed_note_id,
                "parent_seed_source_note": parent_seed_source_note,
                "evidence_level": n["evidence_level"],
                "updated_at": n["updated_at"],
            }
        )

    # Seed papers first, then references. Within each group: year desc, note path asc.
    def sort_key(r: Dict[str, str]):
        try:
            y = int(r["year"])
        except Exception:
            y = -1
        return (0 if r["is_seed_paper"] == "true" else 1, -y, r["source_note"])

    rows.sort(key=sort_key)

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "source_note",
        "paper_title",
        "authors",
        "venue",
        "year",
        "source_pdf",
        "is_seed_paper",
        "reference_group",
        "parent_seed_note_id",
        "parent_seed_source_note",
        "evidence_level",
        "updated_at",
    ]

    with OUT_CSV.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(
        json.dumps(
            {
                "updated_at": date.today().isoformat(),
                "paper_count": len(rows),
                "seed_count": sum(1 for r in rows if r["is_seed_paper"] == "true"),
                "reference_count": sum(1 for r in rows if r["is_seed_paper"] == "false"),
                "rows": rows,
            },
            indent=2,
            ensure_ascii=True,
        )
        + "\n",
        encoding="utf-8",
    )

    print(
        f"wrote {OUT_CSV.relative_to(ROOT)} and {OUT_JSON.relative_to(ROOT)} "
        f"(papers={len(rows)})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
