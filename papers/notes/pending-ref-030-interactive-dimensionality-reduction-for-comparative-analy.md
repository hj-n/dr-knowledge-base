---
id: paper-2022-pending-ref-030
title: "Interactive Dimensionality Reduction for Comparative Analysis"
authors: "Takanori Fujiwara, Xinhai Wei, Jian Zhao, and Kwan-Liu Ma"
venue: "IEEE Transactions on Visualization and Computer Graphics"
year: 2022
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-030-2022-interactive-dimensionality-reduction-for-comparative-analysis.pdf
seed_note_id: "paper-2024-large-scale-text-spatialization"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- With weights wtg and wbg, of which j-th elements wtg j and wbg j (0 ≤ wtg j ,wbg j ≤ 1) represent contributions of group j’s covariance to target and background variances, the optimization problem of gcPCA can be written as: max M⊤M=Id′ tr ( M⊤ ( c ∑ j=1 wtg j Cwi j − α c ∑ j=1 wbg j Cwi j ) M ) . (4) Using wtg and wbg, gcPCA allows any groups to be target or background.
- As discussed by Fujiwara et al. [28], when we want to maximize the variance of the target matrix while simultaneously minimizing the variance of the background matrix, the optimization problem of cPCA can be converted into the maximization of tr(M⊤CtgM)/tr(M⊤CbgM), which is the trace-ratio problem (i.e., maximizing the ratio of matrix traces).
- To address the aforementioned problems, we introduce a novel visual analytics framework for comparative analysis, which consists of a new DR method, called ULCA (uniﬁed linear comparative analysis) , an interactive parameter optimization algorithm, and a visual interface.
- 2.1 Dimensionality Reduction Methods DR is an essential tool to analyze high-dimensional data [67, 81] as it can provide a succinct low-dimensional overview while preserving the essential information of the original data (e.g., data variance when using PCA [43, 54]).

# Method Summary
- Additionally, these DR methods do not provide the functionality that allows analysts to perform hypothetical changes on an embedding result (e.g., changing data points’ positions) and then link these changes to the parameters of the DR algorithms in order to produce a new result that resembles the hypothetical changes [22].
- A few methods such as InterAxis [59] and AxiSketcher [62] take an approach that generates embedding axes by directly indicating how data points should be arranged along the axes.
- These methods produce a sparse projection matrix by penalizing a case where an embedding uses many attributes.
- Similar to the discussion on cPCA by Abid et al. [2], while ULCA uses group labels for embedding, ULCA is different from other supervised learning methods that focus on a task of classiﬁcation/regression and multi-group statistical hypothesis tests whose primary goal is identifying an attribute that has a signiﬁcantly different statistic value (e.g., mean) in each group.
- Self et al. [83] deﬁned that parametric interaction is to directly adjust parameters of a DR method while observationlevel interaction is to manipulate data points in an embedding result (e.g., changing their positions) and interpret the semantic meaning of manipulation in order to update the embedding result accordingly.
- To address the aforementioned problems, we introduce a novel visual analytics framework for comparative analysis, which consists of a new DR method, called ULCA (uniﬁed linear comparative analysis) , an interactive parameter optimization algorithm, and a visual interface.
- Linear DR, such as PCA and classical multidimensional scaling (MDS) [86], can be deﬁned as DR that produces a linear transformation matrix (or projection matrix) M ∈ Rd×d′ where d and d′ are the numbers of dimensions in original and embedding spaces [17].

# When To Use / Not Use
- Use when:
  - More speciﬁcally, using the Riemannian Trust Regions (RTR) method [3] over the Grassmann manifold can be used as a solver to achieve the best performance due to the evaluation by Cunningham and Ghahramani [17].
  - To mitigate this problem, we take an approach similar to one developed to use linear DR in a streaming setting [25] (note that several works addressed mental map preservation for nonlinear DR [13, 80]).
- Avoid when:
  - Similar to other machine learning algorithms (e.g., linear regression), γ0 and γ1 can be used to add the bias into C0 and C1 to avoid overﬁtting.
  - Unlike the above works, our work focuses on the usage of parametric and observation-level interactions for comparative analysis.
- Failure modes:
  - We use γ0 and γ1 to avoid the case where either matrix trace of C0 or C1 is always zero.

