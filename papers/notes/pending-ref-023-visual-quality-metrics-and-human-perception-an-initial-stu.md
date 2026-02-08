---
id: paper-2010-pending-ref-023
title: "Visual quality metrics and human perception: an initial study on 2D projections of large multidimensional data"
authors: "Andrada Tatu, Peter Bak, Enrico Bertini, Daniel Keim, and Joern Schneidewind"
venue: "UNKNOWN"
year: 2010
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-023-2010-visual-quality-metrics-and-human-perception-an-initial-study-on-2d-projections-of-lar.pdf
seed_note_id: "paper-2015-perception-based-projection-evaluation"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- While several techniques and commercial products have proven to be useful to provide eﬀective support to the problem, modern databases are confronted with data complexities that go well beyond the limits of human understanding.
- These techniques have however severe problems in terms of interpretation, as it is no longer possible to interpret the observed patterns in terms of the dimension of the original data space.
- They were told that their challenge is to analyze a large amount of attributes describing the wines, such as color saturation, alcohol content, etc.
- However, one problem with these metrics is the lack of empirical validation based on user studies.

# Method Summary
- Techniques like multi-dimensional scaling (MDS) and principal component analysis (PCA) oﬀer traditional solutions by creating data embedding that try to preserve as much as possible distances in the original multi-dimensional space in the 2D projection.
- The rationale behind this method is that quality metrics can help users reduce the search space of projections by ﬁltering out views with low information content.
- Measure Section Class Consistency (CCM) 3.1 Histogram Density 1D (1D-HDM) 3.2 Histogram Density 2D (2D-HDM) 3.2 Class Density (CDM) 3.3 In the following, the assumption is that each cluster is uniquely labeled (either manually or through some form of n-dimensional clustering algorithm) and that for each point it is possible to know to which cluster it pertains.
- The Histogram Density Measure 2D (2D-HDM) is an extended version of the 1D-HDM, for which a 2-dimensional histogram on the scatter plot is computed, that is each bin represents a small square over the 2D projection and the bin count is the number of data points falling within the square.
- At ﬁrst, participants were asked to select the ﬁve most qualitative projections for separating wine types and then order them using numbers between 1 and 5 (5 indicating the absolute best representation, and 1 the worst out of the ﬁve best quality scatter plots).
- While it is certainly clear how these measures can help users deal with large data spaces there are a number of open issues related to the human perception of the structures captured automatically by the suggested algorithms.
- The idea of using measures calculated over the data or over the visualization space to select interesting projections has been proposed already in some foundational works, like Projection Pursuit [4, 8] and Grand Tour [1].

# When To Use / Not Use
- Use when:
  - The goal of this phase is not only to determine which of the metrics performs best, but also to reason around the results to (1)hunt for interesting insights about how users perceive the selected feature; (2)design better metrics able to capture the desired feature with more accuracy.
  - The rationale behind these techniques is that automatic selection of “best” views is not only useful but also necessary when the number of potential projections exceeds the limit of human interpretation.
- Avoid when:
  - In summary, 2D-HDM, tightly followed by CCM, reﬂected users’ quality assignment best by getting the highest and lowest quality ranking accurately, and having the highest R2 value of the correlation.
  - The outcome of the study permits ﬁrst of all to validate the assumption that the selection of views best ranks by quality measures is a viable way to simulate the selection of users.
- Failure modes:
  - A common denominator of all these works is the total absence of user studies able to inspect the relationship between human-detected and machine-detected data patterns.

# Metrics Mentioned
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- The rationale behind this method is that quality metrics can help users reduce the search space of projections by ﬁltering out views with low information content.
- Measure Section Class Consistency (CCM) 3.1 Histogram Density 1D (1D-HDM) 3.2 Histogram Density 2D (2D-HDM) 3.2 Class Density (CDM) 3.3 In the following, the assumption is that each cluster is uniquely labeled (either manually or through some form of n-dimensional clustering algorithm) and that for each point it is possible to know to which cluster it pertains.
- The Histogram Density Measure 2D (2D-HDM) is an extended version of the 1D-HDM, for which a 2-dimensional histogram on the scatter plot is computed, that is each bin represents a small square over the 2D projection and the bin count is the number of data points falling within the square.
- At ﬁrst, participants were asked to select the ﬁve most qualitative projections for separating wine types and then order them using numbers between 1 and 5 (5 indicating the absolute best representation, and 1 the worst out of the ﬁve best quality scatter plots).
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-023-C1 | stance: support | summary: While several techniques and commercial products have proven to be useful to provide eﬀective support to the problem, modern databases are confronted with data complexities that go well beyond the limits of human understanding. | evidence_ids: PENDING-REF-023-E1, PENDING-REF-023-E2
- CLAIM-PENDING-REF-023-C2 | stance: support | summary: Techniques like multi-dimensional scaling (MDS) and principal component analysis (PCA) oﬀer traditional solutions by creating data embedding that try to preserve as much as possible distances in the original multi-dimensional space in the 2D projection. | evidence_ids: PENDING-REF-023-E3, PENDING-REF-023-E4
- CLAIM-PENDING-REF-023-C3 | stance: support | summary: The rationale behind this method is that quality metrics can help users reduce the search space of projections by ﬁltering out views with low information content. | evidence_ids: PENDING-REF-023-E5, PENDING-REF-023-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 6 | relevance: high | note: guides reliable interpretation of projected views

# Evidence
- PENDING-REF-023-E1 | page: 1, section: extracted, quote: "While several techniques and commercial products have proven to be useful to provide eﬀective support to the problem, modern databases are confronted with data complexities that go well beyond the limits of human understanding."
- PENDING-REF-023-E2 | page: 1, section: extracted, quote: "These techniques have however severe problems in terms of interpretation, as it is no longer possible to interpret the observed patterns in terms of the dimension of the original data space."
- PENDING-REF-023-E3 | page: 5, section: extracted, quote: "They were told that their challenge is to analyze a large amount of attributes describing the wines, such as color saturation, alcohol content, etc."
- PENDING-REF-023-E4 | page: 2, section: extracted, quote: "However, one problem with these metrics is the lack of empirical validation based on user studies."
- PENDING-REF-023-E5 | page: 1, section: extracted, quote: "Techniques like multi-dimensional scaling (MDS) and principal component analysis (PCA) oﬀer traditional solutions by creating data embedding that try to preserve as much as possible distances in the original multi-dimensional space in the 2D projection."
- PENDING-REF-023-E6 | page: 1, section: extracted, quote: "The rationale behind this method is that quality metrics can help users reduce the search space of projections by ﬁltering out views with low information content."
- PENDING-REF-023-E7 | page: 3, section: extracted, quote: "Measure Section Class Consistency (CCM) 3.1 Histogram Density 1D (1D-HDM) 3.2 Histogram Density 2D (2D-HDM) 3.2 Class Density (CDM) 3.3 In the following, the assumption is that each cluster is uniquely labeled (either manually or through some form of n-dimensional clustering algorithm) and that for each point it is possible to know to which cluster it pertains."
- PENDING-REF-023-E8 | page: 3, section: extracted, quote: "The Histogram Density Measure 2D (2D-HDM) is an extended version of the 1D-HDM, for which a 2-dimensional histogram on the scatter plot is computed, that is each bin represents a small square over the 2D projection and the bin count is the number of data points falling within the square."
