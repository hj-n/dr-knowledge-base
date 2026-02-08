---
id: paper-2024-pending-ref-111
title: "The art of seeing the elephant in the room: 2D embeddings of single-cell data do make sense"
authors: "Jan Lause, Philipp Berens, and Dmitry Kobak"
venue: "UNKNOWN"
year: 2024
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-111-2024-the-art-of-seeing-the-elephant-in-the-room-2d-embeddings-of-single-cell-data-do-make.pdf
seed_note_id: "paper-2025-stop-misusing-tsne-umap"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- More appropriate metrics quantifying neighborhood and class preservation reveal the elephant in the room: while t-SNE and UMAP embeddings of single-cell data do not represent high-dimensional distances, they can nevertheless provide biologically relevant information.
- Chari and Pachter (2023) criticized this practice: They claimed that the resulting 2D embeddings fail to faithfully represent the original high-dimensional space, and that instead of meaningful structure these embeddings exhibit “arbitrary” and “specious” shapes.
- For this, they used two metrics of embedding quality: inter-class correlation measured how well high-dimensional distances between class centroids were preserved in the 2D embedding, while intra-class correlation measured how well class variances were preserved.
- While we agree that 2D embeddings necessarily distort high-dimensional distances between data points (Nonato and Aupetit, 2018; Wang et al., 2023b), we believe that UMAP and t-SNE embeddings can nevertheless provide useful information.

# Method Summary
- For all metrics that required a high-dimensional reference space for comparison (inter-class and intra-class correlations, kNN recall), we used the same high-dimensional gene space that we used as input to the embedding methods.
- In single-cell genomics, researchers often visualize data with 2D embedding methods such as t-SNE (Van der Maaten and Hinton, 2008; Kobak and Berens, 2019) and UMAP (McInnes et al., 2018; Becht et al., 2019).
- Indeed, single-cell biologists rarely use multidimensional scaling (MDS), an embedding method explicitly designed to preserve distances, because MDS often fails to represent the cluster structure in the data.
- However, rejecting 2D embeddings altogether throws the baby out with the bathwater: It ignores that these methods do preserve neighbors and highlight high-dimensional cluster structure.
- Embeddings We used the high-dimensional gene space after pre-processing and gene selection as input to all embedding methods.
- Panels correspond to metrics, colors correspond to embedding methods, marker shapes correspond to datasets.
- More appropriate metrics quantifying neighborhood and class preservation reveal the elephant in the room: while t-SNE and UMAP embeddings of single-cell data do not represent high-dimensional distances, they can nevertheless provide biologically relevant information.

# When To Use / Not Use
- Use when:
  - We believe that this conclusion is wrong because the metrics used by Chari and Pachter (2023) were insufficient and only quantified a single aspect: both metrics focused on preservation of distances, where 2D PCA was unsurprisingly the best.
  - Indeed, single-cell biologists rarely use multidimensional scaling (MDS), an embedding method explicitly designed to preserve distances, because MDS often fails to represent the cluster structure in the data.
