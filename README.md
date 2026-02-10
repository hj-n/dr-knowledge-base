# DR Knowledge Base

Task-first guidance for reliable dimensionality-reduction (DR) analysis.
The goal is to help an agent confirm user intent, choose a strong configuration, and explain the final choice clearly.

## Start Here
- `llms.txt`
- [`docs/overview.md`](docs/overview.md)
- [`docs/workflow/dr-analysis-workflow.md`](docs/workflow/dr-analysis-workflow.md)
- [`docs/workflow/task-confirmation-protocol.md`](docs/workflow/task-confirmation-protocol.md)
- [`docs/workflow/preprocessing-profiles.md`](docs/workflow/preprocessing-profiles.md)
- [`docs/workflow/configuration-selection-policy.md`](docs/workflow/configuration-selection-policy.md)
- [`docs/workflow/task-aligned-initialization.md`](docs/workflow/task-aligned-initialization.md)
- [`docs/workflow/hyperparameter-optimization-protocol.md`](docs/workflow/hyperparameter-optimization-protocol.md)
- [`docs/workflow/visualization-policy.md`](docs/workflow/visualization-policy.md)
- [`docs/workflow/communication-layer-policy.md`](docs/workflow/communication-layer-policy.md)
- [`docs/workflow/reliability-report-contract.md`](docs/workflow/reliability-report-contract.md)
- [`docs/metrics-and-libraries.md`](docs/metrics-and-libraries.md)

## Core Execution Intent
1. Confirm one main analysis goal from user language.
2. Keep preprocessing and distance choices consistent across method comparison.
3. Build goal-aligned method and reliability-check candidates.
4. Rank candidates with the deterministic policy.
5. Set initialization strategy.
6. Tune with `bayes_opt` only.
7. Evaluate reliability with `zadu` and explain the final choice in plain language.

## Best/Optimal Requests
- Compare all goal-aligned candidates before pruning.
- Exclude candidates only with explicit hard-failure reasons.

## Key Directories
- `docs/`: user-facing operational guidance.
- `papers/raw/`: raw PDFs.
- notes under `papers/`: extracted evidence records.
- `builder/evidence/`: builder-only traceability and policy artifacts.

## Maintenance Commands
- `python scripts/update_paper_catalog.py`
- `python scripts/update_reference_coverage.py`
- `python scripts/update_reference_backlog.py`
- `python scripts/audit_note_quality.py`
- `python scripts/verify_note_pdf_grounding.py`
- `python scripts/validate_user_explanation_text.py <user-text-file>`
- `python scripts/validate_reliability_report.py <report-file>`
- `python scripts/lint_user_layer_docs.py`

## Context7 Snippet (AGENTS.md / CLAUDE.md)
```md
## Context7 Read Rule
- Before coding, load this project from Context7:
  - `query-docs(libraryId="/hj-n/dr-knowledge-base", query="<task-specific workflow and reporting rules>")`
- Read in this order:
  1) `llms.txt`
  2) `docs/overview.md`
  3) `docs/workflow/dr-analysis-workflow.md`
  4) `docs/workflow/reliability-report-contract.md`
- If references are requested, cite papers (title, authors, venue, year, URL), not internal file paths.
- Keep user explanations plain and concise.
- Use `bayes_opt` for tuning and `zadu` for reliability scoring.
```
