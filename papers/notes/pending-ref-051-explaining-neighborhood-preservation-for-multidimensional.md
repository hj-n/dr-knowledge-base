---
id: paper-2015-pending-ref-051
title: "Explaining Neighborhood Preservation for Multidimensional Projections"
authors: "Rafael Messias Martins, Rosane Minghim, and AC Telea"
venue: "UNKNOWN"
year: 2015
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-051-2015-explaining-neighborhood-preservation-for-multidimensional-projections.pdf
seed_note_id: "paper-2021-quantitative-survey-dr-techniques"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- Telea2 1Institute of Mathematics and Computer Science (ICMC), University of São Paulo, São Carlos, Brazil 2Johann Bernoulli Institute, University of Groningen, The Netherlands Abstract Dimensionality reduction techniques are the tools of choice for exploring high-dimensional datasets by means of low-dimensional projections.
- False neighbors are, thus, points we visually see as being close to point i in the projection, but which are in reality far from point i in the high-dimensional space; • true neighbors ={pj∈ νn k (i)∧ qj∈ ν2 k (i)} These are points which we visually ﬁnd close to point i in c⃝ The Eurographics Association 2015.
- Both types of errors in turn can signiﬁcantly affect the insights obtained on the data at hand when using the projection as a proxy to reason about the high-dimensional visual space in terms of ﬁnding and comparing clusters, outliers, and trends [VDHM97, Aup07, SvLB10, LA11, vdMH12].
- Besides information loss in the sense of not showing all original data dimensions, projections are also challenged by precision loss, in the sense of errors that affect the projected data structure.

# Method Summary
- For this, we propose several metrics to quantify the appearance of such errors in projections and introduce visualizations that allow selecting suitable scales or levels-of-detail to examine such errors, and support users in understanding and using the projection in their presence.
- Our explanatory methods are simple to implement, computationally scalable and can be easily integrated in classical scatterplot views of any projection technique, including linear [Tor65, BTB13] and non-linear ones [PNML08, vdMH08, TMN03, PSN10], in a black box fashion.
- Our method supports assessing the usefulness of a projection in terms of determining its overall quality, local errors, and how these errors should be considered when interpreting the projection to reason about the unc⃝ The Eurographics Association 2015.
- Nonlinear optimization methods iteratively search the projection parameter space to minimize the stress σ [GKN04,Sam69] using, for instance, forcebased relaxation [TMN03], similar to graph layout methods [Ead84].
- However, even state-of-the-art projection methods fail, up to various degrees, in perfectly preserving the structure of the data, expressed in terms of inter-point distances and point neighborhoods.
- This allows globally comparing projection methods [PPM ∗15, EMdS∗15], but does not show how errors are spread over the various points in a given projection.
- At the ﬁnest detail level, several methods show where in the projection Dm distance- and/or neighborhood-preservation errors occur, and how large these are.

# When To Use / Not Use
- Use when:
  - The approximation error of ANN can be thought of as a limitation, but its maximum error is user-speciﬁed, allowing a ﬁne-grained control on the tradeoff between accuracy and running time; the library also allows the error to be set to zero, in which case it reverts to an exact search.
  - Our techniques complement and extend the set of existing tools for projection exploration including aggregate error metrics, neighborhood-preservation plots, and distance-error views, thereby offering users additional ways to reason about the usefulness and usability of multidimensional projections for data analysis tasks.
- Avoid when:
  - For this, we propose several metrics to quantify the appearance of such errors in projections and introduce visualizations that allow selecting suitable scales or levels-of-detail to examine such errors, and support users in understanding and using the projection in their presence.
  - Together, these ﬁndings tell us that the border we discovered by our views is, indeed, the true border between the left and central clusters, an insight that might not be clear for the user of the projection without the investigation supported by the introduced tools.
- Failure modes:
  - Our method supports assessing the usefulness of a projection in terms of determining its overall quality, local errors, and how these errors should be considered when interpreting the projection to reason about the unc⃝ The Eurographics Association 2015.

