---
id: paper-2011-zadu-ref-08
title: "Local Affine Multidimensional Projection"
authors: "theory to build accurate local transformations that can be dynamically modiﬁed according to user knowledge. The accuracy , ﬂexibility"
venue: "IEEE Transactions on Visualization and Computer Graphics"
year: 2011
tags: [dr, zadu-table1-reference, ivm, proc, stress, tnc]
source_pdf: papers/raw/zadu-table1-references/Local_Affine_Multidimensional_Projection (1).pdf
evidence_level: medium
updated_at: 2026-02-08
---
# Problem
- Given an instance x, the Local Afﬁne Multidimensional Projection technique maps x to the visual space by ﬁnding the best afﬁne transformation fx(p)= pM + t that minimizes ∑ i αi∥ fx(xi)−yi∥2, subject to MT M = I (1) where matrix M and vector t are the unknowns, I is the identity matrix, and αi are scalar weights deﬁned as: αi = 1 ∥xi−x∥2 (2) The minimization problem (1) is similar to that employed in “asrigid-as-possible” image deformation [30].
- The minimization problem (4) can be expressed in matricial form ∥AM−B∥F, subject to MT M = I (5) where ∥·∥ F denotes the Frobenius norm and matrices A and B are given by A = ⎡ ⎢⎢⎣ √α1 ˆx1√α2 ˆx2 .. .√ αk ˆxk ⎤ ⎥⎥⎦, B = ⎡ ⎢⎢⎣ √α1 ˆy1√α2 ˆy2 .. .√ αk ˆyk ⎤ ⎥⎥⎦ (6) Fig.
- We refer the interested reader to the book by Gower and Dijksterhuis [17], which provides a detailed discussion on how orthogonality and other more general constraints affect the outcome of minimization problems as the one stated in (1).
- 5U SER -ASSISTED DATA CORRELATION AND GROUPING Incorporating user knowledge into the mapping by dynamically interacting with projected data is a useful functionality that can be exploited in many data visualization problems.
- The minimization problem (5) is a typical example of the so called Orthogonal Procrustes Problem [17], whose solution is known to be M = UV, AT B = UD V (7) where UD V is the singular value decomposition (SVD) of AT B.

# Method Summary
- Good examples of global methods are techniques based on spectral decomposition, which compute the embedding coordinates for each data instance from eigenvectors of a transformation applied to a dissimilarity matrix (symmetric matrix containing the distance between each pair of instances) [34].
- Least Squares Projection [25] (LSP) is a two-step global technique that also uses a non-linear scheme to ﬁrst position a subset of the samples in the visual space, mapping the remaining instances through a Laplacian-like operator, resulting anO(k2 +n2) algorithm.
- One of the main reasons for such a lack of ﬂexibility is that existing local methods accomplish the multidimensional projection based on a subset of samples a priori positioned in the visual space and the number of samples required is typically high.
- Although more efﬁcient than other optimization-based methods, Pekalska’s approach is not ﬂexible enough to support interactive applications while still requiring a minimum number of sample points equivalent to the dimension of the data.
- Local methods make use of two main ingredients to perform the multidimensional projection, namely, the neighborhood information of each data instance and the location of a subset of samples a priori positioned in the visual space.
- First proposed by Kruskal [21], nonlinear-optimization-based techniques comprise the class of global methods that accomplish the mapping to visual space by ﬁnding a minimum for an energy function, usually called stress function.
- [27] proposed a technique that ﬁrst embeds a subset of samples in the visual space by optimizing a stress function and then places the remaining instances using a global linear mapping, resulting in an O(k 3 + kn) algorithm.

# When To Use / Not Use
- Use when:
  - Notice that the Silh coefﬁcient increases consistently when 75%, 50%, 25%, and 10% of the nearest control points are used by LAMP to build the mappings, reaching a silhouette value higher than the three other global methods.
  - The use of 2D information renders LAMP highly sensitive to the position of control points in the visual space, producing mappings that follow the layout of the control points very closely.
  - The same limitation can be observed in the recent linear mapping called PLMP [26] (whose complexity is linear), which also makes use of a subset of samples to deﬁne a global linear map.
- Avoid when:
  - Therefore, when pictures of houses are taken to form a slide show, classic music mapped in their neighborhood are automatically selected to compose the soundtrack.
  - However, the situation changes when LAMP makes use of the nearest control points of x to build the mapping fx, as shown in Figures 8(a) to 8(d).
