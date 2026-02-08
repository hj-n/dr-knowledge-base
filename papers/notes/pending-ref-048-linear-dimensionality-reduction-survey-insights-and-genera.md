---
id: paper-2015-pending-ref-048
title: "Linear dimensionality reduction: Survey, insights, and generalizations"
authors: "John P Cunningham and Zoubin Ghahramani"
venue: "UNKNOWN"
year: 2015
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-048-2015-linear-dimensionality-reduction-survey-insights-and-generalizations.pdf
seed_note_id: "paper-2021-quantitative-survey-dr-techniques"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- Instead of resorting to ad hoc (and often suboptimal) formulations for each new problem in linear dimensionality reduction, practitioners need only specify the objectivefX(·) and the high-dimensional data X, and these numerical technologies can produce the desired low-dimensional data.
- Speciﬁcally, if we have available only pairwise distances dX(xi,xj), a more general MDS problem statement is to ﬁt the low-dimensional data so as to preserve these pairwise distances as closely as possible in the least squares sense: minimizing ∑ i ∑ j(dX(xi,xj) − dY (yi,yj))2 is known as Kruskal-Shephard scaling, and the distance metrics can be arbitrary and diﬀerent between the original and low-dimensional data.
- Perhaps inherited from this eigenvalue misconception, a second common tendency is for practitioners to greedily choose the low-dimensional data: the ﬁrst dimension is chosen to optimize the problem objective, and then subsequent dimensions are chosen to optimize the objective on a residual or reduced data set.
- A ﬁrst example is kernel PCA, which uses PCA on a feature space instead of the inputs themselves (Sch¨ olkopf et al., 1999), and indeed some dimensionality reduction methods and their kernelized counterparts can be considered together as kernel regression problems (De la Torre, 2012).

# Method Summary
- When the data is known, we see here that if we specify a low-dimensional orthogonal projection Y = M⊤X, then indeed this objective will result in the class of linear dimensionality reduction programs minimize ∑ i ∑ j ( dX (xi,xj) −dY ( M⊤xi,M⊤xj ))2 subject to M ∈ Od×r. (4) Special approaches exist to solve this program on a case-by-case basis (Cox and Cox, 2001; Borg and Groenen, 2005).
- Accordingly, CCA and PCA point out two key features of linear dimensionality reduction and Deﬁnition 1: ﬁrst, that the objective function fX(·) need not entirely deﬁne the linear mapping P to the low-dimensional space; and second, that not all linear dimensionality reduction methods need be orthogonal projections, or indeed projections at all.
- Note that several methods will require optimization over additional auxiliary unconstrained variables, which can be addressed algorithmically via a coordinate descent approach (alternating optimizations over the auxiliary variable and Equation 1) or some more nuanced scheme.
- However, by broadly considering Equation 4 as an optimization over orthogonal projections, we again see the motivation for a generic numerical solver for this class of problems, obviating objective-speciﬁc methods.
- This objective does not admit an eigenvalue approach, and as a result several specialized algorithms have been proposed.
- We present PPCA as a separate algorithm below and leave the others as extensions of this core method.
- These algorithms all share a common purpose (modeling covariance) and the same coordinate system for projection (the principal axes of the covariance ellipsoid), even though they diﬀer in the particulars of the projection and which basis is chosen from that coordinate system.

# When To Use / Not Use
- Use when:
  - A ﬁrst example is kernel PCA, which uses PCA on a feature space instead of the inputs themselves (Sch¨ olkopf et al., 1999), and indeed some dimensionality reduction methods and their kernelized counterparts can be considered together as kernel regression problems (De la Torre, 2012).
  - Thus matrix decomposition approaches suggest an unfortunate limitation to the set of possible linear dimensionality reduction problems, and a broader framework is required to fully capture Deﬁnition 1 and linear dimensionality reduction.
- Avoid when:
  - As a point of technical detail, note that the use of two data sets and mappings is only a notational convenience; writing the CCA projection as Y = [Ya Yb ] = [Pa 0 0 Pb ][Xa Xb ] = PX , we see that CCA adheres precisely to Deﬁnition 1.
  - Third, extensions have introduced outlier insensitivity via a diﬀerent implicit noise model such as a Laplace observation model, leading to a few examples of robust PCA (Galpin and Hawkins, 1987; Baccini et al., 1996; Choulakian, 2006).
- Failure modes:
  - This more general form of MDS is used in a variety of nonlinear dimensionality reduction techniques, including prominently Isomap (Tenenbaum et al., 2000), as discussed below in Section 3.3.

