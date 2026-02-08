---
id: paper-2020-pending-ref-041
title: "Quantitative evaluation of time-dependent multidimensional projection techniques"
authors: "E. F. V ernier, R. Garcia, I. d. Silva, J. L. D. Comba, and A. C. Telea"
venue: "Computer Graphics Forum"
year: 2020
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-041-2020-quantitative-evaluation-of-time-dependent-multidimensional-projection-techniques.pdf
seed_note_id: "paper-2022-revisiting-dr-visual-cluster-analysis"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- Compared to other high-dimensional data visualization techniques, projections are especially effective for datasets with many observations (also called samples or points) and attributes (also called measurements, dimensions, or variables) [LMW∗17].
- Such a factor jointly minimizes the Kullback-Leibler divergence proposed by t-SNE to preserve high-dimensional point neighborhoods and also restricts the amount of motion ∥P(xt+1)− P(xt )∥ that points can have between consecutive timesteps.
- Covering all variations of high-dimensional datasets with a benchmark is already daunting for static data [EMK∗19], thus even c⃝ 2020 The Author(s) Computer Graphics Forum c⃝ 2020 The Eurographics Association and John Wiley & Sons Ltd.
- Note that this is a harder (and different) problem from the one we aim to study since one cannot anticipate c⃝ 2020 The Author(s) Computer Graphics Forum c⃝ 2020 The Eurographics Association and John Wiley & Sons Ltd.

# Method Summary
- We next describe the selected techniques. t-SNE and variants: Probably the simplest way to project dynamic data is to compute a single, global, projection P(D) for the entire dataset D and next visualize the timeframes by using the desired method, be it animation, trails, or small multiples.
- Understanding dynamic projection behavior The coarse-grained and ﬁne-grained analyses presented so far highlighted that there are signiﬁcant differences in the behavior of dynamic DR methods that depend on both the method and the dataset.
- We present an evaluation of 11 methods, 10 datasets, and 12 quality metrics, and elect the best-suited methods for projecting time-dependent multivariate data, exploring the design choices and characteristics of each method.
- Introduction Dimensionality reduction (DR) methods, also called projections, are used in many applications in information visualization, machine learning, and statistics.
- Evaluations of static dimensionality reduction Taxonomies as the ones listed above, compare DR methods mainly from technical (algorithmic) and task-suitability aspects.
- In this paper, we aim at providing an approach to assess projection techniques for dynamic data and understand the relationship between visual quality and stability.
- The dynamic t-SNE (dt-SNE) method of Rauber et al. [RFT16] extends the well-known t-SNE method [vdMH08] by adding a stability factor λ to the objective function.

# When To Use / Not Use
- Use when:
  - The networks have the same architecture but use different optimizers, batch sizes, and training-set sizes. • quickdraw: Drawing sequences for 600 objects of 6 different classes drawn by random people.
  - Separately, practitioners can use our ﬁndings into the process of determining which dynamic projection technique is best suited to their given user context.
- Avoid when:
  - Autoencoders: Often used in dimensionality reduction and representation learning, autoencoders [HS06, Bal87] are hourglassshaped neural networks.
  - 1 shows the values, for each autoencoder and dataset, that delivered the best results, and which we used next.
- Failure modes:
  - Analysis of (un)stable behavior Beside empirically measuring and observing that different DR techniques have widely different stabilities, it is useful to analyze the causes of these differences, which we do next. t-SNE and UMAP: Our results tell that TF-t-SNE and TF-UMAP, that is, projections computed independently for each timestep, are the most unstable of the assessed techniques.

# Metrics Mentioned
- `trustworthiness`: referenced as part of projection-quality or reliability assessment.
- `continuity`: referenced as part of projection-quality or reliability assessment.
- `stress`: referenced as part of projection-quality or reliability assessment.
- `co-ranking`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- Autoencoders, in contrast, have the ‘usual’ deep learning challenges, most notably ﬁnding the optimal network architecture and hyperparameter values.
- The benchmark can be extended with new methods, a better way to choose hyperparameters, new datasets, and new metrics.
- We also noticed that dtSNE is very sensitive to the choice of hyperparameters.
- This is so since these are stochastic methods that optimize non-convex objective functions using randomly seeded gradient descent.
- In contrast to t-SNE and UMAP, these artifacts are not due to stochastic seeding, but due to the way PCA works.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-041-C1 | stance: support | summary: Compared to other high-dimensional data visualization techniques, projections are especially effective for datasets with many observations (also called samples or points) and attributes (also called measurements, dimensions, or variables) [LMW∗17]. | evidence_ids: PENDING-REF-041-E1, PENDING-REF-041-E2
- CLAIM-PENDING-REF-041-C2 | stance: support | summary: We next describe the selected techniques. t-SNE and variants: Probably the simplest way to project dynamic data is to compute a single, global, projection P(D) for the entire dataset D and next visualize the timeframes by using the desired method, be it animation, trails, or small multiples. | evidence_ids: PENDING-REF-041-E3, PENDING-REF-041-E4
- CLAIM-PENDING-REF-041-C3 | stance: support | summary: Autoencoders, in contrast, have the ‘usual’ deep learning challenges, most notably ﬁnding the optimal network architecture and hyperparameter values. | evidence_ids: PENDING-REF-041-E5, PENDING-REF-041-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 4 | relevance: high | note: contains initialization sensitivity or control-policy evidence

# Evidence
- PENDING-REF-041-E1 | page: 1, section: extracted, quote: "Compared to other high-dimensional data visualization techniques, projections are especially effective for datasets with many observations (also called samples or points) and attributes (also called measurements, dimensions, or variables) [LMW∗17]."
- PENDING-REF-041-E2 | page: 2, section: extracted, quote: "Such a factor jointly minimizes the Kullback-Leibler divergence proposed by t-SNE to preserve high-dimensional point neighborhoods and also restricts the amount of motion ∥P(xt+1)− P(xt )∥ that points can have between consecutive timesteps."
- PENDING-REF-041-E3 | page: 4, section: extracted, quote: "Covering all variations of high-dimensional datasets with a benchmark is already daunting for static data [EMK∗19], thus even c⃝ 2020 The Author(s) Computer Graphics Forum c⃝ 2020 The Eurographics Association and John Wiley & Sons Ltd."
- PENDING-REF-041-E4 | page: 2, section: extracted, quote: "Note that this is a harder (and different) problem from the one we aim to study since one cannot anticipate c⃝ 2020 The Author(s) Computer Graphics Forum c⃝ 2020 The Eurographics Association and John Wiley & Sons Ltd."
- PENDING-REF-041-E5 | page: 3, section: extracted, quote: "We next describe the selected techniques. t-SNE and variants: Probably the simplest way to project dynamic data is to compute a single, global, projection P(D) for the entire dataset D and next visualize the timeframes by using the desired method, be it animation, trails, or small multiples."
- PENDING-REF-041-E6 | page: 9, section: extracted, quote: "Understanding dynamic projection behavior The coarse-grained and ﬁne-grained analyses presented so far highlighted that there are signiﬁcant differences in the behavior of dynamic DR methods that depend on both the method and the dataset."
- PENDING-REF-041-E7 | page: 1, section: extracted, quote: "We present an evaluation of 11 methods, 10 datasets, and 12 quality metrics, and elect the best-suited methods for projecting time-dependent multivariate data, exploring the design choices and characteristics of each method."
- PENDING-REF-041-E8 | page: 1, section: extracted, quote: "Introduction Dimensionality reduction (DR) methods, also called projections, are used in many applications in information visualization, machine learning, and statistics."
