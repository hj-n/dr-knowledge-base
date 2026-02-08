---
id: paper-2000-pending-extra-weinberger05a
title: "Nonlinear Dimensionality Reduction by Semideﬁnite Programming and Kernel Matrix Factorization"
authors: "Programming and Kernel Matrix Factorization"
venue: "UNKNOWN"
year: 2000
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/weinberger05a.pdf
seed_note_id: "paper-2025-jeon-reliable-va-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- Next, we show that the same linear transformation can be used to reconstruct the unfolded data set —that is, after the mapping from inputs {⃗ xi}n i=1 to outputs 1For the examples in this paper, we used the SDP solver CSDP v4.9 [4] with time complexity of O(n3 +c3) per iteration for sparse problems with n×n target matrices and c constraints.
- In earlier work, this step limited us to problems with n ≈ 2000 examples and k ≤ 5 nearest neighbors; moreover, problems of this size typically required several hours of computation on a mid-range desktop computer.
- In this paper, we describe a new framework that has allowed us to reproduce our original results in a small fraction of this time, as well as to study much larger problems in manifold learning.
- Algorithmic advances may also emerge from the dual formulation of “maximum variance unfolding” [17], which is related to the problem of computing fastest mixing Markov chains on graphs.

# Method Summary
- To eliminate a translational degree of freedom in the embedding, the outputs are also constrained to be centered on the origin: ∑ i ⃗ yi = ⃗0. (3) Finally, the algorithm attempts to “unfold” the inputs by maximizing the variance var(⃗ y) = ∑ i | |⃗ yi| |2 (4) while preserving local distances and angles, as in eq. (2).
- As in kernel PCA [15], the embedding is derived from the eigenvalues and eigenvectors of the kernel matrix; in particular, the algorithm outputs yαi = √ λα uαi , where λα and uα are the top d eigenvalues and eigenvectors.
- This weighted graph is derived by appealing to the symmetries of linear reconstruction coeﬃcients; it is based on a similar intuition as the algorithm for manifold learning by locally linear embedding (LLE) [13, 14].
- Landmark methods were originally developed to accelerate the multidimensional scaling procedure in Isomap [7]; they were subsequently applied to the fast embedding of sparse similarity graphs [11].
- These algorithms can thus be viewed as kernel methods with feature spaces that “unfold” the manifold from which the data was sampled. ∗This work was supported by NSF Award 0238323.
- We are hopeful that a combination of complementary approaches will lead to even faster and more powerful algorithms for manifold learning by semideﬁnite programming.
- As opposed to the Nystr¨ om method, our approach is better described as an adaptation of recent ideas for semisupervised learning on graphs [1, 16, 18, 26, 27].

# When To Use / Not Use
- Use when:
  - In particular, denoting these landmarks by {⃗ µα }m α=1, the reconstructed inputs {ˆxi}n i=1 are given by the linear transformation: ˆxi = ∑ α Qiα ⃗ µα . (5) The linear transformation Q is derived from a sparse weighted graph in which each node represents an input and the weights are used to propagate the positions of the m landmarks to the remaining n− m nodes.
  - Next, we show that the same linear transformation can be used to reconstruct the unfolded data set —that is, after the mapping from inputs {⃗ xi}n i=1 to outputs 1For the examples in this paper, we used the SDP solver CSDP v4.9 [4] with time complexity of O(n3 +c3) per iteration for sparse problems with n×n target matrices and c constraints.
- Avoid when:
  - The free parameters of the algorithm are the number of nearest neighbors r used to derive locally linear reconstructions, the number of nearest neighbors k used to generate distance constraints in the SDP, and the number of landmarks m (which also constrains the rank of the kernel matrix).
  - In what follows, we will refer to this algorithm as landmark SDE, or simply ℓSDE. ℓSDE can be much faster than SDE because its main optimization is performed over m × m matrices, where m ≪ n.
- Failure modes:
  - Acknowledgments We are grateful to Ali Jadbabaie (University of Pennsylvania) for several discussions about semideﬁnite programming and to the anonymous reviewers for many useful comments.

