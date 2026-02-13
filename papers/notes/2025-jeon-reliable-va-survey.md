---
id: paper-2025-jeon-reliable-va-survey
title: "Unveiling High-dimensional Backstage: A Survey for Reliable Visual Analytics with Dimensionality Reduction"
authors: "Hyeon Jeon; Hyunwook Lee; Yun-Hsin Kuo; Taehyun Yang; Daniel Archambault; Sungahn Ko; Takanori Fujiwara; Kwan-Liu Ma; Jinwook Seo"
venue: "CHI 2025"
year: 2025
tags: [dr, reliability, workflow, survey, visual_analytics]
source_pdf: papers/raw/jeon25chi (4).pdf
seed_note_id: ""
evidence_level: high
updated_at: 2026-02-13
---

# Problem
- DR is essential in visual analytics but can generate unreliable conclusions when distortion, configuration, and interpretation risks are unmanaged.
- Prior guidance often over-focused on selecting DR techniques, while many failures actually occur across the broader workflow (preprocessing, evaluation, visualization, and sensemaking transitions).
- The paper targets this gap by building a workflow-wide reliability synthesis rather than a technique-only recommendation list.

# Method Summary
- The paper conducts a systematic review of 133 papers from visualization, HCI, and ML-adjacent literature focused on DR reliability.
- It contributes a workflow model that explicitly separates analyst-side and machine-side stages, then maps reliability issues to these stages.
- It proposes a four-dimension taxonomy (Stage, Problem, Aim, Solution) to classify reliability interventions and failure modes.
- It includes a meta-analysis that surfaces recurring research clusters and identifies field-wide gaps (for example, many new techniques but limited evaluation/interpretation support).
- The result is a workflow-level reliability frame usable for policy design, checklist design, and structured recommendation reporting.

# When To Use / Not Use
- Use when building DR guidance that must remain reliable across the whole analysis lifecycle, not only at method selection time.
- Use when designing operational checkpoints for preprocessing, method configuration, quantitative evaluation, and user explanation.
- Use when you need a principled taxonomy to group reliability issues and map them to concrete mitigation strategies.
- Do not assume that choosing a “good method” alone makes analysis reliable; instability, hyperparameter choices, and visualization interpretation can still break conclusions.
- Failure mode: workflows that skip stage-by-stage validation can produce coherent narratives from projections that are still structurally unreliable.

# Metrics Mentioned
- The survey is metric-agnostic at the policy level: it does not prescribe one dominant metric family.
- It positions metrics as one component inside a wider reliability system that also includes configuration policy, workflow controls, and interpretation safeguards.
- It explicitly highlights that metric-level improvements are insufficient when instability and suboptimal hyperparameter settings are not handled.

# Implementation Notes
- Operationalize reliability checks per stage rather than as a single post-hoc score:
  - preprocessing and configuration sanity,
  - DR execution and stability,
  - quantitative evaluation validity,
  - visualization/sensemaking communication.
- Keep analyst-machine loop explicit: recommendations should document what was configured, what changed, and how those changes affect interpretation risk.
- Treat suboptimal hyperparameter settings and method instability as first-class failure sources, not secondary caveats.
- Use taxonomy-driven documentation to keep KB updates structured: each new paper should map to stage/problem/aim/solution relevance.
- In user-facing output, translate this internal workflow rigor into simple explanations of what was checked, what was selected, and what uncertainty remains.

# Claim Atoms (For Conflict Resolution)
- CLAIM-JEON25S-C1 | stance: support | summary: DR reliability failures are workflow-wide and cannot be solved by technique choice alone. | evidence_ids: JEON25S-E1, JEON25S-E2, JEON25S-E6
- CLAIM-JEON25S-C2 | stance: support | summary: The paper contributes a workflow model and taxonomy for systematic reliability diagnosis. | evidence_ids: JEON25S-E3, JEON25S-E4, JEON25S-E5
- CLAIM-JEON25S-C3 | stance: support | summary: Hyperparameter misconfiguration and inherent instability are explicit recurring failure mechanisms. | evidence_ids: JEON25S-E7
- CLAIM-JEON25S-C4 | stance: support | summary: Reliability interventions must cover the full process from preprocessing to visualization and sensemaking. | evidence_ids: JEON25S-E8, JEON25S-E9, JEON25S-E10

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports clearer analyst-intent modeling as an upstream reliability prerequisite.
- step: 2 | relevance: high | note: emphasizes preprocessing as part of reliability control, not a neutral boilerplate stage.
- step: 3 | relevance: high | note: links method selection to workflow-aware reliability reasoning instead of single-method preference.
- step: 4 | relevance: high | note: strengthens deterministic acceptance/rejection logic with explicit problem taxonomy.
- step: 6 | relevance: high | note: highlights hyperparameter and instability management as core reliability gates.
- step: 7 | relevance: high | note: supports transparent uncertainty reporting and user communication of residual risk.

# Evidence
- JEON25S-E1 | page: 1, section: abstract, quote: "visual analytics using DR often face unreliability"
- JEON25S-E2 | page: 1, section: introduction, quote: "distortions are inevitable in DR projections."
- JEON25S-E3 | page: 1, section: abstract, quote: "we review 133 papers that address the unreliability of visual analytics using DR."
- JEON25S-E4 | page: 1, section: abstract, quote: "a workflow model that describes the interaction between analysts and machines in visual analytics using DR"
- JEON25S-E5 | page: 1, section: abstract, quote: "a taxonomy that identifies where and why reliability issues arise within the workflow"
- JEON25S-E6 | page: 2, section: survey positioning, quote: "covering the entire analytic process—from preprocessing to visualizations and sensemaking."
- JEON25S-E7 | page: 2, section: introduction, quote: "suboptimal hyperparameter settings [106, 217] or the inherent instability of certain DR techniques [106, 137]"
- JEON25S-E8 | page: 6, section: workflow model figure caption, quote: "The model explains how an Analyst and a Machine interact while conducting visual analytics with DR."
- JEON25S-E9 | page: 8, section: taxonomy, quote: "We derive four dimensions—Stages, Problems, Aims, and Solutions—"
- JEON25S-E10 | page: 8, section: taxonomy, quote: "Our taxonomy builds upon the workflow model"
