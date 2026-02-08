#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import os
import re
import time
import html
from difflib import SequenceMatcher
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from urllib.parse import quote, urljoin
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
PENDING_CSV = ROOT / "builder" / "evidence" / "pending-reference-papers.csv"
OUT_DIR = ROOT / "papers" / "raw" / "pending-references"
OUT_REPORT = ROOT / "builder" / "evidence" / "pending-reference-pdf-collection.csv"
OUT_MISSING = ROOT / "builder" / "evidence" / "pending-reference-pdf-missing.csv"

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X) CodexDRBot/1.0"
TIMEOUT = 20
MAX_BYTES = 120 * 1024 * 1024
SLEEP = 0.15


def slugify(s: str, maxlen: int = 90) -> str:
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    if len(s) > maxlen:
        s = s[:maxlen].rstrip("-")
    return s or "paper"


def clean_doi(doi: str) -> str:
    doi = (doi or "").strip()
    doi = re.sub(r"^https?://(dx\.)?doi\.org/", "", doi, flags=re.I)
    return doi.strip()


def http_get(url: str, accept: str = "*/*") -> Tuple[Optional[bytes], str, str, int, str]:
    req = Request(url, headers={"User-Agent": USER_AGENT, "Accept": accept})
    try:
        with urlopen(req, timeout=TIMEOUT) as r:
            ct = r.headers.get("Content-Type", "")
            final = r.geturl()
            status = getattr(r, "status", 200)
            data = r.read(MAX_BYTES + 1)
            if len(data) > MAX_BYTES:
                return None, final, ct, status, "too_large"
            return data, final, ct, status, ""
    except HTTPError as e:
        return None, url, "", e.code, f"http_{e.code}"
    except URLError as e:
        return None, url, "", 0, f"url_error:{e.reason}"
    except Exception as e:
        return None, url, "", 0, f"err:{type(e).__name__}"


def looks_like_pdf(data: bytes, content_type: str) -> bool:
    if not data:
        return False
    if data[:5] == b"%PDF-":
        return True
    c = (content_type or "").lower()
    return "application/pdf" in c and data.startswith(b"%PDF")


def extract_pdf_links_from_html(base_url: str, html_text: str) -> List[str]:
    out: List[str] = []
    for m in re.finditer(r'href=["\']([^"\']+)["\']', html_text, flags=re.I):
        href = html.unescape(m.group(1).strip())
        if not href:
            continue
        low = href.lower()
        if ".pdf" in low or "download" in low or "pdf" in low:
            out.append(urljoin(base_url, href))
    # common meta tags
    for m in re.finditer(r'content=["\']([^"\']+\.pdf[^"\']*)["\']', html_text, flags=re.I):
        out.append(urljoin(base_url, html.unescape(m.group(1).strip())))
    # unique keep order
    seen = set()
    uniq = []
    for u in out:
        if u not in seen:
            seen.add(u)
            uniq.append(u)
    return uniq[:20]


def parse_arxiv_id_from_doi(doi: str) -> Optional[str]:
    m = re.match(r"10\.48550/arXiv\.(.+)$", doi, flags=re.I)
    if m:
        return m.group(1)
    return None


def arxiv_pdf_by_title(title: str) -> Optional[str]:
    q = quote(f'ti:"{title}"')
    url = f"http://export.arxiv.org/api/query?search_query={q}&start=0&max_results=3"
    data, _, _, status, err = http_get(url, accept="application/atom+xml")
    time.sleep(SLEEP)
    if not data or status >= 400:
        return None
    try:
        root = ET.fromstring(data)
    except Exception:
        return None
    ns = {"a": "http://www.w3.org/2005/Atom"}
    entries = root.findall("a:entry", ns)
    best = None
    best_score = 0.0
    for e in entries:
        t = (e.findtext("a:title", default="", namespaces=ns) or "").strip()
        score = SequenceMatcher(None, t.lower(), title.lower()).ratio()
        if score > best_score:
            best_score = score
            best = e
    if best is None or best_score < 0.76:
        return None
    for link in best.findall("a:link", ns):
        if link.attrib.get("title", "") == "pdf":
            return link.attrib.get("href")
    aid = (best.findtext("a:id", default="", namespaces=ns) or "").rstrip("/").split("/")[-1]
    if aid:
        return f"https://arxiv.org/pdf/{aid}.pdf"
    return None


