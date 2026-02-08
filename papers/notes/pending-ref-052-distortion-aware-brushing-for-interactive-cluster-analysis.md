---
id: paper-2022-pending-ref-052
title: "Distortion-Aware Brushing for Reliable Cluster Analysis in Multidimensional Projections"
authors: "Hyeon Jeon, Michael Aupetit, Soohyun Lee, Hyung-Kwon Ko, Youngtaek Kim, and Jinwook Seo"
venue: "IEEE Transactions on Visualization and Computer Graphics"
year: 2022
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-052-2022-distortion-aware-brushing-for-interactive-cluster-analysis-in-multidimensional-projec.pdf
seed_note_id: "paper-2025-jeon-reliable-va-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- 4.2.3 Contextualization within the Original Projection The point relocation mechanism corrects distortions around the brushed points ( O2) but can introduce new distortions elsewhere in the MDP, making it difficult for users to understand the brushed cluster in the context of the original MDP.
- However, applying conventional brushing to 2D representations of multidimensional (MD) data, i.e., Multidimensional Projections (MDPs), can lead to unreliable cluster analysis due to MDP-induced distortions that inaccurately represent the cluster structure of the original MD data.
- O2Allow brushing to be robust against any MDP distortions Previous brushing approaches lead to unreliable cluster analysis as they rely on a compact 2D projection region, which is vulnerable to MDP distortions.
- Therefore, using PCA, participants can experience each brushing technique’s capability to address distortions without being frustrated by the task’s difficulty.

# Method Summary
- We proposeDistortion-aware brushing, a novel brushing technique designed to overcome these issues, enabling users to more accurately identify MD clusters from their 2D projections compared to existing techniques.
- O2Allow brushing to be robust against any MDP distortions Previous brushing approaches lead to unreliable cluster analysis as they rely on a compact 2D projection region, which is vulnerable to MDP distortions.
- MDPs are often created through dimensionality reduction algorithms, e.g.,t-SNE [12], or by mapping two attributes onto thexandyaxes (i.e., orthogonal projections).
- We present a use case leveraging this utility in supporting the visual-interactive labeling [64], [65] for data with noisy MD clusters and distorted projections.
- 5.2 User Study 2: Robustness Against the NonTriviality of Multidimensional Cluster Shape 5.2.1 Objectives and Design We aim to investigate the robustness of Distortion-aware brushing in maintaining user performances (task accuracy and completion time) against the non-triviality of cluster shapes.
- 4.2.3 Contextualization within the Original Projection The point relocation mechanism corrects distortions around the brushed points ( O2) but can introduce new distortions elsewhere in the MDP, making it difficult for users to understand the brushed cluster in the context of the original MDP.
- However, applying conventional brushing to 2D representations of multidimensional (MD) data, i.e., Multidimensional Projections (MDPs), can lead to unreliable cluster analysis due to MDP-induced distortions that inaccurately represent the cluster structure of the original MD data.

# When To Use / Not Use
- Use when:
  - It is important to avoid using every point covered by the painter as seed points because they may consist of points coming from two or more distinct MD clusters due to FN; if this happens, new points brushed from these distinct MD clusters will erroneously agglomerate into a single visual cluster ( O1 O2).
  - 5.2 User Study 2: Robustness Against the NonTriviality of Multidimensional Cluster Shape 5.2.1 Objectives and Design We aim to investigate the robustness of Distortion-aware brushing in maintaining user performances (task accuracy and completion time) against the non-triviality of cluster shapes.
- Avoid when:
  - We useCH btwn as the index is proven to work robustly and fairly regardless of the dimensionality [19], [47] Then, for each stimulus, we select pairs of classes in the MNIST dataset that are mutually separable with aCH btwn separability index higher than the separability threshold.
  - Our user studies demonstrated the usefulness and usability of Distortion-aware brushing in exploring and discovering MD clusters, its robustness to distortions, and its greater accuracy compared to state-of-the-art brushing techniques.
- Failure modes:
  - 5.1 User Study 1: Robustness Against Distortions 5.1.1 Objectives and Design We aim to compare Distortion-aware brushing with baselines regarding accuracy in capturing MD clusters and their robustness to the amount of DR distortions.

