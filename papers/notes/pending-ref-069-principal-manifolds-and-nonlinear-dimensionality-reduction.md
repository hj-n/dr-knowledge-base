---
id: paper-2004-pending-ref-069
title: "Principal manifolds and nonlinear dimensionality reduction via tangent space alignment"
authors: "Z. Zhang and H. Zha"
venue: "Journal of Shanghai University (English Edition)"
year: 2004
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-069-2004-principal-manifolds-and-nonlinear-dimensionality-reduction-via-tangent-space-alignmen.pdf
seed_note_id: "paper-2019-mdp-visual-analytics-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- Therefore, a natural way to approximate the global coordinate is to ﬁnd a global coordinate τ and a local aﬃne transformation Pτ that minimize the error function ∫ dτ ∫ Ω(τ ) ∥Pτ (¯τ−τ )−θ τ∥d¯τ .(3.3) This represents a nonlinear alignment approach for the dimension reduction problem (this idea will be picked up at the end of section 4).
- Recently, there have been much renewed interests in develop ing eﬃcient algorithms for constructing nonlinear low-dimensional manifo lds from sample data points in high-dimensional spaces, emphasizing simple algorithm ic implementation and avoid- ∗ Department of Mathematics, Zhejiang University, Yuquan Ca mpus, Hangzhou, 310027, P.
- The rest of the paper is organized as follows: in section 2, we formulate the problem of manifold learning and dimension reduction in mor e precise terms, and illustrate the intricacy of the problem using the linear cas e as an example.
- Ot herwise, the learning problem becomes the well-researched nonlinear regression problem (for a more detailed discussion, see [4] where techniques from computational ge ometry was used to solve error-free manifold learning problems).

# Method Summary
- The LTSA algorithm can be considered as an approach to ﬁnd an approximate solution to the above minimization probl em.
- The lowdimensional embedding coordinate matrix computed by the LT SA algorithm is denoted by T = [ τ 1, . . . , τ N ].
- In this paper, we proposed a new algorithm (LTSA) for nonlinear manifold learning and nonline ar dimension reduction.
- In this section, we present several numerical examples to illustrate the performance of our LTSA algorithm.
- In this paper we present a new algorithm for manifold learning and no nlinear dimension reduction.
- In this paper, we address two inte r-related objectives of nonlinear structure ﬁnding: 1) to construct the so-called p rincipal manifold [6] that goes through “the middle” of the data points; and 2) to ﬁnd the global coordinate system (the natural parametrization space) that character izes the set of data points in a low-dimensional space.
- Therefore, a natural way to approximate the global coordinate is to ﬁnd a global coordinate τ and a local aﬃne transformation Pτ that minimize the error function ∫ dτ ∫ Ω(τ ) ∥Pτ (¯τ−τ )−θ τ∥d¯τ .(3.3) This represents a nonlinear alignment approach for the dimension reduction problem (this idea will be picked up at the end of section 4).

# When To Use / Not Use
- Use when:
  - Tw o lines of research of manifold learning and nonlinear dimension reduction have e merged: one is exempliﬁed by [2, 3, 18] where pairwise geodesic distances of the data points with respect to the underlying manifold are estimated, and the classical mu lti-dimensional scaling is used to project the data points into a low-dimensional space that best preserves the geodesic distances.
  - Recently, there have been much renewed interests in develop ing eﬃcient algorithms for constructing nonlinear low-dimensional manifo lds from sample data points in high-dimensional spaces, emphasizing simple algorithm ic implementation and avoid- ∗ Department of Mathematics, Zhejiang University, Yuquan Ca mpus, Hangzhou, 310027, P.
- Avoid when:
  - In particular, the local linear embeddin g (LLE) method constructs a local geometric structure that is invariant to translations and orthogonal transformations in a neighborhood of each data points and se eks to project the data points into a low-dimensional space that best preserves tho se local geometries [14, 16].
  - Consider computing the best d-dimensional aﬃne subspace approximation for the data points in Xi, min x, Θ,Q k∑ j=1  xij−(x + Qθ j)  2 2 = min x, Θ,Q  Xi−(xeT + QΘ)  2 2 , where Q is of d columns and is orthonormal, and Θ = [ θ 1, . . . , θ k].
