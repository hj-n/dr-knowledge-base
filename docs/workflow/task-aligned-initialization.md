# Task-Aligned Initialization Rules

This document defines initialization decisions after candidate selection and before hyperparameter optimization.

Related:
- Workflow anchor: [`docs/workflow/dr-analysis-workflow.md`](./dr-analysis-workflow.md)
- Selection policy: [`docs/workflow/configuration-selection-policy.md`](./configuration-selection-policy.md)
- Technique details: [`docs/techniques/README.md`](../techniques/README.md)

## Inputs Required
- `primary_task_axis`
- `selected_configuration`
- `selected_metrics`
- `data_constraints`
- `frozen_preprocessing_signature`

## Method Groups
### Group A: Initialization-sensitive stochastic methods
Examples:
- `t-sne`, `umap`, `sne`, `catsne`, `classnerv`, `classimap`

Default policy:
- use `initialization_mode = informative`
- random initialization is evaluation-only, not production default

### Group B: Graph/manifold methods with optional embedding initialization
Examples:
- `isomap`, `s-isomap`, `lle`, `laplacian_eigenmaps`, `lmds`, `lamp`, `plmp`, `lsp`

Default policy:
- use deterministic or informative graph-consistent initialization when available
- keep graph construction settings fixed during init comparisons

### Group C: Deterministic or initialization-light methods
Examples:
- `pca`, most direct linear transforms

Default policy:
- set `initialization_mode = deterministic_na`
- record that initialization is not a decision variable

## Task-Axis Policy
### Global-structure tasks
- Point distance investigation
- Class separability investigation
- Cluster distance investigation
- Cluster density investigation

Rules:
- informative initialization is mandatory for Group A unless explicitly blocked
- random-only runs cannot be final production basis

### Local-structure tasks
- Neighborhood identification
- Outlier identification
- Cluster identification

Rules:
- informative initialization remains default for reproducibility
- random restarts may be used as variability probes

## Mandatory Comparison Protocol
When initialization affects results:
1. Keep all non-init settings fixed.
2. Compare at least two initialization modes where supported.
3. Evaluate each mode across at least 3 seeds.
4. Report metric-rank consistency and qualitative consistency.

## Stability Decision Threshold
- `stable`: top candidate unchanged in at least 80% of seed runs
- `unstable`: top candidate flips in more than 20% of seed runs

If unstable:
- downgrade recommendation status by one level
- retain at least one fallback configuration

## Output Contract
- `initialization_mode` (`informative|random|deterministic_na`)
- `initialization_method`
- `initialization_rationale`
- `initialization_comparison_protocol`
- `initialization_stability_summary`
- `stability_status` (`stable|unstable`)
