---
id: paper-2014-pending-ref-125
title: "A methodology to compare Dimensionality Reduction algorithms in terms of loss of quality"
authors: "A. Gracia, S. Gonz /C19alez, V. Robles, and E. Menasalvas"
venue: "Information Sciences"
year: 2014
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-125-2014-a-methodology-to-compare-dimensionality-reduction-algorithms-in-terms-of-loss-of-qual.pdf
seed_note_id: "paper-2019-mdp-visual-analytics-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- Introduction The use of Dimensionality Reduction (DR) in recent decades has been motivated by the difficulties in analyzing very high dimensional data.
- In this paper we propose a methodology for comparing DR algorithms based on the concept of loss of quality.
- A methodology to compare Dimensionality Reduction algorithms in terms of loss of quality Antonio Gracia , Santiago González, Víctor Robles, Ernestina Menasalvas ABSTRACT Dimensionality Reduction (DR) is attracting more attention these days as a result of the increasing need to handle huge amounts of data effectively.
- DP methods can be divided into three groups as considered by Lee et al.[62]: Spatial distance algorithms as Multidimensional Scaling (MDS) [17], Sammon Mapping or Curvilinear Component Analysis.

# Method Summary
- In this paper we propose a methodology for comparing DR algorithms based on the concept of loss of quality.
- A methodology to compare Dimensionality Reduction algorithms in terms of loss of quality Antonio Gracia , Santiago González, Víctor Robles, Ernestina Menasalvas ABSTRACT Dimensionality Reduction (DR) is attracting more attention these days as a result of the increasing need to handle huge amounts of data effectively.
- DP methods can be divided into three groups as considered by Lee et al.[62]: Spatial distance algorithms as Multidimensional Scaling (MDS) [17], Sammon Mapping or Curvilinear Component Analysis.
- Methods Once the possible classifications of DR algorithms are presented, it is interesting to highlight those algorithms that are most used in the literature.
- In this paper, we propose a methodology that allows different DR methods to be ana­ lyzed and compared as regards the loss of quality produced by them.
- These techniques help to overcome the drawback of using the DP prin­ ciple: the manifold could be constrained with distance conditions and, in many situations, the embedding of a manifold requires some flexibility because some sub-regions must be locally stretched or shrunk to embed them into other dimen­ sional spaces.
- From the point of view of an ideal case, the preservation of the pairwise distances measured in a dataset ensures that the low-dimen­ sional embedding inherits the main geometric properties of the data, such as the overall shape.

# When To Use / Not Use
- Use when:
  - These techniques help to overcome the drawback of using the DP prin­ ciple: the manifold could be constrained with distance conditions and, in many situations, the embedding of a manifold requires some flexibility because some sub-regions must be locally stretched or shrunk to embed them into other dimen­ sional spaces.
  - However, these studies are not sufficiently complete because of the lack of quality criteria and datasets used, as well as the fact that an exhaustive analysis of the geometry preservation is not carried out throughout the entire DR process (instead, it is carried out on a particular dimensionality, usually 2).
- Avoid when:
  - Furthermore, the behavior of many data, such as a DNA Microarray, cannot be explained by means of LDR because it may contain essential multiple nonlinear relationships between attributes that cannot simply be interpreted by using linear models.
  - Polzlbauer, Survey and comparison of quality measures for self-organizing maps, in: Proceedings of the Fifth Workshop on Data Analysis (WDA'04), Elfa Academic Press, Sliezsky dom, Vysoké Tatry, Slovakia, 2004, pp.
- Failure modes:
  - Martinetz, A new quantitative measure of topology preservation in Kohonen's feature maps, in: 1994 IEEE International Conference on Neural Networks, 1994, IEEE World Congress on Computational Intelligence, vol.

# Metrics Mentioned
- `trustworthiness`: referenced as part of projection-quality or reliability assessment.
- `continuity`: referenced as part of projection-quality or reliability assessment.
- `stress`: referenced as part of projection-quality or reliability assessment.
- `co-ranking`: referenced as part of projection-quality or reliability assessment.
- `procrustes-based quality`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- The intrinsic dimensionality of data is the minimum number of parameters needed to account for the observed properties of the data [29,62].
- A methodology to compare Dimensionality Reduction algorithms in terms of loss of quality Antonio Gracia , Santiago González, Víctor Robles, Ernestina Menasalvas ABSTRACT Dimensionality Reduction (DR) is attracting more attention these days as a result of the increasing need to handle huge amounts of data effectively.
- DP methods can be divided into three groups as considered by Lee et al.[62]: Spatial distance algorithms as Multidimensional Scaling (MDS) [17], Sammon Mapping or Curvilinear Component Analysis.
- Methods Once the possible classifications of DR algorithms are presented, it is interesting to highlight those algorithms that are most used in the literature.
- In this paper, we propose a methodology that allows different DR methods to be ana­ lyzed and compared as regards the loss of quality produced by them.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-125-C1 | stance: support | summary: Introduction The use of Dimensionality Reduction (DR) in recent decades has been motivated by the difficulties in analyzing very high dimensional data. | evidence_ids: PENDING-REF-125-E1, PENDING-REF-125-E2
- CLAIM-PENDING-REF-125-C2 | stance: support | summary: In this paper we propose a methodology for comparing DR algorithms based on the concept of loss of quality. | evidence_ids: PENDING-REF-125-E3, PENDING-REF-125-E4
- CLAIM-PENDING-REF-125-C3 | stance: support | summary: The intrinsic dimensionality of data is the minimum number of parameters needed to account for the observed properties of the data [29,62]. | evidence_ids: PENDING-REF-125-E5, PENDING-REF-125-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-REF-125-E1 | page: 1, section: extracted, quote: "Introduction The use of Dimensionality Reduction (DR) in recent decades has been motivated by the difficulties in analyzing very high dimensional data."
- PENDING-REF-125-E2 | page: 2, section: extracted, quote: "In this paper we propose a methodology for comparing DR algorithms based on the concept of loss of quality."
- PENDING-REF-125-E3 | page: 1, section: extracted, quote: "A methodology to compare Dimensionality Reduction algorithms in terms of loss of quality Antonio Gracia , Santiago González, Víctor Robles, Ernestina Menasalvas ABSTRACT Dimensionality Reduction (DR) is attracting more attention these days as a result of the increasing need to handle huge amounts of data effectively."
- PENDING-REF-125-E4 | page: 3, section: extracted, quote: "DP methods can be divided into three groups as considered by Lee et al.[62]: Spatial distance algorithms as Multidimensional Scaling (MDS) [17], Sammon Mapping or Curvilinear Component Analysis."
- PENDING-REF-125-E5 | page: 4, section: extracted, quote: "Methods Once the possible classifications of DR algorithms are presented, it is interesting to highlight those algorithms that are most used in the literature."
- PENDING-REF-125-E6 | page: 1, section: extracted, quote: "In this paper, we propose a methodology that allows different DR methods to be ana­ lyzed and compared as regards the loss of quality produced by them."
- PENDING-REF-125-E7 | page: 4, section: extracted, quote: "These techniques help to overcome the drawback of using the DP prin­ ciple: the manifold could be constrained with distance conditions and, in many situations, the embedding of a manifold requires some flexibility because some sub-regions must be locally stretched or shrunk to embed them into other dimen­ sional spaces."
- PENDING-REF-125-E8 | page: 3, section: extracted, quote: "From the point of view of an ideal case, the preservation of the pairwise distances measured in a dataset ensures that the low-dimen­ sional embedding inherits the main geometric properties of the data, such as the overall shape."
