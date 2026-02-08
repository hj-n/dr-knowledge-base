---
id: paper-2009-pending-ref-043
title: "Local procrustes for manifold embedding: A measure of embedding quality and embedding algorithms"
authors: "Y. Goldberg and Y. Ritov"
venue: "Machine Learning"
year: 2009
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-043-2009-local-procrustes-for-manifold-embedding-a-measure-of-embedding-quality-and-embedding.pdf
seed_note_id: "paper-2019-mdp-visual-analytics-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- While our main discussion regards isometric embeddings, we will also discuss the conformal embedding problem, which is the framework of algorithms such as c-Isomap (de Silva and Tenenbaum, 2003) and Conformal Embeddings (CE) (Sha and Saul, 2005).
- The main difﬁculty in analyzing such high-dimensional data sets is, that the number of observations required to estimate functions at a set level of accuracy grows exponentially with the dimension.
- A more realistic assumption than that of an underlying linear structure is that the data is on, or next to, an embedded manifold of low dimension in the high-dimensional space.
- We further suggest two new algorithms for discovering the low-dimensional embedding of a high-dimensional data set, based on minimization of the suggested measure function.

# Method Summary
- Abstract We present the Procrustes measure, a novel measure based on Procrustes rotation that enables quantitative comparison of the output of manifold-based embedding algorithms (such as LLE (Roweis and Saul, 2000) and Isomap (Tenenbaum et al, 2000)).
- In addition, we present an iterative method that can improve the output of the two algorithms, as well as other existing algorithms.
- 8) with respect to Y (see Mardia et al, 1979) and using the fact that A′ iAi = I, we obtain ∂ ∂Y R(X,Y|A1, . . . ,An) = 2 n n ∑ i=1 HiXA i− 2 n n ∑ i=1 HiY . (10) Using the general inverse of ∑n i=1 Hi we can write Y as Y = ( n ∑ i=1 Hi )⊥ n ∑ i=1 HiXA i . (11) Summarizing, we present the PSA algorithm.
- Many algorithms were developed to perform embedding for manifold-based data sets, including the algorithms suggested by Roweis and Saul (2000); Tenenbaum et al (2000); Belkin and Niyogi (2003); Zhang and Zha (2004); Donoho and Grimes (2004); Weinberger and Saul (2006); Dollar et al (2007).
- While our main discussion regards isometric embeddings, we will also discuss the conformal embedding problem, which is the framework of algorithms such as c-Isomap (de Silva and Tenenbaum, 2003) and Conformal Embeddings (CE) (Sha and Saul, 2005).
- Second, R(X,Y ) is not an ideal measure of the quality of embedding for algorithms that normalize their output, such as LLE (Roweis and Saul, 2000), Laplacian Eigenmap (Belkin and Niyogi, 2003), and LTSA (Zhang and Zha, 2004).
- Instead of measuring the difference between the original neighborhoods on the manifold and their embeddings, one can compare the local PCA projections (Mardia et al, 1979) of the original neighborhoods with their embeddings.

# When To Use / Not Use
- Use when:
  - Hence (xi j− ¯xi)  2 − J′ i (xi j− ¯xi)  2 = q ∑ p=d+1 (w′ p(xi j− ¯xi))2 = (xi j− ¯xi)− JiJ′ i (xi j− ¯xi)  2 = Ji(zi j− ¯zi)− JiJ′ i (Ji(zi j− ¯zi)) +O(r2 i )  2 = O(r2 i ) 2 = O(r4 i ) , where wd+1, . . . ,wq are a completion of w1, . . . ,wd to an orthonormal basis of Rq and we used the fact that J′ i Ji = I.
  - Find the largest cluster of aligned matrices (for example, use BFS (Corman et al, 1990) and deﬁne an alignment criterion). – Other iterations: Apply SA to the matrices that are not in the largest cluster.
- Avoid when:
  - This is because normalization of the output distorts the structure of the local neighborhoods and therefore yields high Rvalues even if the output seems to ﬁnd the underlying structure of the input.
  - Rather, a different or modiﬁed technique for subspaces alignment, for example the use of landmarks (de Silva and Tenenbaum, 2003), is required in order to make this algorithm truly useful.
- Failure modes:
  - The use of local PCA produces a good lowdimensional description of the neighborhoods, but the description of each of the neighborhoods is in an arbitrary coordinate system.

