---
id: paper-2020-zadu-ref-14
title: "Steering Distortions to Preserve Classes and Neighbors in Supervised Dimensionality Reduction"
authors: "Benoit Colange, Jaakko Peltonen, Michael Aupetit, Denys Dutykh, Sylvain Lespinats"
venue: "Advances in Neural Information Processing Systems (NeurIPS)"
year: 2020
tags: [dr, zadu-table1-reference, kl_div, pr, stress, tnc]
source_pdf: papers/raw/zadu-table1-references/ref06_steering_distortions_to_preserve_classes_and_neighbors_in_supervised_dimensionality_reduct.pdf
evidence_level: medium
updated_at: 2026-02-08
---
# Problem
- Unfortunately, this ideal case is very unlikely because the data neighborhood structure and classes do not always match in the data space, and low dimensional embeddings of high-dimensional data come with unavoidable distortions [3]: false neighbors which are neighboring points in the embedding but not in the data, and missed neighbors which are neighbors in the data but not in the embedding.
- Grenoble Alpes, INES, F-73375, Le Bourget du Lac France sylvain.lespinats@cea.fr Abstract Nonlinear dimensionality reduction of high-dimensional data is challenging as the low-dimensional embedding will necessarily contain distortions, and it can be hard to determine which distortions are the most important to avoid.
- Abstract Nonlinear dimensionality reduction of high-dimensional data is challenging as the low-dimensional embedding will necessarily contain distortions, and it can be hard to determine which distortions are the most important to avoid.
- Dimensionality reduction is intended to support data scientists in analyzing multidimensional data, and can also be used to visualize high-dimensional data representing physical objects or persons in a 2D map for the lay public to get an overview of the main groups of objects/persons based on similarities in their corresponding data.
- Its stress function, derived from the unsupervised NeRV [6, 7], steers the optimization so that the unavoidable distortions of the neighborhood structure are placed where they are less harmful to the class structure.

# Method Summary
- The supervised mapping method introduced in the present paper, called ClassNeRV, proposes an original stress function that takes class annotation into account and evaluates embedding quality both in terms of false neighbors and missed neighbors.
- Many linear or non-linear algorithms have been previously proposed including Principal Component Analysis (PCA) [14], Self Organizing Maps (SOM) [15], isometric feature mapping ( Isomap) [16], Data-Driven High Dimensional Scaling ( DD-HDS) [17], Local Afﬁne Multidimensional Projection (LAMP) [18] and Uniform Manifold Approximation and Projection (UMAP) [12].
- Other methods rely on a global parametric mapping and optimize its parameters to maximize class separation, as Linear Discriminant Analysis ( LDA) [25] and its kernelized variants [ 26, 27, 28], Neighbourhood Component Analysis (NCA) [29] and its neural-network variant [30] or Limited Rank Matrix Learning Vector Quantization (LiRaM L VQ) [31].
- 3.3 Quality Indicators of Supervised Techniques for Exploratory Analysis To assess the preservation of neighborhood structures, we adopt the Trustworthiness and Continuity measures [ 13] which are standard to evaluate unsupervised embeddings in the context of exploratory analysis [3].
- When mapping labeled data, there are two contradictory objectives: • Classiﬁcation is typical of supervised DR techniques: class separation is emphasized and measured with classiﬁcation accuracy in the embedding space.
- 1 Introduction Dimensionality Reduction (DR) methods aim at mapping a high dimensional dataset as points in a lower dimensional embedding space, while preserving some similarity measure between data points.
- Our contribution is two-fold: we propose ClassNeRV which utilizes class information to ensure a better preservation of classes when embedding high dimensional labeled data into a low dimensional space.

# When To Use / Not Use
- Use when:
  - When annotation of data into known relevant classes is available, it can be used to guide the embedding to avoid distortions that worsen class separation.
  - Unfortunately, this ideal case is very unlikely because the data neighborhood structure and classes do not always match in the data space, and low dimensional embeddings of high-dimensional data come with unavoidable distortions [3]: false neighbors which are neighboring points in the embedding but not in the data, and missed neighbors which are neighbors in the data but not in the embedding.
  - The NeRV stress function is a linear trade-off between two sets of Kullback–Leibler (KL) divergences: ζNeRV ≜ ∑ i τ DKL(βi,bi)+(1−τ)DKL(bi,βi) ≜τ ∑ i,j̸=i βij log (βij bij ) +(1−τ) ∑ i,j̸=i bij log (bij βij ) (2) In Equation (2),τ∈ [0; 1] controls the trade-off between∑ i DKL(βi,bi) penalizing missed neighbors (maximally when τ = 1) and∑ i DKL(bi,βi) penalizing false neighbors (maximally when τ = 0).