# Metrics Mentioned
- `trustworthiness`: referenced as part of projection-quality or reliability assessment.
- `stress`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- Nonlinear optimization methods iteratively search the projection parameter space to minimize the stress σ [GKN04,Sam69] using, for instance, forcebased relaxation [TMN03], similar to graph layout methods [Ead84].
- Our explanatory methods are simple to implement, computationally scalable and can be easily integrated in classical scatterplot views of any projection technique, including linear [Tor65, BTB13] and non-linear ones [PNML08, vdMH08, TMN03, PSN10], in a black box fashion.
- Our explanatory methods are simple to implement, computationally scalable and can be easily integrated in classical scatterplot views of any projection technique, including linear [Tor65, BTB13] and non-linear ones [PNML08, vdMH08, TMN03, PSN10], in a black box fashion.
- Our method supports assessing the usefulness of a projection in terms of determining its overall quality, local errors, and how these errors should be considered when interpreting the projection to reason about the unc⃝ The Eurographics Association 2015.
- Nonlinear optimization methods iteratively search the projection parameter space to minimize the stress σ [GKN04,Sam69] using, for instance, forcebased relaxation [TMN03], similar to graph layout methods [Ead84].
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-051-C1 | stance: support | summary: Telea2 1Institute of Mathematics and Computer Science (ICMC), University of São Paulo, São Carlos, Brazil 2Johann Bernoulli Institute, University of Groningen, The Netherlands Abstract Dimensionality reduction techniques are the tools of choice for exploring high-dimensional datasets by means of low-dimensional projections. | evidence_ids: PENDING-REF-051-E1, PENDING-REF-051-E2
- CLAIM-PENDING-REF-051-C2 | stance: support | summary: For this, we propose several metrics to quantify the appearance of such errors in projections and introduce visualizations that allow selecting suitable scales or levels-of-detail to examine such errors, and support users in understanding and using the projection in their presence. | evidence_ids: PENDING-REF-051-E3, PENDING-REF-051-E4
- CLAIM-PENDING-REF-051-C3 | stance: support | summary: Nonlinear optimization methods iteratively search the projection parameter space to minimize the stress σ [GKN04,Sam69] using, for instance, forcebased relaxation [TMN03], similar to graph layout methods [Ead84]. | evidence_ids: PENDING-REF-051-E5, PENDING-REF-051-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-REF-051-E1 | page: 1, section: extracted, quote: "Telea2 1Institute of Mathematics and Computer Science (ICMC), University of São Paulo, São Carlos, Brazil 2Johann Bernoulli Institute, University of Groningen, The Netherlands Abstract Dimensionality reduction techniques are the tools of choice for exploring high-dimensional datasets by means of low-dimensional projections."
- PENDING-REF-051-E2 | page: 2, section: extracted, quote: "False neighbors are, thus, points we visually see as being close to point i in the projection, but which are in reality far from point i in the high-dimensional space; • true neighbors ={pj∈ νn k (i)∧ qj∈ ν2 k (i)} These are points which we visually ﬁnd close to point i in c⃝ The Eurographics Association 2015."
- PENDING-REF-051-E3 | page: 1, section: extracted, quote: "Both types of errors in turn can signiﬁcantly affect the insights obtained on the data at hand when using the projection as a proxy to reason about the high-dimensional visual space in terms of ﬁnding and comparing clusters, outliers, and trends [VDHM97, Aup07, SvLB10, LA11, vdMH12]."
- PENDING-REF-051-E4 | page: 1, section: extracted, quote: "Besides information loss in the sense of not showing all original data dimensions, projections are also challenged by precision loss, in the sense of errors that affect the projected data structure."
- PENDING-REF-051-E5 | page: 1, section: extracted, quote: "For this, we propose several metrics to quantify the appearance of such errors in projections and introduce visualizations that allow selecting suitable scales or levels-of-detail to examine such errors, and support users in understanding and using the projection in their presence."
- PENDING-REF-051-E6 | page: 1, section: extracted, quote: "Our explanatory methods are simple to implement, computationally scalable and can be easily integrated in classical scatterplot views of any projection technique, including linear [Tor65, BTB13] and non-linear ones [PNML08, vdMH08, TMN03, PSN10], in a black box fashion."
- PENDING-REF-051-E7 | page: 7, section: extracted, quote: "Our method supports assessing the usefulness of a projection in terms of determining its overall quality, local errors, and how these errors should be considered when interpreting the projection to reason about the unc⃝ The Eurographics Association 2015."
- PENDING-REF-051-E8 | page: 2, section: extracted, quote: "Nonlinear optimization methods iteratively search the projection parameter space to minimize the stress σ [GKN04,Sam69] using, for instance, forcebased relaxation [TMN03], similar to graph layout methods [Ead84]."
