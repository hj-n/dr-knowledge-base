---
id: paper-2019-pending-ref-032
title: "Dimensionality reduction for visualizing single-cell data using UMAP"
authors: "E. Becht et al"
venue: "Nature Biotechnology"
year: 2019
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-032-2019-dimensionality-reduction-for-visualizing-single-cell-data-using-umap.pdf
seed_note_id: "paper-2022-revisiting-dr-visual-cluster-analysis"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- The color-code is generated using the embedding of the full dataset and propagated to the subsamples.
- Scatterplots of six dimensionality -reduction methods and 6 datasets.

# Method Summary
- The color-code is generated using the embedding of the full dataset and propagated to the subsamples.
- Scatterplots of six dimensionality -reduction methods and 6 datasets.
- Each cluster medoid is represented after column -wise Z -score transformation. b) Identification of each phenograph cluster of both UMAP (left), t -SNE (middle) and 2D PCA (right).
- For clarity, only twelve clusters are shown per plot.
- Bottom: full Han dataset colored by sample type, Sample ID and pre-filtering status.
- Scatterplots of six dimensionality -reduction methods and 6 datasets.
- Cell populations are annotated using manual gating (Samusik dataset), manually-labelled Phenograph clusters (Wong dataset) or sample of origin (Han_400k dataset).

# When To Use / Not Use
- Use when:
  - The color-code is generated using the embedding of the full dataset and propagated to the subsamples.
  - Scatterplots of six dimensionality -reduction methods and 6 datasets.
- Avoid when:
  - Each cluster medoid is represented after column -wise Z -score transformation. b) Identification of each phenograph cluster of both UMAP (left), t -SNE (middle) and 2D PCA (right).
  - For clarity, only twelve clusters are shown per plot.
- Failure modes:
  - For clarity, only twelve clusters are shown per plot.

# Metrics Mentioned
- No explicit named metric was extracted from this source; combine this source with complementary DR quality checks in workflow Step 3.

# Implementation Notes
- Scatterplots of six dimensionality -reduction methods and 6 datasets.
- Each cluster medoid is represented after column -wise Z -score transformation. b) Identification of each phenograph cluster of both UMAP (left), t -SNE (middle) and 2D PCA (right).
- For clarity, only twelve clusters are shown per plot.
- Bottom: full Han dataset colored by sample type, Sample ID and pre-filtering status.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-032-C1 | stance: support | summary: The color-code is generated using the embedding of the full dataset and propagated to the subsamples. | evidence_ids: PENDING-REF-032-E1, PENDING-REF-032-E2
- CLAIM-PENDING-REF-032-C2 | stance: support | summary: The color-code is generated using the embedding of the full dataset and propagated to the subsamples. | evidence_ids: PENDING-REF-032-E3, PENDING-REF-032-E4
- CLAIM-PENDING-REF-032-C3 | stance: support | summary: Scatterplots of six dimensionality -reduction methods and 6 datasets. | evidence_ids: PENDING-REF-032-E5, PENDING-REF-032-E6

# Workflow Relevance Map
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 6 | relevance: high | note: guides reliable interpretation of projected views

# Evidence
- PENDING-REF-032-E1 | page: 9, section: extracted, quote: "The color-code is generated using the embedding of the full dataset and propagated to the subsamples."
- PENDING-REF-032-E2 | page: 6, section: extracted, quote: "Scatterplots of six dimensionality -reduction methods and 6 datasets."
- PENDING-REF-032-E3 | page: 1, section: extracted, quote: "Each cluster medoid is represented after column -wise Z -score transformation. b) Identification of each phenograph cluster of both UMAP (left), t -SNE (middle) and 2D PCA (right)."
- PENDING-REF-032-E4 | page: 1, section: extracted, quote: "For clarity, only twelve clusters are shown per plot."
- PENDING-REF-032-E5 | page: 5, section: extracted, quote: "Bottom: full Han dataset colored by sample type, Sample ID and pre-filtering status."
- PENDING-REF-032-E6 | page: 6, section: extracted, quote: "Cell populations are annotated using manual gating (Samusik dataset), manually-labelled Phenograph clusters (Wong dataset) or sample of origin (Han_400k dataset)."
