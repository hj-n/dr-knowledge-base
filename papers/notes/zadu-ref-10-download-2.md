---
id: paper-2026-zadu-ref-10
title: "Quantifying the Neighborhood Preservation of Self-Organizing Feature Maps"
authors: "UNKNOWN"
venue: "UNKNOWN"
year: 2026
tags: [dr, zadu-table1-reference, topo]
source_pdf: papers/raw/zadu-table1-references/download (2).pdf
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- Neigh b orho o d preserv ation from input space to output space is an essen tial elemen t of self/- organizing feature maps lik e the Kohonen/-map/.
- Ho w ev er/, a measure for the preserv ation or violation of neigh b orho o d relations/, whic h is more systematic than just visual insp ection of the map/, w as lac king/.

# Method Summary
- This source proposes topographic product as a quantitative neighborhood-preservation measure for self-organizing maps.
- The text states the measure is sensitive to large-scale neighborhood-order violations.
- It also states the measure is less sensitive to ordering distortions caused by varying areal magnification factors.
- A near-zero topographic-product value is described as indicating near-perfect neighborhood preservation.

# When To Use / Not Use
- Use when:
  - Use when neighborhood-preservation diagnostics are required for map-style embeddings.
  - Use when you need a topological quality signal beyond visual inspection.
- Avoid when:
  - Avoid using this measure alone when strong geometric or class-level guarantees are needed.
- Failure modes:
  - Misinterpreting mild non-zero values without considering map dimensionality and magnification effects.

# Metrics Mentioned
- `topo`: topographic neighborhood-preservation quality

# Implementation Notes
- For reproducible comparison, keep preprocessing and map-training settings fixed when comparing topographic-product values.
- Pair with at least one complementary local or global metric before final recommendation text.

# Claim Atoms (For Conflict Resolution)
- CLAIM-SOURCE-10-CORE | stance: support | summary: This source contributes DR method/quality evidence relevant to metric selection. | evidence_ids: ZR10-E1
- CLAIM-METRIC-TOPO-SOURCE-10 | stance: support | summary: This source presents `topo` (topographic product) as a neighborhood-preservation quality measure and describes its interpretation bands. | evidence_ids: ZR10-E2, ZR10-E4, ZR10-E5

# Workflow Relevance Map
- step: 3 | relevance: high | note: Informs task-aligned metric/technique selection and metric trust calibration.
- step: 6 | relevance: high | note: Provides rationale that can be translated for end users.

# Evidence
- ZR10-E1 | page: 1, section: extracted, quote: "Neighborhood preservation from input space to output space is an essential element of self-organizing feature maps."
- ZR10-E2 | page: 1, section: extracted, quote: "We show that a topographic product is an appropriate measure in this regard."
- ZR10-E3 | page: 1, section: extracted, quote: "The measure is sensitive to large-scale violations of neighborhood ordering."
- ZR10-E4 | page: 1, section: extracted, quote: "A vanishing value of the topographic product indicates perfect neighborhood preservation."
- ZR10-E5 | page: 1, section: extracted, quote: "Negative/positive values indicate output-space dimensionality that is too small/too large."
