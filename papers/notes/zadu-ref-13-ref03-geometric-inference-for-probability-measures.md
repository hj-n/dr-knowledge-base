---
id: paper-2010-zadu-ref-13
title: "Geometric Inference for Measures based on Distance Functions"
authors: "Frédéric Chazal, David Cohen-Steiner, Quentin Mérigot"
venue: "Foundations of Computational Mathematics"
year: 2010
tags: [dr, zadu-table1-reference, dtm, stress]
source_pdf: papers/raw/zadu-table1-references/ref03_geometric_inference_for_probability_measures.pdf
evidence_level: medium
updated_at: 2026-02-08
---
# Problem
- 1.2 Contributions A possible way to solve the problem of outliers for distance-based inference is then to try to replace the usual distance function to a set K by another notion of distance function that is robust to the addition of a certain amount of outliers.
- 5 Relation with non-parametric density estimation Nearest-neighbor estimators are a family of non-parametric density estimators, that has been extensively used in nonparametric discrimination, pattern recognition and spatial analysis problems.
- Cependant, une des principales limitation de ce cadre est qu’il ne permet pas de consid´ erer des donn´ ees qui sont entach´ ees de valeurs aberrantes et/ou d’un bruit de fond.
- However, one of the main limitations of this framework is that it does not cope well with outliers nor with background noise.
- In this paper, we show how to extend the framework of distance functions to overcome this problem.

# Method Summary
- We propose a method similar to mean shift, but where the distance function replaces the estimated density.
- Mots-cl´ es : estimation de densit´ e, reconstruction, distance de Wasserstein, Mean-Shift Geometric Inference for Measures based on Distance Functions 3 1 Introduction Extracting geometric and topological information from geometric data, such as 3D point clouds obtained from laser scanners, is a requirement for many geometry processing and data analysis algorithms.
- Moreover, by comparing the volume of an intrinsic ball of the unit sphere and the volume of its orthogonal projection on the tangent space to its center, one has: βk, 1/R 2(ε ) = Rkβk, 1(ε/R ) ⩾Rk[sin(ε/R )]kβk where βk is the volume of the k-dimensional unit ball.
- For instance, [11] has described an algorithm that given a point cloud C builds a simplicial complex, called the α -complex, that has the same topology as the union of balls of radius α centered at points in C.
- As mentioned earlier, the question of the convergence of the empirical measure µ N to the underlying measure µ is fundamendal in the measurebased inference approach we propose.
- In this article, we introduce a notion of distance function to a probability measureµ , which we denote by d µ,m 0 — where m0 is a “smoothing” parameter in (0, 1).
- Moreover, in settings where empirical measures are considered these functions can be easily evaluated, making them of particular practical interest.

# When To Use / Not Use
- Use when:
  - If one considers again the example given in the end of ➜ 2.1 of an empirical measure µ N whose samples are drawn according to a “geometric” measure ν convolved with a Gaussian distribution N (0,σ ), the combination of the two previous facts gives: lim N → +∞ W2(µ N,µ ) ⩽σ with probability one Similar bounds are also possible with convolution kernels that are not translation invariant, such as the ones deﬁning the noise model used in [18].
  - Key-words: density estimation, reconstruction, Wasserstein distance, Mean-Shift Inf´ erence g´ eom´ etrique pour les mesures en utilisant la fonction distance R´ esum´ e :De nombreuses donn´ ees sont souvent repr´ esent´ ees sous forme de nuages de points ´ echantillonn´ es dans des espaces Euclidiens au voisinage de sous-ensembles compacts.
  - Because one of the goals of this article is to give inference results, i.e. comparison between discrete and the continuous representations, we cannot give the deﬁnitions and theorems only in the discrete case, but have to deal with the general case of probability measures.
