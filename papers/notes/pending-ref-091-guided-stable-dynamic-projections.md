---
id: paper-2021-pending-ref-091
title: "Guided Stable Dynamic Projections"
authors: "E. F. V ernier, J. L. D. Comba, and A. C. Telea"
venue: "Computer Graphics Forum"
year: 2021
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-091-2021-guided-stable-dynamic-projections.pdf
seed_note_id: "paper-2024-large-scale-text-spatialization"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- While our work – for sure – does not solve the problem of dynamic projection of high-dimensional data, we argue that our methods bring added value to users interested in this goal.
- Motivated by these challenges of understanding and quantifying the quality of dynamic projections, Vernieret al. [VGd∗20] evaluated nine such techniques, and came to the conclusion that there is no perfect method, and that an inherent trade-off between stability and spatial quality (i.e., neighborhood and distance preservation) exists.
- 5.5): If we want the projection to adhere to a certain shape, or we have some prior knowledge over the high-dimensional space and we want areas of the projections to carry a certain data-related semantic, we can easily place landmarks to drive the projection to that behavior.
- Telea3 1Federal University of Rio Grande do Sul, Brazil 2University of Groningen, the Netherlands 3University of Utrecht, the Netherlands Abstract Projections aim to convey the relationships and similarity of high-dimensional data in a low-dimensional representation.

# Method Summary
- We propose two approaches that use global inﬂuences to steer projected points: Our ﬁrst method, LD-tSNE, offers similar ﬂexibility in steering dynamic projections via landmarks as known for static projections, and also reaches good quality values.
- Tens of different projection algorithms exist for static data; detailed taxonomies of such methods, benchmarks, and qualitative and quantitative evaluations are available in a range of surveys [NA19, EMK∗19, Fod02, CG15, SVPM14, vPVdH09].
- Horizontal lines show average metric values over all datasets for each (method, metric class) pair. parameters – or good preset values for all datasets – by grid search, following the approach in [ EMK∗19] for static projections.
- We propose two new guided methods for dynamic projection that use global inﬂuences (landmarks or suggested placements) to steer and stabilize the projection while still accounting for neighborhood preservation.
- We propose two dynamic projection methods (PCD-tSNE and LD-tSNE) that use global guides to steer projection points.
- Motivated by these challenges of understanding and quantifying the quality of dynamic projections, Vernieret al. [VGd∗20] evaluated nine such techniques, and came to the conclusion that there is no perfect method, and that an inherent trade-off between stability and spatial quality (i.e., neighborhood and distance preservation) exists.
- Images without red circles show (suboptimal) projection methods where it is not possible to see this training convergence. refers to minimizing the distance of P(xi) to the position given by the transformation matrix W composed of the top-q eigenvectors of D.

# When To Use / Not Use
- Use when:
  - Additionally, PCD-tSNE overcomes two limitations of AE-based methods and G-PCA: Autoencoders are based on neural networks, which can be challenging to set up, optimize for the architecture, and train; PCA based methods are sensitive to outliers and do not explicitly try to preserve local features.
  - The networks have the same architecture but use different optimizers, batch sizes, and training-set sizes. qtables: Internal state of agents learning to move a car up a hill using the reinforcement learning algorithm Q-learning [ Wat89].
- Avoid when:
  - Used originally to evaluate D-tSNE [RFaT16]. nnset: Internal states (weights and biases) of several neural networks during 30 training epochs to learn classifying the MNIST dataset.
  - The global inﬂuence of both methods can be controlled via simple user parameters to ﬁnd the best balance between stability and spatial quality.
- Failure modes:
  - De Silva et al. [DT05] propose regression models for picking the best landmarks, while Pezzotti et al. [PHL∗16] use a hierarchical approach.

