---
id: paper-2005-zadu-ref-09
title: "Supervised nonlinear dimensionality reduction for visualization and classification"
year: 2005
tags: [dr, zadu-table1-reference]
source_pdf: papers/raw/zadu-table1-references/Supervised_nonlinear_dimensionality_reduction_for_visualization_and_classification.pdf
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- —When performing visualization and classiﬁcation, people often confront the problem of dimensionality reduction.
- Isomap is one of the most promising nonlinear dimensionality reduction techniques.

# Method Summary
- The results show that S-Isomap is also an accurate and robust technique for classiﬁcation.
- In this paper, an improved version of Isomap, namely S-Isomap, is proposed.
- Unfortunately, they have a common inherent limitation: They are all linear methods while the distributions of most real-world data are nonlinear.
- Encouraging results have been reported when the test data contain little noise and are well sampled, but, as can been seen in the following sections of this paper, they are not so powerful when confronted with noisy data, which is often the case for real-world problems.

# When To Use / Not Use
- Use when:
  - Use when selecting DR reliability checks in workflow Step 3.
  - Use with complementary local/cluster/global metrics rather than a single score.
- Avoid when:
  - Avoid using this source as the only decision signal without task constraints.
- Failure modes:
  - Overfitting conclusions to a single metric family or benchmark setup.

# Metrics Mentioned
- No direct ZADU metric-ID keyword was detected in extracted text; this source is retained for contextual method evidence.

# Implementation Notes
- Keep preprocessing and seed policy fixed before comparing reliability scores across methods.
- Use this source with at least one complementary note before final recommendation text.

# Claim Atoms (For Conflict Resolution)
- CLAIM-SOURCE-09-CORE | stance: support | summary: This source contributes DR method/quality evidence relevant to metric selection. | evidence_ids: ZR09-E1

# Workflow Relevance Map
- step: 3 | relevance: high | note: Informs task-aligned metric/technique selection and metric trust calibration.
- step: 6 | relevance: high | note: Provides rationale that can be translated for end users.

# Evidence
- ZR09-E1 | page: 1, section: extracted, quote: "In this paper, an improved version of Isomap, namely S-Isomap, is proposed."
- ZR09-E2 | page: 1, section: extracted, quote: "Unfortunately, they have a common inherent limitation: They are all linear methods while the distributions of most real-world data are nonlinear."
- ZR09-E3 | page: 1, section: extracted, quote: "Encouraging results have been reported when the test data contain little noise and are well sampled, but, as can been seen in the following sections of this paper, they are not so powerful when confronted with noisy data, which is often the case for real-world problems."
- ZR09-E4 | page: 1, section: extracted, quote: "In this paper, a robust method based on the idea of Isomap, namely S-Isomap, is proposed to deal with such situation."
- ZR09-E5 | page: 2, section: extracted, quote: "Unfortunately, this scheme seems not to work very well compared with those widely used classiﬁcation methods (according to the experiments in this paper), such as BP network [10], decision tree [8], and SVM [14], [15]."
- ZR09-E6 | page: 9, section: extracted, quote: "C ONCLUSION In this paper, an improved version of Isomap, namely S-Isomap, is proposed for robust visualization and classi ﬁca- tion."
- ZR09-E7 | page: 9, section: extracted, quote: "The results show that S-Isomap is also an accurate and robust technique for classiﬁcation."
- ZR09-E8 | page: 2, section: extracted, quote: "GENG et al.: SUPERVISED NONLINEAR DIMENSIONALITY REDUCTION 1107 ACKNOWLEDGMENT The authors would like to thank the anonymous reviewers for their comments and suggestions which greatly improved this paper."
