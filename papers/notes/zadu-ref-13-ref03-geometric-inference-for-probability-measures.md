---
id: paper-2011-zadu-ref-13
title: "Geometric Inference for Measures based on Distance Functions"
authors: "Frederic Chazal; David Cohen-Steiner; Quentin Merigot"
venue: "Foundations of Computational Mathematics"
year: 2011
tags: [dr, zadu-table1-reference, dtm]
source_pdf: papers/raw/zadu-table1-references/ref03_geometric_inference_for_probability_measures.pdf
seed_note_id: "paper-2023-zadu-library"
evidence_level: high
updated_at: 2026-02-13
---

# Problem
- Classical distance-to-set inference is brittle under outliers because even small outlier mass can strongly perturb geometric topology.
- The paper replaces set-based modeling with probability-measure modeling and studies robust distance functions under this view.
- It provides theoretical stability and inference guarantees that later DR-quality measures (notably DTM-based ones) rely on.

# Method Summary
- Introduces the distance-to-measure function `d_{mu,m0}`, defined through an average of pseudo-distances over mass levels up to `m0`.
- Shows an equivalent optimal-transport characterization: distance from a Dirac mass to the set of submeasures under Wasserstein distance.
- Proves Wasserstein stability properties for submeasure sets and for the distance-to-measure function.
- Derives geometric/topological inference guarantees (sublevel-set behavior, homotopy-related robustness) under sampling/noise assumptions.

# When To Use / Not Use
- Use when:
  - data contain outliers/noise where Hausdorff/set distance is too fragile,
  - measure-level geometric robustness is needed before downstream DR reliability scoring,
  - Wasserstein-based stability arguments are desired.
- Avoid when:
  - only exact noiseless set geometry is assumed and robustness is unnecessary.
- Failure modes:
  - inappropriate mass parameter (`m0`) selection can over-smooth or under-smooth geometric detail.

# Metrics Mentioned
- `dtm`: this paper is a primary theoretical source for distance-to-measure formulations used in robust geometric reliability analysis.

# Implementation Notes
- Practical use depends on choosing smoothing mass `m0`; this controls robustness/detail tradeoff.
- The optimal-transport equivalence gives a principled computational route for approximate implementations.
- Wasserstein-based stability bounds justify comparing noisy empirical measures to idealized distributions.

# Claim Atoms (For Conflict Resolution)
- CLAIM-ZR13-C1 | stance: support | summary: Distance-to-measure provides a robust replacement for set distance in outlier-prone geometric inference. | evidence_ids: ZR13-E1, ZR13-E2
- CLAIM-ZR13-C2 | stance: support | summary: The proposed function has explicit Wasserstein characterization and stability guarantees. | evidence_ids: ZR13-E3, ZR13-E4, ZR13-E5
- CLAIM-ZR13-C3 | stance: support | summary: The framework supports topological inference with noisy empirical measures. | evidence_ids: ZR13-E6, ZR13-E7, ZR13-E8

# Workflow Relevance Map
- step: 2 | relevance: medium | note: informs noise/outlier-aware preprocessing assumptions for geometry-sensitive workflows.
- step: 3 | relevance: medium | note: supports DTM-family metric choice when robustness is required.
- step: 4 | relevance: high | note: provides theoretical justification for robust geometric scoring under distribution shift/noise.

# Evidence
- ZR13-E1 | page: 7, section: introduction, quote: "adding even a single data point that is far ... will increase by one the number of connected components"
- ZR13-E2 | page: 7, section: introduction, quote: "we replace compact subsets of Rd by finite (probability) measures"
- ZR13-E3 | page: 12, section: definition 3.2, quote: "distance function to mu with parameter m0"
- ZR13-E4 | page: 13, section: proposition 3.3, quote: "minimal Wasserstein distance between the Dirac mass m0 delta_x and the set of submeasures"
- ZR13-E5 | page: 14, section: proposition 3.4, quote: "Proposition 3.4. Let mu and mu' be two probability measures on Rd."
- ZR13-E6 | page: 7, section: background, quote: "the distance between two probability measures will be measured through Wasserstein distance"
- ZR13-E7 | page: 10, section: convergence, quote: "mu_N converges almost surely to mu in the W_p distance"
- ZR13-E8 | page: 18, section: inference results, quote: "one deduces that the oﬀsets of two uniformly close distance-like functions with large weak feature size have the same homotopy type"
