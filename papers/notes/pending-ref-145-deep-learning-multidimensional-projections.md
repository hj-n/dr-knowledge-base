---
id: paper-2020-pending-ref-145
title: "Deep learning multidimensional projections"
authors: "M. Espadoto, N. S. T. Hirata, and A. C. Telea"
venue: "Information Visualization"
year: 2020
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-145-2020-deep-learning-multidimensional-projections.pdf
seed_note_id: "paper-2024-large-scale-text-spatialization"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- Last but not least, we consider more reﬁned approaches to tackle the transfer learning problem for generalizing learning from a given number of jointly considered data universes and projection techniques.
- When one avails of a large datasetD, which consistently samples a given problem domain, we can thus train once and next use the trained network many times to cover all applications within that domain.
- 1 Introduction Exploring high-dimensional data sets is a key task in many application domains such as statistics, data science, machine learning, and information visualization.
- First, we consider generalizing our approach to compute stable projections of dynamic (time-dependent) high-dimensional data and also mixed quantitative-andqualitative data.

# Method Summary
- Our approach generates projections with similar characteristics as the learned ones, is computationally two to three orders of magnitude faster than SNE-class methods, has no complex-to-set user parameters, handles out-of-sample data in a stable manner, and can be used to learn any projection technique.
- Also, note that there is nothing speciﬁc in the implementations of PCA, Isomap, MDS, or LLE in our approach: We claim, although we cannot (of course) formally prove, that we can learn any projection in the same way, since our method does not use any speciﬁcs of the learned projection technique.
- 6 Conclusion We have presented a new method for creating projections of high-dimensional data using a machine learning approach.
- We propose a learning approach to construct such projections.
- Separately, given the dense structure of the fully-conneted network we use (which averages activations from multiple units in an earlier layer to determine those of the current layer), our approach is stable in the sense that small changes in an input dataset yield only small changes in the resulting projection (see example in Sec.
- Ideally, a stable projection technique should not change P(D) if D does not change at all, regardless of changes in parameters of the algorithm P; and conversely, when D changes, e.g. as new samples are added, then the old samples should stay in P(D) as close as possible to their original locations.
- In this family of techniques, dimensionality reduction methods, also called projections, have a particular place: Compared to all other techniques, they scale much better in terms of both the number of samples and the number of dimensions they can accommodate (show) on a given screen space area.

# When To Use / Not Use
- Use when:
  - The ReNDA algorithm [BLS17] is a very recent neural-based approach that uses two networks, improving on earlier work from the same authors.
  - Probably the best known DR method is Principal Component Analysis [Jol86] (PCA), which has been used in several areas for many decades.
- Avoid when:
  - Yet, t-SNE comes with some downsides: It can be very slow to run on large data sets (thousands of observations or more), due to its quadratic nature; its parameters can be tricky to get right, which can lead to unpredictable results; and it lacks the capability of projecting out-of-sample data, which is useful when comparing several (time dependent) datasets [RFT16, NA18].
  - Separately, given the dense structure of the fully-conneted network we use (which averages activations from multiple units in an earlier layer to determine those of the current layer), our approach is stable in the sense that small changes in an input dataset yield only small changes in the resulting projection (see example in Sec.
- Failure modes:
  - Despite its high scoring on the quality criterion (high C1), t-SNE can be very slow (low C2), since it has a complexity of O(N2) in sample count, is very sensitive to small changes in the data (low C5), can be very hard to tune (low C3) in order to get good visualizations, and does not have out-of-sample capability.

# Metrics Mentioned
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- Yet, t-SNE comes with some downsides: It can be very slow to run on large data sets (thousands of observations or more), due to its quadratic nature; its parameters can be tricky to get right, which can lead to unpredictable results; and it lacks the capability of projecting out-of-sample data, which is useful when comparing several (time dependent) datasets [RFT16, NA18].
- Our approach generates projections with similar characteristics as the learned ones, is computationally two to three orders of magnitude faster than SNE-class methods, has no complex-to-set user parameters, handles out-of-sample data in a stable manner, and can be used to learn any projection technique.
- Ideally, a stable projection technique should not change P(D) if D does not change at all, regardless of changes in parameters of the algorithm P; and conversely, when D changes, e.g. as new samples are added, then the old samples should stay in P(D) as close as possible to their original locations.
- No other aspects or parameters of the training or inference process are projection-technique speciﬁc – that is, projections to be learned can be seen as black boxes.
- Moreover, small parameter changes, e.g., perplexity for t-SNE, or choice of control points for LAMP, to mention just a few, can yield large changes in P(D) [Wat16].
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-145-C1 | stance: support | summary: Last but not least, we consider more reﬁned approaches to tackle the transfer learning problem for generalizing learning from a given number of jointly considered data universes and projection techniques. | evidence_ids: PENDING-REF-145-E1, PENDING-REF-145-E2
- CLAIM-PENDING-REF-145-C2 | stance: support | summary: Our approach generates projections with similar characteristics as the learned ones, is computationally two to three orders of magnitude faster than SNE-class methods, has no complex-to-set user parameters, handles out-of-sample data in a stable manner, and can be used to learn any projection technique. | evidence_ids: PENDING-REF-145-E3, PENDING-REF-145-E4
- CLAIM-PENDING-REF-145-C3 | stance: support | summary: Yet, t-SNE comes with some downsides: It can be very slow to run on large data sets (thousands of observations or more), due to its quadratic nature; its parameters can be tricky to get right, which can lead to unpredictable results; and it lacks the capability of projecting out-of-sample data, which is useful when comparing several (time dependent) datasets [RFT16, NA18]. | evidence_ids: PENDING-REF-145-E5, PENDING-REF-145-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 4 | relevance: high | note: contains initialization sensitivity or control-policy evidence

# Evidence
- PENDING-REF-145-E1 | page: 13, section: extracted, quote: "Last but not least, we consider more reﬁned approaches to tackle the transfer learning problem for generalizing learning from a given number of jointly considered data universes and projection techniques."
- PENDING-REF-145-E2 | page: 9, section: extracted, quote: "When one avails of a large datasetD, which consistently samples a given problem domain, we can thus train once and next use the trained network many times to cover all applications within that domain."
- PENDING-REF-145-E3 | page: 1, section: extracted, quote: "1 Introduction Exploring high-dimensional data sets is a key task in many application domains such as statistics, data science, machine learning, and information visualization."
- PENDING-REF-145-E4 | page: 13, section: extracted, quote: "First, we consider generalizing our approach to compute stable projections of dynamic (time-dependent) high-dimensional data and also mixed quantitative-andqualitative data."
- PENDING-REF-145-E5 | page: 1, section: extracted, quote: "Our approach generates projections with similar characteristics as the learned ones, is computationally two to three orders of magnitude faster than SNE-class methods, has no complex-to-set user parameters, handles out-of-sample data in a stable manner, and can be used to learn any projection technique."
- PENDING-REF-145-E6 | page: 9, section: extracted, quote: "Also, note that there is nothing speciﬁc in the implementations of PCA, Isomap, MDS, or LLE in our approach: We claim, although we cannot (of course) formally prove, that we can learn any projection in the same way, since our method does not use any speciﬁcs of the learned projection technique."
- PENDING-REF-145-E7 | page: 13, section: extracted, quote: "6 Conclusion We have presented a new method for creating projections of high-dimensional data using a machine learning approach."
- PENDING-REF-145-E8 | page: 1, section: extracted, quote: "We propose a learning approach to construct such projections."
