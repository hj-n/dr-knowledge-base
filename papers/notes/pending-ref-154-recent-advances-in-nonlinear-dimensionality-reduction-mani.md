---
id: paper-2010-pending-ref-154
title: "Nonlinear Dimensionality Reduction and Manifold Learning"
authors: "A. Wism €uller, M. Verleysen, M. Aupetit, and J. Lee"
venue: "Springer Texts in Statistics"
year: 2010
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-154-2010-recent-advances-in-nonlinear-dimensionality-reduction-manifold-and-topological-learni.pdf
seed_note_id: "paper-2019-mdp-visual-analytics-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- In structure-preserving dimensionality reduction, nonlinear embedding techniques are used to represent high-dimensional data or as preprocessing step for supervised or unsupervised learning task s ,e . g .[ 2 2 ,3 2 ] .H o w e v e r ,t h eﬁ n a ld i - mension of the projected data and the topological properties of the target space are constrained a priori.
- Bruges (Belgium), 28-30 April 2010, d-side publi., ISBN 2-930307-10-2. many mapping distortions, it is still possible to recover the original topology of the data or neuron structure in the data space.
- 3 Learning topology Applying geometrical and topological methods in order to analyze high-dimensional data has attracted recent scientiﬁc attention in themachine learning community, e.g. [22, 23, 24].
- The problem is that the map showsN points while there are aboutN 2 distor76 ESANN 2010 proceedings, European Symposium on Artificial Neural Networks - Computational Intelligence and Machine Learning.

# Method Summary
- As pointed out in [65], XOM represents the general concept of inverting topology-preserving mappings as a fundamental pattern recognition approach, thus implying novel methods for data clustering, semi-supervised learning [66], analysis of non-metric data, pattern matching, and incremental optimization [60].
- This approach provides conceptual and computational advantages when compared to SOM and other dimensionaliy reduction methods [65], which has been demonstrated by computer simulations and real-world applications, such as in functional MRI and gene expression analysis [65, 61].
- Aupetit [69] proposed the proximity measure for nonlinear projection methods, which considers a reference point, and displays its original distance to the other points as a color of their Vorono¨ı cells.
- Several aspects are dealt with, ranging from novel algorithmic approaches to their realworld applications.
- In structure-preserving dimensionality reduction, nonlinear embedding techniques are used to represent high-dimensional data or as preprocessing step for supervised or unsupervised learning task s ,e . g .[ 2 2 ,3 2 ] .H o w e v e r ,t h eﬁ n a ld i - mension of the projected data and the topological properties of the target space are constrained a priori.
- Recent studies about quality assesment of dimensionality reduction [9, 10] (see also Section 4) have shown that embedding errors can be divided into two types: either distant points are erroneously embedded close to each other or initially nearby points are mapped too far away.
- Starting from a ﬁnite set of points in a highdimensional space, several approaches intend to learn, explore and exploit the topology of manifolds, from which these points are supposed to be drawn, or shapes, i.e. topological invariants, such as the intrinsic dimension.

# When To Use / Not Use
- Use when:
  - While this may be a suﬃcient summary to compare several mappings and select the best one, thisisnotenoughconsideringthatmappingsaretobeusedasvisualsupport decision tools which must be interpreted with the eyes.
  - The main conclusion to draw from these last works its that mappings are not an end, but only a means to display useable and useful information on top of them.
- Avoid when:
  - In structure-preserving dimensionality reduction, nonlinear embedding techniques are used to represent high-dimensional data or as preprocessing step for supervised or unsupervised learning task s ,e . g .[ 2 2 ,3 2 ] .H o w e v e r ,t h eﬁ n a ld i - mension of the projected data and the topological properties of the target space are constrained a priori.
  - We stress that nonlinear maps which display multidimensional data as cloud of points, cannot be trusted as such, because axes have no meaning so we cannot tell about the correlation of some original variables, and distances are not well preserved in general so we cannot tell about the authenticity of the cluster structure we observe.
- Failure modes:
  - Aupetit proposed to visualize local amount of compression and stretching, coloring Vorono¨ı cells of edges in the Delaunay graph of the mapped data[69], which is somehow similar to the U-matrix representation used with SOM [72] where color shows the amount of empty space between the neurons in the data space.

