---
id: paper-2019-pending-ref-171
title: "SolarView: Low Distortion Radial Embedding with a Focus"
authors: "Thom Castermans, Kevin Verbeek, Bettina Speckmann, Michel A. Westenberg, Rob Koopman, Shenghui Wang, Hein van den Berg, and Arianna Betti"
venue: "IEEE Transactions on Visualization and Computer Graphics"
year: 2019
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-171-2019-solarview-low-distortion-radial-embedding-with-a-focus.pdf
seed_note_id: "paper-2025-jeon-reliable-va-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- They use dimension reduction to map the high-dimensional semantic space to two dimensions, and provide per-word distortion metrics and a view to display words and their direct neighbors in the high-dimensional space to convey the inherent uncertainty introduced by dimension reduction.
- Neighbor entities who have a similar distance to the focus entity pose a challenge for each embedding algorithm; they are restricted to lie essentially on the same circle around the focus entity and their interactions have a strong inﬂuence on the distortion of the embedding.
- 3 P ROBLEM ANALYSIS AND SCOPE SolarView addresses the following general problem: We are given a number of entities in a high-dimensional metric space, one of which is marked as the focus entity.
- 7 C ONCLUSION We have proposed a novel low distortion radial embedding for visualization of points in high-dimensional space, which we have demonstrated using bibliographic entity similarities.

# Method Summary
- We propose to approach this by constructing a radial embedding of the entities.
- Neighbor entities who have a similar distance to the focus entity pose a challenge for each embedding algorithm; they are restricted to lie essentially on the same circle around the focus entity and their interactions have a strong inﬂuence on the distortion of the embedding.
- Westenberg, Rob Koopman, Shenghui Wang, Hein van den Berg, and Arianna Betti Abstract—We propose a novel type of low distortion radial embedding which focuses on one speciﬁc entity and its closest neighbors.
- Optimize entity placement (see Section 4.2) 4.1 Metric embeddings onto a circle An important part of our algorithm is a metric embedding with small average distortion of a set of entities onto a circle.
- However, as mentioned in [22], this algorithm cannot easily be extended to embeddings onto a circle, and it is clearly not practical for IEEE TRANSACTIONS ON VISUALIZATION AND COMPUTER GRAPHICS, VOL.
- If the goal is to put the entities on rings, as is the case in our application, then our embedding algorithm TSP appears to be the best choice, resulting in the least distortion in general.
- 6 E XPERIMENTAL EVALUATION In this section we experimentally evaluate our embedding algorithm and compare it to state-of-the-art dimensionality reduction and embedding techniques.

# When To Use / Not Use
- Use when:
  - Because it is generally impossible to avoid distortion, the distances in the output will most likely render a distorted view of the actual distances in the input.
  - They also use the TSP , but use dummy rows to, amongst others, avoid the problem of the ﬁrst and last row having only one neighbor.
- Avoid when:
  - They can do so as SolarView encodes entities as points in the plane, allowing them to filter all entities to only the close neighbors of the focus, and select a neighbor to become the new focus, navigating to an updated view. (3) Users can browse entities with a similar distance to the focus and then compare distances between these entities independent of the focus entity.
  - In the near future we are planning to use the complete SolarView system in a large scale user study with eHumanities scholars to determine (i) if the visual encoding is clear and intuitive enough for a more general audience, and (ii) if SolarView does in fact provide an easy overview of (potentially unfamiliar) research ﬁelds.
- Failure modes:
  - They use dimension reduction to map the high-dimensional semantic space to two dimensions, and provide per-word distortion metrics and a view to display words and their direct neighbors in the high-dimensional space to convey the inherent uncertainty introduced by dimension reduction.

# Metrics Mentioned
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- The limit on the number of loop iterations can be tuned so that the optimization process can be pruned in interactive settings.
- We should note that, when used as initialization for FDL, we do not perform the rotational alignment or optimize the entity placement (that is, we skip line 4 and 5 in the Algorithm RADIAL EMBED in Section 4).
- Unfortunately similar optimization techniques do not seem to perform efﬁciently enough to compute optimal metric embeddings on a circle, not even for small inputs of roughly 40 entities.
- We can hence expect that minimizing the average distortion is also NP-hard, since minimization problems involving averages tend to be harder than optimization problems involving maxima.
- The client side component provides a simple search bar that can be used to search for entities, with additional controls for changing certain search parameters.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-171-C1 | stance: support | summary: They use dimension reduction to map the high-dimensional semantic space to two dimensions, and provide per-word distortion metrics and a view to display words and their direct neighbors in the high-dimensional space to convey the inherent uncertainty introduced by dimension reduction. | evidence_ids: PENDING-REF-171-E1, PENDING-REF-171-E2
- CLAIM-PENDING-REF-171-C2 | stance: support | summary: We propose to approach this by constructing a radial embedding of the entities. | evidence_ids: PENDING-REF-171-E3, PENDING-REF-171-E4
- CLAIM-PENDING-REF-171-C3 | stance: support | summary: The limit on the number of loop iterations can be tuned so that the optimization process can be pruned in interactive settings. | evidence_ids: PENDING-REF-171-E5, PENDING-REF-171-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 4 | relevance: high | note: contains initialization sensitivity or control-policy evidence

# Evidence
- PENDING-REF-171-E1 | page: 3, section: extracted, quote: "They use dimension reduction to map the high-dimensional semantic space to two dimensions, and provide per-word distortion metrics and a view to display words and their direct neighbors in the high-dimensional space to convey the inherent uncertainty introduced by dimension reduction."
- PENDING-REF-171-E2 | page: 2, section: extracted, quote: "Neighbor entities who have a similar distance to the focus entity pose a challenge for each embedding algorithm; they are restricted to lie essentially on the same circle around the focus entity and their interactions have a strong inﬂuence on the distortion of the embedding."
- PENDING-REF-171-E3 | page: 4, section: extracted, quote: "3 P ROBLEM ANALYSIS AND SCOPE SolarView addresses the following general problem: We are given a number of entities in a high-dimensional metric space, one of which is marked as the focus entity."
- PENDING-REF-171-E4 | page: 13, section: extracted, quote: "7 C ONCLUSION We have proposed a novel low distortion radial embedding for visualization of points in high-dimensional space, which we have demonstrated using bibliographic entity similarities."
- PENDING-REF-171-E5 | page: 4, section: extracted, quote: "We propose to approach this by constructing a radial embedding of the entities."
- PENDING-REF-171-E6 | page: 2, section: extracted, quote: "Westenberg, Rob Koopman, Shenghui Wang, Hein van den Berg, and Arianna Betti Abstract—We propose a novel type of low distortion radial embedding which focuses on one speciﬁc entity and its closest neighbors."
- PENDING-REF-171-E7 | page: 5, section: extracted, quote: "Optimize entity placement (see Section 4.2) 4.1 Metric embeddings onto a circle An important part of our algorithm is a metric embedding with small average distortion of a set of entities onto a circle."
- PENDING-REF-171-E8 | page: 3, section: extracted, quote: "However, as mentioned in [22], this algorithm cannot easily be extended to embeddings onto a circle, and it is clearly not practical for IEEE TRANSACTIONS ON VISUALIZATION AND COMPUTER GRAPHICS, VOL."