- Avoid when:
  - To quantify these aspects neglected byChari and Pachter (2023), we used four additional metrics, commonly employed in benchmark studies (Espadoto et al., 2021; Huang et al., 2022; Wang et al., 2023a): k-nearest-neighbor (kNN) accuracy, kNN recall (Lee and Verleysen, 2009), the silhouette coefficient (Rousseeuw,1987), and the adjusted mutual information (AMI) between clusters and class labels (Vinh et al., 2009).
  - For tSNE and UMAP, we followed Chari and Pachter (2023) and first reduced the pre-processed count matrices to 50 dimensions with PCA and used that as input to openTSNE 3 .CC-BY-NC-ND 4.0 International licensemade available under a (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity.
- Failure modes:
  - For this, they used two metrics of embedding quality: inter-class correlation measured how well high-dimensional distances between class centroids were preserved in the 2D embedding, while intra-class correlation measured how well class variances were preserved.

# Metrics Mentioned
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- For the maximum AMI metric, we ran HDBSCAN (McInnes and Healy, 2017) from scikit-learn on each embedding for nine hyperparameter values min samples = min size clusters ∈ { 5, 10, 15, 20, 30, 40, 50, 75, 100}.
- This way, the best performing hyperparameter was chosen for each embedding and each dataset.
- For the elephant embeddings, we used the original Picasso code by Chari and Pachter (2023) with minimal adjustments needed to provide the random seed for reproducibility ( https://github.com/ berenslab/picasso).
- The art of seeing the elephant in the room 1.0.1 (Poliˇ car et al.,2019) and umap-learn 0.5.5 with default parameters.
- Overdispersion parameter θ = 10 leads to some additional variance compared to the Poisson distribution.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-111-C1 | stance: support | summary: More appropriate metrics quantifying neighborhood and class preservation reveal the elephant in the room: while t-SNE and UMAP embeddings of single-cell data do not represent high-dimensional distances, they can nevertheless provide biologically relevant information. | evidence_ids: PENDING-REF-111-E1, PENDING-REF-111-E2
- CLAIM-PENDING-REF-111-C2 | stance: support | summary: For all metrics that required a high-dimensional reference space for comparison (inter-class and intra-class correlations, kNN recall), we used the same high-dimensional gene space that we used as input to the embedding methods. | evidence_ids: PENDING-REF-111-E3, PENDING-REF-111-E4
- CLAIM-PENDING-REF-111-C3 | stance: support | summary: For the maximum AMI metric, we ran HDBSCAN (McInnes and Healy, 2017) from scikit-learn on each embedding for nine hyperparameter values min samples = min size clusters ∈ { 5, 10, 15, 20, 30, 40, 50, 75, 100}. | evidence_ids: PENDING-REF-111-E5, PENDING-REF-111-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 4 | relevance: high | note: contains initialization sensitivity or control-policy evidence

# Evidence
- PENDING-REF-111-E1 | page: 1, section: extracted, quote: "More appropriate metrics quantifying neighborhood and class preservation reveal the elephant in the room: while t-SNE and UMAP embeddings of single-cell data do not represent high-dimensional distances, they can nevertheless provide biologically relevant information."
- PENDING-REF-111-E2 | page: 1, section: extracted, quote: "Chari and Pachter (2023) criticized this practice: They claimed that the resulting 2D embeddings fail to faithfully represent the original high-dimensional space, and that instead of meaningful structure these embeddings exhibit “arbitrary” and “specious” shapes."
- PENDING-REF-111-E3 | page: 2, section: extracted, quote: "For this, they used two metrics of embedding quality: inter-class correlation measured how well high-dimensional distances between class centroids were preserved in the 2D embedding, while intra-class correlation measured how well class variances were preserved."
- PENDING-REF-111-E4 | page: 1, section: extracted, quote: "While we agree that 2D embeddings necessarily distort high-dimensional distances between data points (Nonato and Aupetit, 2018; Wang et al., 2023b), we believe that UMAP and t-SNE embeddings can nevertheless provide useful information."
- PENDING-REF-111-E5 | page: 4, section: extracted, quote: "For all metrics that required a high-dimensional reference space for comparison (inter-class and intra-class correlations, kNN recall), we used the same high-dimensional gene space that we used as input to the embedding methods."
- PENDING-REF-111-E6 | page: 1, section: extracted, quote: "In single-cell genomics, researchers often visualize data with 2D embedding methods such as t-SNE (Van der Maaten and Hinton, 2008; Kobak and Berens, 2019) and UMAP (McInnes et al., 2018; Becht et al., 2019)."
- PENDING-REF-111-E7 | page: 3, section: extracted, quote: "Indeed, single-cell biologists rarely use multidimensional scaling (MDS), an embedding method explicitly designed to preserve distances, because MDS often fails to represent the cluster structure in the data."
- PENDING-REF-111-E8 | page: 3, section: extracted, quote: "However, rejecting 2D embeddings altogether throws the baby out with the bathwater: It ignores that these methods do preserve neighbors and highlight high-dimensional cluster structure."