- Avoid when:
  - This gives W2 2(m0δx,ν ) = ∫ R d ∥h − x∥2 dν (h) ⩾ ∫ m0 0 F −1 µ x (m)2dm = ∫ m0 0 δµ,m (x)2dm =m0d2 µ,m 0(x) (3) INRIA Geometric Inference for Measures based on Distance Functions 11 The second inequality is because Fµ x(t) = µ (B(x,t )), and thus F −1 µ x (m) = δµ,m (x).
  - Moreover, in the case of point clouds/empirical measures (ﬁnite sums of Dirac measures), the computation of the distance function to a measure (and its gradient) at a given point boils down to a computation of nearest neighbors making it easy to use in practice.
- Failure modes:
  - Mathematically, it is deﬁned as a function that maps every (Borel) subset B of Rd to a non-negative numberµ (B), which is countably additive in the sense that whenever ( Bi) is a countable family of disjoint Borel subsets of Rd, µ (∪i∈NBi) = ∑ iµ (Bi).
  - 5 Relation with non-parametric density estimation Nearest-neighbor estimators are a family of non-parametric density estimators, that has been extensively used in nonparametric discrimination, pattern recognition and spatial analysis problems.

# Metrics Mentioned
- `nd`: neighbor-shape dissimilarity or neighbor distortion.
- `pr`: pairwise-distance correlation behavior.
- `topo`: topology-related structure behavior.
- `proc`: Procrustes local shape agreement.
- `stress`: stress-based distance distortion.

# Implementation Notes
- INRIA Geometric Inference for Measures based on Distance Functions 17 4.2 Distance to a measure vs. distance to its support In this paragraph, we compare the distance functions dµ,m 0 to a measure µ and the distance function to its support S, and study the convergence properties as the mass parameter m0 converges to zero.
- INRIA Geometric Inference for Measures based on Distance Functions 9 In order to gain both Wasserstein-stability and regularity, we deﬁne the distance function to µ as a L 2 average of the the pseudo-distances δµ,m for a range [0,m 0] of parameters m: Deﬁnition 3.2.
- Similarly, ﬁnding out the number of parameters really needed to faithfully describe a point in the cloud – which is usually much smaller than the dimension of the ambient space – is a matter of estimating the dimension of the underlying set.
- Remark that in the above deﬁnition 4.1 the notion of α -reach could be made dependent on a parameter r, i.e. the ( r,α )-reach ofϕ could be deﬁned as the maximum r′such that the set ϕ −1((r,r +r′]) does not contain any α -critical value.
- We call distance function to µ with parameter m0 the function deﬁned by : d2 µ,m 0 : Rn → R+, x ↦→ 1 m0 ∫ m0 0 δµ,m (x)2dm As an example, let C be a point cloud with N points in Rd, and µ C be the uniform measure on it.
- Indeed, adding even a single data point that is far from the original point cloud will increase by one the number of connected components of the oﬀsets of this point cloud, for a large range of parameters.
- Keep preprocessing, initialization policy, and random-seed protocol fixed when comparing methods.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PAPER2010ZADUREF13-C1 | stance: support | summary: 1.2 Contributions A possible way to solve the problem of outliers for distance-based inference is then to try to replace the usual distance function to a set K by another notion of distance function that is robust to the addition of a certain amount of outliers. | evidence_ids: PAPER2010ZADUREF13-E1, PAPER2010ZADUREF13-E2
- CLAIM-PAPER2010ZADUREF13-C2 | stance: support | summary: We propose a method similar to mean shift, but where the distance function replaces the estimated density. | evidence_ids: PAPER2010ZADUREF13-E3, PAPER2010ZADUREF13-E4
- CLAIM-PAPER2010ZADUREF13-C3 | stance: support | summary: INRIA Geometric Inference for Measures based on Distance Functions 17 4.2 Distance to a measure vs. distance to its support In this paragraph, we compare the distance functions dµ,m 0 to a measure µ and the distance function to its support S, and study the convergence properties as the mass parameter m0 converges to zero. | evidence_ids: PAPER2010ZADUREF13-E5, PAPER2010ZADUREF13-E6
- CLAIM-METRIC-DTM-SOURCE-13 | stance: support | summary: This source includes evidence relevant to `dtm` in dimensionality-reduction reliability evaluation. | evidence_ids: PAPER2010ZADUREF13-E1, PAPER2010ZADUREF13-E2
- CLAIM-METRIC-STRESS-SOURCE-13 | stance: support | summary: This source includes evidence relevant to `stress` in dimensionality-reduction reliability evaluation. | evidence_ids: PAPER2010ZADUREF13-E1, PAPER2010ZADUREF13-E2

