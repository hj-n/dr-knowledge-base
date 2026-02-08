---
id: paper-2009-zadu-ref-05
title: "Selecting good views of high‐dimensional data using class consistency"
authors: "Mike Sips, Boris Neubert, John P. Lewis, Pat Hanrahan"
venue: "Computer Graphics Forum"
year: 2009
tags: [dr, zadu-table1-reference, dsc]
source_pdf: papers/raw/zadu-table1-references/Computer Graphics Forum - 2009 - Sips - Selecting good views of high%E2%80%90dimensional data using class consistency.pdf
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- Many visualization techniques involve mapping high-dimensional data spaces to lower-dimensional views.
- Unfor- tunately, mapping a high-dimensional data space into a scatterplot involves a loss of information; or , even worse, it can give a misleading picture of valuable structure in higher dimensions.

# Method Summary
- In this paper , we propose class con- sistency as a measure of the quality of the mapping.
- We propose two quantitative measures of class consistency, one based on the distance to the class’s center of gravity, and another based on the entropies of the spatial distributions of classes.
- In this paper we propose class consistency as a com- putable measure of the utility of a given view.
- The contributions of this paper are: • We propose class consistency as criteria for choosing good views to a class structure in n–D.

# When To Use / Not Use
- Use when:
  - Use when labeled classes are a core analysis objective.
  - Use label-separation-sensitive metrics only after confirming class separation in original space.
- Avoid when:
  - Avoid assuming class labels always form well-separated clusters in original space.
- Failure modes:
  - Overconfident conclusions when class labels are not well-separated in original space.

# Metrics Mentioned
- `dsc`: class consistency/separation quality in embedding (label-separation-sensitive)

# Implementation Notes
- Runtime/complexity signal: Introduction Today’s scientiﬁc and business applications produce large datasets with increasing complexity and dimensionality.
- If labels are weakly separated in original space, down-weight label-separation-sensitive metrics in final justification.

# Claim Atoms (For Conflict Resolution)
- CLAIM-SOURCE-05-CORE | stance: support | summary: This source analyzes label-based DR evaluation assumptions and proposes class-aware reliability alternatives. | evidence_ids: ZR05-E1
- CLAIM-METRIC-DSC-SOURCE-05 | stance: support | summary: This source uses or discusses `dsc` for class consistency/separation quality in embedding in dimensionality-reduction evaluation. | evidence_ids: ZR05-E2

# Workflow Relevance Map
- step: 3 | relevance: high | note: Informs task-aligned metric/technique selection and metric trust calibration.
- step: 4 | relevance: medium | note: Affects optimization objective design and score interpretation during hyperparameter search.
- step: 6 | relevance: high | note: Provides rationale that can be translated for end users.

# Evidence
- ZR05-E1 | page: 1, section: extracted, quote: "In this paper , we propose class con- sistency as a measure of the quality of the mapping."
- ZR05-E2 | page: 1, section: extracted, quote: "We propose two quantitative measures of class consistency, one based on the distance to the class’s center of gravity, and another based on the entropies of the spatial distributions of classes."
- ZR05-E3 | page: 1, section: extracted, quote: "Introduction Today’s scientiﬁc and business applications produce large datasets with increasing complexity and dimensionality."
- ZR05-E4 | page: 1, section: extracted, quote: "In this paper we propose class consistency as a com- putable measure of the utility of a given view."
- ZR05-E5 | page: 1, section: extracted, quote: "In this paper, we assume that each point in high dimen- sional space has been labeled as belonging to some group."
- ZR05-E6 | page: 2, section: extracted, quote: "The contributions of this paper are: • We propose class consistency as criteria for choosing good views to a class structure in n–D."
- ZR05-E7 | page: 2, section: extracted, quote: "• We introduce and evaluate two methods for calculat- ing class consistency, a distance based and a distribution based technique."
- ZR05-E8 | page: 2, section: extracted, quote: "• We evaluate class consistency over a range of data sets with different dimensionality."
