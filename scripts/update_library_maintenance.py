#!/usr/bin/env python3
"""Refresh maintenance snapshots for technique execution libraries.

Reads:
  - builder/evidence/technique-execution-map.csv
Writes:
  - builder/evidence/library-maintenance.csv
"""

from __future__ import annotations

import csv
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import requests

ROOT = Path(__file__).resolve().parents[1]
MAP_CSV = ROOT / "builder" / "evidence" / "technique-execution-map.csv"
OUT_CSV = ROOT / "builder" / "evidence" / "library-maintenance.csv"

GITHUB_RE = re.compile(r"https?://github\.com/([^/]+)/([^/#?]+)")
PYPI_RE = re.compile(r"https?://pypi\.org/project/([^/]+)/?")


@dataclass
class LibrarySnapshot:
    repo_url: str = ""
    pypi_url: str = ""
    last_commit: Optional[datetime] = None
    repo_updated: Optional[datetime] = None
    open_issues: Optional[int] = None
    stars: Optional[int] = None
    archived: Optional[bool] = None
    last_release: Optional[datetime] = None
    package_name: str = ""
    notes: str = ""


_GITHUB_CACHE: dict[str, LibrarySnapshot] = {}
_PYPI_CACHE: dict[str, LibrarySnapshot] = {}


def parse_dt(value: str | None) -> Optional[datetime]:
    if not value:
        return None
    value = value.replace("Z", "+00:00")
    try:
        return datetime.fromisoformat(value).astimezone(timezone.utc)
    except ValueError:
        return None


def github_api(repo_url: str) -> LibrarySnapshot:
    if repo_url in _GITHUB_CACHE:
        cached = _GITHUB_CACHE[repo_url]
        return LibrarySnapshot(**cached.__dict__)

    snap = LibrarySnapshot(repo_url=repo_url)
    m = GITHUB_RE.match(repo_url.strip())
    if not m:
        snap.notes = "invalid_github_url"
        _GITHUB_CACHE[repo_url] = snap
        return LibrarySnapshot(**snap.__dict__)

    owner, repo = m.group(1), m.group(2)
    base = f"https://api.github.com/repos/{owner}/{repo}"
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "dr-kb-maintenance-bot"}

    try:
        r = requests.get(base, headers=headers, timeout=20)
    except requests.RequestException as exc:
        snap.notes = f"github_request_error:{exc.__class__.__name__}"
        _GITHUB_CACHE[repo_url] = snap
        return LibrarySnapshot(**snap.__dict__)

    if r.status_code != 200:
        snap.notes = f"github_status:{r.status_code}"
        _GITHUB_CACHE[repo_url] = snap
        return LibrarySnapshot(**snap.__dict__)

    data = r.json()
    snap.last_commit = parse_dt(data.get("pushed_at"))
    snap.repo_updated = parse_dt(data.get("updated_at"))
    snap.open_issues = data.get("open_issues_count")
    snap.stars = data.get("stargazers_count")
    snap.archived = data.get("archived")

    try:
        rr = requests.get(f"{base}/releases/latest", headers=headers, timeout=20)
        if rr.status_code == 200:
            rel = rr.json()
            snap.last_release = parse_dt(rel.get("published_at"))
    except requests.RequestException:
        pass

    _GITHUB_CACHE[repo_url] = snap
    return LibrarySnapshot(**snap.__dict__)


def pypi_api(pypi_url: str) -> LibrarySnapshot:
    if pypi_url in _PYPI_CACHE:
        cached = _PYPI_CACHE[pypi_url]
        return LibrarySnapshot(**cached.__dict__)

    snap = LibrarySnapshot(pypi_url=pypi_url)
    m = PYPI_RE.match(pypi_url.strip())
    if not m:
        snap.notes = "invalid_pypi_url"
        _PYPI_CACHE[pypi_url] = snap
        return LibrarySnapshot(**snap.__dict__)

    pkg = m.group(1)
    snap.package_name = pkg
    api = f"https://pypi.org/pypi/{pkg}/json"

    try:
        r = requests.get(api, timeout=20)
    except requests.RequestException as exc:
        snap.notes = f"pypi_request_error:{exc.__class__.__name__}"
        _PYPI_CACHE[pypi_url] = snap
        return LibrarySnapshot(**snap.__dict__)

    if r.status_code != 200:
        snap.notes = f"pypi_status:{r.status_code}"
        return snap

    data = r.json()
    release_dates: list[datetime] = []
    for files in data.get("releases", {}).values():
        for f in files or []:
            dt = parse_dt(f.get("upload_time_iso_8601") or f.get("upload_time"))
            if dt:
                release_dates.append(dt)

    if release_dates:
        snap.last_release = max(release_dates)

    _PYPI_CACHE[pypi_url] = snap
    return LibrarySnapshot(**snap.__dict__)


