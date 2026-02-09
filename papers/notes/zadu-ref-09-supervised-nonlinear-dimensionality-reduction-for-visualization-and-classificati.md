---
id: paper-2005-zadu-ref-09
title: "Supervised Nonlinear Dimensionality Reduction for Visualization and Classification"
authors: "X. Geng, D.-C. Zhan, Z.-H. Zhou"
venue: "IEEE Transactions on Systems, Man and Cybernetics, Part B (Cybernetics)"
year: 2005
tags: [dr, zadu-table1-reference]
source_pdf: papers/raw/zadu-table1-references/Supervised_nonlinear_dimensionality_reduction_for_visualization_and_classification.pdf
evidence_level: medium
updated_at: 2026-02-08
---
# Problem
- Thus, the problem of high-dimensional data classiﬁcation can be solved by ﬁrst mapping the original data into a lower dimensional space by Isomap (which can be viewed as a preprocess) and then applying -NN classiﬁcation to the images.
- People working with them regularly confront the problem of dimensionality reduction, which is a procedure of ﬁnding intrinsic low-dimensional structures hidden in the high-dimensional observations.
- 6, DECEMBER 2005 Supervised Nonlinear Dimensionality Reduction for Visualization and Classiﬁcation Xin Geng, De-Chuan Zhan, and Zhi-Hua Zhou , Member, IEEE Abstract—When performing visualization and classiﬁcation, people often confront the problem of dimensionality reduction.
- Encouraging results have been reported when the test data contain little noise and are well sampled, but, as can been seen in the following sections of this paper, they are not so powerful when confronted with noisy data, which is often the case for real-world problems.
- The central idea of local embeddings is using the locally linear ﬁtting to solve the globally nonlinear problems, which is based on the assumption that data lying on a nonlinear manifold can be viewed as linear in local areas.

# Method Summary
- Both of these methods attempt to preserve as well as possible the local neighborhood of each object while trying to obtain highly nonlinear embeddings.
- To make the algorithm more robust for both visualization and classiﬁcation, a more sophisticated method is proposed in this section.
- Isomap and WeightedIso are used in classi ﬁcation in the similar way except that in the ﬁrst step, S-Isomap is replaced by Isomap and WeightedIso, respectively, and the corresponding classiﬁcation methods are still denoted by“Isomap” and “WeightedIso.” In the dimensionality reduction procedure, the dimensionality of the data is reduced to half of the original.
- Step 3) Construct -dimensional embedding: Let be the th eigenvalue (in decreasing order) of the matrix (The operator is de ﬁned by , where is the matrix of squared distances , and is the “centering matrix” is the Kronecker delta function [7]), and be the th component of the th eigenvector.
- Some preliminary efforts have already been taken toward supervised dimensionality reduction, such as the WeightedIso method [16], which changes the ﬁrst step of Isomap by rescaling the Euclidean distance between two data points with a constant factor if their class labels are the same.
- In the classiﬁcation experiments, S-Isomap is used as a preprocess of classiﬁcation and compared with Isomap, WeightedIso, as well as some other well-established classiﬁcation methods, including the K-nearest neighbor classiﬁer, BP neural network, J4.8 decision tree, and SVM.
- It is worth mentioning that the ten times ten-fold cross validation is completely separate with those used in parameter tuning, i.e., once the parameters for a certain method on a certain data set are determined, the data set is redivided ten times and tested.

# When To Use / Not Use
- Use when:
  - However, when Isomap is applied to real-world data, it shows some limitations, such as being sensitive to noise.
  - However, as can be seen in the following sections, when the input data are more complex and noisy, such as a set of face images captured by a web camera, Isomap often fails to nicely visualize them.
  - When S-Isomap is used for classi ﬁcation, the explicit mapping function from the original data space to the feature space is learned by some other nonlinear interpolation techniques.
- Avoid when:
  - Since such information is used to guide the dimensionality reduction in S-Isomap, when it is relatively limited, S-Isomap may be not signiﬁcantly superior to other methods.
  - Since the Euclidean distance is in the exponent, the parameter is used to prevent to increase too fast when is relatively large.
- Failure modes:
  - Isomap and WeightedIso are used in classi ﬁcation in the similar way except that in the ﬁrst step, S-Isomap is replaced by Isomap and WeightedIso, respectively, and the corresponding classiﬁcation methods are still denoted by“Isomap” and “WeightedIso.” In the dimensionality reduction procedure, the dimensionality of the data is reduced to half of the original.
  - Dimensionality reduction can be performed by keeping only the most important dimensions, i.e., the ones that hold the most useful information for the task at hand, or by projecting the original data into a lower dimensional space that is most expressive Manuscript received February 13, 2004; revised June 10, 2004.

# Metrics Mentioned
- `nh`: label-based neighborhood hit.
- `nd`: neighbor-shape dissimilarity or neighbor distortion.
- `pr`: pairwise-distance correlation behavior.
- `proc`: Procrustes local shape agreement.

