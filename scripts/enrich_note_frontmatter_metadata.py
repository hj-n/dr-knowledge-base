#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import re
import time
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
NOTES_DIR = ROOT / "papers" / "notes"
LOG_CSV = ROOT / "builder" / "evidence" / "metadata-enrichment-log.csv"

UA = "dr-knowledge-metadata-enricher/1.0 (mailto:placeholder@example.com)"
DOI_RE = re.compile(r"10\.\d{4,9}/[-._;()/:A-Za-z0-9]+")
ARXIV_RE = re.compile(r"\b(\d{4}\.\d{4,5})(v\d+)?\b", re.I)
YEAR_RE = re.compile(r"\b(19\d{2}|20\d{2})\b")


def normalize_ws(s: str) -> str:
    s = s.replace("\u00a0", " ")
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def is_filename_like_title(title: str) -> bool:
    t = title.strip().lower()
    if not t:
        return True
    checks = [
        "1-s2",
        ".pdf",
        "pending-ref-",
        "pending-extra-",
        "_",
    ]
    if any(c in t for c in checks):
        return True
    if re.fullmatch(r"\d+(\.\d+)?", t):
        return True
    if re.fullmatch(r"[a-z0-9._-]{1,18}", t) and " " not in t:
        return True
    return False


def fm_bounds(text: str) -> Optional[Tuple[int, int]]:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        return None
    return (4, end)


def parse_frontmatter(text: str) -> Dict[str, str]:
    b = fm_bounds(text)
    if not b:
        return {}
    start, end = b
    out: Dict[str, str] = {}
    for raw in text[start:end].splitlines():
        if ":" not in raw:
            continue
        k, v = raw.split(":", 1)
        out[k.strip()] = v.strip().strip('"')
    return out


def replace_frontmatter(text: str, updates: Dict[str, str]) -> str:
    b = fm_bounds(text)
    if not b:
        return text
    start, end = b
    lines = text[start:end].splitlines()
    key_to_idx: Dict[str, int] = {}
    for i, raw in enumerate(lines):
        if ":" not in raw:
            continue
        k, _ = raw.split(":", 1)
        key_to_idx[k.strip()] = i

    for k, v in updates.items():
        safe = v.replace('"', "'")
        new_line = f'{k}: "{safe}"' if k in {"title", "authors", "venue", "seed_note_id"} else f"{k}: {safe}"
        if k in key_to_idx:
            lines[key_to_idx[k]] = new_line
        else:
            lines.append(new_line)

    new_fm = "\n".join(lines)
    return "---\n" + new_fm + "\n---\n" + text[end + 5 :]


def read_pdf_head(pdf_path: Path, max_pages: int = 3) -> Tuple[str, str, str]:
    """Returns (text, pdf_title, pdf_author)."""
    if not pdf_path.exists():
        return "", "", ""
    try:
        r = PdfReader(str(pdf_path))
    except Exception:
        return "", "", ""

    pdf_title = ""
    pdf_author = ""
    try:
        md = r.metadata or {}
        pdf_title = normalize_ws(str(md.get("/Title", "") or ""))
        pdf_author = normalize_ws(str(md.get("/Author", "") or ""))
    except Exception:
        pass

    chunks: List[str] = []
    n = min(len(r.pages), max_pages)
    for i in range(n):
        try:
            t = r.pages[i].extract_text() or ""
            chunks.append(t)
        except Exception:
            continue
    txt = "\n".join(chunks)
    txt = re.sub(r"(?<=\w)-\n(?=\w)", "", txt)
    return txt, pdf_title, pdf_author


def extract_doi(text: str, source_path: str) -> str:
    m = DOI_RE.search(text)
    if m:
        return m.group(0).rstrip(".,;)")
    m2 = DOI_RE.search(source_path)
    if m2:
        return m2.group(0).rstrip(".,;)")
    return ""


def extract_arxiv_id(text: str, source_path: str) -> str:
    for s in [source_path, text[:5000]]:
        m = ARXIV_RE.search(s)
        if m:
            return m.group(1)
    return ""


