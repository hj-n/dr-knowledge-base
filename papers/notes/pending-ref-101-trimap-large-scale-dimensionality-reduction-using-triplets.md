---
id: paper-2022-pending-ref-101
title: "TriMap: Large-scale Dimensionality Reduction Using Triplets"
authors: "Ehsan Amid and Manfred K. Warmuth"
venue: "UNKNOWN"
year: 2022
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-101-2022-trimap-large-scale-dimensionality-reduction-using-triplets.pdf
seed_note_id: "paper-2025-stop-misusing-tsne-umap"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- The key idea behind TriMap stems from semi-supervised metric learning (Amid et al., 2016): Given an initial lowdimensional representation for the data points, the triplet information from the high-dimensional representation of the points is used to enhance the quality of the embedding.
- Also, UMAP runs out of memory on datasets larger than∼4M points. that is designed to sample the informative triplets from the high-dimensional representation of a set of points and assign weights to these triplets to reﬂect the relative similarities of these points.
- Similarly, TriMap is initialized with the low dimensional PCA embedding and this embedding is then modiﬁed using a set of carefully selected triplets from the high-dimensional representation.
- The aim of DR is to provide a low-dimensional representation (typically in 2D or 3D) of a given high-dimensional dataset that preserves the overall structure of the data as much as possible.

# Method Summary
- To evaluate the local performance, we show the nearest-neighbor accuracy 6Also, the embeddings obtained by simply applying these methods to our set of sampled triplets are quite subpar (see the MNIST result in (Van Der Maaten & Weinberger, 2012)) and are not shown here.
- The triplet embedding methods have been developed for a different setting where the goal is to ﬁnd an embedding based on a given pre-speciﬁed set of triplets obtained from human evaluators (or some form of implicit feedback).
- We deﬁne the Minimum Reconstruction Error (MRE) from the embedding as E(Y| X) := min A∈Rm×d ∥X− AY∥2 F, where∥·∥ F denotes the Frobenius norm.4 Note that PCA has the lowest possible MRE among all the DR methods.
- Finally, note that there exist connections between TriMap and a number oftriplet (aka ordinal) embedding methods such as t-STE (Van Der Maaten & Weinberger, 2012).
- Next, we introduce TriMap, a DR method that focuses on preserving the global structure of the data in the embedding.
- The earlier approaches for DR involve linear methods such as PCA (Pearson, 1901).
- Thus, in order to obtain a normalized measure of global accuracy of a given embeddingY for a data X, we deﬁne the 2https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_s_curve.html 3More speciﬁcally, mapping to low-dimension corresponds to projecting the data onto the top-d eigendirections of the data covariance matrix.

# When To Use / Not Use
- Use when:
  - Warmuth Google Research, Brain Team {eamid, manfred}@google.com Abstract We introduce “TriMap”; a dimensionality reduction technique based on triplet constraints, which preserves the global structure of the data better than the other commonly used methods such as t-SNE, LargeVis, and UMAP.
  - The key idea behind TriMap stems from semi-supervised metric learning (Amid et al., 2016): Given an initial lowdimensional representation for the data points, the triplet information from the high-dimensional representation of the points is used to enhance the quality of the embedding.
- Avoid when:
  - Due to the high computational complexity for calculating the trustworthiness-continuity and AUC scores for large data sets, we use nearest-neighbors accuracy as the local measure of performance henceforth.
  - 4.4 Visualization of Neural Networks We visualize the different embeddings of the test set (10,000 points) from the CIFAR-10 dataset when passed through different layers of a convolutional neural network.
- Failure modes:
  - Note that the other DR methods such as t-SNE are extremely sensitive to the initialization and do not converge well with any initial solution other than small random initialization around the origin.

