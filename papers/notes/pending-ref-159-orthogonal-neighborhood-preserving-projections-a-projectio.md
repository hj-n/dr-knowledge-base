---
id: paper-2007-pending-ref-159
title: "Orthogonal Neighborhood Preserving Projections: A Projection-Based Dimensionality Reduction Technique"
authors: "E. Kokiopoulou, Y. Saad"
venue: "IEEE Transactions on Pattern Analysis and Machine Intelligence"
year: 2007
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-159-2007-orthogonal-neighborhood-preserving-projections-a-projection-based-dimensionality-redu.pdf
seed_note_id: "paper-2014-sorzano-survey-dr-techniques"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- The projected data in reduced space is Y = V ⊤Φ(X) = Z ⊤Q⊤Φ(X) = Z ⊤Q⊤QR = Z ⊤R. (26) In this case, the objective function (21) becomes F(Y ) = tr [ Z ⊤R(I − W ⊤)(I − W )R⊤Z ] = tr [ Z ⊤R M R ⊤Z ] . (27) As a result the columns z of the optimal Z are just the set of eigenvectors of the problem [ R(I − W ⊤)(I − W )R⊤] z = λz (28) associated with the smallest d eigenvalues.
- V ⊤V = I, then the solution V to the above optimization problem is the basis of the eigenvectors associated with the d smallest eigenvalues of the matrix ˜M = X(I − W ⊤)(I − W )X ⊤ = XM X⊤ . (13) The assumptions that were made when deﬁning the weights wij at the beginning of this section, imply that the matrix I − W is singular.
- This optimization problem is formulated under the following constraints in order to make the problem well-posed: 1) ∑ i yi = 0 i.e., the mapped coordinates are centered at the origin and 2) 1 n ∑ i yiy⊤ i = I, that is the embedding vectors have unit covariance.
- Note that F (Y ) can be written F (Y ) = ∥Y − Y W ⊤∥2 F , so F (Y ) = ∥Y (I − W ⊤)∥2 F = tr [ Y (I − W ⊤)(I − W )Y ⊤] . (11) The problem will amount to computing the d smallest eigenvalues of the matrix M = ( I − W ⊤)(I − W ⊤)⊤, and the associated eigenvectors.

# Method Summary
- In particular we propose a method, named Orthogonal Neighborhood Preserving Projections, which works by ﬁrst building an “afﬁnity” graph for the data, in a way that is similar to the method of Locally Linear Embedding (LLE).
- Two dimensional projections of digits using four related methods, where ‘+’ denotes 0, ‘x’ denotes 1, ‘o’ denotes 2, ‘ △’ denotes 3 and ‘ □’ denotes 4. yield more meaningful projections since samples of the same class are mapped close to each other.
- However, the orthogonal methods i.e., OLPP and ONPP preserve global geometric characteristics as well, since they give faithful projections which convey information about how the manifold is folded in the high dimensional space.
- In this case the set V is the eigenbasis associated with the lowest eigenmodes of the matrix Clpp = X(D − W )X ⊤. (5) We refer to this ﬁrst option as the method of Orthogonal Locality Preserving Projections (OLPP).
- The proposed method, named Orthogonal Neighborhood Preserving Projections (ONPP) [3], projects the high dimensional data samples on a lower dimensional space by means of a linear transformation V .
- Two dimensional projections of digits using four related methods, ‘+’ denotes 5, ‘x’ denotes 6, ‘o’ denotes 7, ‘ △’ denotes 8 and ‘ □’ denotes 9.
- In LPP, the projection is deﬁned via a certain objective function, whose minimization leads to eigenvectors of a generalized eigenvalue problem.

# When To Use / Not Use
- Use when:
  - However, our algorithm uses the optimal data-driven weights of LLE which reﬂect the intrinsic geometry of the local neighborhoods, whereas the uniform weights (0/1) used in LPP aim at preserving locality without explicit consideration to the local geometric structure.
  - In particular we propose a method, named Orthogonal Neighborhood Preserving Projections, which works by ﬁrst building an “afﬁnity” graph for the data, in a way that is similar to the method of Locally Linear Embedding (LLE).
- Avoid when:
  - In contrast, imposing the condition Y Y ⊤ = I, will lead to a criterion that is similar to that of PCA: the points yi will tend to be different from one another (because of the orthogonality of the rows of Y ).
  - It appears from the experiments shown here that the weighted graph used by ONPP (based on the one in LLE) to represent locality does better that the simpler technique used by OLPP (based on the one in LPP).
- Failure modes:
  - The linear projection step is determined by imposing the constraint that each data sample in the reduced space is reconstructed from its neighbors by the same weights used in the input space.

