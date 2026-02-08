---
id: paper-2026-pending-extra-clustered-nystrm-met
title: "Clustered Nyström Method for Large Scale Manifold Learning and Dimension Reduction"
authors: "Kai Zhang, James T. Kwok"
venue: "IEEE Transactions on Neural Networks"
year: 2010
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/Clustered_Nystrm_Method_for_Large_Scale_Manifold_Learning_and_Dimension_Reduction.pdf
seed_note_id: "paper-2015-gisbrecht-nonlinear-dr-visualization"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- In particular, when only 5% of the data are used as landmark points, its performance on the abalone dataset is almost identical to that when the ful lk e r n e lm a t r i xi su s e d .T h i s clearly demonstrates the usefulness of low-rank approximation in supervised (regression) problems.
- One problem with the probabilistic sampling scheme is that the sampling probabilities are sometimes computed on the basis of the norms of the rows/columns of the kernel matrix, which requires at least O(n 2) time and space.
- In practice, since the distortion error drops most signiﬁcantly in the ﬁrst few iterations, we ﬁx the number of iterations to a small integer (e.g., l = 5).
- The resultant complexities, namely quadratic in terms of space and (usually) cubic in terms of time, can be quite demanding for large problems.

# Method Summary
- These are the greedy approaches (Section II-A), Nystr¨ om methods (Section II-B), and randomized algorithms (Section II-C).
- Motivated by this observation and the fact that k-means clustering can ﬁnd a local minimum of the quantization error [42], we propose to use the cluster centers obtained from k-means as the landmark points in the Nystr¨om low-rank approximation, with the reconstruction step being the same as in the original Nystr¨om method (5).
- EXPERIMENTS In this section, we perform extensive experiments to compare the proposed method with existing algorithms on the low-rank approximation of kernel matrix (Section IV-A), KPCA (Section IV-B), Laplaci an eigenmap, and spectral clustering (Section IV-C).
- In Section IV, we experimentally compare our approach with a number of state-of-the-art low-rank decomposition techniques for manifold learning and dimensionality reduction, as well as supervised methods Gaussian process (GP) regression.
- Performance of different algorithms in approximating the 3-D embe dding of Laplacian eigenmap. (a) German, (b) splice, (c) adult1a, (d) dna, (e) segment, (f) w1a, (g) uci, and (h) satimage. methods in manifold learning and clustering.
- We apply this clustered Nystr¨om method for low-rank approximation in a number of manifold learning and dimensionality reduction algorithms, such as KPCA and Laplacian eigenmap.
- Kwok Abstract— Kernel (or similarity) matrix plays a key role in many machine learning algorithms such as kernel methods, manifold learning, and dimension reduction.

# When To Use / Not Use
- Use when:
  - We call it “clustered Nystr¨om method.” The k-means-based sampling works on the n × d data matrix, and avoids the storage and manipulation of the n × n kernel matrix.
  - Motivated by this observation and the fact that k-means clustering can ﬁnd a local minimum of the quantization error [42], we propose to use the cluster centers obtained from k-means as the landmark points in the Nystr¨om low-rank approximation, with the reconstruction step being the same as in the original Nystr¨om method (5).
- Avoid when:
  - This use of spherical clusters to approximate nonspherical data is similar to the use of isotropic kernels for approximating globally anisotropic distributions in Parzen window density estimation, and it is known that such an approximation converges to the ground truth asymptotically [50]–[51].
  - In particular, when only 5% of the data are used as landmark points, its performance on the abalone dataset is almost identical to that when the ful lk e r n e lm a t r i xi su s e d .T h i s clearly demonstrates the usefulness of low-rank approximation in supervised (regression) problems.
- Failure modes:
  - His current research interests include data mining applications incl uding bioinformatics and complex networks, machine learning and pattern recognition, in particular large-scale unsupervised learning, semisupervised learning, and dimension reduction algorithms.

