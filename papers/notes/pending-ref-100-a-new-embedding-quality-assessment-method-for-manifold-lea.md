---
id: paper-2012-pending-ref-100
title: "A new embedding quality assessment method for manifold learning"
authors: "P. Zhang, Y. Ren, and B. Zhang"
venue: "Neurocomputing"
year: 2012
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-100-2012-a-new-embedding-quality-assessment-method-for-manifold-learning.pdf
seed_note_id: "paper-2019-mdp-visual-analytics-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- I NTRODUCTION A LONG with the advance of techniques to collect and store large sets of high-dimensional data, how to efﬁciently process such data issues a challenge for many ﬁelds in computer science, such as pattern recognition, visual understanding and data mining.
- Since NIEQA uses ASIM to assess the similarity between patches in high-dimensional input space and their corresponding low-dimensional embeddings, the distortion caused by normalization can be eliminated.
- P i ∈St(n,m ) . (14) 3) Computation of P ∗ i : In the third step, we use gradient descent method over matrix manifold to solve Eq. (14), which is an optimization problem for matrix function over the Stiefel manifold St(n,m ).
- A crucial issue with current manifold learning methods is that they lack a natural quantitative measure to assess the quality of learned embeddings, which greatly limits their applications to real-world problems.

# Method Summary
- C ONCLUSIONS AND DISCUSSIONS In this paper, we proposed a novel normalization independent embedding quality assessment (NIEQA) method for manifold learning, which has wider application range than current approaches.
- Then based on ASIM, we propose a novel embedding quality assessment method, named Normalization Independent Embedding Quality Assessment (NIEQA), which can efﬁciently assess the quality of normalized embeddings quantitatively.
- According to motivation and application range, existent embedding quality assessment methods can be categorized into two groups: local approaches and global approaches.
- In this section, we propose Normalization Independent Embedding Quality Assessment method (NIEQA) to address these two issues, which is independent of normalization.
- A crucial issue with current manifold learning methods is that they lack a natural quantitative measure to assess the quality of learned embeddings, which greatly limits their applications to real-world problems.
- Recently, many methods have been proposed to efﬁciently ﬁnd meaningful low-dimensional embeddings from manifoldmodeled data, and they form a family of dimensionality reduction methods called manifold learning .
- 1 A new embedding quality assessment method for manifold learning Peng Zhang Member, IEEE, Yuanyuan Ren, and Bo Zhang Abstract—Manifold learning is a hot research topic in the ﬁeld of computer science.

# When To Use / Not Use
- Use when:
  - For each Xi and Yi, their method ﬁrst uses Procrustes analysis [24]–[26] to ﬁnd an 3 optimal rigid motion transformation, consisting of a rotation and a translation, after which Yi best matches Xi.
  - A possible solution to this issue is to implement denoising or outlier removal process before training. • Based on NIEQA, whether we can design a manifold learning method with better learning performance is also one of our future works.
- Avoid when:
  - P i ∈St(n,m ) . (14) 3) Computation of P ∗ i : In the third step, we use gradient descent method over matrix manifold to solve Eq. (14), which is an optimization problem for matrix function over the Stiefel manifold St(n,m ).
  - Since NIEQA uses ASIM to assess the similarity between patches in high-dimensional input space and their corresponding low-dimensional embeddings, the distortion caused by normalization can be eliminated.
- Failure modes:
  - Their assessment is used for automatic choice of the number of nearest neighbors for LLE [30] and also exploited in [31] to evaluate the embedding quality of LLE with optimal regularization parameter.

