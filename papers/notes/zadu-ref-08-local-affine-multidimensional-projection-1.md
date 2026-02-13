---
id: paper-2011-zadu-ref-08
title: "Local Affine Multidimensional Projection"
authors: "Paulo Joia; Fernando V. Paulovich; Danilo Coimbra; Jose Alberto Cuminato; Luis Gustavo Nonato"
venue: "IEEE Transactions on Visualization and Computer Graphics"
year: 2011
tags: [dr, zadu-table1-reference, stress, ivm]
source_pdf: papers/raw/zadu-table1-references/Local_Affine_Multidimensional_Projection (1).pdf
seed_note_id: "paper-2023-zadu-library"
evidence_level: high
updated_at: 2026-02-13
---

# Problem
- Interactive DR systems need methods that are not only accurate but also flexible enough to incorporate user manipulation and domain knowledge.
- Existing projection methods were often either computationally heavy or too rigid for interactive editing with sparse control points.
- The paper introduces LAMP to improve flexibility while keeping projection quality and speed practical.

# Method Summary
- LAMP computes a local affine transform for each point, constrained by orthogonality, using nearby control points.
- For each input point `x`, it solves a weighted orthogonal Procrustes-like objective minimizing `sum_i alpha_i ||f_x(x_i)-y_i||^2` under `M^T M = I`.
- Weights are inverse-distance-based (`alpha_i = 1 / ||x_i - x||^2`), emphasizing local anchors.
- The method supports both global and local behavior by varying control-point neighborhoods and can operate with a small number of user-handled controls.

# When To Use / Not Use
- Use when:
  - interactive user steering of projections is required,
  - you need to propagate a sparse set of control correspondences to full data,
  - local geometric stability under control-point edits matters.
- Avoid when:
  - control points are noisy/misaligned and no correction workflow is available.
- Failure modes:
  - errors in control-point positioning propagate through local maps, reducing projection reliability.

# Metrics Mentioned
- `stress`: used for quality/time comparison and sensitivity analyses.
- `ivm`: silhouette-style cluster-separation scores are reported in controlled user-handled comparisons.

# Implementation Notes
- Orthogonality is not cosmetic; the paper states it limits distortion propagation from imperfect controls.
- Quality depends on neighborhood size around control points; increasing neighborhood size affects continuity and stress behavior.
- The method is designed to run with very few controls, which is key for interactive workflows.

# Claim Atoms (For Conflict Resolution)
- CLAIM-ZR08-C1 | stance: support | summary: LAMP uses orthogonality-constrained local affine mappings for interactive projection control. | evidence_ids: ZR08-E1, ZR08-E2, ZR08-E3
- CLAIM-ZR08-C2 | stance: support | summary: Control-point quality and neighborhood design critically affect final projection quality. | evidence_ids: ZR08-E4, ZR08-E5
- CLAIM-ZR08-C3 | stance: support | summary: LAMP achieves competitive stress/runtime while supporting interactive use cases. | evidence_ids: ZR08-E6, ZR08-E7, ZR08-E8

# Workflow Relevance Map
- step: 3 | relevance: medium | note: suitable as a controllable projection technique in interaction-heavy analysis settings.
- step: 5 | relevance: high | note: control-point initialization and neighborhood policy are direct initialization-design decisions.
- step: 7 | relevance: high | note: supports user-driven explanation and what-if manipulation of embedding outcomes.

# Evidence
- ZR08-E1 | page: 1, section: abstract, quote: "called Local Affine Multidimensional Projection (LAMP), relies on orthogonal mapping theory"
- ZR08-E2 | page: 3, section: method, quote: "maps x to the visual space by finding the best affine transformation"
- ZR08-E3 | page: 3, section: method, quote: "where matrix M and vector t are the unknowns, I is the identity matrix"
- ZR08-E4 | page: 3, section: control-point discussion, quote: "errors in the positioning of control points are propagated"
- ZR08-E5 | page: 4, section: results setup, quote: "Stress vs. percentage of nearest neighbors used to build the affine mappings"
- ZR08-E6 | page: 8, section: conclusion, quote: "LAMP ... very effective for interactive applications"
- ZR08-E7 | page: 8, section: conclusion, quote: "outperforms existing projection methods in terms of stress minimization"
- ZR08-E8 | page: 5, section: comparisons, quote: "normalized stress and computational time" are jointly reported for method comparison.
