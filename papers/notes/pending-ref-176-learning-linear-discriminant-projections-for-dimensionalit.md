---
id: paper-2011-pending-ref-176
title: "Learning Linear Discriminant Projections for Dimensionality Reduction of Image Descriptors"
authors: "Hongping Cai, K Mikolajczyk, J Matas"
venue: "IEEE Transactions on Pattern Analysis and Machine Intelligence"
year: 2011
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-176-2011-learning-linear-discriminant-projections-for-dimensionality-reduction-of-image-descri.pdf
seed_note_id: "paper-2014-sorzano-survey-dr-techniques"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- LDA can have at most Nc − 1 projections and suffers from small sample size problem in the case of high-dimensional data, which may lead to singular within-class scatter matrix.
- The distance between the points with the same label is reduced in the projected space while at the same time differently labeled points are made apart to avoid the problem of shrinking the entire data space.
- It is a signiﬁcant contribution as it makes it possible to apply the LDP as well as other discriminant projection approaches to the problems where point-topoint correspondence ground truth is not available.
- The patches from [10] are 64 ×64 pixels, with a canonical scale and orientation but all the experiments are performed on the center 36 ×36 pixels part to avoid boundary problems in the simulation process.

# Method Summary
- 3.1 Relations Between LDP and U Although the approaches to obtain the projection vectors LDP ( P ) [12] and U [11] differ, both methods use the same covariance matrices of pairwise matched feature distances and pairwise unmatched feature distances.
- In this paper we propose a general method for improving the descriptors and reducing their dimensionality by learning their discriminant projections from sample data.
- 3) An approach to train the projections for any data by generating simulated training set also applicable to other discriminant projection methods.
- It has been shown in [2] that many linear dimensionality reduction approaches share the same graph-preserving criterion. w∗ = arg min wT XBX T w=d ∑ i̸=j ∥wT xi − wT xj ∥2Wij = arg min wT XBX T w=d wT X(D − W )X T w (8) where D is a diagonal matrix with diagonal elements Dii = ∑ j Wij, d is a constant and B is a constraint matrix deﬁned to avoid a trivial solution of the objective function.
- In this paper, we show that the training based on simulated data can be successfully used for obtaining discriminant projections, and that it overcomes the issues related to data annotation and makes the LDP approach applicable to any dataset and any descriptor.
- Third approach (SIM) is to sample patches from the test images and to generate the simulated data with parameters estimated in experiment M03 for training the projections, which is possible in practical application scenario.
- In this paper, we build on the top of our initial work from [12], present Linear Discriminant Projections (LDP), analyze in depth their properties as well as relations to other approaches and show that it outperforms PCA.

# When To Use / Not Use
- Use when:
  - The descriptors can be made insensitive to small image perturbations, for example, by quantization or integration, that is robust to those perturbations.
  - Instead, the transformations can be applied to the image region before computing the descriptors, which can then be used to learn a robust feature.
- Avoid when:
  - Thus, 6 LDP can be viewed as a global version of LDE/MFA and it is not as sensitive to noise as local methods that use nearest neighbors only .
  - It has been shown in [2] that many linear dimensionality reduction approaches share the same graph-preserving criterion. w∗ = arg min wT XBX T w=d ∑ i̸=j ∥wT xi − wT xj ∥2Wij = arg min wT XBX T w=d wT X(D − W )X T w (8) where D is a diagonal matrix with diagonal elements Dii = ∑ j Wij, d is a constant and B is a constraint matrix deﬁned to avoid a trivial solution of the objective function.
- Failure modes:
  - All the experiments are tested on Scene-15 with the projections trained on different datasets. training set Scene-15 Patch Caltech101 VOC2007 P (30) 84.6 82.9 83.9 83.8 SIFT (128): 83.5 PCA (30): 82.9 (Liberty); 2) uniform sampling that is used in recognition task results in more diverse local structures than from the interest point detector used for the patch database.

