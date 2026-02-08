---
id: paper-2008-pending-ref-162
title: "Quality assessment of dimensionality reduction: Rank-based criteria"
authors: "Lee J.A, Verleysen M"
venue: "Neurocomputing"
year: 2008
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-162-2008-rank-based-quality-assessment-of-nonlinear-dimensionality-reduction.pdf
seed_note_id: "paper-2015-gisbrecht-nonlinear-dr-visualization"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- In the most general setting, dimensionality reduction transforms a set of N high-dimensional vectors, denoted Ξ =[ ξ i]1≤i≤N ,i n t oN low-dimensional vectors, denoted X =[ xi]1≤i≤N .
- 1 Introduction Dimensionality reduction (DR) gathers techniques that provide a meaningful low-dimensional representation of a high-dimensional data set.
- The rank of ξj with respect to ξi in the high-dimensional space is written as ρij = |{k : δik <δij or (δik = δij and k<j )}|.
- Nonlinear dimensionality reduction aims at providing lowdimensional representions of high-dimensional data sets.

# Method Summary
- As most NLDR methods optimize a given objective function, a simplistic way to assess the quality is to look at the value of the objective function after convergence.
- On the other hand, nonlinear dimensionality reduction [1] (NLDR) emerged later and has deeply evolved for the past twenty ﬁve years, with neural approaches [2, 3, 4] and spectral techniques [5, 6, 7].
- As a matter of fact, the scientiﬁc community has been focusing on the design of new NLDR methods and the question of quality assessment remains mostly unanswered.
- Furthermore, objective function s often fulﬁll some requirements, such ∗JAL is a Postdoctoral Researcher with the Belgian National Fund for Scientiﬁc Research.
- Obviously, this allows us to compare several runs with e.g. diﬀerent parameter values, but makes the comparison of diﬀerent methods unfair.
- Many new methods have been proposed in the recent years, but the question of their assessment and comparison remains open.
- Mo dern NLDR encompasses the domain of manifold learning and is also closely related to graph embedding [8].

# When To Use / Not Use
- Use when:
  - As most NLDR methods optimize a given objective function, a simplistic way to assess the quality is to look at the value of the objective function after convergence.
  - On the other hand, nonlinear dimensionality reduction [1] (NLDR) emerged later and has deeply evolved for the past twenty ﬁve years, with neural approaches [2, 3, 4] and spectral techniques [5, 6, 7].
- Avoid when:
  - As a matter of fact, the scientiﬁc community has been focusing on the design of new NLDR methods and the question of quality assessment remains mostly unanswered.
  - Furthermore, objective function s often fulﬁll some requirements, such ∗JAL is a Postdoctoral Researcher with the Belgian National Fund for Scientiﬁc Research.
- Failure modes:
  - Furthermore, objective function s often fulﬁll some requirements, such ∗JAL is a Postdoctoral Researcher with the Belgian National Fund for Scientiﬁc Research.

# Metrics Mentioned
- `trustworthiness`: referenced as part of projection-quality or reliability assessment.
- `continuity`: referenced as part of projection-quality or reliability assessment.
- `co-ranking`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- Obviously, this allows us to compare several runs with e.g. diﬀerent parameter values, but makes the comparison of diﬀerent methods unfair.
- On the other hand, nonlinear dimensionality reduction [1] (NLDR) emerged later and has deeply evolved for the past twenty ﬁve years, with neural approaches [2, 3, 4] and spectral techniques [5, 6, 7].
- As a matter of fact, the scientiﬁc community has been focusing on the design of new NLDR methods and the question of quality assessment remains mostly unanswered.
- Furthermore, objective function s often fulﬁll some requirements, such ∗JAL is a Postdoctoral Researcher with the Belgian National Fund for Scientiﬁc Research.
- Obviously, this allows us to compare several runs with e.g. diﬀerent parameter values, but makes the comparison of diﬀerent methods unfair.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-162-C1 | stance: support | summary: In the most general setting, dimensionality reduction transforms a set of N high-dimensional vectors, denoted Ξ =[ ξ i]1≤i≤N ,i n t oN low-dimensional vectors, denoted X =[ xi]1≤i≤N . | evidence_ids: PENDING-REF-162-E1, PENDING-REF-162-E2
- CLAIM-PENDING-REF-162-C2 | stance: support | summary: As most NLDR methods optimize a given objective function, a simplistic way to assess the quality is to look at the value of the objective function after convergence. | evidence_ids: PENDING-REF-162-E3, PENDING-REF-162-E4
- CLAIM-PENDING-REF-162-C3 | stance: support | summary: Obviously, this allows us to compare several runs with e.g. diﬀerent parameter values, but makes the comparison of diﬀerent methods unfair. | evidence_ids: PENDING-REF-162-E5, PENDING-REF-162-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-REF-162-E1 | page: 1, section: extracted, quote: "In the most general setting, dimensionality reduction transforms a set of N high-dimensional vectors, denoted Ξ =[ ξ i]1≤i≤N ,i n t oN low-dimensional vectors, denoted X =[ xi]1≤i≤N ."
- PENDING-REF-162-E2 | page: 1, section: extracted, quote: "1 Introduction Dimensionality reduction (DR) gathers techniques that provide a meaningful low-dimensional representation of a high-dimensional data set."
- PENDING-REF-162-E3 | page: 2, section: extracted, quote: "The rank of ξj with respect to ξi in the high-dimensional space is written as ρij = /{k : δik <δij or (δik = δij and k<j )}/."
- PENDING-REF-162-E4 | page: 1, section: extracted, quote: "Nonlinear dimensionality reduction aims at providing lowdimensional representions of high-dimensional data sets."
- PENDING-REF-162-E5 | page: 1, section: extracted, quote: "As most NLDR methods optimize a given objective function, a simplistic way to assess the quality is to look at the value of the objective function after convergence."
- PENDING-REF-162-E6 | page: 1, section: extracted, quote: "On the other hand, nonlinear dimensionality reduction [1] (NLDR) emerged later and has deeply evolved for the past twenty ﬁve years, with neural approaches [2, 3, 4] and spectral techniques [5, 6, 7]."
- PENDING-REF-162-E7 | page: 1, section: extracted, quote: "As a matter of fact, the scientiﬁc community has been focusing on the design of new NLDR methods and the question of quality assessment remains mostly unanswered."
- PENDING-REF-162-E8 | page: 1, section: extracted, quote: "Furthermore, objective function s often fulﬁll some requirements, such ∗JAL is a Postdoctoral Researcher with the Belgian National Fund for Scientiﬁc Research."
