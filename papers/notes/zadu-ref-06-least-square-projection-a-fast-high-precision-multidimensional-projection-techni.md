---
id: paper-2008-zadu-ref-06
title: "Least Square Projection: A Fast High-Precision Multidimensional Projection Technique and Its Application to Document Mapping"
authors: "F.V. Paulovich, L.G. Nonato, R. Minghim, H. Levkowitz"
venue: "IEEE Transactions on Visualization and Computer Graphics"
year: 2008
tags: [dr, zadu-table1-reference, stress]
source_pdf: papers/raw/zadu-table1-references/Least_Square_Projection_A_Fast_High-Precision_Multidimensional_Projection_Technique_and_Its_Application_to_Document_Mapping.pdf
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- —The problem of projecting multidimensional data into lower dimensions has been pursued by many researchers due to its potential application to data analyses of various kinds.
- This paper presents a novel multidimensional projection technique based on least square approximations.

# Method Summary
- The results show the capability of the technique to form groups of points by degree of similarity in 2D.
- This paper presents a novel multidimensional projection technique based on least square approximations.
- Ç 1I NTRODUCTION D ATA sources have increased substantially both in size and complexity, so extracting useful information from them has become a challenge.
- One measure of data complexity is the number of attributes associated with each instance of data.

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

# Implementation Notes
- Runtime/complexity signal: Ç 1I NTRODUCTION D ATA sources have increased substantially both in size and complexity, so extracting useful information from them has become a challenge.

# Claim Atoms (For Conflict Resolution)
- CLAIM-SOURCE-06-CORE | stance: support | summary: This source contributes DR method/quality evidence relevant to metric selection. | evidence_ids: ZR06-E1
- CLAIM-METRIC-STRESS-SOURCE-06 | stance: support | summary: This source uses or discusses `stress` for distance-fitting distortion objective/metric in dimensionality-reduction evaluation. | evidence_ids: ZR06-E2

# Workflow Relevance Map
- step: 3 | relevance: high | note: Informs task-aligned metric/technique selection and metric trust calibration.
- step: 6 | relevance: high | note: Provides rationale that can be translated for end users.

# Evidence
- ZR06-E1 | page: 1, section: extracted, quote: "This paper presents a novel multidimensional projection technique based on least square approximations."
- ZR06-E2 | page: 1, section: extracted, quote: "The results show the capability of the technique to form groups of points by degree of similarity in 2D."
- ZR06-E3 | page: 1, section: extracted, quote: "Ç 1I NTRODUCTION D ATA sources have increased substantially both in size and complexity, so extracting useful information from them has become a challenge."
- ZR06-E4 | page: 1, section: extracted, quote: "One measure of data complexity is the number of attributes associated with each instance of data."
- ZR06-E5 | page: 1, section: extracted, quote: "This paper presents a novel multidimensional projection technique, called Least Square Projection (LSP), that encom- passes good features of both linear and nonlinear projection methods."
- ZR06-E6 | page: 2, section: extracted, quote: "We have presented an initial version of LSP before [4], now significantly extended to employ automatically defined weights to improve control-point definition and to reduce the computational complexity."
- ZR06-E7 | page: 2, section: extracted, quote: "A recurrent problem related to Sammon’s Mapping is its computational complexity Oðn 2Þ."
- ZR06-E8 | page: 3, section: extracted, quote: "In the general case, where each instance is connected to all other instances, the iteration of the FDP model’s complexity is Oðn2Þ."
