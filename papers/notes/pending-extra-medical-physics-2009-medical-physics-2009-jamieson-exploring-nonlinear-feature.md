---
id: paper-2010-pending-extra-medical-physics-2009
title: "Exploring nonlinear feature space dimension reduction and data representation in breast CADx with Laplacian eigenmaps and ‐SNE"
authors: "Andrew R. Jamieson, Maryellen L. Giger, Karen Drukker, Hui Li, Yading Yuan, Neha Bhooshan"
venue: "Medical Physics"
year: 2010
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/Medical Physics - 2009 - Jamieson - Exploring nonlinear feature space dimension reduction and data representation in breast.pdf
seed_note_id: "paper-2025-jeon-reliable-va-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- 1,2 The present methods of interest to this study, Laplacian eigenmaps and t-SNE, offer two distinct approaches for explicitly addressing the challenge of capturing and efﬁciently representing the properties of the low dimensional manifold on which the original high dimensional data may lie.
- Current CADx feature representation Restricted by limited sample data sets, computational power, and lack of complete theoretical formalism, imagebased pattern recognition and classiﬁcation techniques often tackle the objective task at hand by substantially simplifying the problem.
- Classically, the problem of dimension reduction /H20849DR/H20850and data representation has been approached by applying linear transformations such as the well-known principal component analysis /H20849PCA/H20850or more general singular value decomposition.
- While not appropriate as a complete replacement of feature selection in CADx problems, DR techniques offer a complementary approach, which can aid elucidation of additional properties associated with the data.

# Method Summary
- The current study aims to explore the potential enhancements offered to breast mass lesion CADx algorithms through the application of two recently developed dimensionality reduction and data representation techniques, Laplacian eigenmaps and t-distributed stochastic neighbor embedding /H20849t-SNE/H20850.
- 1,2 The present methods of interest to this study, Laplacian eigenmaps and t-SNE, offer two distinct approaches for explicitly addressing the challenge of capturing and efﬁciently representing the properties of the low dimensional manifold on which the original high dimensional data may lie.
- Outline of evaluation for proposed methods The primary objective of this study is to evaluate the classiﬁcation performance characteristics of breast lesion CADx schemes employing the Laplacian eigenmap or t-SNE DR techniques in place of previously developed feature selection methods.
- In either case, when appropriately coupled with a wellregularized supervised classiﬁcation method, the ultimate objective of features selection is to discover the “optimal” data representation, or subset of features for robustly maximizing the desired diagnostic task performance.
- Traditionally, breast CADx systems employ a two pronged approach, ﬁrst, image preprocessing and feature extraction, and second, classiﬁcation in the feature space, either by unsupervised methods, supervised methods, or both.
- Conclusions: Preliminary results appear to indicate capability for the new methods to match or exceed classiﬁcation performance of current advanced breast lesion CADx algorithms.
- Additionally, the feasibility and robustness of these nonlinear reduction methods for CADx feature space reduction are tested across three separate imaging modalities: Ultrasound /H20849U.S./H20850, dynamic contrast enhanced MRI/H20849DCE-MRI/H20850, and full-ﬁeld digital mammography /H20849FFDM/H20850, having case sets of 1126, 356, and 245 cases, respectively.

# When To Use / Not Use
- Use when:
  - Understanding how to optimally make use of the enormity of the initial image information input and best arrive at the succinct conceptual notion of “diagnosis” is a formidable challenge.
  - This option can be used to avoid parameter selection.
- Avoid when:
  - Additionally, the feasibility and robustness of these nonlinear reduction methods for CADx feature space reduction are tested across three separate imaging modalities: Ultrasound /H20849U.S./H20850, dynamic contrast enhanced MRI/H20849DCE-MRI/H20850, and full-ﬁeld digital mammography /H20849FFDM/H20850, having case sets of 1126, 356, and 245 cases, respectively.
  - See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License dimensional Euclidean space using the m eigenvectors after the zero eigenvalued f0, xi → /H20849f1/H20849i/H20850,..., fm/H20849i/H20850/H20850.
- Failure modes:
  - Above three dimensions, as it becomes nontrivial to interpret the structure of the feature space, often instead, the use of a metrics such at the ROC curve and/or AUC based on output from the decision variable of a trained merged feature classiﬁer are used to interrogate the quality of the higher dimensional feature spaces.

