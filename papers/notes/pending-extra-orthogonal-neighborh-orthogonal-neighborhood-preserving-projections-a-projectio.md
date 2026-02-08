---
id: paper-2026-pending-extra-orthogonal-neighborh
title: "Orthogonal Neighborhood Preserving Projections: A Projection-Based Dimensionality Reduction Technique"
authors: "E. Kokiopoulou, Y. Saad"
venue: "IEEE Transactions on Pattern Analysis and Machine Intelligence"
year: 2007
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/Orthogonal_Neighborhood_Preserving_Projections_A_Projection-Based_Dimensionality_Reduction_Technique.pdf
seed_note_id: "paper-2015-gisbrecht-nonlinear-dr-visualization"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- Specifically, it is difficult to capture the local (as well as global) geometry of a complex data set in high-dimensional spaces.
- The projected data in reduced space is Y ¼ V >/C8ðXÞ¼ Z>Q>/C8ðXÞ¼ Z>Q>QR ¼ Z>R: ð26Þ In this case, the objective function (21) becomes Fð Y Þ¼ tr Z>RðI /C0 W >ÞðI /C0 W ÞR>Z /C2/C3 ¼ tr½Z>RMR >Z/C138 : ð27Þ As a result, the columns z of the optimal Z are just the set of eigenvectors of the problem RðI /C0 W >ÞðI /C0 W ÞR>/C2/C3 z ¼ /C21z ð28Þ associated with the smallest d eigenvalues.
- Denoting by XðiÞ a system of vectors consisting of xi and its neighbors, we need to solve the least squares ðXðiÞ /C0 xie>Þwi;: ¼ 0 subject to the constraint e>wi;: ¼ 1.I t can be shown that the solution wi;: of this constrained least squares problem is given by the following [1], which involves the inverse of G: wi;: ¼ G/C0 1e e>G/C0 1e : ð9Þ Recall that e is the vector of all 1s.
- In fact, recalling (26), we observe that (27) is simply trðYM Y >Þ, and minimizing this trace subject to the conditionZ>Z ¼ I is equivalent to solving min Y 2R m/C2 d YK /C0 1 Y > ¼I tr½YM Y >/C138 : ð32Þ Recalling also the LLE problem in Section 3.3, this shows that in effect, the kernel ONPP is mathematically equivalent to LLE with the K/C0 1 inner product.

# Method Summary
- In particular, we propose a method, named Orthogonal Neighborhood Preserving Projections, which works by first building an “affinity” graph for the data in a way that is similar to the method of Locally Linear Embedding (LLE).
- However, the orthogonal methods, that is, OLPP and ONPP, preserve global geometric characteristics as well, since they give faithful projections, which convey information about how the manifold is folded in the highdimensional space.
- In this case, the set V is the eigenbasis associated with the lowest eigenvalues of the matrix Clpp ¼ XðD /C0 W ÞX>: ð5Þ We refer to this first option as the method of Orthogonal Locality Perserving Projections (OLPP).
- Then, the ONPP algorithm is performed and the total dimensionality reduction matrix is given by V ¼ V PCAVONPP; KOKIOPOULOU AND SAAD: ORTHOGONAL NEIGHBORHOOD PRESERVING PROJECTIONS: A PROJECTION-BASED...
- The proposed method, named Orthogonal Neighborhood Preserving Projections (ONPP) [3], projects the high-dimensional data samples on a lower dimensional space by means of a linear transformation V .
- On the other hand, observe that all the four graph-based methods yield more meaningful projections, since samples of the same class are mapped close to each other.
- Two-dimensional projections of digits by using four related methods, where “+” denotes 0, “x” denotes 1, “o” denotes 2, “ 4” denotes 3, and “ tu” denotes 4.

# When To Use / Not Use
- Use when:
  - Orthogonal Neighborhood Preserving Projections: A Projection-Based Dimensionality Reduction Technique Effrosyni Kokiopoulou, Student Member , IEEE, and Yousef Saad Abstract—This paper considers the problem of dimensionality reduction by orthogonal projection techniques.
  - However, our algorithm uses the optimal data-driven weights of LLE, which reflect the intrinsic geometry of the local neighborhoods, whereas the uniform weights (0/1) used in LPP aim at preserving locality without explicit consideration to the local geometric structure.
- Avoid when:
  - In particular, we propose a method, named Orthogonal Neighborhood Preserving Projections, which works by first building an “affinity” graph for the data in a way that is similar to the method of Locally Linear Embedding (LLE).
  - It is useful to point out that determining the wijs for a given point xi is a local calculation in the sense that it only KOKIOPOULOU AND SAAD: ORTHOGONAL NEIGHBORHOOD PRESERVING PROJECTIONS: A PROJECTION-BASED...
- Failure modes:
  - We used three data sets, which are publicly available: University of Manchester Institute of Science and Technology (UMIST) [13], ORL (formerly Olivetti Research Ltd.) [14], and Aleix Face Recognition (AR) [15].

