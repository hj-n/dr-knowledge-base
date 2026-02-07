# DR Analysis Workflow (Primary Axis)

Use this sequence as the default DR-analysis workflow.

## 1) Task clarification
- Ask plain-language questions.
- Identify one primary analytical task.

Output:
- `primary_task`
- `success_criteria`

## 2) Data audit + preprocessing
- Check shape, missingness, sparsity, scale, and label availability.
- Apply preprocessing needed for stable comparison.

Output:
- `preprocessing_plan`
- `data_constraints`

## 3) Task-aligned technique/metric selection
- Choose technique family aligned with the primary task.
- Choose a small metric set across local/cluster/global levels.
- Run warning gate for label-separation-sensitive metrics:
  - `dsc`, `ivm`, `c_evm`, `nh`, `ca_tnc`

Output:
- `selected_technique_family`
- `selected_metrics`
- `warning_gate_result`

## 4) Bayesian hyperparameter optimization (`bayes_opt`)
- Optimize hyperparameters against Step-3 objective.
- Keep seed/search-space settings explicit.

Output:
- `best_params`
- `optimization_trace`

## 5) Visualization
- Generate 2D visual artifacts for analysis communication.
- Apply project-approved visualization constraints only.

Output:
- `visual_artifacts`
- `visual_notes`

## 6) Explain the selection to users
- Explain why this task mapping was chosen.
- Explain why this technique/metric set was chosen.
- Explain warning-gate status and remaining limits.

Output:
- `final_explanation`
- `source_note_links`

## Execution Contract
1. Do not skip Step 1.
2. Do not finalize recommendation before warning gate is resolved.
3. If source notes conflict, mark recommendation status as `contested`.
