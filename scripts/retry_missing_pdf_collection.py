#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import re
import time
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from urllib.parse import quote, urljoin
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

ROOT = Path(__file__).resolve().parents[1]
MISSING_CSV = ROOT / "builder" / "evidence" / "pending-reference-pdf-missing.csv"
COLLECTION_CSV = ROOT / "builder" / "evidence" / "pending-reference-pdf-collection.csv"
OUT_DIR = ROOT / "papers" / "raw" / "pending-references"
OUT_RETRY_LOG = ROOT / "builder" / "evidence" / "pending-reference-pdf-retry-log.csv"
OUT_STILL_MISSING = ROOT / "builder" / "evidence" / "pending-reference-pdf-still-missing.csv"
OUT_OFFICIAL = ROOT / "builder" / "evidence" / "pending-reference-official-urls.csv"
OUT_OFFICIAL_MD = ROOT / "builder" / "evidence" / "pending-reference-official-urls.md"

UA = "Mozilla/5.0 CodexDRBot/1.0"
TIMEOUT = 20
MAX_BYTES = 120 * 1024 * 1024
SLEEP = 0.12


def slugify(s: str, maxlen: int = 90) -> str:
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return (s[:maxlen].rstrip("-") or "paper")


def clean_doi(doi: str) -> str:
    doi = (doi or "").strip()
    doi = re.sub(r"^https?://(dx\.)?doi\.org/", "", doi, flags=re.I)
    return doi


def http_get(url: str, accept: str = "*/*") -> Tuple[Optional[bytes], str, str, int, str]:
    req = Request(url, headers={"User-Agent": UA, "Accept": accept})
    try:
        with urlopen(req, timeout=TIMEOUT) as r:
            data = r.read(MAX_BYTES + 1)
            if len(data) > MAX_BYTES:
                return None, r.geturl(), r.headers.get("Content-Type", ""), getattr(r, "status", 200), "too_large"
            return data, r.geturl(), r.headers.get("Content-Type", ""), getattr(r, "status", 200), ""
    except HTTPError as e:
        return None, url, "", e.code, f"http_{e.code}"
    except URLError as e:
        return None, url, "", 0, f"url_error:{e.reason}"
    except Exception as e:
        return None, url, "", 0, f"err:{type(e).__name__}"


def looks_pdf(data: bytes, ct: str) -> bool:
    if not data:
        return False
    if data[:5] == b"%PDF-":
        return True
    return "application/pdf" in (ct or "").lower() and data.startswith(b"%PDF")


def parse_pdf_links(base_url: str, html_text: str) -> List[str]:
    out = []
    for m in re.finditer(r'href=["\']([^"\']+)["\']', html_text, flags=re.I):
        u = m.group(1).strip()
        if not u:
            continue
        if ".pdf" in u.lower() or "download" in u.lower() or "pdf" in u.lower():
            out.append(urljoin(base_url, u))
    seen, uniq = set(), []
    for u in out:
        if u not in seen:
            seen.add(u)
            uniq.append(u)
    return uniq[:20]


def try_download(url: str, out_file: Path) -> Tuple[bool, str, str]:
    data, final, ct, status, err = http_get(url, accept="application/pdf,text/html,*/*")
    time.sleep(SLEEP)
    if not data or status >= 400:
        return False, final, err or f"http_{status}"
    if looks_pdf(data, ct):
        out_file.parent.mkdir(parents=True, exist_ok=True)
        out_file.write_bytes(data)
        return True, final, ""
    html = data.decode("utf-8", errors="ignore")
    for u in parse_pdf_links(final, html):
        d2, f2, ct2, s2, e2 = http_get(u, accept="application/pdf,*/*")
        time.sleep(SLEEP)
        if d2 and s2 < 400 and looks_pdf(d2, ct2):
            out_file.parent.mkdir(parents=True, exist_ok=True)
            out_file.write_bytes(d2)
            return True, f2, ""
    return False, final, "no_pdf_content"


def semsch_pdf_by_doi(doi: str) -> Optional[str]:
    url = f"https://api.semanticscholar.org/graph/v1/paper/DOI:{quote(doi)}?fields=title,openAccessPdf,url"
    data, _, _, status, _ = http_get(url, accept="application/json")
    time.sleep(SLEEP)
    if not data or status >= 400:
        return None
    try:
        obj = json.loads(data.decode("utf-8", errors="ignore"))
    except Exception:
        return None
    oap = (obj.get("openAccessPdf") or {}).get("url") if isinstance(obj, dict) else None
    return oap


def semsch_pdf_by_title(title: str) -> Optional[str]:
    url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={quote(title)}&limit=3&fields=title,openAccessPdf,url"
    data, _, _, status, _ = http_get(url, accept="application/json")
    time.sleep(SLEEP)
    if not data or status >= 400:
        return None
    try:
        obj = json.loads(data.decode("utf-8", errors="ignore"))
    except Exception:
        return None
    items = obj.get("data", []) if isinstance(obj, dict) else []
    if not items:
        return None
    # take first with openAccessPdf
    for it in items:
        oap = (it.get("openAccessPdf") or {}).get("url") if isinstance(it, dict) else None
        if oap:
            return oap
    return None