# Metrics Mentioned
- `trustworthiness`: referenced as part of projection-quality or reliability assessment.
- `continuity`: referenced as part of projection-quality or reliability assessment.
- `stress`: referenced as part of projection-quality or reliability assessment.
- `kl divergence`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- As pointed out in [65], XOM represents the general concept of inverting topology-preserving mappings as a fundamental pattern recognition approach, thus implying novel methods for data clustering, semi-supervised learning [66], analysis of non-metric data, pattern matching, and incremental optimization [60].
- At the expense of replacing the spectral decomposition with more general optimization tools such as gradient descent, the cost function that formalizes distance preservation can be extended and deﬁned in more ﬂexible ways.
- Bruges (Belgium), 28-30 April 2010, d-side publi., ISBN 2-930307-10-2. proper objective criteria compatible with the application goal, the use of optimization techniques, the need for evaluation criteria, etc.
- The appealing theoretical properties of spectral techniques, such as the guarantee to ﬁnd the global optimum, are thus counterbalanced by the bigger ﬂexibility oﬀered by non-spectral optimization.
- Bruges (Belgium), 28-30 April 2010, d-side publi., ISBN 2-930307-10-2. preserving mappings (as in SOM) and principled direct optimization of divergence measures (e.g.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-154-C1 | stance: support | summary: In structure-preserving dimensionality reduction, nonlinear embedding techniques are used to represent high-dimensional data or as preprocessing step for supervised or unsupervised learning task s ,e . g .[ 2 2 ,3 2 ] .H o w e v e r ,t h eﬁ n a ld i - mension of the projected data and the topological properties of the target space are constrained a priori. | evidence_ids: PENDING-REF-154-E1, PENDING-REF-154-E2
- CLAIM-PENDING-REF-154-C2 | stance: support | summary: As pointed out in [65], XOM represents the general concept of inverting topology-preserving mappings as a fundamental pattern recognition approach, thus implying novel methods for data clustering, semi-supervised learning [66], analysis of non-metric data, pattern matching, and incremental optimization [60]. | evidence_ids: PENDING-REF-154-E3, PENDING-REF-154-E4
- CLAIM-PENDING-REF-154-C3 | stance: support | summary: As pointed out in [65], XOM represents the general concept of inverting topology-preserving mappings as a fundamental pattern recognition approach, thus implying novel methods for data clustering, semi-supervised learning [66], analysis of non-metric data, pattern matching, and incremental optimization [60]. | evidence_ids: PENDING-REF-154-E5, PENDING-REF-154-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-REF-154-E1 | page: 4, section: extracted, quote: "In structure-preserving dimensionality reduction, nonlinear embedding techniques are used to represent high-dimensional data or as preprocessing step for supervised or unsupervised learning task s ,e . g .[ 2 2 ,3 2 ] .H o w e v e r ,t h eﬁ n a ld i - mension of the projected data and the topological properties of the target space are constrained a priori."
- PENDING-REF-154-E2 | page: 2, section: extracted, quote: "Bruges (Belgium), 28-30 April 2010, d-side publi., ISBN 2-930307-10-2. many mapping distortions, it is still possible to recover the original topology of the data or neuron structure in the data space."
- PENDING-REF-154-E3 | page: 4, section: extracted, quote: "3 Learning topology Applying geometrical and topological methods in order to analyze high-dimensional data has attracted recent scientiﬁc attention in themachine learning community, e.g. [22, 23, 24]."
- PENDING-REF-154-E4 | page: 6, section: extracted, quote: "The problem is that the map showsN points while there are aboutN 2 distor76 ESANN 2010 proceedings, European Symposium on Artificial Neural Networks - Computational Intelligence and Machine Learning."
- PENDING-REF-154-E5 | page: 5, section: extracted, quote: "As pointed out in [65], XOM represents the general concept of inverting topology-preserving mappings as a fundamental pattern recognition approach, thus implying novel methods for data clustering, semi-supervised learning [66], analysis of non-metric data, pattern matching, and incremental optimization [60]."
- PENDING-REF-154-E6 | page: 5, section: extracted, quote: "This approach provides conceptual and computational advantages when compared to SOM and other dimensionaliy reduction methods [65], which has been demonstrated by computer simulations and real-world applications, such as in functional MRI and gene expression analysis [65, 61]."
- PENDING-REF-154-E7 | page: 7, section: extracted, quote: "Aupetit [69] proposed the proximity measure for nonlinear projection methods, which considers a reference point, and displays its original distance to the other points as a color of their Vorono¨ı cells."
- PENDING-REF-154-E8 | page: 1, section: extracted, quote: "Several aspects are dealt with, ranging from novel algorithmic approaches to their realworld applications."
