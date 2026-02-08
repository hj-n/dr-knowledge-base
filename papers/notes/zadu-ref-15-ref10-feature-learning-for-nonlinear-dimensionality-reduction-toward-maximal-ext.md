---
id: paper-2023-zadu-ref-15
title: "Feature Learning for Nonlinear Dimensionality Reduction toward Maximal Extraction of Hidden Patterns"
authors: "Takanori Fujiwara, Yun-Hsin Kuo, Anders Ynnerman, Kwan-Liu Ma"
venue: "2023 IEEE 16th Pacific Visualization Symposium (PacificVis)"
year: 2023
tags: [dr, zadu-table1-reference, nd, pr, proc, snc, srho]
source_pdf: papers/raw/zadu-table1-references/ref10_feature_learning_for_nonlinear_dimensionality_reduction_toward_maximal_extraction_of_hid.pdf
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- Dimensionality reduction (DR) plays a vital role in the visual analy- sis of high-dimensional data.
- One main aim of DR is to reveal hidden patterns that lie on intrinsic low-dimensional manifolds.

# Method Summary
- To detect the difference of the graphs, we introduce a new graph dissimilarity measure, called neighbor-shape dissimilarity (or NSD).
- In summary, we consider our primary contributions to be: • a feature learning framework, FEALM, designed to extract a set of latent features for nonlinear DR, each of which produces a signiﬁcantly different DR result; • an exemplifying method for UMAP, where we introduce an NMM- based algorithm as well as a graph dissimilarity measure, NS
- 4 FEALM F RAMEWORK We introduce a feature learning framework, FEALM, to address the stated issues in nonlinear DR.
- NetLSD does not consider the neighbor dissimilarity (i.e., the difference of neigh- borhood relationships); thus, for dGr, we introduce a new measure, NSD, to capture both neighbor and shape dissimilarities.

# When To Use / Not Use
- Use when:
  - Use when selecting DR reliability checks in workflow Step 3.
  - Use with complementary local/cluster/global metrics rather than a single score.
- Avoid when:
  - Avoid using this source as the only decision signal without task constraints.
- Failure modes:
  - Overfitting conclusions to a single metric family or benchmark setup.

# Metrics Mentioned
- `nd`: neighbor-shape/neighbor-change dissimilarity
- `pr`: linear agreement of pairwise relationships
- `proc`: local shape agreement via Procrustes
- `snc`: inter-cluster reliability via steadiness/cohesiveness
- `srho`: rank-order agreement of pairwise relationships

# Implementation Notes
- Runtime/complexity signal: But, it is difﬁcult to judge only based on theoretical time complexity because of their detailed implemen- tation differences (e.g., requiring only fast matrix operations or slow iterative loops).

# Claim Atoms (For Conflict Resolution)
- CLAIM-SOURCE-15-CORE | stance: support | summary: This source contributes DR method/quality evidence relevant to metric selection. | evidence_ids: ZR15-E1
- CLAIM-METRIC-ND-SOURCE-15 | stance: support | summary: This source uses or discusses `nd` for neighbor-shape/neighbor-change dissimilarity in dimensionality-reduction evaluation. | evidence_ids: ZR15-E2
- CLAIM-METRIC-PR-SOURCE-15 | stance: support | summary: This source uses or discusses `pr` for linear agreement of pairwise relationships in dimensionality-reduction evaluation. | evidence_ids: ZR15-E2
- CLAIM-METRIC-PROC-SOURCE-15 | stance: support | summary: This source uses or discusses `proc` for local shape agreement via Procrustes in dimensionality-reduction evaluation. | evidence_ids: ZR15-E2
- CLAIM-METRIC-SNC-SOURCE-15 | stance: support | summary: This source uses or discusses `snc` for inter-cluster reliability via steadiness/cohesiveness in dimensionality-reduction evaluation. | evidence_ids: ZR15-E2
- CLAIM-METRIC-SRHO-SOURCE-15 | stance: support | summary: This source uses or discusses `srho` for rank-order agreement of pairwise relationships in dimensionality-reduction evaluation. | evidence_ids: ZR15-E2

# Workflow Relevance Map
- step: 3 | relevance: high | note: Informs task-aligned metric/technique selection and metric trust calibration.
- step: 6 | relevance: high | note: Provides rationale that can be translated for end users.

# Evidence
- ZR15-E1 | page: 1, section: extracted, quote: "This paper presents a feature learning framework, FEALM, designed to gener- ate a set of optimized data projections for nonlinear DR in order to capture important patterns in the hidden manifolds."
- ZR15-E2 | page: 1, section: extracted, quote: "To detect the difference of the graphs, we introduce a new graph dissimilarity measure, called neighbor-shape dissimilarity (or NSD)."
- ZR15-E3 | page: 1, section: extracted, quote: "In summary, we consider our primary contributions to be: • a feature learning framework, FEALM, designed to extract a set of latent features for nonlinear DR, each of which produces a signiﬁcantly different DR result; • an exemplifying method for UMAP, where we introduce an NMM- based algorithm as well as a graph dissimilarity measure, NS"
- ZR15-E4 | page: 3, section: extracted, quote: "4 FEALM F RAMEWORK We introduce a feature learning framework, FEALM, to address the stated issues in nonlinear DR."
- ZR15-E5 | page: 5, section: extracted, quote: "But, it is difﬁcult to judge only based on theoretical time complexity because of their detailed implemen- tation differences (e.g., requiring only fast matrix operations or slow iterative loops)."
- ZR15-E6 | page: 5, section: extracted, quote: "C.2 in our sup- plementary materials [1]), we identify that NetLSD [39] can better capture differences of graph shapes with a greatly shorter runtime than many other measures available in a library of graph dissimilari- ties [27]."
- ZR15-E7 | page: 5, section: extracted, quote: "2 is generated with NSD, here we use NetLSD (a) and the neighbor dissimilarity (b)."
- ZR15-E8 | page: 5, section: extracted, quote: "time complexity is O(qkn + q2n), where q is the total number of the top and bottom eigenvalues to take for the approximation andk is the number of neighbors set to generate an k-NN graph."
