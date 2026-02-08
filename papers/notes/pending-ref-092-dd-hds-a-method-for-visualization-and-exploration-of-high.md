---
id: paper-2007-pending-ref-092
title: "DD-HDS: A Method for Visualization and Exploration of High-Dimensional Data"
authors: "Sylvain Lespinats, Michel Verleysen, Alain Giron, and Bernard Fertil"
venue: "IEEE Transactions on Neural Networks"
year: 2007
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-092-2007-dd-hds-a-method-for-visualization-and-exploration-of-high-dimensional-data.pdf
seed_note_id: "paper-2025-jeon-reliable-va-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- IEEE Transactions on Neural Networks, 2007, 18 (5), pp.1265-79. ￿inserm-00250168￿ TNN05-P800 1 Abstract — Mapping high-dimensional data in a lowdimensional space, for example for visualization, is a problem of increasingly major concern in data analysis.
- Giving an “objective” quantitative evaluation of the efficiency of mapping methods is quite difficult: there is obviously a subjective part in the low-dimensional mapping of high-dimensional data.
- However, high-dimensional data raise unusual problems of analysis, given that some properties of the spaces they live in cannot be extrapolated from our common experience.
- Abstract — Mapping high-dimensional data in a lowdimensional space, for example for visualization, is a problem of increasingly major concern in data analysis.

# Method Summary
- Locally Linear Embedding (LLE) [30], Laplacian Eigenmaps [31] and Hessian-based Locally Linear Embedding (HLLE) [32] assume that data are located on a manifold, smooth enough to be reasonably well approximated by local linear models ; these methods unfold the set of data through local linear projections.
- Finally, the optimization of the method-specific objective function is performed by Force Directed Placement (FDP), as an alternative to more traditional gradient-based algorithms (see section IV.C).
- DD-HDS: PRINCIPLES RULING THE METHOD In this section a new nonlinear dimensionality reduction method is proposed, which addresses the two shortcomings detailed above: the method implements a weighting of distances specifically adapted to high-dimensional data, and avoids too high risks of both tears and false neighbors through a symmetric weighting approach.
- Section IV presents our original nonlinear mapping algorithm called DD-HDS for Data DD-HDS: a method for visualization and exploration of high-dimensional data Sylvain Lespinats, Michel Verleysen, Senior Member, IEEE, Alain Giron, Bernard Fertil V TNN05-P800 2 Driven High-Dimensional Scaling.
- Approaches for dimension reduction Because keeping exactly all distances between pairs of points unchanged in the representation is most often impossible, all methods emphasize the preservation of some distances or types of distances, therefore privileging a specific point of view.
- The possibility to obtain different mappings when the algorithm is run several times on the same data results from its stochastic character; the only stochastic part of the method is described in section IV.E.
- Giving an “objective” quantitative evaluation of the efficiency of mapping methods is quite difficult: there is obviously a subjective part in the low-dimensional mapping of high-dimensional data.

# When To Use / Not Use
- Use when:
  - Although Sammon’s mapping makes a better use of the output space, it fails to display the species organization: the projection remains folded, because of the limitations resulting from the Sammon's stress weighting by distances in the original space, and also probably because of the concentration of measure phenomenon (see section III.B).
  - However, absolute values are used here instead of squares, to avoid giving a too high importance to large distances (often responsible of large differences) in the criteria.
- Avoid when:
  - False neighbors and tears are limitations of nonlinear dimensionality reduction methods, which cannot be avoided in most cases due to the intrinsic nature of the manifold.
  - DD-HDS: PRINCIPLES RULING THE METHOD In this section a new nonlinear dimensionality reduction method is proposed, which addresses the two shortcomings detailed above: the method implements a weighting of distances specifically adapted to high-dimensional data, and avoids too high risks of both tears and false neighbors through a symmetric weighting approach.
- Failure modes:
  - However, in the first case, it is difficult to tear distributions with loops, leading to the so-called "false neighborhood" representation: data far from each other in the original space could be mapped to close points, exactly as PCA "flattens" volumes when the number of principal components used in the projection is not sufficient.

