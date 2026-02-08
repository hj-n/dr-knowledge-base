---
id: paper-2014-sorzano-survey-dr-techniques
title: "A Survey of Dimensionality Reduction Techniques"
authors: "C.O.S. Sorzano; J. Vargas; A. Pascual-Montano"
venue: "Information Sciences"
year: 2014
tags: [dr, survey, pca, manifold, stability]
source_pdf: papers/raw/1403.2877v1.pdf
seed_note_id: ""
evidence_level: high
updated_at: 2026-02-08
---

# Problem
- High-dimensional datasets in life sciences and other domains contain far more variables than observations, making direct modeling unstable and expensive.
- Practitioners need a structured map of DR families because technique choices depend on whether they must preserve global structure, local neighborhoods, or domain-specific constraints.
- The survey targets the practical gap between many available DR methods and limited guidance on how to reason about their assumptions and failure modes.

# Method Summary
- The paper organizes DR methods by mathematical family and by representation behavior (linear/nonlinear, global/local), then explains core mechanisms and assumptions for each family.
- It explicitly separates feature selection from dimensionality reduction so practitioners do not conflate dropping variables with learning new latent coordinates.
- It emphasizes stability as a first-class property for DR methods, in addition to reconstruction or distance-preservation criteria.
- It discusses local subspace approaches (for clustered structure) as complementary to single global linear models such as PCA.

# When To Use / Not Use
- Use when you need a broad, method-level decision framework before selecting a specific DR technique for a new dataset.
- Use when deciding whether a local model is needed instead of a single global linear mapping.
- Avoid using it as a performance benchmark by itself; it is a taxonomy/insight source rather than a single controlled benchmark.
- Failure mode: adopting only historical popularity (for example PCA) without checking the data geometry and stability assumptions highlighted in the survey.

# Metrics Mentioned
- Distance-preservation and neighborhood-faithfulness are described as core quality lenses when comparing techniques.
- Stability is highlighted as an explicit desirable property of DR mappings.
- No single universal scalar metric is prescribed; method suitability depends on structure-preservation goals.

# Implementation Notes
- Start with a clear statement of whether your downstream task requires global geometry, local neighborhood fidelity, or both.
- For clustered high-dimensional data, consider local-subspace approaches rather than forcing a single global linear model.
- Record preprocessing assumptions (centering/scaling, distance choice) because they implicitly change what is preserved.
- Use this survey as design-space guidance, then validate candidate methods with task-aligned metrics in this repository workflow.

# Claim Atoms (For Conflict Resolution)
- CLAIM-SORZANO14-C1 | stance: support | summary: DR methods should be organized by mathematical assumptions and preservation behavior, not by popularity. | evidence_ids: SOR14-E1, SOR14-E4
- CLAIM-SORZANO14-C2 | stance: support | summary: Global and local bases preserve different structures, so task alignment is required before method selection. | evidence_ids: SOR14-E2, SOR14-E5
- CLAIM-SORZANO14-C3 | stance: support | summary: Stability is a required evaluation property in addition to projection fidelity. | evidence_ids: SOR14-E3

# Workflow Relevance Map
- step: 1 | relevance: medium | note: frames what users should clarify about structure they care to preserve (global vs local).
- step: 3 | relevance: high | note: gives method-family criteria for technique selection under structural assumptions.
- step: 4 | relevance: medium | note: warns that preprocessing and model choices alter stability/fidelity behavior.
- step: 6 | relevance: medium | note: provides principled language for explaining why a method family was selected.

# Evidence
- SOR14-E1 | page: 1, section: Abstract, quote: "In this review we categorize the plethora of dimension reduction techniques available"
- SOR14-E2 | page: 1, section: Introduction, quote: "This new basis can be global or local and can fulfill very different properties"
- SOR14-E3 | page: 2, section: Introduction, quote: "An interesting property of any dimensionality reduction technique is to consider its stability"
- SOR14-E4 | page: 1, section: Introduction, quote: "The dimensionality reduction can be made in two different ways"
- SOR14-E5 | page: 9, section: Localized PCA, quote: "different small datasets or clusters ... approximated well by different linear subspaces"
- SOR14-E6 | page: 1, section: Introduction, quote: "Principal Component Analysis (PCA), dates back to Karl Pearson in 1901"