- Failure modes:
  - The basic idea of our approach is to use the tangent space in the neighborhood of a data point to represent the local geo metry, and then align those local tangent spaces to construct the global coordina te system for the nonlinear manifold.

# Metrics Mentioned
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- We need to investigate a proper formulation of the problem and t he related optimization methods.
- 1 2 ZHENYUE ZHANG AND HONGYUAN ZHA ing optimization problems prone to local minima [14, 18].
- The parameterization of F can be ﬁxed by requiring that τ has a uniform distribution over C.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-069-C1 | stance: support | summary: Therefore, a natural way to approximate the global coordinate is to ﬁnd a global coordinate τ and a local aﬃne transformation Pτ that minimize the error function ∫ dτ ∫ Ω(τ ) ∥Pτ (¯τ−τ )−θ τ∥d¯τ .(3.3) This represents a nonlinear alignment approach for the dimension reduction problem (this idea will be picked up at the end of section 4). | evidence_ids: PENDING-REF-069-E1, PENDING-REF-069-E2
- CLAIM-PENDING-REF-069-C2 | stance: support | summary: The LTSA algorithm can be considered as an approach to ﬁnd an approximate solution to the above minimization probl em. | evidence_ids: PENDING-REF-069-E3, PENDING-REF-069-E4
- CLAIM-PENDING-REF-069-C3 | stance: support | summary: We need to investigate a proper formulation of the problem and t he related optimization methods. | evidence_ids: PENDING-REF-069-E5, PENDING-REF-069-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-REF-069-E1 | page: 5, section: extracted, quote: "Therefore, a natural way to approximate the global coordinate is to ﬁnd a global coordinate τ and a local aﬃne transformation Pτ that minimize the error function ∫ dτ ∫ Ω(τ ) ∥Pτ (¯τ−τ )−θ τ∥d¯τ .(3.3) This represents a nonlinear alignment approach for the dimension reduction problem (this idea will be picked up at the end of section 4)."
- PENDING-REF-069-E2 | page: 1, section: extracted, quote: "Recently, there have been much renewed interests in develop ing eﬃcient algorithms for constructing nonlinear low-dimensional manifo lds from sample data points in high-dimensional spaces, emphasizing simple algorithm ic implementation and avoid- ∗ Department of Mathematics, Zhejiang University, Yuquan Ca mpus, Hangzhou, 310027, P."
- PENDING-REF-069-E3 | page: 2, section: extracted, quote: "The rest of the paper is organized as follows: in section 2, we formulate the problem of manifold learning and dimension reduction in mor e precise terms, and illustrate the intricacy of the problem using the linear cas e as an example."
- PENDING-REF-069-E4 | page: 3, section: extracted, quote: "Ot herwise, the learning problem becomes the well-researched nonlinear regression problem (for a more detailed discussion, see [4] where techniques from computational ge ometry was used to solve error-free manifold learning problems)."
- PENDING-REF-069-E5 | page: 8, section: extracted, quote: "The LTSA algorithm can be considered as an approach to ﬁnd an approximate solution to the above minimization probl em."
- PENDING-REF-069-E6 | page: 10, section: extracted, quote: "The lowdimensional embedding coordinate matrix computed by the LT SA algorithm is denoted by T = [ τ 1, . . . , τ N ]."
- PENDING-REF-069-E7 | page: 18, section: extracted, quote: "In this paper, we proposed a new algorithm (LTSA) for nonlinear manifold learning and nonline ar dimension reduction."
- PENDING-REF-069-E8 | page: 14, section: extracted, quote: "In this section, we present several numerical examples to illustrate the performance of our LTSA algorithm."
