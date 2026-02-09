#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
from collections import defaultdict
from pathlib import Path
from typing import Dict, Tuple

ROOT = Path(__file__).resolve().parents[1]
DETAIL = ROOT / "builder" / "evidence" / "note-pdf-grounding.csv"
NOTES = ROOT / "papers" / "notes"

LINE_RE = re.compile(r'^(-\s+)(?P<eid>[A-Z0-9\-]+)(\s+\|\s+page:\s*)(?P<page>[^,]+)(,\s*section:.*)$')


def main() -> int:
    rows = list(csv.DictReader(DETAIL.open(encoding="utf-8")))

    # note -> evidence_id -> (new_page, mode)
    updates: Dict[str, Dict[str, Tuple[str, str]]] = defaultdict(dict)

    for r in rows:
        st = r["status"]
        if st not in {"exact_other_page", "fuzzy_other_page"}:
            continue
        note = r["note"]
        eid = r["evidence_id"]
        matched = (r.get("matched_pages") or "").split(";")
        matched = [m.strip() for m in matched if m.strip()]
        if not matched:
            continue

        # prefer exact match page when available
        new_page = matched[0]
        prev = updates[note].get(eid)
        if prev is None:
            updates[note][eid] = (new_page, st)
        else:
            # keep exact over fuzzy
            if prev[1] == "fuzzy_other_page" and st == "exact_other_page":
                updates[note][eid] = (new_page, st)

    changed_notes = 0
    changed_lines = 0

    for note_rel, mp in updates.items():
        note_path = ROOT / note_rel
        if not note_path.exists():
            continue
        lines = note_path.read_text(encoding="utf-8", errors="ignore").splitlines()
        touched = False

        for i, line in enumerate(lines):
            m = LINE_RE.match(line)
            if not m:
                continue
            eid = m.group("eid")
            if eid not in mp:
                continue
            new_page, _ = mp[eid]
            old_page = m.group("page").strip()
            if old_page == new_page:
                continue
            lines[i] = f"{m.group(1)}{eid}{m.group(3)}{new_page}{m.group(5)}"
            touched = True
            changed_lines += 1

        if touched:
            note_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
            changed_notes += 1

    print(f"updated_notes={changed_notes} updated_evidence_lines={changed_lines}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