def openalex_candidates_by_doi(doi: str) -> List[str]:
    doi_url = quote(f"https://doi.org/{doi}", safe="")
    api = f"https://api.openalex.org/works/{doi_url}"
    data, _, _, status, _ = http_get(api, accept="application/json")
    time.sleep(SLEEP)
    if not data or status >= 400:
        return []
    try:
        obj = json.loads(data.decode("utf-8", errors="ignore"))
    except Exception:
        return []
    return extract_openalex_urls(obj)


def openalex_candidates_by_title(title: str) -> List[str]:
    api = f"https://api.openalex.org/works?search={quote(title)}&per-page=5"
    data, _, _, status, _ = http_get(api, accept="application/json")
    time.sleep(SLEEP)
    if not data or status >= 400:
        return []
    try:
        obj = json.loads(data.decode("utf-8", errors="ignore"))
    except Exception:
        return []
    results = obj.get("results", []) if isinstance(obj, dict) else []
    best = None
    best_score = 0.0
    for r in results:
        t = (r.get("display_name") or "").strip()
        score = SequenceMatcher(None, t.lower(), title.lower()).ratio()
        if score > best_score:
            best_score = score
            best = r
    if not best or best_score < 0.78:
        return []
    return extract_openalex_urls(best)


def extract_openalex_urls(obj: dict) -> List[str]:
    urls = []
    oa = obj.get("open_access") if isinstance(obj, dict) else None
    if isinstance(oa, dict):
        u = oa.get("oa_url")
        if u:
            urls.append(u)
    for loc in (obj.get("locations") or []):
        if not isinstance(loc, dict):
            continue
        u = loc.get("pdf_url") or loc.get("landing_page_url")
        if u:
            urls.append(u)
    seen = set(); out = []
    for u in urls:
        if u not in seen:
            seen.add(u)
            out.append(u)
    return out[:12]


def crossref_pdf_links(doi: str) -> List[str]:
    api = f"https://api.crossref.org/works/{quote(doi)}"
    data, _, _, status, _ = http_get(api, accept="application/json")
    time.sleep(SLEEP)
    if not data or status >= 400:
        return []
    try:
        obj = json.loads(data.decode("utf-8", errors="ignore"))
    except Exception:
        return []
    msg = obj.get("message", {}) if isinstance(obj, dict) else {}
    links = msg.get("link") or []
    out = []
    for l in links:
        if not isinstance(l, dict):
            continue
        u = l.get("URL") or l.get("url")
        c = (l.get("content-type") or "").lower()
        if u and ("pdf" in c or u.lower().endswith(".pdf")):
            out.append(u)
    return out[:8]


def doi_landing_candidates(doi: str) -> List[str]:
    doi_url = f"https://doi.org/{doi}"
    data, final, ct, status, _ = http_get(doi_url, accept="text/html,application/pdf,*/*")
    time.sleep(SLEEP)
    if not data or status >= 400:
        return []
    if looks_like_pdf(data, ct):
        return [final]
    text = data.decode("utf-8", errors="ignore")
    return extract_pdf_links_from_html(final, text)


