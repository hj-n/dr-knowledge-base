---
id: paper-2026-pending-extra-topoinvis2015
title: "Agreement Analysis of Quality Measures for Dimensionality Reduction"
authors: "Bastian Rieck, Heike Leitte"
venue: "Mathematics and Visualization"
year: 2017
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/TopoInVis2015.pdf
seed_note_id: "paper-2025-jeon-reliable-va-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- Agreement analysis of quality measures for dimensionality reduction Bastian Rieck and Heike Leitte Abstract High-dimensional data sets commonly occur in various application domains.
- For an embedding of a high-dimensional data set, we are thus interested in ﬁnding out which properties (e.g. neighbourhoods, distances, etc.) of it are faithfully retained.
- 4.1.2 The high-dimensional case For a discrete set of unstructured points D ⊆ Rn, we need an auxiliary construction before calculating persistent homology.
- The higher stress values in the bottom part of this region indicate that the distances in t-SNE do not reﬂect the high-dimensional distances very well.

# Method Summary
- We propose an algorithm based on persistent homology that permits the comparative analysis of different quality measures on a given embedding, regardless of their ranges.
- 5.1 Swiss roll The Swiss roll data set is a classical data set that was introduced by Tenenbaum et al. [21] as an example of how non-linear embedding methods ( Isomap) are able to outperform classical linear embeddings (PCA) on certain data sets.
- Since τ affects which peaks are considered relevant and which peaks are considered noise by the algorithm, below we present an algorithm for choosing it automatically, based on the input data.
- Using several real-world data sets, we demonstrate how our method helps users determine which properties of a data set have been respected by an embedding.
- Their algorithm does not allow for comparing clusters in different scalar ﬁelds but has well-deﬁned stability guarantees that we will use in our approach.
- This Agreement analysis of quality measures for dimensionality reduction 3 approach is related to other methods from scalar ﬁeld topology.
- 6 Conclusion We introduced a method for comparing the behaviour of different quality measures for dimensionality reduction algorithms.

# When To Use / Not Use
- Use when:
  - Given an embedding of a data set and several quality measures, users often want to know about compromise solutions: For example, an embedding that distorts local neighbourhoods somewhat but keeps the global structure of the data set intact might be preferable over an embedding that does not distort local neighbourhoods but completely distorts the input data at a global scale.
  - In order to have a ﬁne-grained control about which peaks to consider signiﬁcant and which peaks to prune because they are unstable, Chazal et al. [4] suggest merging peaks based on the differences in their persistence.
- Avoid when:
  - Faced with multiple quality measures with different ranges and different value distributions, it is challenging to decide which aspects of a data set are preserved best by an embedding.
  - To deﬁne similarity between features, they use similarity measures based on the approximated contour volume as well as information-theoretic and graph clustering methods.
- Failure modes:
  - MRRE and rank correlation, by contrast, decompose the top part of the data further into two regions A and B because the corresponding peaks are separated by lower values.

# Metrics Mentioned
- `stress`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- Using the largest vertical distance—which is the width of the desired empty region—and the y-coordinate at which it was detected, we obtain a potential value for the threshold parameter τ.
- The distance to the diagonal from any point within this region is then an admissible value for the threshold parameter τ, which remains stable over a large range.
- Their method is used for parameter studies but does not permit the comparison of multiple scalar ﬁelds.
- When arriving at an existing peak during the iteration, a new entry is added to the data structure.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-EXTRA-C1 | stance: support | summary: Agreement analysis of quality measures for dimensionality reduction Bastian Rieck and Heike Leitte Abstract High-dimensional data sets commonly occur in various application domains. | evidence_ids: PENDING-EXTRA-E1, PENDING-EXTRA-E2
- CLAIM-PENDING-EXTRA-C2 | stance: support | summary: We propose an algorithm based on persistent homology that permits the comparative analysis of different quality measures on a given embedding, regardless of their ranges. | evidence_ids: PENDING-EXTRA-E3, PENDING-EXTRA-E4
- CLAIM-PENDING-EXTRA-C3 | stance: support | summary: Using the largest vertical distance—which is the width of the desired empty region—and the y-coordinate at which it was detected, we obtain a potential value for the threshold parameter τ. | evidence_ids: PENDING-EXTRA-E5, PENDING-EXTRA-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-EXTRA-E1 | page: 1, section: extracted, quote: "Agreement analysis of quality measures for dimensionality reduction Bastian Rieck and Heike Leitte Abstract High-dimensional data sets commonly occur in various application domains."
- PENDING-EXTRA-E2 | page: 2, section: extracted, quote: "For an embedding of a high-dimensional data set, we are thus interested in ﬁnding out which properties (e.g. neighbourhoods, distances, etc.) of it are faithfully retained."
- PENDING-EXTRA-E3 | page: 6, section: extracted, quote: "4.1.2 The high-dimensional case For a discrete set of unstructured points D ⊆ Rn, we need an auxiliary construction before calculating persistent homology."
- PENDING-EXTRA-E4 | page: 11, section: extracted, quote: "The higher stress values in the bottom part of this region indicate that the distances in t-SNE do not reﬂect the high-dimensional distances very well."
- PENDING-EXTRA-E5 | page: 1, section: extracted, quote: "We propose an algorithm based on persistent homology that permits the comparative analysis of different quality measures on a given embedding, regardless of their ranges."
- PENDING-EXTRA-E6 | page: 9, section: extracted, quote: "5.1 Swiss roll The Swiss roll data set is a classical data set that was introduced by Tenenbaum et al. [21] as an example of how non-linear embedding methods ( Isomap) are able to outperform classical linear embeddings (PCA) on certain data sets."
- PENDING-EXTRA-E7 | page: 7, section: extracted, quote: "Since τ affects which peaks are considered relevant and which peaks are considered noise by the algorithm, below we present an algorithm for choosing it automatically, based on the input data."
- PENDING-EXTRA-E8 | page: 2, section: extracted, quote: "Using several real-world data sets, we demonstrate how our method helps users determine which properties of a data set have been respected by an embedding."