# Metrics Mentioned
- `trustworthiness`: referenced as part of projection-quality or reliability assessment.
- `continuity`: referenced as part of projection-quality or reliability assessment.
- `stress`: referenced as part of projection-quality or reliability assessment.
- `procrustes-based quality`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- Once the PCDtSNE optimization starts, the additional term introduced on Equation 5 represents a simple convex function, which means that convergence is reached efﬁciently and PCD-tSNE performs similarly to C-tSNE, that is, inO(n2) time.
- Horizontal lines show average metric values over all datasets for each (method, metric class) pair. parameters – or good preset values for all datasets – by grid search, following the approach in [ EMK∗19] for static projections.
- Dimensionality reduction techniques, also called projections, are an established tool for visualizing such datasets in a simpliﬁed, compact, and scalable way.
- The global inﬂuence of both methods can be controlled via simple user parameters to ﬁnd the best balance between stability and spatial quality.
- To accelerate convergence, improve initialization, and create tighter clusters, exaggeration terms are used [ vH08, van15, LRH∗19, LS17].
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-091-C1 | stance: support | summary: While our work – for sure – does not solve the problem of dynamic projection of high-dimensional data, we argue that our methods bring added value to users interested in this goal. | evidence_ids: PENDING-REF-091-E1, PENDING-REF-091-E2
- CLAIM-PENDING-REF-091-C2 | stance: support | summary: We propose two approaches that use global inﬂuences to steer projected points: Our ﬁrst method, LD-tSNE, offers similar ﬂexibility in steering dynamic projections via landmarks as known for static projections, and also reaches good quality values. | evidence_ids: PENDING-REF-091-E3, PENDING-REF-091-E4
- CLAIM-PENDING-REF-091-C3 | stance: support | summary: Once the PCDtSNE optimization starts, the additional term introduced on Equation 5 represents a simple convex function, which means that convergence is reached efﬁciently and PCD-tSNE performs similarly to C-tSNE, that is, inO(n2) time. | evidence_ids: PENDING-REF-091-E5, PENDING-REF-091-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 4 | relevance: high | note: contains initialization sensitivity or control-policy evidence

# Evidence
- PENDING-REF-091-E1 | page: 11, section: extracted, quote: "While our work – for sure – does not solve the problem of dynamic projection of high-dimensional data, we argue that our methods bring added value to users interested in this goal."
- PENDING-REF-091-E2 | page: 2, section: extracted, quote: "Motivated by these challenges of understanding and quantifying the quality of dynamic projections, Vernieret al. [VGd∗20] evaluated nine such techniques, and came to the conclusion that there is no perfect method, and that an inherent trade-off between stability and spatial quality (i.e., neighborhood and distance preservation) exists."
- PENDING-REF-091-E3 | page: 8, section: extracted, quote: "5.5): If we want the projection to adhere to a certain shape, or we have some prior knowledge over the high-dimensional space and we want areas of the projections to carry a certain data-related semantic, we can easily place landmarks to drive the projection to that behavior."
- PENDING-REF-091-E4 | page: 2, section: extracted, quote: "Telea3 1Federal University of Rio Grande do Sul, Brazil 2University of Groningen, the Netherlands 3University of Utrecht, the Netherlands Abstract Projections aim to convey the relationships and similarity of high-dimensional data in a low-dimensional representation."
- PENDING-REF-091-E5 | page: 2, section: extracted, quote: "We propose two approaches that use global inﬂuences to steer projected points: Our ﬁrst method, LD-tSNE, offers similar ﬂexibility in steering dynamic projections via landmarks as known for static projections, and also reaches good quality values."
- PENDING-REF-091-E6 | page: 3, section: extracted, quote: "Tens of different projection algorithms exist for static data; detailed taxonomies of such methods, benchmarks, and qualitative and quantitative evaluations are available in a range of surveys [NA19, EMK∗19, Fod02, CG15, SVPM14, vPVdH09]."
- PENDING-REF-091-E7 | page: 10, section: extracted, quote: "Horizontal lines show average metric values over all datasets for each (method, metric class) pair. parameters – or good preset values for all datasets – by grid search, following the approach in [ EMK∗19] for static projections."
- PENDING-REF-091-E8 | page: 4, section: extracted, quote: "We propose two new guided methods for dynamic projection that use global inﬂuences (landmarks or suggested placements) to steer and stabilize the projection while still accounting for neighborhood preservation."
