---
id: paper-2024-pending-ref-099
title: "CLAMS: A Cluster Ambiguity Measure for Estimating Perceptual Variability in Visual Clustering"
authors: "Hyeon Jeon, Ghulam Jilani Quadri, Hyunwook Lee, Paul Rosen, Danielle Albers Szafir, and Jinwook Seo"
venue: "IEEE Transactions on Visualization and Computer Graphics"
year: 2024
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-099-2024-clams-a-cluster-ambiguity-measure-for-estimating-perceptual-variability-in-visual-clu.pdf
seed_note_id: "paper-2025-jeon-reliable-va-survey"
evidence_level: medium
updated_at: 2026-02-08
---
# Problem
- 6.1 Reducing Cluster Ambiguity of Nonlinear Dimensionality Reduction Embeddings 6.1.1 Problem Statement and System Design A common way to analyze the cluster structure of high-dimensional data is to use dimensionality reduction (DR) [50] techniques, e.g., t-SNE [74], Isomap [73], or UMAP [46], which synthesizes 2D representation (i.e., embedding) that preserves the original characteristics of the input high-dimensional data.
- This was done by applying eight dimensionality reduction (DR) techniques (t-SNE [74], UMAP [46], Densmap [49], Isomap [73], LLE [61], MDS [35], PCA [52], and Random Projection) to 96 high-dimensional datasets [31].
- For example, we can model the perceptual variability that may arise when examining cluster structures of high-dimensional data via scatterplot matrices or parallel coordinates.
- Note that GMM decomposition has been shown to be applicable to visual identification problems [2, 3], accurately representing a wide range of smooth cluster patterns.
- Visual clustering is an ill-posed problem, where there is no "ground truth" for clusters (i.e., it is not always possible to determine a “correct” clustering).