- Avoid when:
  - Dimensionality reduction is intended to support data scientists in analyzing multidimensional data, and can also be used to visualize high-dimensional data representing physical objects or persons in a 2D map for the lay public to get an overview of the main groups of objects/persons based on similarities in their corresponding data.
  - Grenoble Alpes, INES, F-73375, Le Bourget du Lac France sylvain.lespinats@cea.fr Abstract Nonlinear dimensionality reduction of high-dimensional data is challenging as the low-dimensional embedding will necessarily contain distortions, and it can be hard to determine which distortions are the most important to avoid.
- Failure modes:
  - Munzner, “Visualizing dimensionally-reduced data: interviews with analysts and a characterization of task sequences,” in Proceedings of the Fifth Workshop on Beyond Time and Errors: Novel Evaluation Methods for Visualization, BELIV 2014, Paris, France, November 10, 2014(H.
  - At last, ClassiMap [5] optimizes a stress function similar to the one of Local Multidimensional Scaling (LMDS) [33], but supports the exploratory analysis of labeled data by taking classes into account when penalizing false and missed neighbors.

# Metrics Mentioned
- `tnc`: Trustworthiness and Continuity behavior.
- `nh`: label-based neighborhood hit.
- `nd`: neighbor-shape dissimilarity or neighbor distortion.
- `kl_div`: Kullback-Leibler divergence behavior.
- `pr`: pairwise-distance correlation behavior.
- `proc`: Procrustes local shape agreement.
- `stress`: stress-based distance distortion.

# Implementation Notes
- Scale parameters σi are set to get a ﬁxed user-chosen perplexityp akin to a smooth or fuzzy measure of the number of neighbors of each point [36]:H(βi) = logp, with the entropyH(βi) ≜−∑ j̸=iβij logβij.
- All off-the-shelf algorithms are set with default parameters, except for tSNE initialization, for which we used PCA instead of random (so that all methods beneﬁt from a spectral initialization).
- The ﬁnal perplexity in our multi-scale optimization is set to p = 32 for Globe andp = 30 for Isolet, for comparability with tSNE defaultp = 30.
- Here, we set embedding scale parameterssi equal toσi.
- Other methods rely on a global parametric mapping and optimize its parameters to maximize class separation, as Linear Discriminant Analysis ( LDA) [25] and its kernelized variants [ 26, 27, 28], Neighbourhood Component Analysis (NCA) [29] and its neural-network variant [30] or Limited Rank Matrix Learning Vector Quantization (LiRaM L VQ) [31].
- We re-parameterizeτ∈ andτ/∈ asτ∗ = (τ∈ +τ/∈)/2 andε = (τ∈−τ/∈)/2. τ∗∈ [0, 1] controls the average trade-off between penalizations of false and missed neighbors (asτ in NeRV), while ε∈ [0, 0.5] controls the level of supervision (more supervision for greater values).
- Keep preprocessing, initialization policy, and random-seed protocol fixed when comparing methods.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PAPER2020ZADUREF14-C1 | stance: support | summary: Unfortunately, this ideal case is very unlikely because the data neighborhood structure and classes do not always match in the data space, and low dimensional embeddings of high-dimensional data come with unavoidable distortions [3]: false neighbors which are neighboring points in the embedding but not in the data, and missed neighbors which are neighbors in the data but not in the embedding. | evidence_ids: PAPER2020ZADUREF14-E1, PAPER2020ZADUREF14-E2
- CLAIM-PAPER2020ZADUREF14-C2 | stance: support | summary: The supervised mapping method introduced in the present paper, called ClassNeRV, proposes an original stress function that takes class annotation into account and evaluates embedding quality both in terms of false neighbors and missed neighbors. | evidence_ids: PAPER2020ZADUREF14-E3, PAPER2020ZADUREF14-E4
- CLAIM-PAPER2020ZADUREF14-C3 | stance: support | summary: Scale parameters σi are set to get a ﬁxed user-chosen perplexityp akin to a smooth or fuzzy measure of the number of neighbors of each point [36]:H(βi) = logp, with the entropyH(βi) ≜−∑ j̸=iβij logβij. | evidence_ids: PAPER2020ZADUREF14-E5, PAPER2020ZADUREF14-E6
- CLAIM-METRIC-KL_DIV-SOURCE-14 | stance: support | summary: This source includes evidence relevant to `kl_div` in dimensionality-reduction reliability evaluation. | evidence_ids: PAPER2020ZADUREF14-E1, PAPER2020ZADUREF14-E2
- CLAIM-METRIC-PR-SOURCE-14 | stance: support | summary: This source includes evidence relevant to `pr` in dimensionality-reduction reliability evaluation. | evidence_ids: PAPER2020ZADUREF14-E1, PAPER2020ZADUREF14-E2
- CLAIM-METRIC-STRESS-SOURCE-14 | stance: support | summary: This source includes evidence relevant to `stress` in dimensionality-reduction reliability evaluation. | evidence_ids: PAPER2020ZADUREF14-E1, PAPER2020ZADUREF14-E2
- CLAIM-METRIC-TNC-SOURCE-14 | stance: support | summary: This source includes evidence relevant to `tnc` in dimensionality-reduction reliability evaluation. | evidence_ids: PAPER2020ZADUREF14-E1, PAPER2020ZADUREF14-E2

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports task clarification before model selection
- step: 2 | relevance: medium | note: adds constraints for preprocessing and data-audit checks
- step: 3 | relevance: high | note: directly informs task-aligned technique/metric selection
- step: 5 | relevance: medium | note: adds initialization sensitivity guidance
- step: 6 | relevance: high | note: adds hyperparameter sensitivity or optimization guidance

# Evidence
- PAPER2020ZADUREF14-E1 | page: 2, section: extracted, quote: "Unfortunately, this ideal case is very unlikely because the data neighborhood structure and classes do not always match in the data space, and low dimensional embeddings of high-dimensional data come with unavoidable distortions [3]: false neighbors which are neighboring points in the embedding but not in the data, and missed neighbors which are neighbors in the data but not in the embedding."
- PAPER2020ZADUREF14-E2 | page: 1, section: extracted, quote: "Grenoble Alpes, INES, F-73375, Le Bourget du Lac France sylvain.lespinats@cea.fr Abstract Nonlinear dimensionality reduction of high-dimensional data is challenging as the low-dimensional embedding will necessarily contain distortions, and it can be hard to determine which distortions are the most important to avoid."
- PAPER2020ZADUREF14-E3 | page: 1, section: extracted, quote: "Abstract Nonlinear dimensionality reduction of high-dimensional data is challenging as the low-dimensional embedding will necessarily contain distortions, and it can be hard to determine which distortions are the most important to avoid."
- PAPER2020ZADUREF14-E4 | page: 10, section: extracted, quote: "Dimensionality reduction is intended to support data scientists in analyzing multidimensional data, and can also be used to visualize high-dimensional data representing physical objects or persons in a 2D map for the lay public to get an overview of the main groups of objects/persons based on similarities in their corresponding data."
- PAPER2020ZADUREF14-E5 | page: 2, section: extracted, quote: "Its stress function, derived from the unsupervised NeRV [6, 7], steers the optimization so that the unavoidable distortions of the neighborhood structure are placed where they are less harmful to the class structure."
- PAPER2020ZADUREF14-E6 | page: 9, section: extracted, quote: "Least distortions II NCA S-Isomap ClassiMap S-UMAP NeRV ClassNeRV 50 55 60 65 70 75 80 85 90 95 100 Trustworthiness (%) 50 55 60 65 70 75 80 85 90 95 100 Continuity (%) Most distortions Least false neighb."
- PAPER2020ZADUREF14-E7 | page: 1, section: extracted, quote: "The supervised mapping method introduced in the present paper, called ClassNeRV, proposes an original stress function that takes class annotation into account and evaluates embedding quality both in terms of false neighbors and missed neighbors."
- PAPER2020ZADUREF14-E8 | page: 2, section: extracted, quote: "Many linear or non-linear algorithms have been previously proposed including Principal Component Analysis (PCA) [14], Self Organizing Maps (SOM) [15], isometric feature mapping ( Isomap) [16], Data-Driven High Dimensional Scaling ( DD-HDS) [17], Local Afﬁne Multidimensional Projection (LAMP) [18] and Uniform Manifold Approximation and Projection (UMAP) [12]."
- PAPER2020ZADUREF14-E9 | page: 3, section: extracted, quote: "Other methods rely on a global parametric mapping and optimize its parameters to maximize class separation, as Linear Discriminant Analysis ( LDA) [25] and its kernelized variants [ 26, 27, 28], Neighbourhood Component Analysis (NCA) [29] and its neural-network variant [30] or Limited Rank Matrix Learning Vector Quantization (LiRaM L VQ) [31]."
- PAPER2020ZADUREF14-E10 | page: 4, section: extracted, quote: "3.3 Quality Indicators of Supervised Techniques for Exploratory Analysis To assess the preservation of neighborhood structures, we adopt the Trustworthiness and Continuity measures [ 13] which are standard to evaluate unsupervised embeddings in the context of exploratory analysis [3]."
- PAPER2020ZADUREF14-E11 | page: 1, section: extracted, quote: "When mapping labeled data, there are two contradictory objectives: • Classiﬁcation is typical of supervised DR techniques: class separation is emphasized and measured with classiﬁcation accuracy in the embedding space."
- PAPER2020ZADUREF14-E12 | page: 1, section: extracted, quote: "1 Introduction Dimensionality Reduction (DR) methods aim at mapping a high dimensional dataset as points in a lower dimensional embedding space, while preserving some similarity measure between data points."