- Failure modes:
  - Although such a sensitivity to the difference in scale is not a serious limitation, it is worth to heed the scales when implementing LAMP.
  - To the best of our knowledge, orthogonal mapping theory has never been used in the context of multidimensional projection.

# Metrics Mentioned
- `nh`: label-based neighborhood hit.
- `nd`: neighbor-shape dissimilarity or neighbor distortion.
- `pr`: pairwise-distance correlation behavior.
- `ivm`: internal clustering validation behavior.
- `proc`: Procrustes local shape agreement.
- `stress`: stress-based distance distortion.
- `sn_stress`: scale-normalized stress.

# Implementation Notes
- However, A T B is indeed a m× 2 matrix (only two columns), so it can be decomposed very quickly with compact SVD packages [2] ( O(k) operations), resulting in an algorithm with computational complexity equal to O(kn).
- The same limitation can be observed in the recent linear mapping called PLMP [26] (whose complexity is linear), which also makes use of a subset of samples to deﬁne a global linear map.
- In our experiments we notice that more “pleasant” layouts are produced when the control points x i and their image yi are in the same scale.
- Although such a sensitivity to the difference in scale is not a serious limitation, it is worth to heed the scales when implementing LAMP.
- Multiscale matrix representation was employed by Belkin and Niyogii [1] and Koren et al.
- ACE: A fast multiscale eigenvectors computation for drawing huge graphs.
- Keep preprocessing, initialization policy, and random-seed protocol fixed when comparing methods.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PAPER2011ZADUREF08-C1 | stance: support | summary: Given an instance x, the Local Afﬁne Multidimensional Projection technique maps x to the visual space by ﬁnding the best afﬁne transformation fx(p)= pM + t that minimizes ∑ i αi∥ fx(xi)−yi∥2, subject to MT M = I (1) where matrix M and vector t are the unknowns, I is the identity matrix, and αi are scalar weights deﬁned as: αi = 1 ∥xi−x∥2 (2) The minimization problem (1) is similar to that employed in “asrigid-as-possible” image deformation [30]. | evidence_ids: PAPER2011ZADUREF08-E1, PAPER2011ZADUREF08-E2
- CLAIM-PAPER2011ZADUREF08-C2 | stance: support | summary: Good examples of global methods are techniques based on spectral decomposition, which compute the embedding coordinates for each data instance from eigenvectors of a transformation applied to a dissimilarity matrix (symmetric matrix containing the distance between each pair of instances) [34]. | evidence_ids: PAPER2011ZADUREF08-E3, PAPER2011ZADUREF08-E4
- CLAIM-PAPER2011ZADUREF08-C3 | stance: support | summary: However, A T B is indeed a m× 2 matrix (only two columns), so it can be decomposed very quickly with compact SVD packages [2] ( O(k) operations), resulting in an algorithm with computational complexity equal to O(kn). | evidence_ids: PAPER2011ZADUREF08-E5, PAPER2011ZADUREF08-E6
- CLAIM-METRIC-IVM-SOURCE-08 | stance: support | summary: This source includes evidence relevant to `ivm` in dimensionality-reduction reliability evaluation. | evidence_ids: PAPER2011ZADUREF08-E1, PAPER2011ZADUREF08-E2
- CLAIM-METRIC-PROC-SOURCE-08 | stance: support | summary: This source includes evidence relevant to `proc` in dimensionality-reduction reliability evaluation. | evidence_ids: PAPER2011ZADUREF08-E1, PAPER2011ZADUREF08-E2
- CLAIM-METRIC-STRESS-SOURCE-08 | stance: support | summary: This source includes evidence relevant to `stress` in dimensionality-reduction reliability evaluation. | evidence_ids: PAPER2011ZADUREF08-E1, PAPER2011ZADUREF08-E2
- CLAIM-METRIC-TNC-SOURCE-08 | stance: support | summary: This source includes evidence relevant to `tnc` in dimensionality-reduction reliability evaluation. | evidence_ids: PAPER2011ZADUREF08-E1, PAPER2011ZADUREF08-E2

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports task clarification before model selection
- step: 2 | relevance: medium | note: adds constraints for preprocessing and data-audit checks
- step: 3 | relevance: high | note: directly informs task-aligned technique/metric selection
- step: 6 | relevance: high | note: adds hyperparameter sensitivity or optimization guidance
- step: 7 | relevance: high | note: supports visualization interpretation and user explanation