def openalex_links_by_doi(doi: str) -> List[str]:
    api = f"https://api.openalex.org/works/{quote('https://doi.org/' + doi, safe='')}"
    data, _, _, status, _ = http_get(api, accept="application/json")
    time.sleep(SLEEP)
    if not data or status >= 400:
        return []
    try:
        obj = json.loads(data.decode("utf-8", errors="ignore"))
    except Exception:
        return []
    return extract_openalex_urls(obj)


def openalex_links_by_title(title: str) -> List[str]:
    api = f"https://api.openalex.org/works?search={quote(title)}&per-page=3"
    data, _, _, status, _ = http_get(api, accept="application/json")
    time.sleep(SLEEP)
    if not data or status >= 400:
        return []
    try:
        obj = json.loads(data.decode("utf-8", errors="ignore"))
    except Exception:
        return []
    items = obj.get("results", []) if isinstance(obj, dict) else []
    out: List[str] = []
    for it in items[:2]:
        out.extend(extract_openalex_urls(it))
    # dedupe
    seen=set(); uniq=[]
    for u in out:
        if u and u not in seen:
            seen.add(u); uniq.append(u)
    return uniq[:10]


def extract_openalex_urls(obj: dict) -> List[str]:
    urls=[]
    if not isinstance(obj, dict):
        return urls
    oa=obj.get("open_access") or {}
    if isinstance(oa, dict) and oa.get("oa_url"):
        urls.append(oa.get("oa_url"))
    for loc in obj.get("locations") or []:
        if not isinstance(loc, dict):
            continue
        u=loc.get("pdf_url") or loc.get("landing_page_url")
        if u: urls.append(u)
    return urls


def crossref_urls(doi: str) -> List[str]:
    api = f"https://api.crossref.org/works/{quote(doi)}"
    data, _, _, status, _ = http_get(api, accept="application/json")
    time.sleep(SLEEP)
    if not data or status >= 400:
        return []
    try:
        obj = json.loads(data.decode("utf-8", errors="ignore"))
    except Exception:
        return []
    msg = (obj.get("message") or {}) if isinstance(obj, dict) else {}
    out=[]
    if msg.get("URL"):
        out.append(msg["URL"])
    for link in msg.get("link") or []:
        if isinstance(link, dict) and link.get("URL"):
            out.append(link["URL"])
    return out[:10]


