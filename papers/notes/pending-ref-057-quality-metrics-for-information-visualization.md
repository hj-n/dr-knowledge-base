---
id: paper-2018-pending-ref-057
title: "Quality Metrics for Information Visualization"
authors: "M. Behrisch, M. Blumenschein, N. W. Kim, L. Shao, M. El-Assady, J. Fuchs, D. Seebacher, A. Diehl, U. Brandes, H. Pfister, T. Schreck, D. Weiskopf, and D. A. Keim"
venue: "Computer Graphics Forum"
year: 2018
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-057-2018-quality-metrics-for-information-visualization.pdf
seed_note_id: "paper-2024-large-scale-text-spatialization"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- However, the current data to be visualized puts more and more challenges on visualization designers: high-dimensional spaces, complex relationships, or the sheer amount of data to be visualized demand a careful choice of the visual variables for a faithful representation of the underlying dataset.
- This visualization is designed to satisfy three quality criteria to optimize the layer ordering; namely, “(1) minimizing layer distortion, (2) maximizing the available space within each layer to accommodate rich thematic content, and (3) ensuring visual proximity of layers to be proportional to their semantic similarity” [ LZP∗09].
- Limitations of this Survey This work surveys mid-level perceptual quality metrics by motivating the needs and beneﬁts of quality metrics in the respective 653 visualization subﬁeld, summarizing the challenges and outlining analysis tasks supported by quality metrics in the literature.
- Their biggest disadvantage is that these textual guidelines are often derived from simpliﬁed task- and context settings that often cannot be generalized to real-world environments and problem settings. (ii) In other visualization subﬁelds, purely Heuristic Approaches prevail.

# Method Summary
- As one of the ﬁrst approaches to address Stacked Graph optimization, Byron and Wattenberg [BW08] describe layout algorithms based on the following steps; (1) computing the layer-geometry; (2) choosing the appropriate coloring scheme; (3) labeling of layers; and (4) layer ordering.
- Other approaches start from the constraint that the visualization type is ﬁxed, e.g., Scatter Plots for projections of high-dimensional data and tackle the question which views can be discarded due to the high overlap or visual clutter [BS04, TBB∗10].
- Methodology and Structure Our surveying methodology is based on an iterative and comparative summarization approach, inspired by the grounded theory analysis of Strauss and Corbin [SC94] and the structured content analysis theory of Mayring [May00].
- Their metrics comprise a user-deﬁned weighting of correlation dimensions (by a Pearson correlation coefﬁcient), outlier analysis (by a grid and density based approach), and cluster detection (by applying a subspace clustering algorithm).
- Second, we noticed that, although a wide range of approaches was presented under the headline of quality metrics, only little effort has been devoted to describing the methodological and conceptual background of these approaches.
- Recently, Wang et al. [WWZ ∗17] proposed a novel approach to combine existing aspect ratio selection methods, thus allowing to take advantage of their respective advantages, such as parameterization- or sampling invariances.
- These are often used within the layout algorithms to determine the layer ordering and are, therefore, only useful as evaluation metrics in the broader context, i.e., when comparing the visual quality of different approaches.

# When To Use / Not Use
- Use when:
  - While basic research has been presented in this ﬁeld, such as various task taxonomies with different levels-of-details [BM13,KAF ∗08,LPP∗06,Shn96], only a few works focused on automatically quantifying the current exploration task at hand.
  - While we are trying to educate the user in the selection of QMs for a respective visualization type, a systematic answer to the question “Which QM is the best one for my circumstances?” remains extremely challenging.
- Avoid when:
  - These works either focus on evaluating the connection between human perception and quality metrics (effectiveness) or demonstrating the usefulness of quality metrics base on various use case scenarios (efﬁciency).
  - Notably, many works cited in this survey acknowledge and explicitly mention the fact that the evaluation of QMs is not backed up with perception-focused user studies.
- Failure modes:
  - We consider visual patterns as the target elements of the exploration process, while visual anti-patterns, such as noise, will distract the user without adding to his/her understanding about the dataset and task at hand. (iv) Optimization Algorithm makes use of a quality criterion and -concept to derive, e.g., a ranked or ﬁltered list of visualization instantiations (or views).

