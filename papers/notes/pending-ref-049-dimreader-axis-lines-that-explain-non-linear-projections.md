---
id: paper-2019-pending-ref-049
title: "DimReader: Axis lines that explain non-linear projections"
authors: "R. Faust, D. Glickenstein, and C. Scheidegger"
venue: "IEEE Transactions on Visualization and Computer Graphics"
year: 2019
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-049-2019-dimreader-axis-lines-that-explain-non-linear-projections.pdf
seed_note_id: "paper-2025-critical-analysis-dr-four-domains"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- Cutura et. al’s VisCoDeR allows users to compare and explore different dimensionality reductions by augmenting the projection to allow users to explore how dimensions are mapped in the dimensionality reduction results as well as the high-dimensional proximity of projected points to a selected point in the projection [19].
- Although analyst guidance and validation will always be a part of a well-designed analysis infrastructure, our technique could mitigate some of the problems that have been observed in deployed systems, where projection methods are ultimately discarded because of readability issues [7, 27].
- To solve this problem, we were again able to exploit the block structure of the tangent map as well as the structure of the Laplacian matrix: the diagonal values are ∑ j̸=i Si, j and the off diagonal values are−Si, j.
- Abstract- Non-linear dimensionality reduction (NDR) methods such as LLE and t-SNE are popular with visualization researchers and experienced data analysts, but present serious problems of interpretation.

# Method Summary
- The technique we propose here can be applied to essentially all of the methods above, and offers an attractive complement to both automated and interactive projection methods.
- LLE Experiments Locally Linear Embedding is a popular method due to its performance [39], but is known to produce distorted projections [20].
- In information visualization, force-directed methods have long been used as a dimensionality reduction technique, from fullyautomatic methods [12, 28, 36], to methods which take some amount of interaction, either through placement of exemplar points [21, 30, 37] or through direct interaction with projection parameters [29].
- The perturbation of only one input point at a time offers interesting insight into the NDR method, but if we move all of the points at once in the same direction, NDR methods such as Isomap, LLE, and t-SNE will produce exactly the same projection (the perturbation vectors will be all zeros).
- Although analyst guidance and validation will always be a part of a well-designed analysis infrastructure, our technique could mitigate some of the problems that have been observed in deployed systems, where projection methods are ultimately discarded because of readability issues [7, 27].
- 3.4.2 Perturb each point individually The second method for recovering the best perturbation is to ﬁnd different perturbations for each point that collectively change the projection the most constrained so that points that are projected to similar places have similar perturbations.
- More algorithms, better infrastructure While DimReader shows that it is possible to adapt a large number of existing NDR methods to run within an autodiff framework, one goal is to provide DimReader axes to as much existing visualization infrastructure as practically possible.

# When To Use / Not Use
- Use when:
  - We implemented Isomap not only because of its historical signiﬁcance and relatively high-quality results, but also because it highlights an interesting property of automatic differentiation: it works over code bases that we tend to not think of as differentiable.
  - In practice, some issues arise because of efﬁciency concerns and library limitations.
- Avoid when:
  - Still, since t-SNE typically executes between 100 and 1000 iterations in this loop, this simple optimization achieves a signiﬁcant speedup. t-SNE Experiments T-SNE is often considered to be the state of the art in NDR methods, but one of the main objections to its use in practice is the opaque nature of its optimization criteria [52].
  - In information visualization, force-directed methods have long been used as a dimensionality reduction technique, from fullyautomatic methods [12, 28, 36], to methods which take some amount of interaction, either through placement of exemplar points [21, 30, 37] or through direct interaction with projection parameters [29].
- Failure modes:
  - Cutura et. al’s VisCoDeR allows users to compare and explore different dimensionality reductions by augmenting the projection to allow users to explore how dimensions are mapped in the dimensionality reduction results as well as the high-dimensional proximity of projected points to a selected point in the projection [19].

