---
id: paper-2006-pending-ref-019
title: "Local multidimensional scaling"
authors: "Jarkko Venna and Samuel Kaski"
venue: "Journal of the American Statistical Association"
year: 2006
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-019-2006-local-multidimensional-scaling.pdf
seed_note_id: "paper-2015-gisbrecht-nonlinear-dr-visualization"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- While LMDS’ tuning parameter provides ﬂexibility, it also creates a selection problem: how does one know in practice which among several co nﬁgurations is 4 most faithful to the underlying high-dimensional structur e?
- LMDS’ solution to the localization problem has drawbacks, too, in that it may exhibit systematic distortions.
- We expand the “repulsion term” (3), discarding functions of th e dissimilarities that do not aﬀect the minimization problem: LMDSD N (x1, ..., xN ) ∼ ∑ (i,j)∈N (Di,j − ∥ xi − xj∥)2 (4) − 2wD∞ ∑ (i,j) /∈N ∥xi − xj∥ (5) +w ∑ (i,j) /∈N ∥xi − xj∥2 (6) As D∞ → ∞ , we let w → 0 at least on the order of 1 /D∞ in order to prevent the term (5) from blowing up.
- We have proposed one such family of measures, called “Local C ontinuity” or “LC” meta-criteria and deﬁned as the average size of the over lap of K-nearest neighborhoods in the high-dimensional data and the low-dim ensional conﬁguration (Chen 2006).

# Method Summary
- A hybrid of classical and distance scaling are the semi-deﬁnite programming (SDP) approaches by Lu, Keles, Wright and Wahba (2005) and Weinberger, Sha, Zhu and Saul (2006) who ﬁt full-rank Gram ma trices K to local proximities via Di,j 2 ≈ Ki,i + Kj,j − 2Ki,j and extract hierarchical embeddings by decomposing K.
- 6 DISCUSSION AND CONCLUSION This article makes three contributions: (1) It introduces a novel version of multidimensional scaling, called LMDS, that lends itself t o locally faithful nonlinear dimension reduction and as such competes successful ly with recent proposals such as “local linear embedding” (LLE, Roweis and Sau l 2000) and “isometric feature mapping” (Isomap, Tenenbaum et al.
- The idea is to c ompare for a given case 1) the K ′-NN with regard to Di,j in data space, and 2) the K ′-NN with regard to ∥xi − xj∥ in conﬁguration space. [We use K ′in distinction from the K used in the stress function LMDS K .] A high degree of overlap between the two neighbor sets yields a measure of local faithfulness of the embedding of the given case.
- With practical experience in mind, we introduce an alternat ive to manifold learning and its assumption that the data falls near a “warpe d sheet.” We propose instead that the data be modeled by a distribution in high dimensions that describes the data, warts and all, with variation cause d by digitization, rounding, uneven sampling density, and so on.
- This data example also makes it clear that no single dimension reducti on may be suﬃcient to show all that is of interest: very localized methods (K = 4) reveal 13 the underlying video sequence and transitions between clus ters, whereas global methods (PCA, MDS) show the extent of the major interpretabl e clusters and dimensions more realistically.
- 4 A POPULATION FRAMEWORK Nonlinear dimension reduction can be approached with stati stical modeling if it is thought of as “manifold learning.” Zhang and Zha (2005) , for example, examine “tangent space alignment” with an theoretical erro r analysis whereby an assumed target manifold is reconstructed from noisy poin t observations.
- We show how such measures can be employed as part of data analy tic methodology 1) for choosing tuning parameters such as strength of t he repulsive force and neighborhood size, and 2) as the basis of diagnostic plot s that show how faithfully each point is embedded in a conﬁguration.

# When To Use / Not Use
- Use when:
  - By avoiding “prejudices” implied by assumed models, the data are allowe d to show whatever they have to show, be it manifolds, patchworks of manifo lds of diﬀerent dimensions, clusters, sculpted shapes with protrusions or holes, general uneven density patterns, and so on.
  - An immediate beneﬁt of the distribution view is to recognize Isomap as non-robust due to its use of geodesic distances.
- Avoid when:
  - The idea is to c ompare for a given case 1) the K ′-NN with regard to Di,j in data space, and 2) the K ′-NN with regard to ∥xi − xj∥ in conﬁguration space. [We use K ′in distinction from the K used in the stress function LMDS K .] A high degree of overlap between the two neighbor sets yields a measure of local faithfulness of the embedding of the given case.
  - With practical experience in mind, we introduce an alternat ive to manifold learning and its assumption that the data falls near a “warpe d sheet.” We propose instead that the data be modeled by a distribution in high dimensions that describes the data, warts and all, with variation cause d by digitization, rounding, uneven sampling density, and so on.
- Failure modes:
  - For {xi} we use “conﬁguration” from proximity analysis, and also “embe dding” and “graph layout.” For Di,j we use “dissimilarity” from proximity analysis, and also “target distance,” meaning distances between high-dimens ional feature vectors in dimension reduction and shortest-path-length distance s in graph drawing.

