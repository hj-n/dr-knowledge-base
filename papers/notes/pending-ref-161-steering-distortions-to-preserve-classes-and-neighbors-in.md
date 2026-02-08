---
id: paper-2020-pending-ref-161
title: "Steering Distortions to Preserve Classes and Neighbors in Supervised Dimensionality Reduction"
authors: "Benoît Colange, Jaakko Peltonen, Michael Aupetit, Denys Dutykh, and Sylvain Lespinats"
venue: "UNKNOWN"
year: 2020
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-161-2020-steering-distortions-to-preserve-classes-and-neighbors-in-supervised-dimensionality-r.pdf
seed_note_id: "paper-2025-jeon-reliable-va-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- Unfortunately, this ideal case is very unlikely because the data neighborhood structure and classes do not always match in the data space, and low dimensional embeddings of high-dimensional data come with unavoidable distortions [3]: false neighbors which are neighboring points in the embedding but not in the data, and missed neighbors which are neighbors in the data but not in the embedding.
- Grenoble Alpes, INES, F-73375, Le Bourget du Lac France sylvain.lespinats@cea.fr Abstract Nonlinear dimensionality reduction of high-dimensional data is challenging as the low-dimensional embedding will necessarily contain distortions, and it can be hard to determine which distortions are the most important to avoid.
- Abstract Nonlinear dimensionality reduction of high-dimensional data is challenging as the low-dimensional embedding will necessarily contain distortions, and it can be hard to determine which distortions are the most important to avoid.
- Dimensionality reduction is intended to support data scientists in analyzing multidimensional data, and can also be used to visualize high-dimensional data representing physical objects or persons in a 2D map for the lay public to get an overview of the main groups of objects/persons based on similarities in their corresponding data.

# Method Summary
- Our approach has a key advantage over previous ones: in the literature supervised methods often emphasize class separation at the price of distorting the data neighbors’ structure; conversely, unsupervised methods provide better preservation of structure at the price of often mixing classes.
- The supervised mapping method introduced in the present paper, called ClassNeRV, proposes an original stress function that takes class annotation into account and evaluates embedding quality both in terms of false neighbors and missed neighbors.
- When mapping labeled data, there are two contradictory objectives: • Classiﬁcation is typical of supervised DR techniques: class separation is emphasized and measured with classiﬁcation accuracy in the embedding space.
- 1 Introduction Dimensionality Reduction (DR) methods aim at mapping a high dimensional dataset as points in a lower dimensional embedding space, while preserving some similarity measure between data points.
- Our contribution is two-fold: we propose ClassNeRV which utilizes class information to ensure a better preservation of classes when embedding high dimensional labeled data into a low dimensional space.
- All off-the-shelf algorithms are set with default parameters, except for tSNE initialization, for which we used PCA instead of random (so that all methods beneﬁt from a spectral initialization).
- We propose that the embedding should not artiﬁcially separate points within the same class , or artiﬁcially cluster 3 together points from different classes.

# When To Use / Not Use
- Use when:
  - Unfortunately, this ideal case is very unlikely because the data neighborhood structure and classes do not always match in the data space, and low dimensional embeddings of high-dimensional data come with unavoidable distortions [3]: false neighbors which are neighboring points in the embedding but not in the data, and missed neighbors which are neighbors in the data but not in the embedding.
  - When annotation of data into known relevant classes is available, it can be used to guide the embedding to avoid distortions that worsen class separation.
- Avoid when:
  - Dimensionality reduction is intended to support data scientists in analyzing multidimensional data, and can also be used to visualize high-dimensional data representing physical objects or persons in a 2D map for the lay public to get an overview of the main groups of objects/persons based on similarities in their corresponding data.
  - Grenoble Alpes, INES, F-73375, Le Bourget du Lac France sylvain.lespinats@cea.fr Abstract Nonlinear dimensionality reduction of high-dimensional data is challenging as the low-dimensional embedding will necessarily contain distortions, and it can be hard to determine which distortions are the most important to avoid.
- Failure modes:
  - However, both LMDS and ClassiMap being distance-based are sensitive to the norm concentration phenomenon in high dimensions [34] while NE techniques like NeRV mitigate this effect using shift-invariant membership degrees [35].

