# Task-Aligned Initialization Rules

This document defines initialization decisions that must be made after Step 3 (technique/metric selection) and before Step 5 (hyperparameter optimization).

Related:
- Workflow anchor: [`docs/workflow/dr-analysis-workflow.md`](./dr-analysis-workflow.md)
- Task axis policy: [`docs/task-taxonomy.md`](../task-taxonomy.md)
- Reliability cautions: [`docs/reliability-cautions-and-tips.md`](../reliability-cautions-and-tips.md)
- Technique details: [`docs/techniques/README.md`](../techniques/README.md)

## Inputs Required
- `primary_task_axis`
- `selected_technique_family`
- `selected_metrics`
- `data_constraints`

No initialization decision should be made before these fields are fixed.

## Rule Matrix (Task Axis -> Initialization Policy)

### Global-structure tasks
Applies to:
- Point distance investigation
- Class separability investigation
- Cluster distance investigation
- Cluster density investigation

Policy:
- `Direct evidence`: For initialization-sensitive methods (especially `t-sne`, `umap`), use informative initialization as default.
- `Direct evidence`: Do not use random initialization as the only production setting for these tasks.
- `Direct evidence`: If random initialization is tested, it must be compared against informative initialization under the same protocol.

Method defaults:
- `Direct evidence`: `t-sne` -> prefer PCA initialization.
- `Inferred alignment`: `umap` -> prefer informative initialization (spectral/LE-style when available; PCA fallback when not available).

### Local-structure tasks
Applies to:
- Neighborhood identification
- Outlier identification
- Cluster identification

Policy:
- `Inferred alignment`: Informative initialization is still preferred for reproducibility.
- `Inferred alignment`: If local exploratory diversity is needed, random initialization can be used only as an additional run, not as the sole decision basis.
- `Direct evidence`: Keep initialization fixed when comparing techniques in the same experiment.

Method defaults:
- `Inferred alignment`: `t-sne` -> PCA initialization baseline, optional random-restart comparison.
- `Inferred alignment`: `umap` -> informative initialization baseline, optional random-restart comparison.

### Deterministic or initialization-light methods
Examples:
- `pca`
- many direct linear transforms

Policy:
- `Inferred alignment`: Set `initialization_mode: deterministic_na`.
- `Inferred alignment`: Record why initialization is not a decision variable.

## Mandatory Comparison Protocol
When comparing methods or settings:
1. `Direct evidence`: Keep all parameters identical except initialization when testing initialization effects.
2. `Direct evidence`: Log initialization metadata in every run:
   - `init_method`
   - `random_seed`
   - `restart_index` (if multi-start)
3. `Inferred alignment`: For global tasks, include at least one global-structure metric in the comparison report.
4. `Inferred alignment`: For local tasks, include at least one local-neighborhood metric in the comparison report.

## Initialization Decision Output Contract
Step 4 must produce:
- `initialization_mode` (`informative` | `random` | `deterministic_na`)
- `initialization_method` (for example `pca`, `laplacian_eigenmaps`, `random`)
- `initialization_rationale` (task-aligned explanation)
- `initialization_comparison_protocol` (how fairness and reproducibility are enforced)

## Source Notes
- `papers/notes/2020-kobak-initialization-tsne-umap.md`
- `papers/notes/2025-jeon-reliable-va-survey.md`
- `papers/notes/2019-spectral-overlap-quality-metrics.md`
- `papers/notes/2024-large-scale-text-spatialization.md`
- `papers/notes/zadu-ref-17-ref13-stochastic-neighbor-embedding.md`
