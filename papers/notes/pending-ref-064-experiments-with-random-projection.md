---
id: paper-2000-pending-ref-064
title: "Experiments with random projection"
authors: "S. Dasgupta"
venue: "UNKNOWN"
year: 2000
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-064-2000-experiments-with-random-projection.pdf
seed_note_id: "paper-2017-random-projection-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- We suggest a very simple scheme. • Project the data into a randomly chosen d-dimensional subspace. • Run EM to convergence on the low-dimensional data. • Take the fractional labels from EM's final soft­ clustering of the low-dimensional data, and apply these same labels to the original high-dimensional data.
- This effect is of major impor­ tance because raw high-dimensional data can be expected to form very eccentric clusters, owing, for instance, to dif­ ferent units of measurement for different attributes.
- In particular, if the high-dimensional eccentricity E is at most n 1 12C;1/2(log � + dlogd)- 112 then with probability at least 1 - o, the projected Gaussians will have eccentricity at most two.
- The resulting covariance ma­ trices of the clusters are so ill-conditioned that it is difficult to reliably perform basic linear algebra operations, like de­ terminant or inverse, on them.

# Method Summary
- 4 Random projection and EM 4.1 A simple algorithm EM is at present the method of choice for learning mixtures of Gaussians and it is therefore important to find a way of integrating it with random projection.
- These two benefits have made random projection the key ingredient in the first polynomial-time, provably correct (in *Work done while at University of California, Berkeley. a PAC-like sense) algorithm for learning mixtures of Gaus­ sians (Dasgupta, 1999).
- Dif­ ferent notions of "interesting" lead to different projection algorithms.
- UNCERTAINTY IN ARTIFICIAL INTELLIGENCE PROCEEDINGS 2000 143 Experiments with Random Projection Sanjoy Dasgupta* AT&T Labs - Research Abstract Recent theoretical work has identified random projection as a promising dimensionality reduc­ tion technique for learning mixtures of Gaus­ sians.
- 3 Dimensionality reduction Dimensionality reduction has been the subject of keen study for the past few decades, and instead of trying to summarize this work we will focus upon two popular contemporary techniques: principal component analysis (PCA) and random projection.
- There is a universal constant C2 such that for any o, t E (0 , 1), if the original dimension satisfies n > c2 ° �(log� + dlog � ), then with probability> 1-0 over the choice of random projection, the eccentricity of the projected covariance matrix will be at most 1 + t.
- It is quite easy to symmetrically arrange a group of k spherical Gaussians in ]Rk/2 so that a PCA projection to any smaller dimension will collapse some of the Gaussians together, and thereby decisively derail any hope of learning.

# When To Use / Not Use
- Use when:
  - 4.3 Experiments with OCR To reassure ourselves that random projection is robust to the quirks of real data, we have used it as part of a simple classifier for handwritten digits.
  - This effect is of major impor­ tance because raw high-dimensional data can be expected to form very eccentric clusters, owing, for instance, to dif­ ferent units of measurement for different attributes.
- Avoid when:
  - As an example of when this is not the case, consider two spherical Gaussians N(f11,ln ) and N(f12, In) in some very high dimension n, and suppose that only one of the attributes is at all useful.
  - As explained earlier, PCA can­ not in general be used to reduce the dimension of a mix­ ture of k Gaussians to below O(k), whereas random pro­ jection can reduce the dimension to just 0 (log k).
- Failure modes:
  - For example, they are problematic for the EM algorithm because special pains must be taken to ensure that interme­ diate covariance matrices do not become singular, or close to singular.

# Metrics Mentioned
- No explicit named metric was extracted from this source; combine this source with complementary DR quality checks in workflow Step 3.