# Metrics Mentioned
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- V ⊤V = I, then the solution V to the above optimization problem is the basis of the eigenvectors associated with the d smallest eigenvalues of the matrix ˜M = X(I − W ⊤)(I − W )X ⊤ = XM X⊤ . (13) The assumptions that were made when deﬁning the weights wij at the beginning of this section, imply that the matrix I − W is singular.
- This optimization problem is formulated under the following constraints in order to make the problem well-posed: 1) ∑ i yi = 0 i.e., the mapped coordinates are centered at the origin and 2) 1 n ∑ i yiy⊤ i = I, that is the embedding vectors have unit covariance.
- Note that with the supervised construction of the afﬁnity graph, the parameter k need not be determined by the user, since it is set automatically to be the cardinality of each class.
- While Gaussian weights can be used in LPP, these are somewhat artiﬁcial and require the selection of an appropriate value of the parameter σ, the width of the Gaussian envelope.
- Usually, the property that is preserved is quantiﬁed by an objective function and the dimensionality reduction problem is formulated as an optimization problem.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-159-C1 | stance: support | summary: The projected data in reduced space is Y = V ⊤Φ(X) = Z ⊤Q⊤Φ(X) = Z ⊤Q⊤QR = Z ⊤R. (26) In this case, the objective function (21) becomes F(Y ) = tr [ Z ⊤R(I − W ⊤)(I − W )R⊤Z ] = tr [ Z ⊤R M R ⊤Z ] . (27) As a result the columns z of the optimal Z are just the set of eigenvectors of the problem [ R(I − W ⊤)(I − W )R⊤] z = λz (28) associated with the smallest d eigenvalues. | evidence_ids: PENDING-REF-159-E1, PENDING-REF-159-E2
- CLAIM-PENDING-REF-159-C2 | stance: support | summary: In particular we propose a method, named Orthogonal Neighborhood Preserving Projections, which works by ﬁrst building an “afﬁnity” graph for the data, in a way that is similar to the method of Locally Linear Embedding (LLE). | evidence_ids: PENDING-REF-159-E3, PENDING-REF-159-E4
- CLAIM-PENDING-REF-159-C3 | stance: support | summary: V ⊤V = I, then the solution V to the above optimization problem is the basis of the eigenvectors associated with the d smallest eigenvalues of the matrix ˜M = X(I − W ⊤)(I − W )X ⊤ = XM X⊤ . (13) The assumptions that were made when deﬁning the weights wij at the beginning of this section, imply that the matrix I − W is singular. | evidence_ids: PENDING-REF-159-E5, PENDING-REF-159-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-REF-159-E1 | page: 7, section: extracted, quote: "The projected data in reduced space is Y = V ⊤Φ(X) = Z ⊤Q⊤Φ(X) = Z ⊤Q⊤QR = Z ⊤R. (26) In this case, the objective function (21) becomes F(Y ) = tr [ Z ⊤R(I − W ⊤)(I − W )R⊤Z ] = tr [ Z ⊤R M R ⊤Z ] . (27) As a result the columns z of the optimal Z are just the set of eigenvectors of the problem [ R(I − W ⊤)(I − W )R⊤] z = λz (28) associated with the smallest d eigenvalues."
- PENDING-REF-159-E2 | page: 4, section: extracted, quote: "V ⊤V = I, then the solution V to the above optimization problem is the basis of the eigenvectors associated with the d smallest eigenvalues of the matrix ˜M = X(I − W ⊤)(I − W )X ⊤ = XM X⊤ . (13) The assumptions that were made when deﬁning the weights wij at the beginning of this section, imply that the matrix I − W is singular."
- PENDING-REF-159-E3 | page: 4, section: extracted, quote: "This optimization problem is formulated under the following constraints in order to make the problem well-posed: 1) ∑ i yi = 0 i.e., the mapped coordinates are centered at the origin and 2) 1 n ∑ i yiy⊤ i = I, that is the embedding vectors have unit covariance."
- PENDING-REF-159-E4 | page: 4, section: extracted, quote: "Note that F (Y ) can be written F (Y ) = ∥Y − Y W ⊤∥2 F , so F (Y ) = ∥Y (I − W ⊤)∥2 F = tr [ Y (I − W ⊤)(I − W )Y ⊤] . (11) The problem will amount to computing the d smallest eigenvalues of the matrix M = ( I − W ⊤)(I − W ⊤)⊤, and the associated eigenvectors."
- PENDING-REF-159-E5 | page: 1, section: extracted, quote: "In particular we propose a method, named Orthogonal Neighborhood Preserving Projections, which works by ﬁrst building an “afﬁnity” graph for the data, in a way that is similar to the method of Locally Linear Embedding (LLE)."
- PENDING-REF-159-E6 | page: 10, section: extracted, quote: "Two dimensional projections of digits using four related methods, where ‘+’ denotes 0, ‘x’ denotes 1, ‘o’ denotes 2, ‘ △’ denotes 3 and ‘ □’ denotes 4. yield more meaningful projections since samples of the same class are mapped close to each other."
- PENDING-REF-159-E7 | page: 9, section: extracted, quote: "However, the orthogonal methods i.e., OLPP and ONPP preserve global geometric characteristics as well, since they give faithful projections which convey information about how the manifold is folded in the high dimensional space."
- PENDING-REF-159-E8 | page: 3, section: extracted, quote: "In this case the set V is the eigenbasis associated with the lowest eigenmodes of the matrix Clpp = X(D − W )X ⊤. (5) We refer to this ﬁrst option as the method of Orthogonal Locality Preserving Projections (OLPP)."
