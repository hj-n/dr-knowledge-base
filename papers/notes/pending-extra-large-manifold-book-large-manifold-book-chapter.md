---
id: paper-2006-pending-extra-large-manifold-book
title: "Large-Scale Manifold Learning"
authors: "Ameet Talwalkar, Sanjiv Kumar, Mehryar Mohri, Henry Rowley"
venue: "Manifold Learning Theory and Applications"
year: 2011
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/large_manifold_book_chapter.pdf
seed_note_id: "paper-2025-jeon-reliable-va-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- Chapter 6 Large-scale Manifold Learning Ameet Talwalkar,1 Sanjiv Kumar, 2 Mehryar Mohri, 3 Henry Rowley 4 6.1 Introduction The problem of dimensionality reduction arises in many comp uter vision applications, where it is natural to represent images as vectors i n a high-dimensional space.
- 6.4.1 Manifold learning Manifold learning considers the problem of extracting low- dimensional structure from high-dimensional data.
- Instead of assuming global linearity, these met hods typically make a weaker local-linearity assumption, i.e., for nearby poin ts in high-dimensional input space, l2 distance is assumed to be a good measure of geodesic distance , or distance along the manifold.
- Hence, although matrix projection is often analyzed theoretically, for large-scale problems, the storage and comp utational requirements may be ineﬃcient or even infeasible.

# Method Summary
- The 2D embeddings of PIE-35K (Figur e 6.8) reveal that Laplacian Eigenmaps projects data points into a small compa ct region, consistent with its objective function deﬁned in (6.20), as it tend s to map neighboring 10The diﬀerences are statistically insigniﬁcant.
- 6.4.2 Approximation experiments Since we use sampling-based SVD approximation to scale Isom ap, we ﬁrst examined how well the Nystr¨ om and Column sampling methods app roximated our desired low-dimensional embeddings, i.e., Y = (Σk)1/2U⊤ k .
- In this chapter, we focus mainly on Isomap and Laplaci an Eigenmaps, as both methods have good theoretical properties and the diﬀ erences in their approaches allow us to make interesting comparisons betwee n dense and sparse methods.
- The algorithm takes O( nlk) time to perform compact SVD on C, but is still more expensive than the Nystr¨ om method as the constants for SVD are greater than those for the O( nlk) matrix multiplication step in the Nystr¨ om method.
- In this section, we will discuss i n detail how approximate embeddings can be used in the context of manifold l earning, relying on the sampling based algorithms from the previous section t o generate an approximate SVD.
- We then computed the approximate low-dimensional embeddings usin g the Nystr¨ om and Column sampling methods, and then used these embeddings to c ompute the associated approximate squared distance matrix, ˜D.
- COMPARISON OF SAMPLING METHODS 7 Projection, since it uses only singular vectors to compute the projecti on of K onto the space spanned by vectors Uk.

# When To Use / Not Use
- Use when:
  - Using C⊤ = [W K ⊤ 21] in (6.8) we have: ˜Kcol k = K =⇒ αC ( (C⊤ C) 1 2 k ) + W = C (6.14) =⇒ αUC,rV⊤ C,rW = UC,rΣC,rV⊤ C,r (6.15) =⇒ αVC,rV⊤ C,rW = VC,rΣC,rV⊤ C,r (6.16) =⇒ W = 1 α (C⊤ C)1/2. (6.17) In (6.16) we use U⊤ C,rUC,r = Ir, while (6.17) follows since VC,rV⊤ C,r is an orthogonal projection onto the span of the rows of C and the columns of W lie within this span implying VC,rV⊤ C,rW = W.
  - We also compared the performance of various tec hniques using 9In fact, the techniques we described in the context of approximating geo desic distances via shortest path are currently used by Google for its “People Hopper” a pplication which runs on the social networking site Orkut (Kumar & Rowley, 2010).
- Avoid when:
  - Assuming a uniform sampling of the columns, the Nystr¨ om method generates a rank- k approximation ˜K of K for k < n deﬁned by: ˜Knys k = CW+ k C⊤ ≈ K, (6.2) where Wk is the best k-rank approximation of W with respect to the spectral or Frobenius norm and W+ k denotes the pseudo-inverse of Wk.
  - LARGE-SCALE MANIFOLD LEARNING 6.3 Comparison of sampling methods Given that two sampling-based techniques exist to approxim ate the SVD of SPSD matrices, we pose a natural question: which method shou ld one use to approximate singular values, singular vectors and low-r ank approximations?
- Failure modes:
  - Find the k dimensional representation by minimizing the normalized, weighted distance between neighbors as, Y = argmin Y′ ∑ i,j ( Wij∥y′ i − y′ j∥2 2 √ DiiDjj ) . (6.20) 7The weight matrix should not be confused with the subsampled SPSD matr ix, W, associated with the Nystr¨ om method.

