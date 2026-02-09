---
id: paper-2023-zadu-ref-15
title: "Feature Learning for Nonlinear Dimensionality Reduction toward Maximal Extraction of Hidden Patterns"
authors: "Takanori Fujiwara, Yun-Hsin Kuo, Anders Ynnerman, Kwan-Liu Ma"
venue: "2023 IEEE 16th Pacific Visualization Symposium (PacificVis)"
year: 2023
tags: [dr, zadu-table1-reference, nd, pr, proc, snc, srho]
source_pdf: papers/raw/zadu-table1-references/ref10_feature_learning_for_nonlinear_dimensionality_reduction_toward_maximal_extraction_of_hid.pdf
evidence_level: medium
updated_at: 2026-02-08
---
# Problem
- Feature Learning for Nonlinear Dimensionality Reduction toward Maximal Extraction of Hidden Patterns Takanori Fujiwara* Link¨oping University Yun-Hsin Kuo† University of California, Davis Anders Ynnerman* Link¨oping University Kwan-Liu Ma† University of California, Davis ABSTRACT Dimensionality reduction (DR) plays a vital role in the visual analysis of high-dimensional data.
- 4.1 Problem Scope FEALM aims to supplement nonlinear DR methods, even more speciﬁcally, for those construct agraph-based data representation as their intermediate product or those generate DR results highly related to a graph-based data representation.
- 8-c (left), large weights are assigned to CC20.440b (racial problems), CC20.443.1, CC20.443.2, and CC20.443.5 (legislature’s money use on welfare, healthcare, and transportation/infrastructure, respectively).
- However, as orthogonality between each learned feature is not guaranteed, distance-related functions (e.g., k-NN graph construction using the Euclidean distance) might be heavily inﬂuenced by the distortion.
- By interactively changing the point size based on each of these attributes, we observe that CC20.440b (racial problems) and CC20.443.2 (healthcare) closely associate with the separation between Dem and Rep.