# Metrics Mentioned
- `kl divergence`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- II. t-SNE algorithm outline Beginning with k input points /H20853x1 ,...,x k/H20854in Rl, set perplexity parameter Perp, number of iterations T, learning rate /H9257, and momentum /H9251/H20849t/H20850.
- 4–11,29 In each of the modalities, the lesion center is identiﬁed manually for the CADx algorithm, which then performs automated seeded segmentation of the lesion margin followed by computerized feature extraction.
- Giger, “Automated seeded lesion segmentation on digital mammograms,” IEEE Trans.
- This option can be used to avoid parameter selection.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-EXTRA-C1 | stance: support | summary: 1,2 The present methods of interest to this study, Laplacian eigenmaps and t-SNE, offer two distinct approaches for explicitly addressing the challenge of capturing and efﬁciently representing the properties of the low dimensional manifold on which the original high dimensional data may lie. | evidence_ids: PENDING-EXTRA-E1, PENDING-EXTRA-E2
- CLAIM-PENDING-EXTRA-C2 | stance: support | summary: The current study aims to explore the potential enhancements offered to breast mass lesion CADx algorithms through the application of two recently developed dimensionality reduction and data representation techniques, Laplacian eigenmaps and t-distributed stochastic neighbor embedding /H20849t-SNE/H20850. | evidence_ids: PENDING-EXTRA-E3, PENDING-EXTRA-E4
- CLAIM-PENDING-EXTRA-C3 | stance: support | summary: II. t-SNE algorithm outline Beginning with k input points /H20853x1 ,...,x k/H20854in Rl, set perplexity parameter Perp, number of iterations T, learning rate /H9257, and momentum /H9251/H20849t/H20850. | evidence_ids: PENDING-EXTRA-E5, PENDING-EXTRA-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 4 | relevance: high | note: contains initialization sensitivity or control-policy evidence

# Evidence
- PENDING-EXTRA-E1 | page: 3, section: extracted, quote: "1,2 The present methods of interest to this study, Laplacian eigenmaps and t-SNE, offer two distinct approaches for explicitly addressing the challenge of capturing and efﬁciently representing the properties of the low dimensional manifold on which the original high dimensional data may lie."
- PENDING-EXTRA-E2 | page: 2, section: extracted, quote: "Current CADx feature representation Restricted by limited sample data sets, computational power, and lack of complete theoretical formalism, imagebased pattern recognition and classiﬁcation techniques often tackle the objective task at hand by substantially simplifying the problem."
- PENDING-EXTRA-E3 | page: 3, section: extracted, quote: "Classically, the problem of dimension reduction /H20849DR/H20850and data representation has been approached by applying linear transformations such as the well-known principal component analysis /H20849PCA/H20850or more general singular value decomposition."
- PENDING-EXTRA-E4 | page: 1, section: extracted, quote: "While not appropriate as a complete replacement of feature selection in CADx problems, DR techniques offer a complementary approach, which can aid elucidation of additional properties associated with the data."
- PENDING-EXTRA-E5 | page: 2, section: extracted, quote: "The current study aims to explore the potential enhancements offered to breast mass lesion CADx algorithms through the application of two recently developed dimensionality reduction and data representation techniques, Laplacian eigenmaps and t-distributed stochastic neighbor embedding /H20849t-SNE/H20850."
- PENDING-EXTRA-E6 | page: 3, section: extracted, quote: "Outline of evaluation for proposed methods The primary objective of this study is to evaluate the classiﬁcation performance characteristics of breast lesion CADx schemes employing the Laplacian eigenmap or t-SNE DR techniques in place of previously developed feature selection methods."
- PENDING-EXTRA-E7 | page: 2, section: extracted, quote: "In either case, when appropriately coupled with a wellregularized supervised classiﬁcation method, the ultimate objective of features selection is to discover the “optimal” data representation, or subset of features for robustly maximizing the desired diagnostic task performance."
- PENDING-EXTRA-E8 | page: 2, section: extracted, quote: "Traditionally, breast CADx systems employ a two pronged approach, ﬁrst, image preprocessing and feature extraction, and second, classiﬁcation in the feature space, either by unsupervised methods, supervised methods, or both."
