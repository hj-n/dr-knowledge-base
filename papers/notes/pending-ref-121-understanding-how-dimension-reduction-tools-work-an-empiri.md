---
id: paper-2021-pending-ref-121
title: "Understanding How Dimension Reduction Tools Work: An Empirical Approach to Deciphering t-SNE, UMAP, TriMap, and PaCMAP for Data Visualization"
authors: "Yingfan Wang, Haiyang Huang, Cynthia Rudin, and Yaron Shaposhnik"
venue: "UNKNOWN"
year: 2021
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-121-2021-understanding-how-dimension-reduction-tools-work-an-empirical-approach-to-deciphering.pdf
seed_note_id: "paper-2025-stop-misusing-tsne-umap"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- The speciﬁc choices of which observations are attracted and repulsed are complicated, but at its core, the loss governs the balance between attraction and repulsion; each algorithm aims to preserve the structure of the high-dimensional graph and reduce the crowding problem in diﬀerent ways.
- Intuitively,σi is used to normalize the distances between every observation and its neighbors to preserve the relative high-dimensional proximities. (d) Deﬁne the weight function w(xi, xj) def= exp (− max{0,Distancei,j−ρi} σi ) . (e) Deﬁne a weighted graphG whose vertices are observations and where for each edge (i,j ) it holds that xi is a nearest neighbor of xj, or vice versa.
- In addition, SNE requires a careful choice of hyperparameters and initialization. t-SNE and its variants: Building on SNE, t-Distributed Stochastic Neighbor Embedding (t-SNE) (van der Maaten and Hinton, 2008) successfully handled the crowding problem by substituting the Gaussian distribution, used in the low-dimensional space, with long-tailed t-distributions.
- While there is no single deﬁnition of what it means to preserve local or global structure, local structure methods aim mainly to preserve the set of high-dimensional neighbors for each point when reducing to lower dimensions, as well as the relative distances or rank information among neighbors (namely, which points are closer than which other points).

# Method Summary
- Triplet constraint methods: Triplet constraint methods learn a low-dimensional embedding from triplets of points, with comparisons between points in the form of “ a is more similar to b than to c .” Approaches using triplets include DrLIM (Hadsell et al., 2006), t-STE (van der Maaten and Weinberger, 2012), SNaCK (Wilber et al., 2015) and TriMap (Amid and Warmuth, 2019).
- In this work, our main goal is to understand what aspects of DR methods are important for preserving both local and global structure: it is diﬃcult to design a better method without a true understanding of the choices we make in our algorithms and their empirical impact on the low-dimensional embeddings they produce.
- Intuitively, the algorithm tries to ﬁnd an embedding that preserves the ordering of distances within a subset of triplets that mostly consist of a k-nearest neighbor and a further observation with respect to a focal observation, and a few additional randomized triplets which consist of two non-neighbors.
- 4.1 A uniﬁed DR objective All of the algorithms for DR that we discuss can be viewed as graph-based algorithms where a weighted graph is initially constructed based on the high-dimensional data (in particular, the distances in the high-dimension).
- 5 W ang, Huang, Rudin, and Shaposhnik More broadly, data embedding methods, which are often concerned with reducing the dimension of data to more than 3 dimensions, could also be used for visualization if restricted to 2 to 3 dimensions.
- While embedding is conceptually similar to DR, embedding methods do not tend to produce accurate visualizations and struggle to simultaneously preserve global and local structure (and are not designed to do so).
- 3. t-SNE, UMAP, TriMap, and PaCMAP For completeness, we review the algorithms t-SNE, UMAP, TriMap in common notation in Sections 3.1, 3.2, and 3.3; readers familiar with these methods can skip these subsections.

# When To Use / Not Use
- Use when:
  - Intuitively,σi is used to normalize the distances between every observation and its neighbors to preserve the relative high-dimensional proximities. (d) Deﬁne the weight function w(xi, xj) def= exp (− max{0,Distancei,j−ρi} σi ) . (e) Deﬁne a weighted graphG whose vertices are observations and where for each edge (i,j ) it holds that xi is a nearest neighbor of xj, or vice versa.
  - In addition, SNE requires a careful choice of hyperparameters and initialization. t-SNE and its variants: Building on SNE, t-Distributed Stochastic Neighbor Embedding (t-SNE) (van der Maaten and Hinton, 2008) successfully handled the crowding problem by substituting the Gaussian distribution, used in the low-dimensional space, with long-tailed t-distributions.
- Avoid when:
  - Nevertheless, researchers in the single-cell transcriptomic community have been applying force-directed graph visualization algorithms, such as ForceAtlas2, on k-Nearest Neighbor graphs constructed on transcriptomic data, because they have found that these algorithms are sometimes useful for discovering developmental patterns over time (B¨ ohm et al., 2020).
  - These approaches were largely unsuccessful because distances in high-dimensional spaces tend to concentrate, and tend to be almost identical, so that preservation of raw distances did not always lead to preservation of neighborhood structure (i.e., points that are neighbors of each other in high dimensions are not always neighbors in low dimensions).
- Failure modes:
  - The idea of using triplets to maintain structure is appealing: one would think that preserving triplets would be an excellent way to maintain global structure, which is potentially why there have been so many attempts to use triplets despite the fact that they had not been working before TriMap.

