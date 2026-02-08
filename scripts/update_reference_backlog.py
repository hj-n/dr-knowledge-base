#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
from collections import defaultdict
from dataclasses import dataclass, field
from difflib import SequenceMatcher
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "papers" / "raw"
CATALOG_CSV = ROOT / "docs" / "paper-catalog.csv"
OUT_CSV = ROOT / "builder" / "evidence" / "pending-reference-papers.csv"
OUT_MD = ROOT / "builder" / "evidence" / "pending-reference-papers.md"
OUT_PARSE_ISSUES_CSV = ROOT / "builder" / "evidence" / "pending-reference-parse-issues.csv"

REF_HEADING_RE = re.compile(r"(?im)^\s*(references|bibliography|works\s+cited)\s*$")
REF_ENTRY_RE = re.compile(r"(?ms)^\s*\[(\d+)\]\s*(.*?)(?=^\s*\[\d+\]\s*|\Z)")
REF_ENTRY_DOT_RE = re.compile(r"(?ms)^\s*(\d+)\.\s*(.*?)(?=^\s*\d+\.\s*|\Z)")
YEAR_RE = re.compile(r"\b(19\d{2}|20\d{2})\b")
DOI_RE = re.compile(r"10\.\d{4,9}/[-._;()/:A-Za-z0-9]+")

TITLE_KEYWORDS = {
    "dimensionality reduction",
    "dimension reduction",
    "multidimensional projection",
    "projection",
    "embedding",
    "manifold",
    "visual analytics",
    "visualization",
    "quality",
    "reliability",
    "trustworthiness",
    "continuity",
    "distortion",
    "rank",
    "stress",
    "neighborhood",
    "neighbor",
    "topology",
    "evaluation",
    "comparative review",
    "survey",
    "t-sne",
    "tsne",
    "umap",
    "mds",
    "isomap",
    "lle",
    "laplacian eigenmaps",
    "sammon",
    "local multidimensional scaling",
    "classimap",
    "nerv",
}

CONTEXT_KEYWORDS = {
    "reliability",
    "quality",
    "distortion",
    "trustworthiness",
    "continuity",
    "task",
    "visual analytics",
    "evaluation",
    "compare",
    "comparison",
    "metric",
    "measure",
    "reproducibility",
    "stability",
    "hyperparameter",
    "initialization",
    "topology",
    "neighborhood",
    "cluster",
}

TITLE_ANCHOR_TERMS = {
    "dimension",
    "dimensionality",
    "projection",
    "embedding",
    "manifold",
    "visual",
    "visualization",
    "analytics",
    "cluster",
    "neighborhood",
    "neighbor",
    "trustworthiness",
    "continuity",
    "distortion",
    "topology",
    "metric",
    "metrics",
    "quality",
    "evaluation",
    "interpret",
    "scatterplot",
    "mapping",
    "t-sne",
    "tsne",
    "umap",
    "mds",
    "isomap",
    "lle",
    "pca",
}

SHORT_TOKEN_KEYWORDS = {"lle", "mds", "pca", "umap", "tsne", "t-sne"}

STOP_TITLE_PREFIXES = (
    "ieee transactions on",
    "authorized licensed use",
    "copyright",
)


@dataclass
class SeedPaper:
    source_note: str
    title: str
    source_pdf: str


@dataclass
class CandidateMention:
    seed_note: str
    seed_pdf: str
    ref_id: str
    title: str
    authors: str
    year: str
    doi: str
    title_score: int
    context_score: int
    confidence: str


@dataclass
class CandidateAggregate:
    norm_title: str
    title: str
    authors: str
    year: str
    doi: str
    mentions: List[CandidateMention] = field(default_factory=list)

    def add(self, m: CandidateMention) -> None:
        self.mentions.append(m)
        if len(m.title) > len(self.title):
            self.title = m.title
        if not self.authors and m.authors:
            self.authors = m.authors
        if (not self.year) and m.year:
            self.year = m.year
        if (not self.doi) and m.doi:
            self.doi = m.doi


