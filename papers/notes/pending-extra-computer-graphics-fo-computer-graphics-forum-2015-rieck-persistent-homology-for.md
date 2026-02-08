---
id: paper-2015-pending-extra-computer-graphics-fo
title: "Persistent Homology for the Evaluation of Dimensionality Reduction Schemes"
authors: "B. Rieck, H. Leitte"
venue: "Computer Graphics Forum"
year: 2015
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/Computer Graphics Forum - 2015 - Rieck - Persistent Homology for the Evaluation of Dimensionality Reduction Schemes.pdf
seed_note_id: "paper-2025-jeon-reliable-va-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- To obtain Rε for our high-dimensional data set D, we choose a distance threshold ε with the help of one of the heuristics described above.Rε serves as an approximation of the connectivity of the data set and is used to calculate persistence diagrams for different functions on the point set.
- Despite the large volume of existing techniques, DR is still an active ﬁeld of research and the set of available methods is ever-increasing to better capture predeﬁned characteristics of the high-dimensional data.
- We use this methodology to robustly analyse the quality of DR algorithms by comparing properties of the high-dimensional point cloud, e.g. its local density, to respective properties in its embedding.
- DR methods provide e.g. a two-dimensional embedding of the abstract data that retains relevant high-dimensional characteristics such as local distances between data points.

# Method Summary
- We use this methodology to robustly analyse the quality of DR algorithms by comparing properties of the high-dimensional point cloud, e.g. its local density, to respective properties in its embedding.
- Our pipeline informs about the best DR technique for a given data set and chosen metric (e.g. preservation of local distances) and provides knowledge about the local quality of an embedding, thereby helping users understand the shortcomings of the selected DR method.
- When two connected components are being matched by the Wasserstein distance calculations, we want to assign each of their vertices the matching cost—this cost represents the error that is being introduced by the corresponding embedding algorithm.
- In a similar vein, Baraniuk and Wakin [BW09] used the JohnsonLindenstrauss lemma [JL84] to develop random projections (RP), a very fast algorithm that projects data points using a random projection matrix.
- Depending on the structure of the input data and the analysis goal, a large variety of methods have been proposed that use very diverse approaches to obtain the low-dimensional representation [LV07].
- As can be seen in the ﬁve embeddings, some algorithms are capable of fulﬁlling this task well (HLLE, t-SNE, and Isomap), while others project locally disjoint data on top of each other (PCA and SPE).
- DR methods provide e.g. a two-dimensional embedding of the abstract data that retains relevant high-dimensional characteristics such as local distances between data points.

# When To Use / Not Use
- Use when:
  - Our pipeline informs about the best DR technique for a given data set and chosen metric (e.g. preservation of local distances) and provides knowledge about the local quality of an embedding, thereby helping users understand the shortcomings of the selected DR method.
  - We use this methodology to robustly analyse the quality of DR algorithms by comparing properties of the high-dimensional point cloud, e.g. its local density, to respective properties in its embedding.
- Avoid when:
  - These frameworks can either be automated [TAE ∗09], or more usercentric [FSJ13, IMI∗10, SMT13].
  - To obtain Rε for our high-dimensional data set D, we choose a distance threshold ε with the help of one of the heuristics described above.Rε serves as an approximation of the connectivity of the data set and is used to calculate persistence diagrams for different functions on the point set.
- Failure modes:
  - It also changes the global structure of the data set— there are no artiﬁcial “holes” in the parameter space; its density should be depicted as being more uniform because of the way the data were created (uniform changes over all three variables, without preferring one over the other).

# Metrics Mentioned
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- It also changes the global structure of the data set— there are no artiﬁcial “holes” in the parameter space; its density should be depicted as being more uniform because of the way the data were created (uniform changes over all three variables, without preferring one over the other).
- This combined visualization of physical space and parameter space enables the user to identify structural anomalies in the parameter setting, i.e. the multivariate simulation variables, and link them to physical locations.
- Concrete compressive strength This data set was originally described by Yeh [Yeh98] in the context of performing a parameter study of the compressive strength of concrete for different cement mixtures.
- We compare MDS, and t-SNE, which we found to perform best, to Isomap with varying neighbourhood parameter k. at increasingly ﬁne resolutions, meteorologists aim to predict changes in world climate.
- This is motivated by a previous analysis [GBPW10] which showed that the parameter space contains numerous linear substructures, making it amenable to regression analysis.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-EXTRA-C1 | stance: support | summary: To obtain Rε for our high-dimensional data set D, we choose a distance threshold ε with the help of one of the heuristics described above.Rε serves as an approximation of the connectivity of the data set and is used to calculate persistence diagrams for different functions on the point set. | evidence_ids: PENDING-EXTRA-E1, PENDING-EXTRA-E2
- CLAIM-PENDING-EXTRA-C2 | stance: support | summary: We use this methodology to robustly analyse the quality of DR algorithms by comparing properties of the high-dimensional point cloud, e.g. its local density, to respective properties in its embedding. | evidence_ids: PENDING-EXTRA-E3, PENDING-EXTRA-E4
- CLAIM-PENDING-EXTRA-C3 | stance: support | summary: It also changes the global structure of the data set— there are no artiﬁcial “holes” in the parameter space; its density should be depicted as being more uniform because of the way the data were created (uniform changes over all three variables, without preferring one over the other). | evidence_ids: PENDING-EXTRA-E5, PENDING-EXTRA-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-EXTRA-E1 | page: 4, section: extracted, quote: "To obtain Rε for our high-dimensional data set D, we choose a distance threshold ε with the help of one of the heuristics described above.Rε serves as an approximation of the connectivity of the data set and is used to calculate persistence diagrams for different functions on the point set."
- PENDING-EXTRA-E2 | page: 1, section: extracted, quote: "Despite the large volume of existing techniques, DR is still an active ﬁeld of research and the set of available methods is ever-increasing to better capture predeﬁned characteristics of the high-dimensional data."
- PENDING-EXTRA-E3 | page: 1, section: extracted, quote: "We use this methodology to robustly analyse the quality of DR algorithms by comparing properties of the high-dimensional point cloud, e.g. its local density, to respective properties in its embedding."
- PENDING-EXTRA-E4 | page: 1, section: extracted, quote: "DR methods provide e.g. a two-dimensional embedding of the abstract data that retains relevant high-dimensional characteristics such as local distances between data points."
- PENDING-EXTRA-E5 | page: 1, section: extracted, quote: "Our pipeline informs about the best DR technique for a given data set and chosen metric (e.g. preservation of local distances) and provides knowledge about the local quality of an embedding, thereby helping users understand the shortcomings of the selected DR method."
- PENDING-EXTRA-E6 | page: 5, section: extracted, quote: "When two connected components are being matched by the Wasserstein distance calculations, we want to assign each of their vertices the matching cost—this cost represents the error that is being introduced by the corresponding embedding algorithm."
- PENDING-EXTRA-E7 | page: 2, section: extracted, quote: "In a similar vein, Baraniuk and Wakin [BW09] used the JohnsonLindenstrauss lemma [JL84] to develop random projections (RP), a very fast algorithm that projects data points using a random projection matrix."
- PENDING-EXTRA-E8 | page: 1, section: extracted, quote: "Depending on the structure of the input data and the analysis goal, a large variety of methods have been proposed that use very diverse approaches to obtain the low-dimensional representation [LV07]."
