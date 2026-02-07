---
id: paper-2009-zadu-ref-07
title: "Local Multidimensional Scaling for Nonlinear Dimension Reduction, Graph Drawing, and Proximity Analy"
year: 2009
tags: [dr, zadu-table1-reference, stress, tnc]
source_pdf: papers/raw/zadu-table1-references/Local Multidimensional Scaling for Nonlinear Dimension Reduction  Graph Drawing  and Proximity Analysis.pdf
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- Journal of the American Statistical Association ISSN: 0162-1459 (Print) 1537-274X (Online) Journal homepage: www.tandfonline.com/journals/uasa20 Local Multidimensional Scaling for Nonlinear Dimension Reduction, Graph Drawing, and Proximity Analysis Lisha Chen & Andreas Buja To cite this article: Lisha Chen & Andreas Buja (2009) Local Multidimensional Scaling for Nonlinear Dimension Reduction, Graph Drawing, and Proximity Analysis, Journal of the American Statistical Association, 104:485, 209-219, DOI: 10.1198/jasa.2009.0111 To link to this article: https://doi.org/10.1198/jasa.2009.0111 Published online: 01 Jan 2012.
- Submit your article to this journal Article views: 972 View related articles Citing articles: 14 View citing articles Full Terms & Conditions of access and use can be found at https://www.tandfonline.com/action/journalInformation?journalCode=uasa20 Local Multidimensional Sca

# Method Summary
- We introduce a competing method called ‘‘Local Multidimensional Scaling’’ (LMDS).
- We show how such measures can be employed as part of data analytic method- ology: (1) for choosing tuning parameters such as strength of the repulsive force and neighborhood size, and (2) as the basis of diagnostic plots that show how faithfully each point is embedded in a configuration.
- We apply the force paradigm to create localized versions of MDS stress functions with a tuning parameter to adjust the strength of nonlocal repulsive forces.
- LMDS, proposed here, derives from MDS by restricting the stress function to pairs of points with small distances.

# When To Use / Not Use
- Use when:
  - Use when selecting DR reliability checks in workflow Step 3.
  - Use with complementary local/cluster/global metrics rather than a single score.
- Avoid when:
  - Avoid using this source as the only decision signal without task constraints.
- Failure modes:
  - Overfitting conclusions to a single metric family or benchmark setup.

# Metrics Mentioned
- `stress`: distance-fitting distortion objective/metric
- `tnc`: local neighborhood trustworthiness/continuity balance

# Implementation Notes
- Keep preprocessing and seed policy fixed before comparing reliability scores across methods.
- Use this source with at least one complementary note before final recommendation text.

# Claim Atoms (For Conflict Resolution)
- CLAIM-SOURCE-07-CORE | stance: support | summary: This source uses localized stress formulations for neighborhood-faithful DR behavior. | evidence_ids: ZR07-E1
- CLAIM-METRIC-STRESS-SOURCE-07 | stance: support | summary: This source uses or discusses `stress` for distance-fitting distortion objective/metric in dimensionality-reduction evaluation. | evidence_ids: ZR07-E2
- CLAIM-METRIC-TNC-SOURCE-07 | stance: support | summary: This source uses or discusses `tnc` for local neighborhood trustworthiness/continuity balance in dimensionality-reduction evaluation. | evidence_ids: ZR07-E2

# Workflow Relevance Map
- step: 3 | relevance: high | note: Informs task-aligned metric/technique selection and metric trust calibration.
- step: 6 | relevance: high | note: Provides rationale that can be translated for end users.

# Evidence
- ZR07-E1 | page: 2, section: extracted, quote: "We introduce a competing method called ‘‘Local Multidimensional Scaling’’ (LMDS)."
- ZR07-E2 | page: 2, section: extracted, quote: "We apply the force paradigm to create localized versions of MDS stress functions with a tuning parameter to adjust the strength of nonlocal repulsive forces."
- ZR07-E3 | page: 2, section: extracted, quote: "LMDS, proposed here, derives from MDS by restricting the stress function to pairs of points with small distances."
- ZR07-E4 | page: 2, section: extracted, quote: "Thus, LMDS shares with LLE, Isomap, and KPCA what we may call ‘‘localization.’’ Whereas Isomap completes the ‘‘local graph’’ with shortest path lengths, LMDS stabilizes the stress function by introducing repulsion between points with large distances."
- ZR07-E5 | page: 2, section: extracted, quote: "Removing large distances from the stress function has been tried many times since Kruskal (1964a, 1964b), but the hope that small dissimilarities add up to globally meaningful optimal config- urations was dashed by Graef and Spence (1979): Their simulations showed that removal of the smallest third of Lisha Chen is Assistant Professor of"
- ZR07-E6 | page: 3, section: extracted, quote: "This question can be answered with measures of faithfulness separate from the stress functions."
- ZR07-E7 | page: 3, section: extracted, quote: "We have proposed one such family of measures, called ‘‘Local Continuity’’ or ‘‘LC’’ meta-criteria and defined as the average size of the overlap of K-nearest neighborhoods in the high-dimensional data and the low-dimensional config- uration (Chen 2006)."
- ZR07-E8 | page: 3, section: extracted, quote: "We show how such measures can be employed as part of data analytic method- ology: (1) for choosing tuning parameters such as strength of the repulsive force and neighborhood size, and (2) as the basis of diagnostic plots that show how faithfully each point is embedded in a configuration."
