---
id: paper-2020-pending-ref-113
title: "t-viSNE: Interactive Assessment and Interpretation of t-SNE Projections"
authors: "A. Chatzimparmpas, R. M. Martins, and A. Kerren"
venue: "IEEE Transactions on Visualization and Computer Graphics"
year: 2020
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-113-2020-t-visne-interactive-assessment-and-interpretation-of-t-sne-projections.pdf
seed_note_id: "paper-2022-revisiting-dr-visual-cluster-analysis"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- In contrast to other, more general approaches, t-viSNE was designed with the specific problems related to the investigation of t-SNE projections in mind, bringing to light some of the hidden internal workings of the algorithm which, when visualized, may provide important insights about the high-dimensional data set under analysis.
- The problem that DR tries to solve is, in general, to find a low-dimensional representation of a high-dimensional data set that retains—as much as possible—its original structure.
- While this is of course based on subjective user feedback, we consider that it is nonetheless an important aspect of the results; since both t-viSNE and GEP mainly aim to support the exploratory visual analysis of high-dimensional data—through many different coordinated views and interactive tools—it may become hard to set a single, concrete ground-truth for evaluating their perfomance as a whole.
- 2.3 Interpretation of Projections Some attempts to enrich scatterplots with automatically-derived statistical descriptions of patterns [38], [39], [40] have shown that static mappings may be useful in simple scenarios, but the complex relations between low- and high-dimensional space in non-linear projections cannot be well represented.

# Method Summary
- In contrast to other, more general approaches, t-viSNE was designed with the specific problems related to the investigation of t-SNE projections in mind, bringing to light some of the hidden internal workings of the algorithm which, when visualized, may provide important insights about the high-dimensional data set under analysis.
- Other DR Methods Although our main design goal was to support the investigation of t-SNE projections, most of our views and interaction techniques are not strictly confined to the t-SNE algorithm.
- In this work, we present t-viSNE, an interactive tool for the visual exploration of t-SNE projections that enables analysts to inspect different aspects of their accuracy and meaning, such as the effects of hyper-parameters, distance and neighborhood preservation, densities and costs of specific neighborhoods, and the correlations between dimensions and visual patterns.
- We also evaluated our approach with a user study by comparing it with Google’s Embedding Projector (GEP): the results show that, in general, the participants could manage to reach the intended analysis tasks even with limited training, and their feedback indicates that t-viSNE reached a better level of support for the given tasks than GEP.
- Martins, Member, IEEE Computer Society , and Andreas Kerren, Senior Member, IEEE Abstract—t-Distributed Stochastic Neighbor Embedding (t-SNE) for the visualization of multidimensional data has proven to be a popular approach, with successful applications in a wide range of domains.
- Since t-viSNE adopts an approach of combining many different coordinated views, it is important for the Dimension Correlation to maintain—as much as possible— the users’ mental map of the projection, and to give simple and straightforward interpretations of the patterns they see.
- Neighborhood Preservation Since the proposal of non-linear DR methods, the idea of prioritizing the preservation of close neighborhoods instead of pairwise distances in projections has been accepted as a positive trade-off, especially in visualization scenarios.

# When To Use / Not Use
- Use when:
  - A full scatterplot with (n2 − n)/2 points and variable transparency would have done a similar job when it comes to avoiding clutter, but that would mean (a) a lot of unnecessary details, such as outliers, would be visible and might attract the user’s attention, and (b) t-viSNE would show several scatterplots at the same time, which could be confusing for the user.
  - Fernstad et al. [37] use combinations of quality measures to determine the most interesting dimensions of the data and guide user exploration. t-viSNE is similar to these works in its use of measures to guide the user’s exploration, but we use measures and mappings that are either specific to t-SNE’s algorithm or customized to be more useful in this scenario.
- Avoid when:
  - The main goal here is not to show the 25 best projections, but the most diverse ones; it is then the task of users— through visual exploration and by matching their own personal preferences—to choose the one that looks more promising. © 2020 IEEE.
  - While this might be useful for quick overviews or automatic selection of projections, a single score fails to capture more intricate details, such as where and why a projection is good or bad [27].
- Failure modes:
  - As she does not have any special preference, she selects the top-left projection, because the projections are sorted from best to worst based on the average of all the provided quality metrics.

