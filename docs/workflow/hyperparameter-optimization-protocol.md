# Hyperparameter Optimization Protocol

Use this protocol to tune DR parameters after goal confirmation, candidate selection, and initialization choice.

Related:
- Workflow anchor: [`docs/workflow/dr-analysis-workflow.md`](./dr-analysis-workflow.md)
- Initialization policy: [`docs/workflow/task-aligned-initialization.md`](./task-aligned-initialization.md)
- Selection policy: [`docs/workflow/configuration-selection-policy.md`](./configuration-selection-policy.md)
- Canonical implementation and bound reference: [`docs/workflow/bayesian-optimization-reference.md`](./bayesian-optimization-reference.md)

## Hard Rule
Use `bayes_opt` only.
Do not replace it with grid search, random search, or manual sweep loops.

Score-maximization rationale:
- when the goal is to maximize reliability/quality metric scores, Bayesian optimization is preferred over manual sweeps because it allocates trials adaptively.
- under a comparable evaluation budget, this usually reaches stronger best-score candidates than fixed coarse sweeps.

Explicitly forbidden final-code patterns:
- `GridSearchCV`
- `ParameterGrid`
- nested loops over parameter lists/ranges used as tuning sweeps
- random-search style samplers

Interpretation for permissive external prompts:
- if a prompt says `any optimization allowed`, interpret it as budget flexibility within `bayes_opt` trials.
- do not reinterpret it as permission to use grid/random/manual sweep optimizers.

If `bayes_opt` cannot run (missing package/import/runtime failure):
- stop final recommendation and mark it as `BLOCKED`
- report the concrete fix command (for example `pip install bayesian-optimization`)
- do not switch optimizer family

Validation helper:
- run `python scripts/validate_bayes_opt_policy.py <file-or-dir>` to detect non-compliant optimizer patterns in generated Python code.

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
Metadata-aligned defaults for major techniques (from `umato_exp/_metadata.json`):
- `tsne`:
  - `perplexity`: [5, 50]
- `isomap`:
  - `n_neighbors`: [2, 100]
- `umap` / `umap_pca`:
  - `n_neighbors`: [2, 100]
  - `min_dist`: [0.01, 0.99]
- `umato`:
  - `n_neighbors`: [2, 100]
  - `min_dist`: [0.01, 0.99]
  - `hub_num`: [20, 400]
- `pacmap`:
  - `n_neighbors`: [2, 100]
  - `MN_ratio`: [0.1, 5]
  - `FP_ratio`: [0.1, 5]
- `trimap`:
  - `n_inliers`: [2, 100]
  - `n_outliers`: [2, 10]
- `lle`:
  - `n_neighbors`: [2, 100]
- `lmds`:
  - `hub_num`: [20, 400]
- `pca`, `lamp`:
  - no metadata bounds defined; use low-tuning defaults unless task-specific tuning is required

Primary metadata source:
- [umato_exp `_metadata.json`](https://github.com/hj-n/umato_exp/blob/master/_final_exp/_metadata.json)
- [umato_exp optimization runner](https://github.com/hj-n/umato_exp/blob/master/_final_exp/01_accuracy.py)

Dataset-size clamping is mandatory for size-sensitive bounds:
- `n_neighbors`, `n_inliers`, `n_outliers` upper bound <= `n_samples - 2`
- `hub_num` upper bound <= `n_samples / 4`

## Wide-Range Rule For Unlisted Techniques
If a technique is not covered by metadata, begin with wide bounds:
- `n_neighbors`: [5, min(200, n_samples - 2)]
- `min_dist`: [0.0, 0.99]
- `perplexity`: [5, min(80, (n_samples - 1) / 3)]
- `learning_rate`: [10, 2000]
- `spread`: [0.5, 5.0]
- `gamma`: [1e-4, 10.0]
- `hub_num`: [20, min(800, n_samples / 4)]

Protocol:
1. start wide
2. narrow only after early trial evidence
3. keep optimizer family fixed to `bayes_opt`

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