# Metrics Mentioned
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- It generates appr oximations of K by using the SVD of C.5 If we write the SVD of C as C = UCΣCV⊤ C then the Column sampling method approximates the top k singular values ( Σk) and singular vectors ( Uk) of K as: ˜Σcol = √ n l ΣC,k and ˜Ucol = UC = CVC,kΣ+ C,k. (6.4) The runtime of the Column sampling method is dominated by the SVD of C.
- Then construct W, a sparse, symmetric n × n matrix, where Wij = exp ( − ∥xi − xj∥2 2/σ2) if ( xi, xj) are neighbors, 0 otherwise, and σ is a scaling parameter.
- Results are averaged over 10 random K-means initializations. inputs as nearby as possible in the low-dimensional space.
- Results are averaged over 10 random K-means initializations.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-EXTRA-C1 | stance: support | summary: Chapter 6 Large-scale Manifold Learning Ameet Talwalkar,1 Sanjiv Kumar, 2 Mehryar Mohri, 3 Henry Rowley 4 6.1 Introduction The problem of dimensionality reduction arises in many comp uter vision applications, where it is natural to represent images as vectors i n a high-dimensional space. | evidence_ids: PENDING-EXTRA-E1, PENDING-EXTRA-E2
- CLAIM-PENDING-EXTRA-C2 | stance: support | summary: The 2D embeddings of PIE-35K (Figur e 6.8) reveal that Laplacian Eigenmaps projects data points into a small compa ct region, consistent with its objective function deﬁned in (6.20), as it tend s to map neighboring 10The diﬀerences are statistically insigniﬁcant. | evidence_ids: PENDING-EXTRA-E3, PENDING-EXTRA-E4
- CLAIM-PENDING-EXTRA-C3 | stance: support | summary: It generates appr oximations of K by using the SVD of C.5 If we write the SVD of C as C = UCΣCV⊤ C then the Column sampling method approximates the top k singular values ( Σk) and singular vectors ( Uk) of K as: ˜Σcol = √ n l ΣC,k and ˜Ucol = UC = CVC,kΣ+ C,k. (6.4) The runtime of the Column sampling method is dominated by the SVD of C. | evidence_ids: PENDING-EXTRA-E5, PENDING-EXTRA-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 4 | relevance: high | note: contains initialization sensitivity or control-policy evidence

# Evidence
- PENDING-EXTRA-E1 | page: 1, section: extracted, quote: "Chapter 6 Large-scale Manifold Learning Ameet Talwalkar,1 Sanjiv Kumar, 2 Mehryar Mohri, 3 Henry Rowley 4 6.1 Introduction The problem of dimensionality reduction arises in many comp uter vision applications, where it is natural to represent images as vectors i n a high-dimensional space."
- PENDING-EXTRA-E2 | page: 12, section: extracted, quote: "6.4.1 Manifold learning Manifold learning considers the problem of extracting low- dimensional structure from high-dimensional data."
- PENDING-EXTRA-E3 | page: 1, section: extracted, quote: "Instead of assuming global linearity, these met hods typically make a weaker local-linearity assumption, i.e., for nearby poin ts in high-dimensional input space, l2 distance is assumed to be a good measure of geodesic distance , or distance along the manifold."
- PENDING-EXTRA-E4 | page: 7, section: extracted, quote: "Hence, although matrix projection is often analyzed theoretically, for large-scale problems, the storage and comp utational requirements may be ineﬃcient or even infeasible."
- PENDING-EXTRA-E5 | page: 20, section: extracted, quote: "The 2D embeddings of PIE-35K (Figur e 6.8) reveal that Laplacian Eigenmaps projects data points into a small compa ct region, consistent with its objective function deﬁned in (6.20), as it tend s to map neighboring 10The diﬀerences are statistically insigniﬁcant."
- PENDING-EXTRA-E6 | page: 14, section: extracted, quote: "6.4.2 Approximation experiments Since we use sampling-based SVD approximation to scale Isom ap, we ﬁrst examined how well the Nystr¨ om and Column sampling methods app roximated our desired low-dimensional embeddings, i.e., Y = (Σk)1/2U⊤ k ."
- PENDING-EXTRA-E7 | page: 2, section: extracted, quote: "In this chapter, we focus mainly on Isomap and Laplaci an Eigenmaps, as both methods have good theoretical properties and the diﬀ erences in their approaches allow us to make interesting comparisons betwee n dense and sparse methods."
- PENDING-EXTRA-E8 | page: 5, section: extracted, quote: "The algorithm takes O( nlk) time to perform compact SVD on C, but is still more expensive than the Nystr¨ om method as the constants for SVD are greater than those for the O( nlk) matrix multiplication step in the Nystr¨ om method."