# Metrics Mentioned
- `continuity`: referenced as part of projection-quality or reliability assessment.
- `stress`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- The approaches can be separated into quality criteria measuring the quality of one visualization deﬁnition and optimization algorithms that optimize the adjustable parameters.
- We consider visual patterns as the target elements of the exploration process, while visual anti-patterns, such as noise, will distract the user without adding to his/her understanding about the dataset and task at hand. (iv) Optimization Algorithm makes use of a quality criterion and -concept to derive, e.g., a ranked or ﬁltered list of visualization instantiations (or views).
- QMs are developed with a speciﬁc goal in mind, such as ﬁnding clutter-free visualizations or visualizations with a speciﬁc interpretable visual pattern. (ii) Visualization Deﬁnition φ is an instantiation of the parameter space Φ deﬁning the appearance of a speciﬁc visualization type.
- Bertini et al. [ BTK11] pointed out that all quality metrics that work in the image space try to simulate the human pattern recognition machinery and therefore, it is needed to validate and tune the metrics in a way that the parameters take models of human perception into account.
- As one of the ﬁrst approaches to address Stacked Graph optimization, Byron and Wattenberg [BW08] describe layout algorithms based on the following steps; (1) computing the layer-geometry; (2) choosing the appropriate coloring scheme; (3) labeling of layers; and (4) layer ordering.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-057-C1 | stance: support | summary: However, the current data to be visualized puts more and more challenges on visualization designers: high-dimensional spaces, complex relationships, or the sheer amount of data to be visualized demand a careful choice of the visual variables for a faithful representation of the underlying dataset. | evidence_ids: PENDING-REF-057-E1, PENDING-REF-057-E2
- CLAIM-PENDING-REF-057-C2 | stance: support | summary: As one of the ﬁrst approaches to address Stacked Graph optimization, Byron and Wattenberg [BW08] describe layout algorithms based on the following steps; (1) computing the layer-geometry; (2) choosing the appropriate coloring scheme; (3) labeling of layers; and (4) layer ordering. | evidence_ids: PENDING-REF-057-E3, PENDING-REF-057-E4
- CLAIM-PENDING-REF-057-C3 | stance: support | summary: The approaches can be separated into quality criteria measuring the quality of one visualization deﬁnition and optimization algorithms that optimize the adjustable parameters. | evidence_ids: PENDING-REF-057-E5, PENDING-REF-057-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-REF-057-E1 | page: 1, section: extracted, quote: "However, the current data to be visualized puts more and more challenges on visualization designers: high-dimensional spaces, complex relationships, or the sheer amount of data to be visualized demand a careful choice of the visual variables for a faithful representation of the underlying dataset."
- PENDING-REF-057-E2 | page: 25, section: extracted, quote: "This visualization is designed to satisfy three quality criteria to optimize the layer ordering; namely, “(1) minimizing layer distortion, (2) maximizing the available space within each layer to accommodate rich thematic content, and (3) ensuring visual proximity of layers to be proportional to their semantic similarity” [ LZP∗09]."
- PENDING-REF-057-E3 | page: 2, section: extracted, quote: "Limitations of this Survey This work surveys mid-level perceptual quality metrics by motivating the needs and beneﬁts of quality metrics in the respective 653 visualization subﬁeld, summarizing the challenges and outlining analysis tasks supported by quality metrics in the literature."
- PENDING-REF-057-E4 | page: 7, section: extracted, quote: "Their biggest disadvantage is that these textual guidelines are often derived from simpliﬁed task- and context settings that often cannot be generalized to real-world environments and problem settings. (ii) In other visualization subﬁelds, purely Heuristic Approaches prevail."
- PENDING-REF-057-E5 | page: 25, section: extracted, quote: "As one of the ﬁrst approaches to address Stacked Graph optimization, Byron and Wattenberg [BW08] describe layout algorithms based on the following steps; (1) computing the layer-geometry; (2) choosing the appropriate coloring scheme; (3) labeling of layers; and (4) layer ordering."
- PENDING-REF-057-E6 | page: 3, section: extracted, quote: "Other approaches start from the constraint that the visualization type is ﬁxed, e.g., Scatter Plots for projections of high-dimensional data and tackle the question which views can be discarded due to the high overlap or visual clutter [BS04, TBB∗10]."
- PENDING-REF-057-E7 | page: 8, section: extracted, quote: "Methodology and Structure Our surveying methodology is based on an iterative and comparative summarization approach, inspired by the grounded theory analysis of Strauss and Corbin [SC94] and the structured content analysis theory of Mayring [May00]."
- PENDING-REF-057-E8 | page: 5, section: extracted, quote: "Their metrics comprise a user-deﬁned weighting of correlation dimensions (by a Pearson correlation coefﬁcient), outlier analysis (by a grid and density based approach), and cluster detection (by applying a subspace clustering algorithm)."