def infer_title_from_text(text: str, fallback: str) -> str:
    if not text:
        return fallback
    lines = [normalize_ws(x) for x in text.splitlines() if normalize_ws(x)]
    # focus before abstract
    abstract_idx = None
    for i, ln in enumerate(lines[:120]):
        if ln.lower() in {"abstract", "summary"} or ln.lower().startswith("abstract"):
            abstract_idx = i
            break
    pool = lines[: abstract_idx if abstract_idx is not None else 40]
    bad_sub = [
        "copyright",
        "all rights reserved",
        "doi",
        "arxiv",
        "ieee",
        "proceedings of",
        "journal",
        "volume",
        "accepted",
        "submitted",
        "\u00a9",
        "http",
        "www.",
        "department",
        "university",
        "email",
        "@",
    ]
    candidates: List[str] = []
    for ln in pool:
        low = ln.lower()
        if len(ln) < 20 or len(ln) > 180:
            continue
        if any(b in low for b in bad_sub):
            continue
        if re.fullmatch(r"[\d\W]+", ln):
            continue
        if ln.count(" ") < 3:
            continue
        candidates.append(ln)

    if not candidates:
        return fallback

    # combine adjacent title lines when line ends without punctuation
    best = candidates[0]
    best_idx = pool.index(best) if best in pool else -1
    if best_idx >= 0 and best_idx + 1 < len(pool):
        nxt = pool[best_idx + 1]
        if 8 <= len(nxt) <= 120 and not any(x in nxt.lower() for x in ["abstract", "university", "department", "@"]):
            combined = normalize_ws(best + " " + nxt)
            if 20 <= len(combined) <= 220:
                best = combined

    return best.strip(" .")


def infer_authors_from_text(text: str, title: str, fallback: str) -> str:
    if not text:
        return fallback
    lines = [normalize_ws(x) for x in text.splitlines() if normalize_ws(x)]
    if not lines:
        return fallback

    tnorm = normalize_ws(title).lower()
    idx = -1
    for i, ln in enumerate(lines[:120]):
        if tnorm and tnorm[:40] in ln.lower():
            idx = i
            break

    start = idx + 1 if idx >= 0 else 0
    window = lines[start : start + 20]

    bad = ["abstract", "keywords", "introduction", "doi", "arxiv", "department", "university", "school", "laboratory", "institute", "@"]
    for ln in window:
        low = ln.lower()
        if any(b in low for b in bad):
            continue
        if len(ln) < 6 or len(ln) > 160:
            continue
        if "," not in ln and " and " not in low and len(ln.split()) < 2:
            continue
        # keep likely person-name lines
        token_count = len(ln.split())
        if token_count > 25:
            continue
        if re.search(r"\b(figure|table|volume|issue|pp\.|pages)\b", low):
            continue
        # clean numeric markers
        clean = re.sub(r"\b\d+\b", "", ln)
        clean = normalize_ws(clean)
        if len(clean) < 6:
            continue
        return clean.strip(" ,;")

    return fallback


def http_json(url: str, timeout: int = 20) -> Optional[dict]:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode("utf-8", errors="ignore"))
    except Exception:
        return None


def crossref_by_doi(doi: str) -> Optional[dict]:
    doi_enc = urllib.parse.quote(doi, safe="")
    url = f"https://api.crossref.org/works/{doi_enc}"
    payload = http_json(url)
    if not payload:
        return None
    msg = payload.get("message") or {}
    return parse_crossref_message(msg)


def parse_crossref_message(msg: dict) -> Optional[dict]:
    if not msg:
        return None
    title = ""
    tarr = msg.get("title") or []
    if tarr:
        title = normalize_ws(tarr[0])
    authors = ""
    aarr = msg.get("author") or []
    names = []
    for a in aarr:
        given = normalize_ws(str(a.get("given", "") or ""))
        family = normalize_ws(str(a.get("family", "") or ""))
        full = normalize_ws((given + " " + family).strip())
        if full:
            names.append(full)
    if names:
        authors = ", ".join(names[:12])
    venue = ""
    carr = msg.get("container-title") or []
    if carr:
        venue = normalize_ws(carr[0])
    year = ""
    for key in ["published-print", "published-online", "issued", "created"]:
        part = msg.get(key) or {}
        dps = part.get("date-parts") or []
        if dps and dps[0]:
            y = str(dps[0][0])
            if re.fullmatch(r"\d{4}", y):
                year = y
                break
    doi = normalize_ws(str(msg.get("DOI", "") or ""))
    return {
        "title": title,
        "authors": authors,
        "venue": venue,
        "year": year,
        "doi": doi,
        "source": "crossref",
    }


