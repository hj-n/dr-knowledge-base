---
id: paper-2013-pending-ref-029
title: "Stability Comparison of Dimensionality Reduction Techniques Attending to Data and Parameter Variations"
authors: "Francisco J. García-Fernández, Michel Verleysen, John A. Lee, and Ignacio Díaz"
venue: "UNKNOWN"
year: 2013
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-029-2013-stability-comparison-of-dimensionality-reduction-techniques-attending-to-data-and-par.pdf
seed_note_id: "paper-2019-mdp-visual-analytics-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- The problem with these algorithms comes from the randomness introduced in the process: the initialization is random for all nonconvex techniques, and the way in which the data points are presented in each iteration is also random only in stochastic gradient descent algorithm, so it is difﬁcult to obtain comparable projection under the same conditions.
- As these data are typically high-dimensional and so they can not be visualized directly in a two/three dimensional lattice, dimensionality reduction (DR) techniques play a key role, making a transformation of these data into a meaningful, visualizable and reduceddimensional space.
- On the other, PCA,t-SNE and SNE are not affected by this problem.

# Method Summary
- In order to improve the stability and robustness of the selected DR algorithms, we propose two simple, easily applicable and low computational pre- and post-processing methods.
- It is important to point out that our approach is a postprocessing task in the case of convex techniques, while in non-convex algorithms, the method is a pre-processing.
- The problem with these algorithms comes from the randomness introduced in the process: the initialization is random for all nonconvex techniques, and the way in which the data points are presented in each iteration is also random only in stochastic gradient descent algorithm, so it is difﬁcult to obtain comparable projection under the same conditions.
- Particularly, the application of the methodologies proposed in this paper to visual analytics tools in order to ease the knowledge discovery process by stabilizing the projections, as well as the extension of the study including other an outof-sample comparison, supervised techniques and the deﬁnition of a metric of stability for DR techniques.
- For non-convex techniques, our approach focuses on controlling the initialization of the algorithms, ﬁxing the initial conditions by ﬁxing the random seed used to generate them, while using a stochastic gradient descent algorithm to obtain the optimal solution.
- One of the simplest approaches to data projection is to preserve pairwise distances, either using an appropriate metric [Sam69,DH97] or using a probabilitybased approach [HR02, vdMH08], obtaining a pairwise distance or dissimilarity matrix respectively.
- This paper presents a study of the stability, robustness and performance of some of these dimension reduction algorithms with respect to algorithm and data parameters, which usually have a major inﬂuence in the resulting embeddings.

# When To Use / Not Use
- Use when:
  - Lee2 and Ignacio Díaz1 1University of Oviedo, Spain 2Université Catholique de Louvain, Belgium Abstract The analysis of the big volumes of data requires efﬁcient and robust dimension reduction techniques to represent data into lower-dimensional spaces, which ease human understanding.
  - For non-convex techniques, our approach focuses on controlling the initialization of the algorithms, ﬁxing the initial conditions by ﬁxing the random seed used to generate them, while using a stochastic gradient descent algorithm to obtain the optimal solution.
- Avoid when:
  - These geometric transformations include not only the variations caused by the algorithm, but also the discontinuity when changing some data or algorithm parameters, such as the order of the data points or the neighborhood parameter respectively.
  - Particularly in the case of interactive applications, the time between the action of the user and change in the display must be the shortest possible, so if the algorithm is timeconsuming, maybe it is not suitable for interactive purposes.
- Failure modes:
  - This paper presents a study of the stability, robustness and performance of some of these dimension reduction algorithms with respect to algorithm and data parameters, which usually have a major inﬂuence in the resulting embeddings.

