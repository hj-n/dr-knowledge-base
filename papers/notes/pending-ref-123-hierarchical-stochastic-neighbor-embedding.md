---
id: paper-2016-pending-ref-123
title: "Hierarchical stochastic neighbor embedding"
authors: "N. Pezzotti, T. H €ollt, B. Lelieveldt, E. Eisemann, and A. Vilanova"
venue: "Journal of Proteome Research"
year: 2016
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-123-2016-hierarchical-stochastic-neighbor-embedding.pdf
seed_note_id: "paper-2019-mdp-visual-analytics-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- 37 The hallmark of these algorithms is their ability to preserve local structures of high-dimensional data in a low map representation. t-Distributed stochastic neighbor embedding (tSNE) enables the visualization of high-dimensional nonlinear data by alleviating the crowding problem of SNE and thus is able to visualize high-dimensional data in a single map representation.
- The application of t-SNE to the landmarks at level Ls, using the similarity matrix PS as input, reveals clusters of landmarks; the hierarchical nature of the landmarks mean that these clusters represent larger structures in the high-dimensional data (and in which the hierarchical level determines the scale of the data structures revealed by the t-SNE analysis).
- 48 Recent progress has been made by Pezzotti and coworkers, in which the hierarchical stochastic neighbor embedding (HSNE) is used to create a hierarchical representation of the nonlinear data, allowing scalable exploration of the high-dimensional space in a lowdimensional space by constructing 2D embeddings that contain a few hundred data points.
- 48 The ability of the HSNE to handle large volumes of highdimensional data with reasonable computational and memory complexity makes it promising for other biological application areas that face similar computational challenges, particularly areas of neurology and cancer research.

# Method Summary
- To this end, we present a framework that consists of (a) dimensionality reduction and data visualization using HSNE, (b) a method to derive 3D maps from selected structures in the HSNE embeddings, and (c) a method to identify tissue-speci ﬁc m/z features using the 3D spatial correlations between the 3D HSNE maps and the original 3D MSI data.
- 37 The hallmark of these algorithms is their ability to preserve local structures of high-dimensional data in a low map representation. t-Distributed stochastic neighbor embedding (tSNE) enables the visualization of high-dimensional nonlinear data by alleviating the crowding problem of SNE and thus is able to visualize high-dimensional data in a single map representation.
- The backbone of this methodology is HSNE, which ﬁrst constructs a hierarchical representation of the high-dimensional data using the landmarks and then interactive construction of a hierarchy of t-SNE embeddings.
- The HSNE algorithm automatically constructed the three hierarchical levels in 10 min on a PC workstation with a 3.5 GHz Intel Xeon processor and 128 GB memory, resulting in the overview embedding.
- 36 State-of-the-art nonlinear dimensionality reduction is a family of algorithms inherited from Stochastic Neighbor Embedding (SNE).
- 48 Recent progress has been made by Pezzotti and coworkers, in which the hierarchical stochastic neighbor embedding (HSNE) is used to create a hierarchical representation of the nonlinear data, allowing scalable exploration of the high-dimensional space in a lowdimensional space by constructing 2D embeddings that contain a few hundred data points.
- 2018. “Interactive Visual Exploration of 3D Mass Spectrometry Imaging Data Using Hierarchical Stochastic Neighbor Embedding Reveals Spatiomolecular Structures at Full Data Resolution.” Journal of Proteome Research 17 (3): 1054-1064. doi:10.1021/acs.jproteome.7b00725. http://dx.doi.org/10.1021/acs.jproteome.7b00725.

# When To Use / Not Use
- Use when:
  - This is an important distinction because it means HSNE is implicitly more scalable in terms of computational and memory complexity and avoids the crowded maps that result from analyzing millions of data points and that would otherwise hinder the identi ﬁcation of clusters.
  - 48 Recent progress has been made by Pezzotti and coworkers, in which the hierarchical stochastic neighbor embedding (HSNE) is used to create a hierarchical representation of the nonlinear data, allowing scalable exploration of the high-dimensional space in a lowdimensional space by constructing 2D embeddings that contain a few hundred data points.
- Avoid when:
  - MALDI can be used to analyze a diverse range of molecular classes just by changing the tissue preparation method, DESI is able to provide molecular information about lipids without any tissue preparation, and SIMS provides very high spatial resolution capabilities also without any tissue preparation.
  - 2018, 17, 1054 −1064 This is an open access article published under a Creative Commons Non-Commercial No Derivative Works (CC-BY-NC-ND) Attribution License, which permits copying and redistribution of the article, and creation of adaptations, all for non-commercial purposes. and mass spectra.
