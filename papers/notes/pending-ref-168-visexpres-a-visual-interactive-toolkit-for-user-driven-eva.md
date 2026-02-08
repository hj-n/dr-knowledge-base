---
id: paper-2022-pending-ref-168
title: "VisExPreS: A Visual Interactive Toolkit for User-Driven Evaluations of Embeddings"
authors: "Aindrila Ghosh, Mona Nashaat, James Miller, and Shaikh Quader"
venue: "IEEE Transactions on Visualization and Computer Graphics"
year: 2022
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-168-2022-visexpres-a-visual-interactive-toolkit-for-user-driven-evaluations-of-embeddings.pdf
seed_note_id: "paper-2025-jeon-reliable-va-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- Li∗, Fellow, IEEE Abstract—Dimension reduction (DR) is commonly utilized to capture intrinsic structure and transform high-dimensional data into low-dimensional space while retaining meaningful properties of original data.
- To address these problems, we have developed a deep neural network method called EVNet which provides not only excellent performance in structural maintainability but also explainability to the DR therein.
- Abstract—Dimension reduction (DR) is commonly utilized to capture intrinsic structure and transform high-dimensional data into low-dimensional space while retaining meaningful properties of original data.
- TNP data is a challenging problem for traditional DR methods because of the large number of noise features and irrelevant features in the data, which are closer to the real-world data.

# Method Summary
- 8 C ONCLUSION We propose EVNet, a deep learning-based parametric approach to achieve dimension reduction embedding and three different levels of explanation.
- Can EVNet have better local structure-preserving performance? (Q3) Is the output of EVNet’s DR embedding clear and easy to understand, and what are the differences between ours as compared with t-SNE, UMAP, and other DR methods? (Q4) Whether the time consumption of EVNet is unbearable? (Q5) Whether the data augmentation hyper-parameter of EVNet is stable?
- 3.1 DR Embedding and Explainability Analysis Given a training dataset X, DR methods learn a continues function F(·) to map data X ={x1,··· , xM} (x∈ Rn, n is the number of the features, M is the number of the training data) to a latent This article has been accepted for publication in IEEE Transactions on Visualization and Computer Graphics.
- In this paper, the explanation output of the DR method includes the following aspects I ={Ig, Il, It}: (a) Global explanation (Ig), discovers the essential features of the global embedding process and evaluates the importance of these features.
- The parametric-free DR method directly optimizes the embedding output corresponding to the input data rather than learning a continuous mapping function from the input to the embedding result.
- The lasso network includes gate layer gW (·), projection layers fθ (·) is designed to handle noisy and irrelevant features and discover the globally important features for DR embedding.
- The latent space embedding vectors y∈ Y is the output of projection layers fθ (·). fθ (·) is the backbone network and we use multilayer perceptron (MLP) for all datasets.

# When To Use / Not Use
- Use when:
  - The lasso network allows us to avoid the dilemma of vanilla DR methods (such as t-SNE and UMAP) - constructing the neighborhood parameter σ for each data point, the σ is used to scale the pairwise distances to better compute the similarity, check Eq.(1) in [ 32] for detail.
  - In addition, users can experiment with EVNet and explainable analysis parameters for best results by adjusting the settings in the panel.
- Avoid when:
  - Some DR techniques are even used to analyze the network parameter distribution and diagnose the training state of neural networks [39].
  - It also avoids the damage to the local structure caused by the inappropriate PCA for ultra-high-dimensional data [2].
- Failure modes:
  - However, to the best of our knowledge, few works have been found to improve the DR methods with data augmentation.

# Metrics Mentioned
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- Finally, the complete loss of the model contains structurepreserving loss Lsp and L1 regularization loss Lr: L = Lsp + λLr, Lr =∥W∥1, (7) where regularization loss Lr is constraining the parameter W to be small, and λ is hyperparameter.
- The loss function of the parameter-free model is no longer suitable for the parametric approach, which inevitably causes a degradation of the optimization results.
- The gate operation 1w j>ε ensures that less important features (less than the hyperparameter threshold ε) do not leak to the following network layer.
- Next, based on the interactive interface, we intuitively understand the impact of EVNet’s hyperparameters on the analysis results.
- The combination parameter ru∼ U(0, pU ) is sampled from the uniform distribution U(0, pU ), and pU is the hyperparameter.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-168-C1 | stance: support | summary: Li∗, Fellow, IEEE Abstract—Dimension reduction (DR) is commonly utilized to capture intrinsic structure and transform high-dimensional data into low-dimensional space while retaining meaningful properties of original data. | evidence_ids: PENDING-REF-168-E1, PENDING-REF-168-E2
- CLAIM-PENDING-REF-168-C2 | stance: support | summary: 8 C ONCLUSION We propose EVNet, a deep learning-based parametric approach to achieve dimension reduction embedding and three different levels of explanation. | evidence_ids: PENDING-REF-168-E3, PENDING-REF-168-E4
- CLAIM-PENDING-REF-168-C3 | stance: support | summary: Finally, the complete loss of the model contains structurepreserving loss Lsp and L1 regularization loss Lr: L = Lsp + λLr, Lr =∥W∥1, (7) where regularization loss Lr is constraining the parameter W to be small, and λ is hyperparameter. | evidence_ids: PENDING-REF-168-E5, PENDING-REF-168-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 4 | relevance: high | note: contains initialization sensitivity or control-policy evidence

# Evidence
- PENDING-REF-168-E1 | page: 1, section: extracted, quote: "Li∗, Fellow, IEEE Abstract—Dimension reduction (DR) is commonly utilized to capture intrinsic structure and transform high-dimensional data into low-dimensional space while retaining meaningful properties of original data."
- PENDING-REF-168-E2 | page: 1, section: extracted, quote: "To address these problems, we have developed a deep neural network method called EVNet which provides not only excellent performance in structural maintainability but also explainability to the DR therein."
- PENDING-REF-168-E3 | page: 1, section: extracted, quote: "Abstract—Dimension reduction (DR) is commonly utilized to capture intrinsic structure and transform high-dimensional data into low-dimensional space while retaining meaningful properties of original data."
- PENDING-REF-168-E4 | page: 13, section: extracted, quote: "TNP data is a challenging problem for traditional DR methods because of the large number of noise features and irrelevant features in the data, which are closer to the real-world data."
- PENDING-REF-168-E5 | page: 16, section: extracted, quote: "8 C ONCLUSION We propose EVNet, a deep learning-based parametric approach to achieve dimension reduction embedding and three different levels of explanation."
- PENDING-REF-168-E6 | page: 5, section: extracted, quote: "Can EVNet have better local structure-preserving performance? (Q3) Is the output of EVNet’s DR embedding clear and easy to understand, and what are the differences between ours as compared with t-SNE, UMAP, and other DR methods? (Q4) Whether the time consumption of EVNet is unbearable? (Q5) Whether the data augmentation hyper-parameter of EVNet is stable?"
- PENDING-REF-168-E7 | page: 3, section: extracted, quote: "3.1 DR Embedding and Explainability Analysis Given a training dataset X, DR methods learn a continues function F(·) to map data X ={x1,··· , xM} (x∈ Rn, n is the number of the features, M is the number of the training data) to a latent This article has been accepted for publication in IEEE Transactions on Visualization and Computer Graphics."
- PENDING-REF-168-E8 | page: 4, section: extracted, quote: "In this paper, the explanation output of the DR method includes the following aspects I ={Ig, Il, It}: (a) Global explanation (Ig), discovers the essential features of the global embedding process and evaluates the importance of these features."
