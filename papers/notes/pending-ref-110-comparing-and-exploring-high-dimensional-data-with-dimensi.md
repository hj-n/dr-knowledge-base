---
id: paper-2020-pending-ref-110
title: "Comparing and Exploring High-Dimensional Data with Dimensionality Reduction Algorithms and Matrix Visualizations"
authors: "Rene Cutura, Michaël Aupetit, Jean-Daniel Fekete, and Michael Sedlmair"
venue: "Proceedings of the International Conference on Advanced Visual Interfaces"
year: 2020
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-110-2020-comparing-and-exploring-high-dimensional-data-with-dimensionality-reduction-algorithm.pdf
seed_note_id: "paper-2025-jeon-reliable-va-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- 1 INTRODUCTION This article addresses the problem of exploring and comparing high-dimensional (HD) data through multiple scatterplots coming from multidimensional projections, and a matrix visualizing the similarities and differences between them.
- Those distortions stem from the fact that the n-dimensional space usually cannot be mapped to correct distances in 2D (crowding problem).
- On the other side, DR methods use two dimensions instead of one to find an arrangement that respects HD distances in 2D, with other trade-offs regarding quality and artifacts: more degrees of freedom are available at the expenses of overplotting problems and visual artifacts such as missed and false neighbors [35].
- Comparing and Exploring High-Dimensional Data with Dimensionality Reduction Algorithms and Matrix Visualizations Rene Cutura, Michaël Aupetit, Jean-Daniel Fekete, Michael Sedlmair To cite this version: Rene Cutura, Michaël Aupetit, Jean-Daniel Fekete, Michael Sedlmair.

# Method Summary
- In summary, we make the following main contributions: • We propose a framework to visually compare different dimensional spaces and sub-spaces relying through matrix visualizations and multidimensional projections, • we illustrate this approach throughCompadre, a visualization prototype, and • we conduct a case study with author data of IEEE VIS publications from 1990 to 2018.
- Instead of focusing on comparing a large number of DR results, our main objective is to better support the piece-wise comparison of DR projections and their highdimensional spaces and sub-spaces.
- 3.3 Visual Encoding Before settling on matrix visualizations for showing discrepancies, we considered other visual encoding approaches, specifically Shepard-like diagrams and 2D projections.
- In this paper, we show that matrix visualizations are an adequate approach to fill this gap by directly encoding the differences between all points of different projections and spaces.
- ABSTRACT We propose Compadre, a tool for visual analysis for comparing distances of high-dimensional (HD) data and their low-dimensional projections.
- EmbComp [20] is a recent approach that seeks to bridge the usage of metrics and interactive visual analysis for analyzing different word embeddings.
- Another closely related approach is DimStiller [23], which guides the user in the process of comparing and selecting different DR algorithms.

# When To Use / Not Use
- Use when:
  - We also present a case study, in which we analyze IEEE VIS authors from 1990 to 2018, and gain new insights on the relationships Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page.
  - On the other side, DR methods use two dimensions instead of one to find an arrangement that respects HD distances in 2D, with other trade-offs regarding quality and artifacts: more degrees of freedom are available at the expenses of overplotting problems and visual artifacts such as missed and false neighbors [35].
- Avoid when:
  - The main idea of our approach is to display different facets of the HD data focused on similarities, but also visualizing their discrepancies, and coordinating these complementary views with interactions to support the (HD-2D), (2D-2D), and (Sub-Sub) analytic tasks mentioned above.
  - Yet, the projection is not revealing clusters or visual patterns clearly, and knowing that keywords are typically used in a noisy fashion by authors, we wonder if the coauthor subspace is cleaner than the joint subspaces.
- Failure modes:
  - Users might be interested in comparing entire datasets to each other, such as study data stemming from different populations, different subsets and facets of data, or the results of different data analysis algorithms.

