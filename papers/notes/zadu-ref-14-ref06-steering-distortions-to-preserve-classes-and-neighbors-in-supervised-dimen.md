---
id: paper-2020-zadu-ref-14
title: "Steering Distortions to Preserve Classes and"
authors: "UNKNOWN"
venue: "UNKNOWN"
year: 2020
tags: [dr, zadu-table1-reference, kl_div, pr, stress, tnc]
source_pdf: papers/raw/zadu-table1-references/ref06_steering_distortions_to_preserve_classes_and_neighbors_in_supervised_dimensionality_reduct.pdf
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- Nonlinear dimensionality reduction of high-dimensional data is challenging as the low-dimensional embedding will necessarily contain distortions, and it can be hard to determine which distortions are the most important to avoid.
- When annotation of data into known relevant classes is available, it can be used to guide the embedding to avoid distortions that worsen class separation.

# Method Summary
- The supervised mapping method introduced in the present paper, called ClassNeRV, proposes an original stress function that takes class annotation into account and evaluates embedding quality both in terms of false neighbors and missed neighbors.
- In this work, we propose ClassNeRV, a supervised DR technique to accomplish the exploratory analysis objective while taking class information into account.
- Our contribution is two-fold: we propose ClassNeRV which utilizes class information to ensure a better preservation of classes when embedding high dimensional labeled data into a low dimensional space.
- We also derive two new class-aware quality indicators from the standard Trustworthiness and Continuity quality indicators [ 13], to account speciﬁcally for the distortions affecting class preservation.

# When To Use / Not Use
- Use when:
  - Use when labeled classes are a core analysis objective.
- Avoid when:
  - Avoid assuming class labels always form well-separated clusters in original space.
- Failure modes:
  - Overfitting conclusions to a single metric family or benchmark setup.

# Metrics Mentioned
- `kl_div`: distribution mismatch in neighbor probabilities
- `pr`: linear agreement of pairwise relationships
- `stress`: distance-fitting distortion objective/metric
- `tnc`: local neighborhood trustworthiness/continuity balance

# Implementation Notes
- Keep preprocessing and seed policy fixed before comparing reliability scores across methods.
- Use this source with at least one complementary note before final recommendation text.

# Claim Atoms (For Conflict Resolution)
- CLAIM-SOURCE-14-CORE | stance: support | summary: This source analyzes label-based DR evaluation assumptions and proposes class-aware reliability alternatives. | evidence_ids: ZR14-E1
- CLAIM-METRIC-KL_DIV-SOURCE-14 | stance: support | summary: This source uses or discusses `kl_div` for distribution mismatch in neighbor probabilities in dimensionality-reduction evaluation. | evidence_ids: ZR14-E2
- CLAIM-METRIC-PR-SOURCE-14 | stance: support | summary: This source uses or discusses `pr` for linear agreement of pairwise relationships in dimensionality-reduction evaluation. | evidence_ids: ZR14-E2
- CLAIM-METRIC-STRESS-SOURCE-14 | stance: support | summary: This source uses or discusses `stress` for distance-fitting distortion objective/metric in dimensionality-reduction evaluation. | evidence_ids: ZR14-E2
- CLAIM-METRIC-TNC-SOURCE-14 | stance: support | summary: This source uses or discusses `tnc` for local neighborhood trustworthiness/continuity balance in dimensionality-reduction evaluation. | evidence_ids: ZR14-E2

# Workflow Relevance Map
- step: 3 | relevance: high | note: Informs task-aligned metric/technique selection and metric trust calibration.
- step: 4 | relevance: medium | note: Affects optimization objective design and score interpretation during hyperparameter search.
- step: 6 | relevance: high | note: Provides rationale that can be translated for end users.

# Evidence
- ZR14-E1 | page: 1, section: extracted, quote: "The supervised mapping method introduced in the present paper, called ClassNeRV, proposes an original stress function that takes class annotation into account and evaluates embedding quality both in terms of false neighbors and missed neighbors."
- ZR14-E2 | page: 2, section: extracted, quote: "In this work, we propose ClassNeRV, a supervised DR technique to accomplish the exploratory analysis objective while taking class information into account."
- ZR14-E3 | page: 2, section: extracted, quote: "Our contribution is two-fold: we propose ClassNeRV which utilizes class information to ensure a better preservation of classes when embedding high dimensional labeled data into a low dimensional space."
- ZR14-E4 | page: 2, section: extracted, quote: "Its stress function, derived from the unsupervised NeRV [6, 7], steers the optimization so that the unavoidable distortions of the neighborhood structure are placed where they are less harmful to the class structure."
- ZR14-E5 | page: 2, section: extracted, quote: "We also derive two new class-aware quality indicators from the standard Trustworthiness and Continuity quality indicators [ 13], to account speciﬁcally for the distortions affecting class preservation."
- ZR14-E6 | page: 3, section: extracted, quote: "Class-aware tSNE (catSNE) [32] locally adapts the size of the neighbourhood to preserve based on the distribution of classes."
- ZR14-E7 | page: 3, section: extracted, quote: "At last, Clas- siMap [5] optimizes a stress function similar to the one of Local Multidimensional Scaling (LMDS) [33], but supports the exploratory analysis of labeled data by taking classes into account when penalizing false and missed neighbors."
- ZR14-E8 | page: 3, section: extracted, quote: "ClassNeRV derives the same principles as ClassiMap from the NeRV stress function to get the beneﬁts of both."
