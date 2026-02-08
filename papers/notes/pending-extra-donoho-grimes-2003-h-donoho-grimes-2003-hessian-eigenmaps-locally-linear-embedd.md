---
id: paper-2026-pending-extra-donoho-grimes-2003-h
title: "Hessian eigenmaps: Locally linear embedding techniques for high-dimensional data"
authors: "David L. Donoho, Carrie Grimes"
venue: "Proceedings of the National Academy of Sciences"
year: 2003
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/donoho-grimes-2003-hessian-eigenmaps-locally-linear-embedding-techniques-for-high-dimensional-data.pdf
seed_note_id: "paper-2025-jeon-reliable-va-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- Introduction A recent article in Science (1) proposed to recover a lowdimensional parametrization of high-dimensional data by assuming that the data lie on a manifold M which, viewed as a Riemannian submanifold of the ambient Euclidean space, is globally isometric to a convex subset of a low-dimensional Euclidean space.
- We thank Lawrence Saul (University of Pennsylvania, Philadelphia) for extensive discussions of both LLE and ISOMAP and also both George Papanicolaou (Stanford University) for pointers and Jonathan Kaplan (Harvard University, Cambridge, MA) for extensive discussions about properties of ill-posed boundary-value problems.
- It is now known (2, 3) that there exist high-dimensional libraries of articulated images for which the corresponding data manifold is indeed locally isometric to a subset of a Euclidean space; however, it is easy to see that, in general, the assumption that the subset will be convex is unduly restrictive.
- This functional computes the average of the Laplacian operator over the manifold; Laplacian eigenmap methods propose to solve embedding problems by obtaining the d /H110011 lowest eigenvalues of L and using the corresponding eigenfunctions to embed the data in low-dimensional space.

# Method Summary
- Our method may be viewed as a modiﬁcation of locally linear embedding and our theoretical framework as a modiﬁcation of the Laplacian eigenmaps framework, where we substitute a quadratic form based on the Hessian in place of one based on the Laplacian. manifold learning /H20841ISOMAP /H20841tangent coordinates /H20841isometry /H20841 Laplacian eigenmaps 1.
- The method, Hessian-based locally linear embedding, derives from a conceptual framework of local isometry in which the manifold M, viewed as a Riemannian submanifold of the ambient Euclidean space/H11938 n, is locally isometric to an open, connected subset /H9008of Euclidean space /H11938d.
- This functional computes the average of the Laplacian operator over the manifold; Laplacian eigenmap methods propose to solve embedding problems by obtaining the d /H110011 lowest eigenvalues of L and using the corresponding eigenfunctions to embed the data in low-dimensional space.
- The LLE method is an empirical implementation of the same principle, defining a discrete Laplacian based on a nearest-neighbor graph and embedding scattered n-dimensional data by using the first d nonconstant eigenvectors of the graph Laplacian.
- Y Computational complexity: In effect, the computational cost difference between a sparse and a full matrix using the sparse eigenanalysis implementation in MATLAB 6.1 (using Arnoldi methods) depends on the cost of computing a matrix-vector product using the input matrix.
- Although the data manifold is still locally isometric to Euclidean space, the effect of the missing sampling region is, in the case of LLE, to make the resulting embedding functions asymmetric and nonlinear with respect to the original parametrization.
- Hessian Locally Linear Embedding (HLLE) We now consider the setting where we have sampled data ( mi) lying on M, and we would like to recover the underlying parametrization /H9274and underlying parameter settings /H9258i, at least up to rigid motion.

# When To Use / Not Use
- Use when:
  - However, both LLE and HLLE are more sensitive to the dimensionality of the data space, n, because they must estimate a local tangent space at each point.
  - Although we introduce an orthogonalization step in HLLE that makes the local fits more robust to pathological neighborhoods than LLE, HLLE still requires effectively a numerical second differencing at each point that can be very noisy at low sampling density.
- Avoid when:
  - Y Find basis for null space: Select a basis for Vˆd, which has the property that its restriction to a specific fixed neighborhood N 0 (the neighborhood may be chosen arbitrarily from those used in the algorithm) provides an orthonormal basis.
  - LLE and HLLE are both capable of handling large N problems, because initial computations are performed only on smaller neighborhoods, whereas ISOMAP has to compute a full matrix of graph distances for the initial distance-processing step.
- Failure modes:
  - Recall that /H9278/H11005/H9274/H110021 is a local isometry and gives a coordinate system /H92581, ..., /H9258d on M and therefore induces a choice of coordinate system on Tm(M) that is orthonormal, because /H9278is a local isometry.

