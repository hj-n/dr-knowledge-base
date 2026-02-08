# Techniques Directory

This directory contains general-purpose dimensionality-reduction techniques that map high-dimensional input data to low-dimensional projections.

Related:
- Workflow anchor: [`docs/workflow/dr-analysis-workflow.md`](../workflow/dr-analysis-workflow.md)
- Task-aligned initialization rules: [`docs/workflow/task-aligned-initialization.md`](../workflow/task-aligned-initialization.md)
- Task clarification prerequisite: [`docs/intake-question-tree.md`](../intake-question-tree.md)
- Task axis/subtask policy: [`docs/task-taxonomy.md`](../task-taxonomy.md)
- Selection policy: [`docs/metrics-and-libraries.md`](../metrics-and-libraries.md)
- Metric catalog: [`docs/metrics/README.md`](../metrics/README.md)
- Frequency ranking: [`docs/reference-coverage.md`](../reference-coverage.md)
- Grouped reliability cautions: [`docs/reliability-cautions-and-tips.md`](../reliability-cautions-and-tips.md)

## Required Sections
- Technique Summary
- I/O Contract
- Core Objective
- Computation Outline
- Hyperparameter Impact
- Practical Reliability Notes
- Notable Properties
- Strengths
- Task Alignment
- Known Tradeoffs
- Source Notes

Expectation:
- `Practical Reliability Notes` must describe implementation-sensitive risks and controls (for example seed protocol, initialization, or parameter sensitivity) with task-context.

## Technique Files
- `catsne.md`
- `cca.md`
- `classimap.md`
- `classnerv.md`
- `isomap.md`
- `kpca.md`
- `laplacian_eigenmaps.md`
- `lamp.md`
- `lle.md`
- `lmds.md`
- `lsp.md`
- `mds.md`
- `nerv.md`
- `pca.md`
- `plmp.md`
- `random_projection.md`
- `s-isomap.md`
- `sne.md`
- `som.md`
- `t-sne.md`
- `umap.md`

## Inclusion Rule
- Include methods that directly produce low-dimensional projections from general high-dimensional data.
- Do not exclude methods solely because they are less popular.
- Exclude meta-frameworks and methods that are only domain-specific.

## Task-First Rule
- Identify one primary task axis before selecting a technique.
- If a subtask exists, use it to refine within axis-valid candidates.
- Label alignment statements as `Direct evidence` or `Inferred alignment`.
- Pair technique choice with task-aligned metrics from `docs/metrics/`.
- When multiple techniques fit the same task, use PDF-backed support frequency from `docs/reference-coverage.md` to set recommendation priority.
