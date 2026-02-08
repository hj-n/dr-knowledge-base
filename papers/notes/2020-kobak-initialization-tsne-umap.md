---
id: paper-2020-kobak-initialization-tsne-umap
title: "Initialization Is Critical for Preserving Global Data Structure in Both t-SNE and UMAP"
authors: "Dmitry Kobak; George C. Linderman"
venue: "Nature Biotechnology"
year: 2020
tags: [dr, tsne, umap, initialization, global_structure]
source_pdf: papers/raw/s41587-020-00809-z (5).pdf
seed_note_id: ""
evidence_level: high
updated_at: 2026-02-08
---

# Problem
- Claims that UMAP is intrinsically better than t-SNE for global structure can be confounded by unequal initialization settings.
- Comparative DR conclusions can be invalid when algorithm defaults differ in ways that materially affect outcomes.
- The paper addresses fairness and reliability in method comparison by isolating initialization effects.

# Method Summary
- The authors re-analyze published comparisons while controlling for initialization differences between t-SNE and UMAP implementations.
- They compare random initialization versus informative initialization (PCA for t-SNE, Laplacian-eigenmap-style initialization for UMAP).
- Toy and large-scale data evidence show that initialization largely explains perceived global-structure differences.
- They recommend informative initialization as default for both methods and discuss implications for reproducibility claims.

# When To Use / Not Use
- Use when comparing t-SNE and UMAP for global-structure tasks or reproducibility arguments.
- Use when setting default initialization policy in production DR workflows.
- Avoid reporting algorithm superiority from comparisons that do not control initialization.
- Failure mode: attributing embedding quality differences to algorithm design when they are initialization artifacts.

# Metrics Mentioned
- Pearson correlation of pairwise distances is used as a global-structure quantification signal in the discussed benchmark context.
- Reproducibility is evaluated by correlations over subsampled embeddings in the compared setup.
- The paper reinforces protocol control (same parameters except initialization) as critical for metric interpretation.

# Implementation Notes
- Always log initialization strategy as part of DR hyperparameter configuration.
- For fair method comparison, hold all other settings fixed when testing t-SNE vs UMAP.
- Adopt informative initialization defaults when global structure matters.
- Communicate that global-structure conclusions are protocol-dependent and require controlled comparisons.

# Claim Atoms (For Conflict Resolution)
- CLAIM-KOBAK20-C1 | stance: support | summary: Apparent UMAP-vs-t-SNE global-structure differences can be driven by initialization choices. | evidence_ids: KOB20-E1, KOB20-E2
- CLAIM-KOBAK20-C2 | stance: support | summary: Random initialization degrades global structure for both methods in tested settings. | evidence_ids: KOB20-E3, KOB20-E4
- CLAIM-KOBAK20-C3 | stance: support | summary: Informative initialization should be the default for reliable comparison and use. | evidence_ids: KOB20-E5, KOB20-E6

# Workflow Relevance Map
- step: 3 | relevance: medium | note: prevents unfair algorithm-choice conclusions.
- step: 4 | relevance: high | note: initialization is a key hyperparameter affecting optimization outcome.
- step: 6 | relevance: high | note: supports transparent explanation of comparison fairness and residual uncertainty.

# Evidence
- KOB20-E1 | page: 1, section: Introduction, quote: "alleged superiority of UMAP ... attributed to different choices of initialization"
- KOB20-E2 | page: 1, section: Introduction, quote: "UMAP with random initialization preserves global structure as poorly as t-SNE"
- KOB20-E3 | page: 1, section: Introduction, quote: "currently no evidence that the UMAP algorithm per se has any advantage"
- KOB20-E4 | page: 1, section: Toy Example, quote: "only with informative initialization can UMAP and t-SNE produce a faithful representation"
- KOB20-E5 | page: 1-2, section: Conclusion, quote: "should always use informative initialization by default"
- KOB20-E6 | page: 1, section: Method, quote: "Apart from the initialization, both algorithms were run with the same parameters"