# Metrics Mentioned
- `continuity`: referenced as part of projection-quality or reliability assessment.
- `stress`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- This can be corrected by 9 reparametrizing t with a factor |N |/|NC |)): t = |N | |NC |· medianN (Di,j) · τ , where τ is unit free. — A good strategy for optimization is to start wi th a large value such as τ = 1 to obtain a stable conﬁguration, and lower τ successively as low as 0 .01, using previous conﬁgurations as initializations for sm aller values of τ .
- We let therefore D∞ → ∞ subject to w = t/(2D∞ ), where t is a ﬁxed constant, and arrive at the ﬁnal deﬁnition of localized Stress: LMDSD N (x1, ..., xN ) = ∑ (i,j)∈N (Di,j − ||xi − xj||)2 − t ∑ (i,j) /∈N ||xi − xj|| (7) We call the ﬁrst term “local stress” and the second term “repu lsion.” A beneﬁt of passing to the limit is the replacement of two parameters, w and D∞ , with a single parameter t.
- We show how such measures can be employed as part of data analy tic methodology 1) for choosing tuning parameters such as strength of t he repulsive force and neighborhood size, and 2) as the basis of diagnostic plot s that show how faithfully each point is embedded in a conﬁguration.
- 3 CRITERIA FOR PARAMETER SELECTION For automatic selection of tuning parameters and compariso n of methods we need measures of faithfulness of conﬁgurations separate fr om the stress functions used for optimizing conﬁgurations.
- This problem can be corrected: • Invariance under change of units: Di,j and t have the same units, hence the units of t can be eliminated, for example, by t = median N (Di,j) t′, where the new parameter t′ is unit free.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-019-C1 | stance: support | summary: While LMDS’ tuning parameter provides ﬂexibility, it also creates a selection problem: how does one know in practice which among several co nﬁgurations is 4 most faithful to the underlying high-dimensional structur e? | evidence_ids: PENDING-REF-019-E1, PENDING-REF-019-E2
- CLAIM-PENDING-REF-019-C2 | stance: support | summary: A hybrid of classical and distance scaling are the semi-deﬁnite programming (SDP) approaches by Lu, Keles, Wright and Wahba (2005) and Weinberger, Sha, Zhu and Saul (2006) who ﬁt full-rank Gram ma trices K to local proximities via Di,j 2 ≈ Ki,i + Kj,j − 2Ki,j and extract hierarchical embeddings by decomposing K. | evidence_ids: PENDING-REF-019-E3, PENDING-REF-019-E4
- CLAIM-PENDING-REF-019-C3 | stance: support | summary: This can be corrected by 9 reparametrizing t with a factor /N ///NC /)): t = /N / /NC /· medianN (Di,j) · τ , where τ is unit free. — A good strategy for optimization is to start wi th a large value such as τ = 1 to obtain a stable conﬁguration, and lower τ successively as low as 0 .01, using previous conﬁgurations as initializations for sm aller values of τ . | evidence_ids: PENDING-REF-019-E5, PENDING-REF-019-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 4 | relevance: high | note: contains initialization sensitivity or control-policy evidence

# Evidence
- PENDING-REF-019-E1 | page: 4, section: extracted, quote: "While LMDS’ tuning parameter provides ﬂexibility, it also creates a selection problem: how does one know in practice which among several co nﬁgurations is 4 most faithful to the underlying high-dimensional structur e?"
- PENDING-REF-019-E2 | page: 4, section: extracted, quote: "LMDS’ solution to the localization problem has drawbacks, too, in that it may exhibit systematic distortions."
- PENDING-REF-019-E3 | page: 8, section: extracted, quote: "We expand the “repulsion term” (3), discarding functions of th e dissimilarities that do not aﬀect the minimization problem: LMDSD N (x1, ..., xN ) ∼ ∑ (i,j)∈N (Di,j − ∥ xi − xj∥)2 (4) − 2wD∞ ∑ (i,j) /∈N ∥xi − xj∥ (5) +w ∑ (i,j) /∈N ∥xi − xj∥2 (6) As D∞ → ∞ , we let w → 0 at least on the order of 1 /D∞ in order to prevent the term (5) from blowing up."
- PENDING-REF-019-E4 | page: 5, section: extracted, quote: "We have proposed one such family of measures, called “Local C ontinuity” or “LC” meta-criteria and deﬁned as the average size of the over lap of K-nearest neighborhoods in the high-dimensional data and the low-dim ensional conﬁguration (Chen 2006)."
- PENDING-REF-019-E5 | page: 7, section: extracted, quote: "A hybrid of classical and distance scaling are the semi-deﬁnite programming (SDP) approaches by Lu, Keles, Wright and Wahba (2005) and Weinberger, Sha, Zhu and Saul (2006) who ﬁt full-rank Gram ma trices K to local proximities via Di,j 2 ≈ Ki,i + Kj,j − 2Ki,j and extract hierarchical embeddings by decomposing K."
- PENDING-REF-019-E6 | page: 17, section: extracted, quote: "6 DISCUSSION AND CONCLUSION This article makes three contributions: (1) It introduces a novel version of multidimensional scaling, called LMDS, that lends itself t o locally faithful nonlinear dimension reduction and as such competes successful ly with recent proposals such as “local linear embedding” (LLE, Roweis and Sau l 2000) and “isometric feature mapping” (Isomap, Tenenbaum et al."
- PENDING-REF-019-E7 | page: 10, section: extracted, quote: "The idea is to c ompare for a given case 1) the K ′-NN with regard to Di,j in data space, and 2) the K ′-NN with regard to ∥xi − xj∥ in conﬁguration space. [We use K ′in distinction from the K used in the stress function LMDS K .] A high degree of overlap between the two neighbor sets yields a measure of local faithfulness of the embedding of the given case."
- PENDING-REF-019-E8 | page: 13, section: extracted, quote: "With practical experience in mind, we introduce an alternat ive to manifold learning and its assumption that the data falls near a “warpe d sheet.” We propose instead that the data be modeled by a distribution in high dimensions that describes the data, warts and all, with variation cause d by digitization, rounding, uneven sampling density, and so on."
