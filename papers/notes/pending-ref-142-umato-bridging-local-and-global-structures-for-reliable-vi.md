---
id: paper-2025-pending-ref-142
title: "UMATO: Bridging Local and Global Structures for Reliable Visual Analytics With Dimensionality Reduction"
authors: "Hyeon Jeon, Kwon Ko, Soohyun Lee, Jake Hyun, Taehyun Yang, Gyehun Go, Jaemin Jo, and Jinwook Seo"
venue: "IEEE Transactions on Visualization and Computer Graphics"
year: 2025
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-142-2025-umato-bridging-local-and-global-structures-for-reliable-visual-analytics-with-dimensi.pdf
seed_note_id: "paper-2025-stop-misusing-tsne-umap"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- However, HD data analysis with DR can easily become unreliable as distortions occur when projecting data from a vast HD space to a narrow low-dimensional space [16], [29], [30].
- 2.2 Reliable High-dimensional Data Analysis with Dimensionality Reduction Visual analytics should be reliable, i.e., decision-making or knowledge generation based on visualization should accurately reflect the original data characteristics.
- In this research, we provide a deeper insight into Uniform Manifold Approximation with Two-phase Optimization (UMATO), a DR technique that addresses this problem by effectively capturing local and global structures.
- Abstract—Due to the intrinsic complexity of high-dimensional (HD) data, dimensionality reduction (DR) techniques cannot preserve all the structural characteristics of the original data.

# Method Summary
- As UMATO’s default initialization method (PCA) is substantially faster than the one used by UMAP (Spectral embedding), it may be unfair to compare these two algorithms directly with the default setting.
- Finally, we present a case study and a qualitative demonstration that highlight UMATO’s effectiveness in generating faithful projections, enhancing the overall reliability of visual analytics using DR.
- In this step, the algorithm aims to find a projection Y = {y1,y2, · · ·,yN} that minimizes the loss between HD edge weights and low-dimensional similarities.
- Moreover, PCA is substantially faster than UMAP’s initialization method (Spectral embedding), thus enhancing the overall scalability of UMATO (Section 4.2).
- The evaluation process is as follows: For a given dataset and a DR technique, we generate five projections with diverse initialization methods.
- One way to alleviate this problem is to link multiple DR projections, for example, through small multiples or interactive methods [16], [17].
- Therefore, robustly producing stable projections regardless of the initialization methods is essential for a reliable DR technique.

# When To Use / Not Use
- Use when:
  - For example, DR benchmark studies [34], [35] use these metrics to identify the best matching projection for a given data or visual analytics task.
  - These metrics can also be used to optimize hyperparameters to achieve the best projection possible with a given DR technique [36], [35].
- Avoid when:
  - 8.2 Limitations and Future Works We discuss the limitations of this research and possible future works.
  - To ensure the experiment ends in a reasonable time, we use UMATO and alternative DR techniques that ranked in the top five scalabilities in the previous experiment with small datasets (UMAP with PCA initialization, LLE, PCA, PacMAP, Trimap; refer to Section 4.2.1).
- Failure modes:
  - Here, designing a new DR technique that can explicitly and clearly control the tradeoff between local and global accuracy will be an interesting avenue to explore, as such a technique will allow users “tune” their DR projections to align with their task.

# Metrics Mentioned
- `trustworthiness`: referenced as part of projection-quality or reliability assessment.
- `continuity`: referenced as part of projection-quality or reliability assessment.
- `stress`: referenced as part of projection-quality or reliability assessment.
- `procrustes-based quality`: referenced as part of projection-quality or reliability assessment.
- `kl divergence`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- We check the runtime required to compute each stage of UMATO (Section 3):kNN graph construction, point classification, initialization, global optimization, local optimization, and DCP arrangement.
- Another side effect caused by our optimization design is the addition of hub_num, a hyperparameter that substantially affects final projections.
- We also focus on hub_num, a hyperparameter representing the number of hubs considered in global layout optimization (Section 3.3).
- To guarantee fair comparison across DR techniques, we optimize the hyperparameters of the techniques using Bayesian optimization.
- Furthermore, identifying the optimal number of iterations in local optimization will substantially reduce the runtime.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-142-C1 | stance: support | summary: However, HD data analysis with DR can easily become unreliable as distortions occur when projecting data from a vast HD space to a narrow low-dimensional space [16], [29], [30]. | evidence_ids: PENDING-REF-142-E1, PENDING-REF-142-E2
- CLAIM-PENDING-REF-142-C2 | stance: support | summary: As UMATO’s default initialization method (PCA) is substantially faster than the one used by UMAP (Spectral embedding), it may be unfair to compare these two algorithms directly with the default setting. | evidence_ids: PENDING-REF-142-E3, PENDING-REF-142-E4
- CLAIM-PENDING-REF-142-C3 | stance: support | summary: We check the runtime required to compute each stage of UMATO (Section 3):kNN graph construction, point classification, initialization, global optimization, local optimization, and DCP arrangement. | evidence_ids: PENDING-REF-142-E5, PENDING-REF-142-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 4 | relevance: high | note: contains initialization sensitivity or control-policy evidence

# Evidence
- PENDING-REF-142-E1 | page: 3, section: extracted, quote: "However, HD data analysis with DR can easily become unreliable as distortions occur when projecting data from a vast HD space to a narrow low-dimensional space [16], [29], [30]."
- PENDING-REF-142-E2 | page: 3, section: extracted, quote: "2.2 Reliable High-dimensional Data Analysis with Dimensionality Reduction Visual analytics should be reliable, i.e., decision-making or knowledge generation based on visualization should accurately reflect the original data characteristics."
- PENDING-REF-142-E3 | page: 1, section: extracted, quote: "In this research, we provide a deeper insight into Uniform Manifold Approximation with Two-phase Optimization (UMATO), a DR technique that addresses this problem by effectively capturing local and global structures."
- PENDING-REF-142-E4 | page: 1, section: extracted, quote: "Abstract—Due to the intrinsic complexity of high-dimensional (HD) data, dimensionality reduction (DR) techniques cannot preserve all the structural characteristics of the original data."
- PENDING-REF-142-E5 | page: 8, section: extracted, quote: "As UMATO’s default initialization method (PCA) is substantially faster than the one used by UMAP (Spectral embedding), it may be unfair to compare these two algorithms directly with the default setting."
- PENDING-REF-142-E6 | page: 1, section: extracted, quote: "Finally, we present a case study and a qualitative demonstration that highlight UMATO’s effectiveness in generating faithful projections, enhancing the overall reliability of visual analytics using DR."
- PENDING-REF-142-E7 | page: 2, section: extracted, quote: "In this step, the algorithm aims to find a projection Y = {y1,y2, · · ·,yN} that minimizes the loss between HD edge weights and low-dimensional similarities."
- PENDING-REF-142-E8 | page: 5, section: extracted, quote: "Moreover, PCA is substantially faster than UMAP’s initialization method (Spectral embedding), thus enhancing the overall scalability of UMATO (Section 4.2)."
