# DR Analysis Workflow (Primary Axis)

Use this sequence as the default DR-analysis workflow.

## Step-to-Document Map
1. Task clarification:
   [`docs/intake-question-tree.md`](../intake-question-tree.md)
2. Data audit + preprocessing:
   this file (Step 2 contract) + selected technique file in
   [`docs/techniques/`](../techniques/README.md)
3. Task-aligned technique/metric selection:
   [`docs/metrics-and-libraries.md`](../metrics-and-libraries.md),
   [`docs/metrics/README.md`](../metrics/README.md),
   [`docs/techniques/README.md`](../techniques/README.md)
4. Hyperparameter optimization:
   this file (Step 4 contract) + selected technique file in
   [`docs/techniques/`](../techniques/README.md)
5. Visualization:
   this file (Step 5 contract) + selected technique file in
   [`docs/techniques/`](../techniques/README.md)
6. Final recommendation explanation:
   this file (Step 6 contract) + frequency ranking in
   [`docs/reference-coverage.md`](../reference-coverage.md)

## 1) Task clarification
- Ask plain-language questions.
- Identify one primary analytical task.
- Read:
  [`docs/intake-question-tree.md`](../intake-question-tree.md)

Output:
- `primary_task`
- `success_criteria`

## 2) Data audit + preprocessing
- Check shape, missingness, sparsity, scale, and label availability.
- Apply preprocessing needed for stable comparison.
- Read:
  this section first, then selected-technique hyperparameter constraints in
  [`docs/techniques/README.md`](../techniques/README.md)

Output:
- `preprocessing_plan`
- `data_constraints`

## 3) Task-aligned technique/metric selection
- Choose technique family aligned with the primary task.
- Choose a small metric set across local/cluster/global levels.
- Run warning gate for label-separation-sensitive metrics:
  - `dsc`, `ivm`, `c_evm`, `nh`, `ca_tnc`
- Read:
  [`docs/metrics-and-libraries.md`](../metrics-and-libraries.md),
  [`docs/metrics/README.md`](../metrics/README.md),
  [`docs/techniques/README.md`](../techniques/README.md),
  [`docs/reference-coverage.md`](../reference-coverage.md)

Output:
- `selected_technique_family`
- `selected_metrics`
- `warning_gate_result`

## 4) Bayesian hyperparameter optimization (`bayes_opt`)
- Optimize hyperparameters against Step-3 objective.
- Keep seed/search-space settings explicit.
- Read:
  selected metric/technique file(s) under
  [`docs/metrics/`](../metrics/README.md) and
  [`docs/techniques/`](../techniques/README.md)

Output:
- `best_params`
- `optimization_trace`

## 5) Visualization
- Generate 2D visual artifacts for analysis communication.
- Apply project-approved visualization constraints only.
- Read:
  selected technique tradeoffs in
  [`docs/techniques/`](../techniques/README.md)

Output:
- `visual_artifacts`
- `visual_notes`

## 6) Explain the selection to users
- Explain why this task mapping was chosen.
- Explain why this technique/metric set was chosen.
- Explain warning-gate status and remaining limits.
- Read:
  [`docs/metrics-and-libraries.md`](../metrics-and-libraries.md) and
  [`docs/reference-coverage.md`](../reference-coverage.md)

Output:
- `final_explanation`
- `source_note_links`

## Execution Contract
1. Do not skip Step 1.
2. Do not finalize recommendation before warning gate is resolved.
3. If source notes conflict, mark recommendation status as `contested`.
