---
id: paper-2012-pending-ref-013
title: "High Performance Dimension Reduction and Visualization for Large High-Dimensional Data Analysis"
authors: "D. Engel, L. Hüttenberger, and B. Hamann"
venue: "2010 10th IEEE/ACM International Conference on Cluster, Cloud and Grid Computing"
year: 2012
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-013-2012-a-survey-of-dimension-reduction-methods-for-high-dimensional-data-analysis-and-visual.pdf
seed_note_id: "paper-2021-quantitative-survey-dr-techniques"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- 1998 ACM Subject ClassiﬁcationG.3 Multivariate Statistics, I.2.6 Learning, G.1.2 Approximation Keywordsandphrases high-dimensional, multivariatedata, dimensionreduction, manifoldlearning Digital Object Identiﬁer10.4230/OASIcs.VLUDS.2011.135 1 Introduction Contemporary simulation and experimental data acquisition technologies enable scientists and engineers to generate massive amounts of data.
- MG-MDS, on the other hand, is based on the minimization of the stress function through gradient methods and uses only a weak form of this assumption.6 Hence, for data sets where the convex combination property does not hold, no suitable neighborhood can be found, or when the computation of the neighborhoods is too costly, MG-MDS is better suited to solve the problem.
- 135–149 OpenAccess Series in Informatics Schloss Dagstuhl – Leibniz-Zentrum für Informatik, Dagstuhl Publishing, Germany 136 A Survey of Dimension Reduction Methods for High-dimensional Data Visualization but to provide an overview of basic approaches, as well as to review select state-of-theart methods.
- VLUDS’11 144 A Survey of Dimension Reduction Methods for High-dimensional Data Visualization 3.1 Piecewise Laplacian-based Projection (PLP) Similar to LLE, PLP [19] makes the assumption that every data pointxi can be approximated by a convex combination of its neighborsxj∈Ni based on weightsWi,j.

# Method Summary
- Global approaches ﬁrst learn proximity relationships on a locally low-dimensional sub-manifold and, second, depict these relationships using, for example, projection-based methods like metric MDS.
- 135–149 OpenAccess Series in Informatics Schloss Dagstuhl – Leibniz-Zentrum für Informatik, Dagstuhl Publishing, Germany 136 A Survey of Dimension Reduction Methods for High-dimensional Data Visualization but to provide an overview of basic approaches, as well as to review select state-of-theart methods.
- VLUDS’11 144 A Survey of Dimension Reduction Methods for High-dimensional Data Visualization 3.1 Piecewise Laplacian-based Projection (PLP) Similar to LLE, PLP [19] makes the assumption that every data pointxi can be approximated by a convex combination of its neighborsxj∈Ni based on weightsWi,j.
- The basic idea is to re-state the problem of ﬁnding φ = arg minφε (φ(X); ∆,W ) with respect to the gradient-descent-type method as a problem of ﬁndingφ with∇ε ( φ(X); ∆,W ) = 0 and to embed this problem into a multigrid approach, through which substantial performance improvements can be achieved.
- 2.1 Projection-based Methods Projective techniques display multi-dimensional data by projecting points onto a lowerdimensional space such that distance relationships between points in the projection space reﬂect speciﬁc relationships between the data points in multi-dimensional space.
- Methods that are solely based on linear inner product transformations are deﬁned as projection techniques, while those that are able to ascertain distance relationships in a non-linear data structure are deﬁned as manifold learning techniques.
- We deﬁne VLUDS’11 138 A Survey of Dimension Reduction Methods for High-dimensional Data Visualization a projection by the use of a projection in the geometric sense - projecting the data based on a (linear) inner product transformation.

# When To Use / Not Use
- Use when:
  - An approach to avoid this is to use higherlevel, gradient-descent-type methods, for example, Newton’s methods [12].
  - MG-MDS, on the other hand, is based on the minimization of the stress function through gradient methods and uses only a weak form of this assumption.6 Hence, for data sets where the convex combination property does not hold, no suitable neighborhood can be found, or when the computation of the neighborhoods is too costly, MG-MDS is better suited to solve the problem.
- Avoid when:
  - Since human perception (and output devices) is limited to three-dimensional space, the challenge of visualizing multivariate data is converting the data to a space of lower dimensionality that is depictable and comprehensible to the user while preserving as much information as possible.
  - Our aim is not to be exhaustive ∗ This work was supported by the German Science Foundation (DFG). © Daniel Engel, Lars Hüttenberger, and Bernd Hamann; licensed under Creative Commons License ND Proceedings of IRTG 1131 – Visualization of Large and Unstructured Data Sets Workshop 2011.
- Failure modes:
  - After the local linear systems have been solved for each sample, the user can interact with the projected data set through its representation as a k-nearest neighbor graph and adjust neighborhoods or samples by simply moving data points within the embedding.

