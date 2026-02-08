---
id: paper-2021-pending-ref-104
title: "Implicit Multidimensional Projection of Local Subspaces"
authors: "Rongzheng Bian, Yumeng Xue, Liang Zhou, Jian Zhang, Baoquan Chen, Daniel Weiskopf, and Yunhai Wang"
venue: "IEEE Transactions on Visualization and Computer Graphics"
year: 2021
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-104-2021-implicit-multidimensional-projection-of-local-subspaces.pdf
seed_note_id: "paper-2025-jeon-reliable-va-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- This is a difficult problem [48] addressed in extensive previous work.
- Therefore, we assume that any reasonable projection finds an optimal target location for each data point P by solving the following optimization problem to arrive at the projected data points π(P): min π(P) f (P, π(P)) . (9) In other words, any resulting point π(P) “sits” in a local minimum with respect to the cost function.
- In contrast, more recent DR methods, e.g., locally linear embedding (LLE) [36] and t-distributed stochastic neighbor embedding (t-SNE) [46], seek to map nearby points in the high-dimensional space to nearby points in the low-dimensional space.
- In contrast, our method is designed for multidimensional projections, can be applied to high-dimensional data, considers multiple vectors to faithfully describe local subspaces, and—most importantly—works consistently with any DR method.

# Method Summary
- 4.1 Multidimensional Projection of Points We present a general definition of multidimensional projections that will be used as a basis for our extended projection approach.
- 4.4 Implicit Vector Transformation Nonlinear projection methods typically find the relationship between P and π(P) by optimizing an objective function f (P, π(P)).
- Abstract—We propose a visualization method to understand the effect of multidimensional projection on local subspaces, using implicit function differentiation.
- Multidimensional projection takes points at P to corresponding locations p ∈ Rd (d ≤ D) in the lower-dimensional visualization space: π : RD → Rd , P 7→ p = π(P) . (1) Our discussion and derivation is independent of the choice of π, i.e., we formulate our approach to work with any linear or nonlinear multidimensional projection.
- Our approach extends traditional multidimensional projection in three ways: (1) extract the local linear subspace in the original space, (2) project the subspace in a way that is consistent with the DR technique applied to the data points, and (3) visualize the information from the projection of the subspace.
- Since we do not change the basic intuition associated with traditional multidimensional visualization, our approach readily fits in any existing DR visualization pipeline, regardless of whether it uses linear or nonlinear multidimensional projections.
- In contrast, more recent DR methods, e.g., locally linear embedding (LLE) [36] and t-distributed stochastic neighbor embedding (t-SNE) [46], seek to map nearby points in the high-dimensional space to nearby points in the low-dimensional space.

# When To Use / Not Use
- Use when:
  - A prominent case is the linear projection by PCA [18]: πPCA(P) = M P = p , (2) where M is a d × D matrix consisting of the first d eigenvectors (used as row vectors) that result from the diagonalization in PCA, i.e., in our typical use case of 2D visualization, these are the two eigenvectors corresponding to the two largest eigenvalues.
  - Here, the goal is to recognize how generalized axis lines (visualized as contours) change according to user-specified infinitesimal perturbations; small changes of the data are modeled in the original multidimensional space and their effect on the projected axes in the DR display are computed by automatic differentiation.
- Avoid when:
  - Our work has a different goal in mind: we want to understand the shape and orientation of the local structure, and, furthermore, global correlations of data points; and we use implicit differentiation to accurately transform basis vectors in the multidimensional local neighborhood.
  - Embedding Projector [42] allows the user to explore DR data as a 3D 1https://github.com/VisLabWang/DRImplicitVecXform scatterplot and shows DR processes by animation; however, it is a general tool for overview and more in-depth analysis is not supported.
- Failure modes:
  - Since we do not change the basic intuition associated with traditional multidimensional visualization, our approach readily fits in any existing DR visualization pipeline, regardless of whether it uses linear or nonlinear multidimensional projections.

