---
id: paper-2012-pending-extra-fernstad-et-al-2012
title: "Quality-based guidance for exploratory dimensionality reduction"
authors: "Sara Johansson Fernstad, Jane Shaw, Jimmy Johansson"
venue: "Information Visualization"
year: 2012
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/fernstad-et-al-2012-quality-based-guidance-for-exploratory-dimensionality-reduction.pdf
seed_note_id: "paper-2025-jeon-reliable-va-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- Abstract High-dimensional data sets containing hundreds of variables are difficult to explore, as traditional visualization methods often are unable to represent such data effectively.
- Background and related work Visualization of high-dimensional data sets, sometimes including hundreds of variables, is a major challenge in information visualization.
- Considering the problem of how a subset of variables might be best selected for analysis, with selection guided by a set of metrics of interest, Johansson and Johansson 4 demonstrate how an overall measure of variable interestingness can be used to indicate to the user which variables should be displayed, and why they might be of interest.
- Keywords High-dimensional data, dimensionality reduction, quality metrics, visual exploration, interactive visual analysis Introduction Data sets including hundreds of variables are increasingly common in various application areas, such as bioinformatics, simulations and social sciences.

# Method Summary
- Examples using non-dominated ranking algorithms include Srinivas and Deb 36 drawing on Goldberg’s approach, and Fonseca and Fleming, 37 who demonstrate an extensive framework for interactive decision making around several objectives and preference exploration in this context.
- Other examples are the projection pursuit algorithm, 18 which aims to identify linear projections based on a measure of usefulness, and the family of linear transformations presented by Koren and Carmel, 19 in which several different properties of the data are utilized, such as similarities and cluster structures.
- Their dimensionality reduction approach was later used by Engel et al., 20 who combined it with a hierarchical clustering method and a visual representation based on star coordinates 21 to create a structural decomposition tree for high-dimensional data.
- The analyst’s workflow for analysing these data would commonly include statistical tests, multivariate approaches such as PCA and network visualization methods such as the graphical software Cytoscape.
- A slightly different approach to dimensionality reduction is the grand tour, 22 in which the analyst moves through a sequence of two-dimensional projections of a multivariate data set.
- Subsequently, refinements to ranking approaches for considering multiple objectives have been developed and applied to many problem domains.
- The second method is a density and grid based approach using the Euclidean distance, described in detail in Johansson and Johansson.

# When To Use / Not Use
- Use when:
  - Considering the problem of how a subset of variables might be best selected for analysis, with selection guided by a set of metrics of interest, Johansson and Johansson 4 demonstrate how an overall measure of variable interestingness can be used to indicate to the user which variables should be displayed, and why they might be of interest.
  - 48 Furthermore, the QIIME (Quantitative Insights Into Microbial Ecology) pipeline, 49 which is used to process the sample data, provides a range of unlinked visual outputs such as pie charts, heatmaps, trees and networks.
- Avoid when:
  - T o avoid this, various thresholds are used to define whether a structure is significant enough to be included.
  - First, the overall approach of using quality metrics to extract the potentially most interesting variables, and to combine quality metric analysis and interactive visualization, to provide flexible and user controlled dimensionality reduction, could be applied to almost any type of data, provided the quality metrics used are appropriate for corresponding data.
- Failure modes:
  - However, by solely utilizing a single value of interestingness, information is lost regarding values of the original metrics, and the user is unable to explore explicitly the contribution of each metric to the sing l em e a s u r e .T h eu s e rm a ya l s ob ei n t e r e s t e di n exploring the effect of individual metrics upon the overall view.

# Metrics Mentioned
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- The transformations are controlled by the user, who is guided at a global level by workflows aiding to find useful chains of transformations, as well as at a local level through visual feedback, facilitating parameter tuning and identification of the most informative settings for a single transformation.
- 7 Related work is found in the area of decision making in optimization problems where, rather than metrics of interest, several objectives are considered and handled simultaneously.
- Genetic algorithms for multiobjective optimization: formulation, discussion and generalisation.
- 7 Non-dominated ranking is more commonly used in multiple objective optimization algorithms.
- Multiobjective optimization using nondominated sorting in genetic algorithms.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-EXTRA-C1 | stance: support | summary: Abstract High-dimensional data sets containing hundreds of variables are difficult to explore, as traditional visualization methods often are unable to represent such data effectively. | evidence_ids: PENDING-EXTRA-E1, PENDING-EXTRA-E2
- CLAIM-PENDING-EXTRA-C2 | stance: support | summary: Examples using non-dominated ranking algorithms include Srinivas and Deb 36 drawing on Goldberg’s approach, and Fonseca and Fleming, 37 who demonstrate an extensive framework for interactive decision making around several objectives and preference exploration in this context. | evidence_ids: PENDING-EXTRA-E3, PENDING-EXTRA-E4
- CLAIM-PENDING-EXTRA-C3 | stance: support | summary: The transformations are controlled by the user, who is guided at a global level by workflows aiding to find useful chains of transformations, as well as at a local level through visual feedback, facilitating parameter tuning and identification of the most informative settings for a single transformation. | evidence_ids: PENDING-EXTRA-E5, PENDING-EXTRA-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-EXTRA-E1 | page: 1, section: extracted, quote: "Abstract High-dimensional data sets containing hundreds of variables are difficult to explore, as traditional visualization methods often are unable to represent such data effectively."
- PENDING-EXTRA-E2 | page: 3, section: extracted, quote: "Background and related work Visualization of high-dimensional data sets, sometimes including hundreds of variables, is a major challenge in information visualization."
- PENDING-EXTRA-E3 | page: 4, section: extracted, quote: "Considering the problem of how a subset of variables might be best selected for analysis, with selection guided by a set of metrics of interest, Johansson and Johansson 4 demonstrate how an overall measure of variable interestingness can be used to indicate to the user which variables should be displayed, and why they might be of interest."
- PENDING-EXTRA-E4 | page: 1, section: extracted, quote: "Keywords High-dimensional data, dimensionality reduction, quality metrics, visual exploration, interactive visual analysis Introduction Data sets including hundreds of variables are increasingly common in various application areas, such as bioinformatics, simulations and social sciences."
- PENDING-EXTRA-E5 | page: 5, section: extracted, quote: "Examples using non-dominated ranking algorithms include Srinivas and Deb 36 drawing on Goldberg’s approach, and Fonseca and Fleming, 37 who demonstrate an extensive framework for interactive decision making around several objectives and preference exploration in this context."
- PENDING-EXTRA-E6 | page: 4, section: extracted, quote: "Other examples are the projection pursuit algorithm, 18 which aims to identify linear projections based on a measure of usefulness, and the family of linear transformations presented by Koren and Carmel, 19 in which several different properties of the data are utilized, such as similarities and cluster structures."
- PENDING-EXTRA-E7 | page: 4, section: extracted, quote: "Their dimensionality reduction approach was later used by Engel et al., 20 who combined it with a hierarchical clustering method and a visual representation based on star coordinates 21 to create a structural decomposition tree for high-dimensional data."
- PENDING-EXTRA-E8 | page: 18, section: extracted, quote: "The analyst’s workflow for analysing these data would commonly include statistical tests, multivariate approaches such as PCA and network visualization methods such as the graphical software Cytoscape."
