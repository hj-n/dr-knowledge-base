---
id: paper-2016-pending-ref-087
title: "Explaining three-dimensional dimensionality reduction plots"
authors: "Danilo B. Coimbra, Rafael M. Martins, Tácito T.A.T. Neves, Alexandru C. Telea, and Fernando V. Paulovich"
venue: "Information Visualization"
year: 2016
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-087-2016-explaining-three-dimensional-dimensionality-reduction-plots.pdf
seed_note_id: "paper-2019-mdp-visual-analytics-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- Instead of using the scatterplot idea of plotting observations along two orthogonal (Cartesian) axes mapping two variables, biplots approximate the multivariate distribution of a high-dimensional dataset in a few dimensions, typically 2 or 3, by superimposing representations of variable values on representations of the observations themselves.
- Summarizing the above, with needed brevity, we argue that (a) 2D DR plots are generally found more effective for the specific tasks of cluster separation and searching and require less interaction; while 3D DR plots preserve distances better, but loose appeal due to navigation, orientation, and occlusion problems.
- Enhanced biplot axes Standard biplots project the n variables into biplot axes in the low-dimensional mD space using SVD (equation (3)), as described in section ‘ ‘Explaining projections.’ ’ This has several problems.
- Y et, such methods are not preferred, precisely because of their error rates and the difficulty of finding globally good viewpoints, and thus affect our overall proposal only marginally.

# Method Summary
- The part-linear multidimensional projection (PLMP) method avoids this by using distances only for a small set of sample (representative) points in Dn and using the nD coordinates for the remaining points.14 DR methods can be classified by the techniques used to compute f:14 spectral decomposition techniques project points along the eigenvectors having the largest eigenvalues of the pointwise distance matrix.
- Our methods, realized as linked views, explain the meaning of projected dimensions in terms of original variables; show projection nonlinearities and correlations (or lack thereof) for these variables; help finding good viewpoints from which given variable pairs can be best explored; and quickly show which variable pairs can be explored from any possible viewpoint.
- Scalability Our methods are simple to implement and computationally scalable: we only need to apply the chosen DR projection to a small set of sample points distributed along the input variables (section ‘ ‘Enhanced biplot axes’ ’).
- P denotes the parameter space of f,t h a t is, the settings that control the projection algorithm. f is designed to keep the so-called structure of the data as similar as possible in Rn and Rm.
- W e illustrate our visualization techniques by applying them to several data-exploration scenarios involving real-world multidimensional datasets and a set of recent DR projection algorithms.
- These vectors show the direction of maximal variation in the resulting m-dimensional projection of our n variables.42,44 A different approach to Goal 1 is given in Broeksema et al.
- Finally, we propose an interactive viewpoint legend that provides an overview of the information visible in a given three-dimensional projection from all possible viewpoints.

# When To Use / Not Use
- Use when:
  - The part-linear multidimensional projection (PLMP) method avoids this by using distances only for a small set of sample (representative) points in Dn and using the nD coordinates for the remaining points.14 DR methods can be classified by the techniques used to compute f:14 spectral decomposition techniques project points along the eigenvectors having the largest eigenvalues of the pointwise distance matrix.
  - Projected results can be next visualized by techniques such as scatterplots 1 and parallel coordinates.2 DR methods have been used for the analysis of text documents, 3–7 multimedia,8,9 text mining, 10,11 vector fields,12 and biomedical data.13–15 DR techniques have become very robust, precise, computationally scalable, and easy to apply.
- Avoid when:
  - Third, unlike Broeksema et al., 45 sorting legends allows us to tell which variables can be best read along x and y, or worst read (because being orthogonal to the xy plane); discover variable correlations; and make legends scalable for large n values.
  - W e assign to each pair p 2 P, thus to all C best-visible variable pairs, a distinct color c(p), using a categorical colormap, and color the sphere points v as follows: If p(v) 2 P , we use for v the color c(p), else we use the color gray.
- Failure modes:
  - Given such a viewpoint, a key user question is ‘ ‘what can I see from here?’ ’ This question can be rephrased as follows: the variations in which original nD variables can we see best along screen axes x 1 and x2?

