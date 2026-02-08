---
id: paper-2020-pending-ref-056
title: "Selecting and Sharing Multidimensional Projection Algorithms: A Practical View"
authors: "Mateus Espadoto, Eduardo Faccin Vernier, and Alexandru Telea"
venue: "UNKNOWN"
year: 2020
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-056-2020-selecting-and-sharing-multidimensional-projection-algorithms-a-practical-view.pdf
seed_note_id: "paper-2024-large-scale-text-spatialization"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- Importantly, by a benchmark, we do not understand here just a ‘passive’ collection of high-dimensional datasets to battle-test DR techniques, but rather a runnable software system that lets one select datasets, DR technique implementations (and their parameter values), metrics, execute them, and visually inspect the results in an easy and highly automated way.
- Conclusions We presented an overview of the challenges that exist in the process of selecting and sharing DR techniques from the point of view of different audiences, practitioners and researchers, where we described the typical workﬂows used in their processes.
- Discussion Summarizing, we see a number of open challenges to the selection and sharing of DR algorithms that, jointly, create a gap between the state-of-the art work in DR literature and practical realities in the ﬁeld, as follows.
- In this paper, we try to address those issues systematically by analyzing recent surveys in the area, identifying the methods and tools used, and discussing challenges, limitations, and ideas for further work.

# Method Summary
- Telea / Selecting and Sharing Multidimensional Projection Algorithms: A Practical View accommodate most, if not all, concrete instantiations thereof that we know of from the DR literature and practice.
- Telea / Selecting and Sharing Multidimensional Projection Algorithms: A Practical View dataset D, by preserving various aspects thereof in P(D), e.g., interpoint distances or point neighborhoods.
- In particular, we propose an architecture for a benchmark for DR evaluation that is generic and extensible in terms of datasets, DR algorithms, quality metrics, and visualizations.
- Wischgoll (Editors) Selecting and Sharing Multidimensional Projection Algorithms: A Practical View M.
- Telea / Selecting and Sharing Multidimensional Projection Algorithms: A Practical View [vH08].
- Telea / Selecting and Sharing Multidimensional Projection Algorithms: A Practical View A.
- Abstract Multidimensional Projection techniques are often used by data analysts for exploring multivariate datasets, but the task of selecting the best technique for the job is not trivial, as there are many candidates and the reasons for picking one over another are usually unclear.

# When To Use / Not Use
- Use when:
  - While frameworks best support QP, ﬁnding which implementations (in which frameworks) best match a practitioner’s set of requirements still requires signiﬁcant manual trial-and-error testing of the DR implementations they provide.
  - In this paper, we try to address those issues systematically by analyzing recent surveys in the area, identifying the methods and tools used, and discussing challenges, limitations, and ideas for further work.
- Avoid when:
  - Such aspects can be usually inferred from the technique’s description; • non-functional requirements describe properties of implementations of DR techniques, e.g. ease of use, documentation, portability, third-party software components and programming language needed, and interoperability with other toolkits.
  - We believe the visualization community would beneﬁt from a more integrated, well-documented benchmark framework, where new techniques, datasets, and metrics could be easily added by the user with minimal programming, and with the capability of integration with existing visualization tools.
- Failure modes:
  - Conclusions We presented an overview of the challenges that exist in the process of selecting and sharing DR techniques from the point of view of different audiences, practitioners and researchers, where we described the typical workﬂows used in their processes.

# Metrics Mentioned
- `continuity`: referenced as part of projection-quality or reliability assessment.
- `stress`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- Importantly, by a benchmark, we do not understand here just a ‘passive’ collection of high-dimensional datasets to battle-test DR techniques, but rather a runnable software system that lets one select datasets, DR technique implementations (and their parameter values), metrics, execute them, and visually inspect the results in an easy and highly automated way.
- We believe the two-step API of scikitlearn (create object with parameters, call ﬁt_transform()) to be much simpler to understand for the average user than Tapkee’s method of chaining with globally-namespaced, non-speciﬁc keywords.
- Datasets d from a databaseD are projected in turn by several DR technique implementations p from a DR technique collectionP, using several parameter values params, yielding corresponding 2D scatterplotsd2D = p(d, params).
- Even in the cases where the library is well documented, we often found not enough details on the role of each parameter in the ﬁnal quality of the projection, and even less on the interaction between parameters.
- Extensibility and genericity: The above architecture is easily extensible: Adding new datasets, metrics, DR techniques, or parameter grids implies simply adding entries to the respective dictionaries.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-056-C1 | stance: support | summary: Importantly, by a benchmark, we do not understand here just a ‘passive’ collection of high-dimensional datasets to battle-test DR techniques, but rather a runnable software system that lets one select datasets, DR technique implementations (and their parameter values), metrics, execute them, and visually inspect the results in an easy and highly automated way. | evidence_ids: PENDING-REF-056-E1, PENDING-REF-056-E2
- CLAIM-PENDING-REF-056-C2 | stance: support | summary: Telea / Selecting and Sharing Multidimensional Projection Algorithms: A Practical View accommodate most, if not all, concrete instantiations thereof that we know of from the DR literature and practice. | evidence_ids: PENDING-REF-056-E3, PENDING-REF-056-E4
- CLAIM-PENDING-REF-056-C3 | stance: support | summary: Importantly, by a benchmark, we do not understand here just a ‘passive’ collection of high-dimensional datasets to battle-test DR techniques, but rather a runnable software system that lets one select datasets, DR technique implementations (and their parameter values), metrics, execute them, and visually inspect the results in an easy and highly automated way. | evidence_ids: PENDING-REF-056-E5, PENDING-REF-056-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-REF-056-E1 | page: 5, section: extracted, quote: "Importantly, by a benchmark, we do not understand here just a ‘passive’ collection of high-dimensional datasets to battle-test DR techniques, but rather a runnable software system that lets one select datasets, DR technique implementations (and their parameter values), metrics, execute them, and visually inspect the results in an easy and highly automated way."
- PENDING-REF-056-E2 | page: 6, section: extracted, quote: "Conclusions We presented an overview of the challenges that exist in the process of selecting and sharing DR techniques from the point of view of different audiences, practitioners and researchers, where we described the typical workﬂows used in their processes."
- PENDING-REF-056-E3 | page: 6, section: extracted, quote: "Discussion Summarizing, we see a number of open challenges to the selection and sharing of DR algorithms that, jointly, create a gap between the state-of-the art work in DR literature and practical realities in the ﬁeld, as follows."
- PENDING-REF-056-E4 | page: 1, section: extracted, quote: "In this paper, we try to address those issues systematically by analyzing recent surveys in the area, identifying the methods and tools used, and discussing challenges, limitations, and ideas for further work."
- PENDING-REF-056-E5 | page: 2, section: extracted, quote: "Telea / Selecting and Sharing Multidimensional Projection Algorithms: A Practical View accommodate most, if not all, concrete instantiations thereof that we know of from the DR literature and practice."
- PENDING-REF-056-E6 | page: 2, section: extracted, quote: "Telea / Selecting and Sharing Multidimensional Projection Algorithms: A Practical View dataset D, by preserving various aspects thereof in P(D), e.g., interpoint distances or point neighborhoods."
- PENDING-REF-056-E7 | page: 1, section: extracted, quote: "In particular, we propose an architecture for a benchmark for DR evaluation that is generic and extensible in terms of datasets, DR algorithms, quality metrics, and visualizations."
- PENDING-REF-056-E8 | page: 1, section: extracted, quote: "Wischgoll (Editors) Selecting and Sharing Multidimensional Projection Algorithms: A Practical View M."
