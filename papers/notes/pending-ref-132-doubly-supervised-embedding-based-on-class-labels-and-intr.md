---
id: paper-2015-pending-ref-132
title: "Doubly supervised embedding based on class labels and intrinsic clusters for highdimensional data visualization"
authors: "H. Kim, J. Choo, C. Reddy, and H. Park"
venue: "Neurocomputing"
year: 2015
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-132-2015-doubly-supervised-embedding-based-on-class-labels-and-intrinsic-clusters-for-highdime.pdf
seed_note_id: "paper-2019-mdp-visual-analytics-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- The goal of this survey is to give a comprehensive review of ex - isting work and recent advances in this research area, and to discuss some of the most challenging issues and open problems that co uld potentially lead to new research directions.
- Initially, it arises as an eﬀortless way to perform an inner product⟨x, y⟩ in a high-dimensional feature space H for some data points x, y∈X .

# Method Summary
- The embedding of distribution s enables us to apply RKHS methods to probability measures which promp ts a wide range of applications such as kernel two-sample testin g, independent testing, group anomaly detection, and learning on dist ributional data.
- In addition to the classical applications o f kernel methods, the kernel mean embedding has found novel applications in ﬁelds ranging from probabilistic modeling to statistical infere nce, causal discovery, and deep learning.
- In words, the idea of kernel mean embedding is to extend the feature map φ to the space of probability distributions by representing each distribution P as a mean function φ (P) = µ P := ∫ X k(x,·) dP(x), (1.1) where k : X×X → R is a symmetric and positive deﬁnite kernel function ( Berlinet and Thomas-Agnan 2004 , Smola et al.
- To the best of our knowledge, there is no comparable re view in this area so far; however, the short review paper of Song et al. (2013) on Hilbert space embedding of conditional distributions an d its applications in nonparametric inference in graphical models may be of interest to some readers.
- The survey begin s with a brief introduction to the RKHS and positive deﬁnite kernels which forms the backbone of this survey, followed by a thorough discussion of the Hilbert space embedding of marginal distributions, theoretical gu arantees, and a review of its applications.
- The conditional mean embedding enables us to perform sum, produ ct, and Bayes’ rules—which are ubiquitous in graphical model, prob abilistic inference, and reinforcement learning—in a non-parametri c way using the new representation of distributions in RKHS.
- 2 1 Introduction This work aims to provide a comprehensive review of kernel me an embeddings of distributions and, in the course of doing so, dis cusses some challenging issues that could potentially lead to new resea rch directions.

# When To Use / Not Use
- Use when:
  - The embedding of distribution s enables us to apply RKHS methods to probability measures which promp ts a wide range of applications such as kernel two-sample testin g, independent testing, group anomaly detection, and learning on dist ributional data.
  - In addition to the classical applications o f kernel methods, the kernel mean embedding has found novel applications in ﬁelds ranging from probabilistic modeling to statistical infere nce, causal discovery, and deep learning.
- Avoid when:
  - In words, the idea of kernel mean embedding is to extend the feature map φ to the space of probability distributions by representing each distribution P as a mean function φ (P) = µ P := ∫ X k(x,·) dP(x), (1.1) where k : X×X → R is a symmetric and positive deﬁnite kernel function ( Berlinet and Thomas-Agnan 2004 , Smola et al.
  - To the best of our knowledge, there is no comparable re view in this area so far; however, the short review paper of Song et al. (2013) on Hilbert space embedding of conditional distributions an d its applications in nonparametric inference in graphical models may be of interest to some readers.
- Failure modes:
  - To the best of our knowledge, there is no comparable re view in this area so far; however, the short review paper of Song et al. (2013) on Hilbert space embedding of conditional distributions an d its applications in nonparametric inference in graphical models may be of interest to some readers.

# Metrics Mentioned
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- In addition to the classical applications o f kernel methods, the kernel mean embedding has found novel applications in ﬁelds ranging from probabilistic modeling to statistical infere nce, causal discovery, and deep learning.
- In words, the idea of kernel mean embedding is to extend the feature map φ to the space of probability distributions by representing each distribution P as a mean function φ (P) = µ P := ∫ X k(x,·) dP(x), (1.1) where k : X×X → R is a symmetric and positive deﬁnite kernel function ( Berlinet and Thomas-Agnan 2004 , Smola et al.
- To the best of our knowledge, there is no comparable re view in this area so far; however, the short review paper of Song et al. (2013) on Hilbert space embedding of conditional distributions an d its applications in nonparametric inference in graphical models may be of interest to some readers.
- The survey begin s with a brief introduction to the RKHS and positive deﬁnite kernels which forms the backbone of this survey, followed by a thorough discussion of the Hilbert space embedding of marginal distributions, theoretical gu arantees, and a review of its applications.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-132-C1 | stance: support | summary: The goal of this survey is to give a comprehensive review of ex - isting work and recent advances in this research area, and to discuss some of the most challenging issues and open problems that co uld potentially lead to new research directions. | evidence_ids: PENDING-REF-132-E1, PENDING-REF-132-E2
- CLAIM-PENDING-REF-132-C2 | stance: support | summary: The embedding of distribution s enables us to apply RKHS methods to probability measures which promp ts a wide range of applications such as kernel two-sample testin g, independent testing, group anomaly detection, and learning on dist ributional data. | evidence_ids: PENDING-REF-132-E3, PENDING-REF-132-E4
- CLAIM-PENDING-REF-132-C3 | stance: support | summary: In addition to the classical applications o f kernel methods, the kernel mean embedding has found novel applications in ﬁelds ranging from probabilistic modeling to statistical infere nce, causal discovery, and deep learning. | evidence_ids: PENDING-REF-132-E5, PENDING-REF-132-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance
- step: 6 | relevance: high | note: guides reliable interpretation of projected views

# Evidence
- PENDING-REF-132-E1 | page: 4, section: extracted, quote: "The goal of this survey is to give a comprehensive review of ex - isting work and recent advances in this research area, and to discuss some of the most challenging issues and open problems that co uld potentially lead to new research directions."
- PENDING-REF-132-E2 | page: 6, section: extracted, quote: "Initially, it arises as an eﬀortless way to perform an inner product⟨x, y⟩ in a high-dimensional feature space H for some data points x, y∈X ."
- PENDING-REF-132-E3 | page: 4, section: extracted, quote: "The embedding of distribution s enables us to apply RKHS methods to probability measures which promp ts a wide range of applications such as kernel two-sample testin g, independent testing, group anomaly detection, and learning on dist ributional data."
- PENDING-REF-132-E4 | page: 4, section: extracted, quote: "In addition to the classical applications o f kernel methods, the kernel mean embedding has found novel applications in ﬁelds ranging from probabilistic modeling to statistical infere nce, causal discovery, and deep learning."
- PENDING-REF-132-E5 | page: 7, section: extracted, quote: "In words, the idea of kernel mean embedding is to extend the feature map φ to the space of probability distributions by representing each distribution P as a mean function φ (P) = µ P := ∫ X k(x,·) dP(x), (1.1) where k : X×X → R is a symmetric and positive deﬁnite kernel function ( Berlinet and Thomas-Agnan 2004 , Smola et al."
- PENDING-REF-132-E6 | page: 6, section: extracted, quote: "To the best of our knowledge, there is no comparable re view in this area so far; however, the short review paper of Song et al. (2013) on Hilbert space embedding of conditional distributions an d its applications in nonparametric inference in graphical models may be of interest to some readers."
- PENDING-REF-132-E7 | page: 4, section: extracted, quote: "The survey begin s with a brief introduction to the RKHS and positive deﬁnite kernels which forms the backbone of this survey, followed by a thorough discussion of the Hilbert space embedding of marginal distributions, theoretical gu arantees, and a review of its applications."
- PENDING-REF-132-E8 | page: 4, section: extracted, quote: "The conditional mean embedding enables us to perform sum, produ ct, and Bayes’ rules—which are ubiquitous in graphical model, prob abilistic inference, and reinforcement learning—in a non-parametri c way using the new representation of distributions in RKHS."
