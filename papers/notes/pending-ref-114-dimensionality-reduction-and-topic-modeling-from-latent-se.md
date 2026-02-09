---
id: paper-2012-pending-ref-114
title: "Dimensionality Reduction and Topic Modeling: From Latent Semantic Indexing to Latent Dirichlet Allocation and Beyond"
authors: "S. P . Crain, K. Zhou, S.-H. Y ang, and H. Zha"
venue: "Mining Text Data"
year: 2012
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-114-2012-dimensionality-reduction-and-topic-modeling-from-latent-semantic-indexing-to-latent-d.pdf
seed_note_id: "paper-2024-large-scale-text-spatialization"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- The core task of automated text mining shares many of the same challenges that Lisowsky faced.

# Method Summary
- Chapter 5 DIMENSIONALITY REDUCTION AND TOPIC MODELING: FROM LATENT SEMANTIC INDEXING TO LATENT DIRICHLET ALLOCATION AND BEYOND Steven P.
- Zhai (eds.), Mining Text Data, DOI 10.1007/978-1-4614-3223-4_5, 130 MINING TEXT DATA Abstract The bag-of-words representation commonly used in text analysis can be analyzed very eﬃciently and retains a great deal of useful information, but it is also troublesome because the same thought can be expressed using many diﬀerent terms or one term can have very diﬀerent meanings.
- Dimension reduction can collapse together terms that have the same semantics, to identify and disambiguate terms with multiple meanings and to provide a lower-dimensional representation of documents that reﬂects concepts instead of raw terms.
- In this chapter, we survey two inﬂuential forms of dimension reduction.
- Latent semantic indexing uses spectral decomposition to identify a lower-dimensional representation that maintains semantic properties of the documents.
- Topic modeling, including probabilistic latent semantic indexing and latent Dirichlet allocation, is a form of dimension reduction that uses a probabilistic model to ﬁnd the co-occurrence patterns of terms that correspond to semantic topics in a collection of documents.
- We describe the basic technologies in detail and expose the underlying mechanism.

# When To Use / Not Use
- Use when:
  - Zhai (eds.), Mining Text Data, DOI 10.1007/978-1-4614-3223-4_5, 130 MINING TEXT DATA Abstract The bag-of-words representation commonly used in text analysis can be analyzed very eﬃciently and retains a great deal of useful information, but it is also troublesome because the same thought can be expressed using many diﬀerent terms or one term can have very diﬀerent meanings.
  - Topic modeling, including probabilistic latent semantic indexing and latent Dirichlet allocation, is a form of dimension reduction that uses a probabilistic model to ﬁnd the co-occurrence patterns of terms that correspond to semantic topics in a collection of documents.
- Avoid when:
  - Latent semantic indexing uses spectral decomposition to identify a lower-dimensional representation that maintains semantic properties of the documents.
- Failure modes:
  - Latent semantic indexing uses spectral decomposition to identify a lower-dimensional representation that maintains semantic properties of the documents.

# Metrics Mentioned
- No explicit named metric was extracted from this source; combine this source with complementary DR quality checks in workflow Step 3.

# Implementation Notes
- Zhai (eds.), Mining Text Data, DOI 10.1007/978-1-4614-3223-4_5, 130 MINING TEXT DATA Abstract The bag-of-words representation commonly used in text analysis can be analyzed very eﬃciently and retains a great deal of useful information, but it is also troublesome because the same thought can be expressed using many diﬀerent terms or one term can have very diﬀerent meanings.
- Dimension reduction can collapse together terms that have the same semantics, to identify and disambiguate terms with multiple meanings and to provide a lower-dimensional representation of documents that reﬂects concepts instead of raw terms.
- In this chapter, we survey two inﬂuential forms of dimension reduction.
- Latent semantic indexing uses spectral decomposition to identify a lower-dimensional representation that maintains semantic properties of the documents.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-114-C1 | stance: support | summary: The core task of automated text mining shares many of the same challenges that Lisowsky faced. | evidence_ids: PENDING-REF-114-E1, PENDING-REF-114-E2
- CLAIM-PENDING-REF-114-C2 | stance: support | summary: Chapter 5 DIMENSIONALITY REDUCTION AND TOPIC MODELING: FROM LATENT SEMANTIC INDEXING TO LATENT DIRICHLET ALLOCATION AND BEYOND Steven P. | evidence_ids: PENDING-REF-114-E3, PENDING-REF-114-E4
- CLAIM-PENDING-REF-114-C3 | stance: support | summary: Zhai (eds.), Mining Text Data, DOI 10.1007/978-1-4614-3223-4_5, 130 MINING TEXT DATA Abstract The bag-of-words representation commonly used in text analysis can be analyzed very eﬃciently and retains a great deal of useful information, but it is also troublesome because the same thought can be expressed using many diﬀerent terms or one term can have very diﬀerent meanings. | evidence_ids: PENDING-REF-114-E5, PENDING-REF-114-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection

# Evidence
- PENDING-REF-114-E1 | page: 2, section: extracted, quote: "The core task of automated text mining shares many of the same challenges that Lisowsky faced."
- PENDING-REF-114-E2 | page: 1, section: extracted, quote: "Chapter 5 DIMENSIONALITY REDUCTION AND TOPIC MODELING: FROM LATENT SEMANTIC INDEXING TO LATENT DIRICHLET ALLOCATION AND BEYOND Steven P."
- PENDING-REF-114-E3 | page: 2, section: extracted, quote: "Zhai (eds.), Mining Text Data, DOI 10.1007/978-1-4614-3223-4_5, 130 MINING TEXT DATA Abstract The bag-of-words representation commonly used in text analysis can be analyzed very eﬃciently and retains a great deal of useful information, but it is also troublesome because the same thought can be expressed using many diﬀerent terms or one term can have very diﬀerent meanings."
- PENDING-REF-114-E4 | page: 2, section: extracted, quote: "Dimension reduction can collapse together terms that have the same semantics, to identify and disambiguate terms with multiple meanings and to provide a lower-dimensional representation of documents that reﬂects concepts instead of raw terms."
- PENDING-REF-114-E5 | page: 2, section: extracted, quote: "In this chapter, we survey two inﬂuential forms of dimension reduction."
- PENDING-REF-114-E6 | page: 2, section: extracted, quote: "Latent semantic indexing uses spectral decomposition to identify a lower-dimensional representation that maintains semantic properties of the documents."
- PENDING-REF-114-E7 | page: 2, section: extracted, quote: "Topic modeling, including probabilistic latent semantic indexing and latent Dirichlet allocation, is a form of dimension reduction that uses a probabilistic model to ﬁnd the co-occurrence patterns of terms that correspond to semantic topics in a collection of documents."
- PENDING-REF-114-E8 | page: 2, section: extracted, quote: "We describe the basic technologies in detail and expose the underlying mechanism."
