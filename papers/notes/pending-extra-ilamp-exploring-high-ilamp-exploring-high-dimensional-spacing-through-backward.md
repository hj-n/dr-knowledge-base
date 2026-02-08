---
id: paper-2026-pending-extra-ilamp-exploring-high
title: "iLAMP: Exploring high-dimensional spacing through backward multidimensional projection"
authors: "Elisa Portes dos Santos Amorim, Emilio Vital Brazil, Joel Daniels, Paulo Joia, Luis Gustavo Nonato, Mario Costa Sousa"
venue: "2012 IEEE Conference on Visual Analytics Science and Technology (VAST)"
year: 2012
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/iLAMP_Exploring_high-dimensional_spacing_through_backward_multidimensional_projection.pdf
seed_note_id: "paper-2021-quantitative-survey-dr-techniques"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- Most problems of these and other ﬁelds can be seen as a system whose output depends on a set of parameters which can be concatenated so as to form high-dimensional instances.
- Points are iteratively relaxed within the visual space to reduce distortions in relative distances between local neighbors as they are mapped from the high-dimensional space.
- An informed decision regarding the iLAMP-neighborhood type (lowor high-dimensional) can be made in order to reduce or prevent distortions in the iLAMP-generated points.
- We present an application scenario where iLAMP is used as an exploration tool for high-dimensional parameter spaces governing optimization problems (Section 5).

# Method Summary
- In this paper, we present an inverse linear afﬁne multidimensional projection , coined iLAMP, that enables a novel interactive exploration technique for multidimensional data. iLAMP operates in reverse to traditional projection methods by mapping low-dimensional information into a highdimensional space.
- To summarize, in this work we presented the iLAMP method, a novel approach to explore high-dimensional data.
- The method builds upon the recently proposed MP technique called LAMP [25] to deﬁne afﬁne mappings from the visual to the high-dimensional space (Section 3). • User-driven High Dimensional Space Exploration: iLAMP allows the user to extrapolate existing data in an interactive manner, using visual feedback provided by the projection to generate new data that helps to further explore parameter spaces.
- Instances colored according to optimization function value. (1) Initial data given as input to LAMP; (2) Projection (3) User input passed to iLAMP; (4) New high-dimensional samples; (5) New data is passed as argument to the optimization method; (6) Optimization result incorporated to the dataset.
- In contrast, the iLAMP method proposed in this paper, enables interactive visual exploration of the projected space as well as the backward projection to extrapolate data that could be, creating a robust and fast framework for visual exploration and analysis of high-dimensional data.
- To the best of our knowledge, the methodology presented in this paper is the ﬁrst one to enable a coherent connection between visual representation given by a multidimensional projection technique and interactive exploration/sampling of the high-dimensional data space.
- The complexity of the iLAMP algorithm depends only on the number of neighbors k and in the dimensionality of the original data, as the calculation of the closest neighbors to point p can be accomplished using efﬁcient methods, such as quadtrees.

# When To Use / Not Use
- Use when:
  - However, spectral decomposition lacks a ﬂexibility that would enable user interactions, limiting application of such techniques in visual exploration frameworks.
  - A recent LSP-based interactive system [20] avoids the computational complexity of the control point distribution by relying on user inputs.
- Avoid when:
  - However, dense projections, due to few control points, causes the proposed system to be sensitive during the painting sessions.
  - The reported distances rely on the best back-projection solution found amongst the different iLAMP neighborhood sizes used.
- Failure modes:
  - The method builds upon the recently proposed MP technique called LAMP [25] to deﬁne afﬁne mappings from the visual to the high-dimensional space (Section 3). • User-driven High Dimensional Space Exploration: iLAMP allows the user to extrapolate existing data in an interactive manner, using visual feedback provided by the projection to generate new data that helps to further explore parameter spaces.

