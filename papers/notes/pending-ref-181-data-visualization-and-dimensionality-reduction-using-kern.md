---
id: paper-2007-pending-ref-181
title: "Data Visualization and Dimensionality Reduction Using Kernel Maps With a Reference Point"
authors: "J.A.K. Suykens"
venue: "IEEE Transactions on Neural Networks"
year: 2007
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-181-2007-data-visualization-and-dimensionality-reduction-using-kernel-maps-with-a-reference-po.pdf
seed_note_id: "paper-2009-comparative-review-dr-techniques"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- Kernel-based learning methods have proven to be successful in many applications in different areas, especially, on problems with high-dimensional input spaces.
- The constrained optimization problem (10) is the primal problem with unknown coordinates of the data in the lower dimensional space, the error variables , and the vector for the primal representation of the model (11) evaluated at any point in the input space (and hence also allows for out-of-sample extensions).
- Moreover, the conditioning of the numerical algorithms for computing the eigenvector solutions is inferior (even if one speci ﬁes to compute only a subset of the eigenvectors such as with the Matlab functions and ) with respect to the well-conditioned linear systems to be solved in problems P2 and P3.
- Despite the importance of studies in learning theory with bounds on the generalization error, mainly for classiﬁcation and regression problems [8], [28], practitioners often still rely on validation-based methods, due to the lack of sharp bounds in general.

# Method Summary
- The kernel map with reference point approach can be tuned then in a similar fashion as kernel-based regression and classiﬁcation methods with linear system solving, though for a problem of unsupervised instead of supervised learning now.
- We describe now two practical algorithms: a cross-validation method with grid search and a method with use of a randomized validation set that is more suitable for interactive data exploration.
- In this paper, we propose a new kernel-based method in the framework of least squares support vector machines (LS-SVMs).
- The kernel map approach that we propose in this paper makes use of a reference point.
- For this purpose, we proposed a new method of kernel maps with a reference point.
- While these methods are often applied in practice with a relatively small number of nearest neighbors (e.g., ten), for achieving results similar to the solution of kernel maps with a reference point, a very large number of nearest neighbors is needed in this case (different from the choices illustrated, e.g., in [2]): (LLE) 200 nearest neighbors, (Laplacian eigenmap) 300 nearest neighbors, and .
- The following two criteria are considered here with use of a validation set : • normalized metric multidimensional scaling criterion (normalized metric MDS) (25) • normalized locally linear embedding criterion (normalized LLE) (26) with denoting the th entry of matrix ; where denotes the set of tuning parameters to be determined.

# When To Use / Not Use
- Use when:
  - He has served as a Director and Organizer of the NATO Advanced Study Institute on Learning Theory and Practice (Leuven, Belgium, 2002), as a Program Cochair for the International Joint Conference on Neural Networks 2004 and the International Symposium on Nonlinear Theory and its Applications 2005, and as an Organizer of the International Symposium on Synchronization in Complex Networks 2007.
  - The following two criteria are considered here with use of a validation set : • normalized metric multidimensional scaling criterion (normalized metric MDS) (25) • normalized locally linear embedding criterion (normalized LLE) (26) with denoting the th entry of matrix ; where denotes the set of tuning parameters to be determined.
- Avoid when:
  - The formulations are in terms of constrained optimization problems with use of a feature map in the primal problem and a related positive-deﬁnite kernel in the dual (which is the problem in the Lagrange multipliers that are related to the constraints).
  - Kernel maps with a reference point: illustration of Algorithm 1 using a tenfold cross-validation procedure on the spiral data. (a) Two best res ults selected according to criterion /81 . (b) Two best results according to criterion /81 .
- Failure modes:
  - This gives an indication to the user about whether the observed structure can be trusted in an objective way (in the sense of good generalization) or is rather a “fake” structure corresponding to a situation of data overﬁtting.

