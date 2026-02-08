---
id: paper-2018-pending-ref-108
title: "dimRed and coRanking—Unifying Dimensionality Reduction in R"
authors: "G. Kraemer, M. Reichstein, and M. D. Mahecha"
venue: "The R Journal"
year: 2018
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-108-2018-dimred-and-coranking-unifying-dimensionality-reduction-in-r.pdf
seed_note_id: "paper-2023-zadu-library"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- 10/1, July 2018 ISSN 2073-4859 CONTRIBUTED RESEARCH ARTICLE 343 distribution was used instead of a normal distribution to model probabilities in low dimensional space to avoid the “crowding problem”, that is, a sphere in high dimensional space has a much larger volume than in low dimensional space and may contain too many points to be represented accurately in few dimensions.
- Therefore a stress function, S = √ ∑i<j (dij− ˆdij ) 2 ∑i<j d2 ij , (5) is used, and the algorithm tries to embed yi in such a way that the order of the dij is the same as the order of the ˆdij Because optimization methods can ﬁt a wide variety of problems, there are very loose limits set to the form of the error or stress function.
- PCA may suffer from a scale problem, i.e., when one variable dominates the variance simply because it is in a higher scale, to remedy this, the data can be scaled to zero mean and unit variance, depending on the use case, if this is necessary or desired.
- In ecology the comparison of sites with different species abundances is a classical multivariate problem: each observed species adds an extra dimension, and because species are often bound to certain habitats, there is a lot of redundant information.

# Method Summary
- The dimRed package wants to enable the user to objectively compare methods that rely on very different algorithmic approaches.
- Graph embedding algorithms generally suffer from long running times (though compared to other methods presented here they do not scale as badly) and many local optima.
- Therefore a stress function, S = √ ∑i<j (dij− ˆdij ) 2 ∑i<j d2 ij , (5) is used, and the algorithm tries to embed yi in such a way that the order of the dij is the same as the order of the ˆdij Because optimization methods can ﬁt a wide variety of problems, there are very loose limits set to the form of the error or stress function.
- DR methods can be modeled after physical models with attracting and repelling forces (Force Directed Methods), projections onto low dimensional planes (PCA, ICA), divergence of statistical distributions (SNE family), or the reconstruction of local spaces or points by their neighbors (LLE).
- It also provides a way to directly compare methods by plotting more than one RNX curve and an overall quality of the embedding by taking the area under the curve as an indicator for the overall quality of the embedding (see ﬁg 19) which is shown as a number in the legend.
- This is why a number of methods have been developed that try to deal with some of the shortcomings, for example, the Kamada-Kawai (Kamada and Kawai, 1989), the Fruchtermann-Reingold (Fruchterman and Reingold, 1991), or the DrL (Martin et al., 2007) algorithms.
- In optimization based methods this is generally not the case, the number of dimensions has to be chosen a priori, an embedding of 2 and 3 dimensions may vary signiﬁcantly, and there is no ordered importance of dimensions.

# When To Use / Not Use
- Use when:
  - 10/1, July 2018 ISSN 2073-4859 CONTRIBUTED RESEARCH ARTICLE 343 distribution was used instead of a normal distribution to model probabilities in low dimensional space to avoid the “crowding problem”, that is, a sphere in high dimensional space has a much larger volume than in low dimensional space and may contain too many points to be represented accurately in few dimensions.
  - DR can also be used to visualize the interiors of deep neural networks (e.g., see Han et al., 2017), where the high dimensionality comes from the large number of weights used in a neural network and convergence can be visualized by means of DR.
- Avoid when:
  - There are a number of algorithms for ICA, the most widely used is fastICA (Hyvarinen, 1999) because it provides a fast and robust way to estimate A and S.
  - The method works because of the same reason that kPCA works, i.e., classical scaling can be seen as a kPCA with kernel xTy.
- Failure modes:
  - The implementation in dimRed is based on the diffusionMap::diffuse function. non-Metric Dimensional Scaling While Classical Scaling and derived methods (see section Classical Scaling) use eigenvector decomposition to embed the data in such a way that the given distances are maintained, non-Metric Dimensional Scaling (nMDS, Kruskal, 1964a,b) uses optimization methods to reach the same goal.

