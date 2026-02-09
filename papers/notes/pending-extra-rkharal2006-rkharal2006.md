---
id: paper-2006-pending-extra-rkharal2006
title: "Semideﬁnite Embedding for the Dimensionality Reduction of DNA Microarray Data"
authors: "Reduction of DNA Microarray Data"
venue: "UNKNOWN"
year: 2006
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/rkharal2006.pdf
seed_note_id: "paper-2025-jeon-reliable-va-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- Dimensionality reduction of microarray data has yet to eﬀectively tackle the problem of ﬁnding a low dimensional embedding that provides an accurate visual representation of gene-to-gene interactions.
- In our work, we apply a dimensionality reduction approach that incorporates semideﬁnite programming and kernel alignment into the dimensionality reduction problem.
- Isomap and LLE result in some distortion to the original input data.
- 34 4.1.2 Problem Deﬁnition . . . . . . . . . . . . . . . . . . . .

# Method Summary
- Our method, KAS kernel alignment with semideﬁnite embedding, uses the semideﬁnite embedding algorithm ﬁrst described in [87], and a derivation of kernel alignment [73] in order to successfully tackle the dimensionality reduction of microarray data.
- Our method, KAS (kernel alignment with semideﬁnite embedding) , aids the visualization of microarray data in two dimensions and shows improvement over existing dimensionality reduction methods such as PCA, LLE and Isomap. iii Acknowledgements I would like to extend sincere appreciation to Forbes J.
- 68 6.1 Two dimensional outputs of dimensionality reduction methods tested on Breast Cancer Data: The output of each algorithm was clustered with K-Means clustering.
- The level of accuracy in a low dimensional embedding needs improvement for cur1 rent dimensionality reduction methods that have been applied to microarray data.
- We propose a novel approach for dimensionality reduction of microarray data that eﬀectively combines diﬀerent techniques in the study of DNA microarrays.
- Also, a special thanks to Kilian Weinberger for his explanations and many conversations regarding the semideﬁnite embedding algorithm.
- We describe, in detail, the full KAS algorithm and how it compares to more conventional dimensionality reduction methods in chapter 5.

# When To Use / Not Use
- Use when:
  - Our method, KAS kernel alignment with semideﬁnite embedding, uses the semideﬁnite embedding algorithm ﬁrst described in [87], and a derivation of kernel alignment [73] in order to successfully tackle the dimensionality reduction of microarray data.
  - KAS is a useful visual tool for both the understanding of gene-to-gene interactions and the replacing of a large unmanageable dataset with one of much lower dimensionality.
- Avoid when:
  - Conventionally, a dimensionality reduction technique may be used to reduce the size of the dataset before further processing.
  - Chapter 3 is a survey of prior work and discusses three dimensionality reduction methods in use today.
- Failure modes:
  - fold learning algorithms for localization in wireless sensor networks.

# Metrics Mentioned
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- Using SeDuMi 1.02, a MATLAB toolbox for optimization over symmetric cones.
- 104 A.2 Mathematical Optimization . . . . . . . . . . . . . . . . . . .
- 106 A.2.1 Convex Optimization Problems . . . . . . . . . . . . .
- Optimization Methods and Software , 11–12:625– 653, 1999.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-EXTRA-C1 | stance: support | summary: Dimensionality reduction of microarray data has yet to eﬀectively tackle the problem of ﬁnding a low dimensional embedding that provides an accurate visual representation of gene-to-gene interactions. | evidence_ids: PENDING-EXTRA-E1, PENDING-EXTRA-E2
- CLAIM-PENDING-EXTRA-C2 | stance: support | summary: Our method, KAS kernel alignment with semideﬁnite embedding, uses the semideﬁnite embedding algorithm ﬁrst described in [87], and a derivation of kernel alignment [73] in order to successfully tackle the dimensionality reduction of microarray data. | evidence_ids: PENDING-EXTRA-E3, PENDING-EXTRA-E4
- CLAIM-PENDING-EXTRA-C3 | stance: support | summary: Using SeDuMi 1.02, a MATLAB toolbox for optimization over symmetric cones. | evidence_ids: PENDING-EXTRA-E5, PENDING-EXTRA-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-EXTRA-E1 | page: 14, section: extracted, quote: "Dimensionality reduction of microarray data has yet to eﬀectively tackle the problem of ﬁnding a low dimensional embedding that provides an accurate visual representation of gene-to-gene interactions."
- PENDING-EXTRA-E2 | page: 15, section: extracted, quote: "In our work, we apply a dimensionality reduction approach that incorporates semideﬁnite programming and kernel alignment into the dimensionality reduction problem."
- PENDING-EXTRA-E3 | page: 11, section: extracted, quote: "Isomap and LLE result in some distortion to the original input data."
- PENDING-EXTRA-E4 | page: 7, section: extracted, quote: "34 4.1.2 Problem Deﬁnition . . . . . . . . . . . . . . . . . . . ."
- PENDING-EXTRA-E5 | page: 15, section: extracted, quote: "Our method, KAS kernel alignment with semideﬁnite embedding, uses the semideﬁnite embedding algorithm ﬁrst described in [87], and a derivation of kernel alignment [73] in order to successfully tackle the dimensionality reduction of microarray data."
- PENDING-EXTRA-E6 | page: 3, section: extracted, quote: "Our method, KAS (kernel alignment with semideﬁnite embedding) , aids the visualization of microarray data in two dimensions and shows improvement over existing dimensionality reduction methods such as PCA, LLE and Isomap. iii Acknowledgements I would like to extend sincere appreciation to Forbes J."
- PENDING-EXTRA-E7 | page: 11, section: extracted, quote: "68 6.1 Two dimensional outputs of dimensionality reduction methods tested on Breast Cancer Data: The output of each algorithm was clustered with K-Means clustering."
- PENDING-EXTRA-E8 | page: 3, section: extracted, quote: "The level of accuracy in a low dimensional embedding needs improvement for cur1 rent dimensionality reduction methods that have been applied to microarray data."
