---
id: paper-2013-pending-ref-061
title: "viSNE enables visualization of high dimensional single-cell data and reveals phenotypic heterogeneity of leukemia"
authors: "E.-A. D. Amir et al"
venue: "Nature Biotechnology"
year: 2013
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-061-2013-visne-enables-visualization-of-high-dimensional-single-cell-data-and-reveals-phenotyp.pdf
seed_note_id: "paper-2025-critical-analysis-dr-four-domains"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- The algorithm begins by calculating the pairwise similarity matrix in high-dimensional space, P, and randomizing a starting position for each point in the low-dimensional space, Y0. t-SNE proceeds to iteratively update the position of points in low-dimensional space: in iteration i, the similarity matrix in low-dimensional space, Q, is calculated according to the points’ current positions (Yi-1).
- Additional supplementary methods t-Distributed Stochastic Neighbor Embedding. t-Distributed Stochastic Neighbor Embedding (t-SNE) is a Nonlinear Dimensionality Reduction (NLDR) algorithm that projects points from high-dimensional space to low-dimensional space [1]. t-SNE’s input is a list of points in high-dimensional space, X.
- The cyt visualization tool. cyt is an interactive visualization tool designed for the analysis of viSNE maps and the high-dimensional mass or flow cytometry data from which these maps were projected.
- For each point xi in high-dimensional space, t-SNE defines the similarity of xi to xj as defined below: (Equation 1) σi is xi’s variance.

# Method Summary
- Additional supplementary methods t-Distributed Stochastic Neighbor Embedding. t-Distributed Stochastic Neighbor Embedding (t-SNE) is a Nonlinear Dimensionality Reduction (NLDR) algorithm that projects points from high-dimensional space to low-dimensional space [1]. t-SNE’s input is a list of points in high-dimensional space, X.
- The algorithm begins by calculating the pairwise similarity matrix in high-dimensional space, P, and randomizing a starting position for each point in the low-dimensional space, Y0. t-SNE proceeds to iteratively update the position of points in low-dimensional space: in iteration i, the similarity matrix in low-dimensional space, Q, is calculated according to the points’ current positions (Yi-1).
- For each xi, t-SNE performs a binary search for the value of σi that produces a Pi with a fixed Perplexity (a parameter for the algorithm that is given by the user; an intuitive interpretation for the perplexity is a soft measure for the number of nearest neighbors to consider for each cell).
- This method quickly identifies key differences between populations.

# When To Use / Not Use
- Use when:
  - It plots viSNE maps as scatter and density plots, and information can be overlaid onto this map by coloring cells according to various parameters, such as marker expression, source of sample or subtype. cyt includes a gating feature that can be used with either biaxial plots (to generate a viSNE map on only a defined subset of the cells) or the viSNE map (to further study a population identified by viSNE).
  - For cancer samples, which lack distinct subtypes, cyt lets us quickly identify which populations are similar to each other between multiple maps of the same sample based on their marker combination. cyt presents the data in an intuitive visual manner that allows the user to corroborate the viSNE maps.
- Avoid when:
  - For each xi, t-SNE performs a binary search for the value of σi that produces a Pi with a fixed Perplexity (a parameter for the algorithm that is given by the user; an intuitive interpretation for the perplexity is a soft measure for the number of nearest neighbors to consider for each cell).
  - To do so, first use the channel panel to pick the two viSNE channels; then, click Plot: You can now color code cells by channel intensities by picking the channel under the Color panel at the bottom.
- Failure modes:
  - The eight channels used here are CD38, CD34, CD10, CD45, CD33, HLA-DR, surface IgM and a “dump” channel that combines CD235, CD62 and CD66b.

