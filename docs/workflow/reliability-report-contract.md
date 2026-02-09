# Reliability Report Contract

Use this contract as the mandatory final output format.
The report must make recommendation quality auditable and reproducible.

Related:
- Workflow: [`docs/workflow/dr-analysis-workflow.md`](./dr-analysis-workflow.md)
- Communication layer policy: [`docs/workflow/communication-layer-policy.md`](./communication-layer-policy.md)
- Selection scoring: [`docs/workflow/configuration-selection-policy.md`](./configuration-selection-policy.md)
- Initialization rules: [`docs/workflow/task-aligned-initialization.md`](./task-aligned-initialization.md)
- Optimization protocol: [`docs/workflow/hyperparameter-optimization-protocol.md`](./hyperparameter-optimization-protocol.md)
- Visualization policy: [`docs/workflow/visualization-policy.md`](./visualization-policy.md)
- Contract validator script: `scripts/validate_reliability_report.py`

## Required Sections

## 1) Task Confirmation Contract
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
- `optimizer` must be exactly `bayes_opt`.
- reports using `grid search`, `random search`, or manual parameter sweeps are invalid.
- include at least one guardrail metric from a different structural level.

## 7) Visualization and Communication Contract
- `visual_artifacts`
- `visual_consistency_check`
- `technical_explanation` (internal layer)
- `user_explanation` (user layer)
- `source_note_links`
- `residual_risk_statement`
- `recommendation_status` (`accepted|provisional|exploratory|contested`)
- `final_configuration_for_users`
- `user_goal_restatement`
- `user_what_was_compared`
- `user_why_selected`
- `user_risk_note`
- `user_code_snippet`
- `user_code_reason`

Rule:
- if visual evidence materially contradicts metric narrative, status cannot be `accepted`.
- The report must explicitly disclose the final configuration to users:
  - chosen technique/method name
  - key hyperparameters and fixed values
  - preprocessing choices that affect interpretation
  - initialization method and seed policy (if applicable)
- The report must include concise runnable user code and a short reason block.

## Dual-Layer Communication Contract (Mandatory)
Every final report must contain both layers:

1. Internal technical layer:
   - full technical terms are allowed
   - supports reproducibility and audit
2. User explanation layer:
   - must follow `docs/workflow/communication-layer-policy.md`
   - must avoid standalone internal jargon
   - must avoid metric abbreviations/IDs (for example `tnc`, `nh`, `nd`) in user text
   - must not expose platform/source interfaces (for example `DR KB`, `Context7`, `this repo`)
   - must not expose internal workflow nouns such as `preprocessing freeze`, `primary metric`, `guardrail metric`, `task axis`, `task lock`, `metric bundle`, `bundle scoring`, `warning gate`
   - must not expose internal key-like tokens (for example `primary_task_axis`, `warning_gate_result`, `candidate_score_table`, `selection_status`)
   - must be understandable to a DR novice with basic CS background

Hard rule:
- if user layer contains forbidden standalone jargon, report is invalid.
- if user layer uses metric abbreviations/IDs instead of full names, report is invalid.
- if user layer reveals platform/source interfaces, report is invalid.
- if user layer contains banned workflow phrases (`preprocessing freeze`, `primary metric`, `guardrail metric`, `task lock`, `metric bundle`, etc.), report is invalid.
- if user layer contains internal `snake_case` keys, report is invalid.
- if optimization method is not `bayes_opt`, report is invalid.

## Final Configuration Disclosure (Mandatory)
The user layer must contain one compact section that users can copy and reuse directly.

Required keys in that section:
- `method`
- `key_hyperparameters`
- `preprocessing_summary`
- `initialization_summary`
- `reproducibility_summary`

Rule:
- Do not finalize any recommendation without this section, even when the explanation text is otherwise complete.

## Concise Code Disclosure (Mandatory)
The user layer must include:
- `user_code_snippet`: minimal runnable code for the selected method/configuration.
- `user_code_reason`: short plain-language rationale for why this code was chosen.
- acceptable DR libraries include the selected option (for example `scikit-learn`, `umap-learn`, `openTSNE`, `PaCMAP`) plus `zadu` for reliability evaluation.

