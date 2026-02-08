---
id: paper-2021-pending-ref-039
title: "Assessing singlecell transcriptomic variability through density-preserving data visualization"
authors: "Ashwin Narayan, Bonnie Berger, and Hyunghoon Cho"
venue: "Molecular Systems Biology"
year: 2021
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-039-2021-assessing-singlecell-transcriptomic-variability-through-density-preserving-data-visua.pdf
seed_note_id: "paper-2025-jeon-reliable-va-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- Given the difficulty of assessing successful expression recovery in a practical application, this scenario represents a challenge to the user pondering whether or not to denoise their data.
- While data integration methods can also be applied to simple batch correction problems, we recommend to be wary of over-correction given the increased degrees of freedom of non-linear data integration approaches.
- Considering the above-mentioned challenges, instead of targeting a standardized analysis pipeline, we outline current best practices and common tools independent of programming language.
- The challenges to standardization include the growing number of analysis methods (385 tools as of 7 March 2019) and exploding dataset sizes (Angerer et al , 2017; Zappia et al , 2018).

# Method Summary
- The most common dimensionality reduction method for scRNA-seq visualization is the t-distributed stochastic neighbour embedding (t-SNE; van der Maaten & Hinton, 2008). t-SNE dimensions focus on capturing local similarity at the expense of global structure.
- While data integration methods can also be applied to simple batch correction problems, we recommend to be wary of over-correction given the increased degrees of freedom of non-linear data integration approaches.
- While non-linear normalization methods, or alternative approaches such as downsampling, appear better suited to these conditions, comparative studies are needed to confirm this hypothesis.
- Common alternatives to t-SNE are the Uniform Approximation and Projection method (UMAP; preprint: McInnes & Healy, 2018) or graph-based tools such as SPRING (Weinreb et al , 2018).
- Given the trend of increasing cell numbers in single-cell experiments, algorithm runtime is becoming an increasingly important consideration in method choice.
- Cell-level analysis approaches are again subdivided into cluster and trajectory analysis b ranches, which include also gene-level analysis methods.
- Two approaches exist to generate cell clusters from these similarity scores: clustering alg orithms and community detection methods.

# When To Use / Not Use
- Use when:
  - Irrespective of computational methods, the best method of batch correction is pre-empting the effect and avoiding it altogether by clever experimental design (Hicks et al , 2017).
  - As uncorrected, measured data should be used for DE testing, accounting for confounding factors is crucial to robust estimation of differentially expressed genes.
- Avoid when:
  - Regression frameworks differ in their noise model assumptions and the class of function used to describe the expression as a function of pseudotime.
  - For the above reasons, it is best to use the term “cell identities” rather than “cell types”.
- Failure modes:
  - Ligand –receptor pair labels can be ª 2019 The Authors Molecular Systems Biology 15:e 8746 | 2019 17 of 23 Malte D Luecken & Fabian J Theis Molecular Systems Biology obtained from the recent CellPhoneDB (Vento-Tormo et al , 2018) and used to interpret the highly expressed genes across clusters using statistical models (Zepp et al , 2017; Zhou et al , 2017; Cohen et al , 2018; Vento-Tormo et al , 2018).

# Metrics Mentioned
- `stress`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- For example, Mayer et al (2018) fit a negative binomial model to count data, using technical covariates such as the read depth and the number of counts per gene to fit the model parameters.
- A further difficulty is the choice of its perplexity parameter, as t-SNE graphs may show strongly different numbers of clusters depending on its value (Wattenberg et al , 2016).
- Given the trend of increasing cell numbers in single-cell experiments, algorithm runtime is becoming an increasingly important consideration in method choice.
- In addition to an underestimation of the noise, this optimization of the experimental design signal can lead to an overestimation of the effect size.
- The optimized modularity function includes a resolution parameter, which allows the user to determine the scale of the cluster partition.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-039-C1 | stance: support | summary: Given the difficulty of assessing successful expression recovery in a practical application, this scenario represents a challenge to the user pondering whether or not to denoise their data. | evidence_ids: PENDING-REF-039-E1, PENDING-REF-039-E2
- CLAIM-PENDING-REF-039-C2 | stance: support | summary: The most common dimensionality reduction method for scRNA-seq visualization is the t-distributed stochastic neighbour embedding (t-SNE; van der Maaten & Hinton, 2008). t-SNE dimensions focus on capturing local similarity at the expense of global structure. | evidence_ids: PENDING-REF-039-E3, PENDING-REF-039-E4
- CLAIM-PENDING-REF-039-C3 | stance: support | summary: For example, Mayer et al (2018) fit a negative binomial model to count data, using technical covariates such as the read depth and the number of counts per gene to fit the model parameters. | evidence_ids: PENDING-REF-039-E5, PENDING-REF-039-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-REF-039-E1 | page: 8, section: extracted, quote: "Given the difficulty of assessing successful expression recovery in a practical application, this scenario represents a challenge to the user pondering whether or not to denoise their data."
- PENDING-REF-039-E2 | page: 7, section: extracted, quote: "While data integration methods can also be applied to simple batch correction problems, we recommend to be wary of over-correction given the increased degrees of freedom of non-linear data integration approaches."
- PENDING-REF-039-E3 | page: 1, section: extracted, quote: "Considering the above-mentioned challenges, instead of targeting a standardized analysis pipeline, we outline current best practices and common tools independent of programming language."
- PENDING-REF-039-E4 | page: 1, section: extracted, quote: "The challenges to standardization include the growing number of analysis methods (385 tools as of 7 March 2019) and exploding dataset sizes (Angerer et al , 2017; Zappia et al , 2018)."
- PENDING-REF-039-E5 | page: 9, section: extracted, quote: "The most common dimensionality reduction method for scRNA-seq visualization is the t-distributed stochastic neighbour embedding (t-SNE; van der Maaten & Hinton, 2008). t-SNE dimensions focus on capturing local similarity at the expense of global structure."
- PENDING-REF-039-E6 | page: 5, section: extracted, quote: "While non-linear normalization methods, or alternative approaches such as downsampling, appear better suited to these conditions, comparative studies are needed to confirm this hypothesis."
- PENDING-REF-039-E7 | page: 9, section: extracted, quote: "Common alternatives to t-SNE are the Uniform Approximation and Projection method (UMAP; preprint: McInnes & Healy, 2018) or graph-based tools such as SPRING (Weinreb et al , 2018)."
- PENDING-REF-039-E8 | page: 17, section: extracted, quote: "Given the trend of increasing cell numbers in single-cell experiments, algorithm runtime is becoming an increasingly important consideration in method choice."