def normalize_text(s: str) -> str:
    s = s.lower()
    s = re.sub(r"[\u2010-\u2015]", "-", s)
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def load_seed_papers() -> List[SeedPaper]:
    out: List[SeedPaper] = []
    with CATALOG_CSV.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("is_seed_paper", "").strip().lower() != "true":
                continue
            src_pdf = row.get("source_pdf", "").strip()
            if not src_pdf or not src_pdf.lower().endswith(".pdf"):
                continue
            out.append(
                SeedPaper(
                    source_note=row.get("source_note", "").strip(),
                    title=row.get("paper_title", "").strip(),
                    source_pdf=src_pdf,
                )
            )
    return out


def load_existing_local_titles() -> List[str]:
    titles = []
    with CATALOG_CSV.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            t = row.get("paper_title", "").strip()
            if t:
                titles.append(normalize_text(t))
    return titles


def pdf_text(path: Path) -> str:
    reader = PdfReader(str(path))
    chunks = []
    for p in reader.pages:
        t = p.extract_text() or ""
        chunks.append(t)
    return "\n".join(chunks)


def split_body_refs(full_text: str) -> Tuple[str, str]:
    m = REF_HEADING_RE.search(full_text)
    if not m:
        return full_text, ""
    return full_text[: m.start()], full_text[m.end() :]


def normalize_ref_blob(blob: str) -> str:
    blob = blob.replace("\r", "\n")
    blob = re.sub(r"(?<=\w)-\n(?=\w)", "", blob)
    blob = re.sub(r"\n+", "\n", blob)
    return blob


def parse_numbered_refs(ref_blob: str) -> List[Tuple[str, str]]:
    out: List[Tuple[str, str]] = []
    blob = normalize_ref_blob(ref_blob)

    for rid, entry in REF_ENTRY_RE.findall(blob):
        e = clean_entry(entry)
        if e:
            out.append((rid, e))

    if out:
        return out

    for rid, entry in REF_ENTRY_DOT_RE.findall(blob):
        e = clean_entry(entry)
        if e:
            out.append((rid, e))
    return out


def clean_entry(entry: str) -> str:
    x = entry.strip()
    x = re.sub(r"\s+", " ", x)
    x = x.strip(" .;")
    return x


def extract_year(entry: str) -> str:
    m = YEAR_RE.search(entry)
    if not m:
        return ""
    y = int(m.group(1))
    if y < 1900 or y > 2026:
        return ""
    return str(y)


def extract_doi(entry: str) -> str:
    m = DOI_RE.search(entry)
    return m.group(0).rstrip(".,;") if m else ""


def extract_title(entry: str) -> Tuple[str, str]:
    # Returns (title, confidence)
    normalized = (
        entry.replace("“", "\"")
        .replace("”", "\"")
        .replace("„", "\"")
        .replace("‟", "\"")
    )
    q = re.search(r"\"([^\"]{8,320})\"", normalized)
    if q:
        title = strip_leading_author_fragment(q.group(1).strip(" ."))
        if title and not looks_like_noise(title):
            return title, "high"

    m = re.search(r"\b(19\d{2}|20\d{2})\.\s*([^\.]{8,260})\.", entry)
    if m:
        title = strip_leading_author_fragment(m.group(2).strip(" ."))
        if title and not looks_like_noise(title):
            return title, "medium"

    # fallback: try comma-separated chunk before venue-like token
    parts = [p.strip() for p in entry.split(".") if p.strip()]
    for p in parts:
        if len(p) < 8:
            continue
        low = p.lower()
        if any(low.startswith(pref) for pref in STOP_TITLE_PREFIXES):
            continue
        if YEAR_RE.search(p):
            continue
        if "," in p and len(p.split()) <= 4:
            continue
        return strip_leading_author_fragment(p.strip(" .")), "low"

    return "", "low"