# Metrics Mentioned
- `stress`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- 8 Nonlinear optimization methods iteratively search the parameter space P to minimize the stress s.28,29 Besides naive gradient descent, multigrid numerical solvers are used to speed searching.30 Pekalska et al.31 propose a speedup that projects a sample subset (by gradient descent) and fits remaining points by local interpolation.
- Projected results can be next visualized by techniques such as scatterplots 1 and parallel coordinates.2 DR methods have been used for the analysis of text documents, 3–7 multimedia,8,9 text mining, 10,11 vector fields,12 and biomedical data.13–15 DR techniques have become very robust, precise, computationally scalable, and easy to apply.
- Third, unlike Broeksema et al., 45 sorting legends allows us to tell which variables can be best read along x and y, or worst read (because being orthogonal to the xy plane); discover variable correlations; and make legends scalable for large n values.
- Scalability Our methods are simple to implement and computationally scalable: we only need to apply the chosen DR projection to a small set of sample points distributed along the input variables (section ‘ ‘Enhanced biplot axes’ ’).
- P denotes the parameter space of f,t h a t is, the settings that control the projection algorithm. f is designed to keep the so-called structure of the data as similar as possible in Rn and Rm.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-087-C1 | stance: support | summary: Instead of using the scatterplot idea of plotting observations along two orthogonal (Cartesian) axes mapping two variables, biplots approximate the multivariate distribution of a high-dimensional dataset in a few dimensions, typically 2 or 3, by superimposing representations of variable values on representations of the observations themselves. | evidence_ids: PENDING-REF-087-E1, PENDING-REF-087-E2
- CLAIM-PENDING-REF-087-C2 | stance: support | summary: The part-linear multidimensional projection (PLMP) method avoids this by using distances only for a small set of sample (representative) points in Dn and using the nD coordinates for the remaining points.14 DR methods can be classified by the techniques used to compute f:14 spectral decomposition techniques project points along the eigenvectors having the largest eigenvalues of the pointwise distance matrix. | evidence_ids: PENDING-REF-087-E3, PENDING-REF-087-E4
- CLAIM-PENDING-REF-087-C3 | stance: support | summary: 8 Nonlinear optimization methods iteratively search the parameter space P to minimize the stress s.28,29 Besides naive gradient descent, multigrid numerical solvers are used to speed searching.30 Pekalska et al.31 propose a speedup that projects a sample subset (by gradient descent) and fits remaining points by local interpolation. | evidence_ids: PENDING-REF-087-E5, PENDING-REF-087-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-REF-087-E1 | page: 4, section: extracted, quote: "Instead of using the scatterplot idea of plotting observations along two orthogonal (Cartesian) axes mapping two variables, biplots approximate the multivariate distribution of a high-dimensional dataset in a few dimensions, typically 2 or 3, by superimposing representations of variable values on representations of the observations themselves."
- PENDING-REF-087-E2 | page: 5, section: extracted, quote: "Summarizing the above, with needed brevity, we argue that (a) 2D DR plots are generally found more effective for the specific tasks of cluster separation and searching and require less interaction; while 3D DR plots preserve distances better, but loose appeal due to navigation, orientation, and occlusion problems."
- PENDING-REF-087-E3 | page: 6, section: extracted, quote: "Enhanced biplot axes Standard biplots project the n variables into biplot axes in the low-dimensional mD space using SVD (equation (3)), as described in section ‘ ‘Explaining projections.’ ’ This has several problems."
- PENDING-REF-087-E4 | page: 18, section: extracted, quote: "Y et, such methods are not preferred, precisely because of their error rates and the difficulty of finding globally good viewpoints, and thus affect our overall proposal only marginally."
- PENDING-REF-087-E5 | page: 3, section: extracted, quote: "The part-linear multidimensional projection (PLMP) method avoids this by using distances only for a small set of sample (representative) points in Dn and using the nD coordinates for the remaining points.14 DR methods can be classified by the techniques used to compute f:14 spectral decomposition techniques project points along the eigenvectors having the largest eigenvalues of the pointwise distance matrix."
- PENDING-REF-087-E6 | page: 18, section: extracted, quote: "Our methods, realized as linked views, explain the meaning of projected dimensions in terms of original variables; show projection nonlinearities and correlations (or lack thereof) for these variables; help finding good viewpoints from which given variable pairs can be best explored; and quickly show which variable pairs can be explored from any possible viewpoint."
- PENDING-REF-087-E7 | page: 17, section: extracted, quote: "Scalability Our methods are simple to implement and computationally scalable: we only need to apply the chosen DR projection to a small set of sample points distributed along the input variables (section ‘ ‘Enhanced biplot axes’ ’)."
- PENDING-REF-087-E8 | page: 3, section: extracted, quote: "P denotes the parameter space of f,t h a t is, the settings that control the projection algorithm. f is designed to keep the so-called structure of the data as similar as possible in Rn and Rm."
