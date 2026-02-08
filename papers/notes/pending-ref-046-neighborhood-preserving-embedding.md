---
id: paper-2005-pending-ref-046
title: "Neighborhood preserving embedding"
authors: "X. He, D. Cai, S. Y an, and H.-J. Zhang"
venue: "Tenth IEEE International Conference on Computer Vision (ICCV'05) Volume 1"
year: 2005
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-046-2005-neighborhood-preserving-embedding.pdf
seed_note_id: "paper-2009-comparative-review-dr-techniques"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- We then outline algorithms to solve the resulting problem highlighting the computational challenges and propose an approximate method to alleviate them.
- Thus the Frobenius norm in (11) can be further expressed in the form of matrix trace to reduce the problem to min Uk:∀k=1,··· ,n L(Uk) is Unitary tr(Y⊤EE⊤Y). (12) Based on the cyclic permutation property of the trace operator, (12) is equivalent to min Uk:∀k=1,··· ,n L(Uk) is Unitary tr(E⊤YY⊤E). (13) Let Z = YY⊤∈ R(I1···In)×(I1···In) be the constant matrix.
- Under TNPE model, the embedding needs 3 steps, where solving n linear transformations takes O(Ntrrd) for embedding raw data, matrix generation for an eigenvalue problem takes O(Ntrr2n), and eigenvalue decomposition for updating each linear transformation takes r3n, giving a total computational complexity O(n(Ntrrd + Ntrr2n +r3n)).
- Then, the problem (13) becomes min Uk:∀k=1,··· ,n L(Uk) is Unitary tr(E⊤ZE). (14) We will use the alternating minimization method [24] to solve (14) such that each Uk is updated by solving min Uk:L(Uk) is unitary tr(E⊤ZE). (15) 4 In order to solve (15), we use an iterative algorithm.

# Method Summary
- We further show that TTNPEATN algorithm exhibits improved classiﬁcation performance and better dimensionality reduction among the baseline approaches, and has lower computational complexity as com9 pared to Tucker neighborhood preserving embedding method.
- We further note that the authors of [19] compared their approach with different approaches based on vectorization of data, including Neighborhood Preserving Embedding (NPE), Locality Preserving Projection (LPP), Principal Component Analysis (PCA), and Local Discriminant Embedding (LDE).
- In order to address this, we propose a Tensor Train Neighbor Preserving Embedding using Approximate Tensor Network (TTNPE-ATN) algorithm in the next section, to approximate (15), aiming to reduce computation and memory cost.
- Motivated by recent works [4]–[6] that demonstrate applying tensor factorization (after reshaping matrices to multidimensional arrays or tensors) improves data representation, we consider reshaping vision data into tensors and embedding the tensors into Kronecker structured subspaces, i.e. tensor subspaces, to further reﬁne these subspace based approaches with signiﬁcant gains.
- Under TTNPE-ATN model, the embedding takes 3 steps, where the initialization by tensor train decomposition algorithm takes O(nd 1 nr3), the generation of Z takes O(dN2 tr +d2Ntr), and updating Uk, which includes a gradient calculation by merging a tensor network, takes O(nd 1 nr3)), thus giving a total computational complexity O(nd 1 nr3 +dN2 tr +d2Ntr).
- Then, the problem (13) becomes min Uk:∀k=1,··· ,n L(Uk) is Unitary tr(E⊤ZE). (14) We will use the alternating minimization method [24] to solve (14) such that each Uk is updated by solving min Uk:L(Uk) is unitary tr(E⊤ZE). (15) 4 In order to solve (15), we use an iterative algorithm.
- 1 Tensor Train Neighborhood Preserving Embedding Wenqi Wang, Vaneet Aggarwal, and Shuchin Aeron Abstract—In this paper, we propose a Tensor Train Neighborhood Preserving Embedding (TTNPE) to embed multidimensional tensor data into low dimensional tensor subspace.

# When To Use / Not Use
- Use when:
  - We did not use the absolute stock prices, but the return rates over these days to avoid the information in the absolute value of the stock price.
  - Motivated by recent works [4]–[6] that demonstrate applying tensor factorization (after reshaping matrices to multidimensional arrays or tensors) improves data representation, we consider reshaping vision data into tensors and embedding the tensors into Kronecker structured subspaces, i.e. tensor subspaces, to further reﬁne these subspace based approaches with signiﬁcant gains.
- Avoid when:
  - Then, the problem (13) becomes min Uk:∀k=1,··· ,n L(Uk) is Unitary tr(E⊤ZE). (14) We will use the alternating minimization method [24] to solve (14) such that each Uk is updated by solving min Uk:L(Uk) is unitary tr(E⊤ZE). (15) 4 In order to solve (15), we use an iterative algorithm.
  - Further, the best classiﬁcation results given by TTNPE-ATN are even better than the classiﬁcation results given by KNN algorithm, indicating TTNPE-ATN gives better neighborhood preserving embedding as compared to the TNPE algorithm.
- Failure modes:
  - For Uk:k=1,···n−1, the generation of A requires merging the tensor networks, which has a computation complexity of O ( (I1··· In)2Rk−1 + (I1··· In)2( Rk−1 I1···Ik−1 )2RkRn ) , and solving (19) takesO ( Rk−1IkR2 k ) time.

