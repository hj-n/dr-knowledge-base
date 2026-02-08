---
id: paper-2010-pending-ref-004
title: "Information retrieval perspective to nonlinear dimensionality reduction for data visualization"
authors: "J. V enna, J. Peltonen, K. Nybo, H. Aidos, and S. Kaski"
venue: "UNKNOWN"
year: 2010
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-004-2010-information-retrieval-perspective-to-nonlinear-dimensionality-reduction-for-data-visu.pdf
seed_note_id: "paper-2015-perception-based-projection-evaluation"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- 2.1.3 D ISCUSSION Given a high-dimensional data set, it is generally not possi ble to show all the similarity relationships within the data on a low-dimensional display; therefore, all linear or nonlinear dimensionality reduction methods need to make a tradeoff about which kinds o f similarity relationships they aim to show on the display.
- In high-dimensional data , such as experimental data where each dimension corresponds to a different measured variable, dependencies between different dimensions often restrict the data points to a manifold whose dimensionality is much lower than the dimensionality of the data space.
- Box 15400, FI-00076 Aalto, Finland Editor: Yoshua Bengio Abstract Nonlinear dimensionality reduction methods are often used to visualize high-dimensional data, although the existing methods have been designed for other rel ated tasks such as manifold learning.
- Abstract Nonlinear dimensionality reduction methods are often used to visualize high-dimensional data, although the existing methods have been designed for other rel ated tasks such as manifold learning.

# Method Summary
- Our notion of plug-in supervised metrics could in principle be used with other methods too; other unsupervised embedding algorithms that work based on a distance matrix can also be turned into supervised versions, by plugging in learning metric di stances into the distance matrix.
- In contrast, the embedding B minimizes the number of misses by simply squashing the sphere ﬂat; this results in a large number of false positives because points on opposite sides of the sphere are mapped close to each other.Top right: mean precision-mean recall curves with input neighborhood sizer = 75, as a function of the output neighborhood size k, for the two projections.
- Some of the successful methods include isomap (T enenbaum et al., 2000), locally linear embedding (LLE; Roweis and Saul, 2000), Laplacian eigenmap (LE; Belkin and Niyogi, 2002a), and maximum variance unfolding (MVU; Weinberger and Saul, 2006). c⃝YYYY Jarkko Venna, Jaakko Peltonen, Kristian Nybo, Helena Aidos and Samuel Kaski.
- 5.2 Comparison Methods for Supervised Visualization For each data set to be visualized, the choice of supervised v s. unsupervised visualization is up to the analyst; in general, supervised embedding will preserve differences between classes better but at the expense of within-class details.
- Examples of this approach include the multidimensional scaling (MDS)-type cost functions like Sammon’s cost and Stress, methods that relate the distances in the input space to the output space, and various correlation measures that assess the preservation of all pairw ise distances.
- The locally linear embedding (LLE; Roweis and Saul, 2000) algorithm is based on the assumption that the data manifold is smooth enough and is sampled de nsely enough, such that each data point lies close to a locally linear subspace on the manifold .
- NeRV includes the previous method called stochastic neighbor embedding (SNE; Hinton and Roweis, 2002) as a special case where the tradeoffis set so that only recall is maximized; thus we give a new information retrieval interpretation to SNE.