# Metrics Mentioned
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- Third approach (SIM) is to sample patches from the test images and to generate the simulated data with parameters estimated in experiment M03 for training the projections, which is possible in practical application scenario.
- Simulation Parameters Since no point-to-point annotation exists in image/object categorization, the simulation strategy makes it possible to apply linear discriminant projections to local descriptors in this task.
- His research interests include object recognition, image r etrieval, sequential pattern recognition, ensemble methods, invari ant feature detection, and Hough Transform and RANSAC-type optimization.
- Distribution of 6 afﬁne parameters (rotation, scale log(s), skewing n, stretching log(q), dx translation and dy translation) in afﬁne transform between matched regions from 15 image sequences [31].
- T able 6 shows standard deviations of Gaussian distributions from which the parameters were randomly sampled and the recognition results for different transform combinations on scene-15 dataset.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-176-C1 | stance: support | summary: LDA can have at most Nc − 1 projections and suffers from small sample size problem in the case of high-dimensional data, which may lead to singular within-class scatter matrix. | evidence_ids: PENDING-REF-176-E1, PENDING-REF-176-E2
- CLAIM-PENDING-REF-176-C2 | stance: support | summary: 3.1 Relations Between LDP and U Although the approaches to obtain the projection vectors LDP ( P ) [12] and U [11] differ, both methods use the same covariance matrices of pairwise matched feature distances and pairwise unmatched feature distances. | evidence_ids: PENDING-REF-176-E3, PENDING-REF-176-E4
- CLAIM-PENDING-REF-176-C3 | stance: support | summary: Third approach (SIM) is to sample patches from the test images and to generate the simulated data with parameters estimated in experiment M03 for training the projections, which is possible in practical application scenario. | evidence_ids: PENDING-REF-176-E5, PENDING-REF-176-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-REF-176-E1 | page: 4, section: extracted, quote: "LDA can have at most Nc − 1 projections and suffers from small sample size problem in the case of high-dimensional data, which may lead to singular within-class scatter matrix."
- PENDING-REF-176-E2 | page: 3, section: extracted, quote: "The distance between the points with the same label is reduced in the projected space while at the same time differently labeled points are made apart to avoid the problem of shrinking the entire data space."
- PENDING-REF-176-E3 | page: 15, section: extracted, quote: "It is a signiﬁcant contribution as it makes it possible to apply the LDP as well as other discriminant projection approaches to the problems where point-topoint correspondence ground truth is not available."
- PENDING-REF-176-E4 | page: 9, section: extracted, quote: "The patches from [10] are 64 ×64 pixels, with a canonical scale and orientation but all the experiments are performed on the center 36 ×36 pixels part to avoid boundary problems in the simulation process."
- PENDING-REF-176-E5 | page: 6, section: extracted, quote: "3.1 Relations Between LDP and U Although the approaches to obtain the projection vectors LDP ( P ) [12] and U [11] differ, both methods use the same covariance matrices of pairwise matched feature distances and pairwise unmatched feature distances."
- PENDING-REF-176-E6 | page: 2, section: extracted, quote: "In this paper we propose a general method for improving the descriptors and reducing their dimensionality by learning their discriminant projections from sample data."
- PENDING-REF-176-E7 | page: 3, section: extracted, quote: "3) An approach to train the projections for any data by generating simulated training set also applicable to other discriminant projection methods."
- PENDING-REF-176-E8 | page: 6, section: extracted, quote: "It has been shown in [2] that many linear dimensionality reduction approaches share the same graph-preserving criterion. w∗ = arg min wT XBX T w=d ∑ i̸=j ∥wT xi − wT xj ∥2Wij = arg min wT XBX T w=d wT X(D − W )X T w (8) where D is a diagonal matrix with diagonal elements Dii = ∑ j Wij, d is a constant and B is a constraint matrix deﬁned to avoid a trivial solution of the objective function."
