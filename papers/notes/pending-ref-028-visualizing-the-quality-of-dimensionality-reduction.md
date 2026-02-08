---
id: paper-2013-pending-ref-028
title: "Visualizing the quality of dimensionality reduction"
authors: "Bassam Mokbel, Wouter Lueks, Andrej Gisbrecht, and Barbara Hammer"
venue: "Neurocomputing"
year: 2013
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-028-2013-visualizing-the-quality-of-dimensionality-reduction.pdf
seed_note_id: "paper-2019-mdp-visual-analytics-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- Interestingly, the measure Qi ND(K) clearly singles out positions where tearing and topological mismatches occur, while Qi NX(K) shares the problem of QNX that local rank errors can aﬀect diﬀerent regions of the curv e, thus also indicating many less pronounced points in the mapping.
- 2 Evaluation measures for dimensionality reduction DR techniques are used to map a high-dimensional dataset Ξ = {ξ1, . . . , ξ N } ⊂ RD to a low-dimensional dataset X = {x1, . . . , x N } ⊂ RL, with L < D and L = 2 or L = 3 for the purpose of visualization.
- Sim ilarly, QNX depicts a mapping quality which is not optimum for all ranks K for case (iii) although only the leftmost two clusters are stacked on top of each othe r, hence signiﬁcant distortions take place in the range K ∈ { 1, . . . , 100} only.
- 5 Conclusions We have discussed quality measures based on the co-ranking f ramework and problems which arise if quadratic regions of the matrix are u sed to deﬁne a quality measure.

# Method Summary
- While the approaches [1, 8] prov ide very eﬀective heuristics to do so, surprisingly, none of the formal DR eval uation measures have been used so far to directly visualize the quality of the projections.
- Here, we extend this framework in two ways: (i) we show that the curren t parameterization of the quality shows unpredictable behavior, even in simple settings, and we propose a diﬀerent parameterization which yields more intuitive results; (ii) we propose how to link the quality to poi nt-wise quality measures which can directly be integrated into the visualiza tion.
- The co-ranking framework in its current form, however, has a serious drawback: even if data and its projections can be directly inspec ted, it is diﬃcult to predict the characteristics of the quality measure depen ding on its parameter K, the neighborhood size.
- Further, it coincides with the measures Precision and Recall from [11] based on an information retrieval perspective, provided a local neighborhood of a point is deﬁ ned by its K-nearest neighbors in the original and the projection space, respect ively.
- These measures can be used to display, together with the DR, the quality of the projection at every p oint by means of a color value corresponding to Qi NX(K) or Qi ND(K) for relevant K.
- Based on this observation, we propose a diﬀerent parameterizatio n which yields more predictable behavior and which can directly highlight stru cturally interesting neighborhood sizes.

# When To Use / Not Use
- Use when:
  - The coloring clearly indicates the tearing of the original manifold, wit h less ambiguity in Qi ND on the right. (The sequence of class labels from the inside to the outside of the original spiral-shaped manifold is: ◦▽ 23△ .) rameters, the relevant range Ks and the tolerated rank errors κ t, since it allows users to interactively choose appropriate values accordin g to a given application.
  - 109-123) Doi link to publisher: https://doi.org/10.1016/j.neucom.2012.11.046 Version of the following full text: Author’s version preprint Downloaded from: https://hdl.handle.net/2066/117326 Download date: 2026-02-08 Note: To cite this publication please use the final published version (if applicable).
- Avoid when:
  - 2 Evaluation measures for dimensionality reduction DR techniques are used to map a high-dimensional dataset Ξ = {ξ1, . . . , ξ N } ⊂ RD to a low-dimensional dataset X = {x1, . . . , x N } ⊂ RL, with L < D and L = 2 or L = 3 for the purpose of visualization.
  - In [7], an a ggregated measure is proposed which averages the quality for values K ≤ k0 where the splitting point k0 is taken based on the distance of QNX to the baseline – however, this automatic choice is yet very sensitive to minor changes in th e data.
- Failure modes:
  - While the approaches [1, 8] prov ide very eﬀective heuristics to do so, surprisingly, none of the formal DR eval uation measures have been used so far to directly visualize the quality of the projections.