# Metrics Mentioned
- `stress`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- Moreover, the application presented on Section 5 indicates that iLAMP can provide a good alternative for including the user knowledge into parameter space exploration of optimization problems, a process usually accomplished with automatic methods.
- Moreover, the proposed methodology is employed in an optimization-oriented application whose goal is to ﬁgure out the location of local minima as well as to explore regions of the parameter space not visited by the optimization algorithm.
- 5 E XPLORING PARAMETER SPACES IN OPTIMIZATION PROBLEMS In this section we present an application in which the user expertise is incorporated into the optimization process by iLAMP.
- We present an application scenario where iLAMP is used as an exploration tool for high-dimensional parameter spaces governing optimization problems (Section 5).
- The method builds upon the recently proposed MP technique called LAMP [25] to deﬁne afﬁne mappings from the visual to the high-dimensional space (Section 3). • User-driven High Dimensional Space Exploration: iLAMP allows the user to extrapolate existing data in an interactive manner, using visual feedback provided by the projection to generate new data that helps to further explore parameter spaces.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-EXTRA-C1 | stance: support | summary: Most problems of these and other ﬁelds can be seen as a system whose output depends on a set of parameters which can be concatenated so as to form high-dimensional instances. | evidence_ids: PENDING-EXTRA-E1, PENDING-EXTRA-E2
- CLAIM-PENDING-EXTRA-C2 | stance: support | summary: In this paper, we present an inverse linear afﬁne multidimensional projection , coined iLAMP, that enables a novel interactive exploration technique for multidimensional data. iLAMP operates in reverse to traditional projection methods by mapping low-dimensional information into a highdimensional space. | evidence_ids: PENDING-EXTRA-E3, PENDING-EXTRA-E4
- CLAIM-PENDING-EXTRA-C3 | stance: support | summary: Moreover, the application presented on Section 5 indicates that iLAMP can provide a good alternative for including the user knowledge into parameter space exploration of optimization problems, a process usually accomplished with automatic methods. | evidence_ids: PENDING-EXTRA-E5, PENDING-EXTRA-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 4 | relevance: high | note: contains initialization sensitivity or control-policy evidence

# Evidence
- PENDING-EXTRA-E1 | page: 1, section: extracted, quote: "Most problems of these and other ﬁelds can be seen as a system whose output depends on a set of parameters which can be concatenated so as to form high-dimensional instances."
- PENDING-EXTRA-E2 | page: 2, section: extracted, quote: "Points are iteratively relaxed within the visual space to reduce distortions in relative distances between local neighbors as they are mapped from the high-dimensional space."
- PENDING-EXTRA-E3 | page: 5, section: extracted, quote: "An informed decision regarding the iLAMP-neighborhood type (lowor high-dimensional) can be made in order to reduce or prevent distortions in the iLAMP-generated points."
- PENDING-EXTRA-E4 | page: 2, section: extracted, quote: "We present an application scenario where iLAMP is used as an exploration tool for high-dimensional parameter spaces governing optimization problems (Section 5)."
- PENDING-EXTRA-E5 | page: 1, section: extracted, quote: "In this paper, we present an inverse linear afﬁne multidimensional projection , coined iLAMP, that enables a novel interactive exploration technique for multidimensional data. iLAMP operates in reverse to traditional projection methods by mapping low-dimensional information into a highdimensional space."
- PENDING-EXTRA-E6 | page: 8, section: extracted, quote: "To summarize, in this work we presented the iLAMP method, a novel approach to explore high-dimensional data."
- PENDING-EXTRA-E7 | page: 2, section: extracted, quote: "The method builds upon the recently proposed MP technique called LAMP [25] to deﬁne afﬁne mappings from the visual to the high-dimensional space (Section 3). • User-driven High Dimensional Space Exploration: iLAMP allows the user to extrapolate existing data in an interactive manner, using visual feedback provided by the projection to generate new data that helps to further explore parameter spaces."
- PENDING-EXTRA-E8 | page: 7, section: extracted, quote: "Instances colored according to optimization function value. (1) Initial data given as input to LAMP; (2) Projection (3) User input passed to iLAMP; (4) New high-dimensional samples; (5) New data is passed as argument to the optimization method; (6) Optimization result incorporated to the dataset."
