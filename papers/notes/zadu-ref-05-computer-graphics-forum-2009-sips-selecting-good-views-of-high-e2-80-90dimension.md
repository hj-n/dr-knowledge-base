---
id: paper-2009-zadu-ref-05
title: "Selecting good views of high-dimensional data using class consistency"
authors: "Mike Sips; Boris Neubert; John P. Lewis; Pat Hanrahan"
venue: "Computer Graphics Forum"
year: 2009
tags: [dr, zadu-table1-reference, dsc]
source_pdf: papers/raw/zadu-table1-references/Computer Graphics Forum - 2009 - Sips - Selecting good views of high%E2%80%90dimensional data using class consistency.pdf
seed_note_id: "paper-2023-zadu-library"
evidence_level: high
updated_at: 2026-02-13
---

# Problem
- In large SPLOMs, analysts cannot manually inspect all 2D projections, so they need a quantitative way to rank "good" views.
- The paper defines goodness relative to class structure preservation from high-dimensional space to 2D projection.
- The target is to reduce misleading projections that visually suggest class structure not supported by the original data.

# Method Summary
- The paper introduces **class consistency** as a criterion for ranking 2D orthogonal projections.
- It proposes two measures:
  - **distance consistency** (centroid-distance-based; efficient; best for convex class structure),
  - **distribution consistency** (entropy/distribution-based; more general but more expensive).
- Distance consistency is the conceptual base later used in DR evaluation as `dsc`-style class-separation scoring.
- The paper validates the measures through user studies and precision/recall against human-selected good views.

# When To Use / Not Use
- Use when:
  - your task is to find projections that preserve known class structure,
  - you need automated ranking/filtering of many candidate 2D views,
  - classes are available as labels or from a clustering step.
- Avoid when:
  - class labels are not meaningful for the analysis goal,
  - you need non-class structure quality only (for example pure geometry preservation).
- Failure modes:
  - distance consistency can underperform for non-convex or strongly interleaved class distributions, where distribution consistency is more appropriate.

# Metrics Mentioned
- `dsc`: distance-consistency style class-preservation metric (centroid-distance based), introduced for ranking projection views by class consistency.
- `distribution consistency` (non-catalog metric): entropy-based class-mixture consistency for non-convex/interleaved structures.

# Implementation Notes
- Distance consistency is computationally simpler and practical for large view matrices.
- Distribution consistency requires region-density / entropy estimation and is computationally heavier.
- For reproducible comparison, keep class labels (or clustering labels), projection generation protocol, and consistency thresholds fixed.
- The paper recommends interactive thresholding to hide poor views and focus analyst attention on high-consistency projections.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PAPER2009ZADUREF05-C1 | stance: support | summary: The paper defines class consistency as a criterion for ranking 2D projection quality with respect to class preservation. | evidence_ids: PAPER2009ZADUREF05-E1, PAPER2009ZADUREF05-E2
- CLAIM-PAPER2009ZADUREF05-C2 | stance: support | summary: Two measures are proposed: distance consistency (efficient, convex-class-friendly) and distribution consistency (more general, more expensive). | evidence_ids: PAPER2009ZADUREF05-E3, PAPER2009ZADUREF05-E4
- CLAIM-METRIC-DSC-SOURCE-05 | stance: support | summary: Distance consistency is presented as a computable class-preservation measure for selecting good projection views. | evidence_ids: PAPER2009ZADUREF05-E5, PAPER2009ZADUREF05-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: clarifies when class-structure preservation is the actual analysis goal.
- step: 3 | relevance: high | note: supports selecting class-oriented reliability metrics for projection ranking.
- step: 4 | relevance: high | note: supports deterministic ranking/filtering of many candidate projections.
- step: 7 | relevance: medium | note: gives clear user-facing rationale for why selected views are class-faithful.

# Evidence
- PAPER2009ZADUREF05-E1 | page: 1, section: abstract, quote: "we propose class consistency as a measure of the quality of the mapping."
- PAPER2009ZADUREF05-E2 | page: 2, section: contributions, quote: "Class consistency characterizes the extent to which the class neighborhood structure in n-D is preserved in a 2-D scatterplot."
- PAPER2009ZADUREF05-E3 | page: 2, section: contributions, quote: "We introduce and evaluate two methods for calculating class consistency, a distance based and a distribution based technique. Distribution based class consistency is more general, but more expensive to compute."
- PAPER2009ZADUREF05-E4 | page: 4, section: class consistency algorithms, quote: "we propose two methods for calculating class consistency, the centroid distance metric and distribution consistency."
- PAPER2009ZADUREF05-E5 | page: 8, section: conclusion, quote: "The first, distance consistency, is easy to implement and is well suited for data with convex clusters."
- PAPER2009ZADUREF05-E6 | page: 8, section: conclusion, quote: "The second measure, distribution consistency, is more general and can assess non-convex and interleaved data distributions."
- PAPER2009ZADUREF05-E7 | page: 7, section: user study, quote: "the performance of distance consistency is clearly related to the good views selected by humans."
- PAPER2009ZADUREF05-E8 | page: 8, section: applicability, quote: "This method can be applied to data with preexisting categorical labels, or to data that has been organized into classes with a clustering algorithm."
