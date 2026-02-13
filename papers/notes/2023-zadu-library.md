---
id: paper-2023-zadu-library
title: "ZADU: A Python Library for Evaluating the Reliability of Dimensionality Reduction Embeddings"
authors: "Hyeon Jeon, Aeri Cho, Jinhwa Jang, Soohyun Lee, Jake Hyun, Hyung-Kwon Ko, Jaemin Jo, Jinwook Seo"
venue: "2023 IEEE Visualization and Visual Analytics (VIS)"
year: 2023
tags: [dr, evaluation, zadu, metrics]
source_pdf: papers/raw/ZADU_A_Python_Library_for_Evaluating_the_Reliability_of_Dimensionality_Reduction_Embeddings.pdf
seed_note_id: ""
evidence_level: high
updated_at: 2026-02-13
---

# Problem
- DR embeddings inevitably distort high-dimensional structure, so reliability checks are a prerequisite for trustworthy interpretation.
- Before this work, applying multiple DR distortion measures in practice required scattered implementations, manual environment setup, and repeated preprocessing work.
- The paper targets a practical gap: researchers had measure definitions in papers, but no unified, low-friction, scalable library for routine reliability evaluation.

# Method Summary
- ZADU provides a single Python library for DR reliability evaluation with broad measure coverage and practical execution support.
- The measure set is deliberately balanced across structural granularity levels: seven local, four cluster-level, and six global measures.
- The main interface is specification-driven (`id` + `params`), so one evaluation specification can be reused across multiple embeddings of the same high-dimensional dataset.
- ZADU introduces execution optimization for multi-metric runs by reusing shared preprocessing blocks (pairwise distances, rank computation, and k-nearest-neighbor structures) instead of recomputing them per metric.
- It also supports local pointwise distortions for selected local/cluster measures, enabling region-level diagnosis and downstream distortion visualization workflows.

# When To Use / Not Use
- Use when you need a reproducible, multi-metric reliability evaluation pipeline for DR embeddings before visual or analytic conclusions.
- Use when comparing multiple candidate embeddings of the same source dataset and you want consistent evaluation settings with lower compute overhead.
- Use when local distortion localization is needed (for example distortion maps or pointwise reliability diagnostics).
- Do not treat one metric as universally sufficient; the paper positions reliability as multi-measure by design.
- Do not assume pointwise local distortions are available for every metric; availability is measure-dependent.
- Failure mode: evaluating many methods with mixed ad-hoc metric code paths can produce inconsistent conclusions that reflect tooling differences rather than embedding quality.

# Metrics Mentioned
- Local measures: Trustworthiness & Continuity, Mean Relative Rank Errors, Local Continuity Meta-Criteria, Neighborhood Hit, Neighbor Dissimilarity, Class-Aware Trustworthiness & Continuity, and Procrustes.
- Cluster-level measures: Steadiness & Cohesiveness, Distance Consistency, internal clustering validation measures, and clustering-plus-external validation measures.
- Global measures: Stress, Kullback-Leibler Divergence, Distance-to-Measure, Topographic Product, Pearson correlation, and Spearman rank correlation.
- The paper-level guidance is to use a diverse set across granularity levels, since different metrics capture different distortion behaviors.

# Implementation Notes
- Preferred interface: initialize `ZADU(spec, hd)` once, then call `.measure(ld)` for each candidate embedding under the same high-dimensional reference.
- Alternative direct per-measure function calls are supported but intentionally not optimized for multi-metric workloads.
- Optimization mechanism:
  - identify required preprocessing units from the specification,
  - compute shared units once,
  - reuse intermediate artifacts across metrics and across related k-neighborhood requests.
- Reported runtime outcome in the paper’s simulation: optimized execution is about 1.5x faster on average, with stronger benefit as dataset size grows.
- Local pointwise distortion output is controlled by a return flag and is returned only for measures that expose local contributions.
- For this KB, keep the paper’s local/cluster/global grouping semantics as the primary evaluation design signal and map to current `zadu` IDs at implementation time.

# Claim Atoms (For Conflict Resolution)
- CLAIM-ZADU-PRACTICAL-GAP | stance: support | summary: The paper addresses the practical burden of implementing/executing distortion measures and proposes a unified Python library. | evidence_ids: ZADU23-E1, ZADU23-E2, ZADU23-E3
- CLAIM-ZADU-GRANULARITY-GROUPING | stance: support | summary: ZADU explicitly balances reliability checks across local, cluster-level, and global structural granularity. | evidence_ids: ZADU23-E4, ZADU23-E5
- CLAIM-ZADU-EXECUTION-OPT | stance: support | summary: ZADU accelerates multi-metric evaluation by reusing shared preprocessing blocks and dependencies. | evidence_ids: ZADU23-E6, ZADU23-E7, ZADU23-E8
- CLAIM-ZADU-POINTWISE | stance: support | summary: ZADU supports pointwise local distortions for selected measures to enable fine-grained distortion analysis and visualization. | evidence_ids: ZADU23-E9, ZADU23-E10
- CLAIM-ZADU-RUNTIME-GAIN | stance: support | summary: The paper reports measurable runtime reduction from optimization, including scaling benefits with larger datasets. | evidence_ids: ZADU23-E11

# Workflow Relevance Map
- step: 3 | relevance: high | note: Defines how to compose reliability checks across local/cluster/global structure rather than relying on a single score.
- step: 4 | relevance: high | note: Supports deterministic cross-candidate scoring with one reusable evaluation specification.
- step: 6 | relevance: high | note: Enables efficient repeated objective evaluation during Bayesian optimization by reusing preprocessing.
- step: 7 | relevance: high | note: Supports user explanation with pointwise distortion evidence and explicit multi-metric tradeoffs.

# Evidence
- ZADU23-E1 | page: 1, section: abstract, quote: "Dimensionality reduction (DR) techniques inherently distort the original structure of input high-dimensional data, producing imperfect low-dimensional embeddings."
- ZADU23-E2 | page: 1, section: abstract, quote: "implementing and executing distortion measures in practice has so far been time-consuming and tedious."
- ZADU23-E3 | page: 1, section: abstract, quote: "we present ZADU, a Python library that provides distortion measures."
- ZADU23-E4 | page: 2, section: section 3.1, quote: "we select seven local measures, four cluster-level measures, and six global measures (Table 1)."
- ZADU23-E5 | page: 2, section: section 3.1, quote: "The simultaneous use of multiple measures having different granularity is essential for comprehensively evaluating DR embeddings [9, 19, 30]."
- ZADU23-E6 | page: 3, section: section 3.3.1, quote: "The primary goal of the optimization is to minimize the computational overhead associated with three key preprocessing blocks: pairwise distance computation, pointwise distance ranking computation, and kNN identification."
- ZADU23-E7 | page: 3, section: section 3.3.1, quote: "Given a specification (refer to Section 3.2), ZADU extracts a list of requisite preprocessing units."
- ZADU23-E8 | page: 3, section: section 3.3.1, quote: "The effectiveness of our optimization increases as more distortion measures are executed simultaneously."
- ZADU23-E9 | page: 3, section: section 3.3.2, quote: "ZADU enables users to obtain local pointwise distortions, which indicate how each point contributes to the overall distortions."
- ZADU23-E10 | page: 3, section: section 3.3.2, quote: "The computation of pointwise local distortions is available only for some local measures and cluster-level measures."
- ZADU23-E11 | page: 4, section: section 4.1.1, quote: "ZADU is 1.5 times faster with optimization than without it on average"