# Metrics Mentioned
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- In addition, SNE requires a careful choice of hyperparameters and initialization. t-SNE and its variants: Building on SNE, t-Distributed Stochastic Neighbor Embedding (t-SNE) (van der Maaten and Hinton, 2008) successfully handled the crowding problem by substituting the Gaussian distribution, used in the low-dimensional space, with long-tailed t-distributions.
- Optimization method: apply full batch gradient descent with momentum using the delta-bar-delta method (400 iterations with the value of momentum parameter equal to 0.5 during the ﬁrst 250 iterations and 0.8 thereafter).
- 9 W ang, Huang, Rudin, and Shaposhnik The hyperparameters a and b are tuned using the data by ﬁtting the function ( 1 +a ( ∥yi− yj∥2 2 )b)−1 to the non-normalized weight function exp (− max{0, Distancei,j−ρi}) with the goal of creating a smooth approximation.
- Graph layout optimization (a) Initialization: initialize Y using spectral embedding. (b) Iterate over the graph edges in G, applying gradient descent steps on observation i on every edge (i,j ) as follows: i.
- However, just like many DR algorithm, ForceAtlas2 is not robust to hyperparameter choices and will require careful hyperparameter tuning to achieve optimal results.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-121-C1 | stance: support | summary: The speciﬁc choices of which observations are attracted and repulsed are complicated, but at its core, the loss governs the balance between attraction and repulsion; each algorithm aims to preserve the structure of the high-dimensional graph and reduce the crowding problem in diﬀerent ways. | evidence_ids: PENDING-REF-121-E1, PENDING-REF-121-E2
- CLAIM-PENDING-REF-121-C2 | stance: support | summary: Triplet constraint methods: Triplet constraint methods learn a low-dimensional embedding from triplets of points, with comparisons between points in the form of “ a is more similar to b than to c .” Approaches using triplets include DrLIM (Hadsell et al., 2006), t-STE (van der Maaten and Weinberger, 2012), SNaCK (Wilber et al., 2015) and TriMap (Amid and Warmuth, 2019). | evidence_ids: PENDING-REF-121-E3, PENDING-REF-121-E4
- CLAIM-PENDING-REF-121-C3 | stance: support | summary: In addition, SNE requires a careful choice of hyperparameters and initialization. t-SNE and its variants: Building on SNE, t-Distributed Stochastic Neighbor Embedding (t-SNE) (van der Maaten and Hinton, 2008) successfully handled the crowding problem by substituting the Gaussian distribution, used in the low-dimensional space, with long-tailed t-distributions. | evidence_ids: PENDING-REF-121-E5, PENDING-REF-121-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 4 | relevance: high | note: contains initialization sensitivity or control-policy evidence

# Evidence
- PENDING-REF-121-E1 | page: 14, section: extracted, quote: "The speciﬁc choices of which observations are attracted and repulsed are complicated, but at its core, the loss governs the balance between attraction and repulsion; each algorithm aims to preserve the structure of the high-dimensional graph and reduce the crowding problem in diﬀerent ways."
- PENDING-REF-121-E2 | page: 9, section: extracted, quote: "Intuitively,σi is used to normalize the distances between every observation and its neighbors to preserve the relative high-dimensional proximities. (d) Deﬁne the weight function w(xi, xj) def= exp (− max{0,Distancei,j−ρi} σi ) . (e) Deﬁne a weighted graphG whose vertices are observations and where for each edge (i,j ) it holds that xi is a nearest neighbor of xj, or vice versa."
- PENDING-REF-121-E3 | page: 6, section: extracted, quote: "In addition, SNE requires a careful choice of hyperparameters and initialization. t-SNE and its variants: Building on SNE, t-Distributed Stochastic Neighbor Embedding (t-SNE) (van der Maaten and Hinton, 2008) successfully handled the crowding problem by substituting the Gaussian distribution, used in the low-dimensional space, with long-tailed t-distributions."
- PENDING-REF-121-E4 | page: 4, section: extracted, quote: "While there is no single deﬁnition of what it means to preserve local or global structure, local structure methods aim mainly to preserve the set of high-dimensional neighbors for each point when reducing to lower dimensions, as well as the relative distances or rank information among neighbors (namely, which points are closer than which other points)."
- PENDING-REF-121-E5 | page: 7, section: extracted, quote: "Triplet constraint methods: Triplet constraint methods learn a low-dimensional embedding from triplets of points, with comparisons between points in the form of “ a is more similar to b than to c .” Approaches using triplets include DrLIM (Hadsell et al., 2006), t-STE (van der Maaten and Weinberger, 2012), SNaCK (Wilber et al., 2015) and TriMap (Amid and Warmuth, 2019)."
- PENDING-REF-121-E6 | page: 1, section: extracted, quote: "In this work, our main goal is to understand what aspects of DR methods are important for preserving both local and global structure: it is diﬃcult to design a better method without a true understanding of the choices we make in our algorithms and their empirical impact on the low-dimensional embeddings they produce."
- PENDING-REF-121-E7 | page: 11, section: extracted, quote: "Intuitively, the algorithm tries to ﬁnd an embedding that preserves the ordering of distances within a subset of triplets that mostly consist of a k-nearest neighbor and a further observation with respect to a focal observation, and a few additional randomized triplets which consist of two non-neighbors."
- PENDING-REF-121-E8 | page: 13, section: extracted, quote: "4.1 A uniﬁed DR objective All of the algorithms for DR that we discuss can be viewed as graph-based algorithms where a weighted graph is initially constructed based on the high-dimensional data (in particular, the distances in the high-dimension)."
