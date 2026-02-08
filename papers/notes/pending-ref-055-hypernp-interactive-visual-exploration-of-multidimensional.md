---
id: paper-2022-pending-ref-055
title: "HyperNP: Interactive Visual Exploration of Multidimensional Projection Hyperparameters"
authors: "G. Appleby, M. Espadoto, R. Chen, S. Goree, A. C. Telea, E. W. Anderson, and R. Chang"
venue: "Computer Graphics Forum"
year: 2022
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-055-2022-hypernp-interactive-visual-exploration-of-multidimensional-projection-hyperparameters.pdf
seed_note_id: "paper-2024-large-scale-text-spatialization"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- 4.1 Exploring Perplexity in t-SNE t-SNE is a variation of Stochastic Neighbor Embedding [29] which takes a probabilistic approach to preserving point-wise similarity when mapping high-dimensional data to a low-dimensional (typically 2D) space.
- One challenge of manifold learning based projection techniques is the projection of out-of-sample data which does not exist in the kNN graph used to determine relationships across data points.
- An important class of visualization methods for such data is projection, which maps data from a high-dimensional space to a similarity-preserving low-dimensional representation [23, 55].
- Isomap [6] tackles the problem of projecting curved manifolds by estimating geodesic distances over neighborhoods and using these as a cost function to derive the projection.

# Method Summary
- Digital Object Identiﬁer: xx.xxxx/TVCG.201x.xxxxxxx In order to support a user’s exploration of hyperparameters in projections a method is required that enables real-time interaction with a projection algorithm’s hyperparameter values.
- In this paper we propose HyperNP, a scalable method that allows for real-time interactive hyperparameter exploration of projection methods by training neural network approximations.
- 7 C ONCLUSION We proposed HyperNP, a deep learning approach to approximating projections that enables real-time interactive hyperparameter exploration.
- Training HyperNP to mimic the outcome of a parameterized projection method has two steps: (1) The hyperparameters are sampled and used to project a subset of the data using the user-selected projection technique P. (2) The HyperNP model is trained with a loss function that captures the differences between its prediction and the ground-truth given by P.
- This result suggests that HyperNP is adequately learning the Isomap projection using just 20% of the data as these three images are visually similar. underlying functionality of our method does not depend on any computational or theoretical framework unique to a given projection method, new methods are easily adapted to HyperNP’s model.
- It computes a dynamic projection to discover relationships between different projections and hidden patterns. t-viSNE [12] is an interactive tool for exploring different aspects of the t-SNE method, such as effects of hyperparameters, projection patterns, and accuracy.
- 4: Three UMAP projections of the MNIST dataset. (a) uses three nearest neighbors when constructing the kNN graph, while (b) and (c) both use four nearest neighbors. (b) initializes its embedding with positions from (a), while (c) is initialized as usual.

# When To Use / Not Use
- Use when:
  - We next describe these potential applications, their limitations, and the possibility of future research in developing neural networks as approximations of machine learning functions.
  - While widely used to visualize high-dimensional data, projections can be sensitive to hyperparameter choices which the practitioner must tune carefully.
- Avoid when:
  - Training HyperNP to mimic the outcome of a parameterized projection method has two steps: (1) The hyperparameters are sampled and used to project a subset of the data using the user-selected projection technique P. (2) The HyperNP model is trained with a loss function that captures the differences between its prediction and the ground-truth given by P.
  - Interactivity is key to all these systems [68] and involves two aspects, as users typically (1) aim to analyze subsets of D and/or subsets of its n dimensions to obtain local, more speciﬁc, insights; and (2) need to computeP several times for different values of its hyperparameters h to obtain the desired quality.
- Failure modes:
  - Explorer [59] is a general tool for exploring highdimensional data through projections which can deal with various data types, such as structured tables and unstructured text. iPCA [34] enables users to better understand and utilize PCA in an interactive setting.