# Metrics Mentioned
- `continuity`: referenced as part of projection-quality or reliability assessment.
- `stress`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- This difference is essential in terms of computational complexity; the computational load of the optimization procedures themselves is however quite impossible to evaluate in practical situations, as it depends dramatically on the content of the initial data set, which determines when the stopping criterion is reached.
- The stopping criterion of the algorithm may be a maximum number of iterations, but it has been shown (c.f. [56, 57]) that it is possible to define an energy function whose minimum is attained when the algorithm stabilizes; this function may then be used to control the convergence and stop the algorithm.
- In DD-HDS, a single user-defined parameter allows fixing the compromise between local neighborhood preservation and global mapping; in our experience, this feature turns out very convenient for the interactive exploration of high-dimensional data.
- More precisely, the weighting is set according to the effective distribution of distances in the data set, with the exception of a single user-defined parameter setting the trade-off between local neighborhood preservation and global mapping.
- Its intensity is function of the local pressure: r F browniani = α iteration( ) × Pi N × r u i (11) where r u i is an unit vector randomly oriented and α tends toward 0 when the number of iterations increases to allow system relaxation.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-092-C1 | stance: support | summary: IEEE Transactions on Neural Networks, 2007, 18 (5), pp.1265-79. ￿inserm-00250168￿ TNN05-P800 1 Abstract — Mapping high-dimensional data in a lowdimensional space, for example for visualization, is a problem of increasingly major concern in data analysis. | evidence_ids: PENDING-REF-092-E1, PENDING-REF-092-E2
- CLAIM-PENDING-REF-092-C2 | stance: support | summary: Locally Linear Embedding (LLE) [30], Laplacian Eigenmaps [31] and Hessian-based Locally Linear Embedding (HLLE) [32] assume that data are located on a manifold, smooth enough to be reasonably well approximated by local linear models ; these methods unfold the set of data through local linear projections. | evidence_ids: PENDING-REF-092-E3, PENDING-REF-092-E4
- CLAIM-PENDING-REF-092-C3 | stance: support | summary: This difference is essential in terms of computational complexity; the computational load of the optimization procedures themselves is however quite impossible to evaluate in practical situations, as it depends dramatically on the content of the initial data set, which determines when the stopping criterion is reached. | evidence_ids: PENDING-REF-092-E5, PENDING-REF-092-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 4 | relevance: high | note: contains initialization sensitivity or control-policy evidence

# Evidence
- PENDING-REF-092-E1 | page: 1, section: extracted, quote: "IEEE Transactions on Neural Networks, 2007, 18 (5), pp.1265-79. ￿inserm-00250168￿ TNN05-P800 1 Abstract — Mapping high-dimensional data in a lowdimensional space, for example for visualization, is a problem of increasingly major concern in data analysis."
- PENDING-REF-092-E2 | page: 16, section: extracted, quote: "Giving an “objective” quantitative evaluation of the efficiency of mapping methods is quite difficult: there is obviously a subjective part in the low-dimensional mapping of high-dimensional data."
- PENDING-REF-092-E3 | page: 2, section: extracted, quote: "However, high-dimensional data raise unusual problems of analysis, given that some properties of the spaces they live in cannot be extrapolated from our common experience."
- PENDING-REF-092-E4 | page: 2, section: extracted, quote: "Abstract — Mapping high-dimensional data in a lowdimensional space, for example for visualization, is a problem of increasingly major concern in data analysis."
- PENDING-REF-092-E5 | page: 4, section: extracted, quote: "Locally Linear Embedding (LLE) [30], Laplacian Eigenmaps [31] and Hessian-based Locally Linear Embedding (HLLE) [32] assume that data are located on a manifold, smooth enough to be reasonably well approximated by local linear models ; these methods unfold the set of data through local linear projections."
- PENDING-REF-092-E6 | page: 2, section: extracted, quote: "Finally, the optimization of the method-specific objective function is performed by Force Directed Placement (FDP), as an alternative to more traditional gradient-based algorithms (see section IV.C)."
- PENDING-REF-092-E7 | page: 6, section: extracted, quote: "DD-HDS: PRINCIPLES RULING THE METHOD In this section a new nonlinear dimensionality reduction method is proposed, which addresses the two shortcomings detailed above: the method implements a weighting of distances specifically adapted to high-dimensional data, and avoids too high risks of both tears and false neighbors through a symmetric weighting approach."
- PENDING-REF-092-E8 | page: 2, section: extracted, quote: "Section IV presents our original nonlinear mapping algorithm called DD-HDS for Data DD-HDS: a method for visualization and exploration of high-dimensional data Sylvain Lespinats, Michel Verleysen, Senior Member, IEEE, Alain Giron, Bernard Fertil V TNN05-P800 2 Driven High-Dimensional Scaling."
