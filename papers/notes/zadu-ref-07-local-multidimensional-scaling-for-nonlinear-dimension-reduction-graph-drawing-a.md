---
id: paper-2009-zadu-ref-07
title: "Local Multidimensional Scaling for Nonlinear Dimension Reduction, Graph Drawing, and Proximity Analysis"
authors: "Lisha Chen, Andreas Buja"
venue: "Journal of the American Statistical Association"
year: 2009
tags: [dr, zadu-table1-reference, stress, tnc]
source_pdf: papers/raw/zadu-table1-references/Local Multidimensional Scaling for Nonlinear Dimension Reduction  Graph Drawing  and Proximity Analysis.pdf
evidence_level: medium
updated_at: 2026-02-08
---
# Problem
- One of the newer methods capable of flattening manifolds, called ‘‘local linear embedding’’ or LLE (Roweis and Saul 2000), is a novel idea: it attempts to preserve local affine structure by representing each data point as an approximate affine mixture of its neighbor points and constructing a point scatter in low dimensions that preserves as best as possible the affine mixture coefficients from high-dimensional data space, using an elegant eigenproblem.
- Although LMDS’ tuning parameter provides flexibility, it also creates a selection problem: how does one know in practice which among several configurations is most faithful to the underlying high-dimensional structure?
- LMDS’ solution to the localization problem has drawbacks, too, in that it may exhibit systematic distortions.
- For {xi} we use ‘‘configuration’’ from proximity analysis, and also ‘‘embedding’’ and ‘‘graph layout.’’ For Di,j we use ‘‘dissimilarity’’ from proximity analysis, and also ‘‘target distance,’’ meaning distances between high-dimensional feature vectors in dimension reduction and shortest-path-length distances in graph drawing.
- We expand the ‘‘repulsion term’’ (3), discarding functions of the dissimilarities that do not affect the minimization problem: LMDSD N ðx1; ... ; xN Þ; X ði; jÞ2N Di; j/C0k xi /C0 xj k /C0/C1 2 ð4Þ /C0 2wD‘ X ði; jÞ=2N k xi /C0 xj kð 5Þ þ w X ði; jÞ=2N k xi /C0 xj k2 ð6Þ As D‘ ! ‘, we let w !

