---
id: paper-2013-pending-ref-060
title: "ProxiLens: Interactive Exploration of High-Dimensional Data using Projections"
authors: "Nicolas Heulot, Michael Aupetit, and Jean Daniel Fekete"
venue: "UNKNOWN"
year: 2013
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-060-2013-proxilens-interactive-exploration-of-high-dimensional-data-using-projections.pdf
seed_note_id: "paper-2019-mdp-visual-analytics-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- Introduction Data analysts are faced with challenging problems to analyze and interpret high-dimensional (HD) data.
- However this proximity-based visualization technique has the following issues: Interaction: Flickering problems appear when users explores a region of the projection with many false neighborhoods artifacts, as the proximities in the 2D space does not match the proximities in the HD space.
- We ﬁnally observed that ProxiLens with its local spatial clearing of the false neighbors, and its time delays, enables a true continuous exploration of the HD space despite projection distortions overcoming the limits of the initially proposed proximity-based visualization [Aup07].
- Color encoding : Proximities are displayed on the V oronoi cells which have arbitrary sizes depending on the projection We propose a solution which tackle these problems and helps a continuous and user centric exploration of the HD space.

# Method Summary
- We present ProxiLens: a new interactive technique which allows navigating HD data in a continuous way through their 2D projection, i.e. locally clearing projection artifacts, so that analysts can better understand and analyze local HD data structure.
- Color encoding : Proximities are displayed on the V oronoi cells which have arbitrary sizes depending on the projection We propose a solution which tackle these problems and helps a continuous and user centric exploration of the HD space.
- Nevertheless stress information gives only a global information on how the projection algorithm performed preserving the HD data structure or a local information on where the projection artifacts are mainly located.
- HD distances are displayed using a blue colorscale with a uniform variation of its color intensity (whitest colors map shortest HD distances to the reference point in the center of the lens). are not neighbors on the projection but are neighbors in the HD space, without loosing continuity of the navigation.
- V AMP: EuroVis Workshop on Visual Analytics using Multidimensional Projections, Michael Aupetit; Laurens van der Maaten, Jun 2013, Leipzig, Germany. ￿10.2312/PE.V AMP.V AMP2013.011-015￿. ￿hal-01523025v2￿ EuroVis 2013 Workshop on Visual Analytics using Multidimensional Projections (2013) Short Papers M.
- However this proximity-based visualization technique has the following issues: Interaction: Flickering problems appear when users explores a region of the projection with many false neighborhoods artifacts, as the proximities in the 2D space does not match the proximities in the HD space.
- We ﬁnally observed that ProxiLens with its local spatial clearing of the false neighbors, and its time delays, enables a true continuous exploration of the HD space despite projection distortions overcoming the limits of the initially proposed proximity-based visualization [Aup07].

# When To Use / Not Use
- Use when:
  - We must avoid the selection of false neighbors artifacts as the next reference point because it is what generates ﬂickering colors on the projection due to the sudden change of the location in the HD space.
  - It also uses timers to jump to tear points, in order to avoid ﬂickering of the colors due to discontinuities in the HD space navigation.
- Avoid when:
  - This interpolation computes the color u(x) of a pixel x using the inverse distance weighting of the color ui of each point i: u(x) = N ∑ i=0 wi(x)ui ∑N j=0 w j(x) , with wi(x) = 1 ||x− pi||z We use this color interpolation to encode HD distance of each focus point to the reference data instance in order to let the color of the dots encoding class labels.
  - V AMP: EuroVis Workshop on Visual Analytics using Multidimensional Projections, Michael Aupetit; Laurens van der Maaten, Jun 2013, Leipzig, Germany. ￿10.2312/PE.V AMP.V AMP2013.011-015￿. ￿hal-01523025v2￿ EuroVis 2013 Workshop on Visual Analytics using Multidimensional Projections (2013) Short Papers M.
- Failure modes:
  - However this proximity-based visualization technique has the following issues: Interaction: Flickering problems appear when users explores a region of the projection with many false neighborhoods artifacts, as the proximities in the 2D space does not match the proximities in the HD space.

