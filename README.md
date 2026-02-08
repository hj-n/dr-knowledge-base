# DR Knowledge Base

Task-first knowledge base for reliable dimensionality-reduction (DR) configuration.
The goal is for an agent to: lock user task intent, produce a strong DR configuration, and explain why it was selected.

## Start Here
- [`docs/overview.md`](docs/overview.md)
- [`docs/workflow/dr-analysis-workflow.md`](docs/workflow/dr-analysis-workflow.md)
- [`docs/workflow/task-confirmation-protocol.md`](docs/workflow/task-confirmation-protocol.md)
- [`docs/workflow/preprocessing-profiles.md`](docs/workflow/preprocessing-profiles.md)
- [`docs/workflow/configuration-selection-policy.md`](docs/workflow/configuration-selection-policy.md)
- [`docs/workflow/task-aligned-initialization.md`](docs/workflow/task-aligned-initialization.md)
- [`docs/workflow/hyperparameter-optimization-protocol.md`](docs/workflow/hyperparameter-optimization-protocol.md)
- [`docs/workflow/visualization-policy.md`](docs/workflow/visualization-policy.md)
- [`docs/workflow/reliability-report-contract.md`](docs/workflow/reliability-report-contract.md)
- [`docs/metrics-and-libraries.md`](docs/metrics-and-libraries.md)

## Execution Intent
1. Confirm one primary task axis from user language.
2. Freeze preprocessing profile and distance policy.
3. Build task-aligned technique and metric candidates.
4. Score candidates with deterministic selection policy.
5. Set task-aligned initialization policy.
6. Optimize hyperparameters with `bayes_opt`.
7. Produce visualization artifacts and final explanation contract.

## Key Directories
- `docs/`: consumer-facing operational guidance.
- `papers/notes/`: evidence notes with claim-level support.
- `papers/raw/`: raw PDFs.
- `builder/evidence/`: builder-only conflict/relevance/canonicalization policy and indices.

## Source Note Contract
Each `papers/notes/*.md` file must include frontmatter:
- `id`
- `title`
- `authors`
- `venue`
- `year`
- `tags`
- `source_pdf`
- `evidence_level`
- `updated_at`

And required sections:
1. Problem
2. Method Summary
3. When To Use / Not Use
4. Metrics Mentioned
5. Implementation Notes
6. Claim Atoms (For Conflict Resolution)
7. Workflow Relevance Map
8. Evidence

Template: `templates/paper-note-template.md`

## Maintenance Commands
- `python scripts/update_paper_catalog.py`
- `python scripts/update_reference_coverage.py`
- `python scripts/update_reference_backlog.py`
