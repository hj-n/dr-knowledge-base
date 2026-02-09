# DR Analysis Workflow (Primary Axis)

Use this sequence as the mandatory execution order for reliable DR configuration.
For end-user explanations, translate internal terms into plain wording (for example `main goal`, `reliability checks`) per `docs/workflow/communication-layer-policy.md`.

## Step-to-Document Map
1. Task clarification and confirmation:
   [`docs/intake-question-tree.md`](../intake-question-tree.md),
   [`docs/workflow/task-confirmation-protocol.md`](./task-confirmation-protocol.md)
2. Data audit + consistent preprocessing policy:
   [`docs/workflow/preprocessing-profiles.md`](./preprocessing-profiles.md)
3. Task-aligned candidate generation:
   [`docs/metrics-and-libraries.md`](../metrics-and-libraries.md),
   [`docs/metrics/README.md`](../metrics/README.md),
   [`docs/techniques/README.md`](../techniques/README.md)
4. Deterministic configuration scoring and selection:
   [`docs/workflow/configuration-selection-policy.md`](./configuration-selection-policy.md),
   [`docs/reference-coverage.md`](../reference-coverage.md)
5. Task-aligned initialization decision:
   [`docs/workflow/task-aligned-initialization.md`](./task-aligned-initialization.md)
6. Bayesian hyperparameter optimization:
   [`docs/workflow/hyperparameter-optimization-protocol.md`](./hyperparameter-optimization-protocol.md)
7. Visualization + user explanation:
   [`docs/workflow/visualization-policy.md`](./visualization-policy.md),
   [`docs/workflow/communication-layer-policy.md`](./communication-layer-policy.md),
   [`docs/workflow/reliability-report-contract.md`](./reliability-report-contract.md),
   and `scripts/validate_reliability_report.py`

## 1) Task clarification and confirmation
- Ask plain-language goal question first.
- Resolve ambiguity one question at a time.
- Confirm one primary task axis in user wording.

Required output:
- `primary_task_axis`
- `task_subtype` (optional)
- `axis_confidence`
- `task_confirmation_quote`
- `success_criteria`

Gate:
- Do not continue unless `axis_confidence = high`.

## 2) Data audit + consistent preprocessing policy
- Inspect shape, missingness, sparsity, scale, and label status.
- Select and lock preprocessing profile.
- Freeze distance metric and preprocessing signature.

Required output:
- `preprocessing_profile_id`
- `distance_metric`
- `preprocessing_plan`
- `data_constraints`
- `frozen_preprocessing_signature`

Gate:
- Do not compare methods under mixed preprocessing signatures.

## 3) Task-aligned candidate generation
- Build candidate technique list from task-aligned starters.
- Build metric bundle: primary + guardrail.
- Run warning gate for class-aware metrics:
  - `dsc`, `ivm`, `c_evm`, `nh`, `ca_tnc`

Required output:
- `candidate_techniques`
- `candidate_metrics`
- `warning_gate_result`
- `warning_gate_notes`

Gate:
- If warning gate is `fail` or `unknown`, do not use class-aware metrics as primary objective.

## 4) Deterministic configuration scoring and selection
- Apply hard gates from selection policy.
- Score each technique+metric bundle with the fixed weighted formula.
- Select top candidate by threshold and tie-break rules.

Required output:
- `candidate_score_table`
- `selected_configuration`
- `selection_status` (`accepted|provisional|exploratory`)
- `selection_reasoning_summary`

Gate:
- Production recommendation requires `selection_status = accepted`.

## 5) Task-aligned initialization decision
- Set initialization policy after selected configuration is fixed.
- For initialization-sensitive methods, informative initialization is default unless justified.
- Record seed plan and comparison protocol.

Required output:
- `initialization_mode`
- `initialization_method`
- `initialization_rationale`
- `initialization_comparison_protocol`
- `initialization_stability_summary`

Gate:
- Do not run optimization with unresolved initialization mode.

## 6) Bayesian hyperparameter optimization (`bayes_opt`)
- Optimize under fixed preprocessing and initialization.
- Use primary + guardrail objective.
- Evaluate stability across seeds for top configurations.

Required output:
- `search_space`
- `objective_definition`
- `best_params`
- `optimization_trace`
- `seed_sensitivity_summary`
- `guardrail_metric_summary`

Gate:
- Optimization method must be `bayes_opt` (only).
- `grid search`, `random search`, or manual sweep loops are invalid for final recommendations.
- If top configurations are unstable across seeds, downgrade to `provisional`.

## 7) Visualization + user explanation
- Produce required visual artifacts and consistency check.
- Produce two explanation layers:
  - internal technical explanation for implementation/audit
  - user explanation in novice-friendly language
- Report residual risks and contested/unknown evidence status.
- Explicitly disclose final settings in a copyable user section.

Required output:
- `visual_artifacts`
- `visual_consistency_check`
- `technical_explanation`
- `user_explanation`
- `user_goal_restatement`
- `user_what_was_compared`
- `user_why_selected`
- `user_risk_note`
- `user_code_snippet`
- `user_code_reason`
- `final_configuration_for_users`
- `source_note_links`
- `residual_risk_statement`
- `recommendation_status`
- `report_contract_validation` (`pass|fail`)

Gate:
- If visual and metric evidence materially conflict, set `recommendation_status = exploratory`.
- If user explanation contains standalone internal jargon, set `report_contract_validation = fail` and revise wording.
- If final configuration is not explicitly disclosed to users, set `report_contract_validation = fail`.
- If concise user code and code reason are missing, set `report_contract_validation = fail`.

## Execution Contract
1. Never skip Step 1.
2. Never run Step 6 before Step 5 is fixed.
3. Never finalize without warning-gate outcome.
4. Never finalize without score table and seed-stability summary.
5. If conflict status is `contested`, do not label recommendation as definitive.
6. Do not close analysis until report-contract validation passes.
7. Do not finalize recommendations from non-`bayes_opt` optimization runs.
