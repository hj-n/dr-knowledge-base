---
id: paper-2026-pending-extra-least-square-project
title: "Least Square Projection: A Fast High-Precision Multidimensional Projection Technique and Its Application to Document Mapping"
authors: "F.V. Paulovich, L.G. Nonato, R. Minghim, H. Levkowitz"
venue: "IEEE Transactions on Visualization and Computer Graphics"
year: 2008
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/Least_Square_Projection_A_Fast_High-Precision_Multidimensional_Projection_Technique_and_Its_Application_to_Document_Mapping (1).pdf
seed_note_id: "paper-2015-perception-based-projection-evaluation"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- Conventional methods for multidimensional data visualization such as scatterplots, parallel coordinates, or pixel-oriented methods, which are normally employed to assist data interpretation, can fail if they are directly applied to high-dimensional data (a good review of data visualization methods can be found in [1]).
- Paulovich, Luis Gustavo Nonato, Rosane Minghim, and Haim Levkowitz, Member, IEEE Abstract—The problem of projecting multidimensional data into lower dimensions has been pursued by many researchers due to its potential application to data analyses of various kinds.
- The problem of multidimensional projection has been the concern of many researchers due to the large variety of applications that could benefit from visual representations of data sets with large number of dimensions.
- Moreover, identification of patterns and models grows more difficult as dimensionality increases (the dimensionality curse [2]), and the lack of proper representations can severely impair interpretation.

# Method Summary
- 3L EAST SQUARE PROJECTION Given a set of points S ¼f p1; ... ;p ng in IRm,t h eL S P algorithm aims at representing the points of S in a lower dimensional space IRd, d /C20 m, so as to preserve the neighborhood relationship among the points as much as possible.
- It starts by defining a function that indicates the amount of information lost in the projection and then applies an iterative nonlinear optimization method based on the gradient of this function to find a (local) minimum.
- This paper presents a novel multidimensional projection technique, called Least Square Projection (LSP), that encompasses good features of both linear and nonlinear projection methods.
- In order to achieve high precision with reasonable computation cost for reasonably sized data sets, we present a novel projection technique, called LSP.
- However, we also aim at reduced cost, as compared to the basic algorithms of the projections with the highest quality in these terms.
- One method for reducing the dimensionality that has been successfully applied is the Multidimensional Projection technique.
- The first example aims at verifying that LSP could keep the projection of points (documents) that are considered to be in the same general area close to each other in data sets with documents in various “general areas.” We looked at the positioning of papers within a group to see whether papers previously known to address that subject and to have highly similar content have been mapped close to each other.

# When To Use / Not Use
- Use when:
  - Making use of the neighborhood relationship of the points in IRm and the Cartesian coordinates of the control points inIRd, it is possible to build a linear system whose solutions are the Cartesian coordinates of the points pi in IRd.
  - Well-built projections can be used in this case to display the underlying global structure or local trends of a document collection by organizing similarity in content with neighboring regions on the map.
- Avoid when:
  - Aiming at executing this selection, the data set is split into nc clusters using the k-medoids method [2], and the medoid (the nearest point to the centroid) of each cluster is used as a control point.
  - In fact, the LSP method generalizes the ideas of Sorkine and Cohen-Or in order to deal with highdimensional spaces while avoiding the need of a mesh to define the linear system.
- Failure modes:
  - Haim Levkowitz is an associate professor of computer science and a codirector of the Institute for Visualization and Perception Research, University of Massachusetts, Lowell.

# Metrics Mentioned
- `stress`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- It starts by defining a function that indicates the amount of information lost in the projection and then applies an iterative nonlinear optimization method based on the gradient of this function to find a (local) minimum.
- Aiming at reducing this complexity, two different strategies can be employed: reducing the number of iterations necessary to reach the equilibrium state or reducing the complexity of each iteration.
- Although Sammon’s Mapping can unfold data belonging to manifolds of high-dimension, once large distances are taken into account in the optimization, it can fail for highly twisted spaces.
- Approaches to reduce the complexity of the techniques aim at making them more scalable to very large data sets, since this is one challenge of information visualization tasks.
- In this sense, an improvement is the Curvilinear Component Analysis (CCA) [11], which employs a new optimization function that ignores distances greater than a threshold.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-EXTRA-C1 | stance: support | summary: Conventional methods for multidimensional data visualization such as scatterplots, parallel coordinates, or pixel-oriented methods, which are normally employed to assist data interpretation, can fail if they are directly applied to high-dimensional data (a good review of data visualization methods can be found in [1]). | evidence_ids: PENDING-EXTRA-E1, PENDING-EXTRA-E2
- CLAIM-PENDING-EXTRA-C2 | stance: support | summary: 3L EAST SQUARE PROJECTION Given a set of points S ¼f p1; ... ;p ng in IRm,t h eL S P algorithm aims at representing the points of S in a lower dimensional space IRd, d /C20 m, so as to preserve the neighborhood relationship among the points as much as possible. | evidence_ids: PENDING-EXTRA-E3, PENDING-EXTRA-E4
- CLAIM-PENDING-EXTRA-C3 | stance: support | summary: It starts by defining a function that indicates the amount of information lost in the projection and then applies an iterative nonlinear optimization method based on the gradient of this function to find a (local) minimum. | evidence_ids: PENDING-EXTRA-E5, PENDING-EXTRA-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-EXTRA-E1 | page: 1, section: extracted, quote: "Conventional methods for multidimensional data visualization such as scatterplots, parallel coordinates, or pixel-oriented methods, which are normally employed to assist data interpretation, can fail if they are directly applied to high-dimensional data (a good review of data visualization methods can be found in [1])."
- PENDING-EXTRA-E2 | page: 1, section: extracted, quote: "Paulovich, Luis Gustavo Nonato, Rosane Minghim, and Haim Levkowitz, Member, IEEE Abstract—The problem of projecting multidimensional data into lower dimensions has been pursued by many researchers due to its potential application to data analyses of various kinds."
- PENDING-EXTRA-E3 | page: 1, section: extracted, quote: "The problem of multidimensional projection has been the concern of many researchers due to the large variety of applications that could benefit from visual representations of data sets with large number of dimensions."
- PENDING-EXTRA-E4 | page: 1, section: extracted, quote: "Moreover, identification of patterns and models grows more difficult as dimensionality increases (the dimensionality curse [2]), and the lack of proper representations can severely impair interpretation."
- PENDING-EXTRA-E5 | page: 3, section: extracted, quote: "3L EAST SQUARE PROJECTION Given a set of points S ¼f p1; ... ;p ng in IRm,t h eL S P algorithm aims at representing the points of S in a lower dimensional space IRd, d /C20 m, so as to preserve the neighborhood relationship among the points as much as possible."
- PENDING-EXTRA-E6 | page: 2, section: extracted, quote: "It starts by defining a function that indicates the amount of information lost in the projection and then applies an iterative nonlinear optimization method based on the gradient of this function to find a (local) minimum."
- PENDING-EXTRA-E7 | page: 2, section: extracted, quote: "This paper presents a novel multidimensional projection technique, called Least Square Projection (LSP), that encompasses good features of both linear and nonlinear projection methods."
- PENDING-EXTRA-E8 | page: 3, section: extracted, quote: "In order to achieve high precision with reasonable computation cost for reasonably sized data sets, we present a novel projection technique, called LSP."
