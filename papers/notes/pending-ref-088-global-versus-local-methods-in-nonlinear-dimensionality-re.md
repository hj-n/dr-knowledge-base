---
id: paper-2002-pending-ref-088
title: "Global Versus Local Methods in Nonlinear Dimensionality Reduction"
authors: "Vin Silva and Joshua Tenenbaum"
venue: "UNKNOWN"
year: 2002
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-088-2002-global-versus-local-methods-in-nonlinear-dimensionality-reduction.pdf
seed_note_id: "paper-2019-mdp-visual-analytics-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- 1 Introduction In this paper we discuss the problem of non-linear dimension ality reduction (NLDR): the task of recovering meaningful low-dimensional structureshidden in high-dimensional data.
- An example might be a set of pixel images of an individual's face observed under different pose and lighting conditions; the task is to identify the und erlying variables (pose angles, direction of light, distance from camera, etc.) given only the high-dimensional pixel image data.
- 4 Conclusion Local approaches to nonlinear dimensionality reduction su ch as LLE or Laplacian Eigenmaps have two principal advantages over a global approach such as Isomap: they tolerate a certain amount of curvature and they lead naturally to a sparse eigenvalue problem.
- 2 Isomap for conformal embeddings 2.1 Manifold learning and geometric invariants We can view the problem of manifold learning as an attempt to invert a generative model for a set of observations.

# Method Summary
- MA 02139 jbt@ai.mit.edu Abstract Recently proposed algorithms for nonlinear dimensionality reduction fall broadly into two categories which have different advantage s and disadvantages: global (Isomap [1,2]), and local (Locally Linear Embedding [3], Laplacian Eigenmaps [4]).
- Abstract Recently proposed algorithms for nonlinear dimensionality reduction fall broadly into two categories which have different advantage s and disadvantages: global (Isomap [1,2]), and local (Locally Linear Embedding [3], Laplacian Eigenmaps [4]).
- The class of conformal embeddings includes all isometric embeddings as well as many other classes of map s, including stereographic projections like the Mercator projection.
- In this paper we describe var iants of the Isomap algorithm which overcome two of the apparent disadvantages of the global approach.
- All four algorithms returned a two-dimensional embedding of the data.
- Then for k / p the required optimal k -dimensional embedding vectors are given as the columns of the matrix: L /= /2 /6 /6 /6 /4 p / /1 / /~ v T /1 p / /2 / /~ v T /2 . . . p / k / /~ v T k /3 /7 /7 /7 /5 The embedded vectors are automatically mean-centered, and the principal components of the embedded points are aligned with the axes, most signi®ca nt ®rst.
- The local approaches have two principal advantages: (1) computational ef®ciency: they involve only sparse matrix computations which may yield a polynomial speedup; (2) representational capacity: they may giveuseful results on a broader range of manifolds, whose local geometry is close to Euclidean, but whose global geometry may not be.

# When To Use / Not Use
- Use when:
  - The local approaches have two principal advantages: (1) computational ef®ciency: they involve only sparse matrix computations which may yield a polynomial speedup; (2) representational capacity: they may giveuseful results on a broader range of manifolds, whose local geometry is close to Euclidean, but whose global geometry may not be.
  - In situations where both Isomap and C-Isomap are applicable, it may be preferable to use Isomap, since it is less susceptible to local ¯uctuati ons in the sample density.
- Avoid when:
  - Ordinary Isomap recovers the rectangular structure correctly provided that the neighborhood parameter is not too large (in this casek /= /8 works).
  - Each edge x i x j in the graph is weighted by its Euclidean length j x i /? x j j , or by some other useful metric.
- Failure modes:
  - Tenenbaum Department of Brain and Cognitive Sciences, Massachusetts Institute of Technology, Cambridge.

