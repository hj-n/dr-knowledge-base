---
id: paper-2009-zadu-ref-16
title: "Mach Learn (2009) 77: 1–25"
authors: "Yair Goldberg, Ya’acov Ritov"
venue: "Machine Learning"
year: 2009
tags: [dr, zadu-table1-reference, proc, tnc]
source_pdf: papers/raw/zadu-table1-references/ref12_local_procrustes_for_manifold_embedding_a_measure_of_embedding_quality_and_embedding_algor.pdf
evidence_level: medium
updated_at: 2026-02-08
---
# Problem
- While our main discussion regards isometric embeddings, we will also discuss the conformal embedding problem, which is the framework of algorithms such as c-Isomap (de Silva and Tenenbaum 2003) and Conformal Embeddings (CE) (Sha and Saul 2005).
- All of these measures, unlike the Procrustes measure we suggest, do not take into account the structure of the neighborhoods, either in the high-dimensional input space or in the low-dimensional embedding space.
- The main difﬁculty in analyzing such high-dimensional data sets is that the number of observations required to estimate functions at a set level of accuracy grows exponentially with the dimension.
- Our problem consists of a neighbor-graph with a conﬁguration space that includes all of the rotations of the projection matrices Pi Mach Learn (2009) 77: 1–25 11 at each point xi .
- To overcome this problem, one should choose neighborhoods that are large relative to the magnitude of the noise, but not too large with respect to the curvature of the manifold.