# Metrics Mentioned
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- It has several interesting properties: the main optimization is convex and guaranteed to preserve certain aspects of the local geometry; the method always yields a semipositive deﬁnite kernel matrix; the eigenspectrum of the kernel matrix provides an estimate of the underlying manifold’s dimensionality; also, the method does not rely on estimating geodesic distances between faraway points on the manifold.
- Next, we show that the same linear transformation can be used to reconstruct the unfolded data set —that is, after the mapping from inputs {⃗ xi}n i=1 to outputs 1For the examples in this paper, we used the SDP solver CSDP v4.9 [4] with time complexity of O(n3 +c3) per iteration for sparse problems with n×n target matrices and c constraints.
- The free parameters of the algorithm are the number of nearest neighbors r used to derive locally linear reconstructions, the number of nearest neighbors k used to generate distance constraints in the SDP, and the number of landmarks m (which also constrains the rank of the kernel matrix).
- In what follows, we will refer to this algorithm as landmark SDE, or simply ℓSDE. ℓSDE can be much faster than SDE because its main optimization is performed over m × m matrices, where m ≪ n.
- We then use this representation to derive much simpler semideﬁnite programs for the optimization in the previous section.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-EXTRA-C1 | stance: support | summary: Next, we show that the same linear transformation can be used to reconstruct the unfolded data set —that is, after the mapping from inputs {⃗ xi}n i=1 to outputs 1For the examples in this paper, we used the SDP solver CSDP v4.9 [4] with time complexity of O(n3 +c3) per iteration for sparse problems with n×n target matrices and c constraints. | evidence_ids: PENDING-EXTRA-E1, PENDING-EXTRA-E2
- CLAIM-PENDING-EXTRA-C2 | stance: support | summary: To eliminate a translational degree of freedom in the embedding, the outputs are also constrained to be centered on the origin: ∑ i ⃗ yi = ⃗0. (3) Finally, the algorithm attempts to “unfold” the inputs by maximizing the variance var(⃗ y) = ∑ i / /⃗ yi/ /2 (4) while preserving local distances and angles, as in eq. (2). | evidence_ids: PENDING-EXTRA-E3, PENDING-EXTRA-E4
- CLAIM-PENDING-EXTRA-C3 | stance: support | summary: It has several interesting properties: the main optimization is convex and guaranteed to preserve certain aspects of the local geometry; the method always yields a semipositive deﬁnite kernel matrix; the eigenspectrum of the kernel matrix provides an estimate of the underlying manifold’s dimensionality; also, the method does not rely on estimating geodesic distances between faraway points on the manifold. | evidence_ids: PENDING-EXTRA-E5, PENDING-EXTRA-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-EXTRA-E1 | page: 3, section: extracted, quote: "Next, we show that the same linear transformation can be used to reconstruct the unfolded data set —that is, after the mapping from inputs {⃗ xi}n i=1 to outputs 1For the examples in this paper, we used the SDP solver CSDP v4.9 [4] with time complexity of O(n3 +c3) per iteration for sparse problems with n×n target matrices and c constraints."
- PENDING-EXTRA-E2 | page: 3, section: extracted, quote: "In earlier work, this step limited us to problems with n ≈ 2000 examples and k ≤ 5 nearest neighbors; moreover, problems of this size typically required several hours of computation on a mid-range desktop computer."
- PENDING-EXTRA-E3 | page: 1, section: extracted, quote: "In this paper, we describe a new framework that has allowed us to reproduce our original results in a small fraction of this time, as well as to study much larger problems in manifold learning."
- PENDING-EXTRA-E4 | page: 7, section: extracted, quote: "Algorithmic advances may also emerge from the dual formulation of “maximum variance unfolding” [17], which is related to the problem of computing fastest mixing Markov chains on graphs."
- PENDING-EXTRA-E5 | page: 2, section: extracted, quote: "To eliminate a translational degree of freedom in the embedding, the outputs are also constrained to be centered on the origin: ∑ i ⃗ yi = ⃗0. (3) Finally, the algorithm attempts to “unfold” the inputs by maximizing the variance var(⃗ y) = ∑ i / /⃗ yi/ /2 (4) while preserving local distances and angles, as in eq. (2)."
- PENDING-EXTRA-E6 | page: 2, section: extracted, quote: "As in kernel PCA [15], the embedding is derived from the eigenvalues and eigenvectors of the kernel matrix; in particular, the algorithm outputs yαi = √ λα uαi , where λα and uα are the top d eigenvalues and eigenvectors."
- PENDING-EXTRA-E7 | page: 3, section: extracted, quote: "This weighted graph is derived by appealing to the symmetries of linear reconstruction coeﬃcients; it is based on a similar intuition as the algorithm for manifold learning by locally linear embedding (LLE) [13, 14]."
- PENDING-EXTRA-E8 | page: 2, section: extracted, quote: "Landmark methods were originally developed to accelerate the multidimensional scaling procedure in Isomap [7]; they were subsequently applied to the fast embedding of sparse similarity graphs [11]."
