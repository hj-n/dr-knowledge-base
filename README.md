# DR Knowledge Base v1 (Lean)

This repository is a task-first DR guidance base for LLMs.
The runtime goal is simple: identify the user's analytical task first, then recommend aligned techniques and reliability metrics.

## Start Here
- [`docs/overview.md`](docs/overview.md)
- [`docs/workflow/dr-analysis-workflow.md`](docs/workflow/dr-analysis-workflow.md)
- [`docs/intake-question-tree.md`](docs/intake-question-tree.md)
- [`docs/metrics-and-libraries.md`](docs/metrics-and-libraries.md)
- [`docs/reference-coverage.md`](docs/reference-coverage.md)

## What Consumer LLMs Should Do
1. Clarify one primary analytical task.
2. Audit/preprocess data constraints.
3. Select task-aligned technique family and ZADU metric IDs.
4. Run warning gate for label-separation-sensitive metrics.
5. Optimize hyperparameters (`bayes_opt`) and visualize.
6. Explain the final choice in user language with source-note links.

## Key Directories
- `docs/`: consumer-facing operational guidance.
- `papers/notes/`: source notes that back the guidance.
- `papers/raw/`: raw source files.
- `builder/evidence/`: builder-only relevance/conflict policies.
- `builder/evidence/reference-coverage.md`: metric/technique reference-frequency index (PDF-backed priority).

## Note Contract (for source notes)
Each note in `papers/notes/*.md` must include frontmatter:
- `id`
- `title`
- `year`
- `tags`
- `source_pdf`
- `evidence_level` (`high|medium|low`)
- `updated_at`

And sections:
1. Problem
2. Method Summary
3. When To Use / Not Use
4. Metrics Mentioned
5. Implementation Notes
6. Evidence

Template: `templates/paper-note-template.md`

## Context7 Indexing
- Included: `docs`, `papers/notes`
- Excluded: `papers/raw`
- Initial sync: `add`
- Update sync: `refresh`
