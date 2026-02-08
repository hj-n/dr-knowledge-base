---
id: paper-2021-pending-ref-169
title: "HoroPCA: Hyperbolic Dimensionality Reduction via Horospherical Projections"
authors: "Ines Chami, Albert Gu, Dat P Nguyen, and Christopher Re"
venue: "UNKNOWN"
year: 2021
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-169-2021-horopca-hyperbolic-dimensionality-reduction-via-horospherical-projections.pdf
seed_note_id: "paper-2025-jeon-reliable-va-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- Generalizing PCA to manifolds is a challenging problem that has been studied for decades, starting with Principal Geodesic Analysis (PGA) [ 10] which parameterizes subspaces using tangent vectors at the mean of the data, and maximizes distances from projections to the mean to ﬁnd optimal directions.
- This suggests that our distance-based formulation of the variance (Eq. (4)) effectively captures variations in the 4https://github.com/HazyResearch/HoroPCA 5All mentioned PCA methods, including HOROPCA, optimize for some forms of variance but not Fr´echet variance or distortion.
- By focusing on the core problem of extracting principal directions, HOROPCA theoretically better preserves information in the original data such as distances, compared to previous generalizations of PCA.
- Benjamini & Makarychev [2] adapt the Euclidean Johnson–Lindenstrauss transform to hyperbolic geometry and obtain a distortion bound when the dataset size is not too big compared to the target dimension.

# Method Summary
- Given directions, PCA relies on: (1) a parameterization of subspaces spanned by these directions, (2) a method of projection onto subspaces that preserves information in these directions, and (3) an objective to optimize, namely the variance explained by projections.
- To maximally preserve information in the original data, we propose a new projection method that uses horospheres, a generalization of complementary directions for hyperbolic space.
- The PCA algorithm is then deﬁned as combining these primitives: given a dataset, it chooses directions that maximize the variance of projections onto a subspace spanned by those directions, so that the resulting sequence of directions optimally explains the data.
- They do not seek an analog of Euclidean directions or projections, but nevertheless implicitly use a projection method based on pushing points along horocycles, which shares many properties with our horospherical projections.
- 6 Related Work PCA methods in Riemannian manifolds We ﬁrst review some approaches to extending PCA to general Riemannian geometries, of which hyperbolic geometry is a special case.
- HOROPCA Because we have generalized the notions of ﬂag, projection, and variance to hyperbolic geometry, the HOROPCA algorithm can be deﬁned in the same fashion.
- Here, we propose HOROPCA , a dimensionality reduction method for data deﬁned in hyperbolic spaces which better preserves the properties of Euclidean PCA.

# When To Use / Not Use
- Use when:
  - By considering a more general type of submanifolds, Hauberg [14] gives another way to avoid the sensitive dependence on Fr´echet mean.
  - Recent works have also used Busemann functions for hyperbolic prototype learning [19, 34].
- Avoid when:
  - Because of the close analogy between HOROPCA and Euclidean PCA, these steps can easily map to the hyperbolic case, where we (i) use HOROPCA to ﬁnd principal directions (ideal points), (ii) calculate the Busemann coordinates along these directions, and (iii) normalize them as Euclidean coordinates.
  - This: 1. alleviates the need to use d extra parameters to search for an appropriate base point, and 2. simpliﬁes computations, since in the Poincar´e model, geodesics submanifolds that go through the origin are simply linear subspaces, which are easier to deal with.
- Failure modes:
  - Cvetkovski & Crovella [9] and Sala et al. [27] are examples of hyperbolic multidimensional scaling methods, which seek conﬁgurations of points in lower-dimensional hyperbolic spaces whose pairwise distances best approximate a given dissimilarity matrix.

