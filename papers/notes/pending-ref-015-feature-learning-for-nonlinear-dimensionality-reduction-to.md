---
id: paper-2023-pending-ref-015
title: "Feature Learning for Nonlinear Dimensionality Reduction toward Maximal Extraction of Hidden Patterns"
authors: "Takanori Fujiwara, Yun-Hsin Kuo, Anders Ynnerman, and Kwan-Liu Ma"
venue: "2023 IEEE 16th Pacific Visualization Symposium (PacificVis)"
year: 2023
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-015-2023-feature-learning-for-nonlinear-dimensionality-reduction-toward-maximal-extraction-of.pdf
seed_note_id: "paper-2023-zadu-library"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- Feature Learning for Nonlinear Dimensionality Reduction toward Maximal Extraction of Hidden Patterns Takanori Fujiwara* Link¨oping University Yun-Hsin Kuo† University of California, Davis Anders Ynnerman* Link¨oping University Kwan-Liu Ma† University of California, Davis ABSTRACT Dimensionality reduction (DR) plays a vital role in the visual analysis of high-dimensional data.
- 4.1 Problem Scope FEALM aims to supplement nonlinear DR methods, even more speciﬁcally, for those construct agraph-based data representation as their intermediate product or those generate DR results highly related to a graph-based data representation.
- With a set of already produced graphs, Gi ={G0,··· ,Gi}, we can write a relaxed version of the optimization problem: argmax Pi+1 Φ(dGr(Gi+1,G0),··· ,dGr(Gi+1,Gi)). (2) When developing a method within FEALM, we can choose Eq.
- 8-c (left), large weights are assigned to CC20.440b (racial problems), CC20.443.1, CC20.443.2, and CC20.443.5 (legislature’s money use on welfare, healthcare, and transportation/infrastructure, respectively).

# Method Summary
- We develop an algorithm utilizing the Nelder-Mead optimization method (NMM) [13] to ﬁnd latent features to produce maximally different nearest-neighbor graphs, which are intermediate products of UMAP, and consequently generate diverse UMAP results.
- In addition to the same settings above, we set m′=2, no constraint on a projection matrix, and 1000 as the number of objective function evaluations.
- When only performing a linear projection [6], a DR method is categorized as linear DR.
- For example, PCA and LDA are frequently used in data preprocessing for subsequent machine learning (ML) methods, such as deep neural networks or even other DR methods (e.g., t-SNE), as reducing dimensions is helpful to avoid high computational costs and the curse of dimensionality.
- 6-d, the UI integrates an existing contrastive-learningbased interpretation method, called ccPCA, and the heatmap-based visualization [10]. ccPCA contrasts a target group with a background group to reveal highly-contributed attributes to the characteristics of the target.
- This is because the separation visible in the DR result should be highly related to the projection matrix, the differences should be captured in the attributes’ contributions, and the attributes’ contributions should reﬂect the attribute value distribution.
- 4.1 Problem Scope FEALM aims to supplement nonlinear DR methods, even more speciﬁcally, for those construct agraph-based data representation as their intermediate product or those generate DR results highly related to a graph-based data representation.

# When To Use / Not Use
- Use when:
  - For example, PCA and LDA are frequently used in data preprocessing for subsequent machine learning (ML) methods, such as deep neural networks or even other DR methods (e.g., t-SNE), as reducing dimensions is helpful to avoid high computational costs and the curse of dimensionality.
  - Then, after the user-indicated number of evaluations or the convergence, the NMM returns the best solution so far as a ﬁnal result.
- Avoid when:
  - With this, we can ﬁnd a DR result that is different from all the existing results and avoid a case where the optimization keeps producing the same or similar results (e.g., a case where Y0 has an extremely larger dissimilarity with Y1 than with other potential DR results).
  - 2 is generated with NSD, here we use NetLSD (a) and the neighbor dissimilarity (b). time complexity is O(qkn + q2n), where q is the total number of the top and bottom eigenvalues to take for the approximation andk is the number of neighbors set to generate an k-NN graph.
- Failure modes:
  - Then, we deﬁne the dissimilarity measured by NSD as: dNSD(Gi,G j) = dND(Gi,G j)β· log ( 1 + dSD(Gi,G j) ) (4) where dNSD(Gi,G j)≥ 0 and β (0≤ β≤ ∞) is a hyperparameter that controls how strongly NSD focuses on the neighbor dissimilarity vs. the shape dissimilarity.

