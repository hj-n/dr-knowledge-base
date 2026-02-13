#!/usr/bin/env python3
"""Validate execution-coverage sections in technique docs."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TECH_DIR = ROOT / "docs" / "techniques"

REQUIRED_HEADERS = [
    "## Implementation Options",
    "## Recommended Library",
    "## Official API / GitHub / PyPI Links",
    "## Minimal Python API Pattern",
    "## Key Parameters for Bayesian Optimization",
    "## Initialization in Practice",
    "## Runtime and Memory Notes",
    "## Common Failure Signs and Fixes",
    "## Minimal Runnable Snippet",
]

BANNED_CODE_TERMS = [
    "guardrail",
    "metric bundle",
    "task axis",
    "warning gate",
]


def section_block(text: str, title: str) -> str:
    idx = text.find(title)
    if idx == -1:
        return ""
    rest = text[idx + len(title) :]
    next_h = re.search(r"\n##\s+", rest)
    if not next_h:
        return rest
    return rest[: next_h.start()]


def code_block_from_section(section_text: str) -> str:
    m = re.search(r"```python\n(.*?)\n```", section_text, flags=re.S)
    return m.group(1) if m else ""


def non_empty_lines(text: str) -> int:
    return sum(1 for line in text.splitlines() if line.strip())


def validate_file(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8", errors="replace")

    for h in REQUIRED_HEADERS:
        if h not in text:
            errors.append(f"{path}: missing header '{h}'")

    links_section = section_block(text, "## Official API / GitHub / PyPI Links")
    if "https://" not in links_section:
        errors.append(f"{path}: link section has no https URL")
    if "github" not in links_section.lower():
        errors.append(f"{path}: link section has no GitHub reference")

    snippet_section = section_block(text, "## Minimal Runnable Snippet")
    code = code_block_from_section(snippet_section)
    if not code:
        errors.append(f"{path}: missing python code block in minimal snippet section")
        return errors

    if "BayesianOptimization" not in code:
        errors.append(f"{path}: minimal snippet missing BayesianOptimization")
    if "ZADU" not in code:
        errors.append(f"{path}: minimal snippet missing ZADU usage")

    has_dr_fit = (
        "fit_transform(" in code
        or ".fit(" in code
        or "train_random(" in code
        or "train_batch(" in code
    )
    if not has_dr_fit:
        errors.append(f"{path}: minimal snippet missing DR fit step")

    code_lines = non_empty_lines(code)
    if code_lines > 35:
        errors.append(f"{path}: minimal snippet too long ({code_lines} non-empty lines)")

    low = code.lower()
    for term in BANNED_CODE_TERMS:
        if term in low:
            errors.append(f"{path}: banned internal term in code snippet: '{term}'")

    return errors


def main() -> int:
    errors: list[str] = []
    files = sorted(p for p in TECH_DIR.glob("*.md") if p.name != "README.md")

    for p in files:
        errors.extend(validate_file(p))

    if errors:
        print("TECHNIQUE_EXECUTION_DOC_VALIDATION_FAILED")
        for err in errors:
            print(f"- {err}")
        return 1

    print(f"OK: validated technique execution sections ({len(files)} files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
