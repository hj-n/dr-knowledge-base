---
id: paper-2020-zadu-ref-14
title: "Steering Distortions to Preserve Classes and Neighbors in Supervised Dimensionality Reduction"
authors: "Benoit Colange; Jaakko Peltonen; Michael Aupetit; Denys Dutykh; Sylvain Lespinats"
venue: "Advances in Neural Information Processing Systems (NeurIPS)"
year: 2020
tags: [dr, zadu-table1-reference, ca_tnc, tnc, kl_div]
source_pdf: papers/raw/zadu-table1-references/ref06_steering_distortions_to_preserve_classes_and_neighbors_in_supervised_dimensionality_reduct.pdf
seed_note_id: "paper-2023-zadu-library"
evidence_level: high
updated_at: 2026-02-13
---

# Problem
- Supervised DR methods often over-separate classes while harming neighborhood structure; unsupervised methods do the opposite.
- The paper addresses this conflict by explicitly steering which distortions are penalized under class labels.
- It targets a practical exploratory setting where both class information and neighborhood faithfulness matter.

# Method Summary
- Proposes ClassNeRV, extending NeRV/SNE probabilistic neighborhood embedding.
- Splits distortions into within-class and between-class terms and introduces separate trade-off parameters for them (`tau_in`, `tau_out`).
- Uses Bregman-divergence terms to keep a valid positive objective on class-split memberships.
- Defines class-aware quality indicators: between-class Trustworthiness (`T_notin`) and within-class Continuity (`C_in`) to evaluate class-neighbor preservation behavior.

# When To Use / Not Use
- Use when:
  - labels exist and the goal is to preserve both neighborhood structure and meaningful class relations,
  - you need controllable supervision intensity rather than fixed supervised behavior.
- Avoid when:
  - labels are random/unreliable, which can inject supervision bias.
- Failure modes:
  - very strong supervision can force class separation patterns that misrepresent true spatial adjacency.

# Metrics Mentioned
- `ca_tnc`: class-restricted trustworthiness/continuity indicators are explicitly defined.
- `tnc`: standard trustworthiness/continuity are used as class-independent comparators.
- `kl_div`: NeRV-style KL terms are the foundational objective basis before class-aware decomposition.

# Implementation Notes
- The paper reparameterizes supervision with two interpretable controls (`tau_star`, `epsilon`) to separate false-vs-missed tradeoff from class-supervision strength.
- Multi-scale optimization and perplexity settings are reported for reproducibility (e.g., `p=32` for Globe, `p=30` for Isolet).
- Evaluation should report both class-independent and class-aware indicators to detect over-separation artifacts.

# Claim Atoms (For Conflict Resolution)
- CLAIM-ZR14-C1 | stance: support | summary: ClassNeRV is designed to preserve both class information and neighborhood structure. | evidence_ids: ZR14-E1, ZR14-E2
- CLAIM-ZR14-C2 | stance: support | summary: Explicit within-class vs between-class distortion controls enable tunable supervision. | evidence_ids: ZR14-E3, ZR14-E4, ZR14-E5
- CLAIM-ZR14-C3 | stance: support | summary: ClassNeRV outperforms several supervised alternatives in joint structure/class preservation experiments. | evidence_ids: ZR14-E6, ZR14-E7, ZR14-E8

# Workflow Relevance Map
- step: 3 | relevance: high | note: directly supports choosing class-aware metrics/techniques when labels are valid.
- step: 6 | relevance: high | note: introduces explicit tunable parameters for supervised distortion tradeoffs.
- step: 7 | relevance: medium | note: recommends reporting both neighbor and class preservation to explain tradeoffs to users.

# Evidence
- ZR14-E1 | page: 1, section: abstract, quote: "ClassNeRV ... evaluates embedding quality both in terms of false neighbors and missed neighbors"
- ZR14-E2 | page: 2, section: figure 1 caption, quote: "ClassNeRV is designed to preserve both classes and neighbors"
- ZR14-E3 | page: 4, section: method, quote: "split the divergence terms ... into within-class and between-class relations"
- ZR14-E4 | page: 4, section: equation 3 text, quote: "ClassNeRV is supervised ifτ∈ > τ/∈"
- ZR14-E5 | page: 5, section: equation 5 text, quote: "Trustworthiness restricted to between-class relations" and "Continuity restricted to within-class relations"
- ZR14-E6 | page: 7, section: results discussion, quote: "ClassNeRV ... obtains both better structure and class preservation"
- ZR14-E7 | page: 6, section: experiment setup, quote: "The final perplexity ... p = 32 for Globe and p = 30 for Isolet"
- ZR14-E8 | page: 7, section: comparison, quote: "S-UMAP ... tendency to over-separate classes"