# Metrics Mentioned
- `procrustes-based quality`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- This can be achieved by replacing a linear projection matrix with hyperparameters for the optimization’s search parameters.
- Then, we deﬁne the dissimilarity measured by NSD as: dNSD(Gi,G j) = dND(Gi,G j)β· log ( 1 + dSD(Gi,G j) ) (4) where dNSD(Gi,G j)≥ 0 and β (0≤ β≤ ∞) is a hyperparameter that controls how strongly NSD focuses on the neighbor dissimilarity vs. the shape dissimilarity.
- The optimization by the ordinary NMM begins with initial(p +1) solutions in a p-dimensional space, where p is the number of parameters (i.e., when only allowing data scaling, p = m; for the other cases, p = m× m′).
- Random initialization of solutions and restriction of their movement on a speciﬁed manifold (e.g., the Grassmann manifold) can be easily achieved by utilizing the manifold optimization libraries [38].
- Also, hyperparameter adjustments of UMAP, such ask used for the k-nearest neighbor (k-NN) graph construction, cannot solve this issue as the manifold itself is distorted (for details, refer to [1]).
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-015-C1 | stance: support | summary: Feature Learning for Nonlinear Dimensionality Reduction toward Maximal Extraction of Hidden Patterns Takanori Fujiwara* Link¨oping University Yun-Hsin Kuo† University of California, Davis Anders Ynnerman* Link¨oping University Kwan-Liu Ma† University of California, Davis ABSTRACT Dimensionality reduction (DR) plays a vital role in the visual analysis of high-dimensional data. | evidence_ids: PENDING-REF-015-E1, PENDING-REF-015-E2
- CLAIM-PENDING-REF-015-C2 | stance: support | summary: We develop an algorithm utilizing the Nelder-Mead optimization method (NMM) [13] to ﬁnd latent features to produce maximally different nearest-neighbor graphs, which are intermediate products of UMAP, and consequently generate diverse UMAP results. | evidence_ids: PENDING-REF-015-E3, PENDING-REF-015-E4
- CLAIM-PENDING-REF-015-C3 | stance: support | summary: This can be achieved by replacing a linear projection matrix with hyperparameters for the optimization’s search parameters. | evidence_ids: PENDING-REF-015-E5, PENDING-REF-015-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 4 | relevance: high | note: contains initialization sensitivity or control-policy evidence

# Evidence
- PENDING-REF-015-E1 | page: 1, section: extracted, quote: "Feature Learning for Nonlinear Dimensionality Reduction toward Maximal Extraction of Hidden Patterns Takanori Fujiwara* Link¨oping University Yun-Hsin Kuo† University of California, Davis Anders Ynnerman* Link¨oping University Kwan-Liu Ma† University of California, Davis ABSTRACT Dimensionality reduction (DR) plays a vital role in the visual analysis of high-dimensional data."
- PENDING-REF-015-E2 | page: 3, section: extracted, quote: "4.1 Problem Scope FEALM aims to supplement nonlinear DR methods, even more speciﬁcally, for those construct agraph-based data representation as their intermediate product or those generate DR results highly related to a graph-based data representation."
- PENDING-REF-015-E3 | page: 4, section: extracted, quote: "With a set of already produced graphs, Gi ={G0,··· ,Gi}, we can write a relaxed version of the optimization problem: argmax Pi+1 Φ(dGr(Gi+1,G0),··· ,dGr(Gi+1,Gi)). (2) When developing a method within FEALM, we can choose Eq."
- PENDING-REF-015-E4 | page: 9, section: extracted, quote: "8-c (left), large weights are assigned to CC20.440b (racial problems), CC20.443.1, CC20.443.2, and CC20.443.5 (legislature’s money use on welfare, healthcare, and transportation/infrastructure, respectively)."
- PENDING-REF-015-E5 | page: 1, section: extracted, quote: "We develop an algorithm utilizing the Nelder-Mead optimization method (NMM) [13] to ﬁnd latent features to produce maximally different nearest-neighbor graphs, which are intermediate products of UMAP, and consequently generate diverse UMAP results."
- PENDING-REF-015-E6 | page: 6, section: extracted, quote: "In addition to the same settings above, we set m′=2, no constraint on a projection matrix, and 1000 as the number of objective function evaluations."
- PENDING-REF-015-E7 | page: 1, section: extracted, quote: "When only performing a linear projection [6], a DR method is categorized as linear DR."
- PENDING-REF-015-E8 | page: 2, section: extracted, quote: "For example, PCA and LDA are frequently used in data preprocessing for subsequent machine learning (ML) methods, such as deep neural networks or even other DR methods (e.g., t-SNE), as reducing dimensions is helpful to avoid high computational costs and the curse of dimensionality."
