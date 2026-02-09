---
id: paper-2010-pending-ref-067
title: "iVisClassifier: An interactive visual analytics system for classification based on supervised dimension reduction"
authors: "Jaegul Choo, Hanseung Lee, Jaeyeon Kihm, and Haesun Park"
venue: "Computer Graphics Forum"
year: 2010
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-067-2010-ivisclassifier-an-interactive-visual-analytics-system-for-classification-based-on-sup.pdf
seed_note_id: "paper-2025-jeon-reliable-va-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- Medicine, for example, is one of the fields where the use of ML might offer potential improvements and solutions to many difficult problems [KKS ∗19, SGSG19, SKK∗19].
- 25, 28 [LWBP14] L IU S., WANG B., B REMER P.-T., PASCUCCI V.: Distortionguided structure-driven interactive exploration of high-dimensional data.
- For us researchers, it was difficult to see how the data was collected e.g. patients could do a certain daily activity (e.g. cutting grass) but in our model we accounted that as tremor.” Another important point that was brought up is that visualization-based steering of the ML training process might push the user to “fish” for desired results and invalidate the statistical significance of the model.
- Related Surveys The challenge of enhancing trust in ML models has not yet received the same level of attention in systematic surveys as other topics, for example, the understanding and interpretation of DR or deep learn- © 2020 The Author(s) Computer Graphics Forum © 2020 The Eurographics Association and John Wiley & Sons Ltd. © 2020 The Eurographics Association and John Wiley & Sons Ltd.

# Method Summary
- Visual Representation 199 Bar Charts 82 Box Plots 11 Matrix 50 Glyphs / Icons / Thumbnails 63 Grid-based Approaches 19 Heatmaps 46 Histograms 56 Icicle Plots 6 Line Charts 56 Node-link Diagrams 47 Parallel Coordinates Plots (PCPs) 32 Pixel-based Approaches 8 Radial Layouts 22 Scatterplot Matrices (SPLOMs) 18 Scatterplot / Projections 115 Similarity Layouts 27 Tables / Lists 86 Treemaps 5 Other 59 6.5.5.
- It can be divided into five TLs related to trustworthiness of the following: the raw data (→TL1), the processed data (→TL2), the learning method (i.e., the algorithms) (→TL3), the concrete model(s) for a particular task (→TL4), and the evaluation and the subjective users’ expectations (→TL5).
- This is a very restricted approach when compared to our concept of trust, which should be ensured at various levels, such as data, learning method, concrete model(s), visualizations themselves, and covering users expectations.
- The method designed by Zhou et al. [ZLH ∗16], for example, combines both aspects to enable users to design new dimensions from data projections of subspaces, with the goal of maintaining important cluster information.
- With the termalgorithm, we define an ML method (e.g., logistic regression or random forest); in contrast to a model which is the result of an algorithm and is trained with specific parameters.
- Notice that this category focuses on particular instances, while the source reliability category described previously, considers data globally. • Learning method/algorithms (TL3).
- This final step of the ML pipeline consists of turning its inputs, mainly a set of ML learning methods/algorithms, into a concrete model or a combination of models [SKKC19].

# When To Use / Not Use
- Use when:
  - The final version of this record is available at: 10.1111/cgf.14034 Chatzimparmpas et al. / Enhancing Trust in Machine Learning Models with the Use of Visualizations [BHJ09] B ASTIAN M., H EYMANN S., J ACOMY M.: Gephi: An open source software for exploring and manipulating networks.
  - The impact of this problem can already be observed in recent works, such as the program “Explainable AI (XAI)” founded by DARPA (Defense Advanced Research Projects Agency) [Dar20] and described by Krause et al. [KDS ∗17].
- Avoid when:
  - A paper from Nalcaci et al. [NGB ∗19], for example, works with distinction bias and confirmation bias in visualization systems that are related to user bias when viewing visualizations.
  - Undoubtedly, learned features of convolutional neural networks (CNNs) are a first step to provide trust to users for the models.
- Failure modes:
  - High bias can cause a model to avoid seeing the relevant associations between features and target outputs, thus underfitting.

