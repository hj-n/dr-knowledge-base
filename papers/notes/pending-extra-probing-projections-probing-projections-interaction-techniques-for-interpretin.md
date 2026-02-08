---
id: paper-2026-pending-extra-probing-projections
title: "Probing Projections: Interaction Techniques for Interpreting Arrangements and Errors of Dimensionality Reductions"
authors: "Julian Stahnke, Marian Dork, Boris Muller, Andreas Thom"
venue: "IEEE Transactions on Visualization and Computer Graphics"
year: 2016
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/Probing_Projections_Interaction_Techniques_for_Interpreting_Arrangements_and_Errors_of_Dimensionality_Reductions.pdf
seed_note_id: "paper-2019-mdp-visual-analytics-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- The user should be aware of distortions in the projection, as well as be able to view the true high-dimensional distances and compare them to the approximated distances to allow for a more careful reading and interpretation of it. • Allow for multi-level comparisons.
- A problem with this solution is that it introduces new distortions in the spatial relationship between all other points.
- The projection shows the output of the dimensionality-reduction algorithm. (For the prototype, we decided to use MDS, as it exhibits many of the problems we were dealing with, such as projection errors and no meaningful axes, and we were familiar with it.) Information about projection errors is easily available for the general projection as well as for speciﬁc points.
- 8C ONCLUSION As dimensionality reductions have been gaining popularity for visual analysis of high-dimensional data, there is a growing need to support data-related tasks concerned with the interpretation of the clusters and dimensions, while also enabling the analyst to conﬁdently judge the quality of the projection.

# Method Summary
- But simultaneously some participants questions whether the tool in its current form would support a scientiﬁc approach: “It is important to know what is the projection algorithm and what are the activated dimensions for the clustering. ”(P10) T able 2.
- We contribute the concept of probing as an integrated approach to interpreting the meaning and quality of visualizations and propose a set of interactive methods to examine dimensionality-reduced data as well as the projection itself.
- While there has been substantial research on optimising projection algorithms to increase computation speed and projection accuracy, approximation errors cannot be eradicated, they are built into the method.
- The projection shows the output of the dimensionality-reduction algorithm. (For the prototype, we decided to use MDS, as it exhibits many of the problems we were dealing with, such as projection errors and no meaningful axes, and we were familiar with it.) Information about projection errors is easily available for the general projection as well as for speciﬁc points.
- While the integration of visualization of projection errors and projected data prompted favourable responses, it is not clear whether the idea of probing as an approach to integrate the visualization of data and its errors has wider applicability in visualization.
- Because of its high computational complexity, considerable work on dimensionality reduction has focused on the optimisation of projection techniques, for example, by utilising the graphics card [13] or guiding the algorithm towards regions of interest [30].
- In contrast to the mapping of a standard scatterplot, which can be traced back to the particular dimensions of a given dataset, the axes and positions of projections are the result of a complex algorithm whose iterative mechanism is highly opaque.

# When To Use / Not Use
- Use when:
  - Most participants were also confused by the fact that the error display was context-sensitive; changing to show errors in regards to hovered points: “There’s a difference in the meaning, there seems to be a general white and a country-related white?” (P4).
  - Brightness is used to avoid confusion with the group colours.
- Avoid when:
  - The projection shows the output of the dimensionality-reduction algorithm. (For the prototype, we decided to use MDS, as it exhibits many of the problems we were dealing with, such as projection errors and no meaningful axes, and we were familiar with it.) Information about projection errors is easily available for the general projection as well as for speciﬁc points.
  - First, we conducted a brief user study of the web-based visualization tool to assess the general viability of the concept of probing and identify speciﬁc opportunities for reﬁnement of the prototype; second, we ran a more focused study to better understand how people would use the different probing functions during the analysis.
- Failure modes:
  - A two-year qualitative study of data analysts who use dimensionality reduction led to a characterisation of two main types of task sequences: ﬁrst, analysts tended to verify the explicit and implicit clusters, and second, they sought the mapping between original and synthetic data dimensions [4].