# Metrics Mentioned
- `continuity`: referenced as part of projection-quality or reliability assessment.
- `stress`: referenced as part of projection-quality or reliability assessment.
- `co-ranking`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- The dimRed package tries to make the optimization process for parameters as easy as possible, but, if possible, the parameter space should be narrowed down using prior knowledge.
- The implementation in dimRed is based on the diffusionMap::diffuse function. non-Metric Dimensional Scaling While Classical Scaling and derived methods (see section Classical Scaling) use eigenvector decomposition to embed the data in such a way that the given distances are maintained, non-Metric Dimensional Scaling (nMDS, Kruskal, 1964a,b) uses optimization methods to reach the same goal.
- Therefore a stress function, S = √ ∑i<j (dij− ˆdij ) 2 ∑i<j d2 ij , (5) is used, and the algorithm tries to embed yi in such a way that the order of the dij is the same as the order of the ˆdij Because optimization methods can ﬁt a wide variety of problems, there are very loose limits set to the form of the error or stress function.
- For example, the morphology of a plant’s leaves, stems, and seeds reﬂect the environmental conditions the species usually grow in (e.g., plants with large soft leaves will never grow in a desert but might have an advantage in a humid and shadowy environment).
- In theory, any kind of regression can be used. the authors of the original paper choose Kernel Ridge Regression (KRR; Saunders et al., 1998) because it is a ﬂexible nonlinear regression technique and computational optimizations for a fast calculation exist.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-108-C1 | stance: support | summary: 10/1, July 2018 ISSN 2073-4859 CONTRIBUTED RESEARCH ARTICLE 343 distribution was used instead of a normal distribution to model probabilities in low dimensional space to avoid the “crowding problem”, that is, a sphere in high dimensional space has a much larger volume than in low dimensional space and may contain too many points to be represented accurately in few dimensions. | evidence_ids: PENDING-REF-108-E1, PENDING-REF-108-E2
- CLAIM-PENDING-REF-108-C2 | stance: support | summary: The dimRed package wants to enable the user to objectively compare methods that rely on very different algorithmic approaches. | evidence_ids: PENDING-REF-108-E3, PENDING-REF-108-E4
- CLAIM-PENDING-REF-108-C3 | stance: support | summary: The dimRed package tries to make the optimization process for parameters as easy as possible, but, if possible, the parameter space should be narrowed down using prior knowledge. | evidence_ids: PENDING-REF-108-E5, PENDING-REF-108-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 4 | relevance: high | note: contains initialization sensitivity or control-policy evidence

# Evidence
- PENDING-REF-108-E1 | page: 1, section: extracted, quote: "10/1, July 2018 ISSN 2073-4859 CONTRIBUTED RESEARCH ARTICLE 343 distribution was used instead of a normal distribution to model probabilities in low dimensional space to avoid the “crowding problem”, that is, a sphere in high dimensional space has a much larger volume than in low dimensional space and may contain too many points to be represented accurately in few dimensions."
- PENDING-REF-108-E2 | page: 6, section: extracted, quote: "Therefore a stress function, S = √ ∑i<j (dij− ˆdij ) 2 ∑i<j d2 ij , (5) is used, and the algorithm tries to embed yi in such a way that the order of the dij is the same as the order of the ˆdij Because optimization methods can ﬁt a wide variety of problems, there are very loose limits set to the form of the error or stress function."
- PENDING-REF-108-E3 | page: 4, section: extracted, quote: "PCA may suffer from a scale problem, i.e., when one variable dominates the variance simply because it is in a higher scale, to remedy this, the data can be scaled to zero mean and unit variance, depending on the use case, if this is necessary or desired."
- PENDING-REF-108-E4 | page: 1, section: extracted, quote: "In ecology the comparison of sites with different species abundances is a classical multivariate problem: each observed species adds an extra dimension, and because species are often bound to certain habitats, there is a lot of redundant information."
- PENDING-REF-108-E5 | page: 14, section: extracted, quote: "The dimRed package wants to enable the user to objectively compare methods that rely on very different algorithmic approaches."
- PENDING-REF-108-E6 | page: 7, section: extracted, quote: "Graph embedding algorithms generally suffer from long running times (though compared to other methods presented here they do not scale as badly) and many local optima."
- PENDING-REF-108-E7 | page: 1, section: extracted, quote: "DR methods can be modeled after physical models with attracting and repelling forces (Force Directed Methods), projections onto low dimensional planes (PCA, ICA), divergence of statistical distributions (SNE family), or the reconstruction of local spaces or points by their neighbors (LLE)."
- PENDING-REF-108-E8 | page: 12, section: extracted, quote: "It also provides a way to directly compare methods by plotting more than one RNX curve and an overall quality of the embedding by taking the area under the curve as an indicator for the overall quality of the embedding (see ﬁg 19) which is shown as a number in the legend."
