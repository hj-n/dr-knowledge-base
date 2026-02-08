---
id: paper-2021-pending-ref-144
title: "A survey of visual analytics techniques for machine learning"
authors: "J. Y uan, C. Chen, W. Y ang, M. Liu, J. Xia, and S. Liu"
venue: "Computational Visual Media"
year: 2021
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-144-2021-a-survey-of-visual-analytics-techniques-for-machine-learning.pdf
seed_note_id: "paper-2022-revisiting-dr-visual-cluster-analysis"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- The major challenges here are how to (i) visually represent the evolution patterns of streaming data over time and eﬀectively compare data distributions at diﬀerent points in time, and (ii) tightly integrate such streaming data visualization with drift detection and adaptation algorithms to form an interactive and progressive analysis environment with the human in the loop.
- In order to address the scalability problem, data are aggregated in a hierarchy based on metainformation, which enables analysis of a group of anomalies ( e.g. abnormal time series of the same type) simultaneously.
- 5 Techniques after Model Building Existing visual analytics eﬀorts after model building aim to help users understand and gain insights from model outputs, such as high-dimensional data analysis results [158, 162].
- Earlier works employ directed graph layouts to visualize the structure of neural networks [245], but visual clutter becomes a serious problem as the model structure becoming increasingly complex.

# Method Summary
- 2 OoDAnalyzer [45], an interactive method to detect out-of-distribution samples and explain them in context. the exploration, a kNN-based grid layout algorithm motivated by Hall’s theorem was developed.
- Previously, these tasks were mainly conducted manually or by automatic methods, such as learning-from-crowds algorithms [108] which aim to estimate ground-truth labels from noisy crowd-sourced labels.
- A graph matching algorithm is then developed to match the topic graphs from diﬀerent sources, and a hierarchical clustering method is employed to generate hierarchies of topic graphs.
- A hierarchical visualization combined with an incremental projection method and an outlier biased sampling method facilitate the exploration and identiﬁcation of trusted items.
- The major challenges here are how to (i) visually represent the evolution patterns of streaming data over time and eﬀectively compare data distributions at diﬀerent points in time, and (ii) tightly integrate such streaming data visualization with drift detection and adaptation algorithms to form an interactive and progressive analysis environment with the human in the loop.
- Therefore, a word2Vec model was used to generate the vectorized representation for each origin-destination ﬂow. t-SNE was then employed to project the embedding of the ﬂows into two-dimensional space, where analysts can check the distributions of the origin-destination ﬂows and select some for display on the map.
- 5.1.1 Textual Data Analysis The most widely studied topic is visual text analytics, which tightly integrates interactive visualization techniques with text mining techniques (e.g. document clustering, topic models, and word embedding) to help users better understand a large amount of textual data [162].

# When To Use / Not Use
- Use when:
  - Then at the detail level, it uses segment clustering and a pattern mining algorithm to help experts identify common as well as suspicious patterns in the event-sequences of the agents in Q-networks.
  - As data have the risk of exposing sensitive information, several recent studies have focused on preserving data privacy during the data quality improvement process.
- Avoid when:
  - Therefore, later works have focused on understanding relationships between topics ( e.g. topic splitting and merging) and their evolving patterns over time.
  - However, these works use a ﬂat structure to model topics, which hampers their usage in the era of big data for handling large-scale text corpora.
- Failure modes:
  - Several works have focused on incorporating user knowledge into topic models to improve their results [53, 69, 73, 127, 262, 283].

# Metrics Mentioned
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- It creates a collection of regression models by varying algorithms and their corresponding hyperparameters, with further optimization by interactive weighting of data instances and interactive feature selection and weighting.
- Model understanding methods aim to visually explain the working mechanisms of a model, such as how changes in parameters inﬂuence the model and why the model gives a certain output for a speciﬁc input.
- For example, Ferreira et al. [79] developed BirdVis to explore the relationships between diﬀerent parameter conﬁgurations and model outputs; these were bird occurrence predictions in their application.
- One possible direction is that since the reﬁnement process usually requires several iterations, guidance in later iterations can be learned from users’ previous interactions.
- 4.1 Model Understanding Works related to model understanding belong to two classes: those understanding the eﬀects of parameters, and those understanding model behaviours.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-144-C1 | stance: support | summary: The major challenges here are how to (i) visually represent the evolution patterns of streaming data over time and eﬀectively compare data distributions at diﬀerent points in time, and (ii) tightly integrate such streaming data visualization with drift detection and adaptation algorithms to form an interactive and progressive analysis environment with the human in the loop. | evidence_ids: PENDING-REF-144-E1, PENDING-REF-144-E2
- CLAIM-PENDING-REF-144-C2 | stance: support | summary: 2 OoDAnalyzer [45], an interactive method to detect out-of-distribution samples and explain them in context. the exploration, a kNN-based grid layout algorithm motivated by Hall’s theorem was developed. | evidence_ids: PENDING-REF-144-E3, PENDING-REF-144-E4
- CLAIM-PENDING-REF-144-C3 | stance: support | summary: It creates a collection of regression models by varying algorithms and their corresponding hyperparameters, with further optimization by interactive weighting of data instances and interactive feature selection and weighting. | evidence_ids: PENDING-REF-144-E5, PENDING-REF-144-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-REF-144-E1 | page: 17, section: extracted, quote: "The major challenges here are how to (i) visually represent the evolution patterns of streaming data over time and eﬀectively compare data distributions at diﬀerent points in time, and (ii) tightly integrate such streaming data visualization with drift detection and adaptation algorithms to form an interactive and progressive analysis environment with the human in the loop."
- PENDING-REF-144-E2 | page: 5, section: extracted, quote: "In order to address the scalability problem, data are aggregated in a hierarchy based on metainformation, which enables analysis of a group of anomalies ( e.g. abnormal time series of the same type) simultaneously."
- PENDING-REF-144-E3 | page: 12, section: extracted, quote: "5 Techniques after Model Building Existing visual analytics eﬀorts after model building aim to help users understand and gain insights from model outputs, such as high-dimensional data analysis results [158, 162]."
- PENDING-REF-144-E4 | page: 9, section: extracted, quote: "Earlier works employ directed graph layouts to visualize the structure of neural networks [245], but visual clutter becomes a serious problem as the model structure becoming increasingly complex."
- PENDING-REF-144-E5 | page: 5, section: extracted, quote: "2 OoDAnalyzer [45], an interactive method to detect out-of-distribution samples and explain them in context. the exploration, a kNN-based grid layout algorithm motivated by Hall’s theorem was developed."
- PENDING-REF-144-E6 | page: 2, section: extracted, quote: "Previously, these tasks were mainly conducted manually or by automatic methods, such as learning-from-crowds algorithms [108] which aim to estimate ground-truth labels from noisy crowd-sourced labels."
- PENDING-REF-144-E7 | page: 13, section: extracted, quote: "A graph matching algorithm is then developed to match the topic graphs from diﬀerent sources, and a hierarchical clustering method is employed to generate hierarchies of topic graphs."
- PENDING-REF-144-E8 | page: 6, section: extracted, quote: "A hierarchical visualization combined with an incremental projection method and an outlier biased sampling method facilitate the exploration and identiﬁcation of trusted items."
