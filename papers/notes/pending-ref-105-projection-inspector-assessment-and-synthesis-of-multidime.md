---
id: paper-2015-pending-ref-105
title: "Projection inspector: Assessment and synthesis of multidimensional projections"
authors: "P. Pagliosa, F. Paulovich, R. Minghim, H. Levkowitz, and L. G. Nonato"
venue: "Journal of Cheminformatics"
year: 2015
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-105-2015-projection-inspector-assessment-and-synthesis-of-multidimensional-projections.pdf
seed_note_id: "paper-2019-mdp-visual-analytics-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- To support the analysis of large sets of compounds, cheminformatics tools allow users to explore the data by means of exploratory visualization techniques, for example by projecting a high-dimensional space into a low-dimensional space and enabling interactivity.
- To solve this problem, we serialize this kind of data and store it in a single additional column for later use.

# Method Summary
- Here we present our findings related to one specific group that contains 26 compounds with high structural similarity (see Supple - mentary Material, Additional File 1 for a detailed view of the group and projection).
- Task Understand is addressed by a few approaches [30– 32] that utilize various XAI methods to highlight contributions of compound substructures.
- As part of future work, we plan to provide more projection and clustering algorithms directly within the tool.
- The projection algorithm placed the compounds with positive predictions mostly at the top-right area.
- CIME can also be enhanced programmatically by users to include additional projection methods.
- 1 Data scientists create models that predict molecular properties and XAI reveals logic connecting substructures to the prediction: (left) a compound of interest is selected for inspection; (center) contributions for the predicted property of interest are calculated with an XAI method that delivers one score for each atom; (right) overlaying a molecular structure with those atom-scores Page 3 of 14 Humer et al.
- How: (a) users have two models with similar accu - racy and compare their explanations to select that which is more consistent with chemical knowledge; (b) users compare the predictions of two models and identify specific regions of the chemical space in which both models perform poorly; (c) users com - pare explanations from two XAI methods and iden - tify agreements and disagreements.

# When To Use / Not Use
- Use when:
  - Another limitation of the tool is its inability to save its current state, which means that users must show their live analyses directly to collaborators or make screen - shots to document the results.
  - How: (a) users have two models with similar accu - racy and compare their explanations to select that which is more consistent with chemical knowledge; (b) users compare the predictions of two models and identify specific regions of the chemical space in which both models perform poorly; (c) users com - pare explanations from two XAI methods and iden - tify agreements and disagreements.
- Avoid when:
  - Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made.
  - Projection view Once users have uploaded a file, data points are shown in a two-dimensional scatterplot with random initial positions—if x and y coordinates are not explicitly pro - vided—and can be projected using Uniform Manifold Approximation and Projection (UMAP , [48]) as dimen - sionality reduction (DR) technique.
- Failure modes:
  - Journal of Cheminformatics (2022) 14:21 Tools with exploratory functionalities designed for chemical spaces [19, 22– 26] and molecular-represen - tation methods [27– 29] can be used for the purpose of Task Explore; tools that were not designed for chemical data, can also be used, but may limit the analysis.

# Metrics Mentioned
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- The API call takes as input a list of x and y coordinates, and custom hyperparameters.
- Journal of Cheminformatics (2022) 14:21 Use case 2: comparing the attributions of models trained on physico‑chemical properties Lipophilicity is an important parameter in medicinal chemistry, related to the pharmacokinetic properties of a drug [56].
- Task Understand is addressed by a few approaches [30– 32] that utilize various XAI methods to highlight contributions of compound substructures.
- As part of future work, we plan to provide more projection and clustering algorithms directly within the tool.
- The projection algorithm placed the compounds with positive predictions mostly at the top-right area.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-105-C1 | stance: support | summary: To support the analysis of large sets of compounds, cheminformatics tools allow users to explore the data by means of exploratory visualization techniques, for example by projecting a high-dimensional space into a low-dimensional space and enabling interactivity. | evidence_ids: PENDING-REF-105-E1, PENDING-REF-105-E2
- CLAIM-PENDING-REF-105-C2 | stance: support | summary: Here we present our findings related to one specific group that contains 26 compounds with high structural similarity (see Supple - mentary Material, Additional File 1 for a detailed view of the group and projection). | evidence_ids: PENDING-REF-105-E3, PENDING-REF-105-E4
- CLAIM-PENDING-REF-105-C3 | stance: support | summary: The API call takes as input a list of x and y coordinates, and custom hyperparameters. | evidence_ids: PENDING-REF-105-E5, PENDING-REF-105-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 4 | relevance: high | note: contains initialization sensitivity or control-policy evidence

# Evidence
- PENDING-REF-105-E1 | page: 2, section: extracted, quote: "To support the analysis of large sets of compounds, cheminformatics tools allow users to explore the data by means of exploratory visualization techniques, for example by projecting a high-dimensional space into a low-dimensional space and enabling interactivity."
- PENDING-REF-105-E2 | page: 4, section: extracted, quote: "To solve this problem, we serialize this kind of data and store it in a single additional column for later use."
- PENDING-REF-105-E3 | page: 8, section: extracted, quote: "Here we present our findings related to one specific group that contains 26 compounds with high structural similarity (see Supple - mentary Material, Additional File 1 for a detailed view of the group and projection)."
- PENDING-REF-105-E4 | page: 3, section: extracted, quote: "Task Understand is addressed by a few approaches [30– 32] that utilize various XAI methods to highlight contributions of compound substructures."
- PENDING-REF-105-E5 | page: 12, section: extracted, quote: "As part of future work, we plan to provide more projection and clustering algorithms directly within the tool."
- PENDING-REF-105-E6 | page: 7, section: extracted, quote: "The projection algorithm placed the compounds with positive predictions mostly at the top-right area."
- PENDING-REF-105-E7 | page: 12, section: extracted, quote: "CIME can also be enhanced programmatically by users to include additional projection methods."
- PENDING-REF-105-E8 | page: 2, section: extracted, quote: "1 Data scientists create models that predict molecular properties and XAI reveals logic connecting substructures to the prediction: (left) a compound of interest is selected for inspection; (center) contributions for the predicted property of interest are calculated with an XAI method that delivers one score for each atom; (right) overlaying a molecular structure with those atom-scores Page 3 of 14 Humer et al."