# Metrics Mentioned
- `trustworthiness`: referenced as part of projection-quality or reliability assessment.
- `continuity`: referenced as part of projection-quality or reliability assessment.
- `stress`: referenced as part of projection-quality or reliability assessment.
- `procrustes-based quality`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- The second option of the Visual Mapping panel, theRemaining Cost, indicates (in the points’ sizes, by default) the final value of KLD(Pi∥Qi) for each instance xi, i.e., the remaining cost for each instance after the last iteration of t-SNE’s optimization procedure (see Section 3).
- 4.1 Goal 1: Hyper-parameter Exploration Significantly-different t-SNE projections can be generated from the same data set, due to its well-known sensitivity to hyperparameter settings [14].
- The answers to Q.1.2 also show that t-viSNE users needed fewer iterations to find a good parameter setting.
- In this work, we present t-viSNE, an interactive tool for the visual exploration of t-SNE projections that enables analysts to inspect different aspects of their accuracy and meaning, such as the effects of hyper-parameters, distance and neighborhood preservation, densities and costs of specific neighborhoods, and the correlations between dimensions and visual patterns.
- The search for a Q that faithfully represents P in a lowdimensional space is done by optimizing a cost function ( C) given by the Kullback-Leibler ( KL) divergence between the two distributions, C = KL(P∥Q) = ∑ i KL(Pi∥Qi), KL(Pi∥Qi) = ∑ j pi jlog pi j qi j , (3) which is performed with gradient descent for a user-specified number of iterations.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-113-C1 | stance: support | summary: In contrast to other, more general approaches, t-viSNE was designed with the specific problems related to the investigation of t-SNE projections in mind, bringing to light some of the hidden internal workings of the algorithm which, when visualized, may provide important insights about the high-dimensional data set under analysis. | evidence_ids: PENDING-REF-113-E1, PENDING-REF-113-E2
- CLAIM-PENDING-REF-113-C2 | stance: support | summary: In contrast to other, more general approaches, t-viSNE was designed with the specific problems related to the investigation of t-SNE projections in mind, bringing to light some of the hidden internal workings of the algorithm which, when visualized, may provide important insights about the high-dimensional data set under analysis. | evidence_ids: PENDING-REF-113-E3, PENDING-REF-113-E4
- CLAIM-PENDING-REF-113-C3 | stance: support | summary: The second option of the Visual Mapping panel, theRemaining Cost, indicates (in the points’ sizes, by default) the final value of KLD(Pi∥Qi) for each instance xi, i.e., the remaining cost for each instance after the last iteration of t-SNE’s optimization procedure (see Section 3). | evidence_ids: PENDING-REF-113-E5, PENDING-REF-113-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-REF-113-E1 | page: 1, section: extracted, quote: "In contrast to other, more general approaches, t-viSNE was designed with the specific problems related to the investigation of t-SNE projections in mind, bringing to light some of the hidden internal workings of the algorithm which, when visualized, may provide important insights about the high-dimensional data set under analysis."
- PENDING-REF-113-E2 | page: 1, section: extracted, quote: "The problem that DR tries to solve is, in general, to find a low-dimensional representation of a high-dimensional data set that retains—as much as possible—its original structure."
- PENDING-REF-113-E3 | page: 13, section: extracted, quote: "While this is of course based on subjective user feedback, we consider that it is nonetheless an important aspect of the results; since both t-viSNE and GEP mainly aim to support the exploratory visual analysis of high-dimensional data—through many different coordinated views and interactive tools—it may become hard to set a single, concrete ground-truth for evaluating their perfomance as a whole."
- PENDING-REF-113-E4 | page: 3, section: extracted, quote: "2.3 Interpretation of Projections Some attempts to enrich scatterplots with automatically-derived statistical descriptions of patterns [38], [39], [40] have shown that static mappings may be useful in simple scenarios, but the complex relations between low- and high-dimensional space in non-linear projections cannot be well represented."
- PENDING-REF-113-E5 | page: 16, section: extracted, quote: "Other DR Methods Although our main design goal was to support the investigation of t-SNE projections, most of our views and interaction techniques are not strictly confined to the t-SNE algorithm."
- PENDING-REF-113-E6 | page: 1, section: extracted, quote: "In this work, we present t-viSNE, an interactive tool for the visual exploration of t-SNE projections that enables analysts to inspect different aspects of their accuracy and meaning, such as the effects of hyper-parameters, distance and neighborhood preservation, densities and costs of specific neighborhoods, and the correlations between dimensions and visual patterns."
- PENDING-REF-113-E7 | page: 16, section: extracted, quote: "We also evaluated our approach with a user study by comparing it with Google’s Embedding Projector (GEP): the results show that, in general, the participants could manage to reach the intended analysis tasks even with limited training, and their feedback indicates that t-viSNE reached a better level of support for the given tasks than GEP."
- PENDING-REF-113-E8 | page: 1, section: extracted, quote: "Martins, Member, IEEE Computer Society , and Andreas Kerren, Senior Member, IEEE Abstract—t-Distributed Stochastic Neighbor Embedding (t-SNE) for the visualization of multidimensional data has proven to be a popular approach, with successful applications in a wide range of domains."
