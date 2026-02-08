# DR Analysis Workflow (Primary Axis)

Use this sequence as the default DR-analysis workflow.

## Step-to-Document Map
1. Task clarification:
   [`docs/intake-question-tree.md`](../intake-question-tree.md),
   [`docs/task-taxonomy.md`](../task-taxonomy.md)
2. Data audit + preprocessing:
   this file (Step 2 contract) + selected technique file in
   [`docs/techniques/`](../techniques/README.md)
3. Task-aligned technique/metric selection:
   [`docs/metrics-and-libraries.md`](../metrics-and-libraries.md),
   [`docs/metrics/README.md`](../metrics/README.md),
   [`docs/techniques/README.md`](../techniques/README.md),
   [`docs/reliability-cautions-and-tips.md`](../reliability-cautions-and-tips.md)
4. Task-aligned initialization decision:
   this file (Step 4 contract) +
   [`docs/workflow/task-aligned-initialization.md`](./task-aligned-initialization.md) +
   selected technique file in
   [`docs/techniques/`](../techniques/README.md)
5. Hyperparameter optimization:
   this file (Step 5 contract) + selected technique file in
   [`docs/techniques/`](../techniques/README.md)
6. Visualization:
   this file (Step 6 contract) + selected technique file in
   [`docs/techniques/`](../techniques/README.md)
7. Final recommendation explanation:
   this file (Step 7 contract) + frequency ranking in
   [`docs/reference-coverage.md`](../reference-coverage.md) +
   reliability notes in [`docs/reliability-cautions-and-tips.md`](../reliability-cautions-and-tips.md) +
   report contract in [`docs/workflow/reliability-report-contract.md`](./reliability-report-contract.md)

## 1) Task clarification
- Ask plain-language questions.
- Identify one primary analytical task.
- Optionally define one subtask under the selected primary axis.
- Reconfirm task intent if the user shifts analytical action mid-session (for example, from cluster finding to class matching).
- Read:
  [`docs/intake-question-tree.md`](../intake-question-tree.md),
  [`docs/task-taxonomy.md`](../task-taxonomy.md)

Output:
- `primary_task_axis`
- `task_subtype` (optional)
- `success_criteria`

## 2) Data audit + preprocessing
- Check shape, missingness, sparsity, scale, and label availability.
- Apply preprocessing needed for stable comparison.
- Read:
  this section first, then selected-technique hyperparameter constraints in
  [`docs/techniques/README.md`](../techniques/README.md),
  and relevant cautions in [`docs/reliability-cautions-and-tips.md`](../reliability-cautions-and-tips.md)

Output:
- `preprocessing_plan`
- `data_constraints`

## 3) Task-aligned technique/metric selection
- Choose technique family aligned with the primary task axis.
- Refine ranking with subtask constraints if `task_subtype` is present.
- Choose a small metric set across local/cluster/global levels.
- If a required quality check is not covered by ZADU metrics, an external metric may be added only with explicit source-note provenance.
- Run warning gate for label-separation-sensitive metrics:
  - `dsc`, `ivm`, `c_evm`, `nh`, `ca_tnc`
- Read:
  [`docs/metrics-and-libraries.md`](../metrics-and-libraries.md),
  [`docs/metrics/README.md`](../metrics/README.md),
  [`docs/techniques/README.md`](../techniques/README.md),
  [`docs/reference-coverage.md`](../reference-coverage.md),
  [`docs/reliability-cautions-and-tips.md`](../reliability-cautions-and-tips.md)

Output:
- `selected_technique_family`
- `selected_metrics`
- `warning_gate_result`
- `selection_tradeoffs` (what was improved and what was intentionally not optimized)

## 4) Task-aligned initialization decision
- Decide initialization policy after task, method, and metric selection are fixed.
- Use task-aligned rules from:
  [`docs/workflow/task-aligned-initialization.md`](./task-aligned-initialization.md)
- For initialization-sensitive methods, set informative initialization as default unless explicitly justified otherwise.
- Read:
  [`docs/workflow/task-aligned-initialization.md`](./task-aligned-initialization.md),
  selected technique file(s) in
  [`docs/techniques/`](../techniques/README.md),
  and initialization cautions in
  [`docs/reliability-cautions-and-tips.md`](../reliability-cautions-and-tips.md)

Output:
- `initialization_mode`
- `initialization_method`
- `initialization_rationale`
- `initialization_comparison_protocol`
- `initialization_stability_summary`

## 5) Bayesian hyperparameter optimization (`bayes_opt`)
- Optimize hyperparameters against Step-3 objective, under the fixed Step-4 initialization policy.
- Keep seed/search-space settings explicit.
- Prefer multi-objective scoring when task risk is high:
  - one primary task metric
  - one guardrail metric from a different structural level
- Read:
  selected metric/technique file(s) under
  [`docs/metrics/`](../metrics/README.md) and
  [`docs/techniques/`](../techniques/README.md),
  then apply grouped pitfalls from
  [`docs/reliability-cautions-and-tips.md`](../reliability-cautions-and-tips.md)

Output:
- `best_params`
- `optimization_trace`
- `seed_sensitivity_summary`
- `guardrail_metric_summary`

## 6) Visualization
- Generate 2D visual artifacts for analysis communication.
- Apply project-approved visualization constraints only.
- Read:
  selected technique tradeoffs in
  [`docs/techniques/`](../techniques/README.md)

Output:
- `visual_artifacts`
- `visual_notes`

## 7) Explain the selection to users
- Explain why this task mapping was chosen.
- Explain why this technique/metric set was chosen.
- Explain why this initialization policy was chosen for the selected task and technique.
- Explain technique and metric strengths for the selected task axis/subtask.
- Explain warning-gate status and remaining limits.
- Read:
  [`docs/metrics-and-libraries.md`](../metrics-and-libraries.md) and
  [`docs/reference-coverage.md`](../reference-coverage.md),
  plus grouped limitations in
  [`docs/reliability-cautions-and-tips.md`](../reliability-cautions-and-tips.md)

Output:
- `final_explanation`
- `source_note_links`
- `residual_risk_statement`

## Execution Contract
1. Do not skip Step 1.
2. Do not run Step 5 before Step 4 is resolved.
3. Do not finalize recommendation before warning gate is resolved.
4. If source notes conflict, mark recommendation status as `contested`.
5. For initialization-sensitive methods, do not finalize selection without reporting initialization/seed stability.
