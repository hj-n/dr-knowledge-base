# DR Knowledge Base v1 (Lean)

This repository is a task-first DR guidance base for LLMs (and perhaps humans).
The runtime goal is simple: identify the user's analytical task first, then recommend aligned techniques and reliability metrics.

## Start Here
- [`docs/overview.md`](docs/overview.md)
- [`docs/workflow/dr-analysis-workflow.md`](docs/workflow/dr-analysis-workflow.md)
- [`docs/workflow/task-aligned-initialization.md`](docs/workflow/task-aligned-initialization.md)
- [`docs/intake-question-tree.md`](docs/intake-question-tree.md)
- [`docs/task-taxonomy.md`](docs/task-taxonomy.md)
- [`docs/metrics-and-libraries.md`](docs/metrics-and-libraries.md)
- [`docs/reference-coverage.md`](docs/reference-coverage.md)
- [`docs/reliability-cautions-and-tips.md`](docs/reliability-cautions-and-tips.md)
- [`docs/paper-catalog.md`](docs/paper-catalog.md)
- [`docs/paper-catalog.csv`](docs/paper-catalog.csv)

## What Consumer LLMs Should Do
1. Clarify one primary analytical task.
   - optional: refine with a subtask under that task axis
2. Audit/preprocess data constraints.
3. Select task-aligned technique family and ZADU metric IDs.
4. Run warning gate for label-separation-sensitive metrics.
5. Decide task-aligned initialization method.
6. Optimize hyperparameters (`bayes_opt`) and visualize.
7. Explain the final choice in user language with source-note links.

## Key Directories
- `docs/`: consumer-facing operational guidance.
- `papers/notes/`: source notes that back the guidance.
- `papers/raw/`: raw source files.
- `builder/evidence/`: builder-only relevance/conflict policies.
- `builder/evidence/reference-coverage.md`: metric/technique reference-frequency index (PDF-backed priority).
- `docs/paper-catalog.csv`: user-facing paper list (seed/reference, metadata, source note mapping).

## Note Contract (for source notes)
Each note in `papers/notes/*.md` must include frontmatter:
- `id`
- `title`
- `authors`
- `venue`
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
6. Claim Atoms (For Conflict Resolution)
7. Workflow Relevance Map
8. Evidence

Template: `templates/paper-note-template.md`

After adding or updating paper notes, refresh indexes:
- `python scripts/update_paper_catalog.py`
- `python scripts/update_reference_coverage.py`
- `python scripts/update_reference_backlog.py`

## Context7 Indexing
- Included: `docs`, `papers/notes`
- Excluded: `papers/raw`
- Initial sync: `add`
- Update sync: `refresh`
