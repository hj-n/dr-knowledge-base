---
id: paper-2015-pending-ref-158
title: "LoCH: A neighborhood-based multidimensional projection technique for highdimensional sparse spaces"
authors: "S. Fadel, F. Fatore, F. Duarte, and F. Paulovich"
venue: "IEEE Transactions on Visualization and Computer Graphics"
year: 2015
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-158-2015-loch-a-neighborhood-based-multidimensional-projection-technique-for-highdimensional-s.pdf
seed_note_id: "paper-2019-mdp-visual-analytics-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- As distortions can make visual cluster analysis performed with DR unreliable [27, 29], it is important to evaluate how well the original cluster structure is preserved in the DR embeddings [29, 32, 44, 70], prior to the analysis.
- 2.1.2 Distortions in Dimensionality Reduction While transferring the data from broad high-dimensional space to narrow low-dimensional space, DR unavoidably introduces distortions [2, 50].
- We then generate the variants of the original data by mixing the points in the high-dimensional space with a fixed probability, producing Missing Groups distortions.
- This implies that Missing Groups distortions generally occur more for coarse-grained structures than for fine-grained ones; DR techniques exaggerate the separation between clusters at a global level. t-SNE and UMAP especially give the worst Label-C scores because they focus on the preservation of local neighborhoods, casting doubts on their reliability in identifying global clusters.