# Metrics Mentioned
- `trustworthiness`: referenced as part of projection-quality or reliability assessment.
- `continuity`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- Another potential use case of Distortion-aware brushing is to compare the hyperparameter settings of machine learning models, where Distortion-aware brushing could help users compare different hyperparameter settings, identify a group of optimal configurations, and gain insight into how their variations affect model performance.
- Moreover, Distortion-aware brushing is intentionally designed with minimal hyperparameters ( O4), reducing variability from extensive hyperparameter tuning, which is a common pitfall in automated clustering algorithms.
- We use a convex hull as it is computationally cheap (O(nlogn)fornpoints) while tightly enclosing the brushed points compared to alternatives (e.g., boundary circle) and has no hyperparameter to tune ( O4).
- O4Minimize the number of hand-tuned hyperparameters Previous brushing techniques have at most one hyperparameter that affects brushing results, making them easy to use and learn.
- Similarly, we design Distortion-aware brushing to havea single hyperparameter that affects the granularity of the brushed clusters and make its value automatically optimized.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-052-C1 | stance: support | summary: 4.2.3 Contextualization within the Original Projection The point relocation mechanism corrects distortions around the brushed points ( O2) but can introduce new distortions elsewhere in the MDP, making it difficult for users to understand the brushed cluster in the context of the original MDP. | evidence_ids: PENDING-REF-052-E1, PENDING-REF-052-E2
- CLAIM-PENDING-REF-052-C2 | stance: support | summary: We proposeDistortion-aware brushing, a novel brushing technique designed to overcome these issues, enabling users to more accurately identify MD clusters from their 2D projections compared to existing techniques. | evidence_ids: PENDING-REF-052-E3, PENDING-REF-052-E4
- CLAIM-PENDING-REF-052-C3 | stance: support | summary: Another potential use case of Distortion-aware brushing is to compare the hyperparameter settings of machine learning models, where Distortion-aware brushing could help users compare different hyperparameter settings, identify a group of optimal configurations, and gain insight into how their variations affect model performance. | evidence_ids: PENDING-REF-052-E5, PENDING-REF-052-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 4 | relevance: high | note: contains initialization sensitivity or control-policy evidence

# Evidence
- PENDING-REF-052-E1 | page: 7, section: extracted, quote: "4.2.3 Contextualization within the Original Projection The point relocation mechanism corrects distortions around the brushed points ( O2) but can introduce new distortions elsewhere in the MDP, making it difficult for users to understand the brushed cluster in the context of the original MDP."
- PENDING-REF-052-E2 | page: 1, section: extracted, quote: "However, applying conventional brushing to 2D representations of multidimensional (MD) data, i.e., Multidimensional Projections (MDPs), can lead to unreliable cluster analysis due to MDP-induced distortions that inaccurately represent the cluster structure of the original MD data."
- PENDING-REF-052-E3 | page: 3, section: extracted, quote: "O2Allow brushing to be robust against any MDP distortions Previous brushing approaches lead to unreliable cluster analysis as they rely on a compact 2D projection region, which is vulnerable to MDP distortions."
- PENDING-REF-052-E4 | page: 8, section: extracted, quote: "Therefore, using PCA, participants can experience each brushing technique’s capability to address distortions without being frustrated by the task’s difficulty."
- PENDING-REF-052-E5 | page: 1, section: extracted, quote: "We proposeDistortion-aware brushing, a novel brushing technique designed to overcome these issues, enabling users to more accurately identify MD clusters from their 2D projections compared to existing techniques."
- PENDING-REF-052-E6 | page: 1, section: extracted, quote: "MDPs are often created through dimensionality reduction algorithms, e.g.,t-SNE [12], or by mapping two attributes onto thexandyaxes (i.e., orthogonal projections)."
- PENDING-REF-052-E7 | page: 14, section: extracted, quote: "We present a use case leveraging this utility in supporting the visual-interactive labeling [64], [65] for data with noisy MD clusters and distorted projections."
- PENDING-REF-052-E8 | page: 10, section: extracted, quote: "5.2 User Study 2: Robustness Against the NonTriviality of Multidimensional Cluster Shape 5.2.1 Objectives and Design We aim to investigate the robustness of Distortion-aware brushing in maintaining user performances (task accuracy and completion time) against the non-triviality of cluster shapes."