# Workflow Relevance Map
- step: 2 | relevance: medium | note: adds constraints for preprocessing and data-audit checks
- step: 3 | relevance: high | note: directly informs task-aligned technique/metric selection
- step: 6 | relevance: high | note: adds hyperparameter sensitivity or optimization guidance
- step: 7 | relevance: high | note: supports visualization interpretation and user explanation

# Evidence
- PAPER2010ZADUREF13-E1 | page: 7, section: extracted, quote: "1.2 Contributions A possible way to solve the problem of outliers for distance-based inference is then to try to replace the usual distance function to a set K by another notion of distance function that is robust to the addition of a certain amount of outliers."
- PAPER2010ZADUREF13-E2 | page: 22, section: extracted, quote: "5 Relation with non-parametric density estimation Nearest-neighbor estimators are a family of non-parametric density estimators, that has been extensively used in nonparametric discrimination, pattern recognition and spatial analysis problems."
- PAPER2010ZADUREF13-E3 | page: 5, section: extracted, quote: "Cependant, une des principales limitation de ce cadre est qu’il ne permet pas de consid´ erer des donn´ ees qui sont entach´ ees de valeurs aberrantes et/ou d’un bruit de fond."
- PAPER2010ZADUREF13-E4 | page: 4, section: extracted, quote: "However, one of the main limitations of this framework is that it does not cope well with outliers nor with background noise."
- PAPER2010ZADUREF13-E5 | page: 4, section: extracted, quote: "In this paper, we show how to extend the framework of distance functions to overcome this problem."
- PAPER2010ZADUREF13-E6 | page: 24, section: extracted, quote: "We propose a method similar to mean shift, but where the distance function replaces the estimated density."
- PAPER2010ZADUREF13-E7 | page: 5, section: extracted, quote: "Mots-cl´ es : estimation de densit´ e, reconstruction, distance de Wasserstein, Mean-Shift Geometric Inference for Measures based on Distance Functions 3 1 Introduction Extracting geometric and topological information from geometric data, such as 3D point clouds obtained from laser scanners, is a requirement for many geometry processing and data analysis algorithms."
- PAPER2010ZADUREF13-E8 | page: 21, section: extracted, quote: "Moreover, by comparing the volume of an intrinsic ball of the unit sphere and the volume of its orthogonal projection on the tangent space to its center, one has: βk, 1/R 2(ε ) = Rkβk, 1(ε/R ) ⩾Rk[sin(ε/R )]kβk where βk is the volume of the k-dimensional unit ball."
- PAPER2010ZADUREF13-E9 | page: 6, section: extracted, quote: "For instance, [11] has described an algorithm that given a point cloud C builds a simplicial complex, called the α -complex, that has the same topology as the union of balls of radius α centered at points in C."
- PAPER2010ZADUREF13-E10 | page: 9, section: extracted, quote: "As mentioned earlier, the question of the convergence of the empirical measure µ N to the underlying measure µ is fundamendal in the measurebased inference approach we propose."
- PAPER2010ZADUREF13-E11 | page: 7, section: extracted, quote: "In this article, we introduce a notion of distance function to a probability measureµ , which we denote by d µ,m 0 — where m0 is a “smoothing” parameter in (0, 1)."
- PAPER2010ZADUREF13-E12 | page: 4, section: extracted, quote: "Moreover, in settings where empirical measures are considered these functions can be easily evaluated, making them of particular practical interest."
