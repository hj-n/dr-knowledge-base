#!/usr/bin/env python3
from __future__ import annotations

import csv
import logging
import re
import warnings
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
NOTES_DIR = ROOT / "papers" / "notes"
DETAIL_CSV = ROOT / "builder" / "evidence" / "note-pdf-grounding.csv"
SUMMARY_CSV = ROOT / "builder" / "evidence" / "note-pdf-grounding-summary.csv"

EVIDENCE_RE = re.compile(
    r'^-\s+(?P<eid>[A-Z0-9\-]+)\s+\|\s+page:\s*(?P<page>[^,]+),\s*section:\s*(?P<section>[^,]+),\s*quote:\s*"(?P<quote>.*)"\s*$',
    flags=re.M,
)


@dataclass
class EvidenceRow:
    eid: str
    page: str
    section: str
    quote: str


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


def parse_evidence(text: str) -> List[EvidenceRow]:
    rows: List[EvidenceRow] = []
    for m in EVIDENCE_RE.finditer(text):
        rows.append(
            EvidenceRow(
                eid=m.group("eid").strip(),
                page=m.group("page").strip(),
                section=m.group("section").strip(),
                quote=m.group("quote").strip(),
            )
        )
    return rows


def norm_text(s: str) -> str:
    s = s.replace("\u00a0", " ")
    s = re.sub(r"(?<=\w)-\s+(?=\w)", "", s)
    s = s.lower()
    s = re.sub(r"[^a-z0-9\s]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def page_from_str(s: str) -> Optional[int]:
    m = re.search(r"\d+", s)
    if not m:
        return None
    return int(m.group())


def tokenize_for_fuzzy(s: str) -> List[str]:
    words = [w for w in norm_text(s).split() if len(w) >= 5]
    # frequency-agnostic, keep order unique
    out: List[str] = []
    seen = set()
    for w in words:
        if w in seen:
            continue
        seen.add(w)
        out.append(w)
    return out[:10]


def fuzzy_page_hit(tokens: List[str], page_norm: str) -> bool:
    if len(tokens) < 3:
        return False
    hits = sum(1 for t in tokens if t in page_norm)
    return hits >= max(3, int(len(tokens) * 0.6))


def find_quote_pages(quote: str, pages_norm: List[str]) -> Tuple[List[int], List[int]]:
    qn = norm_text(quote)
    if not qn:
        return [], []

    exact = [i + 1 for i, p in enumerate(pages_norm) if qn in p]
    if exact:
        return exact, []

    tokens = tokenize_for_fuzzy(quote)
    fuzzy = [i + 1 for i, p in enumerate(pages_norm) if fuzzy_page_hit(tokens, p)]
    return [], fuzzy


def main() -> int:
    warnings.filterwarnings("ignore", message=r".*Multiple definitions in dictionary.*")
    warnings.filterwarnings("ignore", message=r".*Ignoring wrong pointing object.*")
    logging.getLogger("pypdf").setLevel(logging.ERROR)

    details: List[Dict[str, str]] = []
    summaries: List[Dict[str, str]] = []

    note_paths = sorted(NOTES_DIR.glob("*.md"))

    for note_path in note_paths:
        rel_note = str(note_path.relative_to(ROOT))
        text = note_path.read_text(encoding="utf-8", errors="ignore")
        fm = parse_frontmatter(text)
        source_pdf = fm.get("source_pdf", "")
        evidence_rows = parse_evidence(text)

        total = len(evidence_rows)
        exact_ref = 0
        exact_other = 0
        fuzzy_ref = 0
        fuzzy_other = 0
        not_found = 0
        invalid_page = 0
        skipped = 0

        if not source_pdf.startswith("papers/raw/"):
            for e in evidence_rows:
                details.append(
                    {
                        "note": rel_note,
                        "source_pdf": source_pdf,
                        "evidence_id": e.eid,
                        "declared_page": e.page,
                        "status": "skipped_non_pdf_source",
                        "matched_pages": "",
                        "matched_mode": "",
                    }
                )
                skipped += 1

            summaries.append(
                {
                    "note": rel_note,
                    "source_pdf": source_pdf,
                    "source_exists": "False",
                    "evidence_total": str(total),
                    "exact_ref_page": str(exact_ref),
                    "exact_other_page": str(exact_other),
                    "fuzzy_ref_page": str(fuzzy_ref),
                    "fuzzy_other_page": str(fuzzy_other),
                    "not_found": str(not_found),
                    "invalid_page": str(invalid_page),
                    "skipped": str(skipped),
                }
            )
            continue

        pdf_path = ROOT / source_pdf
        if not pdf_path.exists():
            for e in evidence_rows:
                details.append(
                    {
                        "note": rel_note,
                        "source_pdf": source_pdf,
                        "evidence_id": e.eid,
                        "declared_page": e.page,
                        "status": "missing_pdf",
                        "matched_pages": "",
                        "matched_mode": "",
                    }
                )
                skipped += 1

            summaries.append(
                {
                    "note": rel_note,
                    "source_pdf": source_pdf,
                    "source_exists": "False",
                    "evidence_total": str(total),
                    "exact_ref_page": str(exact_ref),
                    "exact_other_page": str(exact_other),
                    "fuzzy_ref_page": str(fuzzy_ref),
                    "fuzzy_other_page": str(fuzzy_other),
                    "not_found": str(not_found),
                    "invalid_page": str(invalid_page),
                    "skipped": str(skipped),
                }
            )
            continue

        try:
            reader = PdfReader(str(pdf_path))
            pages_norm = [norm_text(p.extract_text() or "") for p in reader.pages]
        except Exception:
            for e in evidence_rows:
                details.append(
                    {
                        "note": rel_note,
                        "source_pdf": source_pdf,
                        "evidence_id": e.eid,
                        "declared_page": e.page,
                        "status": "pdf_parse_error",
                        "matched_pages": "",
                        "matched_mode": "",
                    }
                )
                skipped += 1

            summaries.append(
                {
                    "note": rel_note,
                    "source_pdf": source_pdf,
                    "source_exists": "True",
                    "evidence_total": str(total),
                    "exact_ref_page": str(exact_ref),
                    "exact_other_page": str(exact_other),
                    "fuzzy_ref_page": str(fuzzy_ref),
                    "fuzzy_other_page": str(fuzzy_other),
                    "not_found": str(not_found),
                    "invalid_page": str(invalid_page),
                    "skipped": str(skipped),
                }
            )
            continue

        npages = len(pages_norm)
        for e in evidence_rows:
            declared = page_from_str(e.page)
            if declared is None or declared < 1 or declared > npages:
                invalid_page += 1

            exact_pages, fuzzy_pages = find_quote_pages(e.quote, pages_norm)

            if exact_pages:
                if declared in exact_pages:
                    status = "exact_ref_page"
                    exact_ref += 1
                else:
                    status = "exact_other_page"
                    exact_other += 1
                details.append(
                    {
                        "note": rel_note,
                        "source_pdf": source_pdf,
                        "evidence_id": e.eid,
                        "declared_page": e.page,
                        "status": status,
                        "matched_pages": ";".join(map(str, exact_pages)),
                        "matched_mode": "exact",
                    }
                )
                continue

            if fuzzy_pages:
                if declared in fuzzy_pages:
                    status = "fuzzy_ref_page"
                    fuzzy_ref += 1
                else:
                    status = "fuzzy_other_page"
                    fuzzy_other += 1
                details.append(
                    {
                        "note": rel_note,
                        "source_pdf": source_pdf,
                        "evidence_id": e.eid,
                        "declared_page": e.page,
                        "status": status,
                        "matched_pages": ";".join(map(str, fuzzy_pages[:8])),
                        "matched_mode": "fuzzy",
                    }
                )
                continue

            not_found += 1
            details.append(
                {
                    "note": rel_note,
                    "source_pdf": source_pdf,
                    "evidence_id": e.eid,
                    "declared_page": e.page,
                    "status": "not_found",
                    "matched_pages": "",
                    "matched_mode": "none",
                }
            )

        summaries.append(
            {
                "note": rel_note,
                "source_pdf": source_pdf,
                "source_exists": "True",
                "evidence_total": str(total),
                "exact_ref_page": str(exact_ref),
                "exact_other_page": str(exact_other),
                "fuzzy_ref_page": str(fuzzy_ref),
                "fuzzy_other_page": str(fuzzy_other),
                "not_found": str(not_found),
                "invalid_page": str(invalid_page),
                "skipped": str(skipped),
            }
        )

    DETAIL_CSV.parent.mkdir(parents=True, exist_ok=True)
    with DETAIL_CSV.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "note",
                "source_pdf",
                "evidence_id",
                "declared_page",
                "status",
                "matched_pages",
                "matched_mode",
            ],
        )
        writer.writeheader()
        writer.writerows(details)

    with SUMMARY_CSV.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "note",
                "source_pdf",
                "source_exists",
                "evidence_total",
                "exact_ref_page",
                "exact_other_page",
                "fuzzy_ref_page",
                "fuzzy_other_page",
                "not_found",
                "invalid_page",
                "skipped",
            ],
        )
        writer.writeheader()
        writer.writerows(summaries)

    total_evidence = sum(int(r["evidence_total"]) for r in summaries)
    total_not_found = sum(int(r["not_found"]) for r in summaries)
    total_exact_ref = sum(int(r["exact_ref_page"]) for r in summaries)
    total_exact_other = sum(int(r["exact_other_page"]) for r in summaries)
    total_fuzzy_ref = sum(int(r["fuzzy_ref_page"]) for r in summaries)
    total_fuzzy_other = sum(int(r["fuzzy_other_page"]) for r in summaries)

    print(
        "wrote"
        f" {DETAIL_CSV.relative_to(ROOT)} and {SUMMARY_CSV.relative_to(ROOT)}"
        f" (notes={len(summaries)}, evidence={total_evidence},"
        f" exact_ref={total_exact_ref}, exact_other={total_exact_other},"
        f" fuzzy_ref={total_fuzzy_ref}, fuzzy_other={total_fuzzy_other},"
        f" not_found={total_not_found})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