# Metrics Mentioned
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- Given //; / /> /0 , for a suitable choice of neighborhood size parameter / or k , we have /1 /? / / recovered distance original distance / /1 /+ / with probability at least /1 /? / , provided that the sample size is suf®ciently large. [The formula is taken to hold for all pairs of points simultaneously.] C-Isomap is a simple variation on Isomap.
- These methods combine the advantages of PCA and MDSÐcomputationa l ef®ciency; few free parameters; non-iterative global optimisation of a natural cost functionÐwith the ability to disentangle the Swiss roll and other classes of nonlinear data manifold.
- More generally there is a wider class of techniques, involving iterative optimization pro cedures, by which unsatisfactory linear representations obtained by PCA or MDS may be ªimprovedº towards more successful non-linear representations of the data.
- Given //; / /> /0 , for a suitable choice of neighborhood size parameter k , we have /1 /? / / recovered distance original distance / /1 /+ / with probability at least /1 /? / , provided that the sample size is suf®ciently large.
- In this case the parameters were left-right pose angle and distance from the camera. /1/2/8 / /1/2/8 color pixel images were converted into grayscale and treated as vectors in 16384-dimensional space.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-088-C1 | stance: support | summary: 1 Introduction In this paper we discuss the problem of non-linear dimension ality reduction (NLDR): the task of recovering meaningful low-dimensional structureshidden in high-dimensional data. | evidence_ids: PENDING-REF-088-E1, PENDING-REF-088-E2
- CLAIM-PENDING-REF-088-C2 | stance: support | summary: MA 02139 jbt@ai.mit.edu Abstract Recently proposed algorithms for nonlinear dimensionality reduction fall broadly into two categories which have different advantage s and disadvantages: global (Isomap [1,2]), and local (Locally Linear Embedding [3], Laplacian Eigenmaps [4]). | evidence_ids: PENDING-REF-088-E3, PENDING-REF-088-E4
- CLAIM-PENDING-REF-088-C3 | stance: support | summary: Given //; / /> /0 , for a suitable choice of neighborhood size parameter / or k , we have /1 /? / / recovered distance original distance / /1 /+ / with probability at least /1 /? / , provided that the sample size is suf®ciently large. [The formula is taken to hold for all pairs of points simultaneously.] C-Isomap is a simple variation on Isomap. | evidence_ids: PENDING-REF-088-E5, PENDING-REF-088-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-REF-088-E1 | page: 1, section: extracted, quote: "1 Introduction In this paper we discuss the problem of non-linear dimension ality reduction (NLDR): the task of recovering meaningful low-dimensional structureshidden in high-dimensional data."
- PENDING-REF-088-E2 | page: 1, section: extracted, quote: "An example might be a set of pixel images of an individual's face observed under different pose and lighting conditions; the task is to identify the und erlying variables (pose angles, direction of light, distance from camera, etc.) given only the high-dimensional pixel image data."
- PENDING-REF-088-E3 | page: 7, section: extracted, quote: "4 Conclusion Local approaches to nonlinear dimensionality reduction su ch as LLE or Laplacian Eigenmaps have two principal advantages over a global approach such as Isomap: they tolerate a certain amount of curvature and they lead naturally to a sparse eigenvalue problem."
- PENDING-REF-088-E4 | page: 2, section: extracted, quote: "2 Isomap for conformal embeddings 2.1 Manifold learning and geometric invariants We can view the problem of manifold learning as an attempt to invert a generative model for a set of observations."
- PENDING-REF-088-E5 | page: 1, section: extracted, quote: "MA 02139 jbt@ai.mit.edu Abstract Recently proposed algorithms for nonlinear dimensionality reduction fall broadly into two categories which have different advantage s and disadvantages: global (Isomap [1,2]), and local (Locally Linear Embedding [3], Laplacian Eigenmaps [4])."
- PENDING-REF-088-E6 | page: 1, section: extracted, quote: "Abstract Recently proposed algorithms for nonlinear dimensionality reduction fall broadly into two categories which have different advantage s and disadvantages: global (Isomap [1,2]), and local (Locally Linear Embedding [3], Laplacian Eigenmaps [4])."
- PENDING-REF-088-E7 | page: 2, section: extracted, quote: "The class of conformal embeddings includes all isometric embeddings as well as many other classes of map s, including stereographic projections like the Mercator projection."
- PENDING-REF-088-E8 | page: 1, section: extracted, quote: "In this paper we describe var iants of the Isomap algorithm which overcome two of the apparent disadvantages of the global approach."