def similarity(a: str, b: str) -> float:
    sa = set(re.findall(r"[a-z0-9]+", a.lower()))
    sb = set(re.findall(r"[a-z0-9]+", b.lower()))
    if not sa or not sb:
        return 0.0
    return len(sa & sb) / len(sa | sb)


def crossref_by_title(title: str, year_hint: str = "") -> Optional[dict]:
    q = urllib.parse.quote(title)
    url = f"https://api.crossref.org/works?query.title={q}&rows=5"
    payload = http_json(url)
    if not payload:
        return None
    items = (payload.get("message") or {}).get("items") or []
    best = None
    best_score = 0.0
    for it in items:
        cand = parse_crossref_message(it)
        if not cand or not cand.get("title"):
            continue
        s = similarity(title, cand["title"])
        if year_hint and cand.get("year") and cand["year"] == year_hint:
            s += 0.05
        if s > best_score:
            best_score = s
            best = cand
    if best and best_score >= 0.55:
        return best
    return None


def arxiv_lookup(arxiv_id: str) -> Optional[dict]:
    q = urllib.parse.quote(arxiv_id)
    url = f"http://export.arxiv.org/api/query?id_list={q}"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            xml = r.read().decode("utf-8", errors="ignore")
    except Exception:
        return None

    tm = re.search(r"<title>(.*?)</title>", xml, re.S)
    if not tm:
        return None
    # first title is feed title; use second if exists
    titles = re.findall(r"<title>(.*?)</title>", xml, re.S)
    if len(titles) < 2:
        return None
    title = normalize_ws(re.sub(r"\s+", " ", re.sub(r"<.*?>", "", titles[1])))
    auths = [normalize_ws(a) for a in re.findall(r"<name>(.*?)</name>", xml, re.S)]
    # first name may still be valid author, no feed-level name in arxiv atom usually
    authors = ", ".join([a for a in auths if a][:12])
    ym = re.search(r"<published>(\d{4})-\d{2}-\d{2}</published>", xml)
    year = ym.group(1) if ym else ""
    return {
        "title": title,
        "authors": authors,
        "venue": "arXiv",
        "year": year,
        "doi": "",
        "source": "arxiv",
    }


def clean_author_field(a: str) -> str:
    a = normalize_ws(a)
    a = re.sub(r"\[(.*?)\]", "", a)
    a = normalize_ws(a)
    return a


def choose_updates(orig: Dict[str, str], local: Dict[str, str], ext: Optional[Dict[str, str]]) -> Tuple[Dict[str, str], str]:
    updates: Dict[str, str] = {}
    reason = []

    cur_title = orig.get("title", "").strip()
    cur_auth = orig.get("authors", "").strip()
    cur_venue = orig.get("venue", "").strip()
    cur_year = str(orig.get("year", "")).strip()

    # title
    best_title = cur_title
    if ext and ext.get("title"):
        if is_filename_like_title(cur_title) or similarity(cur_title, ext["title"]) >= 0.45:
            best_title = ext["title"]
            reason.append(f"title:{ext.get('source','ext')}")
    elif is_filename_like_title(cur_title) and local.get("title"):
        best_title = local["title"]
        reason.append("title:pdf")

    if best_title and best_title != cur_title:
        updates["title"] = best_title

    # authors
    cur_auth_clean = clean_author_field(cur_auth)
    if cur_auth_clean.upper() == "UNKNOWN" or not cur_auth_clean or "[" in cur_auth:
        if ext and ext.get("authors"):
            updates["authors"] = ext["authors"]
            reason.append(f"authors:{ext.get('source','ext')}")
        elif local.get("authors") and local["authors"].upper() != "UNKNOWN":
            updates["authors"] = local["authors"]
            reason.append("authors:pdf")

    # venue
    if cur_venue.upper() == "UNKNOWN" or not cur_venue:
        if ext and ext.get("venue"):
            updates["venue"] = ext["venue"]
            reason.append(f"venue:{ext.get('source','ext')}")

    # year
    if (not re.fullmatch(r"\d{4}", cur_year)) or cur_year in {"2026", ""}:
        if ext and re.fullmatch(r"\d{4}", ext.get("year", "")):
            updates["year"] = ext["year"]
            reason.append(f"year:{ext.get('source','ext')}")
        elif re.fullmatch(r"\d{4}", local.get("year", "")):
            updates["year"] = local["year"]
            reason.append("year:pdf")

    return updates, ";".join(reason)