# Metrics Mentioned
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- The two optimization problems are shown as follows: LLE : min Y 2Rn/C2 d ;YY > ¼I tr½YM Y >/C138 ; ONPP : min Y ¼V > X;V 2Rm/C2 d ;V > V ¼I tr½YM Y >/C138 : However, another point of view is to think in terms of null spaces or approximate null spaces of the matrix I /C0 W >.
- Although Gaussian weights can be used in LPP, these are somewhat artificial and require the selection of an appropriate value of the parameter /C27, which is the width of the Gaussian envelope.
- Note that with the supervised construction of the affinity graph, the parameter k need not be determined by the user since it is set automatically to be the cardinality of each class.
- Usually, the property that is preserved is quantified by an objective function and the dimensionality reduction pr oblem is formulated as an optimization problem.
- Notice that, in this case, one does not need to set the parameter k, which is the number of NNs and the method becomes fully automatic.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-EXTRA-C1 | stance: support | summary: Specifically, it is difficult to capture the local (as well as global) geometry of a complex data set in high-dimensional spaces. | evidence_ids: PENDING-EXTRA-E1, PENDING-EXTRA-E2
- CLAIM-PENDING-EXTRA-C2 | stance: support | summary: In particular, we propose a method, named Orthogonal Neighborhood Preserving Projections, which works by first building an “affinity” graph for the data in a way that is similar to the method of Locally Linear Embedding (LLE). | evidence_ids: PENDING-EXTRA-E3, PENDING-EXTRA-E4
- CLAIM-PENDING-EXTRA-C3 | stance: support | summary: The two optimization problems are shown as follows: LLE : min Y 2Rn/C2 d ;YY > ¼I tr½YM Y >/C138 ; ONPP : min Y ¼V > X;V 2Rm/C2 d ;V > V ¼I tr½YM Y >/C138 : However, another point of view is to think in terms of null spaces or approximate null spaces of the matrix I /C0 W >. | evidence_ids: PENDING-EXTRA-E5, PENDING-EXTRA-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-EXTRA-E1 | page: 12, section: extracted, quote: "Specifically, it is difficult to capture the local (as well as global) geometry of a complex data set in high-dimensional spaces."
- PENDING-EXTRA-E2 | page: 7, section: extracted, quote: "The projected data in reduced space is Y ¼ V >/C8ðXÞ¼ Z>Q>/C8ðXÞ¼ Z>Q>QR ¼ Z>R: ð26Þ In this case, the objective function (21) becomes Fð Y Þ¼ tr Z>RðI /C0 W >ÞðI /C0 W ÞR>Z /C2/C3 ¼ tr½Z>RMR >Z/C138 : ð27Þ As a result, the columns z of the optimal Z are just the set of eigenvectors of the problem RðI /C0 W >ÞðI /C0 W ÞR>/C2/C3 z ¼ /C21z ð28Þ associated with the smallest d eigenvalues."
- PENDING-EXTRA-E3 | page: 4, section: extracted, quote: "Denoting by XðiÞ a system of vectors consisting of xi and its neighbors, we need to solve the least squares ðXðiÞ /C0 xie>Þwi;: ¼ 0 subject to the constraint e>wi;: ¼ 1.I t can be shown that the solution wi;: of this constrained least squares problem is given by the following [1], which involves the inverse of G: wi;: ¼ G/C0 1e e>G/C0 1e : ð9Þ Recall that e is the vector of all 1s."
- PENDING-EXTRA-E4 | page: 7, section: extracted, quote: "In fact, recalling (26), we observe that (27) is simply trðYM Y >Þ, and minimizing this trace subject to the conditionZ>Z ¼ I is equivalent to solving min Y 2R m/C2 d YK /C0 1 Y > ¼I tr½YM Y >/C138 : ð32Þ Recalling also the LLE problem in Section 3.3, this shows that in effect, the kernel ONPP is mathematically equivalent to LLE with the K/C0 1 inner product."
- PENDING-EXTRA-E5 | page: 1, section: extracted, quote: "In particular, we propose a method, named Orthogonal Neighborhood Preserving Projections, which works by first building an “affinity” graph for the data in a way that is similar to the method of Locally Linear Embedding (LLE)."
- PENDING-EXTRA-E6 | page: 8, section: extracted, quote: "However, the orthogonal methods, that is, OLPP and ONPP, preserve global geometric characteristics as well, since they give faithful projections, which convey information about how the manifold is folded in the highdimensional space."
- PENDING-EXTRA-E7 | page: 3, section: extracted, quote: "In this case, the set V is the eigenbasis associated with the lowest eigenvalues of the matrix Clpp ¼ XðD /C0 W ÞX>: ð5Þ We refer to this first option as the method of Orthogonal Locality Perserving Projections (OLPP)."
- PENDING-EXTRA-E8 | page: 5, section: extracted, quote: "Then, the ONPP algorithm is performed and the total dimensionality reduction matrix is given by V ¼ V PCAVONPP; KOKIOPOULOU AND SAAD: ORTHOGONAL NEIGHBORHOOD PRESERVING PROJECTIONS: A PROJECTION-BASED..."