def strip_leading_author_fragment(title: str) -> str:
    t = (
        title.replace("“", "\"")
        .replace("”", "\"")
        .replace("„", "\"")
        .replace("‟", "\"")
        .strip(" .")
    )
    # If a quoted title exists, trust it first.
    q = re.search(r"\"([^\"]{8,320})\"", t)
    if q:
        return q.group(1).strip(" .")
    # Remove common "Surname, title" extraction residue.
    m = re.match(
        r"^[A-Z][A-Za-z'\-]+(?:\s+[A-Z][A-Za-z'\-]+){0,3},\s+(.+)$",
        t,
    )
    if m:
        cand = m.group(1).strip(" .")
        if cand:
            t = cand
    # Strip trailing venue glue if captured into title.
    t = re.sub(
        r"\s*,\s*(in\s+Proc\.|IEEE\s+Trans\.|J\.|Comput\.|Neurocomputing).*$",
        "",
        t,
        flags=re.I,
    )
    return t.strip(" .,;")


def looks_like_noise(title: str) -> bool:
    low = title.lower()
    if any(low.startswith(pref) for pref in STOP_TITLE_PREFIXES):
        return True
    if len(low) < 8:
        return True
    words = [w for w in re.split(r"\s+", low) if w]
    if len(words) < 3:
        return True
    # Common bad extraction pattern: just surnames joined by "and".
    if len(words) <= 5 and " and " in low and "," not in low and ":" not in low:
        return True
    # Reject almost-all single-letter tokens.
    alpha_words = [w for w in words if re.search(r"[a-z]", w)]
    if alpha_words and sum(1 for w in alpha_words if len(w) <= 2) / len(alpha_words) > 0.6:
        return True
    return False


def extract_authors(entry: str, title: str) -> str:
    s = entry
    if title:
        s = s.split(title)[0]
    # drop leading [n] etc already removed
    s = re.sub(r"\b(19\d{2}|20\d{2})\b.*$", "", s).strip(" ,.;")
    s = (
        s.replace("“", "")
        .replace("”", "")
        .replace("\"", "")
        .strip(" ,.;")
    )
    # keep concise
    if len(s) > 220:
        s = s[:220].rstrip()
    return s


def title_keyword_score(title: str) -> int:
    low = title.lower()
    score = 0
    for kw in TITLE_KEYWORDS:
        if keyword_in_text(low, kw):
            score += 1
    return score


def title_has_anchor_term(title: str) -> bool:
    low = title.lower()
    return any(keyword_in_text(low, t) for t in TITLE_ANCHOR_TERMS)


def keyword_in_text(text: str, keyword: str) -> bool:
    if keyword in SHORT_TOKEN_KEYWORDS:
        return re.search(rf"\\b{re.escape(keyword)}\\b", text) is not None
    return keyword in text


def parse_citation_ids(token: str) -> List[str]:
    token = token.strip()
    if not token:
        return []
    ids: List[str] = []
    for part in token.split(","):
        part = part.strip()
        r = re.match(r"^(\d+)\s*[-–]\s*(\d+)$", part)
        if r:
            a, b = int(r.group(1)), int(r.group(2))
            if a <= b and b - a <= 50:
                ids.extend([str(i) for i in range(a, b + 1)])
            continue
        d = re.match(r"^(\d+)$", part)
        if d:
            ids.append(d.group(1))
    return ids


def collect_context_scores(body_text: str) -> Dict[str, int]:
    scores: Dict[str, int] = defaultdict(int)
    # look at contexts around [x], [x,y], [x-y]
    for m in re.finditer(r"\[(\d+[\d,\s\-–]*)\]", body_text):
        token = m.group(1)
        cited_ids = parse_citation_ids(token)
        if not cited_ids:
            continue
        start = max(0, m.start() - 220)
        end = min(len(body_text), m.end() + 220)
        ctx = body_text[start:end].lower()
        hit = sum(1 for kw in CONTEXT_KEYWORDS if kw in ctx)
        if hit == 0:
            continue
        for rid in cited_ids:
            scores[rid] += hit
    return scores


