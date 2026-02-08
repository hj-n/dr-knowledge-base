---
id: paper-2002-zadu-ref-17
title: "Stochastic Neighbor Embedding"
authors: "Geoffrey E. Hinton, Sam T. Roweis"
venue: "Advances in Neural Information Processing Systems (NIPS 15)"
year: 2002
tags: [dr, zadu-table1-reference, kl_div, stress]
source_pdf: papers/raw/zadu-table1-references/ref13_stochastic_neighbor_embedding.pdf
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- We describe a probabilistic approach to the task of placing objects, de- scribed by high-dimensional vectors or by pairwise dissimilarities, in a low-dimensional space in a way that preserves neighbor identities.
- A Gaussian is centered on each object in the high-dimensional space and the densities under this Gaussian (or the given dissimilarities) are used to deﬁne a probability distribution over all the potential neighbors of the object.

# Method Summary
- In this paper we deﬁne a new notion of embedding based on probable neighbors.
- A natural cost function is a sum of Kullback-Leibler divergences, one per object, which leads to a simple gradient for adjusting the positions of the low-dimensional im- ages.
- This is achieved by minimizing a cost function which is a sum of Kullback-Leibler divergences between the original (5 ) and induced (06 ) distributions over neighbors for each object: 7 98  8    *'+ , : 0  ;8 9<>= @?
- Adding random jitter that decreases with time ﬁnds much better local optima and is the method we used for the exam- ples in this paper, even though it is still quite slow.

# When To Use / Not Use
- Use when:
  - Use when selecting DR reliability checks in workflow Step 3.
  - Use with complementary local/cluster/global metrics rather than a single score.
- Avoid when:
  - Avoid using this source as the only decision signal without task constraints.
- Failure modes:
  - Overfitting conclusions to a single metric family or benchmark setup.

# Metrics Mentioned
- `kl_div`: distribution mismatch in neighbor probabilities
- `stress`: distance-fitting distortion objective/metric

# Implementation Notes
- Runtime/complexity signal: Adding random jitter that decreases with time ﬁnds much better local optima and is the method we used for the exam- ples in this paper, even though it is still quite slow.

# Claim Atoms (For Conflict Resolution)
- CLAIM-SOURCE-17-CORE | stance: support | summary: This source formulates neighbor preservation with a KL-divergence objective. | evidence_ids: ZR17-E1
- CLAIM-METRIC-KL_DIV-SOURCE-17 | stance: support | summary: This source uses or discusses `kl_div` for distribution mismatch in neighbor probabilities in dimensionality-reduction evaluation. | evidence_ids: ZR17-E2
- CLAIM-METRIC-STRESS-SOURCE-17 | stance: support | summary: This source uses or discusses `stress` for distance-fitting distortion objective/metric in dimensionality-reduction evaluation. | evidence_ids: ZR17-E2

# Workflow Relevance Map
- step: 3 | relevance: high | note: Informs task-aligned metric/technique selection and metric trust calibration.
- step: 6 | relevance: high | note: Provides rationale that can be translated for end users.

# Evidence
- ZR17-E1 | page: 1, section: extracted, quote: "A natural cost function is a sum of Kullback-Leibler divergences, one per object, which leads to a simple gradient for adjusting the positions of the low-dimensional im- ages."
- ZR17-E2 | page: 1, section: extracted, quote: "In this paper we deﬁne a new notion of embedding based on probable neighbors."
- ZR17-E3 | page: 2, section: extracted, quote: "This is achieved by minimizing a cost function which is a sum of Kullback-Leibler divergences between the original (5 ) and induced (06 ) distributions over neighbors for each object: 7 98  8    *'+ , : 0  ;8 9<>= @?"
- ZR17-E4 | page: 2, section: extracted, quote: "Adding random jitter that decreases with time ﬁnds much better local optima and is the method we used for the exam- ples in this paper, even though it is still quite slow."
- ZR17-E5 | page: 7, section: extracted, quote: "Com- putational physics has attacked exactly this same complexity when performing multibody gravitational or electrostatic simulations using, for example, the fast multipole method."
- ZR17-E6 | page: 8, section: extracted, quote: "This mismatch is very similar to “stress” functions used in nonmetric versions of MDS, and enables us to understand the large-variance limit of SNE as a particular variant of such procedures."
- ZR17-E7 | page: 2, section: extracted, quote: "Here, ... is the effective number of local neighbors or perplexity and is chosen by hand."
- ZR17-E8 | page: 4, section: extracted, quote: "The learning rate was 0.2."
- ZR17-E9 | page: 3, section: extracted, quote: "The variance of the Gaussian ... was set to achieve a perplexity of 15 in the distribution over high-dimensional neighbors."