# Method Summary
- Abstract We present the Procrustes measure, a novel measure based on Procrustes rotation that enables quantitative comparison of the output of manifold-based embedding algorithms such as LLE (Roweis and Saul, Science 290(5500), 2323–2326, 2000) and Isomap (Tenenbaum et al., Science 290(5500), 2319–2323, 2000).
- While our main discussion regards isometric embeddings, we will also discuss the conformal embedding problem, which is the framework of algorithms such as c-Isomap (de Silva and Tenenbaum 2003) and Conformal Embeddings (CE) (Sha and Saul 2005).
- 4.3 Simulated annealing (SA) alignment procedure In step 2 of PSA (see Sect.4.2), it is necessary to align the PCA projection matricesPi .I nt h e following we suggest an alignment method based on simulated annealing (SA) (Kirkpatrick et al.
- Second, R(X,Y) is not an ideal measure of the quality of embedding for algorithms that normalize their output, such as LLE (Roweis and Saul 2000), Laplacian Eigenmap (Belkin and Niyogi 2003), and LTSA (Zhang and Zha 2004).
- Embedding of the ﬁrst neighborhood: – Choose an index i (randomly). – Calculate the embedding Yi = XiPi ,w h e r ePi is the PCA projection matrix of Xi . – Update the list of indices of embedded points N = Neighbors(i).
- Finally, we will discuss the relation between the measures suggested in this work to the objective functions of other algorithms, namely LTSA (Zhang and Zha 2004) and SDE (Weinberger and Saul 2006).
- We further suggest two new algorithms for discovering the low-dimensional embedding of a high-dimensional data set, based on minimization of the suggested measure function.

# When To Use / Not Use
- Use when:
  - Hence (xij −¯xi) 2 − J′ i (xij −¯xi) 2 = q∑ p=d+1 (w′ p(xij −¯xi))2 = (xij −¯xi) − JiJ′ i (xij −¯xi) 2 = Ji(zij −¯zi) − JiJ′ i (Ji(zij −¯zi)) + O(r2 i ) 2 = O(r2 i ) 2 = O(r4 i ), where wd+1,...,w q are a completion of w1,...,w d to an orthonormal basis of Rq and we used the fact that J′ i Ji = I .
  - Theorem 1 claims that when the number of input pointsX increases, the low-dimensional points Z = φ−1(X) of the input data tend to zero R.T h i si m p l i e st h a t the minimizer Y of R should be close to the original data set Z (up to rotation and translation).
  - This is because normalization of the output distorts the structure of the local neighborhoods and therefore yields high R-values even if the output seems to ﬁnd the underlying structure of the input.
- Avoid when:
  - Rather, a different or modiﬁed technique for subspaces alignment, for example the use of landmarks (de Silva and Tenenbaum2003), is required in order to make this algorithm truly useful.
  - The use of local PCA produces a good lowdimensional description of the neighborhoods, but the description of each of the neighborhoods is in an arbitrary coordinate system.
- Failure modes:
  - This assumption is needed because we are interested in an embedding that everywhere preserves the local structure of distances and angles between neighboring points.
  - The statistic computes the sum of squares between pairs of corresponding points after one of the conﬁgurations is rotated and translated to best match the other.

# Metrics Mentioned
- `tnc`: Trustworthiness and Continuity behavior.
- `nh`: label-based neighborhood hit.
- `nd`: neighbor-shape dissimilarity or neighbor distortion.
- `pr`: pairwise-distance correlation behavior.
- `topo`: topology-related structure behavior.
- `proc`: Procrustes local shape agreement.

# Implementation Notes
- (18) As ˜φ is a conformal mapping, we have cmin∥zij − zi∥≤ dM(xij ,xi),w h e r edM is the geodesic metric and cmin > 0 is the minimum of the scale functionc(z) measures the scaling change of φ at z.
- Initialization: – Find the neighbors Xi of each point xi and let Neighbors (i) be the indices of the neighbors Xi . – Initialize the list of all embedded points’ indices to N := ∅.
- Here we want to compare between each original neighborhood Xi and its corresponding embedding Yi , where we allow Yi not only to be rotated and translated but also to be rescaled.
- The parameters of the variations are given by a 30 × 10 array that contains −45 to 45 degrees of azimuth and 0 to 30 degrees of elevation (see Hamm et al.
- The cooling scheme requires the estimation of many parameters, and the run-time depends heavily on the correct choice of these parameters.
- It may also be used to choose optimal parameters, such as neighborhood size and output dimension, before other algorithms are applied.
- Keep preprocessing, initialization policy, and random-seed protocol fixed when comparing methods.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PAPER2009ZADUREF16-C1 | stance: support | summary: While our main discussion regards isometric embeddings, we will also discuss the conformal embedding problem, which is the framework of algorithms such as c-Isomap (de Silva and Tenenbaum 2003) and Conformal Embeddings (CE) (Sha and Saul 2005). | evidence_ids: PAPER2009ZADUREF16-E1, PAPER2009ZADUREF16-E2
- CLAIM-PAPER2009ZADUREF16-C2 | stance: support | summary: Abstract We present the Procrustes measure, a novel measure based on Procrustes rotation that enables quantitative comparison of the output of manifold-based embedding algorithms such as LLE (Roweis and Saul, Science 290(5500), 2323–2326, 2000) and Isomap (Tenenbaum et al., Science 290(5500), 2319–2323, 2000). | evidence_ids: PAPER2009ZADUREF16-E3, PAPER2009ZADUREF16-E4
- CLAIM-PAPER2009ZADUREF16-C3 | stance: support | summary: (18) As ˜φ is a conformal mapping, we have cmin∥zij − zi∥≤ dM(xij ,xi),w h e r edM is the geodesic metric and cmin > 0 is the minimum of the scale functionc(z) measures the scaling change of φ at z. | evidence_ids: PAPER2009ZADUREF16-E5, PAPER2009ZADUREF16-E6
- CLAIM-METRIC-PROC-SOURCE-16 | stance: support | summary: This source includes evidence relevant to `proc` in dimensionality-reduction reliability evaluation. | evidence_ids: PAPER2009ZADUREF16-E1, PAPER2009ZADUREF16-E2
- CLAIM-METRIC-TNC-SOURCE-16 | stance: support | summary: This source includes evidence relevant to `tnc` in dimensionality-reduction reliability evaluation. | evidence_ids: PAPER2009ZADUREF16-E1, PAPER2009ZADUREF16-E2

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports task clarification before model selection
- step: 2 | relevance: medium | note: adds constraints for preprocessing and data-audit checks
- step: 3 | relevance: high | note: directly informs task-aligned technique/metric selection
- step: 5 | relevance: medium | note: adds initialization sensitivity guidance
- step: 6 | relevance: high | note: adds hyperparameter sensitivity or optimization guidance

# Evidence
- PAPER2009ZADUREF16-E1 | page: 3, section: extracted, quote: "While our main discussion regards isometric embeddings, we will also discuss the conformal embedding problem, which is the framework of algorithms such as c-Isomap (de Silva and Tenenbaum 2003) and Conformal Embeddings (CE) (Sha and Saul 2005)."
- PAPER2009ZADUREF16-E2 | page: 2, section: extracted, quote: "All of these measures, unlike the Procrustes measure we suggest, do not take into account the structure of the neighborhoods, either in the high-dimensional input space or in the low-dimensional embedding space."
- PAPER2009ZADUREF16-E3 | page: 1, section: extracted, quote: "The main difﬁculty in analyzing such high-dimensional data sets is that the number of observations required to estimate functions at a set level of accuracy grows exponentially with the dimension."
- PAPER2009ZADUREF16-E4 | page: 10, section: extracted, quote: "Our problem consists of a neighbor-graph with a conﬁguration space that includes all of the rotations of the projection matrices Pi Mach Learn (2009) 77: 1–25 11 at each point xi ."
- PAPER2009ZADUREF16-E5 | page: 17, section: extracted, quote: "To overcome this problem, one should choose neighborhoods that are large relative to the magnitude of the noise, but not too large with respect to the curvature of the manifold."
- PAPER2009ZADUREF16-E6 | page: 2, section: extracted, quote: "We further suggest two new algorithms for discovering the low-dimensional embedding of a high-dimensional data set, based on minimization of the suggested measure function."
- PAPER2009ZADUREF16-E7 | page: 1, section: extracted, quote: "Abstract We present the Procrustes measure, a novel measure based on Procrustes rotation that enables quantitative comparison of the output of manifold-based embedding algorithms such as LLE (Roweis and Saul, Science 290(5500), 2323–2326, 2000) and Isomap (Tenenbaum et al., Science 290(5500), 2319–2323, 2000)."
- PAPER2009ZADUREF16-E8 | page: 10, section: extracted, quote: "4.3 Simulated annealing (SA) alignment procedure In step 2 of PSA (see Sect.4.2), it is necessary to align the PCA projection matricesPi .I nt h e following we suggest an alignment method based on simulated annealing (SA) (Kirkpatrick et al."
- PAPER2009ZADUREF16-E9 | page: 15, section: extracted, quote: "Second, R(X,Y) is not an ideal measure of the quality of embedding for algorithms that normalize their output, such as LLE (Roweis and Saul 2000), Laplacian Eigenmap (Belkin and Niyogi 2003), and LTSA (Zhang and Zha 2004)."
- PAPER2009ZADUREF16-E10 | page: 8, section: extracted, quote: "Embedding of the ﬁrst neighborhood: – Choose an index i (randomly). – Calculate the embedding Yi = XiPi ,w h e r ePi is the PCA projection matrix of Xi . – Update the list of indices of embedded points N = Neighbors(i)."
- PAPER2009ZADUREF16-E11 | page: 5, section: extracted, quote: "Finally, we will discuss the relation between the measures suggested in this work to the objective functions of other algorithms, namely LTSA (Zhang and Zha 2004) and SDE (Weinberger and Saul 2006)."
- PAPER2009ZADUREF16-E12 | page: 6, section: extracted, quote: "Instead of measuring the difference between the original neighborhoods on the manifold and their embeddings, one can compare the local PCA projections (Mardia et al."
