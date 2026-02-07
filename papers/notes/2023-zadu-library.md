---
id: paper-2023-zadu-library
title: "ZADU: A Python Library for Evaluating the Reliability of Dimensionality Reduction Embeddings"
year: 2023
tags: [dr, evaluation, zadu, metrics]
source_pdf: papers/raw/ZADU_A_Python_Library_for_Evaluating_the_Reliability_of_Dimensionality_Reduction_Embeddings.pdf
evidence_level: high
updated_at: 2026-02-07
---

# Problem
- DR embeddings inevitably distort high-dimensional structure.
- Practitioners need reliable, easy-to-run distortion measures for evaluation before analysis decisions.

# Method Summary
- ZADU provides a unified Python interface for DR distortion measures.
- The paper organizes measures by structural granularity: local, cluster-level, and global.
- The original paper set contains 17 measures with balanced coverage across granularities.

# When To Use / Not Use
- Use when you need reliability checks of embeddings before downstream interpretation.
- Use multiple measures together, not a single metric, for more robust assessment.
- Avoid over-interpreting one metric as universal evidence across all analysis goals.

# Metrics Mentioned
- Local examples include T&C, MRRE, LCMC, Neighborhood Hit, Neighbor Dissimilarity, Class-Aware T&C, and Procrustes.
- Cluster-level examples include Steadiness & Cohesiveness, Distance Consistency, IVM, and C+EVM.
- Global examples include Stress, KL Divergence, DTM, Topographic Product, Pearson r, and Spearman rho.

# Implementation Notes
- The paper supports evaluating multiple measures with shared preprocessing for runtime efficiency.
- Local pointwise distortions are available for some local and cluster-level measures.
- For current production usage, combine paper-grounded grouping with current `hj-n/zadu` metric IDs.

# Claim Atoms (For Conflict Resolution)
- CLAIM-ZADU-GRANULARITY-GROUPING | stance: support | summary: ZADU measures are structured by local, cluster-level, and global granularity | evidence_ids: ZADU23-E1, ZADU23-E2
- CLAIM-ZADU-LOCAL-LIST | stance: support | summary: core local list includes tnc, mrre, lcmc, nh, nd, ca_tnc, proc | evidence_ids: ZADU23-E3
- CLAIM-ZADU-CLUSTER-LIST | stance: support | summary: core cluster-level list includes snc, dsc, ivm, c_evm | evidence_ids: ZADU23-E4
- CLAIM-ZADU-GLOBAL-LIST | stance: support | summary: core global list includes stress, kl_div, dtm, topo, pr, srho | evidence_ids: ZADU23-E5

# Evidence
- ZADU23-E1 | page: 1, section: Abstract and Introduction, quote: "Distortion measures can be broadly divided into three categories-local measures, global measures, and cluster-level measures"
- ZADU23-E2 | page: 2, section: Table 1 and Section 3.1, quote: "we select seven local measures, four cluster-level measures, and six global measures"
- ZADU23-E3 | page: 2, section: Table 1, quote: "Trustworthiness & Continuity ... Mean Relative Rank Errors ... Local Continuity Meta-Criteria ... Neighborhood Hit ... Neighbor Dissimilarity ... Class-Aware Trustworthiness & Continuity ... Procrustes Measure"
- ZADU23-E4 | page: 2, section: Table 1, quote: "Steadiness & Cohesiveness ... Distance Consistency ... Internal Clustering Validation Measures ... Clustering + External Clustering Validation Measures"
- ZADU23-E5 | page: 2, section: Table 1, quote: "Stress ... Kullback-Leibler Divergence ... Distance-to-Measure ... Topographic Product ... Pearson's correlation coefficient r ... Spearman's rank correlation coefficient rho"
