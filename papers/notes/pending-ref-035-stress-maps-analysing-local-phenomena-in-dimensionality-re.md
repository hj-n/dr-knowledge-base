---
id: paper-2010-pending-ref-035
title: "Stress Maps: Analysing Local Phenomena in Dimensionality Reduction Based Visualisations"
authors: "Christin Seifert, Vedran Sabol, and Wolfgang Kienreich"
venue: "UNKNOWN"
year: 2010
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-035-2010-stress-maps-analysing-local-phenomena-in-dimensionality-reduction-based-visualisation.pdf
seed_note_id: "paper-2019-mdp-visual-analytics-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- The most elementary stress deﬁnition in metric MDS is the raw stress deﬁned by [Kru64] as the residual of sumsquares of the high-dimensional distances d i j and the geometric distances gi j SG = ∑ i, j (di j− gi j)2 (1) Later extensions to this formula include various weighting and normalizing parameters.
- Relatedness in the data through is conveyed by spatial proximity in the visualisation, i.e. items which are similar and therefore close in the high-dimensional vector space are placed close to each other in the low-dimensional visualisation space.
- Kienreich Know-Center Graz, Austria Abstract Challenges in Visual Analytics frequently involve massive repositories, which do not only contain a large number of information artefacts, but also a high number of relevant dimensions per artefact.
- A plethora of projection algorithms have been developed [GKWZ08] for projecting the document set into a lowdimensional (2D) visualisation space while preserving the high-dimensional relationships as good as possible.

# Method Summary
- Related Work In early 2010, Schreck et al. [SvLB10] described a methodology for the visual assessment of projection precision which, in large parts, antedates our stress map approach (This paper was submitted in early 2010.
- We report on an application of Stress Maps to a scalable text projection algorithm and describe two categories of problems related to localised stress phenomena which we have identiﬁed using the proposed method.
- The recursive, hierarchical projection algorithm starts with top level clusters and projects their centroids into a rectangular area using a force-directed placement (FDP) method.
- Because our approach is, in principle, applicable to arbitrary projection algorithms, we provide a brief overview on dimensionality reduction techniques.
- However, we manually inspected results for a sample data set and a projection algorithm with known properties using the stress map approach.
- We have investigated the results obtained by the proposed methodology using a projection algorithm and test data set with known properties.
- We illustrate this methodology by applying it to a scalable text projection algorithm.

# When To Use / Not Use
- Use when:
  - Information landscapes have been routinely used for visualisation of large document sets containing millions of documents [KBC ∗07], where the dimensionality of the highdimensional term space easily surpasses 10000.
  - We therefore deﬁned a stress function for the visualisation that allows detection of both types of errors by adjusting two parameters (which could even be exposed to users through interface elements).
- Avoid when:
  - In this paper, we propose the use of Stress Maps, a combination of heat maps and information landscapes, to support algorithm development and optimization based on local stress measures.
  - Application to hierarchically organised document collections has been proposed in [AKS ∗02], where spatial tessellations are used to reﬂect hierarchically organised document sets.
- Failure modes:
  - State-of-the-Art In this section, we ﬁrst discuss related work in information landscapes because we conducted our experiments in this application area of projection algorithms.

# Metrics Mentioned
- `stress`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- The LC-Meta criterion is not smooth and can not be subjected to optimization, but can be used to select among various parameter conﬁgurations.
- The most elementary stress deﬁnition in metric MDS is the raw stress deﬁned by [Kru64] as the residual of sumsquares of the high-dimensional distances d i j and the geometric distances gi j SG = ∑ i, j (di j− gi j)2 (1) Later extensions to this formula include various weighting and normalizing parameters.
- We report on an application of Stress Maps to a scalable text projection algorithm and describe two categories of problems related to localised stress phenomena which we have identiﬁed using the proposed method.
- We therefore deﬁned a stress function for the visualisation that allows detection of both types of errors by adjusting two parameters (which could even be exposed to users through interface elements).
- In this paper, we propose the use of Stress Maps, a combination of heat maps and information landscapes, to support algorithm development and optimization based on local stress measures.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-035-C1 | stance: support | summary: The most elementary stress deﬁnition in metric MDS is the raw stress deﬁned by [Kru64] as the residual of sumsquares of the high-dimensional distances d i j and the geometric distances gi j SG = ∑ i, j (di j− gi j)2 (1) Later extensions to this formula include various weighting and normalizing parameters. | evidence_ids: PENDING-REF-035-E1, PENDING-REF-035-E2
- CLAIM-PENDING-REF-035-C2 | stance: support | summary: Related Work In early 2010, Schreck et al. [SvLB10] described a methodology for the visual assessment of projection precision which, in large parts, antedates our stress map approach (This paper was submitted in early 2010. | evidence_ids: PENDING-REF-035-E3, PENDING-REF-035-E4
- CLAIM-PENDING-REF-035-C3 | stance: support | summary: The LC-Meta criterion is not smooth and can not be subjected to optimization, but can be used to select among various parameter conﬁgurations. | evidence_ids: PENDING-REF-035-E5, PENDING-REF-035-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance
- step: 6 | relevance: high | note: guides reliable interpretation of projected views

# Evidence
- PENDING-REF-035-E1 | page: 3, section: extracted, quote: "The most elementary stress deﬁnition in metric MDS is the raw stress deﬁned by [Kru64] as the residual of sumsquares of the high-dimensional distances d i j and the geometric distances gi j SG = ∑ i, j (di j− gi j)2 (1) Later extensions to this formula include various weighting and normalizing parameters."
- PENDING-REF-035-E2 | page: 2, section: extracted, quote: "Relatedness in the data through is conveyed by spatial proximity in the visualisation, i.e. items which are similar and therefore close in the high-dimensional vector space are placed close to each other in the low-dimensional visualisation space."
- PENDING-REF-035-E3 | page: 1, section: extracted, quote: "Kienreich Know-Center Graz, Austria Abstract Challenges in Visual Analytics frequently involve massive repositories, which do not only contain a large number of information artefacts, but also a high number of relevant dimensions per artefact."
- PENDING-REF-035-E4 | page: 1, section: extracted, quote: "A plethora of projection algorithms have been developed [GKWZ08] for projecting the document set into a lowdimensional (2D) visualisation space while preserving the high-dimensional relationships as good as possible."
- PENDING-REF-035-E5 | page: 3, section: extracted, quote: "Related Work In early 2010, Schreck et al. [SvLB10] described a methodology for the visual assessment of projection precision which, in large parts, antedates our stress map approach (This paper was submitted in early 2010."
- PENDING-REF-035-E6 | page: 1, section: extracted, quote: "We report on an application of Stress Maps to a scalable text projection algorithm and describe two categories of problems related to localised stress phenomena which we have identiﬁed using the proposed method."
- PENDING-REF-035-E7 | page: 4, section: extracted, quote: "The recursive, hierarchical projection algorithm starts with top level clusters and projects their centroids into a rectangular area using a force-directed placement (FDP) method."
- PENDING-REF-035-E8 | page: 2, section: extracted, quote: "Because our approach is, in principle, applicable to arbitrary projection algorithms, we provide a brief overview on dimensionality reduction techniques."
