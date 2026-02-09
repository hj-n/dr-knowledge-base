#!/usr/bin/env python3
from __future__ import annotations

import csv
import logging
import re
import warnings
from pathlib import Path
from typing import Dict, List, Tuple

ROOT = Path(__file__).resolve().parents[1]
NOTES_DIR = ROOT / "papers" / "notes"
OUT_CSV = ROOT / "builder" / "evidence" / "note-quality-audit.csv"

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

BOILERPLATE_PATTERNS = [
    r"use this source with at least one complementary note",
    r"use with complementary local/cluster/global metrics",
    r"use when selecting dr reliability checks",
    r"overfitting conclusions to a single metric family",
]

NOISE_PATTERNS = [
    r"authorized licensed use",
    r"all rights reserved",
    r"copyright",
    r"received:\s*\d",
    r"accepted:\s*\d",
    r"published:\s*\d",
]


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


def parse_evidence(text: str) -> List[Tuple[str, str]]:
    out = []
    for m in re.finditer(r"^-\s+([A-Z0-9\-]+)\s+\|\s+page:\s*([^,]+),\s*section:\s*([^,]+),\s*quote:\s*\"", text, flags=re.M):
        out.append((m.group(2).strip(), m.group(3).strip()))
    return out


def count_nonpage_evidence(text: str) -> int:
    return len(re.findall(r"^-\s+[A-Z0-9\-]+\s+\|\s+source:\s+", text, flags=re.M))


def source_pdf_pages(source_pdf: str) -> int:
    if not source_pdf.startswith("papers/raw/"):
        return 0
    p = ROOT / source_pdf
    if not p.exists() or p.suffix.lower() != ".pdf":
        return 0
    try:
        from pypdf import PdfReader

        return len(PdfReader(str(p)).pages)
    except Exception:
        return 0


def audit_one(path: Path) -> Dict[str, str]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    fm = parse_frontmatter(text)
    flags: List[str] = []

    missing = [h for h in REQUIRED_HEADERS if h not in text]
    if missing:
        flags.append("missing-required-sections")

    title = fm.get("title", "")
    if "<" in title and ">" in title:
        flags.append("html-tag-title")

    for pat in BOILERPLATE_PATTERNS:
        if re.search(pat, text, flags=re.I):
            flags.append("boilerplate-fallback")
            break

    evidence = parse_evidence(text)
    nonpage_evidence_count = count_nonpage_evidence(text)
    evidence_count = len(evidence) + nonpage_evidence_count
    pages = sorted(set(p for p, _ in evidence if p))
    unique_pages = len(pages)

    source_pdf = fm.get("source_pdf", "")
    is_web_source = source_pdf.startswith("http://") or source_pdf.startswith("https://")

    if evidence_count < 5:
        flags.append("low-evidence-count")

    pdf_pages = source_pdf_pages(source_pdf)
    if (not is_web_source) and pdf_pages >= 8 and unique_pages < 2:
        flags.append("single-page-evidence")

    noise_hits = sum(1 for pat in NOISE_PATTERNS if re.search(pat, text, flags=re.I))
    if noise_hits >= 1:
        flags.append("metadata-noise")

    return {
        "note": str(path.relative_to(ROOT)),
        "source_pdf": source_pdf,
        "source_exists": str((ROOT / source_pdf).exists()) if source_pdf else "False",
        "pdf_page_count": str(pdf_pages),
        "missing_sections": ";".join(missing),
        "evidence_count": str(evidence_count),
        "unique_evidence_pages": str(unique_pages),
        "flags": ";".join(sorted(set(flags))),
    }


def main() -> int:
    warnings.filterwarnings("ignore", message=r".*Multiple definitions in dictionary.*")
    warnings.filterwarnings("ignore", message=r".*Ignoring wrong pointing object.*")
    logging.getLogger("pypdf").setLevel(logging.ERROR)

    rows = [audit_one(p) for p in sorted(NOTES_DIR.glob("*.md"))]
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=[
                "note",
                "source_pdf",
                "source_exists",
                "pdf_page_count",
                "missing_sections",
                "evidence_count",
                "unique_evidence_pages",
                "flags",
            ],
        )
        w.writeheader()
        w.writerows(rows)

    flagged = sum(1 for r in rows if r["flags"])
    print(f"wrote {OUT_CSV.relative_to(ROOT)} (notes={len(rows)}, flagged={flagged})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
