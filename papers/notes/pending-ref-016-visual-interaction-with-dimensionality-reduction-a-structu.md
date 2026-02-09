---
id: paper-2017-pending-ref-016
title: "Visual Interaction with Dimensionality Reduction: A Structured Literature Analysis"
authors: "D. Sacha et al"
venue: "IEEE Transactions on Visualization and Computer Graphics"
year: 2017
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-016-2017-visual-interaction-with-dimensionality-reduction-a-structured-literature-analysis.pdf
seed_note_id: "paper-2019-mdp-visual-analytics-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- Another framework describes the problem of DR as a two-stage process [12]: it ﬁrst maps high-dimensional data to a lowerdimensional space, then allows another stage to reduce it to 2D for visualization.
- Especially novice analysts with less mathematical skills face problems of interpreting different DR concepts (e.g., linear vs. non-linear models) in a 2D-representation where the actual meaning of the axis is lost.
- It will be a challenge to design and conduct a fair comparative assessment of different interaction scenarios, as they depend on many factors, such as implementation, user experience or tasks.
- A common approach to overcome this challenge is to involve analysts more closely, enabling them to investigate and adapt standard methods through interactive visualizations [39].

# Method Summary
- Each algorithm was assigned to a higher-level category of Distance Based (DB), Linear Projection (LP), Graph/F orce-Directed (FD), Neural Network (NN), General,o r Other (one approach did not match any others – “data driven feature selection”).
- Nonlinear DR ﬁnds either a mapping function or only output coordinates for the data set, interpreted through proximities or distances of output data; for example, mappings are sought to preserve pairwise data distances in multidimensional scaling (MDS), small distances in Sammon mapping, distances along a neighborhood graph in Isomap, or neighborhood relationships in neighbor embedding methods [54, 55].
- As a result we arrived at seven scenarios for DR interaction, encoding “how the DR pipeline is changed” (see Section 4), the interaction paradigm (“how the interaction is performed”, see Section 5), the DR Method(s) or Algorithm(s), and combined machine learning techniques such as clustering or classiﬁcation .
- S1-S3 operate on the data, such as by changing data values or annotating labels (blue); S4 operates on the feature space, such as by changing distance functions or the projection matrix (cyan); and S5-S7 directly affect the DR algorithms (or additional ML models) (green).
- Therefore, it yields a generic approach toward interacting with the output of DR methods, which is one part of our human-in-the-loop process model; i.e., observation-level interaction directly ﬁts in our proposed process of interaction with DR methods.
- 5F URTHER INSIGHTS In this section, we analyze the interaction scenarios in different contexts, such as the interaction paradigm, the combined DR algorithms or other machine learning methods, as well as a temporal perspective.
- This methodological approach is based on identifying and reﬁning categories from a representative set of qualitative data, here papers, which are then used to incrementally build up a theoretical model (Section 6).

# When To Use / Not Use
- Use when:
  - General approaches appear in 5 papers, whereas Neural Networks were used 3 times (all self organizing maps).
  - However, all the aforementioned works do not take into account V A or user interaction.
- Avoid when:
  - 241-250 https://dx.doi.org/10.1109/TVCG.2016.2598495 2R ELATED WORK This study is related to previous work in several ways: it is concerned with general theoretical models of V A and their relationship to machine learning; it makes use of DR methods; it adopts basic ways of interacting with data visualizations; and it is related to the general idea of self-reﬂection in the visualization and V A community.
  - V on Landesberger et al. [56] deﬁne an interaction taxonomy that is suitable for tracking and analyzing user actions in V A, and provides two types of data processing interactions: data changes, such as editing or selecting data, and processing changes, such as scheme or parameter changes.
- Failure modes:
  - First, we checked if the paper is a visualization application or technique paper, and if it handles “abstract data.” (We intended to exclude theory and evaluation papers, as well as papers focused on unrelated or tangential topics such as volume rendering or physical ﬂow data).

