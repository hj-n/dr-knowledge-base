#!/usr/bin/env python3
"""Validate Python code files against the KB optimizer-family policy.

Usage:
  python scripts/validate_bayes_opt_policy.py <file_or_dir> [<file_or_dir> ...]

Policy:
- must use bayes_opt / BayesianOptimization
- must not use grid/random/manual sweep optimizer patterns
"""

from __future__ import annotations

import ast
import re
import sys
from pathlib import Path

BANNED_TEXT_TERMS = [
    "grid search",
    "grid-search",
    "random search",
    "random-search",
    "manual sweep",
    "parameter sweep",
]

BANNED_CALL_SUFFIXES = {
    "GridSearchCV",
    "RandomizedSearchCV",
    "ParameterGrid",
    "product",  # itertools.product
}

SUSPECT_LOOP_VAR_SUFFIXES = ("_cfg", "_cfgs", "_values", "_grid", "_search_space")


def iter_py_files(paths: list[str]) -> list[Path]:
    out: list[Path] = []
    for raw in paths:
        p = Path(raw)
        if not p.exists():
            continue
        if p.is_file() and p.suffix == ".py":
            out.append(p)
            continue
        if p.is_dir():
            out.extend(sorted(fp for fp in p.rglob("*.py") if fp.is_file()))
    return sorted(set(out))


def call_name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        left = call_name(node.value)
        return f"{left}.{node.attr}" if left else node.attr
    return ""


def has_bayes_opt(text: str, tree: ast.AST) -> bool:
    low = text.lower()
    if "bayes_opt" in low or "bayesianoptimization" in low:
        return True

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name == "bayes_opt":
                    return True
        elif isinstance(node, ast.ImportFrom):
            if node.module == "bayes_opt":
                return True
    return False


def scan_file(path: Path) -> list[str]:
    issues: list[str] = []
    text = path.read_text(encoding="utf-8", errors="replace")
    low = text.lower()

    try:
        tree = ast.parse(text)
    except SyntaxError as exc:
        return [f"{path}: syntax_error:{exc.msg} (line {exc.lineno})"]

    if not has_bayes_opt(text, tree):
        issues.append(f"{path}: missing_bayes_opt")

    for term in BANNED_TEXT_TERMS:
        if term in low:
            issues.append(f"{path}: banned_term:{term}")

    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = call_name(node.func)
            short = name.split(".")[-1]
            if short in BANNED_CALL_SUFFIXES:
                if short == "product" and not name.endswith("product"):
                    continue
                issues.append(f"{path}: banned_call:{name}")

        if isinstance(node, ast.For):
            if isinstance(node.iter, (ast.List, ast.Tuple, ast.Set)):
                issues.append(f"{path}: manual_sweep:for_over_literal_container(line={node.lineno})")
            elif isinstance(node.iter, ast.Name):
                if node.iter.id.endswith(SUSPECT_LOOP_VAR_SUFFIXES):
                    issues.append(f"{path}: manual_sweep:for_over_{node.iter.id}(line={node.lineno})")

        if isinstance(node, ast.Assign):
            for tgt in node.targets:
                if isinstance(tgt, ast.Name) and tgt.id.endswith(SUSPECT_LOOP_VAR_SUFFIXES):
                    if isinstance(node.value, (ast.List, ast.Tuple, ast.Set)):
                        issues.append(f"{path}: manual_sweep:suspect_table_{tgt.id}(line={node.lineno})")

    return issues


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python scripts/validate_bayes_opt_policy.py <file_or_dir> [<file_or_dir> ...]")
        return 2

    files = iter_py_files(sys.argv[1:])
    if not files:
        print("ERROR: no Python files found")
        return 2

    all_issues: list[str] = []
    for f in files:
        all_issues.extend(scan_file(f))

    if all_issues:
        print("BAYES_OPT_POLICY_VALIDATION_FAILED")
        for issue in all_issues:
            print(f"- {issue}")
        return 1

    print(f"OK: bayes-opt policy validation passed ({len(files)} files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