def main() -> int:
    rows = []
    changed = 0
    scanned = 0

    note_paths = sorted(NOTES_DIR.glob("*.md"))
    for p in note_paths:
        txt = p.read_text(encoding="utf-8", errors="ignore")
        fm = parse_frontmatter(txt)
        if not fm:
            continue

        title = fm.get("title", "")
        authors = fm.get("authors", "")
        venue = fm.get("venue", "")
        source_pdf = fm.get("source_pdf", "")

        if not source_pdf:
            continue

        needs = (
            is_filename_like_title(title)
            or authors.strip().upper() == "UNKNOWN"
            or venue.strip().upper() == "UNKNOWN"
        )
        if not needs:
            continue

        scanned += 1
        pdf_path = ROOT / source_pdf if source_pdf.startswith("papers/") else None
        head_text, pdf_meta_title, pdf_meta_author = ("", "", "")
        if pdf_path and pdf_path.exists() and pdf_path.suffix.lower() == ".pdf":
            head_text, pdf_meta_title, pdf_meta_author = read_pdf_head(pdf_path, max_pages=3)

        local_title = infer_title_from_text(head_text, title)
        if is_filename_like_title(local_title) and pdf_meta_title and not is_filename_like_title(pdf_meta_title):
            local_title = pdf_meta_title

        local_auth = "UNKNOWN"
        if pdf_meta_author and len(pdf_meta_author) > 3 and "untitled" not in pdf_meta_author.lower():
            local_auth = pdf_meta_author
        local_auth = infer_authors_from_text(head_text, local_title, local_auth)
        local_auth = clean_author_field(local_auth)
        if not local_auth:
            local_auth = "UNKNOWN"

        local_year = ""
        ym = YEAR_RE.search(head_text[:4000])
        if ym:
            local_year = ym.group(1)

        doi = extract_doi(head_text, source_pdf)
        arxiv_id = extract_arxiv_id(head_text, source_pdf)

        ext = None
        src_used = ""
        if arxiv_id:
            ext = arxiv_lookup(arxiv_id)
            if ext:
                src_used = "arxiv"
                time.sleep(0.2)

        if not ext and doi:
            ext = crossref_by_doi(doi)
            if ext:
                src_used = "crossref_doi"
                time.sleep(0.2)

        if not ext:
            title_for_query = local_title if not is_filename_like_title(local_title) else title
            if title_for_query and len(title_for_query) > 12:
                ext = crossref_by_title(title_for_query, str(fm.get("year", "")))
                if ext:
                    src_used = "crossref_title"
                    time.sleep(0.2)

        local = {
            "title": local_title,
            "authors": local_auth,
            "year": local_year,
        }
        updates, why = choose_updates(fm, local, ext)

        if updates:
            new_txt = replace_frontmatter(txt, updates)
            p.write_text(new_txt, encoding="utf-8")
            changed += 1

        rows.append({
            "note": str(p.relative_to(ROOT)),
            "source_pdf": source_pdf,
            "updated": "true" if updates else "false",
            "updates": ",".join(sorted(updates.keys())),
            "reason": why,
            "doi": doi,
            "arxiv_id": arxiv_id,
            "external_source": src_used,
            "old_title": title,
            "new_title": updates.get("title", title),
            "old_authors": authors,
            "new_authors": updates.get("authors", authors),
            "old_venue": venue,
            "new_venue": updates.get("venue", venue),
            "old_year": str(fm.get("year", "")),
            "new_year": updates.get("year", str(fm.get("year", ""))),
        })

    LOG_CSV.parent.mkdir(parents=True, exist_ok=True)
    with LOG_CSV.open("w", encoding="utf-8", newline="") as f:
        if rows:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)

    print(f"scanned={scanned} changed={changed} log={LOG_CSV.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
