#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path
from typing import Dict, List

ROOT = Path(__file__).resolve().parents[1]
NOTES = ROOT / "papers" / "notes"

KNOWN_METRICS = {
    "tnc",
    "mrre",
    "lcmc",
    "nh",
    "ca_tnc",
    "l_tnc",
    "nd",
    "dtm",
    "kl_div",
    "dsc",
    "pr",
    "srho",
    "ivm",
    "c_evm",
    "snc",
    "topo",
    "proc",
    "stress",
    "sn_stress",
    "nm_stress",
    "qnx",
    "spectral_overlap",
}

CLAIM_HEADER = "# Claim Atoms (For Conflict Resolution)"
WORKFLOW_HEADER = "# Workflow Relevance Map"


def parse_frontmatter(text: str) -> Dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    fm = {}
    for line in text[4:end].splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        fm[k.strip()] = v.strip()
    return fm


def parse_tags(tag_str: str) -> List[str]:
    # expected format: [a, b, c]
    s = tag_str.strip()
    if s.startswith("[") and s.endswith("]"):
        s = s[1:-1]
    parts = [p.strip().strip('"').strip("'") for p in s.split(",") if p.strip()]
    return parts


def extract_evidence_ids(text: str) -> List[str]:
    return re.findall(r"^-\s+([A-Z0-9\-]+)\s+\|\s+page:", text, flags=re.M)


def add_aliases(note: Path) -> int:
    text = note.read_text(encoding="utf-8", errors="ignore")
    fm = parse_frontmatter(text)

    m = re.search(r"zadu-ref-(\d{2})", note.name)
    if not m:
        return 0
    sid = m.group(1)

    tags = set(parse_tags(fm.get("tags", "")))
    metrics = sorted(m for m in tags if m in KNOWN_METRICS)
    if not metrics:
        return 0

    claim_start = text.find(CLAIM_HEADER)
    wf_start = text.find(WORKFLOW_HEADER)
    if claim_start == -1 or wf_start == -1 or wf_start <= claim_start:
        return 0

    claim_block = text[claim_start:wf_start]
    evidence_ids = extract_evidence_ids(text)
    ev = ", ".join(evidence_ids[:2]) if len(evidence_ids) >= 2 else (evidence_ids[0] if evidence_ids else "")
    if not ev:
        ev = f"ZR{sid}-E1"

    to_add = []
    for metric in metrics:
        token = metric.upper()
        claim_id = f"CLAIM-METRIC-{token}-SOURCE-{sid}"
        if claim_id in claim_block:
            continue
        summary = f"This source includes evidence relevant to `{metric}` in dimensionality-reduction reliability evaluation."
        to_add.append(f"- {claim_id} | stance: support | summary: {summary} | evidence_ids: {ev}")

    if not to_add:
        return 0

    new_claim_block = claim_block.rstrip() + "\n" + "\n".join(to_add) + "\n\n"
    new_text = text[:claim_start] + new_claim_block + text[wf_start:]
    note.write_text(new_text, encoding="utf-8")
    return len(to_add)


def main() -> int:
    total_notes = 0
    total_aliases = 0
    for note in sorted(NOTES.glob("zadu-ref-*.md")):
        added = add_aliases(note)
        if added > 0:
            total_notes += 1
            total_aliases += added
            print(f"updated {note.name}: +{added} aliases")
    print(f"done notes_updated={total_notes} aliases_added={total_aliases}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