# Metrics Mentioned
- `procrustes-based quality`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- Although SA is a time-consuming algorithm, each iteration is very simple, involving onlyO(Kqd 3) operations, where K is the maximum number of neighbors, and q and d are the input and output dimensions, respectively.
- Find the largest cluster of aligned matrices (for example, use BFS (Corman et al, 1990) and deﬁne an alignment criterion). – Other iterations: Apply SA to the matrices that are not in the largest cluster.
- Initialization: – Choose an initial conﬁguration (for example, using GP). – Compute the initial temperature (see Siarry et al, 1997). – Deﬁne the cooling scheme (see Siarry et al, 1997).
- Initialization: – Find the neighbors Xi of each point xi and let Neighbors (i) be the indices of the neighbors Xi. – Initialize the list of all embedded points’ indices to N := / 0.
- The cooling scheme requires the estimation of many parameters, and the run-time depends heavily on the correct choice of these parameters.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-043-C1 | stance: support | summary: While our main discussion regards isometric embeddings, we will also discuss the conformal embedding problem, which is the framework of algorithms such as c-Isomap (de Silva and Tenenbaum, 2003) and Conformal Embeddings (CE) (Sha and Saul, 2005). | evidence_ids: PENDING-REF-043-E1, PENDING-REF-043-E2
- CLAIM-PENDING-REF-043-C2 | stance: support | summary: Abstract We present the Procrustes measure, a novel measure based on Procrustes rotation that enables quantitative comparison of the output of manifold-based embedding algorithms (such as LLE (Roweis and Saul, 2000) and Isomap (Tenenbaum et al, 2000)). | evidence_ids: PENDING-REF-043-E3, PENDING-REF-043-E4
- CLAIM-PENDING-REF-043-C3 | stance: support | summary: Although SA is a time-consuming algorithm, each iteration is very simple, involving onlyO(Kqd 3) operations, where K is the maximum number of neighbors, and q and d are the input and output dimensions, respectively. | evidence_ids: PENDING-REF-043-E5, PENDING-REF-043-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 4 | relevance: high | note: contains initialization sensitivity or control-policy evidence

# Evidence
- PENDING-REF-043-E1 | page: 3, section: extracted, quote: "While our main discussion regards isometric embeddings, we will also discuss the conformal embedding problem, which is the framework of algorithms such as c-Isomap (de Silva and Tenenbaum, 2003) and Conformal Embeddings (CE) (Sha and Saul, 2005)."
- PENDING-REF-043-E2 | page: 1, section: extracted, quote: "The main difﬁculty in analyzing such high-dimensional data sets is, that the number of observations required to estimate functions at a set level of accuracy grows exponentially with the dimension."
- PENDING-REF-043-E3 | page: 1, section: extracted, quote: "A more realistic assumption than that of an underlying linear structure is that the data is on, or next to, an embedded manifold of low dimension in the high-dimensional space."
- PENDING-REF-043-E4 | page: 2, section: extracted, quote: "We further suggest two new algorithms for discovering the low-dimensional embedding of a high-dimensional data set, based on minimization of the suggested measure function."
- PENDING-REF-043-E5 | page: 1, section: extracted, quote: "Abstract We present the Procrustes measure, a novel measure based on Procrustes rotation that enables quantitative comparison of the output of manifold-based embedding algorithms (such as LLE (Roweis and Saul, 2000) and Isomap (Tenenbaum et al, 2000))."
- PENDING-REF-043-E6 | page: 7, section: extracted, quote: "In addition, we present an iterative method that can improve the output of the two algorithms, as well as other existing algorithms."
- PENDING-REF-043-E7 | page: 9, section: extracted, quote: "8) with respect to Y (see Mardia et al, 1979) and using the fact that A′ iAi = I, we obtain ∂ ∂Y R(X,Y/A1, . . . ,An) = 2 n n ∑ i=1 HiXA i− 2 n n ∑ i=1 HiY . (10) Using the general inverse of ∑n i=1 Hi we can write Y as Y = ( n ∑ i=1 Hi )⊥ n ∑ i=1 HiXA i . (11) Summarizing, we present the PSA algorithm."
- PENDING-REF-043-E8 | page: 2, section: extracted, quote: "Many algorithms were developed to perform embedding for manifold-based data sets, including the algorithms suggested by Roweis and Saul (2000); Tenenbaum et al (2000); Belkin and Niyogi (2003); Zhang and Zha (2004); Donoho and Grimes (2004); Weinberger and Saul (2006); Dollar et al (2007)."
