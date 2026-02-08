---
id: paper-2026-zadu-ref-11
title: "<i>Classes are Not Clusters</i>: Improving Label-Based Evaluation of Dimensionality Reduction"
authors: "Hyeon Jeon, Yun-Hsin Kuo, Michaël Aupetit, Kwan-Liu Ma, Jinwook Seo"
venue: "IEEE Transactions on Visualization and Computer Graphics"
year: 2024
tags: [dr, zadu-table1-reference, c_evm, ca_tnc, dsc, dtm, ivm, kl_div, l_tnc, mrre, snc, tnc]
source_pdf: papers/raw/zadu-table1-references/jeon23tvcg (4).pdf
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- — A common way to evaluate the reliability of dimensionality reduction (DR) embeddings is to quantify how well labeled classes form compact, mutually separated clusters in the embeddings.
- This approach is based on the assumption that the classes stay as clear clusters in the original high-dimensional space.

# Method Summary
- In this paper, we introduce two novel quality measures— Label-T rustworthinessand Label-Continuity (Label-T&C)—advancing the process of DR evaluation based on class labels.
- We introduce two measures— Label-Trustworthiness (Label-T) and Label-Continuity (Label-C)—which examine CLM in an alternative way to assess the reliability of cluster structures in DR embeddings.
- The results show that Label-T&C can better capture the distortions of cluster structures than the existing measures (e.g., Steadiness & Cohesiveness [29] and Trustworthiness & Conti- nuity [62]) and the general process of label-based DR evaluation (i.e., naive application of CVMs).

# When To Use / Not Use
- Use when:
  - Use when labeled classes are a core analysis objective.
  - Use label-separation-sensitive metrics only after confirming class separation in original space.
- Avoid when:
  - Avoid assuming class labels always form well-separated clusters in original space.
- Failure modes:
  - Overconfident conclusions when class labels are not well-separated in original space.

# Metrics Mentioned
- `c_evm`: external-label-aware clustering validation view (label-separation-sensitive)
- `ca_tnc`: class-aware trustworthiness/continuity behavior (label-separation-sensitive)
- `dsc`: class consistency/separation quality in embedding (label-separation-sensitive)
- `dtm`: distance-to-measure based global structure signal
- `ivm`: internal validation view of cluster structure (label-separation-sensitive)
- `kl_div`: distribution mismatch in neighbor probabilities
- `l_tnc`: label-conditioned trustworthiness/continuity behavior
- `mrre`: rank-error behavior across neighborhood sizes
- `snc`: inter-cluster reliability via steadiness/cohesiveness
- `tnc`: local neighborhood trustworthiness/continuity balance

# Implementation Notes
- Runtime/complexity signal: A quantitative evaluation showed that Label-T&C outperform widely used DR evaluation measures (e.g., Trustworthiness and Continuity, Kullback-Leibler divergence) in terms of the accuracy in assessing how well DR embeddings preserve the cluster structure, and are also scalable.
- If labels are weakly separated in original space, down-weight label-separation-sensitive metrics in final justification.