# Metrics Mentioned
- `stress`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- We contribute the concept of probing as an integrated approach to interpreting the meaning and quality of visualizations and propose a set of interactive methods to examine dimensionality-reduced data as well as the projection itself.
- While there has been substantial research on optimising projection algorithms to increase computation speed and projection accuracy, approximation errors cannot be eradicated, they are built into the method.
- The projection shows the output of the dimensionality-reduction algorithm. (For the prototype, we decided to use MDS, as it exhibits many of the problems we were dealing with, such as projection errors and no meaningful axes, and we were familiar with it.) Information about projection errors is easily available for the general projection as well as for speciﬁc points.
- While the integration of visualization of projection errors and projected data prompted favourable responses, it is not clear whether the idea of probing as an approach to integrate the visualization of data and its errors has wider applicability in visualization.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-EXTRA-C1 | stance: support | summary: The user should be aware of distortions in the projection, as well as be able to view the true high-dimensional distances and compare them to the approximated distances to allow for a more careful reading and interpretation of it. • Allow for multi-level comparisons. | evidence_ids: PENDING-EXTRA-E1, PENDING-EXTRA-E2
- CLAIM-PENDING-EXTRA-C2 | stance: support | summary: But simultaneously some participants questions whether the tool in its current form would support a scientiﬁc approach: “It is important to know what is the projection algorithm and what are the activated dimensions for the clustering. ”(P10) T able 2. | evidence_ids: PENDING-EXTRA-E3, PENDING-EXTRA-E4
- CLAIM-PENDING-EXTRA-C3 | stance: support | summary: We contribute the concept of probing as an integrated approach to interpreting the meaning and quality of visualizations and propose a set of interactive methods to examine dimensionality-reduced data as well as the projection itself. | evidence_ids: PENDING-EXTRA-E5, PENDING-EXTRA-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 6 | relevance: high | note: guides reliable interpretation of projected views

# Evidence
- PENDING-EXTRA-E1 | page: 2, section: extracted, quote: "The user should be aware of distortions in the projection, as well as be able to view the true high-dimensional distances and compare them to the approximated distances to allow for a more careful reading and interpretation of it. • Allow for multi-level comparisons."
- PENDING-EXTRA-E2 | page: 6, section: extracted, quote: "A problem with this solution is that it introduces new distortions in the spatial relationship between all other points."
- PENDING-EXTRA-E3 | page: 2, section: extracted, quote: "The projection shows the output of the dimensionality-reduction algorithm. (For the prototype, we decided to use MDS, as it exhibits many of the problems we were dealing with, such as projection errors and no meaningful axes, and we were familiar with it.) Information about projection errors is easily available for the general projection as well as for speciﬁc points."
- PENDING-EXTRA-E4 | page: 8, section: extracted, quote: "8C ONCLUSION As dimensionality reductions have been gaining popularity for visual analysis of high-dimensional data, there is a growing need to support data-related tasks concerned with the interpretation of the clusters and dimensions, while also enabling the analyst to conﬁdently judge the quality of the projection."
- PENDING-EXTRA-E5 | page: 8, section: extracted, quote: "But simultaneously some participants questions whether the tool in its current form would support a scientiﬁc approach: “It is important to know what is the projection algorithm and what are the activated dimensions for the clustering. ”(P10) T able 2."
- PENDING-EXTRA-E6 | page: 1, section: extracted, quote: "We contribute the concept of probing as an integrated approach to interpreting the meaning and quality of visualizations and propose a set of interactive methods to examine dimensionality-reduced data as well as the projection itself."
- PENDING-EXTRA-E7 | page: 2, section: extracted, quote: "While there has been substantial research on optimising projection algorithms to increase computation speed and projection accuracy, approximation errors cannot be eradicated, they are built into the method."
- PENDING-EXTRA-E8 | page: 8, section: extracted, quote: "While the integration of visualization of projection errors and projected data prompted favourable responses, it is not clear whether the idea of probing as an approach to integrate the visualization of data and its errors has wider applicability in visualization."