# When To Use / Not Use
- Use when:
  - Many of the methods have a parameter k denoting the number of nearest neighbors for constructing a neighborhood graph; for each method and each dat a set we tested values of k ranging from 4 to 20, and chose the value that produced the best F-measure. (For MVU and LMVU we used a smaller parameter range to save computational time.
  - To speed up convergence and avoid local minima, we apply a further initialization step: we run ten rounds of conjugate gradient (two conjugate gradient st eps per round), and after each round decrease the neighborhood scaling parameters σi used in Equations (2) and (3).
- Avoid when:
  - Many of the best manifold extraction methods perform surprisingly poorly, most likely because they h ave not been designed to reduce the dimensionality below the intrinsic dimensionality of the d ata manifold.
  - Preservatio n of pairwise distances, the other widely adopted principle, is a well-deﬁned goal; it is a reasonable goal if the analyst wishes to use the visualization to assess distances between selected pairs o f data points, but we argue that this is not the typical way how an analyst would use a visualization, at least in the early stages of analysis when no hypothesis about the data has yet been formed.
- Failure modes:
  - Here we speciﬁed the rough upper limit for the number of relevant neighbors as 0 .5 · n/K where n is the number of data points and K is the number of mixture components used to estimate the metric; this choice roughly means that for well-separated mixture components, each dat a point will on average consider half of the data points from the same mixture component as relevant neighbors.

# Metrics Mentioned
- `trustworthiness`: referenced as part of projection-quality or reliability assessment.
- `continuity`: referenced as part of projection-quality or reliability assessment.
- `stress`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- To speed up convergence and avoid local minima, we apply a further initialization step: we run ten rounds of conjugate gradient (two conjugate gradient st eps per round), and after each round decrease the neighborhood scaling parameters σi used in Equations (2) and (3).
- This initialization step has th e same complexity O(dn2) per iteration as the rest of the algorithm.
- The conditional density estimate is of the form ˆp(c|x) = ∑K k=1 βck exp(−||x − mk||2/2σ2) ∑K k=1 exp(−||x − mk||2/2σ2) (10) where the number of Gaussians K, the centroids mk, the class probabilities βck and the Gaussian width σ (standard deviation) are parameters of the estimate; we require that the βck are nonnegative and that ∑c βck = 1 for all k.
- Many of the methods have a parameter k denoting the number of nearest neighbors for constructing a neighborhood graph; for each method and each dat a set we tested values of k ranging from 4 to 20, and chose the value that produced the best F-measure. (For MVU and LMVU we used a smaller parameter range to save computational time.
- The me asures are very useful for comparing several visualizations of the same data, and will turn ou t to be useful as optimization criteria, but we would additionally like to have measures where the pla in numbers are easily interpretable.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-004-C1 | stance: support | summary: 2.1.3 D ISCUSSION Given a high-dimensional data set, it is generally not possi ble to show all the similarity relationships within the data on a low-dimensional display; therefore, all linear or nonlinear dimensionality reduction methods need to make a tradeoff about which kinds o f similarity relationships they aim to show on the display. | evidence_ids: PENDING-REF-004-E1, PENDING-REF-004-E2
- CLAIM-PENDING-REF-004-C2 | stance: support | summary: Our notion of plug-in supervised metrics could in principle be used with other methods too; other unsupervised embedding algorithms that work based on a distance matrix can also be turned into supervised versions, by plugging in learning metric di stances into the distance matrix. | evidence_ids: PENDING-REF-004-E3, PENDING-REF-004-E4
- CLAIM-PENDING-REF-004-C3 | stance: support | summary: To speed up convergence and avoid local minima, we apply a further initialization step: we run ten rounds of conjugate gradient (two conjugate gradient st eps per round), and after each round decrease the neighborhood scaling parameters σi used in Equations (2) and (3). | evidence_ids: PENDING-REF-004-E5, PENDING-REF-004-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 4 | relevance: high | note: contains initialization sensitivity or control-policy evidence

# Evidence
- PENDING-REF-004-E1 | page: 4, section: extracted, quote: "2.1.3 D ISCUSSION Given a high-dimensional data set, it is generally not possi ble to show all the similarity relationships within the data on a low-dimensional display; therefore, all linear or nonlinear dimensionality reduction methods need to make a tradeoff about which kinds o f similarity relationships they aim to show on the display."
- PENDING-REF-004-E2 | page: 1, section: extracted, quote: "In high-dimensional data , such as experimental data where each dimension corresponds to a different measured variable, dependencies between different dimensions often restrict the data points to a manifold whose dimensionality is much lower than the dimensionality of the data space."
- PENDING-REF-004-E3 | page: 1, section: extracted, quote: "Box 15400, FI-00076 Aalto, Finland Editor: Yoshua Bengio Abstract Nonlinear dimensionality reduction methods are often used to visualize high-dimensional data, although the existing methods have been designed for other rel ated tasks such as manifold learning."
- PENDING-REF-004-E4 | page: 1, section: extracted, quote: "Abstract Nonlinear dimensionality reduction methods are often used to visualize high-dimensional data, although the existing methods have been designed for other rel ated tasks such as manifold learning."
- PENDING-REF-004-E5 | page: 24, section: extracted, quote: "Our notion of plug-in supervised metrics could in principle be used with other methods too; other unsupervised embedding algorithms that work based on a distance matrix can also be turned into supervised versions, by plugging in learning metric di stances into the distance matrix."
- PENDING-REF-004-E6 | page: 6, section: extracted, quote: "In contrast, the embedding B minimizes the number of misses by simply squashing the sphere ﬂat; this results in a large number of false positives because points on opposite sides of the sphere are mapped close to each other.Top right: mean precision-mean recall curves with input neighborhood sizer = 75, as a function of the output neighborhood size k, for the two projections."
- PENDING-REF-004-E7 | page: 1, section: extracted, quote: "Some of the successful methods include isomap (T enenbaum et al., 2000), locally linear embedding (LLE; Roweis and Saul, 2000), Laplacian eigenmap (LE; Belkin and Niyogi, 2002a), and maximum variance unfolding (MVU; Weinberger and Saul, 2006). c⃝YYYY Jarkko Venna, Jaakko Peltonen, Kristian Nybo, Helena Aidos and Samuel Kaski."
- PENDING-REF-004-E8 | page: 19, section: extracted, quote: "5.2 Comparison Methods for Supervised Visualization For each data set to be visualized, the choice of supervised v s. unsupervised visualization is up to the analyst; in general, supervised embedding will preserve differences between classes better but at the expense of within-class details."
