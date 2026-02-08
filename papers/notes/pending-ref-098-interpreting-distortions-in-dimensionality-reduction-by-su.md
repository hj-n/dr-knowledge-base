---
id: paper-2019-pending-ref-098
title: "Interpreting Distortions in Dimensionality Reduction by Superimposing Neighbourhood Graphs"
authors: "Benoît Colange, Laurent Vuillon, Sylvain Lespinats, and Denys Dutykh"
venue: "2019 IEEE Visualization Conference (VIS)"
year: 2019
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-098-2019-interpreting-distortions-in-dimensionality-reduction-by-superimposing-neighbourhood-g.pdf
seed_note_id: "paper-2025-jeon-reliable-va-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- The considered visualization must be enhanced with local evaluation, locating precisely the distortions measured through global indicators. *benoit.colange@cea.fr In the present article, we introduce a new local evaluation method called MING, for “Map Interpretation using Neighbourhood Graphs”.
- On these graphs (considered successively in the embedding and data space), edges corresponding to reliable or unreliable neighbours are then distinguished using different colours, colour range being chosen so as to offer a local representation of the selected global indicators.
- 4.3.2 T rustworthiness and continuity weights Since precision and recall weights are binary, slight rank distortions around the cut-off κ (e.g. tenth neighbour becoming the eleventh) are displayed the same way as severe distortions.
- These graphs allow to diagnose reliable and distortioninduced neighbourhood relations, while quantifying those distortions through a colour scale based on classical map evaluation criteria.

# Method Summary
- 4.4 Edge bundling In order to reduce the visual clutter occasioned by the method, edge bundling was experimented with a variant of the KDEEB algorithm [7], using the previously considered embedding of digits data for the sake of comparison.
- 5 C ONCLUSIONS In this paper, we proposed a new method for interpreting mappings while accounting for distortions by superimposing two colour-coded graphs.
- Those penalized relations are restricted for each point i to the set of κ neighbourhood relations existing at least in the embedding space{(i, j)| j∈ ni(κ)} for false neighbours indicator F, and to the set of neighbourhood relations existing at least in the data space {(i, j)| j∈ νi(κ)} for missed neighbours indicator M.
- The considered visualization must be enhanced with local evaluation, locating precisely the distortions measured through global indicators. *benoit.colange@cea.fr In the present article, we introduce a new local evaluation method called MING, for “Map Interpretation using Neighbourhood Graphs”.
- On these graphs (considered successively in the embedding and data space), edges corresponding to reliable or unreliable neighbours are then distinguished using different colours, colour range being chosen so as to offer a local representation of the selected global indicators.
- This approach adapts global rank-based indicators (e.g. precision and recall [22] or trustworthiness and continuity [21]), designed for assessing overall performances of dimensionality reduction, to the needs of local evaluation.
- They are generally based on the comparison of: • distances ∆ i j and Di j, used in stress functions of many dimensionality reduction methods [4, 14, 19] • ranks ρi j and ri j, used in several rank-based quality criteria [9].

# When To Use / Not Use
- Use when:
  - One key advantage of choosing these images datasets, is that we may use the actual images as markers for points on the map, allowing the reader to assess visually whether two items are similar or not in the data space (within the meaning of Euclidean distances).
  - They are generally based on the comparison of: • distances ∆ i j and Di j, used in stress functions of many dimensionality reduction methods [4, 14, 19] • ranks ρi j and ri j, used in several rank-based quality criteria [9].
- Avoid when:
  - We apply this approach to two pairs of widespread indicators: precision/recall and trustworthiness/continuity, chosen for their wide use in the community, which will allow an easy handling by users.
  - Several values may also be used successively during users interaction with the representation, in order to get information for different scales, and on the hierarchical organization of data.
- Failure modes:
  - Though such penalizations are commonly established, previous works tend to either aggregate them, losing the pairwise information, or to display them for only one reference point at a time.