# Metrics Mentioned
- `trustworthiness`: referenced as part of projection-quality or reliability assessment.
- `continuity`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- In this paper we propose HyperNP, a scalable method that allows for real-time interactive hyperparameter exploration of projection methods by training neural network approximations.
- Secondly, we show that HyperNP supports scalable exploration as it can create high-quality projections using a fraction of the training data and hyperparameter samples.
- HyperNP addresses the challenges of hyperparameter exploration and out-of-sample projection in an interactive, naturally scalable framework.
- Future work can target accelerating of HyperNP for projections with many parameters; a deeper analysis of how ﬁnely sampled the input data and parameter space is needed for high-quality inference; and most importantly, deploying HyperNP in production visual analytics systems where projections need to be explored interactively upon hyperparameter change.
- Training HyperNP to mimic the outcome of a parameterized projection method has two steps: (1) The hyperparameters are sampled and used to project a subset of the data using the user-selected projection technique P. (2) The HyperNP model is trained with a loss function that captures the differences between its prediction and the ground-truth given by P.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-055-C1 | stance: support | summary: 4.1 Exploring Perplexity in t-SNE t-SNE is a variation of Stochastic Neighbor Embedding [29] which takes a probabilistic approach to preserving point-wise similarity when mapping high-dimensional data to a low-dimensional (typically 2D) space. | evidence_ids: PENDING-REF-055-E1, PENDING-REF-055-E2
- CLAIM-PENDING-REF-055-C2 | stance: support | summary: Digital Object Identiﬁer: xx.xxxx/TVCG.201x.xxxxxxx In order to support a user’s exploration of hyperparameters in projections a method is required that enables real-time interaction with a projection algorithm’s hyperparameter values. | evidence_ids: PENDING-REF-055-E3, PENDING-REF-055-E4
- CLAIM-PENDING-REF-055-C3 | stance: support | summary: In this paper we propose HyperNP, a scalable method that allows for real-time interactive hyperparameter exploration of projection methods by training neural network approximations. | evidence_ids: PENDING-REF-055-E5, PENDING-REF-055-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 4 | relevance: high | note: contains initialization sensitivity or control-policy evidence

# Evidence
- PENDING-REF-055-E1 | page: 4, section: extracted, quote: "4.1 Exploring Perplexity in t-SNE t-SNE is a variation of Stochastic Neighbor Embedding [29] which takes a probabilistic approach to preserving point-wise similarity when mapping high-dimensional data to a low-dimensional (typically 2D) space."
- PENDING-REF-055-E2 | page: 5, section: extracted, quote: "One challenge of manifold learning based projection techniques is the projection of out-of-sample data which does not exist in the kNN graph used to determine relationships across data points."
- PENDING-REF-055-E3 | page: 1, section: extracted, quote: "An important class of visualization methods for such data is projection, which maps data from a high-dimensional space to a similarity-preserving low-dimensional representation [23, 55]."
- PENDING-REF-055-E4 | page: 2, section: extracted, quote: "Isomap [6] tackles the problem of projecting curved manifolds by estimating geodesic distances over neighborhoods and using these as a cost function to derive the projection."
- PENDING-REF-055-E5 | page: 1, section: extracted, quote: "Digital Object Identiﬁer: xx.xxxx/TVCG.201x.xxxxxxx In order to support a user’s exploration of hyperparameters in projections a method is required that enables real-time interaction with a projection algorithm’s hyperparameter values."
- PENDING-REF-055-E6 | page: 1, section: extracted, quote: "In this paper we propose HyperNP, a scalable method that allows for real-time interactive hyperparameter exploration of projection methods by training neural network approximations."
- PENDING-REF-055-E7 | page: 9, section: extracted, quote: "7 C ONCLUSION We proposed HyperNP, a deep learning approach to approximating projections that enables real-time interactive hyperparameter exploration."
- PENDING-REF-055-E8 | page: 2, section: extracted, quote: "Training HyperNP to mimic the outcome of a parameterized projection method has two steps: (1) The hyperparameters are sampled and used to project a subset of the data using the user-selected projection technique P. (2) The HyperNP model is trained with a loss function that captures the differences between its prediction and the ground-truth given by P."
