---
id: paper-2021-zadu-ref-19
title: "A Comparison for Dimensionality Reduction Methods of Single-Cell RNA-seq Data"
authors: "UNKNOWN"
venue: "UNKNOWN"
year: 2021
tags: [dr, zadu-table1-reference, c_evm, ivm]
source_pdf: papers/raw/zadu-table1-references/ref42_a_comparison_for_dimensionality_reduction_methods_of_single_cell_rna_seq_data.pdf
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- fgene-12-646936 March 17, 2021 Time: 12:29 # 1 ORIGINAL RESEARCH published: 23 March 2021 doi: 10.3389/fgene.2021.646936 Edited by: Chunjie Jiang, University of Pennsylvania, United States Reviewed by: Quan Zou, University of Electronic Science and Technology of China, China Kuixi Zhu, University of Arizona, United States *Correspondence: Xiaowen Chen hrbmucxw@163.com Chaohan Xu chaohanxu@hrbmu.edu.cn Specialty section: This article was submitted to Computational Genomics, a section of the journal Frontiers in Genetics Received: 28 December 2020 Accepted: 19 February 2021 Published: 23 March 2021 Citation: Xiang R, Wang W, Yang L, Wang S, Xu C and Chen X (2021) A Comparison for Dimensionality Reduction Methods of Single-Cell RNA-seq Data.
- doi: 10.3389/fgene.2021.646936 A Comparison for Dimensionality Reduction Methods of Single-Cell RNA-seq Data Ruizhi Xiang 1, W

# Method Summary
- Compared with the above two linear methods, employing the zero-inﬂation model can give ZIFA more powerful projection capabilities but will pay a corresponding cost in computational complexity.
- The deep leaning framework enables DCA to capture the complexity and non-linearity in scRNA-seq data.
- The variable probability Q(z|X) is used to approximate the posterior distribution P(z|X), and it is optimized to minimize the Kullback–Leibler divergence between Q(z|X) and P(z|X) and reconstruction loss.
- It is worth noting that SIMLR has a high computational complexity as it involves large matrix operations which could not perform dimensionality reduction on data with a cell count greater than or equal to 10,000.

# When To Use / Not Use
- Use when:
  - Use when selecting DR reliability checks in workflow Step 3.
  - Use with complementary local/cluster/global metrics rather than a single score.
- Avoid when:
  - Avoid using this source as the only decision signal without task constraints.
- Failure modes:
  - Overconfident conclusions when class labels are not well-separated in original space.

# Metrics Mentioned
- `c_evm`: external-label-aware clustering validation view (label-separation-sensitive)
- `ivm`: internal validation view of cluster structure (label-separation-sensitive)

# Implementation Notes
- Runtime/complexity signal: Compared with the above two linear methods, employing the zero-inﬂation model can give ZIFA more powerful projection capabilities but will pay a corresponding cost in computational complexity.
- If labels are weakly separated in original space, down-weight label-separation-sensitive metrics in final justification.

# Claim Atoms (For Conflict Resolution)
- CLAIM-SOURCE-19-CORE | stance: support | summary: This source contributes DR method/quality evidence relevant to metric selection. | evidence_ids: ZR19-E1
- CLAIM-METRIC-C_EVM-SOURCE-19 | stance: support | summary: This source uses or discusses `c_evm` for external-label-aware clustering validation view in dimensionality-reduction evaluation. | evidence_ids: ZR19-E2
- CLAIM-METRIC-IVM-SOURCE-19 | stance: support | summary: This source uses or discusses `ivm` for internal validation view of cluster structure in dimensionality-reduction evaluation. | evidence_ids: ZR19-E2

# Workflow Relevance Map
- step: 3 | relevance: high | note: Informs task-aligned metric/technique selection and metric trust calibration.
- step: 6 | relevance: high | note: Provides rationale that can be translated for end users.

# Evidence
- ZR19-E1 | page: 2, section: extracted, quote: "Compared with the above two linear methods, employing the zero-inﬂation model can give ZIFA more powerful projection capabilities but will pay a corresponding cost in computational complexity."
- ZR19-E2 | page: 4, section: extracted, quote: "The deep leaning framework enables DCA to capture the complexity and non-linearity in scRNA-seq data."
- ZR19-E3 | page: 4, section: extracted, quote: "The variable probability Q(z|X) is used to approximate the posterior distribution P(z|X), and it is optimized to minimize the Kullback–Leibler divergence between Q(z|X) and P(z|X) and reconstruction loss."
- ZR19-E4 | page: 6, section: extracted, quote: "It is worth noting that SIMLR has a high computational complexity as it involves large matrix operations which could not perform dimensionality reduction on data with a cell count greater than or equal to 10,000."
- ZR19-E5 | page: 10, section: extracted, quote: "FIGURE 7 | Evaluation computing cost for each method on metrics of (A) running time and (B) memory limitation."
