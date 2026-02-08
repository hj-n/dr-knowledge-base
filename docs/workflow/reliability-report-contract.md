# Reliability Report Contract

Use this contract as the mandatory final output format.
The report must make recommendation quality auditable and reproducible.

Related:
- Workflow: [`docs/workflow/dr-analysis-workflow.md`](./dr-analysis-workflow.md)
- Selection scoring: [`docs/workflow/configuration-selection-policy.md`](./configuration-selection-policy.md)
- Initialization rules: [`docs/workflow/task-aligned-initialization.md`](./task-aligned-initialization.md)
- Optimization protocol: [`docs/workflow/hyperparameter-optimization-protocol.md`](./hyperparameter-optimization-protocol.md)
- Visualization policy: [`docs/workflow/visualization-policy.md`](./visualization-policy.md)
- Contract validator script: `scripts/validate_reliability_report.py`

## Required Sections

## 1) Task Lock Contract
- `primary_task_axis`
- `task_subtype` (optional)
- `axis_confidence` (`high|medium|low`)
- `task_confirmation_quote`
- `success_criteria`

Rule:
- if `axis_confidence != high`, set `recommendation_status = exploratory`.

## 2) Data and Preprocessing Contract
- `dataset_shape`
- `label_status` (`available|partial|unavailable`)
- `preprocessing_profile_id`
- `preprocessing_plan`
- `distance_metric`
- `frozen_preprocessing_signature`

Rule:
- all compared candidates must share one preprocessing signature.

## 3) Candidate Generation Contract
- `candidate_techniques`
- `candidate_metrics`
- `warning_gate_result` (`pass|fail|unknown`)
- `warning_gate_notes`

Rule:
- class-aware metrics cannot be primary objective when warning gate is `fail|unknown`.

## 4) Deterministic Scoring Contract
- `candidate_score_table`
- `selected_configuration`
- `selection_status` (`accepted|provisional|exploratory`)
- `selection_reasoning_summary`
- `rejected_candidates_with_reason`

Rule:
- use weighted score formula from selection policy.
- production recommendation requires `selection_status = accepted`.

## 5) Initialization Contract
- `initialization_mode`
- `initialization_method`
- `initialization_rationale`
- `initialization_comparison_protocol`
- `initialization_stability_summary`
- `stability_status` (`stable|unstable`)

Rule:
- unstable initialization downgrades recommendation by one level.

## 6) Optimization Contract
- `optimizer`
- `search_space`
- `evaluation_budget`
- `objective_definition`
- `best_params`
- `optimization_trace`
- `seed_sensitivity_summary`
- `guardrail_metric_summary`

Rule:
- include at least one guardrail metric from a different structural level.

## 7) Visualization and Communication Contract
- `visual_artifacts`
- `visual_consistency_check`
- `final_explanation`
- `source_note_links`
- `residual_risk_statement`
- `recommendation_status` (`accepted|provisional|exploratory|contested`)
- `plain_language_summary`
- `term_explanations`
- `final_configuration_for_users`

Rule:
- if visual evidence materially contradicts metric narrative, status cannot be `accepted`.
- `final_explanation` must be understandable to DR novices:
  - avoid internal shorthand as standalone phrasing (for example `preprocessing signature`, `guardrail`).
  - when a technical term is required, define it in one short sentence.
  - explain evidence in user terms: what was measured, what it means, and why it matters for the user's task.
- The report must explicitly disclose the final configuration to users:
  - chosen technique/method name
  - key hyperparameters and fixed values
  - preprocessing choices that affect interpretation
  - initialization method and seed policy (if applicable)

## Final Configuration Disclosure (Mandatory)
The final report must contain one compact section that users can copy and reuse directly.

Required keys in that section:
- `method`
- `key_hyperparameters`
- `preprocessing_summary`
- `initialization_summary`
- `reproducibility_summary`

Rule:
- Do not finalize any recommendation without this section, even when the explanation text is otherwise complete.

## Plain-Language Explanation Standard (Mandatory)
Every final report must include this 4-part explanation:
1. `What you asked`:
   - restate the user's goal in plain words.
2. `What we tested`:
   - name candidate methods and metrics with one-line meaning each.
3. `What we found`:
   - summarize the top result and one rejected alternative in plain terms.
4. `Why this is reliable enough`:
   - mention stability check, warning-gate result, and one residual risk.

Required term explanations:
- `primary_task_axis`: the main question the user wants answered.
- `metric`: a numeric check used to verify embedding quality.
- `initialization`: the starting layout before DR optimization.
- `stability`: whether conclusions stay similar across repeated runs.

Preferred wording examples:
- Instead of `same preprocessing signature`, write:
  - `we prepared data in the same way for all methods, so the comparison is fair`.
- Instead of `guardrail metric`, write:
  - `a secondary safety-check metric to ensure one improvement does not hide another failure`.

## Minimal JSON-like Example
```text
primary_task_axis: Cluster identification
axis_confidence: high
task_confirmation_quote: "I want to identify stable groups and ambiguous points."

preprocessing_profile_id: A
distance_metric: euclidean
frozen_preprocessing_signature: profile=A;scale=zscore;distance=euclidean;seed=42

candidate_techniques: [umap, t-sne, lmds]
candidate_metrics:
  primary: [tnc, snc]
  guardrail: [stress]
warning_gate_result: pass

candidate_score_table:
  - candidate: umap+tnc_snc_stress
    total_score: 82.4
    status: accepted
  - candidate: tsne+tnc_snc_stress
    total_score: 78.9
    status: accepted
selected_configuration: umap+tnc_snc_stress
selection_status: accepted

initialization_mode: informative
initialization_method: pca
stability_status: stable

optimizer: bayes_opt
best_params: {...}
seed_sensitivity_summary: rank stable across 5 seeds

global_guardrail_metric: stress
visual_consistency_check: pass
recommendation_status: accepted
source_note_links: [papers/notes/..., papers/notes/...]
residual_risk_statement: minor instability near sparse boundary clusters
plain_language_summary: "We compared methods with the same data preparation and picked the one that best preserved class-level spacing while remaining stable."
term_explanations:
  metric: "A numeric quality check for embeddings."
  stability: "How consistent the result is across repeated runs."
final_configuration_for_users:
  method: umap
  key_hyperparameters: {n_neighbors: 30, min_dist: 0.05, n_components: 2}
  preprocessing_summary: "z-score scaling, euclidean distance"
  initialization_summary: "PCA initialization, fixed random seed"
  reproducibility_summary: "same data-prep rules and seed policy across compared methods"
```

## Completion Checklist
1. Task lock completed with high confidence.
2. Preprocessing signature frozen.
3. Warning gate resolved.
4. Candidate score table present.
5. Initialization stability reported.
6. Optimization and guardrail summaries reported.
7. Final explanation includes source links and residual risk.
8. Contract validator returns success for the report artifact.
