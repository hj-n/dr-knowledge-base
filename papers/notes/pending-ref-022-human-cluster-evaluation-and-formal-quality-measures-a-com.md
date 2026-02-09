---
id: paper-2012-pending-ref-022
title: "Human cluster evaluation and formal quality measures: A comparative study"
authors: "Joshua Lewis, Margareta Ackerman, and Virginia de Sa"
venue: "UNKNOWN"
year: 2012
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-022-2012-human-cluster-evaluation-and-formal-quality-measures-a-comparative-study.pdf
seed_note_id: "paper-2015-perception-based-projection-evaluation"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- Nevertheless, experts show much less sensitivity to the number of clusters and relate more closely to a greater range of clustering quality measures than novices, indicating a nuanced approach to the eval1870 uation problem.
- A Property-Based Taxonomy of CQMs In the absence of formal guidelines for CQM selection 2, in particular for selecting a versatile set of CQMs, we develop a property-based framework for distinguishing CQMs based on such a framework for clustering algorithms discussed in (Ackerman, Ben-David, & Loker, 2010b) (also see (BosaghZadeh & Ben-David, 2009) and (Ackerman, Ben-David, & Loker, 2010a)).
- The evaluation of clusterings is an integral part of the clustering process, needed not only to compare partitions to each other, but also to determine whether any of them are sufﬁciently good.1 As there is no universal clustering objective, there is no consensus on a formal deﬁnition of clustering.
- Previous studies have investigated how humans choose the number of groups (Lewis, 2009) and partition data (Santos & S´a, 2005) in a clustering setting, but these approaches only show what humans think are the optimal partitions rather than how they judge partition quality in general.

# Method Summary
- A Property-Based Taxonomy of CQMs In the absence of formal guidelines for CQM selection 2, in particular for selecting a versatile set of CQMs, we develop a property-based framework for distinguishing CQMs based on such a framework for clustering algorithms discussed in (Ackerman, Ben-David, & Loker, 2010b) (also see (BosaghZadeh & Ben-David, 2009) and (Ackerman, Ben-David, & Loker, 2010a)).
- The evaluation of clusterings is an integral part of the clustering process, needed not only to compare partitions to each other, but also to determine whether any of them are sufﬁciently good.1 As there is no universal clustering objective, there is no consensus on a formal deﬁnition of clustering.
- Previous studies have investigated how humans choose the number of groups (Lewis, 2009) and partition data (Santos & S´a, 2005) in a clustering setting, but these approaches only show what humans think are the optimal partitions rather than how they judge partition quality in general.
- Second we choose cluster centroids using two strategies: for four of the clusterings we randomly select k centroids from the original dataset, and for ﬁve of the clusterings we select k centroids from a Laplacian Eigenmap embedding of the data.
- Nevertheless, experts show much less sensitivity to the number of clusters and relate more closely to a greater range of clustering quality measures than novices, indicating a nuanced approach to the eval1870 uation problem.
- Intuitively, in (Lewis, 2009) and (Santos & S ´a, 2005) subjects took on the role of a k-choosing algorithm and a clustering algorithm (respectively), whereas in this study subjects are in the role of clustering evaluators.
- Our human subjects were divided into a novice group with little or no knowledge of clustering methods and an expert group with detailed knowledge of clustering methods.

# When To Use / Not Use
- Use when:
  - 1871 We used 19 different two dimensional datasets to generate our clustering stimuli, drawn from (Lewis, 2009), and chosen to represent a range of dataset types including mixtures of Gaussians and datasets with hierarchical structure.
  - If one needs to evaluate a very large number of partitions it may be reasonable to use human computation via a service such as Mechanical Turk to rank partitions efﬁciently (or at least throw out the really bad ones).
- Avoid when:
  - We instructed subjects to choose the two best partitioned displays and the one worst partitioned display from the nine available on every trial (leaving six displays implicitly chosen as neutral).
  - Because cluster centroids are chosen randomly, increasing k is likely to increase the chance of getting an undesirable partition (e.g. a partition with very few data points).
- Failure modes:
  - Silhouette provides the best overall correlation with expert classiﬁcations, and Avg Within provides the best overall correlation with novice classiﬁcations (savek).

