---
id: paper-2022-pending-ref-138
title: "Distortionaware brushing for interactive cluster analysis in multidimensional projections"
authors: "H. Jeon, M. Aupetit, S. Lee, H.-K. Ko, Y . Kim, and J. Seo"
venue: "IEEE Transactions on Visualization and Computer Graphics"
year: 2022
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-138-2022-distortionaware-brushing-for-interactive-cluster-analysis-in-multidimensional-project.pdf
seed_note_id: "paper-2025-critical-analysis-dr-four-domains"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- For example, we can model the perceptual variability that may arise when examining cluster structures of high-dimensional data via scatterplot matrices or parallel coordinates.
- Note that GMM decomposition has been shown to be applicable to visual identification problems [2, 3], accurately representing a wide range of smooth cluster patterns.
- Visual clustering is an ill-posed problem, where there is no "ground truth" for clusters (i.e., it is not always possible to determine a “correct” clustering).
- We hypothesized that if the cluster ambiguity of a dataset (a scatterplot in this case) is high, then the clustering benchmark using the dataset is unreliable.

# Method Summary
- A naïve approach in designing VQMs is to reuse existing algorithms (e.g., clustering techniques), where the performance of the algorithm is evaluated against the results of human experiments.
- We present that CLAMS can further optimize nonlinear dimensionality reduction embeddings to reduce cluster ambiguity while maintaining accuracy (Sect.
- First, we propose AmbReducer, an optimization system that reduces the ambiguity of dimensionality reduction embeddings while maintaining accuracy.
- 5.1.1 Study Design Objectives and Design: The study aimed to achieve two objectives: (1) to investigate the accuracy of our regression module in estimating human-judged separability and (2) to analyze how much each feature contributed to the model performance (i.e., the significance of features).
- The detailed explanation of the experiment is as follows: Objectives and Design: We wanted to check whether the cluster ambiguity of benchmark datasets affects the stability of the ranking of clustering techniques, which we use as a proxy for the reliability of the evaluation.
- The elbow is found using the Kneedle [65] algorithm. (Step 2) Component-Pairwise Local Ambiguity Computation We predict local ambiguity for every pair of Gaussian components so that CLAMS can consider every possible interaction between components.
- This is because, unlike other EVMs that interpret clustering assignments as a probabilistic event, arand discretely “counts” the disagreement of clustering results and thus generates results that do not align with our probabilistic approach.

# When To Use / Not Use
- Use when:
  - To ensure that the evaluation reflected the maximum capability of clustering techniques, we ran Bayesian optimization and used the best score obtained while following the hyperparameter range setting of Jeon et al. [31].
  - In contrast, CLAMS (α), which is constructed over perceptual data and a feature engineering based on a user study, automatically produces a score representing cluster ambiguity of an input scatterplot, where low and high scores correspond to clear and ambiguous cluster structure.
- Avoid when:
  - The detailed explanation of the experiment is as follows: Objectives and Design: We wanted to check whether the cluster ambiguity of benchmark datasets affects the stability of the ranking of clustering techniques, which we use as a proxy for the reliability of the evaluation.
  - For example, degradation resulting from switching off AC and DC together was substantially higher than the sum of degradation caused by switching off the features individually and was also higher than the largest degradation possible by removing a single feature (DSR).
- Failure modes:
  - Ellipticity Difference (ED): We directly used ellipticity difference as a feature, defining the ellipticity of a component as the one of an ellipse having the standard deviation along the first and second principal axes as major and minor axes’ lengths, respectively.

# Metrics Mentioned
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- To ensure that the evaluation reflected the maximum capability of clustering techniques, we ran Bayesian optimization and used the best score obtained while following the hyperparameter range setting of Jeon et al. [31].
- This is done by searching a hyperparameter setting h1 = arg max h∈H m(t(Z, h)), where H denotes the set of every possible hyperparameter setting and t(Z, h) represents the embedding made with t using hyperparameter setting h.
- Assuming that a clustering technique with a specific hyperparameter setting represents a human’s perception, this method mimics human variability by running the technique under various hyperparameter settings.
- Formally, this is done by finding hyperparameter setting h2 = arg maxh∈H loss(h, h1), where loss is defined as loss(h, h1) =  CA(t(X, h)) if | m(t(Z, h1))−m(t(Z, h)) |< τ ∞ if | m(t(Z, h1))−m(t(Z, h)) |> τ .
- We can find an optimal hyperparameter setting using clustering validation measures [83], but the optimal setting may depend on the selection criteria [40].
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-138-C1 | stance: support | summary: For example, we can model the perceptual variability that may arise when examining cluster structures of high-dimensional data via scatterplot matrices or parallel coordinates. | evidence_ids: PENDING-REF-138-E1, PENDING-REF-138-E2
- CLAIM-PENDING-REF-138-C2 | stance: support | summary: A naïve approach in designing VQMs is to reuse existing algorithms (e.g., clustering techniques), where the performance of the algorithm is evaluated against the results of human experiments. | evidence_ids: PENDING-REF-138-E3, PENDING-REF-138-E4
- CLAIM-PENDING-REF-138-C3 | stance: support | summary: To ensure that the evaluation reflected the maximum capability of clustering techniques, we ran Bayesian optimization and used the best score obtained while following the hyperparameter range setting of Jeon et al. [31]. | evidence_ids: PENDING-REF-138-E5, PENDING-REF-138-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-REF-138-E1 | page: 9, section: extracted, quote: "For example, we can model the perceptual variability that may arise when examining cluster structures of high-dimensional data via scatterplot matrices or parallel coordinates."
- PENDING-REF-138-E2 | page: 3, section: extracted, quote: "Note that GMM decomposition has been shown to be applicable to visual identification problems [2, 3], accurately representing a wide range of smooth cluster patterns."
- PENDING-REF-138-E3 | page: 1, section: extracted, quote: "Visual clustering is an ill-posed problem, where there is no 'ground truth' for clusters (i.e., it is not always possible to determine a “correct” clustering)."
- PENDING-REF-138-E4 | page: 8, section: extracted, quote: "We hypothesized that if the cluster ambiguity of a dataset (a scatterplot in this case) is high, then the clustering benchmark using the dataset is unreliable."
- PENDING-REF-138-E5 | page: 2, section: extracted, quote: "A naïve approach in designing VQMs is to reuse existing algorithms (e.g., clustering techniques), where the performance of the algorithm is evaluated against the results of human experiments."
- PENDING-REF-138-E6 | page: 7, section: extracted, quote: "We present that CLAMS can further optimize nonlinear dimensionality reduction embeddings to reduce cluster ambiguity while maintaining accuracy (Sect."
- PENDING-REF-138-E7 | page: 2, section: extracted, quote: "First, we propose AmbReducer, an optimization system that reduces the ambiguity of dimensionality reduction embeddings while maintaining accuracy."
- PENDING-REF-138-E8 | page: 5, section: extracted, quote: "5.1.1 Study Design Objectives and Design: The study aimed to achieve two objectives: (1) to investigate the accuracy of our regression module in estimating human-judged separability and (2) to analyze how much each feature contributed to the model performance (i.e., the significance of features)."
