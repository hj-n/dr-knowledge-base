---
id: paper-2020-pending-ref-077
title: "Assessing single-cell transcriptomic variability through density-preserving data visualization"
authors: "A. Narayan, B. Berger, and H. Cho"
venue: "Nature Biotechnology"
year: 2020
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-077-2020-assessing-single-cell-transcriptomic-variability-through-density-preserving-data-visu.pdf
seed_note_id: "paper-2022-revisiting-dr-visual-cluster-analysis"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- To test whether the monocyte (a) and dendritic cell (b) subtypes with density diﬀerences highlighted by our visualizations reﬂect distinct subpopulations of cells, we performed Louvain clustering of each cell type in the PBMC dataset based on their high-dimensional gene expression proﬁles.
- Since the objective functions of each algorithm prioritize preserving local structure, they should encourage i and j to be nearest neighbors in the embedding as well, and so we only need to consider density with respect to those points.
- Overall, however, our algorithms still retain the substantial edge that nonlinear data visualization algorithms have in preserving clustering structure; e.g., a traditional approach to dimension reduction using PCA results in 35.7% (36.7%) lower performance on CS and 63.2% (64.1%) lower on MIS on average compared to t-SNE (UMAP).
- We computed the classiﬁcation score ( a), the mutual information score ( b), and the pairwise distance scores ( c and d) as proposed in the literature (Methods) for t-SNE, den-SNE, UMAP, and densMAP, additionally including PCA as a baseline representing traditional dimensionality reduction approach. a.

# Method Summary
- Since the objective functions of each algorithm prioritize preserving local structure, they should encourage i and j to be nearest neighbors in the embedding as well, and so we only need to consider density with respect to those points.
- Overall, however, our algorithms still retain the substantial edge that nonlinear data visualization algorithms have in preserving clustering structure; e.g., a traditional approach to dimension reduction using PCA results in 35.7% (36.7%) lower performance on CS and 63.2% (64.1%) lower on MIS on average compared to t-SNE (UMAP).
- We computed the classiﬁcation score ( a), the mutual information score ( b), and the pairwise distance scores ( c and d) as proposed in the literature (Methods) for t-SNE, den-SNE, UMAP, and densMAP, additionally including PCA as a baseline representing traditional dimensionality reduction approach. a.
- We computed the classiﬁcation score ( a), the mutual information score ( b), and the pairwise distance scores (c and d) as proposed in the literature (Methods) for t-SNE, den-SNE, UMAP, and densMAP, additionally including PCA as a baseline representing traditional dimensionality reduction approach. a.
- We computed the classiﬁcation score ( a), the mutual information score (b), and the pairwise distance scores ( c and d) as proposed in the literature (Methods) for t-SNE, den-SNE, UMAP, and densMAP, additionally including PCA as a baseline representing traditional dimensionality reduction approach. a.
- We computed the classiﬁcation score (a), the mutual information score ( b), and the pairwise distance scores ( c and d) as proposed in the literature (Methods) for t-SNE, den-SNE, UMAP, and densMAP, additionally including PCA as a baseline representing traditional dimensionality reduction approach. a.
- Supplementary Note 2 Gradient derivation for den-SNE and densMAP The core of our density-preserving tools lies in the optimization of the Pearson correlation between the log local radius of points in the original dataset and in the embedding (see Methods).

# When To Use / Not Use
- Use when:
  - We write: ρe,o = Cov(re,ro) σoσe = ∑N k=1(re k−µe)ro k so(N− 1) 1 2 [ σ2 + ∑N k=1(rk−µe)2 ] 1 2 (1) where µe is the average of re; σo and σe are the sample standard deviations of ro and re respectively, andσ2 is a user-speciﬁed constant for regularization (this ensures that the standard deviation of the embedded local radii does not go to zero).
  - Moreover, the trade-oﬀ between preserving density and capturing the clustering structure can be modulated by the user by changing the weight of the density-preservation objective, and we conﬁrmed that the den-SNE and densMAP scores converge to t-SNE and UMAP scores as that weight decreases (Supplementary Figures 4 to 8).
- Avoid when:
  - For many density functions (and certainly the one we use), ri will only depend on {dik,dki}N k=1, so we can further simplify the above expressions to: ∂ ˜Cov(re,ro) ∂d2 ij =ro i ∂re i ∂d2 ij +ro j ∂re j ∂d2 ij ∂ ˜Var(re) ∂d2 ij = 2 ( (re i−µe)∂re i ∂d2 ij + (re j−µe)∂re j ∂d2 ij ) .
  - Traditional dimensionality reduction algorithms, such as principal component analysis (PCA), Isomap, and multidimensional scaling (MDS), do not use an adaptive length-scale to model the data manifold, thus having the potential to preserve density better than t-SNE and UMAP.
- Failure modes:
  - Assume that for a given point X, we draw its n-nearest neighbors (which are used in the computation of t-SNE’s P matrix) as iid random variables X ={X1,...,X n} where each Xi∈ Rd is drawn from a Gaussian distribution with mean X and covariance matrix Σ.

