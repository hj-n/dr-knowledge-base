---
id: paper-2025-pending-ref-054
title: "A Large-Scale Sensitivity Analysis on Latent Embeddings and Dimensionality Reductions for Text Spatializations"
authors: "D. Atzberger, T. Cech, W. Scheibel, J. Döllner, M. Behrisch, and T. Schreck"
venue: "IEEE Transactions on Visualization and Computer Graphics"
year: 2025
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-054-2025-a-large-scale-sensitivity-analysis-on-latent-embeddings-and-dimensionality-reductions.pdf
seed_note_id: "paper-2025-critical-analysis-dr-four-domains"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- Reinbold et al. applied k-order V oronoi diagrams to visualize the neighborhood preservation of several two-dimensional scatterplot representations of a high-dimensional dataset to analyze the stability of MDS and t-SNE concerning input data and hyperparameters [58].
- We further consider Bidirectional Encoder Representations from Transformers (BERT) - a deep learning model that is trained for two unsupervised NLP tasks and, as a result, generates high-dimensional representations for documents within a corpus [18].
- Changes to the underlying scatterplot are impeding the information exploration process since “geometric variations, e.g., rotation, translation, ..., in the projection make the analysis for the user difficult.
- It operates by modeling a Gaussian distribution centered around each data point in the high-dimensional space, where the perplexity hyperparameter regulates the effective number of neighbors considered.

# Method Summary
- Such scatterplots are derived from a layout algorithm that applies a dimensionality reduction (DR) to the DTM directly or an intermediate latent embedding of the text corpus, which is, for example, derived from a topic model (TM) [57].
- To draw a “big picture”, we further see possible applications of our evaluation setup – particularly the metrics – for selecting DRs for exploring different embeddings, e.g., internal representations of neural network approaches.
- Their studies are based on benchmarks comprising a set of text corpora, layout algorithms that are combinations of text embeddings and DRs, as well as metrics for quantifying the accuracy and cluster separation.
- Based on a detailed statistical analysis of the results, we analyzed the impact of the embedding algorithms and the DRs concerning the different stability aspects.
- The findings from such experiments could be integrated into visualization approaches that aim to help users explain high-dimensional embeddings [10, 64, 74].
- In this work, we present a sensitivity analysis of layout algorithms for text corpora concerning changes to the input data, hyperparameters, and randomness.
- Our work follows the methodology of such quantitative studies based on a benchmark comprising a set of text corpora, layout algorithms, and metrics.

# When To Use / Not Use
- Use when:
  - 2 R ELATED WORK We consider the following three aspects as related work: (1) previous studies that focused on the stability of DRs, (2) comparisons of DRs that propose guidelines for their effective use, and (3) studies that focus on the visual perception of scatterplots and allow for comparison of scatterplots using similarity measures.
  - From the study of the related work, we derived three different types of metrics for quantifying scatterplot similarity: (1) latent representations learned from neural networks, (2) perceptual similarity features, and (3) features that capture selected aspects, e.g., neighborhood preservation.
- Avoid when:
  - Thus, we define the global similarity measure β as β = 1 2 0.5 · (βPC + 1) +0.5 · (βSC + 1) 2 + 1 2 (βCO + 1) ! . (4) To quantify changes to the class separability, we use the absolute difference between the distance consistencies between two scatterplots.
  - 3.2 Document Embeddings Starting from the DTM representation, we further consider five additional document embeddings that are commonly used for corpus visualization and text analytics tasks, resulting in six latent representations for further analysis.
- Failure modes:
  - Xia et al. formulated similar findings after conducting a user study to investigate which DRs are suitable for visual cluster analysis tasks, e.g., cluster identification, membership identification, distance comparison, and density comparison [81].

