# Hyperparameter Optimization Protocol

Use this protocol to tune DR parameters after goal confirmation, candidate selection, and initialization choice.

Related:
- Workflow anchor: [`docs/workflow/dr-analysis-workflow.md`](./dr-analysis-workflow.md)
- Initialization policy: [`docs/workflow/task-aligned-initialization.md`](./task-aligned-initialization.md)
- Selection policy: [`docs/workflow/configuration-selection-policy.md`](./configuration-selection-policy.md)

## Hard Rule
Use `bayes_opt` only.
Do not replace it with grid search, random search, or manual sweep loops.

## Preconditions
- the main goal is confirmed with high confidence
- preprocessing is fixed
- initialization strategy is fixed
- aligned reliability checks are fixed

## Objective Design
Use two signals together:
- main goal signal
- cross-level safety signal

Composite objective:
`objective = 0.8 * main_goal_score + 0.2 * safety_score`

If safety score repeatedly fails minimum acceptance, reject that configuration.

## Suggested Budget
- small datasets (`n < 10k`): 40-60 evaluations
- medium datasets (`10k <= n < 100k`): 25-40 evaluations
- large datasets (`n >= 100k`): 15-25 evaluations with controlled subsampling

## Typical Search Bounds
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
- neighborhood and graph parameters: bounded, task-specific ranges
- iteration controls: bounded ranges for convergence/runtime balance

## Stability Check
- re-run top configurations across at least three seeds
- compare rank stability across repeats
- downgrade to provisional when instability is material

## Early Stop
Stop when one condition holds:
- no objective improvement over 10 consecutive evaluations
- runtime budget exhausted
- repeated safety-score failures

## Internal Record Schema
Technical field names are maintained in:
- [`builder/evidence/internal-report-schema.md`](../../builder/evidence/internal-report-schema.md)