# Metrics Mentioned
- `trustworthiness`: referenced as part of projection-quality or reliability assessment.
- `continuity`: referenced as part of projection-quality or reliability assessment.
- `co-ranking`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- Here, we extend this framework in two ways: (i) we show that the curren t parameterization of the quality shows unpredictable behavior, even in simple settings, and we propose a diﬀerent parameterization which yields more intuitive results; (ii) we propose how to link the quality to poi nt-wise quality measures which can directly be integrated into the visualiza tion.
- To reduce the number of parameters and hence the complexity, we suggest to choose the tolerated error to be of the same size as the regi on of interest: κ t = Ks =: κ, resulting in a reparameterized quality where, similar to [ 6], normalization takes place to guarantee values in the interval [ 0, 1]: QND(κ) = 1 κN ∑ i≤κ ∑ j:|i−j|≤κ Qij .
- 1 Introduction With more and more nonlinear dimensionality reduction (DR) techniques becoming readily available, there is an increasing need for forma l evaluation measures to compare DR techniques, to optimize their parameters and s olutions in case of multiple optima, and to directly assess the quality of such m appings.
- In contrast, we have proposed an alternati ve parameterization scheme which yields more intuitive behavior, and by linking the co-ranking matrix to a point-wise version, which also oﬀers meaningful lo cal color values to visualize the quality of a given mapping.
- The co-ranking framework in its current form, however, has a serious drawback: even if data and its projections can be directly inspec ted, it is diﬃcult to predict the characteristics of the quality measure depen ding on its parameter K, the neighborhood size.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-028-C1 | stance: support | summary: Interestingly, the measure Qi ND(K) clearly singles out positions where tearing and topological mismatches occur, while Qi NX(K) shares the problem of QNX that local rank errors can aﬀect diﬀerent regions of the curv e, thus also indicating many less pronounced points in the mapping. | evidence_ids: PENDING-REF-028-E1, PENDING-REF-028-E2
- CLAIM-PENDING-REF-028-C2 | stance: support | summary: While the approaches [1, 8] prov ide very eﬀective heuristics to do so, surprisingly, none of the formal DR eval uation measures have been used so far to directly visualize the quality of the projections. | evidence_ids: PENDING-REF-028-E3, PENDING-REF-028-E4
- CLAIM-PENDING-REF-028-C3 | stance: support | summary: Here, we extend this framework in two ways: (i) we show that the curren t parameterization of the quality shows unpredictable behavior, even in simple settings, and we propose a diﬀerent parameterization which yields more intuitive results; (ii) we propose how to link the quality to poi nt-wise quality measures which can directly be integrated into the visualiza tion. | evidence_ids: PENDING-REF-028-E5, PENDING-REF-028-E6

# Workflow Relevance Map
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance
- step: 6 | relevance: high | note: guides reliable interpretation of projected views

# Evidence
- PENDING-REF-028-E1 | page: 6, section: extracted, quote: "Interestingly, the measure Qi ND(K) clearly singles out positions where tearing and topological mismatches occur, while Qi NX(K) shares the problem of QNX that local rank errors can aﬀect diﬀerent regions of the curv e, thus also indicating many less pronounced points in the mapping."
- PENDING-REF-028-E2 | page: 2, section: extracted, quote: "2 Evaluation measures for dimensionality reduction DR techniques are used to map a high-dimensional dataset Ξ = {ξ1, . . . , ξ N } ⊂ RD to a low-dimensional dataset X = {x1, . . . , x N } ⊂ RL, with L < D and L = 2 or L = 3 for the purpose of visualization."
- PENDING-REF-028-E3 | page: 4, section: extracted, quote: "Sim ilarly, QNX depicts a mapping quality which is not optimum for all ranks K for case (iii) although only the leftmost two clusters are stacked on top of each othe r, hence signiﬁcant distortions take place in the range K ∈ { 1, . . . , 100} only."
- PENDING-REF-028-E4 | page: 6, section: extracted, quote: "5 Conclusions We have discussed quality measures based on the co-ranking f ramework and problems which arise if quadratic regions of the matrix are u sed to deﬁne a quality measure."
- PENDING-REF-028-E5 | page: 6, section: extracted, quote: "While the approaches [1, 8] prov ide very eﬀective heuristics to do so, surprisingly, none of the formal DR eval uation measures have been used so far to directly visualize the quality of the projections."
- PENDING-REF-028-E6 | page: 2, section: extracted, quote: "Here, we extend this framework in two ways: (i) we show that the curren t parameterization of the quality shows unpredictable behavior, even in simple settings, and we propose a diﬀerent parameterization which yields more intuitive results; (ii) we propose how to link the quality to poi nt-wise quality measures which can directly be integrated into the visualiza tion."
- PENDING-REF-028-E7 | page: 2, section: extracted, quote: "The co-ranking framework in its current form, however, has a serious drawback: even if data and its projections can be directly inspec ted, it is diﬃcult to predict the characteristics of the quality measure depen ding on its parameter K, the neighborhood size."
- PENDING-REF-028-E8 | page: 3, section: extracted, quote: "Further, it coincides with the measures Precision and Recall from [11] based on an information retrieval perspective, provided a local neighborhood of a point is deﬁ ned by its K-nearest neighbors in the original and the projection space, respect ively."
