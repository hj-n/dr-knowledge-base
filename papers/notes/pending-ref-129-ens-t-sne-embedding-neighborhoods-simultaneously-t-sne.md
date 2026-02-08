---
id: paper-2024-pending-ref-129
title: "ENS-t-SNE: Embedding Neighborhoods Simultaneously t-SNE"
authors: "Jacob Miller, Vahan Huroyan, Raymundo Navarrete, Md Iqbal Hossain, and Stephen Kobourov"
venue: "2024 IEEE 17th Pacific Visualization Conference (PacificVis)"
year: 2024
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-129-2024-ens-t-sne-embedding-neighborhoods-simultaneously-t-sne.pdf
seed_note_id: "paper-2025-stop-misusing-tsne-umap"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- 1.2 Our Contributions We propose, describe and provide an implementation for ENS-t-SNE: a technique to perform dimension reduction on a high-dimensional dataset that captures multiple subspaces of interest in a single 3D embedding.
- First, subspace clustering algorithms are the natural way to select interesting subspaces as input into ENS-t-SNE, especially for truly large and high-dimensional datasets where domain knowledge and expertise might not be enough.
- Even with coordinated views, it is difficult to track where groups of points go from one projection to the next, in effect offloading the mental effort of comparison to the user [16].
- Abstract—When visualizing a high-dimensional dataset, dimension reduction techniques are commonly employed which provide a single 2 dimensional view of the data.

# Method Summary
- The approaches above seek to achieve one of two objectives: either generating an embedding that encompasses multiple subspaces [38–40], thereby potentially blending the information and lacking a guarantee of preserving individual subspaces of interest, or solely creating 2D projections where each corresponds to a distinct subspace [30, 31].
- The MPSE algorithm can be seen as a generalization of MDS that is able to visualize multiple distance matrices simultaneously, by producing a three-dimensional embedding, so that the different distance matrices are preserved after projecting the 3D coordinates to 2D ones using specified projections.
- We describe ENS-t-SNE: an algorithm for Embedding Neighborhoods Simultaneously that generalizes the t-Stochastic Neighborhood Embedding approach.
- The objective function eC is a function of the embedding y1, . . . ,yN and projections Π1, . . . ,ΠM.
- Some recent algorithms for simultaneous embedding/multiview embedding include Multiview Stochastic Neighbor Embedding (m-SNE) [39, 40], based on a probabilistic framework that integrates heterogeneous features of the dataset into one combined embedding and Multiview Spectral Embedding (MSE) [38], which encodes features in such a way to achieve a physically meaningful embedding.
- Motivated by such 3D physicalizations, as well as by work on Multi-Perspective Simultaneous Embedding [19], our proposed algorithm enables viewers to virtually “walk around” an ENS-t-SNE embedding and see different aspects of the same dataset.
- 1https://www.jameshopkinsworks.com/commissions4.html 2https://trendland.com/troika-squaring-the-circle/ 1 arXiv:2205.11720v3 [cs.LG] 30 Mar 2024 We present a technique to capture multiple subspaces of interest in a single 3D embedding.

# When To Use / Not Use
- Use when:
  - In practice, we found that a combination of adaptive learning rate and stochastic gradient descent works the best in consistently avoiding local minima.
  - In order to measure the accuracy of the embedding for a dataset containing several clusters, we define the separation error as follows: For a 2D image containing two labels, the best linear classifier is found and the proportion of errors in this classification is returned.
- Avoid when:
  - The perplexity is defined as Perp(Pm i ) = 2H(Pm i ), (8) where H(Pm i ) is the Shannon entropy function, defined as H(Pm i ) = −∑ j pm j|i log2(pm j|i). (9) In order to optimize the objective function of ENS-T-SNE(5) we use stochastic gradient descent discussed in Sec.
  - The USDA food composition dataset is frequently analyzed in subspace clustering literature; we use two interesting subspaces identified by Tatu et al. [34] and show how ENS-t-SNE can provide insights about the different groups in the data.
- Failure modes:
  - 1https://www.jameshopkinsworks.com/commissions4.html 2https://trendland.com/troika-squaring-the-circle/ 1 arXiv:2205.11720v3 [cs.LG] 30 Mar 2024 We present a technique to capture multiple subspaces of interest in a single 3D embedding.

