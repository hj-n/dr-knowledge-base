---
id: paper-1964-zadu-ref-12
title: "Multidimensional scaling by optimizing goodness of fit to a nonmetric hypothesis"
authors: "J. B. Kruskal"
venue: "Psychometrika"
year: 1964
tags: [dr, zadu-table1-reference, stress, nm_stress]
source_pdf: papers/raw/zadu-table1-references/kruskal_1964a.pdf
seed_note_id: "paper-2023-zadu-library"
evidence_level: high
updated_at: 2026-02-13
---

# Problem
- The paper provides a formal foundation for MDS when only ordinal (rank-order) dissimilarity information is trusted.
- Earlier approaches often lacked a mathematically explicit objective for nonmetric correspondence between dissimilarities and embedding distances.
- Kruskal defines an explicit goodness-of-fit objective and a corresponding optimization view of MDS.

# Method Summary
- Core hypothesis: dissimilarities and embedding distances are monotonically related, not necessarily linearly related.
- Defines raw stress as squared residuals between fitted monotone disparities and embedding distances.
- Defines normalized stress as a scale-normalized variant, making fit comparable across configurations.
- The target embedding is the configuration minimizing stress via iterative numerical optimization.

# When To Use / Not Use
- Use when:
  - only ordinal proximity information is reliable,
  - monotone relation is a better assumption than strict metric proportionality,
  - you need interpretable stress-vs-dimension diagnostics.
- Avoid when:
  - exact metric preservation with fixed functional form is mandatory.
- Failure modes:
  - stress can always drop with more dimensions; model-selection requires explicit dimension-vs-fit diagnostics.

# Metrics Mentioned
- `stress`: introduced as a formal goodness-of-fit criterion for nonmetric MDS.
- `nm_stress`: foundational source for nonmetric/Kruskal stress interpretation and optimization.

# Implementation Notes
- The paper recommends plotting minimum stress against dimension and selecting an elbow where extra dimensions provide limited gain.
- It provides practical stress interpretation bands (poor/fair/good/excellent) as heuristic guidance.
- Optimization is iterative and initialization-sensitive, motivating multiple runs in modern practice.

# Claim Atoms (For Conflict Resolution)
- CLAIM-ZR12-C1 | stance: support | summary: Nonmetric MDS should optimize monotone consistency, not fixed-form distance matching. | evidence_ids: ZR12-E1, ZR12-E2
- CLAIM-ZR12-C2 | stance: support | summary: Stress provides a quantitative, optimization-ready goodness-of-fit objective. | evidence_ids: ZR12-E3, ZR12-E4, ZR12-E5
- CLAIM-ZR12-C3 | stance: support | summary: Dimension choice should use stress-vs-dimension behavior rather than fit alone. | evidence_ids: ZR12-E6, ZR12-E7

# Workflow Relevance Map
- step: 3 | relevance: medium | note: supports nonmetric stress as a principled objective for ordinal-structure tasks.
- step: 4 | relevance: high | note: provides formal scoring rationale and stress interpretation for configuration comparison.
- step: 6 | relevance: medium | note: iterative optimization and dimension-selection diagnostics inform hyperparameter search.

# Evidence
- ZR12-E1 | page: 1, section: abstract, quote: "Our fundamental hypothesis is that dissimilarities and distances are monotonically related."
- ZR12-E2 | page: 2, section: background, quote: "the rank order of the dissimilarities is itself enough to determine the solution."
- ZR12-E3 | page: 3, section: method overview, quote: "We call this the stress."
- ZR12-E4 | page: 8, section: stress definition, quote: "Following a time-honored tradition of statistics, we square each deviation and add the results: raw stress"
- ZR12-E5 | page: 9, section: normalization, quote: "our definition of the normalized stress"
- ZR12-E6 | page: 16, section: dimensionality, quote: "as t increases, minimum stress decreases"
- ZR12-E7 | page: 16, section: dimensionality, quote: "choose a value of t which makes the stress acceptably small"
- ZR12-E8 | page: 3, section: practical interpretation, quote: "Stress Goodness of fit 20% poor 10% fair 5% good"
