---
id: paper-2002-zadu-ref-17
title: "Stochastic Neighbor Embedding"
authors: "Geoffrey E. Hinton; Sam T. Roweis"
venue: "Advances in Neural Information Processing Systems (NIPS 15)"
year: 2002
tags: [dr, zadu-table1-reference, kl_div]
source_pdf: papers/raw/zadu-table1-references/ref13_stochastic_neighbor_embedding.pdf
seed_note_id: "paper-2023-zadu-library"
evidence_level: high
updated_at: 2026-02-13
---

# Problem
- Traditional DR methods often preserve global distances but can fail to preserve neighborhood identity in a probabilistically coherent way.
- The paper proposes a neighbor-probability matching perspective where each point defines a distribution over candidate neighbors.
- It also addresses ambiguity cases where one object should map near multiple semantic regions.

# Method Summary
- Defines high-dimensional neighbor probabilities (`p_{j|i}`) using Gaussian kernels (or given dissimilarities).
- Defines low-dimensional neighbor probabilities (`q_{j|i}`) from embedding distances.
- Minimizes a sum of per-point KL divergences `sum_i KL(P_i || Q_i)`, yielding a push-pull gradient update.
- Introduces perplexity-based bandwidth selection and discusses practical optimization with annealed jitter.

# When To Use / Not Use
- Use when:
  - local neighborhood identity is primary,
  - probabilistic neighbor matching is preferred over direct distance matching,
  - ambiguity/multi-neighborhood representation matters.
- Avoid when:
  - purely linear, variance-maximizing embeddings are sufficient.
- Failure modes:
  - optimization can be slow and sensitive to local minima without robust search/annealing strategy.

# Metrics Mentioned
- `kl_div`: SNE objective is a sum of KL divergences between high- and low-dimensional neighborhood distributions.

# Implementation Notes
- Perplexity controls effective neighborhood size; the paper uses binary search to set local bandwidths.
- The gradient has an interpretable push-pull form that highlights under-selected vs over-selected neighbors.
- The paper notes computational burden and suggests sparsification/approximation ideas for scaling.

# Claim Atoms (For Conflict Resolution)
- CLAIM-ZR17-C1 | stance: support | summary: SNE formulates DR as probabilistic neighborhood matching with KL objective. | evidence_ids: ZR17-E1, ZR17-E2, ZR17-E3
- CLAIM-ZR17-C2 | stance: support | summary: The method emphasizes local neighborhood fidelity while still penalizing harmful collapses. | evidence_ids: ZR17-E4, ZR17-E5
- CLAIM-ZR17-C3 | stance: support | summary: Optimization strategy (perplexity, jitter, annealing) is practically important for usable embeddings. | evidence_ids: ZR17-E6, ZR17-E7, ZR17-E8

# Workflow Relevance Map
- step: 3 | relevance: medium | note: foundational technique for neighborhood-preserving DR tasks.
- step: 6 | relevance: high | note: perplexity and optimization schedule are central tunable parameters.
- step: 7 | relevance: medium | note: useful for explaining local-neighborhood-focused embedding behavior.

# Evidence
- ZR17-E1 | page: 1, section: abstract, quote: "A Gaussian is centered on each object ... to define a probability distribution over all the potential neighbors"
- ZR17-E2 | page: 2, section: section 2, quote: "The aim of the embedding is to match these two distributions"
- ZR17-E3 | page: 2, section: equation 4 text, quote: "cost function ... a sum of Kullback-Leibler divergences"
- ZR17-E4 | page: 2, section: discussion, quote: "there is a cost for modeling a big distance ... with a small distance"
- ZR17-E5 | page: 3, section: experiments, quote: "SNE ... quite cleanly separates the digit groups"
- ZR17-E6 | page: 2, section: bandwidth selection, quote: "binary search ... entropy ... perplexity"
- ZR17-E7 | page: 7, section: optimization, quote: "use steepest descent with added jitter that is slowly reduced"
- ZR17-E8 | page: 7, section: discussion, quote: "annealing the perplexities ... and only reducing the jitter after"