Rules:
- keep code focused on the selected path; do not expose internal policy wiring in user snippet.
- keep explanation short and understandable to DR novices.
- user code must not include internal report objects or key names (for example `task_lock`, `preprocessing_config`, `primary_task_axis`, `axis_confidence`, `candidate_score_table`).
- user code should use normal analysis-library flow (data -> preprocessing -> DR -> reliability evaluation) with real library calls.
- do not hard-code one DR library as the only valid option in user guidance; use the method selected by the recommendation.
- user code should include `bayes_opt` for tuning and `zadu` for reliability scoring.

## Plain-Language Explanation Standard (Mandatory)
The user layer must include this 4-part explanation:
1. `What you asked`:
   - restate the user's goal in plain words.
2. `What we tested`:
   - name compared methods and quality checks with one-line meaning each.
3. `What we found`:
   - summarize the top result and one rejected alternative in plain terms.
4. `Why this is reliable enough`:
   - mention repeat-run consistency, safety-check result, and one residual risk.

## Minimal JSON-like Example (Internal Technical Layer)
```text
primary_task_axis: Cluster identification
axis_confidence: high
task_confirmation_quote: "I want to identify stable groups and ambiguous points."

preprocessing_profile_id: A
distance_metric: euclidean
frozen_preprocessing_signature: profile=A;scale=zscore;distance=euclidean;seed=42

candidate_techniques: [pca, isomap, t-sne]
candidate_metrics:
  primary: [tnc, snc]
  guardrail: [stress]
warning_gate_result: pass

candidate_score_table:
  - candidate: pca+tnc_snc_stress
    total_score: 82.4
    status: accepted
  - candidate: isomap+tnc_snc_stress
    total_score: 78.9
    status: accepted
selected_configuration: pca+tnc_snc_stress
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
technical_explanation: "Candidate ranking used weighted score with primary metrics and guardrail checks."
user_explanation: "We compared several methods using the same data-preparation steps and chose the one that kept class distances most consistent."
user_goal_restatement: "You want to compare how far apart digit classes are."
user_what_was_compared: "We compared three mapping methods and checked distance quality with multiple scores."
user_why_selected: "The selected method best preserved class-distance patterns and stayed stable across repeated runs."
user_risk_note: "Nearby classes can still look slightly overlapped in 2D."
user_code_snippet: |
  from bayes_opt import BayesianOptimization
  from sklearn.decomposition import PCA
  from zadu import zadu

  # Example only: replace PCA with your selected DR method/library.
  def objective(n_components):
      nc = int(round(n_components))
      Z_tmp = PCA(n_components=nc, random_state=42).fit_transform(X_scaled)
      spec = zadu.make_spec(zadu.MEASURE.TNC | zadu.MEASURE.STRESS)
      scores = zadu.ZADU(spec, X_scaled).measure(Z_tmp, label=y)
      return aggregate_reliability_score(scores)  # project-defined scalar objective

  opt = BayesianOptimization(f=objective, pbounds={"n_components": (2, 10)}, random_state=42)
  opt.maximize(init_points=5, n_iter=25)

  best_n = int(round(opt.max["params"]["n_components"]))
  Z = PCA(n_components=best_n, random_state=42).fit_transform(X_scaled)
user_code_reason: "This keeps code practical while following policy: tune with bayes_opt, then score reliability with ZADU using the selected DR method."
final_configuration_for_users:
  method: pca
  key_hyperparameters: {n_components: 2}
  preprocessing_summary: "z-score scaling, euclidean distance"
  initialization_summary: "PCA initialization, fixed random seed"
  reproducibility_summary: "same data-prep rules and seed policy across compared methods"
```

## Completion Checklist
1. Task confirmation completed with high confidence.
2. Preprocessing signature frozen.
3. Warning gate resolved.
4. Candidate score table present.
5. Initialization stability reported.
6. Optimization and guardrail summaries reported.
7. `optimizer` is exactly `bayes_opt`.
8. Internal and user explanation layers are both present.
9. User layer includes concise code and code reason.
10. `user_code_snippet` includes `bayes_opt`, `zadu`, and a DR fit step.
11. Contract validator returns success for the report artifact.
