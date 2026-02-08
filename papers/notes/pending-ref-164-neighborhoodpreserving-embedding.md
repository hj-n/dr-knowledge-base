---
id: paper-2005-pending-ref-164
title: "Neighborhoodpreserving embedding"
authors: "HeX,CaiD,YanS,ZhangH"
venue: "UNKNOWN"
year: 2005
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-164-2005-neighborhoodpreserving-embedding.pdf
seed_note_id: "paper-2015-gisbrecht-nonlinear-dr-visualization"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- One problem with this single-bit quantization (SBQ) is that the threshold θ (0 for most cases if the data are zero centered) typically lies in the region of the highest point density and consequently a lot of neighboring points close to the threshold might be hashed to totally different bits, which is unexpected according to the principle of hashing.
- One problem with this single-bit quantization (SBQ) is that the threshold typically lies in the region of the highest point density and consequently a lot of neighboring points close to the threshold will be hashed to totally different bits, which is unexpected according to the principle of hashing.
- Problem Deﬁnition Given a set of n data points S = {x1, x2, · · ·, xn} with xi ∈ Rd, the goal of hashing is to learn a mapping to encode point xi with a binary string yi ∈ { 0, 1}c, where c denotes the code size.
- In this paper, we clearly claim that using double bits with adaptively learned thresholds to quantize each projected dimension can completely solve the problem of SBQ.

# Method Summary
- One of the most recent data-dependent methods is iterative quantization (ITQ) (Gong and Lazebnik 2011) which ﬁnds an orthogonal rotation matrix to reﬁne the initial projection matrix learned by principal component analysis (PCA) so that the quantization error of mapping the data to the vertices of binary hypercube is minimized.
- Let’s take SH as an example. “SH-SBQ” denotes the original SH method based on single-bit quantization, “SH-HH” denotes the combination of SH projection with HH quantization (Liu et al.
- When the data have been normalized to have zero mean which is adopted by most methods, a common encoding approach is to use functionsgn(x), wheresgn(x) = 1 ifx ≥ 0 and 0 otherwise.
- 2011), and “SH-DBQ” denotes the method combining the SH projection with double-bit quantization.
- For most methods, the projection step is the most time-consuming step.
- These real-valued functions are often called projection functions (Andoni and Indyk 2008; Wang, Kumar, and Chang 2010; Gong and Lazebnik 2011), and each function corresponds to one of the c projected dimensions; • In the second stage, the real-valued vector zi is encoded into binary vector yi, typically by thresholding.
- In this paper, we just select the most representative methods for evaluation, which contain SH (Weiss, Torralba, and Fergus 2008), PCA (Gong and Lazebnik 2011), ITQ (Gong and Lazebnik 2011), LSH (Andoni and Indyk 2008), and SIKH (Raginsky and Lazebnik 2009).

# When To Use / Not Use
- Use when:
  - Because it is NP hard to directly compute the best binary codes for a given data set (Weiss, Torralba, and Fergus 2008), both data-independent and data-dependent hashing methods typically adopt a two-stage strategy.
  - Considering the shortcomings of data-independent methods, more and more recent works have focused on datadependent methods whose hash functions are learned from the training data.
- Avoid when:
  - Because it is NP hard to directly compute the best binary codes for a given data set, mainstream hashing methods typically adopt a two-stage strategy.
  - This result is caused by the limitation of Hamming distance.
- Failure modes:
  - Evaluation Protocols and Baseline Methods As the protocols widely used in recent papers (Weiss, Torralba, and Fergus 2008; Raginsky and Lazebnik 2009; Gong and Lazebnik 2011), Euclidean neighbors in the original space are considered as ground truth.

# Metrics Mentioned
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- Please note that threshold optimization techniques in (Liu et al.
- Let’s take SH as an example. “SH-SBQ” denotes the original SH method based on single-bit quantization, “SH-HH” denotes the combination of SH projection with HH quantization (Liu et al.
- When the data have been normalized to have zero mean which is adopted by most methods, a common encoding approach is to use functionsgn(x), wheresgn(x) = 1 ifx ≥ 0 and 0 otherwise.
- 2011), and “SH-DBQ” denotes the method combining the SH projection with double-bit quantization.
- For most methods, the projection step is the most time-consuming step.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-164-C1 | stance: support | summary: One problem with this single-bit quantization (SBQ) is that the threshold θ (0 for most cases if the data are zero centered) typically lies in the region of the highest point density and consequently a lot of neighboring points close to the threshold might be hashed to totally different bits, which is unexpected according to the principle of hashing. | evidence_ids: PENDING-REF-164-E1, PENDING-REF-164-E2
- CLAIM-PENDING-REF-164-C2 | stance: support | summary: One of the most recent data-dependent methods is iterative quantization (ITQ) (Gong and Lazebnik 2011) which ﬁnds an orthogonal rotation matrix to reﬁne the initial projection matrix learned by principal component analysis (PCA) so that the quantization error of mapping the data to the vertices of binary hypercube is minimized. | evidence_ids: PENDING-REF-164-E3, PENDING-REF-164-E4
- CLAIM-PENDING-REF-164-C3 | stance: support | summary: Please note that threshold optimization techniques in (Liu et al. | evidence_ids: PENDING-REF-164-E5, PENDING-REF-164-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-REF-164-E1 | page: 2, section: extracted, quote: "One problem with this single-bit quantization (SBQ) is that the threshold θ (0 for most cases if the data are zero centered) typically lies in the region of the highest point density and consequently a lot of neighboring points close to the threshold might be hashed to totally different bits, which is unexpected according to the principle of hashing."
- PENDING-REF-164-E2 | page: 1, section: extracted, quote: "One problem with this single-bit quantization (SBQ) is that the threshold typically lies in the region of the highest point density and consequently a lot of neighboring points close to the threshold will be hashed to totally different bits, which is unexpected according to the principle of hashing."
- PENDING-REF-164-E3 | page: 2, section: extracted, quote: "Problem Deﬁnition Given a set of n data points S = {x1, x2, · · ·, xn} with xi ∈ Rd, the goal of hashing is to learn a mapping to encode point xi with a binary string yi ∈ { 0, 1}c, where c denotes the code size."
- PENDING-REF-164-E4 | page: 2, section: extracted, quote: "In this paper, we clearly claim that using double bits with adaptively learned thresholds to quantize each projected dimension can completely solve the problem of SBQ."
- PENDING-REF-164-E5 | page: 2, section: extracted, quote: "One of the most recent data-dependent methods is iterative quantization (ITQ) (Gong and Lazebnik 2011) which ﬁnds an orthogonal rotation matrix to reﬁne the initial projection matrix learned by principal component analysis (PCA) so that the quantization error of mapping the data to the vertices of binary hypercube is minimized."
- PENDING-REF-164-E6 | page: 4, section: extracted, quote: "Let’s take SH as an example. “SH-SBQ” denotes the original SH method based on single-bit quantization, “SH-HH” denotes the combination of SH projection with HH quantization (Liu et al."
- PENDING-REF-164-E7 | page: 2, section: extracted, quote: "When the data have been normalized to have zero mean which is adopted by most methods, a common encoding approach is to use functionsgn(x), wheresgn(x) = 1 ifx ≥ 0 and 0 otherwise."
- PENDING-REF-164-E8 | page: 4, section: extracted, quote: "2011), and “SH-DBQ” denotes the method combining the SH projection with double-bit quantization."
