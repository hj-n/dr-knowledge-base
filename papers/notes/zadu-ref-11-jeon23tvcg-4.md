---
id: paper-2026-zadu-ref-11
title: "Classes are Not Clusters: Improving Label-Based Evaluation of Dimensionality Reduction"
authors: "Hyeon Jeon, Yun-Hsin Kuo, Michaël Aupetit, Kwan-Liu Ma, Jinwook Seo"
venue: "IEEE Transactions on Visualization and Computer Graphics"
year: 2024
tags: [dr, zadu-table1-reference, c_evm, ca_tnc, dsc, dtm, ivm, kl_div, l_tnc, mrre, snc, tnc]
source_pdf: papers/raw/zadu-table1-references/jeon23tvcg (4).pdf
evidence_level: high
updated_at: 2026-02-08
---

# Problem
- The paper identifies a systematic bias in label-based DR evaluation: many workflows only score class separation in the embedding and implicitly assume classes are already well-separated in the original high-dimensional space.
- Under that assumption, embeddings that artificially separate overlapping classes can look "better" than embeddings that faithfully preserve overlap.
- It names two distortion families behind this failure: `False Groups` and `Missing Groups`, and argues that reliable evaluation must compare class-label matching in both original and embedded spaces.

# Method Summary
- The paper introduces Label-Trustworthiness and Label-Continuity (Label-T&C) as class-label reliability measures for DR embeddings.
- Step 1: compute class-pairwise class-label-matching matrices `M(X)` and `M(Z)` using a clustering-validation measure (CVM) for every pair of classes.
- Step 2: compute distortion matrix `M* = M(X) - M(Z)`, then split into `MFG` (positive part; False Groups) and `MMG` (negative part magnitude; Missing Groups).
- Step 3: aggregate upper-triangle values into final scores:
  - Label-Trustworthiness = `1 - avg(MFG)`
  - Label-Continuity = `1 - avg(MMG)`
- The paper formalizes CVM requirements for this framework: scale invariance (R1), shift invariance (R2), range invariance (R3), and hyperparameter robustness (R4).
- It reports DSC and CHbtwn as suitable CVMs under those requirements and discusses why common alternatives can violate them.

# When To Use / Not Use
- Use when:
  - class relationships are central to the analysis task and labels are available,
  - you need to know whether apparent class separation in 2D is faithful to the original data,
  - you need separate diagnostics for false-group vs missing-group distortions.
- Avoid when:
  - labels are unreliable or semantically inconsistent,
  - the task is fully label-agnostic and class-conditioned reliability is not required.
- Failure modes:
  - using CVMs that violate R1-R4 can destabilize the metric across datasets,
  - optimizing only class separation can overstate reliability by hiding class-overlap fidelity.

# Metrics Mentioned
- `l_tnc`: label-conditioned trustworthiness/continuity through class-pair distortion between original and embedded spaces.
- `dsc`: candidate CVM used inside Label-T&C after normalization for range compatibility.
- `ivm`: internal validation measures are analyzed as building blocks and compared for suitability.
- `c_evm`: external validation measures are analyzed, with clustering-hyperparameter dependence highlighted.
- `ca_tnc`: class-aware trustworthiness/continuity family conceptually related to class-conditioned reliability.
- `tnc`: trustworthiness/continuity directionality is the conceptual baseline used for naming and interpretation.

# Implementation Notes
- Required inputs are explicit: high-dimensional data `X`, embedding `Z`, class labels `PL`, and a CVM choice (plus clustering choice when using EVMs).
- The paper reports linear-time behavior in major variables for Label-T&C with DSC/CHbtwn (`O(|S||PL|ΔS)`), supporting repeated use during evaluation and tuning.
- Interpretation requires reading Label-Trustworthiness and Label-Continuity jointly; one score alone can hide the distortion tradeoff.
- Preserve preprocessing, distance definition, and label policy across runs to keep scores comparable.

