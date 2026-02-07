---
id: paper-1964-zadu-ref-12
title: "Multidimensional scaling by optimizing goodness of fit to a nonmetric hypothesis"
year: 1964
tags: [dr, zadu-table1-reference, stress]
source_pdf: papers/raw/zadu-table1-references/kruskal_1964a.pdf
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- 1 mARCH, 1964 MULTIDIMENSIONAL SCALING BY OPTIMIZING GOODNESS OF FIT TO A NONMETRIC HYPOTHESIS J.
- KRUSKAL BELL TELEPHONE LABORATORIES MURRAY HILL, N.

# Method Summary
- In this paper we present a technique for multidimensional scaling, similar to Shepard's, which arose from attempts to improve and perfect his ideas.
- (A complete explanation is given in the next section.) Thus for any given configuration the stress measures how well that configuration matches the data.
- Once the stress has been defined and the definition justified, the rest of the theory follows without further difficulty.
- The solution is defined to be the best-fitting configuration of points, that is, the configuration of minimum stress.

# When To Use / Not Use
- Use when:
  - Use when comparing embeddings under explicit scale control.
  - Use scale-invariant variants when ranking methods across plots.
- Avoid when:
  - Avoid comparing raw normalized stress or raw KL-divergence values across arbitrary scales.
- Failure modes:
  - Mis-ranking methods due to embedding-scale artifacts.

# Metrics Mentioned
- `stress`: distance-fitting distortion objective/metric

# Implementation Notes
- Fix or optimize embedding scale before comparing stress/KL-based scores across methods.

# Claim Atoms (For Conflict Resolution)
- CLAIM-SOURCE-12-CORE | stance: support | summary: This source reports scale sensitivity of common DR quality metrics and motivates scale-aware evaluation. | evidence_ids: ZR12-E1
- CLAIM-METRIC-STRESS-SOURCE-12 | stance: support | summary: This source uses or discusses `stress` for distance-fitting distortion objective/metric in dimensionality-reduction evaluation. | evidence_ids: ZR12-E2

# Workflow Relevance Map
- step: 3 | relevance: high | note: Informs task-aligned metric/technique selection and metric trust calibration.
- step: 4 | relevance: medium | note: Affects optimization objective design and score interpretation during hyperparameter search.
- step: 6 | relevance: high | note: Provides rationale that can be translated for end users.

# Evidence
- ZR12-E1 | page: 2, section: extracted, quote: "In this paper we present a technique for multidimensional scaling, similar to Shepard's, which arose from attempts to improve and perfect his ideas."
- ZR12-E2 | page: 3, section: extracted, quote: "(A complete explanation is given in the next section.) Thus for any given configuration the stress measures how well that configuration matches the data."
- ZR12-E3 | page: 3, section: extracted, quote: "Once the stress has been defined and the definition justified, the rest of the theory follows without further difficulty."
- ZR12-E4 | page: 3, section: extracted, quote: "The solution is defined to be the best-fitting configuration of points, that is, the configuration of minimum stress."
- ZR12-E5 | page: 3, section: extracted, quote: "Stress Goodness of fit 20% poor 10% fair 5% good 2½% excellent 0% \"perfect\" By \"perfect\" we mean only that there is a perfect monotone relationship between dissimilarities and the distances."
- ZR12-E6 | page: 5, section: extracted, quote: "KRUSKAL 5 t b* .J ¢q B PERFECT ASCENDING RELATIONSHIP STRESS -~- O DISTANCE, d Fm~R~ 2 represents the data best."
- ZR12-E7 | page: 7, section: extracted, quote: "KRUSKAL 7 t .( IMPERFECT ASCENDING RELATIONSHIP / (NORMALIZED) STRESS 2,4 ......"
- ZR12-E8 | page: 8, section: extracted, quote: "Following a time-honored tradition of statistics, we square each deviation and add the results: raw stress = S* = ~ (d,i -- d,) 2."