# Metrics Mentioned
- `continuity`: referenced as part of projection-quality or reliability assessment.
- `procrustes-based quality`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- 7 García-Fernández et al. / Stability comparison of dimensionality reduction techniques attending to data and parameter variations Isomap (k=5) Experiment 1: Order of data Experiment 2: Influence of parameter Experiment 3: Incrementally changing dataset Experiment 4: Same distribution t-SNE (P=13) LLE (k=11) A B w/ Procrustes A (Random seed 1) B (Random seed 2) A (Fixed seed) B (Fixed seed) A: Original Input data.
- The problem with these algorithms comes from the randomness introduced in the process: the initialization is random for all nonconvex techniques, and the way in which the data points are presented in each iteration is also random only in stochastic gradient descent algorithm, so it is difﬁcult to obtain comparable projection under the same conditions.
- For non-convex techniques, our approach focuses on controlling the initialization of the algorithms, ﬁxing the initial conditions by ﬁxing the random seed used to generate them, while using a stochastic gradient descent algorithm to obtain the optimal solution.
- 6 García-Fernández et al. / Stability comparison of dimensionality reduction techniques attending to data and parameter variations • Locally Linear Embedding (LLE) [RS00]. • Stochastic Neighbor Embedding (SNE) [HR02]. • t-Distributed Stochastic Neighbor Embedding ( t-SNE) [vdMH08].
- These geometric transformations include not only the variations caused by the algorithm, but also the discontinuity when changing some data or algorithm parameters, such as the order of the data points or the neighborhood parameter respectively.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-029-C1 | stance: support | summary: The problem with these algorithms comes from the randomness introduced in the process: the initialization is random for all nonconvex techniques, and the way in which the data points are presented in each iteration is also random only in stochastic gradient descent algorithm, so it is difﬁcult to obtain comparable projection under the same conditions. | evidence_ids: PENDING-REF-029-E1, PENDING-REF-029-E2
- CLAIM-PENDING-REF-029-C2 | stance: support | summary: In order to improve the stability and robustness of the selected DR algorithms, we propose two simple, easily applicable and low computational pre- and post-processing methods. | evidence_ids: PENDING-REF-029-E3, PENDING-REF-029-E4
- CLAIM-PENDING-REF-029-C3 | stance: support | summary: 7 García-Fernández et al. / Stability comparison of dimensionality reduction techniques attending to data and parameter variations Isomap (k=5) Experiment 1: Order of data Experiment 2: Influence of parameter Experiment 3: Incrementally changing dataset Experiment 4: Same distribution t-SNE (P=13) LLE (k=11) A B w/ Procrustes A (Random seed 1) B (Random seed 2) A (Fixed seed) B (Fixed seed) A: Original Input data. | evidence_ids: PENDING-REF-029-E5, PENDING-REF-029-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 4 | relevance: high | note: contains initialization sensitivity or control-policy evidence
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-REF-029-E1 | page: 2, section: extracted, quote: "The problem with these algorithms comes from the randomness introduced in the process: the initialization is random for all nonconvex techniques, and the way in which the data points are presented in each iteration is also random only in stochastic gradient descent algorithm, so it is difﬁcult to obtain comparable projection under the same conditions."
- PENDING-REF-029-E2 | page: 1, section: extracted, quote: "As these data are typically high-dimensional and so they can not be visualized directly in a two/three dimensional lattice, dimensionality reduction (DR) techniques play a key role, making a transformation of these data into a meaningful, visualizable and reduceddimensional space."
- PENDING-REF-029-E3 | page: 4, section: extracted, quote: "On the other, PCA,t-SNE and SNE are not affected by this problem."
- PENDING-REF-029-E4 | page: 3, section: extracted, quote: "In order to improve the stability and robustness of the selected DR algorithms, we propose two simple, easily applicable and low computational pre- and post-processing methods."
- PENDING-REF-029-E5 | page: 3, section: extracted, quote: "It is important to point out that our approach is a postprocessing task in the case of convex techniques, while in non-convex algorithms, the method is a pre-processing."
- PENDING-REF-029-E6 | page: 4, section: extracted, quote: "Particularly, the application of the methodologies proposed in this paper to visual analytics tools in order to ease the knowledge discovery process by stabilizing the projections, as well as the extension of the study including other an outof-sample comparison, supervised techniques and the deﬁnition of a metric of stability for DR techniques."
- PENDING-REF-029-E7 | page: 3, section: extracted, quote: "For non-convex techniques, our approach focuses on controlling the initialization of the algorithms, ﬁxing the initial conditions by ﬁxing the random seed used to generate them, while using a stochastic gradient descent algorithm to obtain the optimal solution."
- PENDING-REF-029-E8 | page: 2, section: extracted, quote: "One of the simplest approaches to data projection is to preserve pairwise distances, either using an appropriate metric [Sam69,DH97] or using a probabilitybased approach [HR02, vdMH08], obtaining a pairwise distance or dissimilarity matrix respectively."