# Metrics Mentioned
- `trustworthiness`: referenced as part of projection-quality or reliability assessment.
- `stress`: referenced as part of projection-quality or reliability assessment.
- `kl divergence`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- Therefore, we assume that any reasonable projection finds an optimal target location for each data point P by solving the following optimization problem to arrive at the projected data points π(P): min π(P) f (P, π(P)) . (9) In other words, any resulting point π(P) “sits” in a local minimum with respect to the cost function.
- Most nonlinear multidimensional projection techniques employ some complex optimization approaches to arrive at the projection π.
- 4.4 Implicit Vector Transformation Nonlinear projection methods typically find the relationship between P and π(P) by optimizing an objective function f (P, π(P)).
- Abstract—We propose a visualization method to understand the effect of multidimensional projection on local subspaces, using implicit function differentiation.
- Multidimensional projection takes points at P to corresponding locations p ∈ Rd (d ≤ D) in the lower-dimensional visualization space: π : RD → Rd , P 7→ p = π(P) . (1) Our discussion and derivation is independent of the choice of π, i.e., we formulate our approach to work with any linear or nonlinear multidimensional projection.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-104-C1 | stance: support | summary: This is a difficult problem [48] addressed in extensive previous work. | evidence_ids: PENDING-REF-104-E1, PENDING-REF-104-E2
- CLAIM-PENDING-REF-104-C2 | stance: support | summary: 4.1 Multidimensional Projection of Points We present a general definition of multidimensional projections that will be used as a basis for our extended projection approach. | evidence_ids: PENDING-REF-104-E3, PENDING-REF-104-E4
- CLAIM-PENDING-REF-104-C3 | stance: support | summary: Therefore, we assume that any reasonable projection finds an optimal target location for each data point P by solving the following optimization problem to arrive at the projected data points π(P): min π(P) f (P, π(P)) . (9) In other words, any resulting point π(P) “sits” in a local minimum with respect to the cost function. | evidence_ids: PENDING-REF-104-E5, PENDING-REF-104-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 4 | relevance: high | note: contains initialization sensitivity or control-policy evidence
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-REF-104-E1 | page: 2, section: extracted, quote: "This is a difficult problem [48] addressed in extensive previous work."
- PENDING-REF-104-E2 | page: 4, section: extracted, quote: "Therefore, we assume that any reasonable projection finds an optimal target location for each data point P by solving the following optimization problem to arrive at the projected data points π(P): min π(P) f (P, π(P)) . (9) In other words, any resulting point π(P) “sits” in a local minimum with respect to the cost function."
- PENDING-REF-104-E3 | page: 1, section: extracted, quote: "In contrast, more recent DR methods, e.g., locally linear embedding (LLE) [36] and t-distributed stochastic neighbor embedding (t-SNE) [46], seek to map nearby points in the high-dimensional space to nearby points in the low-dimensional space."
- PENDING-REF-104-E4 | page: 2, section: extracted, quote: "In contrast, our method is designed for multidimensional projections, can be applied to high-dimensional data, considers multiple vectors to faithfully describe local subspaces, and—most importantly—works consistently with any DR method."
- PENDING-REF-104-E5 | page: 3, section: extracted, quote: "4.1 Multidimensional Projection of Points We present a general definition of multidimensional projections that will be used as a basis for our extended projection approach."
- PENDING-REF-104-E6 | page: 4, section: extracted, quote: "4.4 Implicit Vector Transformation Nonlinear projection methods typically find the relationship between P and π(P) by optimizing an objective function f (P, π(P))."
- PENDING-REF-104-E7 | page: 1, section: extracted, quote: "Abstract—We propose a visualization method to understand the effect of multidimensional projection on local subspaces, using implicit function differentiation."
- PENDING-REF-104-E8 | page: 3, section: extracted, quote: "Multidimensional projection takes points at P to corresponding locations p ∈ Rd (d ≤ D) in the lower-dimensional visualization space: π : RD → Rd , P 7→ p = π(P) . (1) Our discussion and derivation is independent of the choice of π, i.e., we formulate our approach to work with any linear or nonlinear multidimensional projection."