def is_existing_local_title(norm_title: str, existing_norm_titles: List[str]) -> bool:
    if not norm_title:
        return False
    if norm_title in existing_norm_titles:
        return True
    for ex in existing_norm_titles:
        # fast short-circuit by token overlap
        a = set(norm_title.split())
        b = set(ex.split())
        if not a or not b:
            continue
        j = len(a & b) / len(a | b)
        if j >= 0.82:
            return True
        if len(norm_title) > 16 and len(ex) > 16:
            if SequenceMatcher(None, norm_title, ex).ratio() >= 0.92:
                return True
    return False


def relevance_reason(title_score: int, context_score: int, doi: str) -> str:
    parts = []
    if title_score > 0:
        parts.append(f"title_keywords={title_score}")
    if context_score > 0:
        parts.append(f"body_citation_context={context_score}")
    if doi:
        parts.append("doi_found")
    return "; ".join(parts) if parts else "weak_signal"


def write_outputs(
    rows: List[Dict[str, str]],
    seeds: List[SeedPaper],
    parse_issues: List[Dict[str, str]],
) -> None:
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8", newline="") as f:
        fieldnames = [
            "candidate_id",
            "paper_title",
            "authors",
            "year",
            "doi",
            "source_seed_count",
            "source_seed_notes",
            "source_seed_pdfs",
            "mentions",
            "max_title_keyword_score",
            "max_context_score",
            "confidence",
            "relevance_signals",
            "status",
            "next_action",
        ]
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow(r)

    with OUT_MD.open("w", encoding="utf-8") as f:
        f.write("# Pending Reference Papers (No Local PDF Yet)\n\n")
        f.write(
            "This list is generated from seed-paper bibliographies plus body citation-context signals, "
            "filtered for DR reliability and visual analytics relevance.\n\n"
        )
        f.write(f"- Seed papers scanned: `{len(seeds)}`\n")
        f.write(f"- Pending candidates: `{len(rows)}`\n")
        f.write(f"- Seed parse issues: `{len(parse_issues)}`\n")
        f.write(f"- CSV: `{OUT_CSV.relative_to(ROOT)}`\n\n")

        f.write("## Top Candidates\n\n")
        f.write("| # | Title | Year | Seeds | Signals |\n")
        f.write("|---:|---|---:|---:|---|\n")
        for i, r in enumerate(rows[:80], 1):
            t = r["paper_title"].replace("|", "\\|")
            f.write(
                f"| {i} | {t} | {r['year'] or '-'} | {r['source_seed_count']} | {r['relevance_signals']} |\n"
            )

        if parse_issues:
            f.write("\n## Seed Parse Issues\n\n")
            f.write("| Seed Note | Source PDF | Issue |\n")
            f.write("|---|---|---|\n")
            for p in parse_issues:
                f.write(
                    f"| `{p['seed_note']}` | `{p['source_pdf']}` | `{p['issue']}` |\n"
                )

    with OUT_PARSE_ISSUES_CSV.open("w", encoding="utf-8", newline="") as f:
        fields = ["seed_note", "source_pdf", "issue"]
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for p in parse_issues:
            w.writerow(p)