# Metrics Mentioned
- `continuity`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- V on Landesberger et al. [56] deﬁne an interaction taxonomy that is suitable for tracking and analyzing user actions in V A, and provides two types of data processing interactions: data changes, such as editing or selecting data, and processing changes, such as scheme or parameter changes.
- Finally, parameter sets or conﬁgurations can be set indirectly, such as when the analyst is offered several visualization recommendations or previously deﬁned parameter sets, and may compare them to select the most appropriate one.
- This was followed by 5 related papers published in 2007, where a wider range of interaction techniques such as S4 Feature Selection & Emphasis, S2 Annotation & Labeling , and S5 DR Parameter Tuning were included.
- It allows the analyst to explore data, feature, parameter and model spaces, taking advantage of their understanding of the data, application domain, and experience in the analysis task at hand.
- An ideal system would provide ﬂexible access to a range of DR algorithms, distance functions, optimization algorithms or quality metrics, and offer many of the interaction types we identiﬁed.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-016-C1 | stance: support | summary: Another framework describes the problem of DR as a two-stage process [12]: it ﬁrst maps high-dimensional data to a lowerdimensional space, then allows another stage to reduce it to 2D for visualization. | evidence_ids: PENDING-REF-016-E1, PENDING-REF-016-E2
- CLAIM-PENDING-REF-016-C2 | stance: support | summary: Each algorithm was assigned to a higher-level category of Distance Based (DB), Linear Projection (LP), Graph/F orce-Directed (FD), Neural Network (NN), General,o r Other (one approach did not match any others – “data driven feature selection”). | evidence_ids: PENDING-REF-016-E3, PENDING-REF-016-E4
- CLAIM-PENDING-REF-016-C3 | stance: support | summary: V on Landesberger et al. [56] deﬁne an interaction taxonomy that is suitable for tracking and analyzing user actions in V A, and provides two types of data processing interactions: data changes, such as editing or selecting data, and processing changes, such as scheme or parameter changes. | evidence_ids: PENDING-REF-016-E5, PENDING-REF-016-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-REF-016-E1 | page: 2, section: extracted, quote: "Another framework describes the problem of DR as a two-stage process [12]: it ﬁrst maps high-dimensional data to a lowerdimensional space, then allows another stage to reduce it to 2D for visualization."
- PENDING-REF-016-E2 | page: 7, section: extracted, quote: "Especially novice analysts with less mathematical skills face problems of interpreting different DR concepts (e.g., linear vs. non-linear models) in a 2D-representation where the actual meaning of the axis is lost."
- PENDING-REF-016-E3 | page: 9, section: extracted, quote: "It will be a challenge to design and conduct a fair comparative assessment of different interaction scenarios, as they depend on many factors, such as implementation, user experience or tasks."
- PENDING-REF-016-E4 | page: 1, section: extracted, quote: "A common approach to overcome this challenge is to involve analysts more closely, enabling them to investigate and adapt standard methods through interactive visualizations [39]."
- PENDING-REF-016-E5 | page: 6, section: extracted, quote: "Each algorithm was assigned to a higher-level category of Distance Based (DB), Linear Projection (LP), Graph/F orce-Directed (FD), Neural Network (NN), General,o r Other (one approach did not match any others – “data driven feature selection”)."
- PENDING-REF-016-E6 | page: 2, section: extracted, quote: "Nonlinear DR ﬁnds either a mapping function or only output coordinates for the data set, interpreted through proximities or distances of output data; for example, mappings are sought to preserve pairwise data distances in multidimensional scaling (MDS), small distances in Sammon mapping, distances along a neighborhood graph in Isomap, or neighborhood relationships in neighbor embedding methods [54, 55]."
- PENDING-REF-016-E7 | page: 3, section: extracted, quote: "As a result we arrived at seven scenarios for DR interaction, encoding “how the DR pipeline is changed” (see Section 4), the interaction paradigm (“how the interaction is performed”, see Section 5), the DR Method(s) or Algorithm(s), and combined machine learning techniques such as clustering or classiﬁcation ."
- PENDING-REF-016-E8 | page: 7, section: extracted, quote: "S1-S3 operate on the data, such as by changing data values or annotating labels (blue); S4 operates on the feature space, such as by changing distance functions or the projection matrix (cyan); and S5-S7 directly affect the DR algorithms (or additional ML models) (green)."