# Metrics Mentioned
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- The following two criteria are considered here with use of a validation set : • normalized metric multidimensional scaling criterion (normalized metric MDS) (25) • normalized locally linear embedding criterion (normalized LLE) (26) with denoting the th entry of matrix ; where denotes the set of tuning parameters to be determined.
- The constrained optimization problem (10) is the primal problem with unknown coordinates of the data in the lower dimensional space, the error variables , and the vector for the primal representation of the model (11) evaluated at any point in the input space (and hence also allows for out-of-sample extensions).
- The formulations are in terms of constrained optimization problems with use of a feature map in the primal problem and a related positive-deﬁnite kernel in the dual (which is the problem in the Lagrange multipliers that are related to the constraints).
- SUYKENS: DATA VISUALIZA TION AND DIMENSIONALITY REDUCTION USING KERNEL MAPS WITH A REFERENCE POINT 1507 For existing methods, one often varies then the tuning parameters of the method that results in different data visualizations of a given data set.
- The different curves on both plots correspond to the ten runs in the tenfold cross validation. tuning parameters are set as follows: (LLE and Hessian LLE) ten nearest neighbors, (Laplacian eigenmap) ten nearest neighbors, , (diffusion map) , .
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-181-C1 | stance: support | summary: Kernel-based learning methods have proven to be successful in many applications in different areas, especially, on problems with high-dimensional input spaces. | evidence_ids: PENDING-REF-181-E1, PENDING-REF-181-E2
- CLAIM-PENDING-REF-181-C2 | stance: support | summary: The kernel map with reference point approach can be tuned then in a similar fashion as kernel-based regression and classiﬁcation methods with linear system solving, though for a problem of unsupervised instead of supervised learning now. | evidence_ids: PENDING-REF-181-E3, PENDING-REF-181-E4
- CLAIM-PENDING-REF-181-C3 | stance: support | summary: The following two criteria are considered here with use of a validation set : • normalized metric multidimensional scaling criterion (normalized metric MDS) (25) • normalized locally linear embedding criterion (normalized LLE) (26) with denoting the th entry of matrix ; where denotes the set of tuning parameters to be determined. | evidence_ids: PENDING-REF-181-E5, PENDING-REF-181-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance
- step: 6 | relevance: high | note: guides reliable interpretation of projected views

# Evidence
- PENDING-REF-181-E1 | page: 1, section: extracted, quote: "Kernel-based learning methods have proven to be successful in many applications in different areas, especially, on problems with high-dimensional input spaces."
- PENDING-REF-181-E2 | page: 3, section: extracted, quote: "The constrained optimization problem (10) is the primal problem with unknown coordinates of the data in the lower dimensional space, the error variables , and the vector for the primal representation of the model (11) evaluated at any point in the input space (and hence also allows for out-of-sample extensions)."
- PENDING-REF-181-E3 | page: 10, section: extracted, quote: "Moreover, the conditioning of the numerical algorithms for computing the eigenvector solutions is inferior (even if one speci ﬁes to compute only a subset of the eigenvectors such as with the Matlab functions and ) with respect to the well-conditioned linear systems to be solved in problems P2 and P3."
- PENDING-REF-181-E4 | page: 2, section: extracted, quote: "Despite the importance of studies in learning theory with bounds on the generalization error, mainly for classiﬁcation and regression problems [8], [28], practitioners often still rely on validation-based methods, due to the lack of sharp bounds in general."
- PENDING-REF-181-E5 | page: 6, section: extracted, quote: "The kernel map with reference point approach can be tuned then in a similar fashion as kernel-based regression and classiﬁcation methods with linear system solving, though for a problem of unsupervised instead of supervised learning now."
- PENDING-REF-181-E6 | page: 7, section: extracted, quote: "We describe now two practical algorithms: a cross-validation method with grid search and a method with use of a randomized validation set that is more suitable for interactive data exploration."
- PENDING-REF-181-E7 | page: 1, section: extracted, quote: "In this paper, we propose a new kernel-based method in the framework of least squares support vector machines (LS-SVMs)."
- PENDING-REF-181-E8 | page: 1, section: extracted, quote: "The kernel map approach that we propose in this paper makes use of a reference point."
