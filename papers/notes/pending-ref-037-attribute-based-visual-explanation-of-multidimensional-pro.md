---
id: paper-2015-pending-ref-037
title: "Attribute-based Visual Explanation of Multidimensional Projections"
authors: "Renato R. O. da Silva, Paulo E. Rauber, Rafael M. Martins, Rosane Minghim, and Alexandru C. Telea"
venue: "UNKNOWN"
year: 2015
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-037-2015-attribute-based-visual-explanation-of-multidimensional-projections.pdf
seed_note_id: "paper-2019-mdp-visual-analytics-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- Explaining multidimensional projections is an important problem in visual analytics.
- We demonstrate our method on several real-world high-dimensional datasets.

# Method Summary
- We propose a visual approach to describe which dimensions contribute mostly to similarity relationships over the projection, thus explain the projection’s layout.
- This has interesting connections with methods using shaded cushions to display various types of quantitative and categorical data [TE10, BT09]; (4) testing our method for datasets having hundreds of dimensions, and adapting its heuristics and parameters to compactly and intuitively explain 2D projections of such data.
- Advantages: Our method is intuitive, easy to use, computationally efﬁcient (runs in real-time for datasets up to 10K points on a typical PC for a C++ CPU single-threaded implementation), and generic (can use any projection and/or dataset having quantitative dimensions).
- This approach works well when the data and projection can be easily and robustly separated into several clusters, and less well when there is no such clear separation.
- Such approaches explain an MP on several levels of detail, but require user interaction effort to specify where to explain the projection.
- Applications We next use our method to explain projections from three real datasets.
- Pagliosa et al. color-code the value of quality measurements on a family of projections and their interpolation, to show differences between projections vs a particular error distribution and also to provide alternative mappings between distinct projections [PPM∗15].

# When To Use / Not Use
- Use when:
  - This approach works well when the data and projection can be easily and robustly separated into several clusters, and less well when there is no such clear separation.
  - Limitations: Color-coding explanations are inherently limited to the maximum number of colors that a categorical colormap can reasonably use.
- Avoid when:
  - Advantages: Our method is intuitive, easy to use, computationally efﬁcient (runs in real-time for datasets up to 10K points on a typical PC for a C++ CPU single-threaded implementation), and generic (can use any projection and/or dataset having quantitative dimensions).
  - Given a point i, its dimension-set (used for explaining the projection around i), contains all the topranked dimensions µ j i whose rank values sum up to a value equal of just larger than a user-deﬁned small threshold value τ.
- Failure modes:
  - To illustrate this, we use a simple synthetic dataset of 3000 points randomly sampled from three faces of a 3D cube, and additionally perturbed by uniform spatial random noise of amplitude equal to 5% of the dataset’s extent.

# Metrics Mentioned
- `stress`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- The right region is split in several compact sub-regions: A 3 is a union between lines of code and lack of function cohesion; A5 adds the same dimension of A3 and also the number of function parameters; A4 also adds the number of function parameters; ﬁnally, A6 adds the metric number of public variables to its explanation.
- This has interesting connections with methods using shaded cushions to display various types of quantitative and categorical data [TE10, BT09]; (4) testing our method for datasets having hundreds of dimensions, and adapting its heuristics and parameters to compactly and intuitively explain 2D projections of such data.
- The partition of the 2D projection space into sameexplanation regions occurs automatically and implicitly, without the need to select or set any clustering parameters.
- While MP techniques grow more precise and scalable, they still do not show how the original dimensions (attributes) inﬂuence the projection’s layout.
- e 2D projection space into sameexplanation regions occurs automatically and implicitly, without the need to select or set any clustering parameters.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-037-C1 | stance: support | summary: Explaining multidimensional projections is an important problem in visual analytics. | evidence_ids: PENDING-REF-037-E1, PENDING-REF-037-E2
- CLAIM-PENDING-REF-037-C2 | stance: support | summary: We propose a visual approach to describe which dimensions contribute mostly to similarity relationships over the projection, thus explain the projection’s layout. | evidence_ids: PENDING-REF-037-E3, PENDING-REF-037-E4
- CLAIM-PENDING-REF-037-C3 | stance: support | summary: The right region is split in several compact sub-regions: A 3 is a union between lines of code and lack of function cohesion; A5 adds the same dimension of A3 and also the number of function parameters; A4 also adds the number of function parameters; ﬁnally, A6 adds the metric number of public variables to its explanation. | evidence_ids: PENDING-REF-037-E5, PENDING-REF-037-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-REF-037-E1 | page: 2, section: extracted, quote: "Explaining multidimensional projections is an important problem in visual analytics."
- PENDING-REF-037-E2 | page: 2, section: extracted, quote: "We demonstrate our method on several real-world high-dimensional datasets."
- PENDING-REF-037-E3 | page: 2, section: extracted, quote: "We propose a visual approach to describe which dimensions contribute mostly to similarity relationships over the projection, thus explain the projection’s layout."
- PENDING-REF-037-E4 | page: 5, section: extracted, quote: "This has interesting connections with methods using shaded cushions to display various types of quantitative and categorical data [TE10, BT09]; (4) testing our method for datasets having hundreds of dimensions, and adapting its heuristics and parameters to compactly and intuitively explain 2D projections of such data."
- PENDING-REF-037-E5 | page: 4, section: extracted, quote: "Advantages: Our method is intuitive, easy to use, computationally efﬁcient (runs in real-time for datasets up to 10K points on a typical PC for a C++ CPU single-threaded implementation), and generic (can use any projection and/or dataset having quantitative dimensions)."
- PENDING-REF-037-E6 | page: 3, section: extracted, quote: "This approach works well when the data and projection can be easily and robustly separated into several clusters, and less well when there is no such clear separation."
- PENDING-REF-037-E7 | page: 2, section: extracted, quote: "Such approaches explain an MP on several levels of detail, but require user interaction effort to specify where to explain the projection."
- PENDING-REF-037-E8 | page: 4, section: extracted, quote: "Applications We next use our method to explain projections from three real datasets."