# Metrics Mentioned
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- Generalizing PCA to manifolds is a challenging problem that has been studied for decades, starting with Principal Geodesic Analysis (PGA) [ 10] which parameterizes subspaces using tangent vectors at the mean of the data, and maximizes distances from projections to the mean to ﬁnd optimal directions.
- Given directions, PCA relies on: (1) a parameterization of subspaces spanned by these directions, (2) a method of projection onto subspaces that preserves information in these directions, and (3) an objective to optimize, namely the variance explained by projections.
- This: 1. alleviates the need to use d extra parameters to search for an appropriate base point, and 2. simpliﬁes computations, since in the Poincar´e model, geodesics submanifolds that go through the origin are simply linear subspaces, which are easier to deal with.
- In hyperbolic geometry, this construction coincides with the one based on geodesic hulls that we use in Section 3, except that it applies to points inside Hd instead of ideal points and thus needs more parameters to parameterize a ﬂag (see Remark A.8).
- Instead of using the exponential map at a base point, it parameterizes K-dimensional subspaces as the barycenter loci ofK + 1 points.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-169-C1 | stance: support | summary: Generalizing PCA to manifolds is a challenging problem that has been studied for decades, starting with Principal Geodesic Analysis (PGA) [ 10] which parameterizes subspaces using tangent vectors at the mean of the data, and maximizes distances from projections to the mean to ﬁnd optimal directions. | evidence_ids: PENDING-REF-169-E1, PENDING-REF-169-E2
- CLAIM-PENDING-REF-169-C2 | stance: support | summary: Given directions, PCA relies on: (1) a parameterization of subspaces spanned by these directions, (2) a method of projection onto subspaces that preserves information in these directions, and (3) an objective to optimize, namely the variance explained by projections. | evidence_ids: PENDING-REF-169-E3, PENDING-REF-169-E4
- CLAIM-PENDING-REF-169-C3 | stance: support | summary: Generalizing PCA to manifolds is a challenging problem that has been studied for decades, starting with Principal Geodesic Analysis (PGA) [ 10] which parameterizes subspaces using tangent vectors at the mean of the data, and maximizes distances from projections to the mean to ﬁnd optimal directions. | evidence_ids: PENDING-REF-169-E5, PENDING-REF-169-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-REF-169-E1 | page: 2, section: extracted, quote: "Generalizing PCA to manifolds is a challenging problem that has been studied for decades, starting with Principal Geodesic Analysis (PGA) [ 10] which parameterizes subspaces using tangent vectors at the mean of the data, and maximizes distances from projections to the mean to ﬁnd optimal directions."
- PENDING-REF-169-E2 | page: 9, section: extracted, quote: "This suggests that our distance-based formulation of the variance (Eq. (4)) effectively captures variations in the 4https://github.com/HazyResearch/HoroPCA 5All mentioned PCA methods, including HOROPCA, optimize for some forms of variance but not Fr´echet variance or distortion."
- PENDING-REF-169-E3 | page: 1, section: extracted, quote: "By focusing on the core problem of extracting principal directions, HOROPCA theoretically better preserves information in the original data such as distances, compared to previous generalizations of PCA."
- PENDING-REF-169-E4 | page: 12, section: extracted, quote: "Benjamini & Makarychev [2] adapt the Euclidean Johnson–Lindenstrauss transform to hyperbolic geometry and obtain a distortion bound when the dataset size is not too big compared to the target dimension."
- PENDING-REF-169-E5 | page: 1, section: extracted, quote: "Given directions, PCA relies on: (1) a parameterization of subspaces spanned by these directions, (2) a method of projection onto subspaces that preserves information in these directions, and (3) an objective to optimize, namely the variance explained by projections."
- PENDING-REF-169-E6 | page: 2, section: extracted, quote: "To maximally preserve information in the original data, we propose a new projection method that uses horospheres, a generalization of complementary directions for hyperbolic space."
- PENDING-REF-169-E7 | page: 1, section: extracted, quote: "The PCA algorithm is then deﬁned as combining these primitives: given a dataset, it chooses directions that maximize the variance of projections onto a subspace spanned by those directions, so that the resulting sequence of directions optimally explains the data."
- PENDING-REF-169-E8 | page: 12, section: extracted, quote: "They do not seek an analog of Euclidean directions or projections, but nevertheless implicitly use a projection method based on pushing points along horocycles, which shares many properties with our horospherical projections."