def try_download_pdf(url: str, out_path: Path) -> Tuple[bool, str, str]:
    data, final, ct, status, err = http_get(url, accept="application/pdf,text/html,*/*")
    time.sleep(SLEEP)
    if not data or status >= 400:
        return False, final, err or f"http_{status}"
    if looks_like_pdf(data, ct):
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_bytes(data)
        return True, final, ""

    # if html, follow embedded pdf links
    text = data.decode("utf-8", errors="ignore")
    for link in extract_pdf_links_from_html(final, text):
        d2, f2, ct2, s2, e2 = http_get(link, accept="application/pdf,*/*")
        time.sleep(SLEEP)
        if d2 and s2 < 400 and looks_like_pdf(d2, ct2):
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_bytes(d2)
            return True, f2, ""
    return False, final, "no_pdf_content"


def collect_candidates(title: str, doi: str) -> List[Tuple[str, str]]:
    cands: List[Tuple[str, str]] = []

    d = clean_doi(doi)
    if d:
        arx = parse_arxiv_id_from_doi(d)
        if arx:
            cands.append((f"arxiv_doi", f"https://arxiv.org/pdf/{arx}.pdf"))
        for u in openalex_candidates_by_doi(d):
            cands.append(("openalex_doi", u))
        for u in crossref_pdf_links(d):
            cands.append(("crossref_doi", u))
        for u in doi_landing_candidates(d):
            cands.append(("doi_landing", u))

    arx_title = arxiv_pdf_by_title(title)
    if arx_title:
        cands.append(("arxiv_title", arx_title))

    for u in openalex_candidates_by_title(title):
        cands.append(("openalex_title", u))

    # unique
    seen = set(); out = []
    for src, u in cands:
        if not u:
            continue
        u = u.strip()
        if u in seen:
            continue
        seen.add(u)
        out.append((src, u))
    return out


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    with PENDING_CSV.open("r", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))

    results = []
    missing = []

    for i, r in enumerate(rows, 1):
        cid = r.get("candidate_id", "")
        title = (r.get("paper_title", "") or "").strip()
        year = (r.get("year", "") or "").strip()
        doi = (r.get("doi", "") or "").strip()

        slug = slugify(f"{year}-{title}" if year else title)
        out_file = OUT_DIR / f"{cid}-{slug}.pdf"

        if out_file.exists() and out_file.stat().st_size > 1000:
            results.append(
                {
                    **r,
                    "download_status": "found_existing",
                    "downloaded_pdf": str(out_file.relative_to(ROOT)),
                    "resolved_url": "",
                    "source_channel": "existing",
                    "error": "",
                }
            )
            continue

        candidates = collect_candidates(title, doi)
        found = False
        last_err = "no_candidate_url"
        last_url = ""
        last_src = ""

        for src, u in candidates:
            ok, resolved, err = try_download_pdf(u, out_file)
            last_url = resolved or u
            last_src = src
            if ok:
                results.append(
                    {
                        **r,
                        "download_status": "found",
                        "downloaded_pdf": str(out_file.relative_to(ROOT)),
                        "resolved_url": last_url,
                        "source_channel": src,
                        "error": "",
                    }
                )
                found = True
                break
            last_err = err or "download_failed"

        if not found:
            missing_row = {
                **r,
                "download_status": "missing",
                "downloaded_pdf": "",
                "resolved_url": last_url,
                "source_channel": last_src,
                "error": last_err,
            }
            results.append(missing_row)
            missing.append(missing_row)

        if i % 15 == 0:
            print(f"progress {i}/{len(rows)}")

    fieldnames = list(rows[0].keys()) + [
        "download_status",
        "downloaded_pdf",
        "resolved_url",
        "source_channel",
        "error",
    ]

    with OUT_REPORT.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for rr in results:
            w.writerow(rr)

    with OUT_MISSING.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for rr in missing:
            w.writerow(rr)

    found_n = sum(1 for x in results if x["download_status"] in {"found", "found_existing"})
    miss_n = sum(1 for x in results if x["download_status"] == "missing")
    print(
        f"wrote {OUT_REPORT.relative_to(ROOT)} and {OUT_MISSING.relative_to(ROOT)} "
        f"(total={len(results)}, found={found_n}, missing={miss_n})"
    )


if __name__ == "__main__":
    main()