# Implementation Notes
- In the following experiments, if not explicitly stated, the number of neighbors is set to 10 (including the parameter in Isomap, LLE, WeightedIso, and S-Isomap), the parameter in WeightedIso is set to 0.1, the parameter in S-Isomap is set to 0.5, and the parameter in S-Isomap is set to be the average Euclidean distance between all pairs of data points.
- It is worth mentioning that the ten times ten-fold cross validation is completely separate with those used in parameter tuning, i.e., once the parameters for a certain method on a certain data set are determined, the data set is redivided ten times and tested.
- The parameter gives a certain chance to the points in different classes to be“more similar,” i.e., to have a smaller value of dissimilarity, than those in the same class.
- Since the Euclidean distance is in the exponent, the parameter is used to prevent to increase too fast when is relatively large.
- That is, for each parameter, several values are tested through ten-fold cross validation and the best one is selected.
- The parameters for most of the methods are determined empirically through ten-fold cross validation.
- Keep preprocessing, initialization policy, and random-seed protocol fixed when comparing methods.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PAPER2005ZADUREF09-C1 | stance: support | summary: Thus, the problem of high-dimensional data classiﬁcation can be solved by ﬁrst mapping the original data into a lower dimensional space by Isomap (which can be viewed as a preprocess) and then applying -NN classiﬁcation to the images. | evidence_ids: PAPER2005ZADUREF09-E1, PAPER2005ZADUREF09-E2
- CLAIM-PAPER2005ZADUREF09-C2 | stance: support | summary: Both of these methods attempt to preserve as well as possible the local neighborhood of each object while trying to obtain highly nonlinear embeddings. | evidence_ids: PAPER2005ZADUREF09-E3, PAPER2005ZADUREF09-E4
- CLAIM-PAPER2005ZADUREF09-C3 | stance: support | summary: In the following experiments, if not explicitly stated, the number of neighbors is set to 10 (including the parameter in Isomap, LLE, WeightedIso, and S-Isomap), the parameter in WeightedIso is set to 0.1, the parameter in S-Isomap is set to 0.5, and the parameter in S-Isomap is set to be the average Euclidean distance between all pairs of data points. | evidence_ids: PAPER2005ZADUREF09-E5, PAPER2005ZADUREF09-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports task clarification before model selection
- step: 2 | relevance: medium | note: adds constraints for preprocessing and data-audit checks
- step: 3 | relevance: high | note: directly informs task-aligned technique/metric selection
- step: 6 | relevance: high | note: adds hyperparameter sensitivity or optimization guidance
- step: 7 | relevance: high | note: supports visualization interpretation and user explanation

# Evidence
- PAPER2005ZADUREF09-E1 | page: 2, section: extracted, quote: "Thus, the problem of high-dimensional data classiﬁcation can be solved by ﬁrst mapping the original data into a lower dimensional space by Isomap (which can be viewed as a preprocess) and then applying -NN classiﬁcation to the images."
- PAPER2005ZADUREF09-E2 | page: 1, section: extracted, quote: "People working with them regularly confront the problem of dimensionality reduction, which is a procedure of ﬁnding intrinsic low-dimensional structures hidden in the high-dimensional observations."
- PAPER2005ZADUREF09-E3 | page: 1, section: extracted, quote: "6, DECEMBER 2005 Supervised Nonlinear Dimensionality Reduction for Visualization and Classiﬁcation Xin Geng, De-Chuan Zhan, and Zhi-Hua Zhou , Member, IEEE Abstract—When performing visualization and classiﬁcation, people often confront the problem of dimensionality reduction."
- PAPER2005ZADUREF09-E4 | page: 1, section: extracted, quote: "Encouraging results have been reported when the test data contain little noise and are well sampled, but, as can been seen in the following sections of this paper, they are not so powerful when confronted with noisy data, which is often the case for real-world problems."
- PAPER2005ZADUREF09-E5 | page: 1, section: extracted, quote: "The central idea of local embeddings is using the locally linear ﬁtting to solve the globally nonlinear problems, which is based on the assumption that data lying on a nonlinear manifold can be viewed as linear in local areas."
- PAPER2005ZADUREF09-E6 | page: 1, section: extracted, quote: "The dissimilarity has several good properties which help to discover the true neighborhood of the data and, thus, makes S-Isomap a robust technique for both visualization and classiﬁcation, especially for real-world problems."
- PAPER2005ZADUREF09-E7 | page: 1, section: extracted, quote: "Both of these methods attempt to preserve as well as possible the local neighborhood of each object while trying to obtain highly nonlinear embeddings."
- PAPER2005ZADUREF09-E8 | page: 3, section: extracted, quote: "To make the algorithm more robust for both visualization and classiﬁcation, a more sophisticated method is proposed in this section."
- PAPER2005ZADUREF09-E9 | page: 7, section: extracted, quote: "Isomap and WeightedIso are used in classi ﬁcation in the similar way except that in the ﬁrst step, S-Isomap is replaced by Isomap and WeightedIso, respectively, and the corresponding classiﬁcation methods are still denoted by“Isomap” and “WeightedIso.” In the dimensionality reduction procedure, the dimensionality of the data is reduced to half of the original."
- PAPER2005ZADUREF09-E10 | page: 2, section: extracted, quote: "Step 3) Construct -dimensional embedding: Let be the th eigenvalue (in decreasing order) of the matrix (The operator is de ﬁned by , where is the matrix of squared distances , and is the “centering matrix” is the Kronecker delta function [7]), and be the th component of the th eigenvector."
- PAPER2005ZADUREF09-E11 | page: 2, section: extracted, quote: "Some preliminary efforts have already been taken toward supervised dimensionality reduction, such as the WeightedIso method [16], which changes the ﬁrst step of Isomap by rescaling the Euclidean distance between two data points with a constant factor if their class labels are the same."
- PAPER2005ZADUREF09-E12 | page: 1, section: extracted, quote: "In the classiﬁcation experiments, S-Isomap is used as a preprocess of classiﬁcation and compared with Isomap, WeightedIso, as well as some other well-established classiﬁcation methods, including the K-nearest neighbor classiﬁer, BP neural network, J4.8 decision tree, and SVM."
