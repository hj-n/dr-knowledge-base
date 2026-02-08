---
id: paper-2020-pending-ref-026
title: "UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction"
authors: "Leland McInnes, John Healy, and James Melville"
venue: "Journal of Open Source Software"
year: 2020
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-026-2020-umap-uniform-manifold-approximation-and-projection-for-dimension-reduction.pdf
seed_note_id: "paper-2021-quantitative-survey-dr-techniques"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- UMAP then optimizes the layout of the data representation in the low dimensional space, to minimize the cross-entropy between the two topological representations. /T_he construction of fuzzy topological representations can be broken down into two problems: approximating a manifold on which the data is assumed to lie; and constructing a fuzzy simplicial set representation of the approximated manifold.
- One of the primary contributions of this paper is to reframe the problem of manifold learning and dimension reduction in a different mathematical language allowing pracitioners to apply a new /f_ield of mathemtaics to the problems.
- Without strong theoretical foundations the only arguments which can be made about algorithms amount to empirical measures, for which there are no clear universal choices for unsupervised problems.

# Method Summary
- In the second phase a low dimensional layout of this graph is computed. /T_he diﬀerences between all algorithms in this class amount to speci/f_ic details in how the graph is constructed and how the layout is computed. /T_he theoretical basis for UMAP as described in Section 2 provides novel approaches to both of these phases, and provides clear motivation for the choices involved.
- C From t-SNE to UMAP As an aid to implementation of UMAP and to illuminate the algorithmic similarities with t-SNE and LargeVis, here we review the main equations used in those methods, and then present the equivalent UMAP expressions in a notation which may be more familiar to users of those other methods.
- In particular the use of approximate nearest neighbor algorithms, and the negative sampling used in optimization, can result in suboptimal embeddings.
- In explaining the algorithm we will /f_irst discuss the method of approximating the manifold for the source data.
- In particular it introduces so called ”reverse-nearestneighbors” into the classical knn-graph. /T_his, combined with the fact that UMAP is preserving topology rather than pure metric structures, mean that UMAP will not perform as well as some methods on quality measures based on metric structure preservation – particularly methods, such as MDS – which are explicitly designed to optimize metric structure preservation.
- We denote the subcategory of /f_inite extended-pseudo-metric spacesFinEPMet. /T_he choice of non-expansive maps in De/f_inition 6 is due to Spivak, but we note that it closely mirrors the work of Carlsson and Memoli in [13] on topological methods for clustering as applied to /f_inite metric spaces. /T_his choice is signi/f_icant since pure isometries are too strict and do not provide large enough Hom-sets.
- Use cases for (semi-)supervised dimension reduction include semi-supervised clustering, and interactive labelling tools. /T_he computational framework established for UMAP allows for the potential development of techniques to add new unseen data points into an 50 existing embedding, and to generate high dimensional representations of arbitrary points in the embedded space.

# When To Use / Not Use
- Use when:
  - Similarities in the high dimensions are eﬀectively zero outside of the nearest neighbors of each point due to the calibration of thepj|i values to reproduce a desired perplexity. /T_herefore an approximation used in Barnes-Hut t-SNE is to only calculatevj|i forn nearest neighbors ofi, wheren is a multiple of the user-selected perplexity and to assumevj|i = 0 for all otherj.
  - Use cases for (semi-)supervised dimension reduction include semi-supervised clustering, and interactive labelling tools. /T_he computational framework established for UMAP allows for the potential development of techniques to add new unseen data points into an 50 existing embedding, and to generate high dimensional representations of arbitrary points in the embedded space.
- Avoid when:
  - By the density theorem and employing a minor abuse of notation we then have colim x∈Xn ∆n ∼=X /T_here is a standard covariant functor| · | : ∆ → Top mapping from the category ∆ to the category of topological spaces that sends [n] to the standardn-simplex |∆n| ⊂ Rn+1 de/f_ined as |∆n| ≜ { (t0,...,t n) ∈ Rn+1 | n∑ i=0 ti = 1,ti ≥ 0 } with the standard subspace topology.
  - Furthermore, the combination of supervision and the addition of new samples to an existing embedding provides avenues for metric learning. /T_he addition of new samples to an existing embedding would allow UMAP to be used as a feature engineering tool as part of a general machine learning pipeline for either clustering or classi/f_ication tasks.
- Failure modes:
  - C From t-SNE to UMAP As an aid to implementation of UMAP and to illuminate the algorithmic similarities with t-SNE and LargeVis, here we review the main equations used in those methods, and then present the equivalent UMAP expressions in a notation which may be more familiar to users of those other methods.