# Metrics Mentioned
- `stress`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- Still, since t-SNE typically executes between 100 and 1000 iterations in this loop, this simple optimization achieves a signiﬁcant speedup. t-SNE Experiments T-SNE is often considered to be the state of the art in NDR methods, but one of the main objections to its use in practice is the opaque nature of its optimization criteria [52].
- The formulation is as follows: argmax ¯v∈Rd ∑ i ||Bi ¯vi||2−λ ∑ i ∑ j || ¯vi− ¯v j||2S(i, j) s.t || ¯v2|| = 1 where Bi is the block on the diagonal for point i, ¯vi is the perturbation for the point i, λ is a free parameter for how much smoothing we want, and S(i, j) is the similarity between the projection of points i and j, pi and p j.
- DimReader extends the same principle to non-linear dimensionality reduction (NDR) methods, and recovers generalized axis lines, which help explain NDR methods in terms of interpretable data transformations. power to uncover cluster relationships in very challenging datasets, its sensitivity to the hyper-parameters is remarkable [52].
- In information visualization, force-directed methods have long been used as a dimensionality reduction technique, from fullyautomatic methods [12, 28, 36], to methods which take some amount of interaction, either through placement of exemplar points [21, 30, 37] or through direct interaction with projection parameters [29].
- To solve this issue, we implement the eigenvalue computation through power iterations [25], since matrix-vector multiplication of dual numbers has efﬁcient dual-number implementations in terms of matrices of values and ε terms.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-049-C1 | stance: support | summary: Cutura et. al’s VisCoDeR allows users to compare and explore different dimensionality reductions by augmenting the projection to allow users to explore how dimensions are mapped in the dimensionality reduction results as well as the high-dimensional proximity of projected points to a selected point in the projection [19]. | evidence_ids: PENDING-REF-049-E1, PENDING-REF-049-E2
- CLAIM-PENDING-REF-049-C2 | stance: support | summary: The technique we propose here can be applied to essentially all of the methods above, and offers an attractive complement to both automated and interactive projection methods. | evidence_ids: PENDING-REF-049-E3, PENDING-REF-049-E4
- CLAIM-PENDING-REF-049-C3 | stance: support | summary: Still, since t-SNE typically executes between 100 and 1000 iterations in this loop, this simple optimization achieves a signiﬁcant speedup. t-SNE Experiments T-SNE is often considered to be the state of the art in NDR methods, but one of the main objections to its use in practice is the opaque nature of its optimization criteria [52]. | evidence_ids: PENDING-REF-049-E5, PENDING-REF-049-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 4 | relevance: high | note: contains initialization sensitivity or control-policy evidence
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-REF-049-E1 | page: 3, section: extracted, quote: "Cutura et. al’s VisCoDeR allows users to compare and explore different dimensionality reductions by augmenting the projection to allow users to explore how dimensions are mapped in the dimensionality reduction results as well as the high-dimensional proximity of projected points to a selected point in the projection [19]."
- PENDING-REF-049-E2 | page: 3, section: extracted, quote: "Although analyst guidance and validation will always be a part of a well-designed analysis infrastructure, our technique could mitigate some of the problems that have been observed in deployed systems, where projection methods are ultimately discarded because of readability issues [7, 27]."
- PENDING-REF-049-E3 | page: 9, section: extracted, quote: "To solve this problem, we were again able to exploit the block structure of the tangent map as well as the structure of the Laplacian matrix: the diagonal values are ∑ j̸=i Si, j and the off diagonal values are−Si, j."
- PENDING-REF-049-E4 | page: 1, section: extracted, quote: "Abstract- Non-linear dimensionality reduction (NDR) methods such as LLE and t-SNE are popular with visualization researchers and experienced data analysts, but present serious problems of interpretation."
- PENDING-REF-049-E5 | page: 2, section: extracted, quote: "The technique we propose here can be applied to essentially all of the methods above, and offers an attractive complement to both automated and interactive projection methods."
- PENDING-REF-049-E6 | page: 8, section: extracted, quote: "LLE Experiments Locally Linear Embedding is a popular method due to its performance [39], but is known to produce distorted projections [20]."
- PENDING-REF-049-E7 | page: 2, section: extracted, quote: "In information visualization, force-directed methods have long been used as a dimensionality reduction technique, from fullyautomatic methods [12, 28, 36], to methods which take some amount of interaction, either through placement of exemplar points [21, 30, 37] or through direct interaction with projection parameters [29]."
- PENDING-REF-049-E8 | page: 5, section: extracted, quote: "The perturbation of only one input point at a time offers interesting insight into the NDR method, but if we move all of the points at once in the same direction, NDR methods such as Isomap, LLE, and t-SNE will produce exactly the same projection (the perturbation vectors will be all zeros)."