# Claim Atoms (For Conflict Resolution)
- CLAIM-SOURCE-11-CORE | stance: support | summary: This source analyzes label-based DR evaluation assumptions and proposes class-aware reliability alternatives. | evidence_ids: ZR11-E1
- CLAIM-METRIC-C_EVM-SOURCE-11 | stance: support | summary: This source uses or discusses `c_evm` for external-label-aware clustering validation view in dimensionality-reduction evaluation. | evidence_ids: ZR11-E2
- CLAIM-METRIC-CA_TNC-SOURCE-11 | stance: support | summary: This source uses or discusses `ca_tnc` for class-aware trustworthiness/continuity behavior in dimensionality-reduction evaluation. | evidence_ids: ZR11-E2
- CLAIM-METRIC-DSC-SOURCE-11 | stance: support | summary: This source uses or discusses `dsc` for class consistency/separation quality in embedding in dimensionality-reduction evaluation. | evidence_ids: ZR11-E2
- CLAIM-METRIC-DTM-SOURCE-11 | stance: support | summary: This source uses or discusses `dtm` for distance-to-measure based global structure signal in dimensionality-reduction evaluation. | evidence_ids: ZR11-E2
- CLAIM-METRIC-IVM-SOURCE-11 | stance: support | summary: This source uses or discusses `ivm` for internal validation view of cluster structure in dimensionality-reduction evaluation. | evidence_ids: ZR11-E2
- CLAIM-METRIC-KL_DIV-SOURCE-11 | stance: support | summary: This source uses or discusses `kl_div` for distribution mismatch in neighbor probabilities in dimensionality-reduction evaluation. | evidence_ids: ZR11-E2
- CLAIM-METRIC-L_TNC-SOURCE-11 | stance: support | summary: This source uses or discusses `l_tnc` for label-conditioned trustworthiness/continuity behavior in dimensionality-reduction evaluation. | evidence_ids: ZR11-E2
- CLAIM-METRIC-MRRE-SOURCE-11 | stance: support | summary: This source uses or discusses `mrre` for rank-error behavior across neighborhood sizes in dimensionality-reduction evaluation. | evidence_ids: ZR11-E2
- CLAIM-METRIC-SNC-SOURCE-11 | stance: support | summary: This source uses or discusses `snc` for inter-cluster reliability via steadiness/cohesiveness in dimensionality-reduction evaluation. | evidence_ids: ZR11-E2
- CLAIM-METRIC-TNC-SOURCE-11 | stance: support | summary: This source uses or discusses `tnc` for local neighborhood trustworthiness/continuity balance in dimensionality-reduction evaluation. | evidence_ids: ZR11-E2

# Workflow Relevance Map
- step: 3 | relevance: high | note: Informs task-aligned metric/technique selection and metric trust calibration.
- step: 4 | relevance: medium | note: Affects optimization objective design and score interpretation during hyperparameter search.
- step: 6 | relevance: high | note: Provides rationale that can be translated for end users.

# Evidence
- ZR11-E1 | page: 1, section: extracted, quote: "In this paper, we introduce two novel quality measures— Label-T rustworthinessand Label-Continuity (Label-T&C)—advancing the process of DR evaluation based on class labels."
- ZR11-E2 | page: 1, section: extracted, quote: "Instead of assuming that classes are well-clustered in the original space, Label-T&C work by (1) estimating the extent to which classes form clusters in the original and embedded spaces and (2) evaluating the difference between the two."
- ZR11-E3 | page: 1, section: extracted, quote: "A quantitative evaluation showed that Label-T&C outperform widely used DR evaluation measures (e.g., Trustworthiness and Continuity, Kullback-Leibler divergence) in terms of the accuracy in assessing how well DR embeddings preserve the cluster structure, and are also scalable."
- ZR11-E4 | page: 1, section: extracted, quote: "Moreover, we present case studies demonstrating that Label-T&C can be successfully used for revealing the intrinsic characteristics of DR techniques and their hyperparameters."
- ZR11-E5 | page: 1, section: extracted, quote: "We introduce two measures— Label-Trustworthiness (Label-T) and Label-Continuity (Label-C)—which examine CLM in an alternative way to assess the reliability of cluster structures in DR embeddings."
- ZR11-E6 | page: 1, section: extracted, quote: "In contrast to the general label-based evaluation process, Label-T&C use CVM to quantify CLM distortions as the difference between CLM estimated in both original and embedded spaces."
- ZR11-E7 | page: 1, section: extracted, quote: "Since CLM distortions reduce the reliability of cluster structures represented by the embeddings, Label-T&C scores can be interpreted as proxies for the credibility of DR-based cluster analysis."
- ZR11-E8 | page: 1, section: extracted, quote: "We conduct a series of quantitative experiments to validate the effec- tiveness of Label-T&C."