# Method Summary
- 6.1 Examining the Effect of t-SNE Perplexity 6.1.1 Objectives and Design We want to use Label-T&C to evaluate the reliability of the cluster structures from t-SNE embeddings (Sect.
- 5.1.1 Objectives and Design Experiment A: Randomizing embeddings We examine whether Label-T&C and competitors can accurately quantify False Groups distortions.
- 4.3 Guidelines to Interpret Label-T&C We present the guidelines to interpret embeddings based on Label-T&C.
- In this work, we propose Label-T&C as novel measures utilizing class labels to evaluate DR embeddings.
- However, the approach is prone to producing errors while examining the quality of DR embedding.
- We generate embeddings using t-SNE, UMAP, PCA, and random projection for all 94 datasets.
- Classes are not Clusters : Improving Label-based Evaluation of Dimensionality Reduction Hyeon Jeon, Yun-Hsin Kuo, Micha¨el Aupetit, Kwan-Liu Ma, and Jinwook Seo Abstract— A common way to evaluate the reliability of dimensionality reduction (DR) embeddings is to quantify how well labeled classes form compact, mutually separated clusters in the embeddings.

# When To Use / Not Use
- Use when:
  - However, S&C require users to specify the way of extracting and investigating clusters in both spaces, e.g., using clustering techniques, making the results of the cluster-level distortion measures sensitive to the clustering technique and hyperparameters used.
  - We use CVMs to find the optimal clustering technique or hyperparameter setting that produces the partition of the data that best matches its cluster structure.
- Avoid when:
  - This implies that Missing Groups distortions generally occur more for coarse-grained structures than for fine-grained ones; DR techniques exaggerate the separation between clusters at a global level. t-SNE and UMAP especially give the worst Label-C scores because they focus on the preservation of local neighborhoods, casting doubts on their reliability in identifying global clusters.
  - A quantitative evaluation showed that Label-T&C outperform widely used DR evaluation measures (e.g., Trustworthiness and Continuity, Kullback-Leibler divergence) in terms of the accuracy in assessing how well DR embeddings preserve the cluster structure, and are also scalable.
- Failure modes:
  - As non-expert users typically assume that DR techniques generate reliable embeddings of the original data, they may incorrectly conclude that CLM is also good in the high-dimensional space, while it is not actually true [3, 28].

# Metrics Mentioned
- `trustworthiness`: referenced as part of projection-quality or reliability assessment.
- `continuity`: referenced as part of projection-quality or reliability assessment.
- `kl divergence`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- We additionally found that the between-dataset Calinski-Harabasz index (CHbtwn) [28], a variant of Calinski-Harabasz index [60], satisfies the four requirements: satisfaction of R1, R2, and R3 has been demonstrated earlier [28]; it also satisfies R4 as its unique hyperparameter is the number of Monte-Carlo simulations for normalizing the measure, which barely affects the output if the number is sufficiently high.
- However, S&C require users to specify the way of extracting and investigating clusters in both spaces, e.g., using clustering techniques, making the results of the cluster-level distortion measures sensitive to the clustering technique and hyperparameters used.
- 4.1 Design Rationale Inputs, output, and hyperparameters Label-T&C take (1) the highdimensional data X, (2) its DR embedding Z, and (3) class labels PL = {PL,1,PL,2, · · ·PL,k} as inputs.
- Moreover, we present case studies demonstrating that Label-T&C can be successfully used for revealing the intrinsic characteristics of DR techniques and their hyperparameters.
- Finally, we demonstrate two case studies showing that Label-T&C can be used to reveal how different DR techniques or hyperparameter settings affect embedding results.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-158-C1 | stance: support | summary: As distortions can make visual cluster analysis performed with DR unreliable [27, 29], it is important to evaluate how well the original cluster structure is preserved in the DR embeddings [29, 32, 44, 70], prior to the analysis. | evidence_ids: PENDING-REF-158-E1, PENDING-REF-158-E2
- CLAIM-PENDING-REF-158-C2 | stance: support | summary: 6.1 Examining the Effect of t-SNE Perplexity 6.1.1 Objectives and Design We want to use Label-T&C to evaluate the reliability of the cluster structures from t-SNE embeddings (Sect. | evidence_ids: PENDING-REF-158-E3, PENDING-REF-158-E4
- CLAIM-PENDING-REF-158-C3 | stance: support | summary: We additionally found that the between-dataset Calinski-Harabasz index (CHbtwn) [28], a variant of Calinski-Harabasz index [60], satisfies the four requirements: satisfaction of R1, R2, and R3 has been demonstrated earlier [28]; it also satisfies R4 as its unique hyperparameter is the number of Monte-Carlo simulations for normalizing the measure, which barely affects the output if the number is sufficiently high. | evidence_ids: PENDING-REF-158-E5, PENDING-REF-158-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance
- step: 6 | relevance: high | note: guides reliable interpretation of projected views

# Evidence
- PENDING-REF-158-E1 | page: 1, section: extracted, quote: "As distortions can make visual cluster analysis performed with DR unreliable [27, 29], it is important to evaluate how well the original cluster structure is preserved in the DR embeddings [29, 32, 44, 70], prior to the analysis."
- PENDING-REF-158-E2 | page: 2, section: extracted, quote: "2.1.2 Distortions in Dimensionality Reduction While transferring the data from broad high-dimensional space to narrow low-dimensional space, DR unavoidably introduces distortions [2, 50]."
- PENDING-REF-158-E3 | page: 6, section: extracted, quote: "We then generate the variants of the original data by mixing the points in the high-dimensional space with a fixed probability, producing Missing Groups distortions."
- PENDING-REF-158-E4 | page: 9, section: extracted, quote: "This implies that Missing Groups distortions generally occur more for coarse-grained structures than for fine-grained ones; DR techniques exaggerate the separation between clusters at a global level. t-SNE and UMAP especially give the worst Label-C scores because they focus on the preservation of local neighborhoods, casting doubts on their reliability in identifying global clusters."
- PENDING-REF-158-E5 | page: 8, section: extracted, quote: "6.1 Examining the Effect of t-SNE Perplexity 6.1.1 Objectives and Design We want to use Label-T&C to evaluate the reliability of the cluster structures from t-SNE embeddings (Sect."
- PENDING-REF-158-E6 | page: 5, section: extracted, quote: "5.1.1 Objectives and Design Experiment A: Randomizing embeddings We examine whether Label-T&C and competitors can accurately quantify False Groups distortions."
- PENDING-REF-158-E7 | page: 4, section: extracted, quote: "4.3 Guidelines to Interpret Label-T&C We present the guidelines to interpret embeddings based on Label-T&C."
- PENDING-REF-158-E8 | page: 2, section: extracted, quote: "In this work, we propose Label-T&C as novel measures utilizing class labels to evaluate DR embeddings."