# Metrics Mentioned
- `stress`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- There, users can select among different implemented DR algorithms (UMAP, t-SNE, TRIMAP, MDS, ISOMAP, PCA, LLE, and LTSA), parameterize them, select a distance metric, and set seed values.
- The choice of data features, similarity metric, type of DR, and parameters highly impact the resulting 2D layout summary of the data [35], while for matrices, re-ordering [6, 15] and color scale are the key factors.
- An overview map allows to arrange these projections by similarity and supports tasks such as analyzing the sensitivity of DR parameter settings.
- Closest to our work is VisCoDeR [12] which uses visual parameter space analysis [40] to compare 100s to 1000s of different DR projections.
- In contrast, t-SNE, as a non-linear DR method, can unroll the manifold if carefully parameterized [51].
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-110-C1 | stance: support | summary: 1 INTRODUCTION This article addresses the problem of exploring and comparing high-dimensional (HD) data through multiple scatterplots coming from multidimensional projections, and a matrix visualizing the similarities and differences between them. | evidence_ids: PENDING-REF-110-E1, PENDING-REF-110-E2
- CLAIM-PENDING-REF-110-C2 | stance: support | summary: In summary, we make the following main contributions: • We propose a framework to visually compare different dimensional spaces and sub-spaces relying through matrix visualizations and multidimensional projections, • we illustrate this approach throughCompadre, a visualization prototype, and • we conduct a case study with author data of IEEE VIS publications from 1990 to 2018. | evidence_ids: PENDING-REF-110-E3, PENDING-REF-110-E4
- CLAIM-PENDING-REF-110-C3 | stance: support | summary: There, users can select among different implemented DR algorithms (UMAP, t-SNE, TRIMAP, MDS, ISOMAP, PCA, LLE, and LTSA), parameterize them, select a distance metric, and set seed values. | evidence_ids: PENDING-REF-110-E5, PENDING-REF-110-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 4 | relevance: high | note: contains initialization sensitivity or control-policy evidence

# Evidence
- PENDING-REF-110-E1 | page: 3, section: extracted, quote: "1 INTRODUCTION This article addresses the problem of exploring and comparing high-dimensional (HD) data through multiple scatterplots coming from multidimensional projections, and a matrix visualizing the similarities and differences between them."
- PENDING-REF-110-E2 | page: 5, section: extracted, quote: "Those distortions stem from the fact that the n-dimensional space usually cannot be mapped to correct distances in 2D (crowding problem)."
- PENDING-REF-110-E3 | page: 4, section: extracted, quote: "On the other side, DR methods use two dimensions instead of one to find an arrangement that respects HD distances in 2D, with other trade-offs regarding quality and artifacts: more degrees of freedom are available at the expenses of overplotting problems and visual artifacts such as missed and false neighbors [35]."
- PENDING-REF-110-E4 | page: 1, section: extracted, quote: "Comparing and Exploring High-Dimensional Data with Dimensionality Reduction Algorithms and Matrix Visualizations Rene Cutura, Michaël Aupetit, Jean-Daniel Fekete, Michael Sedlmair To cite this version: Rene Cutura, Michaël Aupetit, Jean-Daniel Fekete, Michael Sedlmair."
- PENDING-REF-110-E5 | page: 3, section: extracted, quote: "In summary, we make the following main contributions: • We propose a framework to visually compare different dimensional spaces and sub-spaces relying through matrix visualizations and multidimensional projections, • we illustrate this approach throughCompadre, a visualization prototype, and • we conduct a case study with author data of IEEE VIS publications from 1990 to 2018."
- PENDING-REF-110-E6 | page: 4, section: extracted, quote: "Instead of focusing on comparing a large number of DR results, our main objective is to better support the piece-wise comparison of DR projections and their highdimensional spaces and sub-spaces."
- PENDING-REF-110-E7 | page: 7, section: extracted, quote: "3.3 Visual Encoding Before settling on matrix visualizations for showing discrepancies, we considered other visual encoding approaches, specifically Shepard-like diagrams and 2D projections."
- PENDING-REF-110-E8 | page: 4, section: extracted, quote: "In this paper, we show that matrix visualizations are an adequate approach to fill this gap by directly encoding the differences between all points of different projections and spaces."