# Metrics Mentioned
- `trustworthiness`: referenced as part of projection-quality or reliability assessment.
- `continuity`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- This yieldsm×m′ +r = 55 triplets per point in total. ([Update] The new default parameters are set tom = 12, m′ = 4, andr = 3.) Thus, the overall complexity of the optimization step is linear in number of points n.
- In all our experiments, we perform 400 iterations with the value of momentum parameter equal to 0.5 during the ﬁrst 250 iterations and 0.8 afterwards.
- On our performance benchmarks, TriMap easily scales to millions of points without depleting the memory and clearly outperforms t-SNE, LargeVis, and UMAP in terms of runtime. [Update] The results in the current version of the paper is using an older version of the code available at:https: //github.com/eamid.
- We also perform many large-scale experiments on various datasets to show the efﬁcacy of TriMap in terms of DR performance measures and runtime. [Update] A JAX implementation of TriMap is available at: https://github.com/google/ trimap.
- Note that the other DR methods such as t-SNE are extremely sensitive to the initialization and do not converge well with any initial solution other than small random initialization around the origin.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-101-C1 | stance: support | summary: The key idea behind TriMap stems from semi-supervised metric learning (Amid et al., 2016): Given an initial lowdimensional representation for the data points, the triplet information from the high-dimensional representation of the points is used to enhance the quality of the embedding. | evidence_ids: PENDING-REF-101-E1, PENDING-REF-101-E2
- CLAIM-PENDING-REF-101-C2 | stance: support | summary: To evaluate the local performance, we show the nearest-neighbor accuracy 6Also, the embeddings obtained by simply applying these methods to our set of sampled triplets are quite subpar (see the MNIST result in (Van Der Maaten & Weinberger, 2012)) and are not shown here. | evidence_ids: PENDING-REF-101-E3, PENDING-REF-101-E4
- CLAIM-PENDING-REF-101-C3 | stance: support | summary: This yieldsm×m′ +r = 55 triplets per point in total. ([Update] The new default parameters are set tom = 12, m′ = 4, andr = 3.) Thus, the overall complexity of the optimization step is linear in number of points n. | evidence_ids: PENDING-REF-101-E5, PENDING-REF-101-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 4 | relevance: high | note: contains initialization sensitivity or control-policy evidence

# Evidence
- PENDING-REF-101-E1 | page: 2, section: extracted, quote: "The key idea behind TriMap stems from semi-supervised metric learning (Amid et al., 2016): Given an initial lowdimensional representation for the data points, the triplet information from the high-dimensional representation of the points is used to enhance the quality of the embedding."
- PENDING-REF-101-E2 | page: 6, section: extracted, quote: "Also, UMAP runs out of memory on datasets larger than∼4M points. that is designed to sample the informative triplets from the high-dimensional representation of a set of points and assign weights to these triplets to reﬂect the relative similarities of these points."
- PENDING-REF-101-E3 | page: 2, section: extracted, quote: "Similarly, TriMap is initialized with the low dimensional PCA embedding and this embedding is then modiﬁed using a set of carefully selected triplets from the high-dimensional representation."
- PENDING-REF-101-E4 | page: 1, section: extracted, quote: "The aim of DR is to provide a low-dimensional representation (typically in 2D or 3D) of a given high-dimensional dataset that preserves the overall structure of the data as much as possible."
- PENDING-REF-101-E5 | page: 6, section: extracted, quote: "To evaluate the local performance, we show the nearest-neighbor accuracy 6Also, the embeddings obtained by simply applying these methods to our set of sampled triplets are quite subpar (see the MNIST result in (Van Der Maaten & Weinberger, 2012)) and are not shown here."
- PENDING-REF-101-E6 | page: 5, section: extracted, quote: "The triplet embedding methods have been developed for a different setting where the goal is to ﬁnd an embedding based on a given pre-speciﬁed set of triplets obtained from human evaluators (or some form of implicit feedback)."
- PENDING-REF-101-E7 | page: 3, section: extracted, quote: "We deﬁne the Minimum Reconstruction Error (MRE) from the embedding as E(Y/ X) := min A∈Rm×d ∥X− AY∥2 F, where∥·∥ F denotes the Frobenius norm.4 Note that PCA has the lowest possible MRE among all the DR methods."
- PENDING-REF-101-E8 | page: 5, section: extracted, quote: "Finally, note that there exist connections between TriMap and a number oftriplet (aka ordinal) embedding methods such as t-STE (Van Der Maaten & Weinberger, 2012)."