- Failure modes:
  - DISCUSSION The proposed methodology is the ﬁrst of its kind, to the best of our knowledge, to handle the computational challenges of 3D MSI data analysis at full spatial and mass spectral resolution and in a reasonable time frame while maintaining high accuracy.

# Metrics Mentioned
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- 48 Recent progress has been made by Pezzotti and coworkers, in which the hierarchical stochastic neighbor embedding (HSNE) is used to create a hierarchical representation of the nonlinear data, allowing scalable exploration of the high-dimensional space in a lowdimensional space by constructing 2D embeddings that contain a few hundred data points.
- This is an important distinction because it means HSNE is implicitly more scalable in terms of computational and memory complexity and avoids the crowded maps that result from analyzing millions of data points and that would otherwise hinder the identi ﬁcation of clusters.
- For 3D MSI, a similar approach can be used to coregister the MSI data sets from sequential tissue sections; namely, the global registration parameters (e.g., rotation and translation) are corrected using each tissue section ’s individual t-SNE segmentation map.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-123-C1 | stance: support | summary: 37 The hallmark of these algorithms is their ability to preserve local structures of high-dimensional data in a low map representation. t-Distributed stochastic neighbor embedding (tSNE) enables the visualization of high-dimensional nonlinear data by alleviating the crowding problem of SNE and thus is able to visualize high-dimensional data in a single map representation. | evidence_ids: PENDING-REF-123-E1, PENDING-REF-123-E2
- CLAIM-PENDING-REF-123-C2 | stance: support | summary: To this end, we present a framework that consists of (a) dimensionality reduction and data visualization using HSNE, (b) a method to derive 3D maps from selected structures in the HSNE embeddings, and (c) a method to identify tissue-speci ﬁc m/z features using the 3D spatial correlations between the 3D HSNE maps and the original 3D MSI data. | evidence_ids: PENDING-REF-123-E3, PENDING-REF-123-E4
- CLAIM-PENDING-REF-123-C3 | stance: support | summary: 48 Recent progress has been made by Pezzotti and coworkers, in which the hierarchical stochastic neighbor embedding (HSNE) is used to create a hierarchical representation of the nonlinear data, allowing scalable exploration of the high-dimensional space in a lowdimensional space by constructing 2D embeddings that contain a few hundred data points. | evidence_ids: PENDING-REF-123-E5, PENDING-REF-123-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-REF-123-E1 | page: 3, section: extracted, quote: "37 The hallmark of these algorithms is their ability to preserve local structures of high-dimensional data in a low map representation. t-Distributed stochastic neighbor embedding (tSNE) enables the visualization of high-dimensional nonlinear data by alleviating the crowding problem of SNE and thus is able to visualize high-dimensional data in a single map representation."
- PENDING-REF-123-E2 | page: 4, section: extracted, quote: "The application of t-SNE to the landmarks at level Ls, using the similarity matrix PS as input, reveals clusters of landmarks; the hierarchical nature of the landmarks mean that these clusters represent larger structures in the high-dimensional data (and in which the hierarchical level determines the scale of the data structures revealed by the t-SNE analysis)."
- PENDING-REF-123-E3 | page: 3, section: extracted, quote: "48 Recent progress has been made by Pezzotti and coworkers, in which the hierarchical stochastic neighbor embedding (HSNE) is used to create a hierarchical representation of the nonlinear data, allowing scalable exploration of the high-dimensional space in a lowdimensional space by constructing 2D embeddings that contain a few hundred data points."
- PENDING-REF-123-E4 | page: 10, section: extracted, quote: "48 The ability of the HSNE to handle large volumes of highdimensional data with reasonable computational and memory complexity makes it promising for other biological application areas that face similar computational challenges, particularly areas of neurology and cancer research."
- PENDING-REF-123-E5 | page: 3, section: extracted, quote: "To this end, we present a framework that consists of (a) dimensionality reduction and data visualization using HSNE, (b) a method to derive 3D maps from selected structures in the HSNE embeddings, and (c) a method to identify tissue-speci ﬁc m/z features using the 3D spatial correlations between the 3D HSNE maps and the original 3D MSI data."
- PENDING-REF-123-E6 | page: 9, section: extracted, quote: "The backbone of this methodology is HSNE, which ﬁrst constructs a hierarchical representation of the high-dimensional data using the landmarks and then interactive construction of a hierarchy of t-SNE embeddings."
- PENDING-REF-123-E7 | page: 6, section: extracted, quote: "The HSNE algorithm automatically constructed the three hierarchical levels in 10 min on a PC workstation with a 3.5 GHz Intel Xeon processor and 128 GB memory, resulting in the overview embedding."
- PENDING-REF-123-E8 | page: 3, section: extracted, quote: "36 State-of-the-art nonlinear dimensionality reduction is a family of algorithms inherited from Stochastic Neighbor Embedding (SNE)."