# Claim Atoms (For Conflict Resolution)
- CLAIM-SOURCE-11-C1 | stance: support | summary: Naive label-based DR evaluation can prefer embeddings that maximize class separation even when this departs from original-space class structure. | evidence_ids: ZR11-E1, ZR11-E4, ZR11-E5
- CLAIM-SOURCE-11-C2 | stance: support | summary: Label-T&C computes class-pair distortions via `M(X)`, `M(Z)`, `M*`, `MFG`, and `MMG`, then aggregates into Label-Trustworthiness and Label-Continuity. | evidence_ids: ZR11-E6, ZR11-E7, ZR11-E8
- CLAIM-METRIC-L_TNC-SOURCE-11 | stance: support | summary: Valid CVMs for Label-T&C must satisfy scale/shift/range invariance and hyperparameter robustness; DSC and CHbtwn are reported as suitable. | evidence_ids: ZR11-E9, ZR11-E10, ZR11-E11
- CLAIM-METRIC-C_EVM-SOURCE-11 | stance: support | summary: This source includes evidence relevant to `c_evm` in dimensionality-reduction reliability evaluation. | evidence_ids: ZR11-E1, ZR11-E2
- CLAIM-METRIC-CA_TNC-SOURCE-11 | stance: support | summary: This source includes evidence relevant to `ca_tnc` in dimensionality-reduction reliability evaluation. | evidence_ids: ZR11-E1, ZR11-E2
- CLAIM-METRIC-DSC-SOURCE-11 | stance: support | summary: This source includes evidence relevant to `dsc` in dimensionality-reduction reliability evaluation. | evidence_ids: ZR11-E1, ZR11-E2
- CLAIM-METRIC-DTM-SOURCE-11 | stance: support | summary: This source includes evidence relevant to `dtm` in dimensionality-reduction reliability evaluation. | evidence_ids: ZR11-E1, ZR11-E2
- CLAIM-METRIC-IVM-SOURCE-11 | stance: support | summary: This source includes evidence relevant to `ivm` in dimensionality-reduction reliability evaluation. | evidence_ids: ZR11-E1, ZR11-E2
- CLAIM-METRIC-KL_DIV-SOURCE-11 | stance: support | summary: This source includes evidence relevant to `kl_div` in dimensionality-reduction reliability evaluation. | evidence_ids: ZR11-E1, ZR11-E2
- CLAIM-METRIC-MRRE-SOURCE-11 | stance: support | summary: This source includes evidence relevant to `mrre` in dimensionality-reduction reliability evaluation. | evidence_ids: ZR11-E1, ZR11-E2
- CLAIM-METRIC-SNC-SOURCE-11 | stance: support | summary: This source includes evidence relevant to `snc` in dimensionality-reduction reliability evaluation. | evidence_ids: ZR11-E1, ZR11-E2
- CLAIM-METRIC-TNC-SOURCE-11 | stance: support | summary: This source includes evidence relevant to `tnc` in dimensionality-reduction reliability evaluation. | evidence_ids: ZR11-E1, ZR11-E2

# Workflow Relevance Map
- step: 3 | relevance: high | note: constrains when class-aware metrics are valid and how to structure class-conditioned evaluation.
- step: 4 | relevance: high | note: provides distortion-aware scoring logic beyond raw class-separation values.
- step: 6 | relevance: medium | note: informs optimization objectives by separating false-group and missing-group penalties.
- step: 7 | relevance: high | note: supports user-facing explanation of why class-oriented recommendations are reliable or uncertain.

# Evidence
- ZR11-E1 | page: 1, section: abstract, quote: "A common way to evaluate the reliability of dimensionality reduction (DR) embeddings is to quantify how well labeled classes form compact, mutually separated clusters in the embeddings."
- ZR11-E2 | page: 1, section: abstract, quote: "This approach is based on the assumption that the classes stay as clear clusters in the original high-dimensional space."
- ZR11-E3 | page: 1, section: abstract, quote: "Label-T&C work by (1) estimating the extent to which classes form clusters in the original and embedded spaces and (2) evaluating the difference between the two."
- ZR11-E4 | page: 3, section: pitfalls, quote: "The general process of label-based DR evaluation promotes embeddings with good CLM regardless of the CLM of the original data."
- ZR11-E5 | page: 3, section: pitfalls, quote: "The general process of label-based evaluation erroneously prefers DR techniques that maximize the separation among classes, instead of the ones that aim to preserve the original structure of data if the datasets have bad CLM."
- ZR11-E6 | page: 3, section: method-step-1, quote: "we construct the class-pairwise CLM matrices M(X) and M(Z)"
- ZR11-E7 | page: 3, section: method-step-2, quote: "We construct a matrix M* = M(X) − M(Z) representing CLM distortions."
- ZR11-E8 | page: 3, section: method-step-3, quote: "LABEL-TRUSTWORTHINESS: 1 − avg_{i>j} MFG_{i,j}; LABEL-CONTINUITY: 1 − avg_{i>j} MMG_{i,j}."
- ZR11-E9 | page: 4, section: cvm-requirements, quote: "(R1) A CVM should satisfy scale invariance."
- ZR11-E10 | page: 4, section: cvm-requirements, quote: "(R2) A CVM should satisfy shift invariance."
- ZR11-E11 | page: 4, section: cvm-candidates, quote: "we found that DSC satisfies all requirements, setting it as a proper CVM for Label-T&C ... We additionally found that ... CHbtwn ... satisfies the four requirements"
- ZR11-E12 | page: 4, section: complexity, quote: "In both cases, the time complexity is linear in all variables."