# Implementation Notes
- The number of low-dimensional iter­ ations needed by our adaptation of EM is slightly more than that required by regular EM; however, each of these low­ dimensional iterations is much quicker, taking time propor­ tional to d3 instead of n3.
- In these experi­ ments, regular EM suffered a curse of dimensionality: as n was increased, the success probability dropped sharply, and the number of iterations required for convergence increased gradually.
- Part of PCA's appeal lies in the fact that it cor­ responds to an optimization problem which can be solved exactly and efficiently, via eigenvalue computations.
- The correspond­ ing covariance matrices were forced to be spherical at the outset, �}o) = af0)2 I, with variance parameter (o)2 _ 1 .
- It is common to not allow each cluster its own full covari­ ance matrix, because of the large number of parameters in­ volved.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-064-C1 | stance: support | summary: We suggest a very simple scheme. • Project the data into a randomly chosen d-dimensional subspace. • Run EM to convergence on the low-dimensional data. • Take the fractional labels from EM's final soft­ clustering of the low-dimensional data, and apply these same labels to the original high-dimensional data. | evidence_ids: PENDING-REF-064-E1, PENDING-REF-064-E2
- CLAIM-PENDING-REF-064-C2 | stance: support | summary: 4 Random projection and EM 4.1 A simple algorithm EM is at present the method of choice for learning mixtures of Gaussians and it is therefore important to find a way of integrating it with random projection. | evidence_ids: PENDING-REF-064-E3, PENDING-REF-064-E4
- CLAIM-PENDING-REF-064-C3 | stance: support | summary: The number of low-dimensional iter­ ations needed by our adaptation of EM is slightly more than that required by regular EM; however, each of these low­ dimensional iterations is much quicker, taking time propor­ tional to d3 instead of n3. | evidence_ids: PENDING-REF-064-E5, PENDING-REF-064-E6

# Workflow Relevance Map
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 4 | relevance: high | note: contains initialization sensitivity or control-policy evidence
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-REF-064-E1 | page: 6, section: extracted, quote: "We suggest a very simple scheme. • Project the data into a randomly chosen d-dimensional subspace. • Run EM to convergence on the low-dimensional data. • Take the fractional labels from EM's final soft­ clustering of the low-dimensional data, and apply these same labels to the original high-dimensional data."
- PENDING-REF-064-E2 | page: 1, section: extracted, quote: "This effect is of major impor­ tance because raw high-dimensional data can be expected to form very eccentric clusters, owing, for instance, to dif­ ferent units of measurement for different attributes."
- PENDING-REF-064-E3 | page: 4, section: extracted, quote: "In particular, if the high-dimensional eccentricity E is at most n 1 12C;1/2(log � + dlogd)- 112 then with probability at least 1 - o, the projected Gaussians will have eccentricity at most two."
- PENDING-REF-064-E4 | page: 8, section: extracted, quote: "The resulting covariance ma­ trices of the clusters are so ill-conditioned that it is difficult to reliably perform basic linear algebra operations, like de­ terminant or inverse, on them."
- PENDING-REF-064-E5 | page: 6, section: extracted, quote: "4 Random projection and EM 4.1 A simple algorithm EM is at present the method of choice for learning mixtures of Gaussians and it is therefore important to find a way of integrating it with random projection."
- PENDING-REF-064-E6 | page: 1, section: extracted, quote: "These two benefits have made random projection the key ingredient in the first polynomial-time, provably correct (in *Work done while at University of California, Berkeley. a PAC-like sense) algorithm for learning mixtures of Gaus­ sians (Dasgupta, 1999)."
- PENDING-REF-064-E7 | page: 3, section: extracted, quote: "Dif­ ferent notions of 'interesting' lead to different projection algorithms."
- PENDING-REF-064-E8 | page: 1, section: extracted, quote: "UNCERTAINTY IN ARTIFICIAL INTELLIGENCE PROCEEDINGS 2000 143 Experiments with Random Projection Sanjoy Dasgupta* AT&T Labs - Research Abstract Recent theoretical work has identified random projection as a promising dimensionality reduc­ tion technique for learning mixtures of Gaus­ sians."
