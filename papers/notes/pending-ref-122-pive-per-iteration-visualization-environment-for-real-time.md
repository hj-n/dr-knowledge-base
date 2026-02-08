---
id: paper-2017-pending-ref-122
title: "PIVE: Per-Iteration Visualization Environment for Real-Time Interactions with Dimension Reduction and Clustering"
authors: "Hannah Kim, Jaegul Choo, Changhyun Lee, Hanseung Lee, Chandan Reddy, and Haesun Park"
venue: "Proceedings of the AAAI Conference on Artificial Intelligence"
year: 2017
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-122-2017-pive-per-iteration-visualization-environment-for-real-time-interactions-with-dimensio.pdf
seed_note_id: "paper-2025-jeon-reliable-va-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- To tackle this problem, this paper presents PIVE (Per-Iteration Visualization Environment) that supports real-time interactive visualization with machine learning.
- 3.3 Further Considerations Stability and Convergence 1 PIVE poses a challenge as the difﬁculty in deciding when to start interactions with machine learning.
- This can be useful in ﬁnding a better local optimum for non-convex problems or ﬁnding a good initialization in a user’s own manner.
- These interactions can reveal interesting knowledge about high-dimensional data relationships without additional computations.

# Method Summary
- In response, we propose a novel approach called PIVE (Per-Iteration Visualization Environment), which visualizes the intermediate results from algorithm iterations as soon as they become available, achieving an efﬁcient real-time interactive visualization with machine learning.
- In contrast, PIVE (b) splits a machine learning method into iterations, visualizing and interacting with intermediate results during iterations. popular approaches relied upon multi-threading techniques to separate data processing and computation from visualization and rendering (Ma 2009; Y u et al.
- Unlike many previous approaches that treat a machine learning method as a black box, PIVE breaks it down to an iteration level and tightly integrates them with visual analytics so that a user can check and interact with the visualization of machine learning outputs.
- Furthermore, our replacement-based methodology directly interprets a user interaction in the same form as an algorithm output, e.g., low-dimensional coordinates in dimension reduction and cluster assignments in clustering.
- In addition, we propose a widely-applicable interaction methodology that allows efﬁcient incorporation of user feedback into virtually any iterative computational method without introducing additional computational cost.
- Since such a methodology does not require any major algorithmic modiﬁcations nor computational overhead, a user can efﬁciently perform multiple interactions with machine learning in real time.
- 5 Experiments In this section, we present the analyses on the iteration-wise behaviors of machine learning methods as well as various user interaction scenarios in PIVE.

# When To Use / Not Use
- Use when:
  - Stability and Convergence For convergence measure, we use the relative number of cluster membership changes at a given iteration t with respect to the previous iteration, i.e., SCL (t)= 1 n ∑ 1≤i≤n I ( yt i ̸= yt−1 i ) . (5) By monitoring this measure over iterations, a user can check the stability of the clustering result.
  - Unlike many previous approaches that treat a machine learning method as a black box, PIVE breaks it down to an iteration level and tightly integrates them with visual analytics so that a user can check and interact with the visualization of machine learning outputs.
- Avoid when:
  - From a clustering viewpoint, the former corresponds to a cluster representative vector μj for topic cluster j, and the latter corresponds to a soft-clustering coefﬁcient, which is used to determine yi by taking the topic index with the maximum value.
  - To help determine whether the intermediate result is sufﬁciently stable and close to the ﬁnal solution, we provide users with separate charts showing the corresponding measures as well as visual encoding within existing visualizations.
- Failure modes:
  - This makes sense because these two letters ‘q’ and ‘u’ sound similar but quite different from the other previously overlapping letters, ‘b’, ‘d’, ‘e’, ‘g’, ‘p’, ‘t’, and ‘v’, all of which are pronounced with the ‘–ee’ sound at the end.

# Metrics Mentioned
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- As summarized in Algorithm 1, given a set of data items X and parameter vector α,a t t-th iteration, iterative methods reﬁne previous solution Y t−1 intoY t.
- Stability and Convergence To show the stability of intermediate outputs, we propose a quantitative measure at iteration t as an average number of the k nearest neighbor changes from the previous iteration t−1, i.e., S1 DR (t)= 1 nk ∑ 1≤i≤n ⏐⏐Nk ( yt i ) −Nk ( yt−1 i )⏐ ⏐, (3) where Nk (yt i) is the set of the k nearest neighbor data items of yt i at the iteration t.
- Stability and Convergence For convergence measure, we use the relative number of cluster membership changes at a given iteration t with respect to the previous iteration, i.e., SCL (t)= 1 n ∑ 1≤i≤n I ( yt i ̸= yt−1 i ) . (5) By monitoring this measure over iterations, a user can check the stability of the clustering result.
- In classiﬁcation and regression, the training process performed in support vector machines, decision trees, and deep neural network can signiﬁcantly beneﬁt from PIVE via interactively changing parameters, removing noisy features, and correcting misclassiﬁed data items for better prediction performance.
- In contrast, PIVE (b) splits a machine learning method into iterations, visualizing and interacting with intermediate results during iterations. popular approaches relied upon multi-threading techniques to separate data processing and computation from visualization and rendering (Ma 2009; Y u et al.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-122-C1 | stance: support | summary: To tackle this problem, this paper presents PIVE (Per-Iteration Visualization Environment) that supports real-time interactive visualization with machine learning. | evidence_ids: PENDING-REF-122-E1, PENDING-REF-122-E2
- CLAIM-PENDING-REF-122-C2 | stance: support | summary: In response, we propose a novel approach called PIVE (Per-Iteration Visualization Environment), which visualizes the intermediate results from algorithm iterations as soon as they become available, achieving an efﬁcient real-time interactive visualization with machine learning. | evidence_ids: PENDING-REF-122-E3, PENDING-REF-122-E4
- CLAIM-PENDING-REF-122-C3 | stance: support | summary: As summarized in Algorithm 1, given a set of data items X and parameter vector α,a t t-th iteration, iterative methods reﬁne previous solution Y t−1 intoY t. | evidence_ids: PENDING-REF-122-E5, PENDING-REF-122-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 4 | relevance: high | note: contains initialization sensitivity or control-policy evidence
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-REF-122-E1 | page: 1, section: extracted, quote: "To tackle this problem, this paper presents PIVE (Per-Iteration Visualization Environment) that supports real-time interactive visualization with machine learning."
- PENDING-REF-122-E2 | page: 3, section: extracted, quote: "3.3 Further Considerations Stability and Convergence 1 PIVE poses a challenge as the difﬁculty in deciding when to start interactions with machine learning."
- PENDING-REF-122-E3 | page: 3, section: extracted, quote: "This can be useful in ﬁnding a better local optimum for non-convex problems or ﬁnding a good initialization in a user’s own manner."
- PENDING-REF-122-E4 | page: 4, section: extracted, quote: "These interactions can reveal interesting knowledge about high-dimensional data relationships without additional computations."
- PENDING-REF-122-E5 | page: 1, section: extracted, quote: "In response, we propose a novel approach called PIVE (Per-Iteration Visualization Environment), which visualizes the intermediate results from algorithm iterations as soon as they become available, achieving an efﬁcient real-time interactive visualization with machine learning."
- PENDING-REF-122-E6 | page: 2, section: extracted, quote: "In contrast, PIVE (b) splits a machine learning method into iterations, visualizing and interacting with intermediate results during iterations. popular approaches relied upon multi-threading techniques to separate data processing and computation from visualization and rendering (Ma 2009; Y u et al."
- PENDING-REF-122-E7 | page: 1, section: extracted, quote: "Unlike many previous approaches that treat a machine learning method as a black box, PIVE breaks it down to an iteration level and tightly integrates them with visual analytics so that a user can check and interact with the visualization of machine learning outputs."
- PENDING-REF-122-E8 | page: 6, section: extracted, quote: "Furthermore, our replacement-based methodology directly interprets a user interaction in the same form as an algorithm output, e.g., low-dimensional coordinates in dimension reduction and cluster assignments in clustering."