# Metrics Mentioned
- `continuity`: referenced as part of projection-quality or reliability assessment.
- `stress`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- Studies on the automatic setting of the radii parameters and the selection of more than one focus point needs to be experimented in order to improve the technique.
- Color encoding : Proximities are displayed on the V oronoi cells which have arbitrary sizes depending on the projection We propose a solution which tackle these problems and helps a continuous and user centric exploration of the HD space.
- Nevertheless stress information gives only a global information on how the projection algorithm performed preserving the HD data structure or a local information on where the projection artifacts are mainly located.
- HD distances are displayed using a blue colorscale with a uniform variation of its color intensity (whitest colors map shortest HD distances to the reference point in the center of the lens). are not neighbors on the projection but are neighbors in the HD space, without loosing continuity of the navigation.
- V AMP: EuroVis Workshop on Visual Analytics using Multidimensional Projections, Michael Aupetit; Laurens van der Maaten, Jun 2013, Leipzig, Germany. ￿10.2312/PE.V AMP.V AMP2013.011-015￿. ￿hal-01523025v2￿ EuroVis 2013 Workshop on Visual Analytics using Multidimensional Projections (2013) Short Papers M.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-060-C1 | stance: support | summary: Introduction Data analysts are faced with challenging problems to analyze and interpret high-dimensional (HD) data. | evidence_ids: PENDING-REF-060-E1, PENDING-REF-060-E2
- CLAIM-PENDING-REF-060-C2 | stance: support | summary: We present ProxiLens: a new interactive technique which allows navigating HD data in a continuous way through their 2D projection, i.e. locally clearing projection artifacts, so that analysts can better understand and analyze local HD data structure. | evidence_ids: PENDING-REF-060-E3, PENDING-REF-060-E4
- CLAIM-PENDING-REF-060-C3 | stance: support | summary: Studies on the automatic setting of the radii parameters and the selection of more than one focus point needs to be experimented in order to improve the technique. | evidence_ids: PENDING-REF-060-E5, PENDING-REF-060-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-REF-060-E1 | page: 2, section: extracted, quote: "Introduction Data analysts are faced with challenging problems to analyze and interpret high-dimensional (HD) data."
- PENDING-REF-060-E2 | page: 3, section: extracted, quote: "However this proximity-based visualization technique has the following issues: Interaction: Flickering problems appear when users explores a region of the projection with many false neighborhoods artifacts, as the proximities in the 2D space does not match the proximities in the HD space."
- PENDING-REF-060-E3 | page: 5, section: extracted, quote: "We ﬁnally observed that ProxiLens with its local spatial clearing of the false neighbors, and its time delays, enables a true continuous exploration of the HD space despite projection distortions overcoming the limits of the initially proposed proximity-based visualization [Aup07]."
- PENDING-REF-060-E4 | page: 3, section: extracted, quote: "Color encoding : Proximities are displayed on the V oronoi cells which have arbitrary sizes depending on the projection We propose a solution which tackle these problems and helps a continuous and user centric exploration of the HD space."
- PENDING-REF-060-E5 | page: 2, section: extracted, quote: "We present ProxiLens: a new interactive technique which allows navigating HD data in a continuous way through their 2D projection, i.e. locally clearing projection artifacts, so that analysts can better understand and analyze local HD data structure."
- PENDING-REF-060-E6 | page: 2, section: extracted, quote: "Nevertheless stress information gives only a global information on how the projection algorithm performed preserving the HD data structure or a local information on where the projection artifacts are mainly located."
- PENDING-REF-060-E7 | page: 4, section: extracted, quote: "HD distances are displayed using a blue colorscale with a uniform variation of its color intensity (whitest colors map shortest HD distances to the reference point in the center of the lens). are not neighbors on the projection but are neighbors in the HD space, without loosing continuity of the navigation."
- PENDING-REF-060-E8 | page: 1, section: extracted, quote: "V AMP: EuroVis Workshop on Visual Analytics using Multidimensional Projections, Michael Aupetit; Laurens van der Maaten, Jun 2013, Leipzig, Germany. ￿10.2312/PE.V AMP.V AMP2013.011-015￿. ￿hal-01523025v2￿ EuroVis 2013 Workshop on Visual Analytics using Multidimensional Projections (2013) Short Papers M."