# Metrics Mentioned
- `trustworthiness`: referenced as part of projection-quality or reliability assessment.
- `continuity`: referenced as part of projection-quality or reliability assessment.
- `stress`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- Although the original paper proposes default values and ranges for the t-SNE hyperparameters (perplexity, learning rate, etc.), automatically selecting these parameters is also a topic of interest [7, 9]. recent paper reviews t-SNE and applications thereof [15].
- When using this initialization scheme we also deterministically compute a set of 2x3 orthogonal matrices, ensuring that the ENS-t-SNE optimization is deterministic.
- The results indicate that the runtime of ENS-t-SNE scales reasonably well as these parameters increase.
- Therefore, we devise a ‘smart initialization’ strategy by first taking the average over all pairwise dissimilarity matrices and then applying dimensionality reduction to 3D via classical (Torgerson) MDS [35].
- We wish to minimize the following cost function eC(X, Π;perp 1,perp2, . . . ,perpM) = M ∑ m=1 C(ΠmX;perp m) (18) where Y 7→ C(Y ;perp m) is the t-SNE cost function with perplexity parameter perpm.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-129-C1 | stance: support | summary: 1.2 Our Contributions We propose, describe and provide an implementation for ENS-t-SNE: a technique to perform dimension reduction on a high-dimensional dataset that captures multiple subspaces of interest in a single 3D embedding. | evidence_ids: PENDING-REF-129-E1, PENDING-REF-129-E2
- CLAIM-PENDING-REF-129-C2 | stance: support | summary: The approaches above seek to achieve one of two objectives: either generating an embedding that encompasses multiple subspaces [38–40], thereby potentially blending the information and lacking a guarantee of preserving individual subspaces of interest, or solely creating 2D projections where each corresponds to a distinct subspace [30, 31]. | evidence_ids: PENDING-REF-129-E3, PENDING-REF-129-E4
- CLAIM-PENDING-REF-129-C3 | stance: support | summary: Although the original paper proposes default values and ranges for the t-SNE hyperparameters (perplexity, learning rate, etc.), automatically selecting these parameters is also a topic of interest [7, 9]. recent paper reviews t-SNE and applications thereof [15]. | evidence_ids: PENDING-REF-129-E5, PENDING-REF-129-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 4 | relevance: high | note: contains initialization sensitivity or control-policy evidence

# Evidence
- PENDING-REF-129-E1 | page: 2, section: extracted, quote: "1.2 Our Contributions We propose, describe and provide an implementation for ENS-t-SNE: a technique to perform dimension reduction on a high-dimensional dataset that captures multiple subspaces of interest in a single 3D embedding."
- PENDING-REF-129-E2 | page: 2, section: extracted, quote: "First, subspace clustering algorithms are the natural way to select interesting subspaces as input into ENS-t-SNE, especially for truly large and high-dimensional datasets where domain knowledge and expertise might not be enough."
- PENDING-REF-129-E3 | page: 1, section: extracted, quote: "Even with coordinated views, it is difficult to track where groups of points go from one projection to the next, in effect offloading the mental effort of comparison to the user [16]."
- PENDING-REF-129-E4 | page: 1, section: extracted, quote: "Abstract—When visualizing a high-dimensional dataset, dimension reduction techniques are commonly employed which provide a single 2 dimensional view of the data."
- PENDING-REF-129-E5 | page: 2, section: extracted, quote: "The approaches above seek to achieve one of two objectives: either generating an embedding that encompasses multiple subspaces [38–40], thereby potentially blending the information and lacking a guarantee of preserving individual subspaces of interest, or solely creating 2D projections where each corresponds to a distinct subspace [30, 31]."
- PENDING-REF-129-E6 | page: 3, section: extracted, quote: "The MPSE algorithm can be seen as a generalization of MDS that is able to visualize multiple distance matrices simultaneously, by producing a three-dimensional embedding, so that the different distance matrices are preserved after projecting the 3D coordinates to 2D ones using specified projections."
- PENDING-REF-129-E7 | page: 1, section: extracted, quote: "We describe ENS-t-SNE: an algorithm for Embedding Neighborhoods Simultaneously that generalizes the t-Stochastic Neighborhood Embedding approach."
- PENDING-REF-129-E8 | page: 3, section: extracted, quote: "The objective function eC is a function of the embedding y1, . . . ,yN and projections Π1, . . . ,ΠM."
