---
id: paper-2017-pending-ref-047
title: "Visualizing dimensionality reduction artifacts: An evaluation"
authors: "N. Heulot, J. Fekete, and M. Aupetit"
venue: "UNKNOWN"
year: 2017
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-047-2017-visualizing-dimensionality-reduction-artifacts-an-evaluation.pdf
seed_note_id: "paper-2019-mdp-visual-analytics-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- Multidimensional scaling is one of them: it tackles the visualization problem by summarizing many dimensions into a similarity matrix that is visualized as a 2D scatterplot called a projection: 2D distances between points in the projection are meant to preserve the original dissimilarities between data items in high-dimensions.
- When distortions are “important”, they can lead to topological artifacts: the visible neighborhood is wrong, some items seem close when they are actually far-away in data-space (false neighbors) while items that are close in data-space become far-away in 2D-space (tears).
- Abstract Multidimensional scaling allows visualizing high-dimensional data as 2D maps with the premise that insights in 2D reveal valid information in high-dimensions, but the resulting projections always suffer from artifacts such as false neighborhoods and tears.
- A large number of projection algorithms [vdMPvdH08] have been designed to effectively and efﬁciently map a set of data items from a high-dimensional space ( data-space) to a lower dimensional space ( 2D-space), while preserving as much information as possible.

# Method Summary
- Because projection algorithms are black-boxes, these approaches tend to help choosing and setting an algorithm that will provide a projection that can be easily and faithfully interpreted.
- However, each projection algorithm, and especially multidimensional scaling projections, gives its own stress deﬁnition through the objective function it optimize.
- Projection artifacts Even if projection algorithms tend to preserve “most of” the important aspects of the underlying data structures existing in data-space, all the 2D distances do not faithfully respect data-space distances: some points are misplaced and we call these points artifacts.
- We can distinguish approaches that target an automatic processing of dimensionality reduction [BTK11] and other interactive approaches that provide measures and visualizations to help users explore different projection settings, such as the DimStiller system [IMI∗10].
- A large number of projection algorithms [vdMPvdH08] have been designed to effectively and efﬁciently map a set of data items from a high-dimensional space ( data-space) to a lower dimensional space ( 2D-space), while preserving as much information as possible.
- As projection artifacts have still a signiﬁcant effect on local analysis, measures and approaches that help assessing the quality of projection must be generalized in existing softwares that visualize high-dimensional data with projections.
- This system helps understand the impact of the parameters and algorithm choices on the projection quality, but it does not directly help to reveal actual clusters hidden by projection artifacts.

# When To Use / Not Use
- Use when:
  - Our results indicate that ProxiViz is suitable for this use case as is robust to projection artifacts for outlier detection.
  - The ProxiViz technique interactively colors the whole visualization when the user moves the pointer to a particular point: it shows a color-map where the intensity decreases with the dissimilarity in data-space from the focus point, conveying dissimilarity information using the color channel.
- Avoid when:
  - We can distinguish approaches that target an automatic processing of dimensionality reduction [BTK11] and other interactive approaches that provide measures and visualizations to help users explore different projection settings, such as the DimStiller system [IMI∗10].
  - Introducing this order for the techniques may slightly bias our results, but we believe that considering our high level tasks, it is important to avoid the observed learning effect while keeping the conditions equivalent by reusing the same projections.
- Failure modes:
  - However using ProxiViz, they were revealed and participants were able to use their ﬁnding to answer questions without having to explore, which explains that correctess results were better for hard questions than for easy questions using ProxiViz.

# Metrics Mentioned
- `trustworthiness`: referenced as part of projection-quality or reliability assessment.
- `stress`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- This system helps understand the impact of the parameters and algorithm choices on the projection quality, but it does not directly help to reveal actual clusters hidden by projection artifacts.
- The proximity-based visualization [Aup07] is a simple technique; unlike other techniques it does not require any parameter, only the user selection of a reference point.
- We then projected datasets using two different projection algorithms: classical MDS [Tor52], erV [VPN∗10], using different settings of the parameters.
- These studies consider a quality metric and a predeﬁned setup of parameters to compare the algorithms on benchmark data sets.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-047-C1 | stance: support | summary: Multidimensional scaling is one of them: it tackles the visualization problem by summarizing many dimensions into a similarity matrix that is visualized as a 2D scatterplot called a projection: 2D distances between points in the projection are meant to preserve the original dissimilarities between data items in high-dimensions. | evidence_ids: PENDING-REF-047-E1, PENDING-REF-047-E2
- CLAIM-PENDING-REF-047-C2 | stance: support | summary: Because projection algorithms are black-boxes, these approaches tend to help choosing and setting an algorithm that will provide a projection that can be easily and faithfully interpreted. | evidence_ids: PENDING-REF-047-E3, PENDING-REF-047-E4
- CLAIM-PENDING-REF-047-C3 | stance: support | summary: This system helps understand the impact of the parameters and algorithm choices on the projection quality, but it does not directly help to reveal actual clusters hidden by projection artifacts. | evidence_ids: PENDING-REF-047-E5, PENDING-REF-047-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-REF-047-E1 | page: 2, section: extracted, quote: "Multidimensional scaling is one of them: it tackles the visualization problem by summarizing many dimensions into a similarity matrix that is visualized as a 2D scatterplot called a projection: 2D distances between points in the projection are meant to preserve the original dissimilarities between data items in high-dimensions."
- PENDING-REF-047-E2 | page: 3, section: extracted, quote: "When distortions are “important”, they can lead to topological artifacts: the visible neighborhood is wrong, some items seem close when they are actually far-away in data-space (false neighbors) while items that are close in data-space become far-away in 2D-space (tears)."
- PENDING-REF-047-E3 | page: 1, section: extracted, quote: "Abstract Multidimensional scaling allows visualizing high-dimensional data as 2D maps with the premise that insights in 2D reveal valid information in high-dimensions, but the resulting projections always suffer from artifacts such as false neighborhoods and tears."
- PENDING-REF-047-E4 | page: 2, section: extracted, quote: "A large number of projection algorithms [vdMPvdH08] have been designed to effectively and efﬁciently map a set of data items from a high-dimensional space ( data-space) to a lower dimensional space ( 2D-space), while preserving as much information as possible."
- PENDING-REF-047-E5 | page: 2, section: extracted, quote: "Because projection algorithms are black-boxes, these approaches tend to help choosing and setting an algorithm that will provide a projection that can be easily and faithfully interpreted."
- PENDING-REF-047-E6 | page: 2, section: extracted, quote: "However, each projection algorithm, and especially multidimensional scaling projections, gives its own stress deﬁnition through the objective function it optimize."
- PENDING-REF-047-E7 | page: 2, section: extracted, quote: "Projection artifacts Even if projection algorithms tend to preserve “most of” the important aspects of the underlying data structures existing in data-space, all the 2D distances do not faithfully respect data-space distances: some points are misplaced and we call these points artifacts."
- PENDING-REF-047-E8 | page: 2, section: extracted, quote: "We can distinguish approaches that target an automatic processing of dimensionality reduction [BTK11] and other interactive approaches that provide measures and visualizations to help users explore different projection settings, such as the DimStiller system [IMI∗10]."
