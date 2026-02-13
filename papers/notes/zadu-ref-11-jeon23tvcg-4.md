---
id: paper-2024-zadu-ref-11
title: "Classes are not Clusters: Improving Label-based Evaluation of Dimensionality Reduction"
authors: "Hyeon Jeon; Yun-Hsin Kuo; Michael Aupetit; Kwan-Liu Ma; Jinwook Seo"
venue: "IEEE Transactions on Visualization and Computer Graphics"
year: 2024
tags: [dr, zadu-table1-reference, l_tnc, ca_tnc, dsc, c_evm, ivm, tnc, kl_div, dtm, mrre, snc]
source_pdf: papers/raw/zadu-table1-references/jeon23tvcg (4).pdf
seed_note_id: "paper-2023-zadu-library"
evidence_level: high
updated_at: 2026-02-13
---

# Problem
- Standard label-based DR evaluation often assumes each class forms one compact cluster in the original space.
- The paper shows this assumption can fail: one class may split into multiple groups, or several classes can merge, making naive class-based scores unreliable.
- It targets this mismatch directly by defining class-aware reliability measures that compare class-structure consistency between original and embedded spaces.

# Method Summary
- The paper introduces Label-Trustworthiness and Label-Continuity (Label-T&C), built from class-level matching matrices in original and embedded spaces.
- Instead of scoring only class compactness in embedding space, it measures how class-cluster relations change from input to embedding.
- It formalizes requirements for underlying clustering-validation measures used inside Label-T&C (scale invariance, shift invariance, fixed range, and low hyperparameter sensitivity).
- It evaluates Label-T&C with `DSC` and `CHbtwn` back-ends and compares against non-label and label baselines across synthetic and real datasets.

# When To Use / Not Use
- Use when:
  - labels exist but class geometry may be complex or non-convex,
  - you need reliability estimates tied to class-structure preservation rather than pure separation,
  - you analyze DR hyperparameter effects on class-level distortions.
- Avoid when:
  - labels are unavailable or not meaningful for the analysis objective.
- Failure modes:
  - conventional class-only compactness scores can overrate embeddings that distort true class relations.

# Metrics Mentioned
- `l_tnc`: primary contribution (Label-Trustworthiness and Label-Continuity).
- `ca_tnc`: compared as prior class-aware T&C baseline.
- `dsc`: used as a valid back-end CVM for Label-T&C.
- `ivm`: internal-validation framing (Silhouette, Davies-Bouldin, CH variants) is analyzed for suitability.
- `c_evm`: external validation process is discussed but noted to be harder to satisfy required axioms.
- `tnc`, `mrre`, `snc`, `kl_div`, `dtm`: compared as non-label baselines in sensitivity experiments.

# Implementation Notes
- The authors provide a Python implementation (`github.com/hj-n/ltnc`) with configurable CVM back-ends.
- Choice of CVM back-end matters; the paper favors back-ends satisfying the formal axioms (e.g., DSC, CHbtwn).
- The method is used to profile DR hyperparameters (e.g., t-SNE perplexity) and technique behavior across cluster granularity.

# Claim Atoms (For Conflict Resolution)
- CLAIM-ZR11-C1 | stance: support | summary: Class labels are not always equivalent to compact clusters; naive label-based DR evaluation can be misleading. | evidence_ids: ZR11-E1, ZR11-E2
- CLAIM-ZR11-C2 | stance: support | summary: Label-T&C improves class-aware reliability assessment by comparing class-structure consistency across spaces. | evidence_ids: ZR11-E3, ZR11-E4, ZR11-E5
- CLAIM-ZR11-C3 | stance: support | summary: Label-T&C can outperform widely used local/global DR quality measures for class-structure reliability tasks. | evidence_ids: ZR11-E6, ZR11-E7, ZR11-E8

# Workflow Relevance Map
- step: 1 | relevance: medium | note: clarifies when class-structure reliability is the actual analysis target.
- step: 3 | relevance: high | note: strongly informs metric choice for labeled class-relation tasks.
- step: 6 | relevance: high | note: directly supports hyperparameter tuning with class-structure reliability objectives.

# Evidence
- ZR11-E1 | page: 1, section: abstract, quote: "a single class can be fragmented into multiple separated clusters, and multiple classes can be merged into a single cluster."
- ZR11-E2 | page: 1, section: abstract, quote: "We thus cannot always assure the credibility of the evaluation using class labels."
- ZR11-E3 | page: 1, section: abstract, quote: "we introduce two novel quality measures—Label-Trustworthiness and Label-Continuity"
- ZR11-E4 | page: 1, section: abstract, quote: "Label-T&C work by (1) estimating ... classes form clusters ... and (2) evaluating the difference between the two."
- ZR11-E5 | page: 4, section: requirements, quote: "Scale Invariance ... Shift Invariance" are required CVM properties.
- ZR11-E6 | page: 1, section: abstract, quote: "Label-T&C outperform widely used DR evaluation measures (e.g., Trustworthiness and Continuity, Kullback-Leibler divergence)"
- ZR11-E7 | page: 4, section: implementation, quote: "We deploy Label-T&C as a Python library ... source code is available at github.com/hj-n/ltnc"
- ZR11-E8 | page: 8, section: hyperparameter study, quote: "Overall reliability of t-SNE embeddings according to the sigma value quantified by Label-T&C"
