# Reliability Report Contract

Use this contract as the required output format after running the DR workflow.
The goal is to make recommendations auditable, reproducible, and task-aligned.

Related:
- Workflow: [`docs/workflow/dr-analysis-workflow.md`](./dr-analysis-workflow.md)
- Initialization policy: [`docs/workflow/task-aligned-initialization.md`](./task-aligned-initialization.md)
- Metric/technique policy: [`docs/metrics-and-libraries.md`](../metrics-and-libraries.md)
- Reliability cautions: [`docs/reliability-cautions-and-tips.md`](../reliability-cautions-and-tips.md)

## Required Sections

## 1) Task Contract
- `primary_task_axis`
- `task_subtype` (optional)
- `success_criteria`
- `task_confidence` (`high|medium|low`)

Rule:
- If `task_confidence` is not `high`, do not finalize method recommendation.

## 2) Data & Preprocessing Contract
- `dataset_shape`
- `label_status` (`available|partial|unavailable`)
- `preprocessing_plan`
- `data_constraints`

Rule:
- Keep preprocessing fixed during method comparison.

## 3) Candidate Set Contract
- `candidate_techniques` (ranked)
- `candidate_metrics` (bundle by local/cluster/global role)
- `warning_gate_result` (`pass|fail|unknown`)
- `warning_gate_notes`

Rule:
- If warning gate is `fail` or `unknown` for class-aware metrics, down-weight those metrics and document why.

## 4) Initialization Contract
- `initialization_mode`
- `initialization_method`
- `initialization_rationale`
- `initialization_comparison_protocol`
- `initialization_stability_summary`

Rule:
- For initialization-sensitive stochastic methods, include multi-seed evidence before finalizing.

## 5) Optimization Contract
- `search_space`
- `objective_metrics`
- `best_params`
- `optimization_trace`
- `seed_sensitivity_summary`
- `guardrail_metric_summary`

Rule:
- Include at least one guardrail metric from a different structural level than the primary objective metric.

## 6) Selection Tradeoff Contract
- `selection_tradeoffs`
- `rejected_candidates_with_reason`
- `runtime_feasibility_notes`

Rule:
- Explain what was intentionally not optimized (for example local quality vs global distance faithfulness).

## 7) Final Explanation Contract
- `final_explanation`
- `source_note_links`
- `residual_risk_statement`
- `recommendation_status` (`accepted|contested|exploratory`)

Rule:
- If source claims are contested, set `recommendation_status: contested`.

## Minimal JSON-like Example
```text
primary_task_axis: Cluster identification
task_subtype: ambiguous-boundary point assignment
success_criteria: stable cluster assignment across seeds and two methods
task_confidence: high

preprocessing_plan: z-score + outlier clipping + duplicate removal
data_constraints: class imbalance mild, sparse tail clusters

candidate_techniques: [umap, t-sne, lmds]
candidate_metrics:
  local: [tnc, nd]
  cluster: [snc]
  global_guardrail: [stress]
warning_gate_result: pass

initialization_mode: informative
initialization_method: pca
initialization_stability_summary: stable across 5 seeds

best_params: {...}
guardrail_metric_summary: no global collapse detected

selection_tradeoffs: improved local cluster integrity with minor global distance loss
recommendation_status: accepted
source_note_links: [papers/notes/..., papers/notes/...]
residual_risk_statement: minor sensitivity at sparse boundary clusters
```

## Completion Checklist
1. Task clarified and mapped to one axis.
2. Warning gate resolved and recorded.
3. Initialization policy and stability reported.
4. Optimization trace and guardrail metrics reported.
5. Final explanation includes explicit residual risk.