# Metrics Mentioned
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- Convexity can fail in the setting of image libraries due to ( i) exclusion phenomena (2, 3), where certain regions of the parameter space would correspond to collisions of objects in the image, or ( ii) unsystematic data sampling, which investigates only a haphazardly chosen region of the parameter space.
- Then the isometry assumption says that G/H20849m, m/H11032/H20850/H11005/H20841 /H9258/H11002/H9258/H11032/H20841, @m7 /H9258, m/H110327 /H9258/H11032, where /H20841/H18528/H20841denotes Euclidean distance in /H11938d. (ISO2) Convexity: The parameter space /H9008is a convex subset of /H11938d.
- In this case, the parameter space /H9008/H20666/H11938 4 becomes nonconvex; writing /H9258/H11005(/H92581, /H92582) as a concatenation of the parameters of the two ball centers, we see that it is missing a tube where /H20841 /H92581 /H11002/H92582/H20841/H113491.
- We describe an implementation of this procedure on sampled data and demonstrate that it performs consistently with the theoretical predictions on a variant of the ‘‘Swiss roll’’ example, where the data are not sampled from a convex region in parameter space.
- Hessian Locally Linear Embedding (HLLE) We now consider the setting where we have sampled data ( mi) lying on M, and we would like to recover the underlying parametrization /H9274and underlying parameter settings /H9258i, at least up to rigid motion.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-EXTRA-C1 | stance: support | summary: Introduction A recent article in Science (1) proposed to recover a lowdimensional parametrization of high-dimensional data by assuming that the data lie on a manifold M which, viewed as a Riemannian submanifold of the ambient Euclidean space, is globally isometric to a convex subset of a low-dimensional Euclidean space. | evidence_ids: PENDING-EXTRA-E1, PENDING-EXTRA-E2
- CLAIM-PENDING-EXTRA-C2 | stance: support | summary: Our method may be viewed as a modiﬁcation of locally linear embedding and our theoretical framework as a modiﬁcation of the Laplacian eigenmaps framework, where we substitute a quadratic form based on the Hessian in place of one based on the Laplacian. manifold learning /H20841ISOMAP /H20841tangent coordinates /H20841isometry /H20841 Laplacian eigenmaps 1. | evidence_ids: PENDING-EXTRA-E3, PENDING-EXTRA-E4
- CLAIM-PENDING-EXTRA-C3 | stance: support | summary: Convexity can fail in the setting of image libraries due to ( i) exclusion phenomena (2, 3), where certain regions of the parameter space would correspond to collisions of objects in the image, or ( ii) unsystematic data sampling, which investigates only a haphazardly chosen region of the parameter space. | evidence_ids: PENDING-EXTRA-E5, PENDING-EXTRA-E6

# Workflow Relevance Map
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance
- step: 6 | relevance: high | note: guides reliable interpretation of projected views

# Evidence
- PENDING-EXTRA-E1 | page: 1, section: extracted, quote: "Introduction A recent article in Science (1) proposed to recover a lowdimensional parametrization of high-dimensional data by assuming that the data lie on a manifold M which, viewed as a Riemannian submanifold of the ambient Euclidean space, is globally isometric to a convex subset of a low-dimensional Euclidean space."
- PENDING-EXTRA-E2 | page: 6, section: extracted, quote: "We thank Lawrence Saul (University of Pennsylvania, Philadelphia) for extensive discussions of both LLE and ISOMAP and also both George Papanicolaou (Stanford University) for pointers and Jonathan Kaplan (Harvard University, Cambridge, MA) for extensive discussions about properties of ill-posed boundary-value problems."
- PENDING-EXTRA-E3 | page: 1, section: extracted, quote: "It is now known (2, 3) that there exist high-dimensional libraries of articulated images for which the corresponding data manifold is indeed locally isometric to a subset of a Euclidean space; however, it is easy to see that, in general, the assumption that the subset will be convex is unduly restrictive."
- PENDING-EXTRA-E4 | page: 4, section: extracted, quote: "This functional computes the average of the Laplacian operator over the manifold; Laplacian eigenmap methods propose to solve embedding problems by obtaining the d /H110011 lowest eigenvalues of L and using the corresponding eigenfunctions to embed the data in low-dimensional space."
- PENDING-EXTRA-E5 | page: 1, section: extracted, quote: "Our method may be viewed as a modiﬁcation of locally linear embedding and our theoretical framework as a modiﬁcation of the Laplacian eigenmaps framework, where we substitute a quadratic form based on the Hessian in place of one based on the Laplacian. manifold learning /H20841ISOMAP /H20841tangent coordinates /H20841isometry /H20841 Laplacian eigenmaps 1."
- PENDING-EXTRA-E6 | page: 1, section: extracted, quote: "The method, Hessian-based locally linear embedding, derives from a conceptual framework of local isometry in which the manifold M, viewed as a Riemannian submanifold of the ambient Euclidean space/H11938 n, is locally isometric to an open, connected subset /H9008of Euclidean space /H11938d."
- PENDING-EXTRA-E7 | page: 4, section: extracted, quote: "The LLE method is an empirical implementation of the same principle, defining a discrete Laplacian based on a nearest-neighbor graph and embedding scattered n-dimensional data by using the first d nonconstant eigenvectors of the graph Laplacian."
- PENDING-EXTRA-E8 | page: 3, section: extracted, quote: "Y Computational complexity: In effect, the computational cost difference between a sparse and a full matrix using the sparse eigenanalysis implementation in MATLAB 6.1 (using Arnoldi methods) depends on the cost of computing a matrix-vector product using the input matrix."
