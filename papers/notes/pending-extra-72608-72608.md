---
id: paper-2019-pending-extra-72608
title: "Visual Analytics of Multidimensional Projections for Constructing Classifier Decision Boundary Maps"
authors: "Mateus Espadoto, Francisco Rodrigues, Alexandru Telea"
venue: "Proceedings of the 14th International Joint Conference on Computer Vision, Imaging and Computer Graphics Theory and Applications"
year: 2019
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/72608.pdf
seed_note_id: "paper-2025-jeon-reliable-va-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- We design and perform a detailed study aimed at ﬁnding the best DR techniques to use when creating trustworthy dense maps, by studying a large collection of 28 DR algorithms, 4 classiﬁers, and 2 datasets from a real-world challenging classiﬁcation problem.
- In turn, this means that (a) either the projection did a bad job (the island does not actually exist in the high-dimensional space D); or (b) the island actually exist in D, i.e., there are very similar samples that get assigned different labels.
- To limit the amount of work required to analyze over hundred classiﬁer-projection combinations, we designed a two-phase experiment where we pre-select the best projections (using a simple classiﬁcation problem) to study next in detail.
- 4.2 Phase 2: Reﬁned Insights on Complex Data We now examine how the ﬁve selected projections (in phase 1) perform on the 10-class dataset S10 which is a tough classiﬁcation problem (Xiao et al., 2017).

# Method Summary
- 6 CONCLUSIONS In this paper we have presented a methodology for evaluating the quality of multidimensional projections for the task of constructing 2D dense maps to visualize decision boundaries of ML classiﬁers.
- However, it is well known that different DR methods create widely different projections for the same input data (Nonato and Aupetit, 2018; van der Maaten and Postma, 2009; Sorzano et al., 2014).
- Using a visual analytics methodology, we next reﬁned our analysis to a small set of ﬁve high-quality projections, and found that t-SNE and UMAP perform best for this task.
- To visualize these, one typically constructs a scatterplot using projections or dimensionality reduction (DR) methods (Hoffman and Grinstein, 2002; Liu et al., 2015).
- All involved materials and methods (projections, datasets, dense maps, classiﬁers, automated workﬂow scripts) are available online (Espadoto et al., 2018).
- Visual Analytics of Multidimensional Projections for Constructing Classiﬁer Decision Boundary Maps 35 UMAP appear to be the best projections for constructing dense maps in terms of recognizability of decision boundaries in the produced patterns, limited errors (spurious islands), and concentration of confusion zones (misclassiﬁcations).
- Our key observations are as follows: Visual Analytics of Multidimensional Projections for Constructing Classiﬁer Decision Boundary Maps 33 Stability: The dense maps are surprisingly stable for the same projection over all four classiﬁers, except for LLA, LTSA, Random Projection (Gaussian), and Random Projection (Sparse).

# When To Use / Not Use
- Use when:
  - Different machine learning (ML) techniques exist to construct f , some of the best known being Support Vector Machines (SVM), k-Nearest Neighbors (k-NN), Logistic Regression (LR), Random Forests (RF), and Convolutional Neural Networks (CNN) (Krizhevsky et al., 2012).
  - We design and perform a detailed study aimed at ﬁnding the best DR techniques to use when creating trustworthy dense maps, by studying a large collection of 28 DR algorithms, 4 classiﬁers, and 2 datasets from a real-world challenging classiﬁcation problem.
- Avoid when:
  - However, such solutions have several limitations: Visualizing color-coded scatterplots of training and/or test sets does not actually show the decision boundaries, leaving the user to guess where these lie (Rauber et al., 2017b).
  - While useful and simple to construct, such scatterplots have the fundamental limitation that they do not show how the classiﬁer treats the entire universe D, but only a sparse sampling ST thereof.
- Failure modes:
  - Visual Analytics of Multidimensional Projections for Constructing Classiﬁer Decision Boundary Maps 35 UMAP appear to be the best projections for constructing dense maps in terms of recognizability of decision boundaries in the produced patterns, limited errors (spurious islands), and concentration of confusion zones (misclassiﬁcations).

