#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Dict, List, Set

ROOT = Path(__file__).resolve().parents[1]
MENTIONS_JSON = ROOT / "builder" / "evidence" / "pending-note-entity-mentions.json"

METRICS_DIR = ROOT / "docs" / "metrics"
TECH_DIR = ROOT / "docs" / "techniques"

NOTE_RE = re.compile(r"`(papers/notes/[^`]+\.md)`")

BLOCKLIST = [
    "perception",
    "explainer",
    "explainers",
    "bias-in-perceiving",
    "user-centered",
    "narrative",
    "interactive-toolkit",
]


def read_mentions() -> Dict[str, Dict[str, List[str]]]:
    return json.loads(MENTIONS_JSON.read_text(encoding="utf-8"))


def is_allowed_note(path: str) -> bool:
    p = path.lower()
    if not (p.startswith("papers/notes/pending-ref-") or p.startswith("papers/notes/pending-extra-")):
        return False
    return not any(b in p for b in BLOCKLIST)


def split_sections(text: str) -> tuple[str, str, str]:
    marker = "\n## Source Notes\n"
    i = text.find(marker)
    if i == -1:
        return text, "", ""
    head = text[: i + len(marker)]
    tail = text[i + len(marker) :]
    # next heading after Source Notes
    m = re.search(r"\n## ", tail)
    if m:
        body = tail[: m.start()]
        rest = tail[m.start() :]
    else:
        body = tail
        rest = ""
    return head, body, rest


def enrich_file(path: Path, candidates: List[str], max_add: int) -> int:
    text = path.read_text(encoding="utf-8")
    head, body, rest = split_sections(text)
    if not body and "## Source Notes" not in text:
        return 0

    existing: Set[str] = set(NOTE_RE.findall(body))

    # prefer pending-ref over pending-extra
    cand = [c for c in candidates if is_allowed_note(c)]
    cand.sort(key=lambda x: (0 if "/pending-ref-" in x else 1, x))

    add: List[str] = []
    for c in cand:
        if c in existing:
            continue
        add.append(c)
        if len(add) >= max_add:
            break

    if not add:
        return 0

    body_lines = body.rstrip("\n").splitlines() if body.strip() else []
    if not body_lines:
        body_lines = ["- No source notes linked yet."]

    if len(body_lines) == 1 and body_lines[0].strip() == "- No source notes linked yet.":
        body_lines = []

    for c in add:
        body_lines.append(f"- `{c}` (pending-reference evidence)")

    new_text = head + "\n".join(body_lines).rstrip() + "\n"
    if rest:
        new_text += rest.lstrip("\n")
        if not new_text.endswith("\n"):
            new_text += "\n"

    path.write_text(new_text, encoding="utf-8")
    return len(add)


def main() -> int:
    mentions = read_mentions()

    total_files = 0
    total_added = 0

    for metric_id, refs in mentions.get("metrics", {}).items():
        f = METRICS_DIR / f"{metric_id}.md"
        if not f.exists():
            continue
        n = enrich_file(f, refs, max_add=6)
        if n > 0:
            total_files += 1
            total_added += n

    for tech_id, refs in mentions.get("techniques", {}).items():
        f = TECH_DIR / f"{tech_id}.md"
        if not f.exists():
            continue
        n = enrich_file(f, refs, max_add=8)
        if n > 0:
            total_files += 1
            total_added += n

    print(f"updated_files={total_files} added_source_note_links={total_added}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