# Metrics Mentioned
- `trustworthiness`: referenced as part of projection-quality or reliability assessment.
- `continuity`: referenced as part of projection-quality or reliability assessment.
- `co-ranking`: referenced as part of projection-quality or reliability assessment.
- `procrustes-based quality`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- Then ∇¯φ(Pi) is given by the following formula ∇¯φ(Pi) = 2Miδ2(P T i Mi) , and by using Eq. (15), ∇φ(Pi) now reads ∇φ(Pi) = 2Miδ2(P T i Mi)−PiP T i δ2(P T i Mi)−Pδ 2(P T i Mi)M T i Pi. (17) Given a step length for iteration, we apply gradient descent method to ﬁnd P ∗ i such that ∇φ(Pi) vanishes.
- P i ∈St(n,m ) . (14) 3) Computation of P ∗ i : In the third step, we use gradient descent method over matrix manifold to solve Eq. (14), which is an optimization problem for matrix function over the Stiefel manifold St(n,m ).
- Their assessment is used for automatic choice of the number of nearest neighbors for LLE [30] and also exploited in [31] to evaluate the embedding quality of LLE with optimal regularization parameter.
- Using NIEQA to provide quantitative evaluations on learned embeddings, we can select optimal parameters for a speciﬁc method and compare the performance among different methods.
- In the third experiment, we apply NIEQA to model evaluation of the Gaussian manifold, whose parameter equation is    x1 = u1 x2 = u2 x3 = (1 /2π) exp{−((u1)2 + (u2)2)/2} .
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-100-C1 | stance: support | summary: I NTRODUCTION A LONG with the advance of techniques to collect and store large sets of high-dimensional data, how to efﬁciently process such data issues a challenge for many ﬁelds in computer science, such as pattern recognition, visual understanding and data mining. | evidence_ids: PENDING-REF-100-E1, PENDING-REF-100-E2
- CLAIM-PENDING-REF-100-C2 | stance: support | summary: C ONCLUSIONS AND DISCUSSIONS In this paper, we proposed a novel normalization independent embedding quality assessment (NIEQA) method for manifold learning, which has wider application range than current approaches. | evidence_ids: PENDING-REF-100-E3, PENDING-REF-100-E4
- CLAIM-PENDING-REF-100-C3 | stance: support | summary: Then ∇¯φ(Pi) is given by the following formula ∇¯φ(Pi) = 2Miδ2(P T i Mi) , and by using Eq. (15), ∇φ(Pi) now reads ∇φ(Pi) = 2Miδ2(P T i Mi)−PiP T i δ2(P T i Mi)−Pδ 2(P T i Mi)M T i Pi. (17) Given a step length for iteration, we apply gradient descent method to ﬁnd P ∗ i such that ∇φ(Pi) vanishes. | evidence_ids: PENDING-REF-100-E5, PENDING-REF-100-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-REF-100-E1 | page: 1, section: extracted, quote: "I NTRODUCTION A LONG with the advance of techniques to collect and store large sets of high-dimensional data, how to efﬁciently process such data issues a challenge for many ﬁelds in computer science, such as pattern recognition, visual understanding and data mining."
- PENDING-REF-100-E2 | page: 2, section: extracted, quote: "Since NIEQA uses ASIM to assess the similarity between patches in high-dimensional input space and their corresponding low-dimensional embeddings, the distortion caused by normalization can be eliminated."
- PENDING-REF-100-E3 | page: 6, section: extracted, quote: "P i ∈St(n,m ) . (14) 3) Computation of P ∗ i : In the third step, we use gradient descent method over matrix manifold to solve Eq. (14), which is an optimization problem for matrix function over the Stiefel manifold St(n,m )."
- PENDING-REF-100-E4 | page: 1, section: extracted, quote: "A crucial issue with current manifold learning methods is that they lack a natural quantitative measure to assess the quality of learned embeddings, which greatly limits their applications to real-world problems."
- PENDING-REF-100-E5 | page: 12, section: extracted, quote: "C ONCLUSIONS AND DISCUSSIONS In this paper, we proposed a novel normalization independent embedding quality assessment (NIEQA) method for manifold learning, which has wider application range than current approaches."
- PENDING-REF-100-E6 | page: 2, section: extracted, quote: "Then based on ASIM, we propose a novel embedding quality assessment method, named Normalization Independent Embedding Quality Assessment (NIEQA), which can efﬁciently assess the quality of normalized embeddings quantitatively."
- PENDING-REF-100-E7 | page: 2, section: extracted, quote: "According to motivation and application range, existent embedding quality assessment methods can be categorized into two groups: local approaches and global approaches."
- PENDING-REF-100-E8 | page: 7, section: extracted, quote: "In this section, we propose Normalization Independent Embedding Quality Assessment method (NIEQA) to address these two issues, which is independent of normalization."