# Metrics Mentioned
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- Given an input hyperparameterk, for eachxi we compute the set{xi1,...,x ik } of thek nearest neighbors ofxi under the metricd. /T_his computation can be performed via any nearest neighbour or approximate nearest neighbour search algorithm.
- A further heuristic algorithm optimization technique employed by tSNE implementations is the use ofearly exaggeration where, for some number of initial iterations, thepij are multiplied by some constant greater than 55 1.0 (usually 12.0).
- UMAP is constructed from a theoretical framework based in Riemannian geometry and algebraic topology. /T_he result is a practical scalable algorithm that is applicable to real world data. /T_he UMAP algorithm is competitive with t-SNE for visualization quality, and arguably preserves more of the global structure with superior run time performance.
- Of note, we still want to incorporate the distance to the nearest neighbor as per the local connectedness requirement. /T_his can be achieved by supplying a parameter that de/f_ines the expected distance between nearest neighbors in the embedded space.
- In Section 4 we discuss implementation details of the UMAP algorithm. /T_his includes a more detailed algorithmic description, and discussion of the hyper-parameters involved and their practical eﬀects.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-026-C1 | stance: support | summary: UMAP then optimizes the layout of the data representation in the low dimensional space, to minimize the cross-entropy between the two topological representations. /T_he construction of fuzzy topological representations can be broken down into two problems: approximating a manifold on which the data is assumed to lie; and constructing a fuzzy simplicial set representation of the approximated manifold. | evidence_ids: PENDING-REF-026-E1, PENDING-REF-026-E2
- CLAIM-PENDING-REF-026-C2 | stance: support | summary: In the second phase a low dimensional layout of this graph is computed. /T_he diﬀerences between all algorithms in this class amount to speci/f_ic details in how the graph is constructed and how the layout is computed. /T_he theoretical basis for UMAP as described in Section 2 provides novel approaches to both of these phases, and provides clear motivation for the choices involved. | evidence_ids: PENDING-REF-026-E3, PENDING-REF-026-E4
- CLAIM-PENDING-REF-026-C3 | stance: support | summary: Given an input hyperparameterk, for eachxi we compute the set{xi1,...,x ik } of thek nearest neighbors ofxi under the metricd. /T_his computation can be performed via any nearest neighbour or approximate nearest neighbour search algorithm. | evidence_ids: PENDING-REF-026-E5, PENDING-REF-026-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 4 | relevance: high | note: contains initialization sensitivity or control-policy evidence

# Evidence
- PENDING-REF-026-E1 | page: 4, section: extracted, quote: "UMAP then optimizes the layout of the data representation in the low dimensional space, to minimize the cross-entropy between the two topological representations. /T_he construction of fuzzy topological representations can be broken down into two problems: approximating a manifold on which the data is assumed to lie; and constructing a fuzzy simplicial set representation of the approximated manifold."
- PENDING-REF-026-E2 | page: 3, section: extracted, quote: "One of the primary contributions of this paper is to reframe the problem of manifold learning and dimension reduction in a different mathematical language allowing pracitioners to apply a new /f_ield of mathemtaics to the problems."
- PENDING-REF-026-E3 | page: 4, section: extracted, quote: "Without strong theoretical foundations the only arguments which can be made about algorithms amount to empirical measures, for which there are no clear universal choices for unsupervised problems."
- PENDING-REF-026-E4 | page: 13, section: extracted, quote: "In the second phase a low dimensional layout of this graph is computed. /T_he diﬀerences between all algorithms in this class amount to speci/f_ic details in how the graph is constructed and how the layout is computed. /T_he theoretical basis for UMAP as described in Section 2 provides novel approaches to both of these phases, and provides clear motivation for the choices involved."
- PENDING-REF-026-E5 | page: 21, section: extracted, quote: "C From t-SNE to UMAP As an aid to implementation of UMAP and to illuminate the algorithmic similarities with t-SNE and LargeVis, here we review the main equations used in those methods, and then present the equivalent UMAP expressions in a notation which may be more familiar to users of those other methods."
- PENDING-REF-026-E6 | page: 16, section: extracted, quote: "In particular the use of approximate nearest neighbor algorithms, and the negative sampling used in optimization, can result in suboptimal embeddings."
- PENDING-REF-026-E7 | page: 4, section: extracted, quote: "In explaining the algorithm we will /f_irst discuss the method of approximating the manifold for the source data."
- PENDING-REF-026-E8 | page: 16, section: extracted, quote: "In particular it introduces so called ”reverse-nearestneighbors” into the classical knn-graph. /T_his, combined with the fact that UMAP is preserving topology rather than pure metric structures, mean that UMAP will not perform as well as some methods on quality measures based on metric structure preservation – particularly methods, such as MDS – which are explicitly designed to optimize metric structure preservation."