# Metrics Mentioned
- `trustworthiness`: referenced as part of projection-quality or reliability assessment.
- `continuity`: referenced as part of projection-quality or reliability assessment.
- `stress`: referenced as part of projection-quality or reliability assessment.
- `procrustes-based quality`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- Nevertheless, one of our main findings, that embeddings can improve the stability concerning changes to the input data, the hyperparameters, and the random seed, was validated in our experiments by using embeddings following best practices.
- In this work, we present a sensitivity study that analyzes the stability of these layouts concerning (1) changes in the text corpora, (2) changes in the hyperparameter, and (3) randomness in the initialization.
- The number of iterations constitutes a hyperparameter of the model.
- For this, we compare the aggregated stability metrics ˜α, ˜β, and ˜γ in the case of stability concerning input data, and α, β, and γ in the case of the other two stability aspects of two pairs of scatterplots (Φ1(DTM), Φ2(DTM)) and (Φ1(DTMtf-idf), Φ2(DTMtf-idf)), where Φ1 and Φ2 are layout algorithms with specified hyperparameters that were compared in the respective experiment.
- Reinbold et al. applied k-order V oronoi diagrams to visualize the neighborhood preservation of several two-dimensional scatterplot representations of a high-dimensional dataset to analyze the stability of MDS and t-SNE concerning input data and hyperparameters [58].
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-054-C1 | stance: support | summary: Reinbold et al. applied k-order V oronoi diagrams to visualize the neighborhood preservation of several two-dimensional scatterplot representations of a high-dimensional dataset to analyze the stability of MDS and t-SNE concerning input data and hyperparameters [58]. | evidence_ids: PENDING-REF-054-E1, PENDING-REF-054-E2
- CLAIM-PENDING-REF-054-C2 | stance: support | summary: Such scatterplots are derived from a layout algorithm that applies a dimensionality reduction (DR) to the DTM directly or an intermediate latent embedding of the text corpus, which is, for example, derived from a topic model (TM) [57]. | evidence_ids: PENDING-REF-054-E3, PENDING-REF-054-E4
- CLAIM-PENDING-REF-054-C3 | stance: support | summary: Nevertheless, one of our main findings, that embeddings can improve the stability concerning changes to the input data, the hyperparameters, and the random seed, was validated in our experiments by using embeddings following best practices. | evidence_ids: PENDING-REF-054-E5, PENDING-REF-054-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 4 | relevance: high | note: contains initialization sensitivity or control-policy evidence

# Evidence
- PENDING-REF-054-E1 | page: 2, section: extracted, quote: "Reinbold et al. applied k-order V oronoi diagrams to visualize the neighborhood preservation of several two-dimensional scatterplot representations of a high-dimensional dataset to analyze the stability of MDS and t-SNE concerning input data and hyperparameters [58]."
- PENDING-REF-054-E2 | page: 3, section: extracted, quote: "We further consider Bidirectional Encoder Representations from Transformers (BERT) - a deep learning model that is trained for two unsupervised NLP tasks and, as a result, generates high-dimensional representations for documents within a corpus [18]."
- PENDING-REF-054-E3 | page: 1, section: extracted, quote: "Changes to the underlying scatterplot are impeding the information exploration process since “geometric variations, e.g., rotation, translation, ..., in the projection make the analysis for the user difficult."
- PENDING-REF-054-E4 | page: 4, section: extracted, quote: "It operates by modeling a Gaussian distribution centered around each data point in the high-dimensional space, where the perplexity hyperparameter regulates the effective number of neighbors considered."
- PENDING-REF-054-E5 | page: 1, section: extracted, quote: "Such scatterplots are derived from a layout algorithm that applies a dimensionality reduction (DR) to the DTM directly or an intermediate latent embedding of the text corpus, which is, for example, derived from a topic model (TM) [57]."
- PENDING-REF-054-E6 | page: 9, section: extracted, quote: "To draw a “big picture”, we further see possible applications of our evaluation setup – particularly the metrics – for selecting DRs for exploring different embeddings, e.g., internal representations of neural network approaches."
- PENDING-REF-054-E7 | page: 2, section: extracted, quote: "Their studies are based on benchmarks comprising a set of text corpora, layout algorithms that are combinations of text embeddings and DRs, as well as metrics for quantifying the accuracy and cluster separation."
- PENDING-REF-054-E8 | page: 9, section: extracted, quote: "Based on a detailed statistical analysis of the results, we analyzed the impact of the embedding algorithms and the DRs concerning the different stability aspects."