# Metrics Mentioned
- `kl divergence`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- It plots viSNE maps as scatter and density plots, and information can be overlaid onto this map by coloring cells according to various parameters, such as marker expression, source of sample or subtype. cyt includes a gating feature that can be used with either biaxial plots (to generate a viSNE map on only a defined subset of the cells) or the viSNE map (to further study a population identified by viSNE).
- The algorithm begins by calculating the pairwise similarity matrix in high-dimensional space, P, and randomizing a starting position for each point in the low-dimensional space, Y0. t-SNE proceeds to iteratively update the position of points in low-dimensional space: in iteration i, the similarity matrix in low-dimensional space, Q, is calculated according to the points’ current positions (Yi-1).
- For each xi, t-SNE performs a binary search for the value of σi that produces a Pi with a fixed Perplexity (a parameter for the algorithm that is given by the user; an intuitive interpretation for the perplexity is a soft measure for the number of nearest neighbors to consider for each cell).
- However, all of t-SNE’s calculations are local: for a given point yi in low-dimensional space, only the vectors pi and qi are needed to calculate the next iteration for yi. viSNE is a distributed implementation of t-SNE that relies on the locality of t-SNE’s calculations.
- For each iteration, each core locally updates Yi for points in its partition and broadcasts these values to the other cores, guaranteeing that all cores have the updated similarity matrix.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-061-C1 | stance: support | summary: The algorithm begins by calculating the pairwise similarity matrix in high-dimensional space, P, and randomizing a starting position for each point in the low-dimensional space, Y0. t-SNE proceeds to iteratively update the position of points in low-dimensional space: in iteration i, the similarity matrix in low-dimensional space, Q, is calculated according to the points’ current positions (Yi-1). | evidence_ids: PENDING-REF-061-E1, PENDING-REF-061-E2
- CLAIM-PENDING-REF-061-C2 | stance: support | summary: Additional supplementary methods t-Distributed Stochastic Neighbor Embedding. t-Distributed Stochastic Neighbor Embedding (t-SNE) is a Nonlinear Dimensionality Reduction (NLDR) algorithm that projects points from high-dimensional space to low-dimensional space [1]. t-SNE’s input is a list of points in high-dimensional space, X. | evidence_ids: PENDING-REF-061-E3, PENDING-REF-061-E4
- CLAIM-PENDING-REF-061-C3 | stance: support | summary: It plots viSNE maps as scatter and density plots, and information can be overlaid onto this map by coloring cells according to various parameters, such as marker expression, source of sample or subtype. cyt includes a gating feature that can be used with either biaxial plots (to generate a viSNE map on only a defined subset of the cells) or the viSNE map (to further study a population identified by viSNE). | evidence_ids: PENDING-REF-061-E5, PENDING-REF-061-E6

# Workflow Relevance Map
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance
- step: 6 | relevance: high | note: guides reliable interpretation of projected views

# Evidence
- PENDING-REF-061-E1 | page: 1, section: extracted, quote: "The algorithm begins by calculating the pairwise similarity matrix in high-dimensional space, P, and randomizing a starting position for each point in the low-dimensional space, Y0. t-SNE proceeds to iteratively update the position of points in low-dimensional space: in iteration i, the similarity matrix in low-dimensional space, Q, is calculated according to the points’ current positions (Yi-1)."
- PENDING-REF-061-E2 | page: 1, section: extracted, quote: "Additional supplementary methods t-Distributed Stochastic Neighbor Embedding. t-Distributed Stochastic Neighbor Embedding (t-SNE) is a Nonlinear Dimensionality Reduction (NLDR) algorithm that projects points from high-dimensional space to low-dimensional space [1]. t-SNE’s input is a list of points in high-dimensional space, X."
- PENDING-REF-061-E3 | page: 2, section: extracted, quote: "The cyt visualization tool. cyt is an interactive visualization tool designed for the analysis of viSNE maps and the high-dimensional mass or flow cytometry data from which these maps were projected."
- PENDING-REF-061-E4 | page: 1, section: extracted, quote: "For each point xi in high-dimensional space, t-SNE defines the similarity of xi to xj as defined below: (Equation 1) σi is xi’s variance."
- PENDING-REF-061-E5 | page: 1, section: extracted, quote: "For each xi, t-SNE performs a binary search for the value of σi that produces a Pi with a fixed Perplexity (a parameter for the algorithm that is given by the user; an intuitive interpretation for the perplexity is a soft measure for the number of nearest neighbors to consider for each cell)."
- PENDING-REF-061-E6 | page: 3, section: extracted, quote: "This method quickly identifies key differences between populations."
- PENDING-REF-061-E7 | page: 3, section: extracted, quote: "It plots viSNE maps as scatter and density plots, and information can be overlaid onto this map by coloring cells according to various parameters, such as marker expression, source of sample or subtype. cyt includes a gating feature that can be used with either biaxial plots (to generate a viSNE map on only a defined subset of the cells) or the viSNE map (to further study a population identified by viSNE)."
- PENDING-REF-061-E8 | page: 3, section: extracted, quote: "For cancer samples, which lack distinct subtypes, cyt lets us quickly identify which populations are similar to each other between multiple maps of the same sample based on their marker combination. cyt presents the data in an intuitive visual manner that allows the user to corroborate the viSNE maps."