# Evidence
- PAPER2011ZADUREF08-E1 | page: 3, section: extracted, quote: "Given an instance x, the Local Afﬁne Multidimensional Projection technique maps x to the visual space by ﬁnding the best afﬁne transformation fx(p)= pM + t that minimizes ∑ i αi∥ fx(xi)−yi∥2, subject to MT M = I (1) where matrix M and vector t are the unknowns, I is the identity matrix, and αi are scalar weights deﬁned as: αi = 1 ∥xi−x∥2 (2) The minimization problem (1) is similar to that employed in “asrigid-as-possible” image deformation [30]."
- PAPER2011ZADUREF08-E2 | page: 3, section: extracted, quote: "The minimization problem (4) can be expressed in matricial form ∥AM−B∥F, subject to MT M = I (5) where ∥·∥ F denotes the Frobenius norm and matrices A and B are given by A = ⎡ ⎢⎢⎣ √α1 ˆx1√α2 ˆx2 .. .√ αk ˆxk ⎤ ⎥⎥⎦, B = ⎡ ⎢⎢⎣ √α1 ˆy1√α2 ˆy2 .. .√ αk ˆyk ⎤ ⎥⎥⎦ (6) Fig."
- PAPER2011ZADUREF08-E3 | page: 3, section: extracted, quote: "We refer the interested reader to the book by Gower and Dijksterhuis [17], which provides a detailed discussion on how orthogonality and other more general constraints affect the outcome of minimization problems as the one stated in (1)."
- PAPER2011ZADUREF08-E4 | page: 7, section: extracted, quote: "5U SER -ASSISTED DATA CORRELATION AND GROUPING Incorporating user knowledge into the mapping by dynamically interacting with projected data is a useful functionality that can be exploited in many data visualization problems."
- PAPER2011ZADUREF08-E5 | page: 3, section: extracted, quote: "The minimization problem (5) is a typical example of the so called Orthogonal Procrustes Problem [17], whose solution is known to be M = UV, AT B = UD V (7) where UD V is the singular value decomposition (SVD) of AT B."
- PAPER2011ZADUREF08-E6 | page: 7, section: extracted, quote: "6D ISCUSSION AND LIMITATIONS The comparisons presented in Section 4 clearly show the effectiveness of the LAMP technique, surpassing, in requisites such as accuracy, robustness, and ﬂexibility, state-of-art methods."
- PAPER2011ZADUREF08-E7 | page: 2, section: extracted, quote: "Good examples of global methods are techniques based on spectral decomposition, which compute the embedding coordinates for each data instance from eigenvectors of a transformation applied to a dissimilarity matrix (symmetric matrix containing the distance between each pair of instances) [34]."
- PAPER2011ZADUREF08-E8 | page: 2, section: extracted, quote: "Least Squares Projection [25] (LSP) is a two-step global technique that also uses a non-linear scheme to ﬁrst position a subset of the samples in the visual space, mapping the remaining instances through a Laplacian-like operator, resulting anO(k2 +n2) algorithm."
- PAPER2011ZADUREF08-E9 | page: 1, section: extracted, quote: "One of the main reasons for such a lack of ﬂexibility is that existing local methods accomplish the multidimensional projection based on a subset of samples a priori positioned in the visual space and the number of samples required is typically high."
- PAPER2011ZADUREF08-E10 | page: 2, section: extracted, quote: "Although more efﬁcient than other optimization-based methods, Pekalska’s approach is not ﬂexible enough to support interactive applications while still requiring a minimum number of sample points equivalent to the dimension of the data."
- PAPER2011ZADUREF08-E11 | page: 2, section: extracted, quote: "Local methods make use of two main ingredients to perform the multidimensional projection, namely, the neighborhood information of each data instance and the location of a subset of samples a priori positioned in the visual space."
- PAPER2011ZADUREF08-E12 | page: 2, section: extracted, quote: "First proposed by Kruskal [21], nonlinear-optimization-based techniques comprise the class of global methods that accomplish the mapping to visual space by ﬁnding a minimum for an energy function, usually called stress function."
