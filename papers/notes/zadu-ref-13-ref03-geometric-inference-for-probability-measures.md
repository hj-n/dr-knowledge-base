---
id: paper-2010-zadu-ref-13
title: "Geometric Inference for Measures based on Distance Functions"
authors: "UNKNOWN"
venue: "UNKNOWN"
year: 2010
tags: [dr, zadu-table1-reference, dtm, stress]
source_pdf: papers/raw/zadu-table1-references/ref03_geometric_inference_for_probability_measures.pdf
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- Data often comes in the form of a point cloud sampled from an unknown compact subset of Euclidean space.
- The general goal of geometric inference is then to recover geometric and topological features (e.g.

# Method Summary
- In this paper, we show how to extend the framework of distance functions to overcome this problem.
- Replacing compact subsets by measures, we introduce a notion of distance function to a probability distri- bution in Rn.
- In this article, we introduce a notion of distance function to a probability measureµ , which we denote by d µ,m 0 — where m0 is a “smoothing” param- eter in (0, 1).
- We show that this function retains all the required properties for extending oﬀset-based inference results to the case where the data can be corrupted by outliers.

# When To Use / Not Use
- Use when:
  - Use when selecting DR reliability checks in workflow Step 3.
  - Use with complementary local/cluster/global metrics rather than a single score.
- Avoid when:
  - Avoid using this source as the only decision signal without task constraints.
- Failure modes:
  - Overfitting conclusions to a single metric family or benchmark setup.

# Metrics Mentioned
- `dtm`: distance-to-measure based global structure signal
- `stress`: distance-fitting distortion objective/metric

# Implementation Notes
- Keep preprocessing and seed policy fixed before comparing reliability scores across methods.
- Use this source with at least one complementary note before final recommendation text.

# Claim Atoms (For Conflict Resolution)
- CLAIM-SOURCE-13-CORE | stance: support | summary: This source introduces distance-to-measure style distance functions robust to outliers/noise. | evidence_ids: ZR13-E1
- CLAIM-METRIC-DTM-SOURCE-13 | stance: support | summary: This source uses or discusses `dtm` for distance-to-measure based global structure signal in dimensionality-reduction evaluation. | evidence_ids: ZR13-E2
- CLAIM-METRIC-STRESS-SOURCE-13 | stance: support | summary: This source uses or discusses `stress` for distance-fitting distortion objective/metric in dimensionality-reduction evaluation. | evidence_ids: ZR13-E2

# Workflow Relevance Map
- step: 3 | relevance: high | note: Informs task-aligned metric/technique selection and metric trust calibration.
- step: 6 | relevance: high | note: Provides rationale that can be translated for end users.

# Evidence
- ZR13-E1 | page: 4, section: extracted, quote: "In this paper, we show how to extend the framework of distance functions to overcome this problem."
- ZR13-E2 | page: 4, section: extracted, quote: "Replacing compact subsets by measures, we introduce a notion of distance function to a probability distri- bution in Rn."
- ZR13-E3 | page: 5, section: extracted, quote: "Cependant, une des principales limitation de ce cadre est qu’il ne permet pas de consid´ erer des donn´ ees qui sont entach´ ees de valeurs aberrantes et/ou d’un bruit de fond."
- ZR13-E4 | page: 7, section: extracted, quote: "In this article, we introduce a notion of distance function to a probability measureµ , which we denote by d µ,m 0 — where m0 is a “smoothing” param- eter in (0, 1)."
- ZR13-E5 | page: 7, section: extracted, quote: "We show that this function retains all the required properties for extending oﬀset-based inference results to the case where the data can be corrupted by outliers."
- ZR13-E6 | page: 7, section: extracted, quote: "In particular, we show that considering sublevel sets of our distance functions allows for correct inference of the homotopy type of the unknown object under fairly general assumptions."
- ZR13-E7 | page: 9, section: extracted, quote: "As mentioned earlier, the question of the convergence of the empirical measure µ N to the underlying measure µ is fundamendal in the measure- based inference approach we propose."
- ZR13-E8 | page: 10, section: extracted, quote: "This being said, we would like to stress that the stability results we obtain for the distance functions introduced below do not depend on any noise model; they just depend on the Wasserstein distance between the two probability measures being small."
