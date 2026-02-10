# Internal Report Schema

This file defines internal field names for technical audit artifacts.
Do not expose these field names in user-facing answers.

## Task Confirmation
- `primary_task_axis`
- `task_subtype`
- `axis_confidence`
- `task_confirmation_quote`
- `success_criteria`

## Preprocessing
- `preprocessing_profile_id`
- `distance_metric`
- `preprocessing_plan`
- `data_constraints`
- `frozen_preprocessing_signature`

## Candidate Generation and Selection
- `candidate_techniques`
- `candidate_metrics`
- `warning_gate_result`
- `warning_gate_notes`
- `candidate_score_table`
- `selected_configuration`
- `selection_status`
- `selection_reasoning_summary`
- `aligned_candidate_coverage`

## Initialization and Optimization
- `initialization_mode`
- `initialization_method`
- `initialization_rationale`
- `initialization_comparison_protocol`
- `initialization_stability_summary`
- `optimizer`
- `search_space`
- `objective_definition`
- `best_params`
- `optimization_trace`
- `seed_sensitivity_summary`
- `safety_check_summary`

## Communication and Delivery
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
- `report_contract_validation`