# Metrics Mentioned
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- Given the plethora of clustering techniques and their possible parameter settings, data analysts require sound means of comparing alternate partitions of the same data.
- The evaluation of clusterings is an integral part of the clustering process, needed not only to compare partitions to each other, but also to determine whether any of them are sufﬁciently good.1 As there is no universal clustering objective, there is no consensus on a formal deﬁnition of clustering.
- Previous studies have investigated how humans choose the number of groups (Lewis, 2009) and partition data (Santos & S´a, 2005) in a clustering setting, but these approaches only show what humans think are the optimal partitions rather than how they judge partition quality in general.
- Second we choose cluster centroids using two strategies: for four of the clusterings we randomly select k centroids from the original dataset, and for ﬁve of the clusterings we select k centroids from a Laplacian Eigenmap embedding of the data.
- Nevertheless, experts show much less sensitivity to the number of clusters and relate more closely to a greater range of clustering quality measures than novices, indicating a nuanced approach to the eval1870 uation problem.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-022-C1 | stance: support | summary: Nevertheless, experts show much less sensitivity to the number of clusters and relate more closely to a greater range of clustering quality measures than novices, indicating a nuanced approach to the eval1870 uation problem. | evidence_ids: PENDING-REF-022-E1, PENDING-REF-022-E2
- CLAIM-PENDING-REF-022-C2 | stance: support | summary: A Property-Based Taxonomy of CQMs In the absence of formal guidelines for CQM selection 2, in particular for selecting a versatile set of CQMs, we develop a property-based framework for distinguishing CQMs based on such a framework for clustering algorithms discussed in (Ackerman, Ben-David, & Loker, 2010b) (also see (BosaghZadeh & Ben-David, 2009) and (Ackerman, Ben-David, & Loker, 2010a)). | evidence_ids: PENDING-REF-022-E3, PENDING-REF-022-E4
- CLAIM-PENDING-REF-022-C3 | stance: support | summary: Given the plethora of clustering techniques and their possible parameter settings, data analysts require sound means of comparing alternate partitions of the same data. | evidence_ids: PENDING-REF-022-E5, PENDING-REF-022-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance
- step: 6 | relevance: high | note: guides reliable interpretation of projected views

# Evidence
- PENDING-REF-022-E1 | page: 2, section: extracted, quote: "Nevertheless, experts show much less sensitivity to the number of clusters and relate more closely to a greater range of clustering quality measures than novices, indicating a nuanced approach to the eval1870 uation problem."
- PENDING-REF-022-E2 | page: 6, section: extracted, quote: "A Property-Based Taxonomy of CQMs In the absence of formal guidelines for CQM selection 2, in particular for selecting a versatile set of CQMs, we develop a property-based framework for distinguishing CQMs based on such a framework for clustering algorithms discussed in (Ackerman, Ben-David, & Loker, 2010b) (also see (BosaghZadeh & Ben-David, 2009) and (Ackerman, Ben-David, & Loker, 2010a))."
- PENDING-REF-022-E3 | page: 2, section: extracted, quote: "The evaluation of clusterings is an integral part of the clustering process, needed not only to compare partitions to each other, but also to determine whether any of them are sufﬁciently good.1 As there is no universal clustering objective, there is no consensus on a formal deﬁnition of clustering."
- PENDING-REF-022-E4 | page: 2, section: extracted, quote: "Previous studies have investigated how humans choose the number of groups (Lewis, 2009) and partition data (Santos & S´a, 2005) in a clustering setting, but these approaches only show what humans think are the optimal partitions rather than how they judge partition quality in general."
- PENDING-REF-022-E5 | page: 4, section: extracted, quote: "Second we choose cluster centroids using two strategies: for four of the clusterings we randomly select k centroids from the original dataset, and for ﬁve of the clusterings we select k centroids from a Laplacian Eigenmap embedding of the data."
- PENDING-REF-022-E6 | page: 2, section: extracted, quote: "Intuitively, in (Lewis, 2009) and (Santos & S ´a, 2005) subjects took on the role of a k-choosing algorithm and a clustering algorithm (respectively), whereas in this study subjects are in the role of clustering evaluators."
- PENDING-REF-022-E7 | page: 3, section: extracted, quote: "Our human subjects were divided into a novice group with little or no knowledge of clustering methods and an expert group with detailed knowledge of clustering methods."
- PENDING-REF-022-E8 | page: 4, section: extracted, quote: "1871 We used 19 different two dimensional datasets to generate our clustering stimuli, drawn from (Lewis, 2009), and chosen to represent a range of dataset types including mixtures of Gaussians and datasets with hierarchical structure."