# Metrics Mentioned
- `stress`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- 3.2 Multigrid Multidimensional Scaling (MG-MDS) As a variant of multidimensional scaling, MG-MDS [3] is based on the direct optimization of the weighted mapping error as a stress functionεφ given by (2), although, the method 4 Note that√n is an upper bound for the number of groups in a data set of sizen [18].
- Although the projection step ﬁnds the global optimum for the embedding, the initial retrieval of distance relationships is based on optimization problems such as shortest path problems, least squares ﬁts, or semideﬁnite programming.
- For this, MG-MDS was chosen as a representative over numerous other state-of-the-art methods that followthestressoptimizationapproach, becauseitsuniqueadvantagesarealsorestrictedtothe input being metric dissimilarities.
- While LLE ﬁnds those weights through optimization, PLP uses pre-deﬁned weights according to: Wi,j = 1 δm(xi,xj) / ∑ xk∈Ni 1 δm(xi,xk) (10) with δm being the metric distance function of the data space.
- A comparison between them is diﬃcult because stress optimization solves the much harder problem of embedding non-metric distance relationships, while spectral methods are restricted to metric ones.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-013-C1 | stance: support | summary: 1998 ACM Subject ClassiﬁcationG.3 Multivariate Statistics, I.2.6 Learning, G.1.2 Approximation Keywordsandphrases high-dimensional, multivariatedata, dimensionreduction, manifoldlearning Digital Object Identiﬁer10.4230/OASIcs.VLUDS.2011.135 1 Introduction Contemporary simulation and experimental data acquisition technologies enable scientists and engineers to generate massive amounts of data. | evidence_ids: PENDING-REF-013-E1, PENDING-REF-013-E2
- CLAIM-PENDING-REF-013-C2 | stance: support | summary: Global approaches ﬁrst learn proximity relationships on a locally low-dimensional sub-manifold and, second, depict these relationships using, for example, projection-based methods like metric MDS. | evidence_ids: PENDING-REF-013-E3, PENDING-REF-013-E4
- CLAIM-PENDING-REF-013-C3 | stance: support | summary: 3.2 Multigrid Multidimensional Scaling (MG-MDS) As a variant of multidimensional scaling, MG-MDS [3] is based on the direct optimization of the weighted mapping error as a stress functionεφ given by (2), although, the method 4 Note that√n is an upper bound for the number of groups in a data set of sizen [18]. | evidence_ids: PENDING-REF-013-E5, PENDING-REF-013-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 4 | relevance: high | note: contains initialization sensitivity or control-policy evidence

# Evidence
- PENDING-REF-013-E1 | page: 1, section: extracted, quote: "1998 ACM Subject ClassiﬁcationG.3 Multivariate Statistics, I.2.6 Learning, G.1.2 Approximation Keywordsandphrases high-dimensional, multivariatedata, dimensionreduction, manifoldlearning Digital Object Identiﬁer10.4230/OASIcs.VLUDS.2011.135 1 Introduction Contemporary simulation and experimental data acquisition technologies enable scientists and engineers to generate massive amounts of data."
- PENDING-REF-013-E2 | page: 12, section: extracted, quote: "MG-MDS, on the other hand, is based on the minimization of the stress function through gradient methods and uses only a weak form of this assumption.6 Hence, for data sets where the convex combination property does not hold, no suitable neighborhood can be found, or when the computation of the neighborhoods is too costly, MG-MDS is better suited to solve the problem."
- PENDING-REF-013-E3 | page: 1, section: extracted, quote: "135–149 OpenAccess Series in Informatics Schloss Dagstuhl – Leibniz-Zentrum für Informatik, Dagstuhl Publishing, Germany 136 A Survey of Dimension Reduction Methods for High-dimensional Data Visualization but to provide an overview of basic approaches, as well as to review select state-of-theart methods."
- PENDING-REF-013-E4 | page: 1, section: extracted, quote: "VLUDS’11 144 A Survey of Dimension Reduction Methods for High-dimensional Data Visualization 3.1 Piecewise Laplacian-based Projection (PLP) Similar to LLE, PLP [19] makes the assumption that every data pointxi can be approximated by a convex combination of its neighborsxj∈Ni based on weightsWi,j."
- PENDING-REF-013-E5 | page: 7, section: extracted, quote: "Global approaches ﬁrst learn proximity relationships on a locally low-dimensional sub-manifold and, second, depict these relationships using, for example, projection-based methods like metric MDS."
- PENDING-REF-013-E6 | page: 11, section: extracted, quote: "The basic idea is to re-state the problem of ﬁnding φ = arg minφε (φ(X); ∆,W ) with respect to the gradient-descent-type method as a problem of ﬁndingφ with∇ε ( φ(X); ∆,W ) = 0 and to embed this problem into a multigrid approach, through which substantial performance improvements can be achieved."
- PENDING-REF-013-E7 | page: 3, section: extracted, quote: "2.1 Projection-based Methods Projective techniques display multi-dimensional data by projecting points onto a lowerdimensional space such that distance relationships between points in the projection space reﬂect speciﬁc relationships between the data points in multi-dimensional space."
- PENDING-REF-013-E8 | page: 3, section: extracted, quote: "Methods that are solely based on linear inner product transformations are deﬁned as projection techniques, while those that are able to ascertain distance relationships in a non-linear data structure are deﬁned as manifold learning techniques."
