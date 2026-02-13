#!/usr/bin/env python3
"""Lint user-facing docs for internal-leak patterns."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DOCS_BANNED_PATTERNS = [
    ("internal phrase", re.compile(r"\bIn this repository\b", re.IGNORECASE)),
    ("internal phrase", re.compile(r"\bthis repo\b", re.IGNORECASE)),
    ("internal jargon", re.compile(r"\btask\s+axis\b", re.IGNORECASE)),
    ("internal jargon", re.compile(r"\btask\s+lock\b", re.IGNORECASE)),
    ("internal jargon", re.compile(r"\block\s+the\s+task\b", re.IGNORECASE)),
    ("internal jargon", re.compile(r"\bmetric\s+bundle\b", re.IGNORECASE)),
    ("internal jargon", re.compile(r"\bbundle\s+scoring\b", re.IGNORECASE)),
    ("internal jargon", re.compile(r"\bguardrail\s+metric\b", re.IGNORECASE)),
    ("internal jargon", re.compile(r"\bprimary\s+metric\b", re.IGNORECASE)),
    ("internal jargon", re.compile(r"\bpreprocessing\s+freeze\b", re.IGNORECASE)),
    ("internal jargon", re.compile(r"\bpreprocessing\s+lock\b", re.IGNORECASE)),
    ("internal jargon", re.compile(r"\bsafety\s+check\s+evidence\b", re.IGNORECASE)),
    ("internal phrase", re.compile(r"\bDR\s*KB\b", re.IGNORECASE)),
    ("internal phrase", re.compile(r"\bContext7\b", re.IGNORECASE)),
]

REQUIRED_DOC_FILES = [
    ROOT / "docs" / "workflow" / "quick-answer-mode.md",
]

REQUIRED_LLMS_PHRASES = [
    "Tune with Bayesian optimization (`bayes_opt`) only.",
    "Score reliability with `zadu`.",
    "Always disclose final method and key settings.",
    "Do not justify selections by popularity alone.",
]

WORKFLOW_KEY_LEAKS = [
    "primary_task_axis",
    "warning_gate_result",
    "candidate_score_table",
    "selection_status",
    "axis_confidence",
    "frozen_preprocessing_signature",
]

METRICS_LIB_BANNED = [
    re.compile(r"\btask\s*(->|→)\s*metric\b", re.IGNORECASE),
    re.compile(r"\bprimary\s*:\s*`?[a-z0-9_\-]", re.IGNORECASE),
    re.compile(r"\bsafety\s*check\s*:\s*`?[a-z0-9_\-]", re.IGNORECASE),
    re.compile(r"\bTask-to-Metric Starter Bundles\b", re.IGNORECASE),
]

LLMS_BANNED = [
    re.compile(r"task\s*(->|→)\s*metric", re.IGNORECASE),
    re.compile(r"primary\s*=\s*\[", re.IGNORECASE),
    re.compile(r"safety\s*check\s*=\s*\[", re.IGNORECASE),
    re.compile(r"papers/notes/", re.IGNORECASE),
    re.compile(r"docs/", re.IGNORECASE),
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def check_docs() -> list[str]:
    errors: list[str] = []
    for req in REQUIRED_DOC_FILES:
        if not req.exists():
            errors.append(f"missing required doc file: {req}")

    for path in (ROOT / "docs").rglob("*.md"):
        text = read_text(path)
        for label, pat in DOCS_BANNED_PATTERNS:
            if pat.search(text):
                errors.append(f"{path}: banned {label}: {pat.pattern}")

    for path in list((ROOT / "docs" / "metrics").glob("*.md")) + list((ROOT / "docs" / "techniques").glob("*.md")):
        text = read_text(path)
        if "papers/notes/" in text:
            errors.append(f"{path}: contains internal note-path reference papers/notes/")

    metrics_lib = ROOT / "docs" / "metrics-and-libraries.md"
    text = read_text(metrics_lib)
    for pat in METRICS_LIB_BANNED:
        if pat.search(text):
            errors.append(f"{metrics_lib}: contains banned mapping style: {pat.pattern}")

    workflow_paths = list((ROOT / "docs" / "workflow").glob("*.md")) + [ROOT / "docs" / "intake-question-tree.md", ROOT / "docs" / "task-taxonomy.md"]
    for path in workflow_paths:
        text = read_text(path)
        for token in WORKFLOW_KEY_LEAKS:
            if re.search(rf"\b{re.escape(token)}\b", text):
                errors.append(f"{path}: contains internal key token: {token}")

    return errors


def check_llms() -> list[str]:
    errors: list[str] = []
    path = ROOT / "llms.txt"
    if not path.exists():
        errors.append("llms.txt is missing")
        return errors

    text = read_text(path)
    for pat in LLMS_BANNED:
        if pat.search(text):
            errors.append(f"{path}: contains banned pattern: {pat.pattern}")
    for phrase in REQUIRED_LLMS_PHRASES:
        if phrase not in text:
            errors.append(f"{path}: missing required phrase: {phrase}")
    return errors


def check_context7() -> list[str]:
    errors: list[str] = []
    path = ROOT / "context7.json"
    try:
        cfg = json.loads(read_text(path))
    except Exception as exc:  # pragma: no cover
        return [f"{path}: invalid JSON: {exc}"]

    for key in ["url", "public_key", "include", "exclude"]:
        if key not in cfg:
            errors.append(f"{path}: missing key: {key}")

    include = cfg.get("include", [])
    exclude = cfg.get("exclude", [])
    if "docs/**" not in include:
        errors.append(f"{path}: include must contain docs/**")
    if "papers/notes/**" not in exclude:
        errors.append(f"{path}: exclude must contain papers/notes/**")
    if "papers/raw/**" not in exclude:
        errors.append(f"{path}: exclude must contain papers/raw/**")
    if "docs/reference-coverage.md" not in exclude:
        errors.append(f"{path}: exclude must contain docs/reference-coverage.md")
    return errors


def main() -> int:
    errors = []
    errors.extend(check_docs())
    errors.extend(check_llms())
    errors.extend(check_context7())

    if errors:
        print("USER_LAYER_DOC_LINT_FAILED")
        for err in errors:
            print(f"- {err}")
        return 1

    print("OK: user-layer doc lint passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
