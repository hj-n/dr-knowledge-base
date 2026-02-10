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
    "aligned_candidate_coverage",
    "selected_configuration",
    "selection_status",
    "initialization_mode",
    "initialization_method",
    "stability_status",
    "optimizer",
    "best_params",
    "optimization_trace",
    "seed_sensitivity_summary",
    "safety_check_summary",
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
    "aligned_candidate_coverage": {"full", "partial_with_reason"},
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
    "guardrail metric",
    "guardrail",
    "primary metric",
    "primary metric + guardrail metric",
    "candidate score table",
    "selection_status",
    "axis_confidence",
]

BANNED_USER_METRIC_IDS = [
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

BANNED_USER_INTERFACE_TERMS = [
    "dr kb",
    "dr knowledge base",
    "context7",
    "this repo",
    "workflow step",
    "contract validator",
]

BANNED_USER_REFERENCE_TOKENS = [
    "papers/notes/",
    "docs/",
    "llms.txt",
    "github.com/hj-n/dr-knowledge-base",
    "dr-knowledge-base/blob/",
]

BANNED_USER_REFERENCE_REGEX = [
    r"https?://[^\s)]+\.md\b",
    r"\[[^\]]+\]\([^)]+/papers/notes/[^)]+\)",
    r"\[[^\]]+\]\([^)]+/docs/[^)]+\)",
]

BANNED_USER_MAPPING_STYLE_PHRASES = [
    "task->metric",
    "task→metric",
    "task-to-metric",
    "task to metric mapping",
    "primary = [",
    "primary:[",
    "safety check = [",
    "safety check:[",
]

BANNED_USER_MAPPING_STYLE_REGEX = [
    r"\b(primary|safety check)\s*(=|:)\s*\[[^\]]+\]",
    r"\b(task\s*(->|→)\s*metric|task-?to-?metric)\b",
    r"\[\s*\"[a-z0-9_]+\"(\s*,\s*\"[a-z0-9_]+\")+\s*\]",
]

BANNED_USER_INTERNAL_KEYS = [
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

BANNED_USER_CODE_TOKENS = [
    "TASK_METRIC_BUNDLES",
    "task_lock",
    "preprocessing_config",
    "recommendation_status",
    "report_contract_validation",
    "primary_task_axis",
    "task_confirmation_quote",
    "warning_gate_result",
    "warning_gate_notes",
    "candidate_metrics",
    "candidate_techniques",
    "candidate_score_table",
    "selected_configuration",
    "metric_bundle",
    "selection_status",
    "axis_confidence",
    "frozen_preprocessing_signature",
]

ALLOWED_OPTIMIZER = "bayes_opt"

BANNED_USER_OPTIMIZATION_TERMS = [
    "grid search",
    "grid-search",
    "random search",
    "random-search",
    "parameter sweep",
    "manual sweep",
    "gridsearchcv",
    "randomizedsearchcv",
]

BAYES_OPT_CODE_HINTS = [
    "from bayes_opt",
    "import bayes_opt",
    "bayesianoptimization(",
]

ZADU_CODE_HINTS = [
    "zadu",
    "from zadu",
]

DR_STEP_CODE_HINTS = [
    "fit_transform(",
    ".fit(",
]

BANNED_USER_CODE_JARGON_TERMS = [
    "guardrail",
    "metric bundle",
    "task axis",
    "warning gate",
    "primary metric",
    "selection_status",
    "axis_confidence",
]

MAX_USER_CODE_NONEMPTY_LINES = 25


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

    optimizer_value = read_value(text, "optimizer")
    optimizer_violation = None
    if optimizer_value is not None and optimizer_value != ALLOWED_OPTIMIZER:
        optimizer_violation = (optimizer_value, ALLOWED_OPTIMIZER)

    jargon_violations = []
    for key in USER_TEXT_KEYS:
        value = read_value(text, key)
        if not value:
            continue
        lv = value.lower()
        for term in BANNED_USER_JARGON:
            if term in lv:
                jargon_violations.append((key, term, value))

    metric_id_violations = []
    for key in USER_TEXT_KEYS:
        value = read_value(text, key)
        if not value:
            continue
        lv = value.lower()
        for token in BANNED_USER_METRIC_IDS:
            if re.search(rf"\b{re.escape(token)}\b", lv):
                metric_id_violations.append((key, token, value))

    interface_violations = []
    for key in USER_TEXT_KEYS:
        value = read_value(text, key)
        if not value:
            continue
        lv = value.lower()
        for term in BANNED_USER_INTERFACE_TERMS:
            if term in lv:
                interface_violations.append((key, term, value))

    reference_leak_violations = []
    for key in USER_TEXT_KEYS:
        value = read_value(text, key)
        if not value:
            continue
        lv = value.lower()
        for term in BANNED_USER_REFERENCE_TOKENS:
            if term in lv:
                reference_leak_violations.append((key, term, value))
        for pattern in BANNED_USER_REFERENCE_REGEX:
            if re.search(pattern, lv):
                reference_leak_violations.append((key, pattern, value))

    mapping_style_violations = []
    for key in USER_TEXT_KEYS:
        value = read_value(text, key)
        if not value:
            continue
        lv = value.lower()
        for term in BANNED_USER_MAPPING_STYLE_PHRASES:
            if term in lv:
                mapping_style_violations.append((key, term, value))
        for pattern in BANNED_USER_MAPPING_STYLE_REGEX:
            if re.search(pattern, lv):
                mapping_style_violations.append((key, pattern, value))

    internal_key_violations = []
    for key in USER_TEXT_KEYS:
        value = read_value(text, key)
        if not value:
            continue
        lv = value.lower()
        for token in BANNED_USER_INTERNAL_KEYS:
            if re.search(rf"\b{re.escape(token)}\b", lv):
                internal_key_violations.append((key, token, value))

    user_optimization_violations = []
    for key in USER_TEXT_KEYS:
        value = read_value(text, key)
        if not value:
            continue
        lv = value.lower()
        for term in BANNED_USER_OPTIMIZATION_TERMS:
            if term in lv:
                user_optimization_violations.append((key, term, value))

    code_leak_violations = []
    code_required_component_violations = []
    code_minimality_violations = []
    code_snippet = read_value(text, "user_code_snippet")
    if code_snippet:
        snippet = code_snippet
        snippet_lower = snippet.lower()
        for token in BANNED_USER_CODE_TOKENS:
            if token in snippet:
                code_leak_violations.append((token, snippet))
        for term in BANNED_USER_OPTIMIZATION_TERMS:
            if term in snippet_lower:
                code_leak_violations.append((term, snippet))

        if not any(token in snippet_lower for token in BAYES_OPT_CODE_HINTS):
            code_required_component_violations.append(("bayes_opt", snippet))
        if not any(token in snippet_lower for token in ZADU_CODE_HINTS):
            code_required_component_violations.append(("zadu", snippet))
        if not any(token in snippet_lower for token in DR_STEP_CODE_HINTS):
            code_required_component_violations.append(("dr_fit_step", snippet))

        nonempty_lines = [ln for ln in snippet.splitlines() if ln.strip()]
        if len(nonempty_lines) > MAX_USER_CODE_NONEMPTY_LINES:
            code_minimality_violations.append(
                (f"too_many_lines:{len(nonempty_lines)}", snippet)
            )

        for term in BANNED_USER_CODE_JARGON_TERMS:
            if term in snippet_lower:
                code_minimality_violations.append((f"internal_jargon:{term}", snippet))

    if missing:
        print("MISSING_KEYS")
        for k in missing:
            print(f"- {k}")

    if invalid:
        print("INVALID_VALUES")
        for key, value, allowed in invalid:
            print(f"- {key}: '{value}' not in {allowed}")

    if optimizer_violation:
        print("OPTIMIZER_POLICY_VIOLATION")
        print(f"- optimizer: '{optimizer_violation[0]}' (allowed: '{optimizer_violation[1]}')")

    if jargon_violations:
        print("USER_JARGON_VIOLATIONS")
        for key, term, value in jargon_violations:
            print(f"- {key}: contains forbidden term '{term}' in '{value}'")

    if metric_id_violations:
        print("USER_METRIC_ABBREVIATION_VIOLATIONS")
        for key, token, value in metric_id_violations:
            print(f"- {key}: contains metric ID/abbreviation '{token}' in '{value}'")

    if interface_violations:
        print("USER_INTERFACE_LEAK_VIOLATIONS")
        for key, term, value in interface_violations:
            print(f"- {key}: contains forbidden interface term '{term}' in '{value}'")

    if reference_leak_violations:
        print("USER_REFERENCE_LEAK_VIOLATIONS")
        for key, term, value in reference_leak_violations:
            print(f"- {key}: contains forbidden KB/file reference '{term}' in '{value}'")

    if mapping_style_violations:
        print("USER_MAPPING_STYLE_LEAK_VIOLATIONS")
        for key, term, value in mapping_style_violations:
            print(f"- {key}: contains forbidden mapping-style phrasing '{term}' in '{value}'")

    if internal_key_violations:
        print("USER_INTERNAL_KEY_LEAK_VIOLATIONS")
        for key, token, value in internal_key_violations:
            print(f"- {key}: contains internal key '{token}' in '{value}'")

    if user_optimization_violations:
        print("USER_OPTIMIZATION_POLICY_VIOLATIONS")
        for key, term, value in user_optimization_violations:
            print(f"- {key}: contains forbidden optimization term '{term}' in '{value}'")

    if code_leak_violations:
        print("USER_CODE_POLICY_LEAK")
        for token, snippet in code_leak_violations:
            print(f"- user_code_snippet: contains internal token '{token}' in '{snippet}'")

    if code_required_component_violations:
        print("USER_CODE_REQUIRED_COMPONENTS_VIOLATIONS")
        for token, snippet in code_required_component_violations:
            print(f"- user_code_snippet: missing required component '{token}' in '{snippet}'")

    if code_minimality_violations:
        print("USER_CODE_MINIMALITY_VIOLATIONS")
        for token, snippet in code_minimality_violations:
            print(f"- user_code_snippet: violates minimality rule '{token}' in '{snippet}'")

    if (
        missing
        or invalid
        or optimizer_violation
        or jargon_violations
        or metric_id_violations
        or interface_violations
        or reference_leak_violations
        or mapping_style_violations
        or internal_key_violations
        or user_optimization_violations
        or code_leak_violations
        or code_required_component_violations
        or code_minimality_violations
    ):
        return 1

    print("OK: report satisfies required key contract")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
