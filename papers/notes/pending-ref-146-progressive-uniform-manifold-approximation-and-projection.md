---
id: paper-2020-pending-ref-146
title: "Progressive Uniform Manifold Approximation and Projection"
authors: "Hyung-Kwon Ko, Jaemin Jo, and Jinwook Seo"
venue: "Nature Reviews Methods Primers"
year: 2020
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-146-2020-progressive-uniform-manifold-approximation-and-projection.pdf
seed_note_id: "paper-2025-stop-misusing-tsne-umap"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- UMAP has several important hyperparameters: k (the number of neighbors to consider), min_dist (the minimum distance between points in the low-dimensional space) and metric (a metric to compute the distance between points in the high-dimensional space).
- In our experiment with the Fashion MNIST dataset, we found that Progressive UMAP could generate the ﬁrst approximate projection within a few seconds while also sufﬁciently capturing the important structures of the high-dimensional dataset.
- To tackle this problem, we improve the sequential computations in UMAP by making them progressive, which allows people to incrementally append a batch of data points into the projection at the desired pace.
- Graph Construction: UMAP starts by generating a weighted k-nearest neighbor graph that describes the distances between data points in the high-dimensional space.

# Method Summary
- Marai Short Paper Progressive Uniform Manifold Approximation and Projection Hyung-Kwon Ko, Jaemin Jo, and Jinwook Seo† Seoul National University Abstract We present a progressive algorithm for the Uniform Manifold Approximation and Projection (UMAP), called the Progressive UMAP .
- Abstract We present a progressive algorithm for the Uniform Manifold Approximation and Projection (UMAP), called the Progressive UMAP .
- Conclusion and Future Work We present a progressive algorithm for the Uniform Manifold Approximation and Projection (Progressive UMAP).
- To address this issue, we present a progressive algorithm for UMAP (Progressive UMAP). † Correspondence: jseo@snu.ac.kr After brieﬂy introducing UMAP in Section 3, we identify a number of sequential computations in UMAP and explain how we improve each one by making it ( Section 4).
- In this section, we elaborate on our novel algorithm, Progressive UMAP (Algorithm 1 ), which allows users to feed small batches of data points into UMAP incrementally to obtain the desired latency between intermediate projection outputs.
- However, applying the objective function directly to both algorithms induces bias since the total numbers of edges in UMAP and Progressive UMAP are different when data points are being inserted progressively in Progressive UMAP.
- Evaluation and Discussion To measure the loss of our method and UMAP at run-time we employ the objective function suggested by Tang et al. [TQW ∗15 ].

# When To Use / Not Use
- Use when:
  - Progressive UMAP We found that the current implementation of UMAP [MHM18] could suffer a long initial delay depending on the size of the dataset, because it only works on a ﬁxed set of data points with no support for adding new points progressively.
  - Although performance benchmarks [MHM18] demonstrated that UMAP is much faster than t-SNE, it still is too slow to be used in interactive analysis effectively; when tested on a Macbook Pro with a 3.1 GHz Intel Core i7 and 8GB of RAM, UMAP took about 87 seconds to project the MNIST dataset onto a 2D space, far exceeding the time window of 10 seconds needed to keep the user’s attention [ Mil68, Shn84].
- Avoid when:
  - Kim et al. [ KCL∗17] introduced a per-iteration visualization environment in which users can interact in real time with algorithms that require complex computation, such as multidimensional scaling, t-SNE and latent Dirichlet allocation.
  - In this section, we elaborate on our novel algorithm, Progressive UMAP (Algorithm 1 ), which allows users to feed small batches of data points into UMAP incrementally to obtain the desired latency between intermediate projection outputs.
- Failure modes:
  - For the evaluation, we ran both UMAP and Progressive UMAP on the Fashion MNIST dataset [XRV17 ] which has 70,000 rows of 784 dimensions (28 × 28), each row describing an item from 10 classes (e.g., t-shirt, trouser, etc.).