# Metrics Mentioned
- `stress`: referenced as part of projection-quality or reliability assessment.
- `procrustes-based quality`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- Instead, viewed through the lens of Equation 1, linear dimensionality reduction is simply an optimization program over a matrix manifold, and indeed there is a well-developed optimization literature for matrix manifolds (foundations include Luenberger, 1972; Gabay, 1982; Edelman et al., 1998; an excellent summary is Absil et al., 2008).
- Note that several methods will require optimization over additional auxiliary unconstrained variables, which can be addressed algorithmically via a coordinate descent approach (alternating optimizations over the auxiliary variable and Equation 1) or some more nuanced scheme.
- This simple perspective leads to a generic algorithm for linear dimensionality reduction, suggesting that, like numerical optimization more generally, linear dimensionality reduction can become abstracted as a numerical technology for a range of problem-speciﬁc objectives.
- However, this choice is a convenience of implementation and not a fundamental issue, and thus approaches for optimization of nondiﬀerentiable objectives over nonconvex sets (here Od×r) could be readily introduced to remove this restriction (for example, Boyd et al., 2011).
- MDS leads to the seemingly novel optimization program (Equation 1) over the scatter objective fX(M) = ∑ i ∑ j ||M⊤xi −M⊤xj||2, which can be expanded as fX(M) ∝ tr ( M⊤XX⊤M ) − 1⊤X⊤MM⊤X1 = tr ( M⊤X ( I − 1 n11⊤ ) X⊤M ) , (3) where we denote the vector of all ones as 1.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-048-C1 | stance: support | summary: Instead of resorting to ad hoc (and often suboptimal) formulations for each new problem in linear dimensionality reduction, practitioners need only specify the objectivefX(·) and the high-dimensional data X, and these numerical technologies can produce the desired low-dimensional data. | evidence_ids: PENDING-REF-048-E1, PENDING-REF-048-E2
- CLAIM-PENDING-REF-048-C2 | stance: support | summary: When the data is known, we see here that if we specify a low-dimensional orthogonal projection Y = M⊤X, then indeed this objective will result in the class of linear dimensionality reduction programs minimize ∑ i ∑ j ( dX (xi,xj) −dY ( M⊤xi,M⊤xj ))2 subject to M ∈ Od×r. (4) Special approaches exist to solve this program on a case-by-case basis (Cox and Cox, 2001; Borg and Groenen, 2005). | evidence_ids: PENDING-REF-048-E3, PENDING-REF-048-E4
- CLAIM-PENDING-REF-048-C3 | stance: support | summary: Instead, viewed through the lens of Equation 1, linear dimensionality reduction is simply an optimization program over a matrix manifold, and indeed there is a well-developed optimization literature for matrix manifolds (foundations include Luenberger, 1972; Gabay, 1982; Edelman et al., 1998; an excellent summary is Absil et al., 2008). | evidence_ids: PENDING-REF-048-E5, PENDING-REF-048-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-REF-048-E1 | page: 5, section: extracted, quote: "Instead of resorting to ad hoc (and often suboptimal) formulations for each new problem in linear dimensionality reduction, practitioners need only specify the objectivefX(·) and the high-dimensional data X, and these numerical technologies can produce the desired low-dimensional data."
- PENDING-REF-048-E2 | page: 7, section: extracted, quote: "Speciﬁcally, if we have available only pairwise distances dX(xi,xj), a more general MDS problem statement is to ﬁt the low-dimensional data so as to preserve these pairwise distances as closely as possible in the least squares sense: minimizing ∑ i ∑ j(dX(xi,xj) − dY (yi,yj))2 is known as Kruskal-Shephard scaling, and the distance metrics can be arbitrary and diﬀerent between the original and low-dimensional data."
- PENDING-REF-048-E3 | page: 2, section: extracted, quote: "Perhaps inherited from this eigenvalue misconception, a second common tendency is for practitioners to greedily choose the low-dimensional data: the ﬁrst dimension is chosen to optimize the problem objective, and then subsequent dimensions are chosen to optimize the objective on a residual or reduced data set."
- PENDING-REF-048-E4 | page: 5, section: extracted, quote: "A ﬁrst example is kernel PCA, which uses PCA on a feature space instead of the inputs themselves (Sch¨ olkopf et al., 1999), and indeed some dimensionality reduction methods and their kernelized counterparts can be considered together as kernel regression problems (De la Torre, 2012)."
- PENDING-REF-048-E5 | page: 7, section: extracted, quote: "When the data is known, we see here that if we specify a low-dimensional orthogonal projection Y = M⊤X, then indeed this objective will result in the class of linear dimensionality reduction programs minimize ∑ i ∑ j ( dX (xi,xj) −dY ( M⊤xi,M⊤xj ))2 subject to M ∈ Od×r. (4) Special approaches exist to solve this program on a case-by-case basis (Cox and Cox, 2001; Borg and Groenen, 2005)."
- PENDING-REF-048-E6 | page: 3, section: extracted, quote: "Accordingly, CCA and PCA point out two key features of linear dimensionality reduction and Deﬁnition 1: ﬁrst, that the objective function fX(·) need not entirely deﬁne the linear mapping P to the low-dimensional space; and second, that not all linear dimensionality reduction methods need be orthogonal projections, or indeed projections at all."
- PENDING-REF-048-E7 | page: 4, section: extracted, quote: "Note that several methods will require optimization over additional auxiliary unconstrained variables, which can be addressed algorithmically via a coordinate descent approach (alternating optimizations over the auxiliary variable and Equation 1) or some more nuanced scheme."
- PENDING-REF-048-E8 | page: 7, section: extracted, quote: "However, by broadly considering Equation 4 as an optimization over orthogonal projections, we again see the motivation for a generic numerical solver for this class of problems, obviating objective-speciﬁc methods."
