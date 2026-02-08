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
    "technical_explanation",
    "user_explanation",
    "user_goal_restatement",
    "user_what_was_compared",
    "user_why_selected",
    "user_risk_note",
    "user_code_snippet",
    "user_code_reason",
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

USER_TEXT_KEYS = [
    "user_explanation",
    "user_goal_restatement",
    "user_what_was_compared",
    "user_why_selected",
    "user_risk_note",
]

BANNED_USER_JARGON = [
    "task axis",
    "metric bundle",
    "warning gate",
    "preprocessing signature",
    "guardrail metric",
    "candidate score table",
    "selection_status",
    "axis_confidence",
]

BANNED_USER_CODE_TOKENS = [
    "TASK_METRIC_BUNDLES",
    "primary_task_axis",
    "warning_gate_result",
    "metric_bundle",
    "selection_status",
    "axis_confidence",
]


def find_key(text: str, key: str) -> bool:
    pattern = rf"(?mi)^\s*{re.escape(key)}\s*:"
    return bool(re.search(pattern, text))


def read_value(text: str, key: str) -> str | None:
    lines = text.splitlines()
    key_re = re.compile(rf"^\s*{re.escape(key)}\s*:\s*(.*)$", re.IGNORECASE)

    for i, line in enumerate(lines):
        m = key_re.match(line)
        if not m:
            continue
        raw = m.group(1).strip()

        # YAML-like block scalar support:
        # key: |
        #   line1
        #   line2
        if raw in {"|", "|-", ">", ">-"}:
            block = []
            j = i + 1
            while j < len(lines):
                nxt = lines[j]
                if nxt.startswith("  ") or nxt.startswith("\t"):
                    block.append(nxt.lstrip())
                    j += 1
                    continue
                break
            return "\n".join(block).strip()

        return raw.strip("`\"")

    return None


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

    jargon_violations = []
    for key in USER_TEXT_KEYS:
        value = read_value(text, key)
        if not value:
            continue
        lv = value.lower()
        for term in BANNED_USER_JARGON:
            if term in lv:
                jargon_violations.append((key, term, value))

    code_leak_violations = []
    code_snippet = read_value(text, "user_code_snippet")
    if code_snippet:
        snippet = code_snippet
        for token in BANNED_USER_CODE_TOKENS:
            if token in snippet:
                code_leak_violations.append((token, snippet))

    if missing:
        print("MISSING_KEYS")
        for k in missing:
            print(f"- {k}")

    if invalid:
        print("INVALID_VALUES")
        for key, value, allowed in invalid:
            print(f"- {key}: '{value}' not in {allowed}")

    if jargon_violations:
        print("USER_JARGON_VIOLATIONS")
        for key, term, value in jargon_violations:
            print(f"- {key}: contains forbidden term '{term}' in '{value}'")

    if code_leak_violations:
        print("USER_CODE_POLICY_LEAK")
        for token, snippet in code_leak_violations:
            print(f"- user_code_snippet: contains internal token '{token}' in '{snippet}'")

    if missing or invalid or jargon_violations or code_leak_violations:
        return 1

    print("OK: report satisfies required key contract")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