# Metrics Mentioned
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- For example, in each iteration of the interior point method (as applied to SVM), the most expensive step is in the solving of the linear system (K + δI)u = w, where δ> 0 is a regularization parameter and I is the n × n identity matrix.
- The complexity of k-means is only linear in the sample size and dimensionality, and, as will be shown in our experimental evaluations, only a few iterations sufﬁce in practice.
- In practice, since the distortion error drops most signiﬁcantly in the ﬁrst few iterations, we ﬁx the number of iterations to a small integer (e.g., l = 5).
- The time complexity of the k-means algorithm is O(ndl ), where n is the sample size, d is the dimension, and l the number of iterations.
- In order to compare with standard algorithms that are not quite scalable, we are restricted to samples smaller than 5000.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-EXTRA-C1 | stance: support | summary: In particular, when only 5% of the data are used as landmark points, its performance on the abalone dataset is almost identical to that when the ful lk e r n e lm a t r i xi su s e d .T h i s clearly demonstrates the usefulness of low-rank approximation in supervised (regression) problems. | evidence_ids: PENDING-EXTRA-E1, PENDING-EXTRA-E2
- CLAIM-PENDING-EXTRA-C2 | stance: support | summary: These are the greedy approaches (Section II-A), Nystr¨ om methods (Section II-B), and randomized algorithms (Section II-C). | evidence_ids: PENDING-EXTRA-E3, PENDING-EXTRA-E4
- CLAIM-PENDING-EXTRA-C3 | stance: support | summary: For example, in each iteration of the interior point method (as applied to SVM), the most expensive step is in the solving of the linear system (K + δI)u = w, where δ> 0 is a regularization parameter and I is the n × n identity matrix. | evidence_ids: PENDING-EXTRA-E5, PENDING-EXTRA-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 4 | relevance: high | note: contains initialization sensitivity or control-policy evidence

# Evidence
- PENDING-EXTRA-E1 | page: 11, section: extracted, quote: "In particular, when only 5% of the data are used as landmark points, its performance on the abalone dataset is almost identical to that when the ful lk e r n e lm a t r i xi su s e d .T h i s clearly demonstrates the usefulness of low-rank approximation in supervised (regression) problems."
- PENDING-EXTRA-E2 | page: 2, section: extracted, quote: "One problem with the probabilistic sampling scheme is that the sampling probabilities are sometimes computed on the basis of the norms of the rows/columns of the kernel matrix, which requires at least O(n 2) time and space."
- PENDING-EXTRA-E3 | page: 6, section: extracted, quote: "In practice, since the distortion error drops most signiﬁcantly in the ﬁrst few iterations, we ﬁx the number of iterations to a small integer (e.g., l = 5)."
- PENDING-EXTRA-E4 | page: 1, section: extracted, quote: "The resultant complexities, namely quadratic in terms of space and (usually) cubic in terms of time, can be quite demanding for large problems."
- PENDING-EXTRA-E5 | page: 2, section: extracted, quote: "These are the greedy approaches (Section II-A), Nystr¨ om methods (Section II-B), and randomized algorithms (Section II-C)."
- PENDING-EXTRA-E6 | page: 5, section: extracted, quote: "Motivated by this observation and the fact that k-means clustering can ﬁnd a local minimum of the quantization error [42], we propose to use the cluster centers obtained from k-means as the landmark points in the Nystr¨om low-rank approximation, with the reconstruction step being the same as in the original Nystr¨om method (5)."
- PENDING-EXTRA-E7 | page: 6, section: extracted, quote: "EXPERIMENTS In this section, we perform extensive experiments to compare the proposed method with existing algorithms on the low-rank approximation of kernel matrix (Section IV-A), KPCA (Section IV-B), Laplaci an eigenmap, and spectral clustering (Section IV-C)."
- PENDING-EXTRA-E8 | page: 2, section: extracted, quote: "In Section IV, we experimentally compare our approach with a number of state-of-the-art low-rank decomposition techniques for manifold learning and dimensionality reduction, as well as supervised methods Gaussian process (GP) regression."
