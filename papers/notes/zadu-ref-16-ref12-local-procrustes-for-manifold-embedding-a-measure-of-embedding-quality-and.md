---
id: paper-2009-zadu-ref-16
title: "Mach Learn (2009) 77: 1–25"
authors: "UNKNOWN"
venue: "UNKNOWN"
year: 2009
tags: [dr, zadu-table1-reference, proc, tnc]
source_pdf: papers/raw/zadu-table1-references/ref12_local_procrustes_for_manifold_embedding_a_measure_of_embedding_quality_and_embedding_algor.pdf
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- We present the Procrustes measure, a novel measure based on Procrustes rotation that enables quantitative comparison of the output of manifold-based embedding algorithms such as LLE (Roweis and Saul, Science 290(5500), 2323–2326, 2000) and Isomap (Tenen- baum et al., Science 290(5500), 2319–2323, 2000).
- The measure also serves as a natural tool when choosing dimension-reduction parameters.

# Method Summary
- Mach Learn (2009) 77: 1–25 DOI 10.1007/s10994-009-5107-9 Local procrustes for manifold embedding: a measure of embedding quality and embedding algorithms Yair Goldberg· Ya’acov Ritov Received: 27 December 2007 / Revised: 5 October 2008 / Accepted: 30 January 2009 / Published online: 7 April 2009 Springer Science+Business Media, LLC 2009 A
- Keywords Dimension reducing · Manifold learning · Procrustes analysis · Local PCA · Simulated annealing 1 Introduction Technological advances constantly improve our ability to collect and store large sets of data.
- The function we present, based on the Procrustes analysis, compares each neighborhood in the high- dimensional space and its corresponding low-dimensional embedding.
- The ﬁrst measure tests the trustwor- thiness of the embedding, where trustworthiness errors are deﬁned as distant input points that entered the same output neighborhood.

# When To Use / Not Use
- Use when:
  - Use when selecting DR reliability checks in workflow Step 3.
  - Use with complementary local/cluster/global metrics rather than a single score.
- Avoid when:
  - Avoid using this source as the only decision signal without task constraints.
- Failure modes:
  - Overfitting conclusions to a single metric family or benchmark setup.

# Metrics Mentioned
- `proc`: local shape agreement via Procrustes
- `tnc`: local neighborhood trustworthiness/continuity balance

# Implementation Notes
- Keep preprocessing and seed policy fixed before comparing reliability scores across methods.
- Use this source with at least one complementary note before final recommendation text.

# Claim Atoms (For Conflict Resolution)
- CLAIM-SOURCE-16-CORE | stance: support | summary: This source introduces local Procrustes-style neighborhood shape agreement for embedding quality. | evidence_ids: ZR16-E1
- CLAIM-METRIC-PROC-SOURCE-16 | stance: support | summary: This source uses or discusses `proc` for local shape agreement via Procrustes in dimensionality-reduction evaluation. | evidence_ids: ZR16-E2
- CLAIM-METRIC-TNC-SOURCE-16 | stance: support | summary: This source uses or discusses `tnc` for local neighborhood trustworthiness/continuity balance in dimensionality-reduction evaluation. | evidence_ids: ZR16-E2

# Workflow Relevance Map
- step: 3 | relevance: high | note: Informs task-aligned metric/technique selection and metric trust calibration.
- step: 6 | relevance: high | note: Provides rationale that can be translated for end users.

# Evidence
- ZR16-E1 | page: 1, section: extracted, quote: "Mach Learn (2009) 77: 1–25 DOI 10.1007/s10994-009-5107-9 Local procrustes for manifold embedding: a measure of embedding quality and embedding algorithms Yair Goldberg· Ya’acov Ritov Received: 27 December 2007 / Revised: 5 October 2008 / Accepted: 30 January 2009 / Published online: 7 April 2009 Springer Science+Business Media, LLC 2009 A"
- ZR16-E2 | page: 1, section: extracted, quote: "Keywords Dimension reducing · Manifold learning · Procrustes analysis · Local PCA · Simulated annealing 1 Introduction Technological advances constantly improve our ability to collect and store large sets of data."
- ZR16-E3 | page: 2, section: extracted, quote: "The function we present, based on the Procrustes analysis, compares each neighborhood in the high- dimensional space and its corresponding low-dimensional embedding."
- ZR16-E4 | page: 2, section: extracted, quote: "The ﬁrst measure tests the trustwor- thiness of the embedding, where trustworthiness errors are deﬁned as distant input points that entered the same output neighborhood."
- ZR16-E5 | page: 2, section: extracted, quote: "The second measure tests the continuity of the embedding, where continuity errors are deﬁned as data points that are in the same input neighborhood but not in the same output neighborhood."
- ZR16-E6 | page: 2, section: extracted, quote: "A closely related measure was sug- gested by Chen ( 2006), called the local continuity criterion."
- ZR16-E7 | page: 2, section: extracted, quote: "All of these measures, unlike the Procrustes mea- sure we suggest, do not take into account the structure of the neighborhoods, either in the high-dimensional input space or in the low-dimensional embedding space."
- ZR16-E8 | page: 4, section: extracted, quote: "A neighborhood on the manifold and its embedding can be compared using the Procrustes statistic."
