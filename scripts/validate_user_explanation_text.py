#!/usr/bin/env python3
"""Validate plain user-facing text for internal-jargon leakage.

Usage:
  python scripts/validate_user_explanation_text.py <text_file>
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

BANNED_PHRASES = [
    "task axis",
    "task-axis",
    "task lock",
    "lock the task",
    "metric bundle",
    "metric-bundle",
    "bundle scoring",
    "score with bundles",
    "warning gate",
    "preprocessing signature",
    "preprocessing freeze",
    "preprocessing lock",
    "primary metric",
    "guardrail metric",
    "guardrail",
    "candidate score table",
    "selection_status",
    "axis_confidence",
]

BANNED_INTERFACE = [
    "dr kb",
    "dr knowledge base",
    "context7",
    "this repo",
    "workflow step",
    "contract validator",
]

BANNED_REFERENCE_TOKENS = [
    "papers/notes/",
    "docs/",
    "llms.txt",
    "github.com/hj-n/dr-knowledge-base",
    "dr-knowledge-base/blob/",
]

BANNED_REFERENCE_REGEX = [
    r"https?://[^\s)]+\.md\b",
    r"\[[^\]]+\]\([^)]+/papers/notes/[^)]+\)",
    r"\[[^\]]+\]\([^)]+/docs/[^)]+\)",
]

BANNED_MAPPING_STYLE_PHRASES = [
    "task->metric",
    "task→metric",
    "task-to-metric",
    "task to metric mapping",
    "primary = [",
    "primary:[",
    "safety check = [",
    "safety check:[",
]

BANNED_MAPPING_STYLE_REGEX = [
    r"\b(primary|safety check)\s*(=|:)\s*\[[^\]]+\]",
    r"\b(task\s*(->|→)\s*metric|task-?to-?metric)\b",
    r"\[\s*\"[a-z0-9_]+\"(\s*,\s*\"[a-z0-9_]+\")+\s*\]",
]

BANNED_METRIC_IDS = [
    "tnc",
    "nh",
    "nd",
    "mrre",
    "lcmc",
    "ca_tnc",
    "l_tnc",
    "dsc",
    "ivm",
    "c_evm",
    "snc",
    "kl_div",
    "dtm",
    "topo",
    "srho",
    "proc",
    "qnx",
    "spectral_overlap",
]

INTERNAL_KEYS = [
    "primary_task_axis",
    "warning_gate_result",
    "warning_gate_notes",
    "candidate_score_table",
    "selected_configuration",
    "selection_status",
    "axis_confidence",
    "frozen_preprocessing_signature",
    "safety_check_summary",
    "metric_bundle",
]

BANNED_OPTIMIZATION_TERMS = [
    "grid search",
    "grid-search",
    "random search",
    "random-search",
    "parameter sweep",
    "manual sweep",
    "gridsearchcv",
    "randomizedsearchcv",
]

VERBOSITY_WARNING_WORDS = 220

QUESTION_CUE_TERMS = [
    "what",
    "why",
    "how",
    "can i",
    "should i",
    "?",
]


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/validate_user_explanation_text.py <text_file>")
        return 2

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"ERROR: file not found: {path}")
        return 2

    text = path.read_text(encoding="utf-8", errors="replace")
    low = text.lower()

    violations = []
    warnings = []

    for phrase in BANNED_PHRASES:
        if phrase in low:
            violations.append(("BANNED_PHRASE", phrase))

    for phrase in BANNED_INTERFACE:
        if phrase in low:
            violations.append(("INTERFACE_LEAK", phrase))

    for token in BANNED_REFERENCE_TOKENS:
        if token in low:
            violations.append(("REFERENCE_LEAK", token))

    for pattern in BANNED_REFERENCE_REGEX:
        if re.search(pattern, low):
            violations.append(("REFERENCE_LEAK", pattern))

    for phrase in BANNED_MAPPING_STYLE_PHRASES:
        if phrase in low:
            violations.append(("MAPPING_STYLE_LEAK", phrase))

    for pattern in BANNED_MAPPING_STYLE_REGEX:
        if re.search(pattern, low):
            violations.append(("MAPPING_STYLE_LEAK", pattern))

    for token in BANNED_METRIC_IDS:
        if re.search(rf"\b{re.escape(token)}\b", low):
            violations.append(("METRIC_ID_LEAK", token))

    for token in INTERNAL_KEYS:
        if re.search(rf"\b{re.escape(token)}\b", low):
            violations.append(("INTERNAL_KEY_LEAK", token))

    for phrase in BANNED_OPTIMIZATION_TERMS:
        if phrase in low:
            violations.append(("OPTIMIZATION_POLICY_LEAK", phrase))

    word_count = len(re.findall(r"\S+", text))
    is_question_like = any(token in low for token in QUESTION_CUE_TERMS)
    if is_question_like and word_count > VERBOSITY_WARNING_WORDS:
        warnings.append(("POSSIBLE_OVER_VERBOSE_FOR_QUESTION", str(word_count)))

    if violations:
        for kind, token in violations:
            print(f"{kind}: {token}")
        return 1

    for kind, token in warnings:
        print(f"{kind}: {token}")

    print("OK: user-facing text has no blocked internal terms")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
