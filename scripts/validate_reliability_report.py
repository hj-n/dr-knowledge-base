#!/usr/bin/env python3
"""Validate that a report text contains the required reliability-report contract keys.

Usage:
  python scripts/validate_reliability_report.py <report_file>
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REQUIRED_KEYS = [
    "primary_task_axis",
    "axis_confidence",
    "task_confirmation_quote",
    "preprocessing_profile_id",
    "distance_metric",
    "frozen_preprocessing_signature",
    "candidate_techniques",
    "candidate_metrics",
    "warning_gate_result",
    "candidate_score_table",
    "selected_configuration",
    "selection_status",
    "initialization_mode",
    "initialization_method",
    "stability_status",
    "best_params",
    "optimization_trace",
    "seed_sensitivity_summary",
    "guardrail_metric_summary",
    "visual_artifacts",
    "final_explanation",
    "plain_language_summary",
    "term_explanations",
    "final_configuration_for_users",
    "source_note_links",
    "residual_risk_statement",
    "recommendation_status",
]

STATUS_VALUES = {
    "selection_status": {"accepted", "provisional", "exploratory"},
    "recommendation_status": {"accepted", "provisional", "exploratory", "contested"},
    "axis_confidence": {"high", "medium", "low"},
    "warning_gate_result": {"pass", "fail", "unknown"},
    "stability_status": {"stable", "unstable"},
}


def find_key(text: str, key: str) -> bool:
    pattern = rf"(?mi)^\s*{re.escape(key)}\s*:"
    return bool(re.search(pattern, text))


def read_value(text: str, key: str) -> str | None:
    pattern = rf"(?mi)^\s*{re.escape(key)}\s*:\s*(.+)$"
    m = re.search(pattern, text)
    if not m:
        return None
    return m.group(1).strip().strip("`\"")


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/validate_reliability_report.py <report_file>")
        return 2

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"ERROR: file not found: {path}")
        return 2

    text = path.read_text(encoding="utf-8", errors="replace")

    missing = [k for k in REQUIRED_KEYS if not find_key(text, k)]
    invalid = []
    for key, allowed in STATUS_VALUES.items():
        value = read_value(text, key)
        if value is None:
            continue
        if value not in allowed:
            invalid.append((key, value, sorted(allowed)))

    if missing:
        print("MISSING_KEYS")
        for k in missing:
            print(f"- {k}")

    if invalid:
        print("INVALID_VALUES")
        for key, value, allowed in invalid:
            print(f"- {key}: '{value}' not in {allowed}")

    if missing or invalid:
        return 1

    print("OK: report satisfies required key contract")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