# Metrics Mentioned
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- Under TTNPE-ATN model, the embedding takes 3 steps, where the initialization by tensor train decomposition algorithm takes O(nd 1 nr3), the generation of Z takes O(dN2 tr +d2Ntr), and updating Uk, which includes a gradient calculation by merging a tensor network, takes O(nd 1 nr3)), thus giving a total computational complexity O(nd 1 nr3 +dN2 tr +d2Ntr).
- Each Uk:k=1,··· ,n is initialized by tensor train decomposition [22] with a thresholding parameter τ, which zeros out the singular values which are smaller than τ times the maximum singular value, such that tensor train ranks (R1,··· ,R n) are determined.
- While there has been work on parameter selection for matrix-based approaches [30], [31], ﬁnding the thresholding parameter for TTNPE is an interesting future research direction.
- 3: Apply tensor train decomposition [22] on X to initialize Ui=1,··· ,n with thresholding parameter τ, and the tensor train ranks are determined based on selection of τ.
- In the future, we will investigate the convergence of tensor network optimization and provide the theoretical gap between TTNPE-ATN and TTNPE-TN.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-046-C1 | stance: support | summary: We then outline algorithms to solve the resulting problem highlighting the computational challenges and propose an approximate method to alleviate them. | evidence_ids: PENDING-REF-046-E1, PENDING-REF-046-E2
- CLAIM-PENDING-REF-046-C2 | stance: support | summary: We further show that TTNPEATN algorithm exhibits improved classiﬁcation performance and better dimensionality reduction among the baseline approaches, and has lower computational complexity as com9 pared to Tucker neighborhood preserving embedding method. | evidence_ids: PENDING-REF-046-E3, PENDING-REF-046-E4
- CLAIM-PENDING-REF-046-C3 | stance: support | summary: Under TTNPE-ATN model, the embedding takes 3 steps, where the initialization by tensor train decomposition algorithm takes O(nd 1 nr3), the generation of Z takes O(dN2 tr +d2Ntr), and updating Uk, which includes a gradient calculation by merging a tensor network, takes O(nd 1 nr3)), thus giving a total computational complexity O(nd 1 nr3 +dN2 tr +d2Ntr). | evidence_ids: PENDING-REF-046-E5, PENDING-REF-046-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 4 | relevance: high | note: contains initialization sensitivity or control-policy evidence

# Evidence
- PENDING-REF-046-E1 | page: 1, section: extracted, quote: "We then outline algorithms to solve the resulting problem highlighting the computational challenges and propose an approximate method to alleviate them."
- PENDING-REF-046-E2 | page: 3, section: extracted, quote: "Thus the Frobenius norm in (11) can be further expressed in the form of matrix trace to reduce the problem to min Uk:∀k=1,··· ,n L(Uk) is Unitary tr(Y⊤EE⊤Y). (12) Based on the cyclic permutation property of the trace operator, (12) is equivalent to min Uk:∀k=1,··· ,n L(Uk) is Unitary tr(E⊤YY⊤E). (13) Let Z = YY⊤∈ R(I1···In)×(I1···In) be the constant matrix."
- PENDING-REF-046-E3 | page: 5, section: extracted, quote: "Under TNPE model, the embedding needs 3 steps, where solving n linear transformations takes O(Ntrrd) for embedding raw data, matrix generation for an eigenvalue problem takes O(Ntrr2n), and eigenvalue decomposition for updating each linear transformation takes r3n, giving a total computational complexity O(n(Ntrrd + Ntrr2n +r3n))."
- PENDING-REF-046-E4 | page: 3, section: extracted, quote: "Then, the problem (13) becomes min Uk:∀k=1,··· ,n L(Uk) is Unitary tr(E⊤ZE). (14) We will use the alternating minimization method [24] to solve (14) such that each Uk is updated by solving min Uk:L(Uk) is unitary tr(E⊤ZE). (15) 4 In order to solve (15), we use an iterative algorithm."
- PENDING-REF-046-E5 | page: 8, section: extracted, quote: "We further show that TTNPEATN algorithm exhibits improved classiﬁcation performance and better dimensionality reduction among the baseline approaches, and has lower computational complexity as com9 pared to Tucker neighborhood preserving embedding method."
- PENDING-REF-046-E6 | page: 6, section: extracted, quote: "We further note that the authors of [19] compared their approach with different approaches based on vectorization of data, including Neighborhood Preserving Embedding (NPE), Locality Preserving Projection (LPP), Principal Component Analysis (PCA), and Local Discriminant Embedding (LDE)."
- PENDING-REF-046-E7 | page: 4, section: extracted, quote: "In order to address this, we propose a Tensor Train Neighbor Preserving Embedding using Approximate Tensor Network (TTNPE-ATN) algorithm in the next section, to approximate (15), aiming to reduce computation and memory cost."
- PENDING-REF-046-E8 | page: 1, section: extracted, quote: "Motivated by recent works [4]–[6] that demonstrate applying tensor factorization (after reshaping matrices to multidimensional arrays or tensors) improves data representation, we consider reshaping vision data into tensors and embedding the tensors into Kronecker structured subspaces, i.e. tensor subspaces, to further reﬁne these subspace based approaches with signiﬁcant gains."