def main() -> None:
    seeds = load_seed_papers()
    existing_titles = load_existing_local_titles()

    aggregates: Dict[str, CandidateAggregate] = {}
    parse_issues: List[Dict[str, str]] = []

    for seed in seeds:
        pdf_path = ROOT / seed.source_pdf
        if not pdf_path.exists():
            continue

        full_text = pdf_text(pdf_path)
        body_text, refs_text = split_body_refs(full_text)
        if not refs_text.strip():
            # no parsable references section
            parse_issues.append(
                {
                    "seed_note": seed.source_note,
                    "source_pdf": seed.source_pdf,
                    "issue": "no_reference_heading_or_empty_section",
                }
            )
            continue

        entries = parse_numbered_refs(refs_text)
        if not entries:
            parse_issues.append(
                {
                    "seed_note": seed.source_note,
                    "source_pdf": seed.source_pdf,
                    "issue": "reference_section_found_but_not_numbered_entries",
                }
            )
            continue

        ctx_scores = collect_context_scores(body_text)

        for ref_id, entry in entries:
            year = extract_year(entry)
            doi = extract_doi(entry)
            title, conf = extract_title(entry)
            if not title:
                continue
            norm = normalize_text(title)
            if not norm:
                continue

            tscore = title_keyword_score(title)
            cscore = ctx_scores.get(ref_id, 0)

            # Relevance gate:
            # - keep direct title-signal references
            # - keep context-supported references only if title still looks DR/VA-related
            if tscore == 0 and cscore < 3:
                continue
            if tscore == 0 and not title_has_anchor_term(title):
                continue
            # Strong noise guard for context-only entries.
            if tscore == 0 and cscore < 6 and not re.search(
                r"(dimension|projection|embedding|visual|cluster|metric|quality|manifold|topology|neigh|t-sne|umap|mds)",
                title.lower(),
            ):
                continue

            # Skip if already in local PDF-backed catalog
            if is_existing_local_title(norm, existing_titles):
                continue

            authors = extract_authors(entry, title)

            mention = CandidateMention(
                seed_note=seed.source_note,
                seed_pdf=seed.source_pdf,
                ref_id=ref_id,
                title=title,
                authors=authors,
                year=year,
                doi=doi,
                title_score=tscore,
                context_score=cscore,
                confidence=conf,
            )

            agg = aggregates.get(norm)
            if agg is None:
                aggregates[norm] = CandidateAggregate(
                    norm_title=norm,
                    title=title,
                    authors=authors,
                    year=year,
                    doi=doi,
                    mentions=[mention],
                )
            else:
                agg.add(mention)

    rows: List[Dict[str, str]] = []
    for i, agg in enumerate(aggregates.values(), 1):
        seed_notes = sorted({m.seed_note for m in agg.mentions})
        seed_pdfs = sorted({m.seed_pdf for m in agg.mentions})
        max_t = max(m.title_score for m in agg.mentions)
        max_c = max(m.context_score for m in agg.mentions)
        conf = "high" if any(m.confidence == "high" for m in agg.mentions) else "medium"
        has_anchor = title_has_anchor_term(agg.title)

        # Final priority gate to reduce noisy extraction artifacts.
        keep = False
        if max_t >= 2:
            keep = True
        elif max_t >= 1 and len(seed_notes) >= 2:
            keep = True
        elif max_t >= 1 and max_c >= 4:
            keep = True
        elif max_c >= 8 and has_anchor:
            keep = True
        if not keep:
            continue

        rows.append(
            {
                "candidate_id": f"pending-ref-{i:03d}",
                "paper_title": agg.title,
                "authors": agg.authors,
                "year": agg.year,
                "doi": agg.doi,
                "source_seed_count": str(len(seed_notes)),
                "source_seed_notes": "; ".join(seed_notes),
                "source_seed_pdfs": "; ".join(seed_pdfs),
                "mentions": str(len(agg.mentions)),
                "max_title_keyword_score": str(max_t),
                "max_context_score": str(max_c),
                "confidence": conf,
                "relevance_signals": relevance_reason(max_t, max_c, agg.doi),
                "status": "missing_local_pdf",
                "next_action": "collect_pdf",
            }
        )

    rows.sort(
        key=lambda r: (
            -int(r["source_seed_count"]),
            -int(r["max_context_score"]),
            -int(r["max_title_keyword_score"]),
            -(int(r["year"]) if r["year"].isdigit() else 0),
            r["paper_title"].lower(),
        )
    )

    # Reassign IDs post-sort for stable priority order
    for idx, r in enumerate(rows, 1):
        r["candidate_id"] = f"pending-ref-{idx:03d}"

    write_outputs(rows, seeds, parse_issues)
    print(
        f"wrote {OUT_CSV.relative_to(ROOT)}, {OUT_MD.relative_to(ROOT)}, and "
        f"{OUT_PARSE_ISSUES_CSV.relative_to(ROOT)} "
        f"(seed_scanned={len(seeds)}, pending={len(rows)}, parse_issues={len(parse_issues)})"
    )


if __name__ == "__main__":
    main()