# Metrics Mentioned
- `procrustes-based quality`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- This optimization can be written as: max M⊤M=Id′ tr ( M⊤(Ctg − αCbg)M ) (2) where Ctg, Cbg ∈ Rd×d are covariance matrices of target and background groups Xtg ∈ Rntg×d, Xbg ∈ Rnbg×d, respectively (ntg, nbg: the number of data points in each group). α (0 ≤ α ≤ ∞) is a hyperparameter, called a contrast parameter, which controls the trade-off between having a high target variance and a low background variance.
- For example, to complete the optimization in similar runtime with the EVD-based approach, we can use d as the maximum number of iterations.
- To address the aforementioned problems, we introduce a novel visual analytics framework for comparative analysis, which consists of a new DR method, called ULCA (uniﬁed linear comparative analysis) , an interactive parameter optimization algorithm, and a visual interface.
- Additionally, to help analysts intuitively adjust the related parameters, we develop a backward optimization algorithm that updates the embedding result by ﬁnding optimal parameters to achieve the analyst’s demonstrated changes in the embedding result.
- We use only the manifold-optimization-based approach and a ﬁxed number of data points (i.e., n = 1,000) but various values for the maximum number of iterations for COBYLA (here, we represent it with m), number of groups c, and number of attributes d.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-030-C1 | stance: support | summary: With weights wtg and wbg, of which j-th elements wtg j and wbg j (0 ≤ wtg j ,wbg j ≤ 1) represent contributions of group j’s covariance to target and background variances, the optimization problem of gcPCA can be written as: max M⊤M=Id′ tr ( M⊤ ( c ∑ j=1 wtg j Cwi j − α c ∑ j=1 wbg j Cwi j ) M ) . (4) Using wtg and wbg, gcPCA allows any groups to be target or background. | evidence_ids: PENDING-REF-030-E1, PENDING-REF-030-E2
- CLAIM-PENDING-REF-030-C2 | stance: support | summary: Additionally, these DR methods do not provide the functionality that allows analysts to perform hypothetical changes on an embedding result (e.g., changing data points’ positions) and then link these changes to the parameters of the DR algorithms in order to produce a new result that resembles the hypothetical changes [22]. | evidence_ids: PENDING-REF-030-E3, PENDING-REF-030-E4
- CLAIM-PENDING-REF-030-C3 | stance: support | summary: This optimization can be written as: max M⊤M=Id′ tr ( M⊤(Ctg − αCbg)M ) (2) where Ctg, Cbg ∈ Rd×d are covariance matrices of target and background groups Xtg ∈ Rntg×d, Xbg ∈ Rnbg×d, respectively (ntg, nbg: the number of data points in each group). α (0 ≤ α ≤ ∞) is a hyperparameter, called a contrast parameter, which controls the trade-off between having a high target variance and a low background variance. | evidence_ids: PENDING-REF-030-E5, PENDING-REF-030-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-REF-030-E1 | page: 4, section: extracted, quote: "With weights wtg and wbg, of which j-th elements wtg j and wbg j (0 ≤ wtg j ,wbg j ≤ 1) represent contributions of group j’s covariance to target and background variances, the optimization problem of gcPCA can be written as: max M⊤M=Id′ tr ( M⊤ ( c ∑ j=1 wtg j Cwi j − α c ∑ j=1 wbg j Cwi j ) M ) . (4) Using wtg and wbg, gcPCA allows any groups to be target or background."
- PENDING-REF-030-E2 | page: 4, section: extracted, quote: "As discussed by Fujiwara et al. [28], when we want to maximize the variance of the target matrix while simultaneously minimizing the variance of the background matrix, the optimization problem of cPCA can be converted into the maximization of tr(M⊤CtgM)/tr(M⊤CbgM), which is the trace-ratio problem (i.e., maximizing the ratio of matrix traces)."
- PENDING-REF-030-E3 | page: 1, section: extracted, quote: "To address the aforementioned problems, we introduce a novel visual analytics framework for comparative analysis, which consists of a new DR method, called ULCA (uniﬁed linear comparative analysis) , an interactive parameter optimization algorithm, and a visual interface."
- PENDING-REF-030-E4 | page: 2, section: extracted, quote: "2.1 Dimensionality Reduction Methods DR is an essential tool to analyze high-dimensional data [67, 81] as it can provide a succinct low-dimensional overview while preserving the essential information of the original data (e.g., data variance when using PCA [43, 54])."
- PENDING-REF-030-E5 | page: 1, section: extracted, quote: "Additionally, these DR methods do not provide the functionality that allows analysts to perform hypothetical changes on an embedding result (e.g., changing data points’ positions) and then link these changes to the parameters of the DR algorithms in order to produce a new result that resembles the hypothetical changes [22]."
- PENDING-REF-030-E6 | page: 2, section: extracted, quote: "A few methods such as InterAxis [59] and AxiSketcher [62] take an approach that generates embedding axes by directly indicating how data points should be arranged along the axes."
- PENDING-REF-030-E7 | page: 9, section: extracted, quote: "These methods produce a sparse projection matrix by penalizing a case where an embedding uses many attributes."
- PENDING-REF-030-E8 | page: 9, section: extracted, quote: "Similar to the discussion on cPCA by Abid et al. [2], while ULCA uses group labels for embedding, ULCA is different from other supervised learning methods that focus on a task of classiﬁcation/regression and multi-group statistical hypothesis tests whose primary goal is identifying an attribute that has a signiﬁcantly different statistic value (e.g., mean) in each group."
