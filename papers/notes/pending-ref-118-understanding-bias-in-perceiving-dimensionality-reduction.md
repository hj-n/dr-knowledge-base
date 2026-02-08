---
id: paper-2025-pending-ref-118
title: "Understanding Bias in Perceiving Dimensionality Reduction Projections"
authors: "Seoyoung Doh, Hyeon Jeon, Sungbok Shin, Ghulam Jilani Quadri, Nam Wook Kim, and Jinwook Seo"
venue: "UNKNOWN"
year: 2025
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-118-2025-understanding-bias-in-perceiving-dimensionality-reduction-projections.pdf
seed_note_id: "paper-2025-stop-misusing-tsne-umap"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- This issue is particularly concerning for researchers and data analysts who regularly perform visual analytics with high-dimensional datasets but have limited DR literacy, as their vulnerability to the bias threatens the reliability of their scientific discoveries [5].
- Here, faithfulness [26, 25, 16], the degree to which the structural characteristics of the original data are preserved without distortions, should be prioritized to ensure that the projection reliably supports the tasks.
- We first introduce the theory, then discuss how this theory aligns with our problem statement and the bias in perceiving DR projections.

# Method Summary
- In the second phase, we present participants with the same projections alongside artificially created faithfulness scores that contradict the visual interestingness rankings from phase 1.
- After each session, we determine the visual interestingness rankings of the 20 projections based on the participants’ 50 pairwise selections using an active ranking algorithm [12].
- In the first phase, we present participants with pairs of projections and ask them to select the one that are more visually interesting (H1).
- Note that this algorithm also determines which pairs of projections to present to participants in each trial.
- Additionally, we present faithfulness scores for the projections.
- 1). *e-mail: 0303dsy@snu.ac.kr †e-mail: hj@hcil.snu.ac.kr ‡e-mail: sungbok.shin@inria.fr §e-mail: quadri@ou.edu ¶e-mail: nam.wook.kim@bc.edu ||e-mail: jseo@snu.ac.kr, corresponding author This bias towards visual interestingness [28, 35, 8], the degree to which projections exhibit perceptually appealing patterns, may prompt analysts to select unsuitable techniques.
- To do so, we verify the following hypotheses: • (H1) Visual interestingnessmore strongly influencesanalytical preference of DR projections than faithfulness does. • (H2) The tendency observed in H1 becomes more pronounced when the color encoding of classes is provided. • (H3) The tendency observed in H1 becomes more pronounced with shorter exposure time to stimuli.

# When To Use / Not Use
- Use when:
  - 3.2.2 Phase 2: Analytical Preference Phase 2 shares most design choices and stimuli with Phase 1, except that we request analytical preferences: participants are guided to select projections that they wish to use for cluster analysis.
  - Our results verify the bias towards visual interestingness over faithfulness in determining analytical preference of DR projections, i.e., the degree to which analysts prefer to use projections for their analysis.
- Avoid when:
  - Also, to minimize potential bias from participants’ background knowledge, we use generic labels (metrics A through E) for each pair of faithfulness scores, rather than actual metric names.
  - These findings prompt discussions on design strategies that can help mitigate bias in perceiving DR projections, enabling more reliable use of DR in visual analytics and communications.
- Failure modes:
  - We assign visual interestingness scores (our target variable) using a linear transformation: projection with rank r receives score 21− r, to align with the use of linear regression.

# Metrics Mentioned
- `trustworthiness`: referenced as part of projection-quality or reliability assessment.
- `continuity`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- However, even with the same dataset, DR projections can show different visual patterns depending on the chosen technique and hyperparameters [26, 36].
- Therefore, analysts must carefully select both techniques and hyperparameters to align with their analytical objectives [36, 16].
- Upon selection, the result feeds into an active ranking algorithm [12] that identifies optimal comparison pairs to efficiently converge on stable rankings with minimal iterations.
- Initialization is critical for preserving global data structure in both t-sne and umap.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-118-C1 | stance: support | summary: This issue is particularly concerning for researchers and data analysts who regularly perform visual analytics with high-dimensional datasets but have limited DR literacy, as their vulnerability to the bias threatens the reliability of their scientific discoveries [5]. | evidence_ids: PENDING-REF-118-E1, PENDING-REF-118-E2
- CLAIM-PENDING-REF-118-C2 | stance: support | summary: In the second phase, we present participants with the same projections alongside artificially created faithfulness scores that contradict the visual interestingness rankings from phase 1. | evidence_ids: PENDING-REF-118-E3, PENDING-REF-118-E4
- CLAIM-PENDING-REF-118-C3 | stance: support | summary: However, even with the same dataset, DR projections can show different visual patterns depending on the chosen technique and hyperparameters [26, 36]. | evidence_ids: PENDING-REF-118-E5, PENDING-REF-118-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 4 | relevance: high | note: contains initialization sensitivity or control-policy evidence
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-REF-118-E1 | page: 1, section: extracted, quote: "This issue is particularly concerning for researchers and data analysts who regularly perform visual analytics with high-dimensional datasets but have limited DR literacy, as their vulnerability to the bias threatens the reliability of their scientific discoveries [5]."
- PENDING-REF-118-E2 | page: 1, section: extracted, quote: "Here, faithfulness [26, 25, 16], the degree to which the structural characteristics of the original data are preserved without distortions, should be prioritized to ensure that the projection reliably supports the tasks."
- PENDING-REF-118-E3 | page: 2, section: extracted, quote: "We first introduce the theory, then discuss how this theory aligns with our problem statement and the bias in perceiving DR projections."
- PENDING-REF-118-E4 | page: 1, section: extracted, quote: "In the second phase, we present participants with the same projections alongside artificially created faithfulness scores that contradict the visual interestingness rankings from phase 1."
- PENDING-REF-118-E5 | page: 3, section: extracted, quote: "After each session, we determine the visual interestingness rankings of the 20 projections based on the participants’ 50 pairwise selections using an active ranking algorithm [12]."
- PENDING-REF-118-E6 | page: 2, section: extracted, quote: "In the first phase, we present participants with pairs of projections and ask them to select the one that are more visually interesting (H1)."
- PENDING-REF-118-E7 | page: 3, section: extracted, quote: "Note that this algorithm also determines which pairs of projections to present to participants in each trial."
- PENDING-REF-118-E8 | page: 3, section: extracted, quote: "Additionally, we present faithfulness scores for the projections."
