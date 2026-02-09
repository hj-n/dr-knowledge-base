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
updated_at: 2026-02-08
---

# Problem
- DR-based visual analytics remains vulnerable to unreliable interpretations due to inevitable projection distortions and workflow failures.
- Prior guidance often focused narrowly on technique selection while under-covering broader reliability breakdown points.
- The paper addresses this gap through a large cross-paper reliability survey and workflow-level synthesis.

# Method Summary
- It reviews 133 papers across visualization/HCI-related venues focused on DR reliability concerns.
- It contributes a workflow model describing analyst-machine interaction over the full DR analysis lifecycle.
- It builds a taxonomy of where and why reliability issues arise and summarizes mitigation strategies from the literature.
- It highlights research imbalance: heavy focus on new techniques versus interpretation/evaluation support.

# When To Use / Not Use
- Use as a workflow-level reliability reference when building DR guidance beyond pure algorithm selection.
- Use when designing checkpoints for distortion awareness, parameter tuning, and instability handling.
- Avoid limiting reliability policy to one stage (for example only method choice); failures occur across stages.
- Failure mode: assuming awareness of method purpose is sufficient despite unresolved instability/hyperparameter issues.

# Metrics Mentioned
- The survey is not tied to one metric; it frames reliability as multi-stage and multi-factor.
- It reinforces combining projection-quality checks with process controls (workflow checkpoints).
- It explicitly notes hyperparameter and instability issues as recurrent reliability drivers.

# Implementation Notes
- Embed reliability checks at each workflow step, especially before and after method/parameter selection.
- Keep distortions explicit in user communication; do not treat projection as direct ground truth.
- Record parameter settings and instability observations as part of recommendation evidence.
- Use this workflow framing to extend caution/tip documentation in the KB.

# Claim Atoms (For Conflict Resolution)
- CLAIM-JEON25-C1 | stance: support | summary: Reliability issues in DR visual analytics are workflow-wide, not method-only. | evidence_ids: JEON25S-E1, JEON25S-E2
- CLAIM-JEON25-C2 | stance: support | summary: A workflow model and issue taxonomy improve systematic reliability handling. | evidence_ids: JEON25S-E3, JEON25S-E4
- CLAIM-JEON25-C3 | stance: support | summary: Hyperparameter settings and method instability remain major unresolved reliability risks. | evidence_ids: JEON25S-E5

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports clearer intent capture as reliability prerequisite.
- step: 3 | relevance: high | note: links method selection to distortion-aware reliability reasoning.
- step: 4 | relevance: high | note: explicitly highlights hyperparameter/instability reliability risks.
- step: 6 | relevance: high | note: strengthens explanation of uncertainty and limitations to users.

# Evidence
- JEON25S-E1 | page: 1, section: Abstract, quote: "visual analytics using DR often face unreliability"
- JEON25S-E2 | page: 1, section: Introduction, quote: "distortions are inevitable in DR projections"
- JEON25S-E3 | page: 3, section: Abstract, quote: "contribute ... a workflow model"
- JEON25S-E4 | page: 1, section: Abstract, quote: "taxonomy that identifies where and why reliability issues arise"
- JEON25S-E5 | page: 2, section: Introduction, quote: "suboptimal hyperparameter settings ... inherent instability"
- JEON25S-E6 | page: 1, section: Survey Scope, quote: "review 133 papers"
