---
id: paper-2021-zadu-ref-18
title: "Measuring and Explaining the Inter-Cluster Reliability of Multidimensional Projections"
authors: "Hyeon Jeon, Hyung-Kwon Ko, Jaemin Jo, Youngtaek Kim, Jinwook Seo"
venue: "IEEE Transactions on Visualization and Computer Graphics"
year: 2021
tags: [dr, zadu-table1-reference, ivm, lcmc, mrre, nd, pr, snc, stress, tnc]
source_pdf: papers/raw/zadu-table1-references/ref18_measuring_and_explaining_the_inter_cluster_reliability_of_multidimensional_projections.pdf
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- — We propose Steadiness and Cohesiveness, two novel metrics to measure the inter-cluster reliability of multidimensional projection (MDP), speciﬁcally how well the inter-cluster structures are preserved between the original high-dimensional space and the low-dimensional projection space.
- Measuring inter-cluster reliability is crucial as it directly affects how well inter-cluster tasks (e.g., identifying cluster relationships in the original space from a projected view) can be conducted; however, despite the importance of inter-cluster tasks, we found that previous metrics, such as Trustworthiness and Continuity, fail to measure inter-cluster reliability.

# Method Summary
- The ﬁnal version of this record is available at: xx.xxxx/TVCG.201x.xxxxxxx/ Measuring and Explaining the Inter-Cluster Reliability of Multidimensional Projections Hyeon Jeon, Hyung-Kwon Ko, Jaemin Jo, Y oungtaek Kim, and Jinwook Seo Abstract— We propose Steadiness and Cohesiveness, two novel metrics to measure the inter-cluster reliabilit
- In this paper, we propose Steadiness and Cohesiveness, two metrics that quantitatively evaluate inter-cluster reliability.
- We ﬁrst formulated three design considerations of Steadiness and Cohesiveness so that the metrics can adequately evaluate inter-cluster reliability by quantifying how well inter-cluster tasks can be performed accurately in MDPs (i.e., measure the potential accuracy of the inter-cluster tasks).
- To make our metrics fulﬁll the considerations, we deﬁned new inter-cluster distortion types—False Groups and Missing Groups—and designed Steadiness and Cohesiveness to measure each, respectively.

# When To Use / Not Use
- Use when:
  - Use when selecting DR reliability checks in workflow Step 3.
  - Use with complementary local/cluster/global metrics rather than a single score.
- Avoid when:
  - Avoid using this source as the only decision signal without task constraints.
- Failure modes:
  - Overconfident conclusions when class labels are not well-separated in original space.

# Metrics Mentioned
- `ivm`: internal validation view of cluster structure (label-separation-sensitive)
- `lcmc`: local neighborhood overlap quality
- `mrre`: rank-error behavior across neighborhood sizes
- `nd`: neighbor-shape/neighbor-change dissimilarity
- `pr`: linear agreement of pairwise relationships
- `snc`: inter-cluster reliability via steadiness/cohesiveness
- `stress`: distance-fitting distortion objective/metric
- `tnc`: local neighborhood trustworthiness/continuity balance

# Implementation Notes
- If labels are weakly separated in original space, down-weight label-separation-sensitive metrics in final justification.