# Metrics Mentioned
- `trustworthiness`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- As selection criteria, we considered well-known projections of high quality (following a recent survey (Nonato and Aupetit, 2018)), good computational scalability, ease of use (P should come with well-documented parameter presets), and publicly available implementation.
- Classiﬁers: We consider the same classiﬁers as in (Rodrigues et al., 2018): LR, RF, k-NN (implemented in scikit-learn, using their toolkit’s default parameters), and CNN (implemented in keras).
- This is due to the fact that we are not aware of any other scalable, generic, and publicly-available inverse projection alternative.
- Visual analysis of dimensionality reduction quality for parameterized projections.
- Adam: A method for stochastic optimization. arXiv:1412.6980v9 [cs.LG].
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-EXTRA-C1 | stance: support | summary: We design and perform a detailed study aimed at ﬁnding the best DR techniques to use when creating trustworthy dense maps, by studying a large collection of 28 DR algorithms, 4 classiﬁers, and 2 datasets from a real-world challenging classiﬁcation problem. | evidence_ids: PENDING-EXTRA-E1, PENDING-EXTRA-E2
- CLAIM-PENDING-EXTRA-C2 | stance: support | summary: 6 CONCLUSIONS In this paper we have presented a methodology for evaluating the quality of multidimensional projections for the task of constructing 2D dense maps to visualize decision boundaries of ML classiﬁers. | evidence_ids: PENDING-EXTRA-E3, PENDING-EXTRA-E4
- CLAIM-PENDING-EXTRA-C3 | stance: support | summary: As selection criteria, we considered well-known projections of high quality (following a recent survey (Nonato and Aupetit, 2018)), good computational scalability, ease of use (P should come with well-documented parameter presets), and publicly available implementation. | evidence_ids: PENDING-EXTRA-E5, PENDING-EXTRA-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-EXTRA-E1 | page: 1, section: extracted, quote: "We design and perform a detailed study aimed at ﬁnding the best DR techniques to use when creating trustworthy dense maps, by studying a large collection of 28 DR algorithms, 4 classiﬁers, and 2 datasets from a real-world challenging classiﬁcation problem."
- PENDING-EXTRA-E2 | page: 7, section: extracted, quote: "In turn, this means that (a) either the projection did a bad job (the island does not actually exist in the high-dimensional space D); or (b) the island actually exist in D, i.e., there are very similar samples that get assigned different labels."
- PENDING-EXTRA-E3 | page: 9, section: extracted, quote: "To limit the amount of work required to analyze over hundred classiﬁer-projection combinations, we designed a two-phase experiment where we pre-select the best projections (using a simple classiﬁcation problem) to study next in detail."
- PENDING-EXTRA-E4 | page: 7, section: extracted, quote: "4.2 Phase 2: Reﬁned Insights on Complex Data We now examine how the ﬁve selected projections (in phase 1) perform on the 10-class dataset S10 which is a tough classiﬁcation problem (Xiao et al., 2017)."
- PENDING-EXTRA-E5 | page: 9, section: extracted, quote: "6 CONCLUSIONS In this paper we have presented a methodology for evaluating the quality of multidimensional projections for the task of constructing 2D dense maps to visualize decision boundaries of ML classiﬁers."
- PENDING-EXTRA-E6 | page: 1, section: extracted, quote: "However, it is well known that different DR methods create widely different projections for the same input data (Nonato and Aupetit, 2018; van der Maaten and Postma, 2009; Sorzano et al., 2014)."
- PENDING-EXTRA-E7 | page: 9, section: extracted, quote: "Using a visual analytics methodology, we next reﬁned our analysis to a small set of ﬁve high-quality projections, and found that t-SNE and UMAP perform best for this task."
- PENDING-EXTRA-E8 | page: 2, section: extracted, quote: "To visualize these, one typically constructs a scatterplot using projections or dimensionality reduction (DR) methods (Hoffman and Grinstein, 2002; Liu et al., 2015)."