def classify_status(last_commit: Optional[datetime], last_release: Optional[datetime], archived: Optional[bool]) -> str:
    if archived:
        return "risk"

    candidates = [dt for dt in [last_commit, last_release] if dt is not None]
    if not candidates:
        return "risk"

    newest = max(candidates)
    days = (datetime.now(timezone.utc) - newest).days

    if days <= 180:
        return "active"
    if days <= 540:
        return "watch"
    return "risk"


def fmt(dt: Optional[datetime]) -> str:
    return dt.date().isoformat() if dt else ""


def pick_snapshot(repo_url: str, pypi_url: str) -> LibrarySnapshot:
    repo_snap = github_api(repo_url) if repo_url else LibrarySnapshot()
    pypi_snap = pypi_api(pypi_url) if pypi_url else LibrarySnapshot()

    merged = LibrarySnapshot(
        repo_url=repo_snap.repo_url,
        pypi_url=pypi_snap.pypi_url,
        last_commit=repo_snap.last_commit,
        repo_updated=repo_snap.repo_updated,
        open_issues=repo_snap.open_issues,
        stars=repo_snap.stars,
        archived=repo_snap.archived,
        last_release=repo_snap.last_release or pypi_snap.last_release,
        package_name=pypi_snap.package_name,
        notes=";".join(x for x in [repo_snap.notes, pypi_snap.notes] if x),
    )
    return merged


def main() -> int:
    if not MAP_CSV.exists():
        raise FileNotFoundError(f"missing mapping file: {MAP_CSV}")

    rows = []
    checked_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    with MAP_CSV.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            primary = pick_snapshot(row.get("github_url", ""), row.get("pypi_url", ""))
            fallback = pick_snapshot(row.get("fallback_github_url", ""), row.get("fallback_pypi_url", ""))

            primary_status = classify_status(primary.last_commit, primary.last_release, primary.archived)
            fallback_status = classify_status(fallback.last_commit, fallback.last_release, fallback.archived)

            rows.append(
                {
                    "technique_id": row["technique_id"],
                    "primary_library": row.get("primary_library", ""),
                    "primary_repo_url": row.get("github_url", ""),
                    "primary_pypi_url": row.get("pypi_url", ""),
                    "primary_package_name": primary.package_name,
                    "primary_last_commit_date": fmt(primary.last_commit),
                    "primary_last_release_date": fmt(primary.last_release),
                    "primary_repo_updated_date": fmt(primary.repo_updated),
                    "primary_open_issues": "" if primary.open_issues is None else str(primary.open_issues),
                    "primary_stars": "" if primary.stars is None else str(primary.stars),
                    "primary_status": primary_status,
                    "fallback_library": row.get("fallback_library", ""),
                    "fallback_repo_url": row.get("fallback_github_url", ""),
                    "fallback_pypi_url": row.get("fallback_pypi_url", ""),
                    "fallback_package_name": fallback.package_name,
                    "fallback_last_commit_date": fmt(fallback.last_commit),
                    "fallback_last_release_date": fmt(fallback.last_release),
                    "fallback_repo_updated_date": fmt(fallback.repo_updated),
                    "fallback_open_issues": "" if fallback.open_issues is None else str(fallback.open_issues),
                    "fallback_stars": "" if fallback.stars is None else str(fallback.stars),
                    "fallback_status": fallback_status,
                    "notes": ";".join(x for x in [primary.notes, fallback.notes] if x),
                    "checked_at": checked_at,
                }
            )

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "technique_id",
        "primary_library",
        "primary_repo_url",
        "primary_pypi_url",
        "primary_package_name",
        "primary_last_commit_date",
        "primary_last_release_date",
        "primary_repo_updated_date",
        "primary_open_issues",
        "primary_stars",
        "primary_status",
        "fallback_library",
        "fallback_repo_url",
        "fallback_pypi_url",
        "fallback_package_name",
        "fallback_last_commit_date",
        "fallback_last_release_date",
        "fallback_repo_updated_date",
        "fallback_open_issues",
        "fallback_stars",
        "fallback_status",
        "notes",
        "checked_at",
    ]

    with OUT_CSV.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"wrote {OUT_CSV.relative_to(ROOT)} ({len(rows)} rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