def build_official_urls(title: str, doi: str) -> List[str]:
    out=[]
    d=clean_doi(doi)
    if d:
        out.append(f"https://doi.org/{d}")
        if d.startswith("10.1109/"):
            out.append(f"https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText={quote(d)}")
        if d.startswith("10.1145/"):
            out.append(f"https://dl.acm.org/doi/{d}")
        if d.startswith("10.1016/"):
            out.append(f"https://www.sciencedirect.com/search?qs={quote(d)}")
        if d.startswith("10.1111/"):
            out.append(f"https://onlinelibrary.wiley.com/doi/{d}")
        if d.startswith("10.1038/"):
            out.append(f"https://www.nature.com/search?q={quote(d)}")
        if d.startswith("10.1126/"):
            out.append(f"https://www.science.org/action/doSearch?AllField={quote(d)}")
        out.extend(crossref_urls(d))
        out.extend(openalex_links_by_doi(d))
    out.extend(openalex_links_by_title(title))
    # generic official searches
    out.append(f"https://scholar.google.com/scholar?q={quote(title)}")
    out.append(f"https://ieeexplore.ieee.org/search/searchresult.jsp?queryText={quote(title)}")
    out.append(f"https://dl.acm.org/action/doSearch?AllField={quote(title)}")
    # dedupe
    seen=set(); uniq=[]
    for u in out:
        if u and u not in seen:
            seen.add(u); uniq.append(u)
    return uniq[:12]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", type=int, default=0, help="start index in missing list (0-based)")
    ap.add_argument("--count", type=int, default=0, help="number of rows to process (0 means all)")
    args = ap.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    miss = list(csv.DictReader(MISSING_CSV.open(encoding="utf-8")))
    total_missing = len(miss)
    start = max(0, args.start)
    end = total_missing if args.count <= 0 else min(total_missing, start + args.count)
    miss = miss[start:end]

    suffix = f".part-{start}-{end}"
    out_retry_log = OUT_RETRY_LOG.with_name(OUT_RETRY_LOG.stem + suffix + OUT_RETRY_LOG.suffix)
    out_still_missing = OUT_STILL_MISSING.with_name(OUT_STILL_MISSING.stem + suffix + OUT_STILL_MISSING.suffix)
    out_official = OUT_OFFICIAL.with_name(OUT_OFFICIAL.stem + suffix + OUT_OFFICIAL.suffix)
    out_official_md = OUT_OFFICIAL_MD.with_name(OUT_OFFICIAL_MD.stem + suffix + OUT_OFFICIAL_MD.suffix)

    retry_logs=[]
    still=[]

    for i, r in enumerate(miss, 1):
        cid=r.get("candidate_id","")
        title=(r.get("paper_title","") or "").strip()
        year=(r.get("year","") or "").strip()
        doi=clean_doi(r.get("doi","") or "")
        out_file = OUT_DIR / f"{cid}-{slugify((year+'-' if year else '')+title)}.pdf"

        if out_file.exists() and out_file.stat().st_size > 1000:
            retry_logs.append({**r, "retry_status":"found_existing", "retry_url":"", "retry_source":"existing", "retry_error":""})
            continue

        candidates=[]
        if doi:
            sp=semsch_pdf_by_doi(doi)
            if sp: candidates.append(("semanticscholar_doi", sp))
            for u in openalex_links_by_doi(doi):
                candidates.append(("openalex_doi", u))
            for u in crossref_urls(doi):
                candidates.append(("crossref_doi", u))
            candidates.append(("doi", f"https://doi.org/{doi}"))
        sp2=semsch_pdf_by_title(title)
        if sp2: candidates.append(("semanticscholar_title", sp2))
        for u in openalex_links_by_title(title):
            candidates.append(("openalex_title", u))

        # unique
        seen=set(); uniq=[]
        for src,u in candidates:
            if u not in seen:
                seen.add(u); uniq.append((src,u))

        found=False
        last_err="no_candidate_url"
        last_url=""
        last_src=""
        for src,u in uniq:
            ok,resolved,err=try_download(u,out_file)
            last_url=resolved or u
            last_src=src
            if ok:
                retry_logs.append({**r, "retry_status":"found", "retry_url":last_url, "retry_source":src, "retry_error":""})
                found=True
                break
            last_err=err or "download_failed"

        if not found:
            retry_logs.append({**r, "retry_status":"missing", "retry_url":last_url, "retry_source":last_src, "retry_error":last_err})
            still.append(r)

        if i % 15 == 0:
            print(f"retry progress {i}/{len(miss)}")

    # write retry log
    base_fields=list(miss[0].keys()) if miss else []
    log_fields=base_fields + ["retry_status","retry_url","retry_source","retry_error"]
    with out_retry_log.open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=log_fields)
        w.writeheader()
        for rr in retry_logs:
            w.writerow({k: rr.get(k, "") for k in log_fields})

    with out_still_missing.open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=base_fields)
        w.writeheader()
        for rr in still:
            w.writerow({k: rr.get(k, "") for k in base_fields})

    # official URL suggestions for still missing
    off_fields=["candidate_id","paper_title","year","doi","official_url_1","official_url_2","official_url_3","official_url_4","official_url_5","official_url_6","official_url_7","official_url_8","official_url_9","official_url_10","official_url_11","official_url_12"]
    with out_official.open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=off_fields)
        w.writeheader()
        for rr in still:
            urls=build_official_urls((rr.get("paper_title") or "").strip(), clean_doi(rr.get("doi") or ""))
            row={"candidate_id":rr.get("candidate_id",""),"paper_title":rr.get("paper_title",""),"year":rr.get("year",""),"doi":clean_doi(rr.get("doi") or "")}
            for i,u in enumerate(urls[:12],1):
                row[f"official_url_{i}"]=u
            w.writerow(row)

    with out_official_md.open("w",encoding="utf-8") as f:
        f.write("# Official URLs For Still-Missing PDFs\n\n")
        f.write(f"- Still missing after retry: `{len(still)}`\n")
        f.write(f"- CSV: `builder/evidence/pending-reference-official-urls.csv`\n\n")
        f.write("| # | Candidate | Year | Title | URL 1 | URL 2 |\n")
        f.write("|---:|---|---:|---|---|---|\n")
        for i,rr in enumerate(still,1):
            urls=build_official_urls((rr.get("paper_title") or "").strip(), clean_doi(rr.get("doi") or ""))
            u1=(urls[0] if urls else "").replace("|","\\|")
            u2=(urls[1] if len(urls)>1 else "").replace("|","\\|")
            t=(rr.get("paper_title") or "").replace("|","\\|")
            f.write(f"| {i} | `{rr.get('candidate_id','')}` | {rr.get('year','')} | {t} | {u1} | {u2} |\n")

    print(
        f"wrote {out_retry_log.relative_to(ROOT)}, {out_still_missing.relative_to(ROOT)}, "
        f"{out_official.relative_to(ROOT)}, {out_official_md.relative_to(ROOT)} "
        f"(batch={start}:{end}, retry_total={len(miss)}, still_missing={len(still)})"
    )


if __name__ == "__main__":
    main()
