---
id: paper-2022-pending-ref-009
title: "Uniform manifold approximation with two-phase optimization"
authors: "H. Jeon, H.-K. Ko, S. Lee, J. Jo, and J. Seo"
venue: "2022 IEEE Visualization and Visual Analytics (VIS)"
year: 2022
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-009-2022-uniform-manifold-approximation-with-two-phase-optimization.pdf
seed_note_id: "paper-2023-zadu-library"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- UMATO avoids this problem by separating hubs and non-hub points; the hubs take their position in the ﬁrst phase and barely move but guide other points in the second phase so that the global structure can be preserved robustly.
- UMAP avoids such a problem by employing the cross-entropy function as a loss function.

# Method Summary
- The shape of embeddings also supports such a Global quality metrics Local quality metrics ( k = 5) Dataset Algorithm DTM 0.01 DTM0.1 DTM1 KL0.01 KL0.1 KL1 Conti.
- 6 C ONCLUSION We present a two-phase DR algorithm called UMATO that can effectively preserve the global and local properties of HD data.
- Moreover, this procedure makes the embedding more stable and less sensitive to initialization methods.
- Considering negative sampling, the modiﬁed objective function is: O = ∑ (i, j)∈E vi j(log(wi j) + M ∑ k=1 E jk∼Pn( j)γ log(1− wi jk )). (7) Here, vi j and wi j are the similarities in the high and low-dimensional spaces, respectively, and γ is a weight constant to apply to negative samples.
- For example, in the case of t-SNE, inaccuracy in preserving the global structure comes from the fact that its loss function, Kullback-Leibler (KL) divergence, assigns too little penalty for the points that are distant in the original space and stay close in the embedding space [26].
- In the case of local metrics, we used mean relative rank errors (MRREs [20]) and Trustworthiness & Continuity (T&C [36]), which quantiﬁes the quality of embedding based on the preservation of neighborhood structure.
- Although the same approximation techniques as UMAP are used for these points, the embedding becomes more accurate in preserving the global structure because we use already embedded hub points as anchors.

# When To Use / Not Use
- Use when:
  - UMATO avoids this problem by separating hubs and non-hub points; the hubs take their position in the ﬁrst phase and barely move but guide other points in the second phase so that the global structure can be preserved robustly.
  - 2 B ACKGROUND AND RELATED WORKS 2.1 UMAP Because UMATO shares the overall pipeline of UMAP, we provide a brief introduction to UMAP.
- Avoid when:
  - For a synthetic dataset, we used Spheres [28]; it consists of 11 101-dimensional spheres, where ten spheres with relatively small radius of 5 and the number of points of 500 are enclosed by a larger sphere with a radius of 25 and the number of 5,000.
  - In our experiments with diverse datasets, we have proven that UMATO outperforms previous widely used baselines (e.g.,t-SNE and UMAP) in capturing global structures while showing competitive performance in preserving local structures.
- Failure modes:
  - In the case of local metrics, we used mean relative rank errors (MRREs [20]) and Trustworthiness & Continuity (T&C [36]), which quantiﬁes the quality of embedding based on the preservation of neighborhood structure.

# Metrics Mentioned
- `trustworthiness`: referenced as part of projection-quality or reliability assessment.
- `continuity`: referenced as part of projection-quality or reliability assessment.
- `kl divergence`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- They require a hyperparameterk, the number of nearest neighbors; we used k = 5 throughout our experiments, aligned with the experiment of TopoAE [28].
- The hyperparameters of the DR algorithms are chosen to minimizeKL0.1.
- The hyperparameters of the techniques are set to minimize KL 0.1.
- 3 Sungkyunkwan University ABSTRACT We introduce Uniform Manifold Approximation with Two-phase Optimization (UMATO), a dimensionality reduction (DR) technique that improves UMAP to capture the global structure of highdimensional data more accurately.
- Uniform Manifold Approximation with Two-phase Optimization Hyeon Jeon 1 * † Hyung-Kwon Ko 2∗ ‡ Soohyun Lee 1 § Jaemin Jo 3 ¶ Jinwook Seo 1 || 1 Seoul National University 2 NAVER Webtoon Corp.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-009-C1 | stance: support | summary: UMATO avoids this problem by separating hubs and non-hub points; the hubs take their position in the ﬁrst phase and barely move but guide other points in the second phase so that the global structure can be preserved robustly. | evidence_ids: PENDING-REF-009-E1, PENDING-REF-009-E2
- CLAIM-PENDING-REF-009-C2 | stance: support | summary: The shape of embeddings also supports such a Global quality metrics Local quality metrics ( k = 5) Dataset Algorithm DTM 0.01 DTM0.1 DTM1 KL0.01 KL0.1 KL1 Conti. | evidence_ids: PENDING-REF-009-E3, PENDING-REF-009-E4
- CLAIM-PENDING-REF-009-C3 | stance: support | summary: They require a hyperparameterk, the number of nearest neighbors; we used k = 5 throughout our experiments, aligned with the experiment of TopoAE [28]. | evidence_ids: PENDING-REF-009-E5, PENDING-REF-009-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 4 | relevance: high | note: contains initialization sensitivity or control-policy evidence

# Evidence
- PENDING-REF-009-E1 | page: 2, section: extracted, quote: "UMATO avoids this problem by separating hubs and non-hub points; the hubs take their position in the ﬁrst phase and barely move but guide other points in the second phase so that the global structure can be preserved robustly."
- PENDING-REF-009-E2 | page: 1, section: extracted, quote: "UMAP avoids such a problem by employing the cross-entropy function as a loss function."
- PENDING-REF-009-E3 | page: 1, section: extracted, quote: "The shape of embeddings also supports such a Global quality metrics Local quality metrics ( k = 5) Dataset Algorithm DTM 0.01 DTM0.1 DTM1 KL0.01 KL0.1 KL1 Conti."
- PENDING-REF-009-E4 | page: 4, section: extracted, quote: "6 C ONCLUSION We present a two-phase DR algorithm called UMATO that can effectively preserve the global and local properties of HD data."
- PENDING-REF-009-E5 | page: 1, section: extracted, quote: "Moreover, this procedure makes the embedding more stable and less sensitive to initialization methods."
- PENDING-REF-009-E6 | page: 2, section: extracted, quote: "Considering negative sampling, the modiﬁed objective function is: O = ∑ (i, j)∈E vi j(log(wi j) + M ∑ k=1 E jk∼Pn( j)γ log(1− wi jk )). (7) Here, vi j and wi j are the similarities in the high and low-dimensional spaces, respectively, and γ is a weight constant to apply to negative samples."
- PENDING-REF-009-E7 | page: 1, section: extracted, quote: "For example, in the case of t-SNE, inaccuracy in preserving the global structure comes from the fact that its loss function, Kullback-Leibler (KL) divergence, assigns too little penalty for the points that are distant in the original space and stay close in the embedding space [26]."
- PENDING-REF-009-E8 | page: 3, section: extracted, quote: "In the case of local metrics, we used mean relative rank errors (MRREs [20]) and Trustworthiness & Continuity (T&C [36]), which quantiﬁes the quality of embedding based on the preservation of neighborhood structure."