# Metrics Mentioned
- `trustworthiness`: referenced as part of projection-quality or reliability assessment.
- `continuity`: referenced as part of projection-quality or reliability assessment.
- `stress`: referenced as part of projection-quality or reliability assessment.
- `kl divergence`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- All off-the-shelf algorithms are set with default parameters, except for tSNE initialization, for which we used PCA instead of random (so that all methods beneﬁt from a spectral initialization).
- We re-parameterizeτ∈ andτ/∈ asτ∗ = (τ∈ +τ/∈)/2 andε = (τ∈−τ/∈)/2. τ∗∈ [0, 1] controls the average trade-off between penalizations of false and missed neighbors (asτ in NeRV), while ε∈ [0, 0.5] controls the level of supervision (more supervision for greater values).
- Parametersτ∈ andτ/∈ deﬁneClassNeRV mapping behavior by weighting these terms.τ∈ controls the balance for penalization of false neighbors and missed neighborswithin classes, whileτ/∈ controls a similar balancing between classes.
- Top heat maps show structure preservation indicators in the same{τ∗,ε}-parameter space: whenτ∗ increases, the amount of false neighbors (T in blue) increases, while the amount of missed neighbors (C in red) decreases.
- Its stress function, derived from the unsupervised NeRV [6, 7], steers the optimization so that the unavoidable distortions of the neighborhood structure are placed where they are less harmful to the class structure.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-161-C1 | stance: support | summary: Unfortunately, this ideal case is very unlikely because the data neighborhood structure and classes do not always match in the data space, and low dimensional embeddings of high-dimensional data come with unavoidable distortions [3]: false neighbors which are neighboring points in the embedding but not in the data, and missed neighbors which are neighbors in the data but not in the embedding. | evidence_ids: PENDING-REF-161-E1, PENDING-REF-161-E2
- CLAIM-PENDING-REF-161-C2 | stance: support | summary: Our approach has a key advantage over previous ones: in the literature supervised methods often emphasize class separation at the price of distorting the data neighbors’ structure; conversely, unsupervised methods provide better preservation of structure at the price of often mixing classes. | evidence_ids: PENDING-REF-161-E3, PENDING-REF-161-E4
- CLAIM-PENDING-REF-161-C3 | stance: support | summary: All off-the-shelf algorithms are set with default parameters, except for tSNE initialization, for which we used PCA instead of random (so that all methods beneﬁt from a spectral initialization). | evidence_ids: PENDING-REF-161-E5, PENDING-REF-161-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 4 | relevance: high | note: contains initialization sensitivity or control-policy evidence

# Evidence
- PENDING-REF-161-E1 | page: 2, section: extracted, quote: "Unfortunately, this ideal case is very unlikely because the data neighborhood structure and classes do not always match in the data space, and low dimensional embeddings of high-dimensional data come with unavoidable distortions [3]: false neighbors which are neighboring points in the embedding but not in the data, and missed neighbors which are neighbors in the data but not in the embedding."
- PENDING-REF-161-E2 | page: 1, section: extracted, quote: "Grenoble Alpes, INES, F-73375, Le Bourget du Lac France sylvain.lespinats@cea.fr Abstract Nonlinear dimensionality reduction of high-dimensional data is challenging as the low-dimensional embedding will necessarily contain distortions, and it can be hard to determine which distortions are the most important to avoid."
- PENDING-REF-161-E3 | page: 1, section: extracted, quote: "Abstract Nonlinear dimensionality reduction of high-dimensional data is challenging as the low-dimensional embedding will necessarily contain distortions, and it can be hard to determine which distortions are the most important to avoid."
- PENDING-REF-161-E4 | page: 10, section: extracted, quote: "Dimensionality reduction is intended to support data scientists in analyzing multidimensional data, and can also be used to visualize high-dimensional data representing physical objects or persons in a 2D map for the lay public to get an overview of the main groups of objects/persons based on similarities in their corresponding data."
- PENDING-REF-161-E5 | page: 1, section: extracted, quote: "Our approach has a key advantage over previous ones: in the literature supervised methods often emphasize class separation at the price of distorting the data neighbors’ structure; conversely, unsupervised methods provide better preservation of structure at the price of often mixing classes."
- PENDING-REF-161-E6 | page: 1, section: extracted, quote: "The supervised mapping method introduced in the present paper, called ClassNeRV, proposes an original stress function that takes class annotation into account and evaluates embedding quality both in terms of false neighbors and missed neighbors."
- PENDING-REF-161-E7 | page: 1, section: extracted, quote: "When mapping labeled data, there are two contradictory objectives: • Classiﬁcation is typical of supervised DR techniques: class separation is emphasized and measured with classiﬁcation accuracy in the embedding space."
- PENDING-REF-161-E8 | page: 1, section: extracted, quote: "1 Introduction Dimensionality Reduction (DR) methods aim at mapping a high dimensional dataset as points in a lower dimensional embedding space, while preserving some similarity measure between data points."
