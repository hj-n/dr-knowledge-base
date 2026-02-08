---
id: paper-2011-pending-ref-072
title: "Piecewise laplacian-based projection for interactive data exploration and organization"
authors: "F. V. Paulovich, D. M. Eler, J. Poco, , C. P. Botha, R. Minghim, and L. G. Nonato"
venue: "Information"
year: 2011
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-072-2011-piecewise-laplacian-based-projection-for-interactive-data-exploration-and-organizatio.pdf
seed_note_id: "paper-2019-mdp-visual-analytics-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- To tackle this problem, we proposed a visualization-based approach to aid in the analysis and comprehension of the pre-processing effects in text mining.
- For the text mining task, pre-preprocessing effects are shown by means of correct classiﬁcation rates from classiﬁers, and a visualization approach is also employed to show the impact of pre-processing methods in document similarities and cluster formation.
- In this paper, we used an automatic approach based on Otsu’s threshold selection method [24], which is an approach proposed to estimate a good low-frequency cut; • Term weighting: in this step, we can set weights for each term.
- In such an approach, graphical representations were computed with multidimensional projection techniques to show the group formation in 2D space and the document similarities described in the vector space model.

# Method Summary
- For the text mining task, pre-preprocessing effects are shown by means of correct classiﬁcation rates from classiﬁers, and a visualization approach is also employed to show the impact of pre-processing methods in document similarities and cluster formation.
- In this paper, we used an automatic approach based on Otsu’s threshold selection method [24], which is an approach proposed to estimate a good low-frequency cut; • Term weighting: in this step, we can set weights for each term.
- In such an approach, graphical representations were computed with multidimensional projection techniques to show the group formation in 2D space and the document similarities described in the vector space model.
- To validate this visual approach, we compared the quality of each projection with the traditional approach based on classiﬁcation rates, and for that, we used the k-nearest neighbor and naive Bayes classiﬁers.
- For that, once all vector space models are computed, a multidimensional visualization approach creates a graphical representation (projection) to represent the document similarities in a 2D space.
- Therefore, we propose a methodology to vary distinct combinations of pre-processing steps and to analyze which pre-processing combination allows high precision.
- To tackle this problem, we proposed a visualization-based approach to aid in the analysis and comprehension of the pre-processing effects in text mining.

# When To Use / Not Use
- Use when:
  - Based on these results, for SentiWordNet, no pre-processing reaches the best result; for SenticNet, the best pre-processing method is the combination of stemming and stop words; and for naive Bayes, the analyst could choose only to use stop words or stemming and stop words.
  - In order to analyze the effects of pre-processing and parameter conﬁgurations in text and opinion mining tasks, quality measures are used to verify which pre-processing step leads to the best mining result [3].
- Avoid when:
  - SentiWordNet reaches the best precision with stop words elimination, presenting a different result from the training dataset; SenticNet reaches the best precision with stemming and stop words, presenting a consistent behavior when compared with the training dataset; and naive Bayes also presents a consistent behavior, presenting the best results with stemming and stop words and only using stop words.
  - Vector Space Model SentiWordNet SenticNet Naive Bayes No Stem-No Stop Words 72.04% 62.90% 55.91% No Stem-Stop Words 73.12% 63.44% 62.90% Stem-No Stop Words 77.42% 62.37% 62.37% Stem-Stop Words 72.58% 62.37% 65.05% There is no consistency among the mining techniques used in this experiment, that is each one reaches a better precision with a distinct vector space model.
- Failure modes:
  - Some of these processing steps are presented in the following: • Document selection: ﬁlters which documents will be used in the text mining task; • Tokenization: identiﬁes the terms that will be considered in the pre-processing; • Stop-word elimination: several terms are not relevant to mining tasks and can be eliminated in this step.

# Metrics Mentioned
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- The visual analysis facilitates the comprehension of pre-processing effects on document similarities, that is what steps or parameter conﬁguration can improve both groups’ cohesion and separation or the correct classiﬁcation rate.
- In order to analyze the effects of pre-processing and parameter conﬁgurations in text and opinion mining tasks, quality measures are used to verify which pre-processing step leads to the best mining result [3].
- Usually, the correct classiﬁcation rate is employed to verify the quality of VSMs computed from a distinct combination of pre-processing steps or parameter conﬁguration.
- However, the pre-processing phase is less focused on the text mining scenario [ 2] due to its non-automatic nature, in which the user needs to deﬁne parameters.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-072-C1 | stance: support | summary: To tackle this problem, we proposed a visualization-based approach to aid in the analysis and comprehension of the pre-processing effects in text mining. | evidence_ids: PENDING-REF-072-E1, PENDING-REF-072-E2
- CLAIM-PENDING-REF-072-C2 | stance: support | summary: For the text mining task, pre-preprocessing effects are shown by means of correct classiﬁcation rates from classiﬁers, and a visualization approach is also employed to show the impact of pre-processing methods in document similarities and cluster formation. | evidence_ids: PENDING-REF-072-E3, PENDING-REF-072-E4
- CLAIM-PENDING-REF-072-C3 | stance: support | summary: The visual analysis facilitates the comprehension of pre-processing effects on document similarities, that is what steps or parameter conﬁguration can improve both groups’ cohesion and separation or the correct classiﬁcation rate. | evidence_ids: PENDING-REF-072-E5, PENDING-REF-072-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-REF-072-E1 | page: 12, section: extracted, quote: "To tackle this problem, we proposed a visualization-based approach to aid in the analysis and comprehension of the pre-processing effects in text mining."
- PENDING-REF-072-E2 | page: 4, section: extracted, quote: "For the text mining task, pre-preprocessing effects are shown by means of correct classiﬁcation rates from classiﬁers, and a visualization approach is also employed to show the impact of pre-processing methods in document similarities and cluster formation."
- PENDING-REF-072-E3 | page: 5, section: extracted, quote: "In this paper, we used an automatic approach based on Otsu’s threshold selection method [24], which is an approach proposed to estimate a good low-frequency cut; • Term weighting: in this step, we can set weights for each term."
- PENDING-REF-072-E4 | page: 12, section: extracted, quote: "In such an approach, graphical representations were computed with multidimensional projection techniques to show the group formation in 2D space and the document similarities described in the vector space model."
- PENDING-REF-072-E5 | page: 12, section: extracted, quote: "To validate this visual approach, we compared the quality of each projection with the traditional approach based on classiﬁcation rates, and for that, we used the k-nearest neighbor and naive Bayes classiﬁers."
- PENDING-REF-072-E6 | page: 4, section: extracted, quote: "For that, once all vector space models are computed, a multidimensional visualization approach creates a graphical representation (projection) to represent the document similarities in a 2D space."
- PENDING-REF-072-E7 | page: 1, section: extracted, quote: "Therefore, we propose a methodology to vary distinct combinations of pre-processing steps and to analyze which pre-processing combination allows high precision."
- PENDING-REF-072-E8 | page: 11, section: extracted, quote: "Based on these results, for SentiWordNet, no pre-processing reaches the best result; for SenticNet, the best pre-processing method is the combination of stemming and stop words; and for naive Bayes, the analyst could choose only to use stop words or stemming and stop words."
