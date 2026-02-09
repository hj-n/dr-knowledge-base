# Hyperparameter Optimization Protocol

Use this protocol to optimize DR method parameters after task, reliability check set, and initialization are fixed.
Only allowed optimizer is `bayes_opt`.

Related:
- Workflow anchor: [`docs/workflow/dr-analysis-workflow.md`](./dr-analysis-workflow.md)
- Initialization policy: [`docs/workflow/task-aligned-initialization.md`](./task-aligned-initialization.md)
- Selection policy: [`docs/workflow/configuration-selection-policy.md`](./configuration-selection-policy.md)

## Preconditions
- `primary_task_axis` is locked with `axis_confidence = high`
- preprocessing signature is frozen
- initialization policy is fixed
- reliability check set is fixed (primary + safety check)

## Optimizer Policy (Hard Rule)
- `optimizer` must be exactly `bayes_opt`.
- Use the `bayes_opt` Python library (`BayesianOptimization`) for implementation.
- Do not use `grid search`.
- Do not use `random search`.
- Do not use manual parameter sweep loops as a substitute for Bayesian optimization.
- If `bayes_opt` cannot be executed in the current environment, stop and report configuration as blocked instead of switching optimizer family.

## Objective Construction
Use two-level objective:
- primary objective: task-aligned metric aggregate
- safety check objective: one metric from a different structural level

Composite objective:
`objective = 0.8 * primary_metric_score + 0.2 * safety_check_metric_score`

If safety check violates minimum acceptance, reject configuration regardless of objective value.

## Search Budget Defaults (`bayes_opt`)
- small datasets (`n < 10k`): 40-60 evaluations
- medium datasets (`10k <= n < 100k`): 25-40 evaluations
- large datasets (`n >= 100k`): 15-25 evaluations with subsampling protocol

## Method Parameter Templates
Use bounded search spaces and document every bound.

### UMAP
- `n_neighbors`: [5, 200]
- `min_dist`: [0.0, 0.8]
- `spread`: [0.5, 3.0]
- `learning_rate`: [0.1, 5.0]

### t-SNE
- `perplexity`: [5, 100]
- `early_exaggeration`: [4, 24]
- `learning_rate`: [10, 1000]
- `n_iter`: [750, 3000]

### MDS / Isomap family
- neighborhood/graph controls: task-appropriate bounded range
- iteration controls: bounded for convergence vs runtime balance

## Stability Protocol
- evaluate top 3 configurations under at least 3 seeds each
- compute rank stability of candidates across seeds
- downgrade status to `provisional` if rank instability is material

## Early Stop Rules
Stop optimization when one of the following holds:
- no composite objective improvement for 10 consecutive evaluations
- runtime budget exhausted
- safety check metric degrades below acceptance floor repeatedly

## Output Contract
Step 5 must output:
- `optimizer`
- `search_space`
- `evaluation_budget`
- `objective_definition`
- `top_configurations`
- `best_params`
- `seed_sensitivity_summary`
- `safety_check_summary`