# Method Summary
- We develop an algorithm utilizing the Nelder-Mead optimization method (NMM) [13] to ﬁnd latent features to produce maximally different nearest-neighbor graphs, which are intermediate products of UMAP, and consequently generate diverse UMAP results.
- When compared with other derivative-free solvers such as the particle-swarm optimization [21], the NMM does not involve many evaluations of the objective function, and efﬁciently ﬁnds a reasonable solution [48].
- However, our work is for the use with nonlinear DR methods and provides optimization and visualization methods to ﬁnd appropriate linear subspaces, which are not limited to axis-parallel subspaces.
- This paper presents a feature learning framework, FEALM, designed to generate a set of optimized data projections for nonlinear DR in order to capture important patterns in the hidden manifolds.
- Note that the patterns uncovered in the case studies are difﬁcult to identify with the aforesaid optimization method by Lehmann and Theisel [24] or attribute selection (refer to [1]).
- As in other ML methods, currently, we recommend manually searching appropriate values based on the observed results (e.g., the quality of optimization in Sec.
- To achieve such a capability, we design an optimization algorithm as well as introduce a new graph dissimilarity measure, named neighbor-shape dissimilarity.

# When To Use / Not Use
- Use when:
  - For example, PCA and LDA are frequently used in data preprocessing for subsequent machine learning (ML) methods, such as deep neural networks or even other DR methods (e.g., t-SNE), as reducing dimensions is helpful to avoid high computational costs and the curse of dimensionality.
  - Using negative λ1 is especially effective when we want to avoid generating dissimilar graphs, Gi (or dissimilar DR results, Yi), that can be derived from a selection of few attributes (e.g., when analyzing binary or ordinal data).
  - Since NetLSD involves an exponential function when computing the dissimilarity (refer to [39]), we take a logarithm of 1 + dSD (1 is added to avoid taking a logarithm of 0) to avoid excessive inﬂuence from the shape difference.
- Avoid when:
  - The above examples demonstrate that nonlinear DR can easily overlook important, obvious data patterns when certain attributes inﬂuence intrinsic manifolds—even a single attribute can cause this situation.
  - We chose UMAP because it is computationally rather efﬁcient (e.g., when compared with t-SNE) [28] and frequently used for visualization in various applications [7, 11, 22].
- Failure modes:
  - Thus, when computing the best solution with the NMM, the cost calculation for each solution takes O(rn(q2 + kn)), where r is the number of produced graphs so far.
  - However, even nonlinear DR easily fails to ﬁnd important patterns when some attributes affect manifolds that contain the corresponding patterns.

# Metrics Mentioned
- `nh`: label-based neighborhood hit.
- `nd`: neighbor-shape dissimilarity or neighbor distortion.
- `pr`: pairwise-distance correlation behavior.
- `srho`: rank-correlation of pairwise distances.
- `snc`: Steadiness/Cohesiveness inter-cluster reliability.
- `topo`: topology-related structure behavior.
- `proc`: Procrustes local shape agreement.

# Implementation Notes
- Then, we deﬁne the dissimilarity measured by NSD as: dNSD(Gi,G j) = dND(Gi,G j)β· log ( 1 + dSD(Gi,G j) ) (4) where dNSD(Gi,G j)≥ 0 and β (0≤ β≤ ∞) is a hyperparameter that controls how strongly NSD focuses on the neighbor dissimilarity vs. the shape dissimilarity.
- Also, hyperparameter adjustments of UMAP, such ask used for the k-nearest neighbor (k-NN) graph construction, cannot solve this issue as the manifold itself is distorted (for details, refer to [1]).
- The remaining hyperparameters that need to be adjusted are m′, λ1, and λ2 (the number of latent features in a projection matrix and the weights for L1 and L2 norm-based regularizations).
- 2 to recommend sets of graph-related hyperparameters of DR (e.g., the number of neighbors in UMAP), which produce signiﬁcantly different DR results [4].
- With fDR, a function that performs DR with a given method and hyperparameters, we can obtain a DR result or representation, Yi, i.e., Yi= fDR(XPi).
- In addition to the projection constraint, FEALM-UMAP has several hyperparameters, m′, λ1, λ2, q, β, r, which can also inﬂuence the DR results.
- Keep preprocessing, initialization policy, and random-seed protocol fixed when comparing methods.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PAPER2023ZADUREF15-C1 | stance: support | summary: Feature Learning for Nonlinear Dimensionality Reduction toward Maximal Extraction of Hidden Patterns Takanori Fujiwara* Link¨oping University Yun-Hsin Kuo† University of California, Davis Anders Ynnerman* Link¨oping University Kwan-Liu Ma† University of California, Davis ABSTRACT Dimensionality reduction (DR) plays a vital role in the visual analysis of high-dimensional data. | evidence_ids: PAPER2023ZADUREF15-E1, PAPER2023ZADUREF15-E2
- CLAIM-PAPER2023ZADUREF15-C2 | stance: support | summary: We develop an algorithm utilizing the Nelder-Mead optimization method (NMM) [13] to ﬁnd latent features to produce maximally different nearest-neighbor graphs, which are intermediate products of UMAP, and consequently generate diverse UMAP results. | evidence_ids: PAPER2023ZADUREF15-E3, PAPER2023ZADUREF15-E4
- CLAIM-PAPER2023ZADUREF15-C3 | stance: support | summary: Then, we deﬁne the dissimilarity measured by NSD as: dNSD(Gi,G j) = dND(Gi,G j)β· log ( 1 + dSD(Gi,G j) ) (4) where dNSD(Gi,G j)≥ 0 and β (0≤ β≤ ∞) is a hyperparameter that controls how strongly NSD focuses on the neighbor dissimilarity vs. the shape dissimilarity. | evidence_ids: PAPER2023ZADUREF15-E5, PAPER2023ZADUREF15-E6
- CLAIM-METRIC-ND-SOURCE-15 | stance: support | summary: This source includes evidence relevant to `nd` in dimensionality-reduction reliability evaluation. | evidence_ids: PAPER2023ZADUREF15-E1, PAPER2023ZADUREF15-E2
- CLAIM-METRIC-PR-SOURCE-15 | stance: support | summary: This source includes evidence relevant to `pr` in dimensionality-reduction reliability evaluation. | evidence_ids: PAPER2023ZADUREF15-E1, PAPER2023ZADUREF15-E2
- CLAIM-METRIC-PROC-SOURCE-15 | stance: support | summary: This source includes evidence relevant to `proc` in dimensionality-reduction reliability evaluation. | evidence_ids: PAPER2023ZADUREF15-E1, PAPER2023ZADUREF15-E2
- CLAIM-METRIC-SNC-SOURCE-15 | stance: support | summary: This source includes evidence relevant to `snc` in dimensionality-reduction reliability evaluation. | evidence_ids: PAPER2023ZADUREF15-E1, PAPER2023ZADUREF15-E2
- CLAIM-METRIC-SRHO-SOURCE-15 | stance: support | summary: This source includes evidence relevant to `srho` in dimensionality-reduction reliability evaluation. | evidence_ids: PAPER2023ZADUREF15-E1, PAPER2023ZADUREF15-E2

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports task clarification before model selection
- step: 2 | relevance: medium | note: adds constraints for preprocessing and data-audit checks
- step: 3 | relevance: high | note: directly informs task-aligned technique/metric selection
- step: 5 | relevance: medium | note: adds initialization sensitivity guidance
- step: 6 | relevance: high | note: adds hyperparameter sensitivity or optimization guidance

# Evidence
- PAPER2023ZADUREF15-E1 | page: 1, section: extracted, quote: "Feature Learning for Nonlinear Dimensionality Reduction toward Maximal Extraction of Hidden Patterns Takanori Fujiwara* Link¨oping University Yun-Hsin Kuo† University of California, Davis Anders Ynnerman* Link¨oping University Kwan-Liu Ma† University of California, Davis ABSTRACT Dimensionality reduction (DR) plays a vital role in the visual analysis of high-dimensional data."
- PAPER2023ZADUREF15-E2 | page: 3, section: extracted, quote: "4.1 Problem Scope FEALM aims to supplement nonlinear DR methods, even more speciﬁcally, for those construct agraph-based data representation as their intermediate product or those generate DR results highly related to a graph-based data representation."
- PAPER2023ZADUREF15-E3 | page: 9, section: extracted, quote: "8-c (left), large weights are assigned to CC20.440b (racial problems), CC20.443.1, CC20.443.2, and CC20.443.5 (legislature’s money use on welfare, healthcare, and transportation/infrastructure, respectively)."
- PAPER2023ZADUREF15-E4 | page: 4, section: extracted, quote: "However, as orthogonality between each learned feature is not guaranteed, distance-related functions (e.g., k-NN graph construction using the Euclidean distance) might be heavily inﬂuenced by the distortion."
- PAPER2023ZADUREF15-E5 | page: 9, section: extracted, quote: "By interactively changing the point size based on each of these attributes, we observe that CC20.440b (racial problems) and CC20.443.2 (healthcare) closely associate with the separation between Dem and Rep."
- PAPER2023ZADUREF15-E6 | page: 2, section: extracted, quote: "2.3 Exploration of Linear Subspaces To show high-dimensional data distributions in a selected 2D linear subspace, scatterplots and star coordinates are often used with interactive enhancements [26, 44]."
- PAPER2023ZADUREF15-E7 | page: 1, section: extracted, quote: "We develop an algorithm utilizing the Nelder-Mead optimization method (NMM) [13] to ﬁnd latent features to produce maximally different nearest-neighbor graphs, which are intermediate products of UMAP, and consequently generate diverse UMAP results."
- PAPER2023ZADUREF15-E8 | page: 6, section: extracted, quote: "When compared with other derivative-free solvers such as the particle-swarm optimization [21], the NMM does not involve many evaluations of the objective function, and efﬁciently ﬁnds a reasonable solution [48]."
- PAPER2023ZADUREF15-E9 | page: 2, section: extracted, quote: "However, our work is for the use with nonlinear DR methods and provides optimization and visualization methods to ﬁnd appropriate linear subspaces, which are not limited to axis-parallel subspaces."
- PAPER2023ZADUREF15-E10 | page: 1, section: extracted, quote: "This paper presents a feature learning framework, FEALM, designed to generate a set of optimized data projections for nonlinear DR in order to capture important patterns in the hidden manifolds."
- PAPER2023ZADUREF15-E11 | page: 8, section: extracted, quote: "Note that the patterns uncovered in the case studies are difﬁcult to identify with the aforesaid optimization method by Lehmann and Theisel [24] or attribute selection (refer to [1])."
- PAPER2023ZADUREF15-E12 | page: 9, section: extracted, quote: "As in other ML methods, currently, we recommend manually searching appropriate values based on the observed results (e.g., the quality of optimization in Sec."
- PAPER2023ZADUREF15-E13 | page: 2, section: extracted, quote: "Despite the frequent use of the aforementioned DR methods for visual analytics [34], they may fail to show important patterns when data contains noises or inﬂuential attributes to the overall data distribution."
- PAPER2023ZADUREF15-E14 | page: 3, section: extracted, quote: "Figure 1: Three datasets (a,d,g) and corresponding DR results: PCA (b) and UMAP (c,e,f,h,i). larly, by assigning a large weight only to the 3-class attribute, DR can ﬁnd Classes A–C."
