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

## Initialization Stability Requirement
For initialization-sensitive stochastic methods (`t-sne`, `umap`, `trimap`, and related variants), include a stability check before final recommendation:
- run at least 3 seeds under the same hyperparameter setting and initialization mode;
- compare both metric ranks and qualitative structure stability across runs;
- if ranking or interpretation changes materially across seeds, mark recommendation confidence as `reduced` and keep multiple candidates.

When random initialization is evaluated, treat it as a variability probe rather than a default production policy for distance-critical tasks. For global-structure tasks, keep informative initialization as the baseline and document why any random-initialization result is still acceptable.

## Initialization Decision Output Contract
Step 4 must produce:
- `initialization_mode` (`informative` | `random` | `deterministic_na`)
- `initialization_method` (for example `pca`, `laplacian_eigenmaps`, `random`)
- `initialization_rationale` (task-aligned explanation)
- `initialization_comparison_protocol` (how fairness and reproducibility are enforced)
- `initialization_stability_summary` (seed-wise variance and whether recommendation confidence is reduced)

## Source Notes
- `papers/notes/2020-kobak-initialization-tsne-umap.md`
- `papers/notes/2025-jeon-reliable-va-survey.md`
- `papers/notes/2019-spectral-overlap-quality-metrics.md`
- `papers/notes/2024-large-scale-text-spatialization.md`
- `papers/notes/zadu-ref-17-ref13-stochastic-neighbor-embedding.md`
- `papers/notes/pending-ref-029-stability-comparison-of-dimensionality-reduction-technique.md`
- `papers/notes/pending-ref-054-a-large-scale-sensitivity-analysis-on-latent-embeddings-an.md`
- `papers/notes/pending-ref-101-trimap-large-scale-dimensionality-reduction-using-triplets.md`
- `papers/notes/pending-ref-121-understanding-how-dimension-reduction-tools-work-an-empiri.md`
- `papers/notes/pending-ref-129-ens-t-sne-embedding-neighborhoods-simultaneously-t-sne.md`