# Metrics Mentioned
- `trustworthiness`: referenced as part of projection-quality or reliability assessment.
- `continuity`: referenced as part of projection-quality or reliability assessment.
- `stress`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- Clustering and Dimensionality Reduction Sacha et al. [SZS ∗17] propose, in their survey, a detailed categorization with seven guiding scenarios for interactive DR: (i) data selection and emphasis, (ii) annotation and labeling, (iii) data manipulation, (iv) feature selection and emphasis, (v) DR parameter tuning, (vi) defining constraints, and (vii)DR type selection.
- Additionally, out of all the specific concepts and ideas that emerged, the most popular were the visualization of feature importance (4 answers), the impact of different characteristics of the data instances (4 answers), investigation of hyper-parameters (3 answers), visualizing the pre-processing steps (3 answers), and the evaluation of the model (3 answers).
- Factors such as visualizing details of the source of the data (Q1), data quality issues (Q3), performance comparison of different ML algorithms (Q4), hyper-parameter tuning (Q5), exploration of “what-if” scenarios (Q11), and investigation of fairness (Q12) obtained the majority of votes on score 5.
- A potential question is: “What is the consequence if we change one parameter and keep the rest stable for a specific model, or select some points to explore further?” Model bias and model variance are well-known concepts originating from statistics with regard to the bias-variance trade-off.
- 17 [PSMD14] P ADUA L., S CHULZE H., M ATKOVI ´C K., D ELRIEUX C.: Interactive exploration of parameter space in data mining: Comprehending the predictive quality of large decision tree collections.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-067-C1 | stance: support | summary: Medicine, for example, is one of the fields where the use of ML might offer potential improvements and solutions to many difficult problems [KKS ∗19, SGSG19, SKK∗19]. | evidence_ids: PENDING-REF-067-E1, PENDING-REF-067-E2
- CLAIM-PENDING-REF-067-C2 | stance: support | summary: Visual Representation 199 Bar Charts 82 Box Plots 11 Matrix 50 Glyphs / Icons / Thumbnails 63 Grid-based Approaches 19 Heatmaps 46 Histograms 56 Icicle Plots 6 Line Charts 56 Node-link Diagrams 47 Parallel Coordinates Plots (PCPs) 32 Pixel-based Approaches 8 Radial Layouts 22 Scatterplot Matrices (SPLOMs) 18 Scatterplot / Projections 115 Similarity Layouts 27 Tables / Lists 86 Treemaps 5 Other 59 6.5.5. | evidence_ids: PENDING-REF-067-E3, PENDING-REF-067-E4
- CLAIM-PENDING-REF-067-C3 | stance: support | summary: Clustering and Dimensionality Reduction Sacha et al. [SZS ∗17] propose, in their survey, a detailed categorization with seven guiding scenarios for interactive DR: (i) data selection and emphasis, (ii) annotation and labeling, (iii) data manipulation, (iv) feature selection and emphasis, (v) DR parameter tuning, (vi) defining constraints, and (vii)DR type selection. | evidence_ids: PENDING-REF-067-E5, PENDING-REF-067-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-REF-067-E1 | page: 1, section: extracted, quote: "Medicine, for example, is one of the fields where the use of ML might offer potential improvements and solutions to many difficult problems [KKS ∗19, SGSG19, SKK∗19]."
- PENDING-REF-067-E2 | page: 37, section: extracted, quote: "25, 28 [LWBP14] L IU S., WANG B., B REMER P.-T., PASCUCCI V.: Distortionguided structure-driven interactive exploration of high-dimensional data."
- PENDING-REF-067-E3 | page: 4, section: extracted, quote: "For us researchers, it was difficult to see how the data was collected e.g. patients could do a certain daily activity (e.g. cutting grass) but in our model we accounted that as tremor.” Another important point that was brought up is that visualization-based steering of the ML training process might push the user to “fish” for desired results and invalidate the statistical significance of the model."
- PENDING-REF-067-E4 | page: 7, section: extracted, quote: "Related Surveys The challenge of enhancing trust in ML models has not yet received the same level of attention in systematic surveys as other topics, for example, the understanding and interpretation of DR or deep learn- © 2020 The Author(s) Computer Graphics Forum © 2020 The Eurographics Association and John Wiley & Sons Ltd. © 2020 The Eurographics Association and John Wiley & Sons Ltd."
- PENDING-REF-067-E5 | page: 14, section: extracted, quote: "Visual Representation 199 Bar Charts 82 Box Plots 11 Matrix 50 Glyphs / Icons / Thumbnails 63 Grid-based Approaches 19 Heatmaps 46 Histograms 56 Icicle Plots 6 Line Charts 56 Node-link Diagrams 47 Parallel Coordinates Plots (PCPs) 32 Pixel-based Approaches 8 Radial Layouts 22 Scatterplot Matrices (SPLOMs) 18 Scatterplot / Projections 115 Similarity Layouts 27 Tables / Lists 86 Treemaps 5 Other 59 6.5.5."
- PENDING-REF-067-E6 | page: 5, section: extracted, quote: "It can be divided into five TLs related to trustworthiness of the following: the raw data (→TL1), the processed data (→TL2), the learning method (i.e., the algorithms) (→TL3), the concrete model(s) for a particular task (→TL4), and the evaluation and the subjective users’ expectations (→TL5)."
- PENDING-REF-067-E7 | page: 9, section: extracted, quote: "This is a very restricted approach when compared to our concept of trust, which should be ensured at various levels, such as data, learning method, concrete model(s), visualizations themselves, and covering users expectations."
- PENDING-REF-067-E8 | page: 15, section: extracted, quote: "The method designed by Zhou et al. [ZLH ∗16], for example, combines both aspects to enable users to design new dimensions from data projections of subspaces, with the goal of maintaining important cluster information."