# Method Summary
- Here, we introduce an optimization system that can discover DR embeddings satisfying both high accuracy and low ambiguity, which we call AmbReducer.
- First, we propose AmbReducer, an optimization system that reduces the ambiguity of dimensionality reduction embeddings while maintaining accuracy.
- 7: Dimensionality reduction embeddings optimized solely based on the accuracy (top row; intermediate results of AmbReducer) and those optimized considering both accuracy and cluster ambiguity (bottom row; final results of AmbReducer).
- These metrics enable analysts to rapidly evaluate their scatterplots in terms of supporting general pattern exploration [11] or a specific perceptual task [4], and can also be used to optimize scatterplots [56].
- We compared the accuracy and cluster ambiguity of the intermediate (optimized solely on accuracy; blue) and final (optimized based on both accuracy and cluster ambiguity; orange) embeddings made by AmbReducer.
- A naïve approach in designing VQMs is to reuse existing algorithms (e.g., clustering techniques), where the performance of the algorithm is evaluated against the results of human experiments.
- We present that CLAMS can further optimize nonlinear dimensionality reduction embeddings to reduce cluster ambiguity while maintaining accuracy (Sect.

# When To Use / Not Use
- Use when:
  - To ensure that the evaluation reflected the maximum capability of clustering techniques, we ran Bayesian optimization and used the best score obtained while following the hyperparameter range setting of Jeon et al.
  - We found that CLAMS’s performance is better than the average performance of participants but fails to outperform the performance made by the best annotator. negligibleweakmoderatestrongvery strong Fig.
  - Given the significance of perceptual variability in information visualization [16,86], recent research explores when, where, and how perceptual variability influences visualization use (see Liu et al.
- Avoid when:
  - 6.1 Reducing Cluster Ambiguity of Nonlinear Dimensionality Reduction Embeddings 6.1.1 Problem Statement and System Design A common way to analyze the cluster structure of high-dimensional data is to use dimensionality reduction (DR) [50] techniques, e.g., t-SNE [74], Isomap [73], or UMAP [46], which synthesizes 2D representation (i.e., embedding) that preserves the original characteristics of the input high-dimensional data.
  - A is minimized when S is 0 or 1 (i.e., every participant gave the same answer, meaning there was no variability in visual clustering), and is maximized when S is 0.5 (i.e., half of the participants saw a single cluster and the other half saw more than one cluster, maximizing variability).
- Failure modes:
  - In contrast, CLAMS (α), which is constructed over perceptual data and a feature engineering based on a user study, automatically produces a score representing cluster ambiguity of an input scatterplot, where low and high scores correspond to clear and ambiguous cluster structure.
  - The detailed explanation of the experiment is as follows: Objectives and Design: We wanted to check whether the cluster ambiguity of benchmark datasets affects the stability of the ranking of clustering techniques, which we use as a proxy for the reliability of the evaluation.

# Metrics Mentioned
- `nh`: label-based neighborhood hit.
- `nd`: neighbor-shape dissimilarity or neighbor distortion.
- `pr`: pairwise-distance correlation behavior.
- `srho`: rank-correlation of pairwise distances.
- `ivm`: internal clustering validation behavior.
- `c_evm`: external clustering validation against labels.
- `snc`: Steadiness/Cohesiveness inter-cluster reliability.
- `topo`: topology-related structure behavior.
- `proc`: Procrustes local shape agreement.

# Implementation Notes
- This is done by searching a hyperparameter setting h1 = arg max h∈H m(t(Z, h)), where H denotes the set of every possible hyperparameter setting and t(Z, h) represents the embedding made with t using hyperparameter setting h.
- To ensure that the evaluation reflected the maximum capability of clustering techniques, we ran Bayesian optimization and used the best score obtained while following the hyperparameter range setting of Jeon et al.
- Assuming that a clustering technique with a specific hyperparameter setting represents a human’s perception, this method mimics human variability by running the technique under various hyperparameter settings.
- We can find an optimal hyperparameter setting using clustering validation measures [83], but the optimal setting may depend on the selection criteria [40].
- Except for PCA and MDS, we generated 20 scatterplots while randomly adjusting the hyperparameters to further diversify the patterns.
- Embedding varies by choice of DR technique or hyperparameter, where each can lead to significantly different analysis results.
- Keep preprocessing, initialization policy, and random-seed protocol fixed when comparing methods.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PAPER2024PENDINGRE-C1 | stance: support | summary: 6.1 Reducing Cluster Ambiguity of Nonlinear Dimensionality Reduction Embeddings 6.1.1 Problem Statement and System Design A common way to analyze the cluster structure of high-dimensional data is to use dimensionality reduction (DR) [50] techniques, e.g., t-SNE [74], Isomap [73], or UMAP [46], which synthesizes 2D representation (i.e., embedding) that preserves the original characteristics of the input high-dimensional data. | evidence_ids: PAPER2024PENDINGRE-E1, PAPER2024PENDINGRE-E2
- CLAIM-PAPER2024PENDINGRE-C2 | stance: support | summary: Here, we introduce an optimization system that can discover DR embeddings satisfying both high accuracy and low ambiguity, which we call AmbReducer. | evidence_ids: PAPER2024PENDINGRE-E3, PAPER2024PENDINGRE-E4
- CLAIM-PAPER2024PENDINGRE-C3 | stance: support | summary: This is done by searching a hyperparameter setting h1 = arg max h∈H m(t(Z, h)), where H denotes the set of every possible hyperparameter setting and t(Z, h) represents the embedding made with t using hyperparameter setting h. | evidence_ids: PAPER2024PENDINGRE-E5, PAPER2024PENDINGRE-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports task clarification before model selection
- step: 2 | relevance: medium | note: adds constraints for preprocessing and data-audit checks
- step: 3 | relevance: high | note: directly informs task-aligned technique/metric selection
- step: 6 | relevance: high | note: adds hyperparameter sensitivity or optimization guidance
- step: 7 | relevance: high | note: supports visualization interpretation and user explanation

# Evidence
- PAPER2024PENDINGRE-E1 | page: 7, section: extracted, quote: "6.1 Reducing Cluster Ambiguity of Nonlinear Dimensionality Reduction Embeddings 6.1.1 Problem Statement and System Design A common way to analyze the cluster structure of high-dimensional data is to use dimensionality reduction (DR) [50] techniques, e.g., t-SNE [74], Isomap [73], or UMAP [46], which synthesizes 2D representation (i.e., embedding) that preserves the original characteristics of the input high-dimensional data."
- PAPER2024PENDINGRE-E2 | page: 6, section: extracted, quote: "This was done by applying eight dimensionality reduction (DR) techniques (t-SNE [74], UMAP [46], Densmap [49], Isomap [73], LLE [61], MDS [35], PCA [52], and Random Projection) to 96 high-dimensional datasets [31]."
- PAPER2024PENDINGRE-E3 | page: 9, section: extracted, quote: "For example, we can model the perceptual variability that may arise when examining cluster structures of high-dimensional data via scatterplot matrices or parallel coordinates."
- PAPER2024PENDINGRE-E4 | page: 3, section: extracted, quote: "Note that GMM decomposition has been shown to be applicable to visual identification problems [2, 3], accurately representing a wide range of smooth cluster patterns."
- PAPER2024PENDINGRE-E5 | page: 2, section: extracted, quote: "Visual clustering is an ill-posed problem, where there is no 'ground truth' for clusters (i.e., it is not always possible to determine a “correct” clustering)."
- PAPER2024PENDINGRE-E6 | page: 8, section: extracted, quote: "We hypothesized that if the cluster ambiguity of a dataset (a scatterplot in this case) is high, then the clustering benchmark using the dataset is unreliable."
- PAPER2024PENDINGRE-E7 | page: 8, section: extracted, quote: "Here, we introduce an optimization system that can discover DR embeddings satisfying both high accuracy and low ambiguity, which we call AmbReducer."
- PAPER2024PENDINGRE-E8 | page: 2, section: extracted, quote: "First, we propose AmbReducer, an optimization system that reduces the ambiguity of dimensionality reduction embeddings while maintaining accuracy."
- PAPER2024PENDINGRE-E9 | page: 8, section: extracted, quote: "7: Dimensionality reduction embeddings optimized solely based on the accuracy (top row; intermediate results of AmbReducer) and those optimized considering both accuracy and cluster ambiguity (bottom row; final results of AmbReducer)."
- PAPER2024PENDINGRE-E10 | page: 2, section: extracted, quote: "These metrics enable analysts to rapidly evaluate their scatterplots in terms of supporting general pattern exploration [11] or a specific perceptual task [4], and can also be used to optimize scatterplots [56]."
- PAPER2024PENDINGRE-E11 | page: 8, section: extracted, quote: "We compared the accuracy and cluster ambiguity of the intermediate (optimized solely on accuracy; blue) and final (optimized based on both accuracy and cluster ambiguity; orange) embeddings made by AmbReducer."
- PAPER2024PENDINGRE-E12 | page: 2, section: extracted, quote: "A naïve approach in designing VQMs is to reuse existing algorithms (e.g., clustering techniques), where the performance of the algorithm is evaluated against the results of human experiments."