# Method Summary
- One of the newer methods capable of flattening manifolds, called ‘‘local linear embedding’’ or LLE (Roweis and Saul 2000), is a novel idea: it attempts to preserve local affine structure by representing each data point as an approximate affine mixture of its neighbor points and constructing a point scatter in low dimensions that preserves as best as possible the affine mixture coefficients from high-dimensional data space, using an elegant eigenproblem.
- CRITERIA FOR PARAMETER SELECTION For automatic selection of tuning parameters and comparison of methods, we need measures of faithfulness of configurations separate from the stress functions used for optimizing configurations.
- (1964a), ‘‘Multidimensional Scaling by Optimizing Goodness of Fit to a Nonmetric Hypothesis,’’ Psychometrika, 29, 1–27. ——— (1964b), ‘‘Nonmetric Multidimensional Scaling: A Numerical Method,’’ Psychometrika, 29, 115–129.
- We introduce a competing method called ‘‘Local Multidimensional Scaling’’ (LMDS).
- DISCUSSION AND CONCLUSION This article makes three contributions: (1) It introduces a novel version of multidimensional scaling, called LMDS, that lends itself to locally faithful nonlinear dimension reduction and as such competes successfully with recent proposals, such as ‘‘local linear embedding’’ (LLE, Roweis and Saul 2000) and ‘‘isometric feature mapping’’ (Isomap, Tenenbaum et al.
- For {xi} we use ‘‘configuration’’ from proximity analysis, and also ‘‘embedding’’ and ‘‘graph layout.’’ For Di,j we use ‘‘dissimilarity’’ from proximity analysis, and also ‘‘target distance,’’ meaning distances between high-dimensional feature vectors in dimension reduction and shortest-path-length distances in graph drawing.
- A hybrid of classical and distance scaling are the semidefinite programming (SDP) approaches by Lu, Keles, Wright,and Wahba (2005) and Weinberger, Sha, Zhu, and Saul (2006) who fit full-rank Gram matrices K to local proximities via D i,j 2 /C25 Ki,i þ Kj,j /C0 2Ki,j and extract hierarchical embeddings by decomposing K.

# When To Use / Not Use
- Use when:
  - Although widely used, these methods fail to flatten curved, intrinsically low-dimensional manifolds.
  - One of the newer methods capable of flattening manifolds, called ‘‘local linear embedding’’ or LLE (Roweis and Saul 2000), is a novel idea: it attempts to preserve local affine structure by representing each data point as an approximate affine mixture of its neighbor points and constructing a point scatter in low dimensions that preserves as best as possible the affine mixture coefficients from high-dimensional data space, using an elegant eigenproblem.
  - For {xi} we use ‘‘configuration’’ from proximity analysis, and also ‘‘embedding’’ and ‘‘graph layout.’’ For Di,j we use ‘‘dissimilarity’’ from proximity analysis, and also ‘‘target distance,’’ meaning distances between high-dimensional feature vectors in dimension reduction and shortest-path-length distances in graph drawing.
- Avoid when:
  - [A version of it was independently proposed by Akkucuk and Carroll (2006) for comparing different dimension reduction methods.] In addition, we are able to use LC meta-criteria for tuning the degree of localization, that is, the size of neighborhoods in the LMDS stress function.
  - The idea is borrowed from ‘‘force-directed energy functions’’ used in graph drawing, an important specialty in scientific visualization (Di Battista, Eades, Tamassia, and Tollis 1999; Kaufmann and Wagner, 2001; Brandes 2001; Noack 2003; Michailidis and de Leeuw 2001).
- Failure modes:
  - Akkucuk and Carroll (2006) go further by mapping N K9 to a z-score under random overlap, but in most applications these z-scores are extreme because even weak structure results in extreme statistical significance under the null hypothesis of random overlap.
  - It turns out that configurations based on LMDS K with K ¼ 4 (circles) performs best in terms of Madj K9 for K9 up to 8, whereas the configurations generated by K ¼ 8 (triangles) and K ¼ 12 (plus signs) perform badly, as they are uniformly beaten by MDS.

# Metrics Mentioned
- `nh`: label-based neighborhood hit.
- `nd`: neighbor-shape dissimilarity or neighbor distortion.
- `pr`: pairwise-distance correlation behavior.
- `proc`: Procrustes local shape agreement.
- `stress`: stress-based distance distortion.

# Implementation Notes
- To compare recovery of the three angular parameters, we shaded the configuration points by dividing the range of each parameter in turn into its three tercile brackets and encoding them in grayscale.
- We show how such measures can be employed as part of data analytic methodology: (1) for choosing tuning parameters such as strength of the repulsive force and neighborhood size, and (2) as the basis of diagnostic plots that show how faithfully each point is embedded in a configuration.
- A good strategy for optimization is to start with a large value such as t ¼ 1 to obtain a stable configuration, and lower t successively as low as 0.01, using previous configurations as initializations for smaller values of t.
- CRITERIA FOR PARAMETER SELECTION For automatic selection of tuning parameters and comparison of methods, we need measures of faithfulness of configurations separate from the stress functions used for optimizing configurations.
- Although LMDS’ tuning parameter provides flexibility, it also creates a selection problem: how does one know in practice which among several configurations is most faithful to the underlying high-dimensional structure?
- This problem can be corrected: Invariance under change of units: D i,j and t have the same units, hence the units of t can be eliminated, for example, by t ¼ medianN(Di, j)t9, where the new parameter t9 is unit free.
- Keep preprocessing, initialization policy, and random-seed protocol fixed when comparing methods.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PAPER2009ZADUREF07-C1 | stance: support | summary: One of the newer methods capable of flattening manifolds, called ‘‘local linear embedding’’ or LLE (Roweis and Saul 2000), is a novel idea: it attempts to preserve local affine structure by representing each data point as an approximate affine mixture of its neighbor points and constructing a point scatter in low dimensions that preserves as best as possible the affine mixture coefficients from high-dimensional data space, using an elegant eigenproblem. | evidence_ids: PAPER2009ZADUREF07-E1, PAPER2009ZADUREF07-E2
- CLAIM-PAPER2009ZADUREF07-C2 | stance: support | summary: One of the newer methods capable of flattening manifolds, called ‘‘local linear embedding’’ or LLE (Roweis and Saul 2000), is a novel idea: it attempts to preserve local affine structure by representing each data point as an approximate affine mixture of its neighbor points and constructing a point scatter in low dimensions that preserves as best as possible the affine mixture coefficients from high-dimensional data space, using an elegant eigenproblem. | evidence_ids: PAPER2009ZADUREF07-E3, PAPER2009ZADUREF07-E4
- CLAIM-PAPER2009ZADUREF07-C3 | stance: support | summary: To compare recovery of the three angular parameters, we shaded the configuration points by dividing the range of each parameter in turn into its three tercile brackets and encoding them in grayscale. | evidence_ids: PAPER2009ZADUREF07-E5, PAPER2009ZADUREF07-E6
- CLAIM-METRIC-STRESS-SOURCE-07 | stance: support | summary: This source includes evidence relevant to `stress` in dimensionality-reduction reliability evaluation. | evidence_ids: PAPER2009ZADUREF07-E1, PAPER2009ZADUREF07-E2
- CLAIM-METRIC-TNC-SOURCE-07 | stance: support | summary: This source includes evidence relevant to `tnc` in dimensionality-reduction reliability evaluation. | evidence_ids: PAPER2009ZADUREF07-E1, PAPER2009ZADUREF07-E2

# Workflow Relevance Map
- step: 2 | relevance: medium | note: adds constraints for preprocessing and data-audit checks
- step: 3 | relevance: high | note: directly informs task-aligned technique/metric selection
- step: 5 | relevance: medium | note: adds initialization sensitivity guidance
- step: 6 | relevance: high | note: adds hyperparameter sensitivity or optimization guidance
- step: 7 | relevance: high | note: supports visualization interpretation and user explanation

# Evidence
- PAPER2009ZADUREF07-E1 | page: 2, section: extracted, quote: "One of the newer methods capable of flattening manifolds, called ‘‘local linear embedding’’ or LLE (Roweis and Saul 2000), is a novel idea: it attempts to preserve local affine structure by representing each data point as an approximate affine mixture of its neighbor points and constructing a point scatter in low dimensions that preserves as best as possible the affine mixture coefficients from high-dimensional data space, using an elegant eigenproblem."
- PAPER2009ZADUREF07-E2 | page: 3, section: extracted, quote: "Although LMDS’ tuning parameter provides flexibility, it also creates a selection problem: how does one know in practice which among several configurations is most faithful to the underlying high-dimensional structure?"
- PAPER2009ZADUREF07-E3 | page: 3, section: extracted, quote: "LMDS’ solution to the localization problem has drawbacks, too, in that it may exhibit systematic distortions."
- PAPER2009ZADUREF07-E4 | page: 3, section: extracted, quote: "For {xi} we use ‘‘configuration’’ from proximity analysis, and also ‘‘embedding’’ and ‘‘graph layout.’’ For Di,j we use ‘‘dissimilarity’’ from proximity analysis, and also ‘‘target distance,’’ meaning distances between high-dimensional feature vectors in dimension reduction and shortest-path-length distances in graph drawing."
- PAPER2009ZADUREF07-E5 | page: 4, section: extracted, quote: "We expand the ‘‘repulsion term’’ (3), discarding functions of the dissimilarities that do not affect the minimization problem: LMDSD N ðx1; ... ; xN Þ; X ði; jÞ2N Di; j/C0k xi /C0 xj k /C0/C1 2 ð4Þ /C0 2wD‘ X ði; jÞ=2N k xi /C0 xj kð 5Þ þ w X ði; jÞ=2N k xi /C0 xj k2 ð6Þ As D‘ ! ‘, we let w !"
- PAPER2009ZADUREF07-E6 | page: 2, section: extracted, quote: "High-dimensional data have arisen naturally as one has moved from the analysis of single images or single signals to the analysis of databases of images and signals, so that images and signals are treated as cases and pixel intensities or amplitudes as the variables."
- PAPER2009ZADUREF07-E7 | page: 5, section: extracted, quote: "CRITERIA FOR PARAMETER SELECTION For automatic selection of tuning parameters and comparison of methods, we need measures of faithfulness of configurations separate from the stress functions used for optimizing configurations."
- PAPER2009ZADUREF07-E8 | page: 12, section: extracted, quote: "(1964a), ‘‘Multidimensional Scaling by Optimizing Goodness of Fit to a Nonmetric Hypothesis,’’ Psychometrika, 29, 1–27. ——— (1964b), ‘‘Nonmetric Multidimensional Scaling: A Numerical Method,’’ Psychometrika, 29, 115–129."
- PAPER2009ZADUREF07-E9 | page: 2, section: extracted, quote: "We introduce a competing method called ‘‘Local Multidimensional Scaling’’ (LMDS)."
- PAPER2009ZADUREF07-E10 | page: 12, section: extracted, quote: "DISCUSSION AND CONCLUSION This article makes three contributions: (1) It introduces a novel version of multidimensional scaling, called LMDS, that lends itself to locally faithful nonlinear dimension reduction and as such competes successfully with recent proposals, such as ‘‘local linear embedding’’ (LLE, Roweis and Saul 2000) and ‘‘isometric feature mapping’’ (Isomap, Tenenbaum et al."
- PAPER2009ZADUREF07-E11 | page: 3, section: extracted, quote: "A hybrid of classical and distance scaling are the semidefinite programming (SDP) approaches by Lu, Keles, Wright,and Wahba (2005) and Weinberger, Sha, Zhu, and Saul (2006) who fit full-rank Gram matrices K to local proximities via D i,j 2 /C25 Ki,i þ Kj,j /C0 2Ki,j and extract hierarchical embeddings by decomposing K."
- PAPER2009ZADUREF07-E12 | page: 3, section: extracted, quote: "We show how such measures can be employed as part of data analytic methodology: (1) for choosing tuning parameters such as strength of the repulsive force and neighborhood size, and (2) as the basis of diagnostic plots that show how faithfully each point is embedded in a configuration."