# Claim Atoms (For Conflict Resolution)
- CLAIM-SOURCE-18-CORE | stance: support | summary: This source introduces inter-cluster reliability metrics (steadiness/cohesiveness) for projection analysis. | evidence_ids: ZR18-E1
- CLAIM-METRIC-IVM-SOURCE-18 | stance: support | summary: This source uses or discusses `ivm` for internal validation view of cluster structure in dimensionality-reduction evaluation. | evidence_ids: ZR18-E2
- CLAIM-METRIC-LCMC-SOURCE-18 | stance: support | summary: This source uses or discusses `lcmc` for local neighborhood overlap quality in dimensionality-reduction evaluation. | evidence_ids: ZR18-E2
- CLAIM-METRIC-MRRE-SOURCE-18 | stance: support | summary: This source uses or discusses `mrre` for rank-error behavior across neighborhood sizes in dimensionality-reduction evaluation. | evidence_ids: ZR18-E2
- CLAIM-METRIC-ND-SOURCE-18 | stance: support | summary: This source uses or discusses `nd` for neighbor-shape/neighbor-change dissimilarity in dimensionality-reduction evaluation. | evidence_ids: ZR18-E2
- CLAIM-METRIC-PR-SOURCE-18 | stance: support | summary: This source uses or discusses `pr` for linear agreement of pairwise relationships in dimensionality-reduction evaluation. | evidence_ids: ZR18-E2
- CLAIM-METRIC-SNC-SOURCE-18 | stance: support | summary: This source uses or discusses `snc` for inter-cluster reliability via steadiness/cohesiveness in dimensionality-reduction evaluation. | evidence_ids: ZR18-E2
- CLAIM-METRIC-STRESS-SOURCE-18 | stance: support | summary: This source uses or discusses `stress` for distance-fitting distortion objective/metric in dimensionality-reduction evaluation. | evidence_ids: ZR18-E2
- CLAIM-METRIC-TNC-SOURCE-18 | stance: support | summary: This source uses or discusses `tnc` for local neighborhood trustworthiness/continuity balance in dimensionality-reduction evaluation. | evidence_ids: ZR18-E2

# Workflow Relevance Map
- step: 3 | relevance: high | note: Informs task-aligned metric/technique selection and metric trust calibration.
- step: 4 | relevance: medium | note: Affects optimization objective design and score interpretation during hyperparameter search.
- step: 6 | relevance: high | note: Provides rationale that can be translated for end users.

# Evidence
- ZR18-E1 | page: 1, section: extracted, quote: "The ﬁnal version of this record is available at: xx.xxxx/TVCG.201x.xxxxxxx/ Measuring and Explaining the Inter-Cluster Reliability of Multidimensional Projections Hyeon Jeon, Hyung-Kwon Ko, Jaemin Jo, Y oungtaek Kim, and Jinwook Seo Abstract— We propose Steadiness and Cohesiveness, two novel metrics to measure the inter-cluster reliabilit"
- ZR18-E2 | page: 1, section: extracted, quote: "Measuring inter-cluster reliability is crucial as it directly affects how well inter-cluster tasks (e.g., identifying cluster relationships in the original space from a projected view) can be conducted; however, despite the importance of inter-cluster tasks, we found that previous metrics, such as Trustworthiness and Continuity, fail to m"
- ZR18-E3 | page: 1, section: extracted, quote: "Our metrics consider two aspects of the inter-cluster reliability: Steadiness measures the extent to which clusters in the projected space form clusters in the original space, and Cohesiveness measures the opposite."
- ZR18-E4 | page: 1, section: extracted, quote: "In this paper, we propose Steadiness and Cohesiveness, two metrics that quantitatively evaluate inter-cluster reliability."
- ZR18-E5 | page: 1, section: extracted, quote: "Steadiness measures the inter-cluster reliability in the projected space (i.e., to what degree the cluster in the projection is in a steady state that reﬂects the actual cluster in the original space)."
- ZR18-E6 | page: 1, section: extracted, quote: "Cohesiveness measures the inter-cluster reliability in the original space (i.e., to what degree real clusters in the original space stand together cohesively in the projection)."
- ZR18-E7 | page: 1, section: extracted, quote: "We ﬁrst formulated three design considerations of Steadiness and Cohesiveness so that the metrics can adequately evaluate inter-cluster reliability by quantifying how well inter-cluster tasks can be performed accurately in MDPs (i.e., measure the potential accuracy of the inter-cluster tasks)."
- ZR18-E8 | page: 1, section: extracted, quote: "To make our metrics fulﬁll the considerations, we deﬁned new inter-cluster distortion types—False Groups and Missing Groups—and designed Steadiness and Cohesiveness to measure each, respectively."
