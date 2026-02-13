---
id: paper-2009-zadu-ref-16
title: "Local procrustes for manifold embedding: a measure of embedding quality and embedding algorithms"
authors: "Yair Goldberg; Ya'acov Ritov"
venue: "Machine Learning"
year: 2009
tags: [dr, zadu-table1-reference, proc, tnc]
source_pdf: papers/raw/zadu-table1-references/ref12_local_procrustes_for_manifold_embedding_a_measure_of_embedding_quality_and_embedding_algor.pdf
seed_note_id: "paper-2023-zadu-library"
evidence_level: high
updated_at: 2026-02-13
---

# Problem
- Manifold-learning methods (for example LLE, Isomap) lacked a robust quantitative quality measure that compares local structure in input space and embedding space.
- Existing measures discussed by the paper (including trustworthiness-style criteria) were argued to be incomplete for neighborhood-structure comparison because they do not directly align full local neighborhoods in both spaces.
- The paper targets a neighborhood-structure-preserving quality function that can also be used for parameter selection and post-processing improvement.

# Method Summary
- The paper introduces the **Procrustes measure** for manifold embedding quality.
- For each point, it compares the original local neighborhood and the embedded local neighborhood after optimal alignment (rotation + translation; scaling extension for conformal settings).
- The total quality is an aggregate of local Procrustes residuals across neighborhoods.
- Beyond the metric, the paper proposes optimization procedures (including simulated-annealing-based neighborhood alignment) and iterative improvement of existing embeddings.
- Theoretical analysis is provided for convergence behavior under manifold assumptions.

# When To Use / Not Use
- Use when:
  - you need a quantitative neighborhood-structure fidelity score for manifold embeddings,
  - you are comparing embeddings that may be equivalent up to local rigid transforms,
  - you want a metric that can support parameter selection (for example neighborhood size, target dimension).
- Avoid when:
  - local neighborhoods are too sparse/noisy to estimate stable local tangent structure,
  - manifold assumptions (local smoothness, sufficient sampling density) are strongly violated.
- Failure modes:
  - unstable local PCA/tangent estimation can inflate Procrustes residuals and make method comparisons unreliable.

# Metrics Mentioned
- `proc`: local Procrustes neighborhood-alignment residual; the core metric introduced by this paper.
- `tnc`: trustworthiness/continuity-style neighborhood criteria discussed as related but less structural neighborhood-comparison approaches.

# Implementation Notes
- The metric requires consistent neighborhood construction and consistent local-PCA policy across all candidates.
- For conformal variants, local scaling must be handled consistently; otherwise results are not comparable.
- The paper’s optimization variants show that the same quality function can be used both for evaluation and for improving embeddings.
- Reproducibility depends on fixed neighborhood size, deterministic neighbor graph, and stable local alignment settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PAPER2009ZADUREF16-C1 | stance: support | summary: The paper introduces Procrustes-based local neighborhood alignment as a DR quality measure. | evidence_ids: PAPER2009ZADUREF16-E1, PAPER2009ZADUREF16-E2
- CLAIM-PAPER2009ZADUREF16-C2 | stance: support | summary: The measure supports parameter selection and can drive embedding optimization/improvement procedures. | evidence_ids: PAPER2009ZADUREF16-E3, PAPER2009ZADUREF16-E4
- CLAIM-PAPER2009ZADUREF16-C3 | stance: support | summary: Assumptions about local manifold structure and neighborhood estimation are central to validity. | evidence_ids: PAPER2009ZADUREF16-E5, PAPER2009ZADUREF16-E6

# Workflow Relevance Map
- step: 3 | relevance: medium | note: supports choosing quality checks for local manifold-structure goals.
- step: 4 | relevance: high | note: offers a structure-aware scoring signal complementary to rank-only local metrics.
- step: 6 | relevance: medium | note: useful as an optimization objective or acceptance check in parameter tuning.
- step: 7 | relevance: medium | note: improves explanation of why local neighborhood geometry is or is not preserved.

# Evidence
- PAPER2009ZADUREF16-E1 | page: 1, section: abstract, quote: "We present the Procrustes measure, a novel measure based on Procrustes rotation that enables quantitative comparison of the output of manifold-based embedding algorithms such as LLE ... and Isomap ..."
- PAPER2009ZADUREF16-E2 | page: 2, section: introduction, quote: "The function we present, based on the Procrustes analysis, compares each neighborhood in the high-dimensional space and its corresponding low-dimensional embedding."
- PAPER2009ZADUREF16-E3 | page: 1, section: abstract, quote: "The measure also serves as a natural tool when choosing dimension-reduction parameters."
- PAPER2009ZADUREF16-E4 | page: 1, section: abstract, quote: "We also present two novel dimension-reduction techniques that attempt to minimize the suggested measure ..."
- PAPER2009ZADUREF16-E5 | page: 3, section: assumptions, quote: "we assume that M is isometrically embedded ... This assumption is needed because we are interested in an embedding that everywhere preserves the local structure of distances and angles between neighboring points."
- PAPER2009ZADUREF16-E6 | page: 3, section: assumptions, quote: "The second assumption is that the sample taken from the manifold M is dense."
- PAPER2009ZADUREF16-E7 | page: 2, section: related measures, quote: "Other embedding quality measures were previously suggested. Venna and Kaski (2006) define two quality measures ..."
- PAPER2009ZADUREF16-E8 | page: 2, section: motivation, quote: "to date there exists no good tool to estimate the quality of the result of these algorithms."