# Metrics Mentioned
- `stress`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- Supplementary Note 2 Gradient derivation for den-SNE and densMAP The core of our density-preserving tools lies in the optimization of the Pearson correlation between the log local radius of points in the original dataset and in the embedding (see Methods).
- The densMAP gradient estimate for an edge {i,j} at each iteration of the SGD is then: ∇yiL|{i,j} = ( ∂ ∂d2 ij [logQij] +λ Z NPij ∂ρe,o ∂d2 ij − 1 |S| ∑ k∈S ∂ ∂d2 ik [log(1−Qik)] ) (yi−yj), where S is a set of edges adjacent to i chosen uniformly at random.
- The full gradient becomes: ∇yiL = ∑ {i,j}∈E ( Pij ∂ ∂d2 ij [logQij] + (1−Pij) ∂ ∂d2 ij [log(1−Qij)] +λ∂ρe,o ∂d2 ij ) (yi−yj).Note that, for the correlation term of the optimization, each edge is given equal weight (i.e. the term is not weighted by Pij).
- Although changing the perplexity and n neighbor parameters in t-SNE (a) and UMAP (b), respectively, can yield drastically diﬀerent embeddings, this does not result in density preservation.
- However, we can still connect the local radius to the length-scale parameter σ chosen by t-SNE, which itself is known to empirically proxy the length scale at each point.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-077-C1 | stance: support | summary: To test whether the monocyte (a) and dendritic cell (b) subtypes with density diﬀerences highlighted by our visualizations reﬂect distinct subpopulations of cells, we performed Louvain clustering of each cell type in the PBMC dataset based on their high-dimensional gene expression proﬁles. | evidence_ids: PENDING-REF-077-E1, PENDING-REF-077-E2
- CLAIM-PENDING-REF-077-C2 | stance: support | summary: Since the objective functions of each algorithm prioritize preserving local structure, they should encourage i and j to be nearest neighbors in the embedding as well, and so we only need to consider density with respect to those points. | evidence_ids: PENDING-REF-077-E3, PENDING-REF-077-E4
- CLAIM-PENDING-REF-077-C3 | stance: support | summary: Supplementary Note 2 Gradient derivation for den-SNE and densMAP The core of our density-preserving tools lies in the optimization of the Pearson correlation between the log local radius of points in the original dataset and in the embedding (see Methods). | evidence_ids: PENDING-REF-077-E5, PENDING-REF-077-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-REF-077-E1 | page: 14, section: extracted, quote: "To test whether the monocyte (a) and dendritic cell (b) subtypes with density diﬀerences highlighted by our visualizations reﬂect distinct subpopulations of cells, we performed Louvain clustering of each cell type in the PBMC dataset based on their high-dimensional gene expression proﬁles."
- PENDING-REF-077-E2 | page: 33, section: extracted, quote: "Since the objective functions of each algorithm prioritize preserving local structure, they should encourage i and j to be nearest neighbors in the embedding as well, and so we only need to consider density with respect to those points."
- PENDING-REF-077-E3 | page: 41, section: extracted, quote: "Overall, however, our algorithms still retain the substantial edge that nonlinear data visualization algorithms have in preserving clustering structure; e.g., a traditional approach to dimension reduction using PCA results in 35.7% (36.7%) lower performance on CS and 63.2% (64.1%) lower on MIS on average compared to t-SNE (UMAP)."
- PENDING-REF-077-E4 | page: 5, section: extracted, quote: "We computed the classiﬁcation score ( a), the mutual information score ( b), and the pairwise distance scores ( c and d) as proposed in the literature (Methods) for t-SNE, den-SNE, UMAP, and densMAP, additionally including PCA as a baseline representing traditional dimensionality reduction approach. a."
- PENDING-REF-077-E5 | page: 5, section: extracted, quote: "We computed the classiﬁcation score ( a), the mutual information score ( b), and the pairwise distance scores (c and d) as proposed in the literature (Methods) for t-SNE, den-SNE, UMAP, and densMAP, additionally including PCA as a baseline representing traditional dimensionality reduction approach. a."
- PENDING-REF-077-E6 | page: 8, section: extracted, quote: "We computed the classiﬁcation score ( a), the mutual information score (b), and the pairwise distance scores ( c and d) as proposed in the literature (Methods) for t-SNE, den-SNE, UMAP, and densMAP, additionally including PCA as a baseline representing traditional dimensionality reduction approach. a."
- PENDING-REF-077-E7 | page: 9, section: extracted, quote: "We computed the classiﬁcation score (a), the mutual information score ( b), and the pairwise distance scores ( c and d) as proposed in the literature (Methods) for t-SNE, den-SNE, UMAP, and densMAP, additionally including PCA as a baseline representing traditional dimensionality reduction approach. a."
- PENDING-REF-077-E8 | page: 31, section: extracted, quote: "Supplementary Note 2 Gradient derivation for den-SNE and densMAP The core of our density-preserving tools lies in the optimization of the Pearson correlation between the log local radius of points in the original dataset and in the embedding (see Methods)."