# Metrics Mentioned
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- UMAP has several important hyperparameters: k (the number of neighbors to consider), min_dist (the minimum distance between points in the low-dimensional space) and metric (a metric to compute the distance between points in the high-dimensional space).
- PANENE accepts a parameter called ops that indicates the allowed number of tasks per iteration that can be controlled to ﬁnd the balance between latency and accuracy.
- The problem compounds as users often have to run the algorithm several times to tune its hyperparameters.
- Although UMAP produced a smaller average loss at the end of iterations, Progressive UMAP could project the data points in a reasonable time-bound, sufﬁciently capturing the characteristics of the data. the original UMAP algorithm and transform them into progressive procedures.
- Kim et al. [ KCL∗17] introduced a per-iteration visualization environment in which users can interact in real time with algorithms that require complex computation, such as multidimensional scaling, t-SNE and latent Dirichlet allocation.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-146-C1 | stance: support | summary: UMAP has several important hyperparameters: k (the number of neighbors to consider), min_dist (the minimum distance between points in the low-dimensional space) and metric (a metric to compute the distance between points in the high-dimensional space). | evidence_ids: PENDING-REF-146-E1, PENDING-REF-146-E2
- CLAIM-PENDING-REF-146-C2 | stance: support | summary: Marai Short Paper Progressive Uniform Manifold Approximation and Projection Hyung-Kwon Ko, Jaemin Jo, and Jinwook Seo† Seoul National University Abstract We present a progressive algorithm for the Uniform Manifold Approximation and Projection (UMAP), called the Progressive UMAP . | evidence_ids: PENDING-REF-146-E3, PENDING-REF-146-E4
- CLAIM-PENDING-REF-146-C3 | stance: support | summary: UMAP has several important hyperparameters: k (the number of neighbors to consider), min_dist (the minimum distance between points in the low-dimensional space) and metric (a metric to compute the distance between points in the high-dimensional space). | evidence_ids: PENDING-REF-146-E5, PENDING-REF-146-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 4 | relevance: high | note: contains initialization sensitivity or control-policy evidence

# Evidence
- PENDING-REF-146-E1 | page: 4, section: extracted, quote: "UMAP has several important hyperparameters: k (the number of neighbors to consider), min_dist (the minimum distance between points in the low-dimensional space) and metric (a metric to compute the distance between points in the high-dimensional space)."
- PENDING-REF-146-E2 | page: 1, section: extracted, quote: "In our experiment with the Fashion MNIST dataset, we found that Progressive UMAP could generate the ﬁrst approximate projection within a few seconds while also sufﬁciently capturing the important structures of the high-dimensional dataset."
- PENDING-REF-146-E3 | page: 1, section: extracted, quote: "To tackle this problem, we improve the sequential computations in UMAP by making them progressive, which allows people to incrementally append a batch of data points into the projection at the desired pace."
- PENDING-REF-146-E4 | page: 2, section: extracted, quote: "Graph Construction: UMAP starts by generating a weighted k-nearest neighbor graph that describes the distances between data points in the high-dimensional space."
- PENDING-REF-146-E5 | page: 1, section: extracted, quote: "Marai Short Paper Progressive Uniform Manifold Approximation and Projection Hyung-Kwon Ko, Jaemin Jo, and Jinwook Seo† Seoul National University Abstract We present a progressive algorithm for the Uniform Manifold Approximation and Projection (UMAP), called the Progressive UMAP ."
- PENDING-REF-146-E6 | page: 1, section: extracted, quote: "Abstract We present a progressive algorithm for the Uniform Manifold Approximation and Projection (UMAP), called the Progressive UMAP ."
- PENDING-REF-146-E7 | page: 4, section: extracted, quote: "Conclusion and Future Work We present a progressive algorithm for the Uniform Manifold Approximation and Projection (Progressive UMAP)."
- PENDING-REF-146-E8 | page: 1, section: extracted, quote: "To address this issue, we present a progressive algorithm for UMAP (Progressive UMAP). † Correspondence: jseo@snu.ac.kr After brieﬂy introducing UMAP in Section 3, we identify a number of sequential computations in UMAP and explain how we improve each one by making it ( Section 4)."
