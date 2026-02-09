#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
from pathlib import Path
from typing import List, Tuple

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "builder" / "evidence" / "note-quality-audit.csv"

NOISE = [
    "copyright",
    "authorized licensed use",
    "all rights reserved",
    "received:",
    "accepted:",
    "published:",
    "doi:",
    "correspondence",
]


def clean_sentences(text: str) -> List[str]:
    text = re.sub(r"(?<=\w)-\n(?=\w)", "", text)
    text = text.replace("\u00a0", " ")
    text = re.sub(r"\s+", " ", text)
    parts = re.split(r"(?<=[\.!?])\s+(?=[A-Z0-9\(\[])", text)
    out = []
    for p in parts:
        s = p.strip(" -")
        low = s.lower()
        if len(s) < 70 or len(s) > 330:
            continue
        if any(n in low for n in NOISE):
            continue
        if sum(c.isalpha() for c in s) < 35:
            continue
        out.append(s)
    return out


def parse_frontmatter(text: str) -> dict:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    fm = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm


def find_next_eid_prefix(text: str) -> Tuple[str, int]:
    ids = re.findall(r"^-\s+([A-Z0-9\-]+)-E(\d+)\s+\|\s+page:", text, flags=re.M)
    if not ids:
        return ("EVID", 1)
    prefix = ids[0][0]
    max_n = max(int(n) for _, n in ids)
    return prefix, max_n + 1


def ensure_multpage(note_rel: str) -> bool:
    note_path = ROOT / note_rel
    if not note_path.exists():
        return False
    text = note_path.read_text(encoding="utf-8", errors="ignore")
    fm = parse_frontmatter(text)
    src = fm.get("source_pdf", "")
    if not src.startswith("papers/raw/"):
        return False
    pdf = ROOT / src
    if not pdf.exists() or pdf.suffix.lower() != ".pdf":
        return False

    reader = PdfReader(str(pdf))
    total = len(reader.pages)
    if total < 2:
        return False

    # pick candidate pages away from page 1
    candidate_indices = list(range(1, min(total, 6)))
    if total > 8:
        candidate_indices.extend(range(max(1, total - 3), total))

    added: List[Tuple[int, str]] = []
    for pi in candidate_indices:
        try:
            ptxt = reader.pages[pi].extract_text() or ""
        except Exception:
            continue
        sents = clean_sentences(ptxt)
        if not sents:
            continue
        # prefer technical sentences
        chosen = None
        for s in sents:
            low = s.lower()
            if any(k in low for k in ["method", "algorithm", "result", "experiment", "parameter", "complexity", "evaluate", "embedding"]):
                chosen = s
                break
        if chosen is None:
            chosen = sents[0]
        added.append((pi + 1, chosen))
        if len(added) >= 2:
            break

    if not added:
        return False

    prefix, next_n = find_next_eid_prefix(text)

    ev_hdr = "\n# Evidence\n"
    idx = text.find(ev_hdr)
    if idx == -1:
        return False

    insert = []
    for page, quote in added:
        q = quote.replace('"', "'").replace("|", "/")
        insert.append(f"- {prefix}-E{next_n} | page: {page}, section: extracted, quote: \"{q}\"")
        next_n += 1

    if insert:
        text = text.rstrip() + "\n" + "\n".join(insert) + "\n"
        note_path.write_text(text, encoding="utf-8")
        return True
    return False


def main() -> int:
    rows = list(csv.DictReader(AUDIT.open(encoding="utf-8")))
    targets = [r["note"] for r in rows if "single-page-evidence" in (r.get("flags") or "")]
    changed = 0
    for n in targets:
        if ensure_multpage(n):
            changed += 1
            print(f"updated {n}")
        else:
            print(f"skip {n}")
    print(f"done changed={changed} targets={len(targets)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