# Metrics Mentioned
- `trustworthiness`: referenced as part of projection-quality or reliability assessment.
- `continuity`: referenced as part of projection-quality or reliability assessment.
- `stress`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- Such global indicators are currently used to compare several maps, which helps to choose the most appropriate mapping method and its hyperparameters.
- 4.2 Choice of κ In MING, as in CheckViz, the user remains free to set the parameter κ, depending on the number of neighbours they judge relevant.
- 5 C ONCLUSIONS In this paper, we proposed a new method for interpreting mappings while accounting for distortions by superimposing two colour-coded graphs.
- Those penalized relations are restricted for each point i to the set of κ neighbourhood relations existing at least in the embedding space{(i, j)| j∈ ni(κ)} for false neighbours indicator F, and to the set of neighbourhood relations existing at least in the data space {(i, j)| j∈ νi(κ)} for missed neighbours indicator M.
- The considered visualization must be enhanced with local evaluation, locating precisely the distortions measured through global indicators. *benoit.colange@cea.fr In the present article, we introduce a new local evaluation method called MING, for “Map Interpretation using Neighbourhood Graphs”.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-098-C1 | stance: support | summary: The considered visualization must be enhanced with local evaluation, locating precisely the distortions measured through global indicators. *benoit.colange@cea.fr In the present article, we introduce a new local evaluation method called MING, for “Map Interpretation using Neighbourhood Graphs”. | evidence_ids: PENDING-REF-098-E1, PENDING-REF-098-E2
- CLAIM-PENDING-REF-098-C2 | stance: support | summary: 4.4 Edge bundling In order to reduce the visual clutter occasioned by the method, edge bundling was experimented with a variant of the KDEEB algorithm [7], using the previously considered embedding of digits data for the sake of comparison. | evidence_ids: PENDING-REF-098-E3, PENDING-REF-098-E4
- CLAIM-PENDING-REF-098-C3 | stance: support | summary: Such global indicators are currently used to compare several maps, which helps to choose the most appropriate mapping method and its hyperparameters. | evidence_ids: PENDING-REF-098-E5, PENDING-REF-098-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-REF-098-E1 | page: 1, section: extracted, quote: "The considered visualization must be enhanced with local evaluation, locating precisely the distortions measured through global indicators. *benoit.colange@cea.fr In the present article, we introduce a new local evaluation method called MING, for “Map Interpretation using Neighbourhood Graphs”."
- PENDING-REF-098-E2 | page: 1, section: extracted, quote: "On these graphs (considered successively in the embedding and data space), edges corresponding to reliable or unreliable neighbours are then distinguished using different colours, colour range being chosen so as to offer a local representation of the selected global indicators."
- PENDING-REF-098-E3 | page: 4, section: extracted, quote: "4.3.2 T rustworthiness and continuity weights Since precision and recall weights are binary, slight rank distortions around the cut-off κ (e.g. tenth neighbour becoming the eleventh) are displayed the same way as severe distortions."
- PENDING-REF-098-E4 | page: 4, section: extracted, quote: "These graphs allow to diagnose reliable and distortioninduced neighbourhood relations, while quantifying those distortions through a colour scale based on classical map evaluation criteria."
- PENDING-REF-098-E5 | page: 4, section: extracted, quote: "4.4 Edge bundling In order to reduce the visual clutter occasioned by the method, edge bundling was experimented with a variant of the KDEEB algorithm [7], using the previously considered embedding of digits data for the sake of comparison."
- PENDING-REF-098-E6 | page: 4, section: extracted, quote: "5 C ONCLUSIONS In this paper, we proposed a new method for interpreting mappings while accounting for distortions by superimposing two colour-coded graphs."
- PENDING-REF-098-E7 | page: 2, section: extracted, quote: "Those penalized relations are restricted for each point i to the set of κ neighbourhood relations existing at least in the embedding space{(i, j)/ j∈ ni(κ)} for false neighbours indicator F, and to the set of neighbourhood relations existing at least in the data space {(i, j)/ j∈ νi(κ)} for missed neighbours indicator M."
- PENDING-REF-098-E8 | page: 1, section: extracted, quote: "This approach adapts global rank-based indicators (e.g. precision and recall [22] or trustworthiness and continuity [21]), designed for assessing overall performances of dimensionality reduction, to the needs of local evaluation."
