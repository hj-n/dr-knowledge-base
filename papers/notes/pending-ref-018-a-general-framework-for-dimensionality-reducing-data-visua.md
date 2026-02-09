---
id: paper-2012-pending-ref-018
title: "A General Framework for Dimensionality-Reducing Data Visualization Mapping"
authors: "Kerstin Bunte, Michael Biehl, and Barbara Hammer"
venue: "Journal of Statistical Software"
year: 2012
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-018-2012-a-general-framework-for-dimensionality-reducing-data-visualization-mapping.pdf
seed_note_id: "paper-2021-quantitative-survey-dr-techniques"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- In particular, the PLS problem is to minimize the penalized weighted residual sum-of-squares, r2(θ,β,u) =ρ2(θ,β,u) +∥u∥2, (14) 4N (µ,σ 2I) distributions are called “spherical” because contours of the probability density are spheres.
- The below-diagonal panels allow us to see distortions from an elliptical shape due to nonlinearity of the traces, separately from the one-dimensional distortions caused by a poor choice of scale for the parameters.
- It also suggests framing the inference problem as a likelihood ratio test, achieved by supplying multiple ‘merMod’ objects to theanova method, as well as alternatives top values such as conﬁdence intervals.
- The absence of analytical results for null distributions of parameter estimates in complex situations (e.g., unbalanced or partially crossed designs) is a long-standing problem in mixed-model inference.

# Method Summary
- Therefore, although the package does not provide them (except via parametric bootstrapping, Section 5.1), we have provided a help page to guide users in ﬁnding appropriate methods: R> help("pvalues") Journal of Statistical Software 35 This help page provides pointers to other packages that provide machinery for calculating p values associated with ‘merMod’ objects.
- The standard simulation method (based on a ‘merMod’ object) is the basis of parametric bootstrapping (Section 5.1) and posterior predictive simulation (Section 5.2);de novosimulation based on a formula provides a ﬂexible framework for power analysis.
- Thefitted method retrieves ﬁtted values that are conditional on all of the modes of the random eﬀects; the predict method returns the same values by default, but also allows for predictions to be made conditional on diﬀerent sets of random eﬀects.
- Thus approximate methods for computing the approximate degrees of freedom fort distributions, or the denominator degrees of freedom forF statistics (Satterthwaite 1946; Kenward and Roger 1997), are at bestad hocsolutions.
- The largest change is a 26% diﬀerence in conﬁdence interval widths between proﬁle and parametric bootstrap methods for the correlation between the intercept and slope random eﬀects ({−0.54,0.98} vs. {−0.48,0.68}).
- As the number of levels is often large in practice, it is essential for speed and eﬃciency to take account of this sparsity, for example by using sparse matrix methods, when ﬁtting mixed models (Section 3.7).
- It also suggests framing the inference problem as a likelihood ratio test, achieved by supplying multiple ‘merMod’ objects to theanova method, as well as alternatives top values such as conﬁdence intervals.

# When To Use / Not Use
- Use when:
  - We have learned much about linear mixed models in the process of developinglme4, both from our own attempts to develop robust and reliable procedures and from the broad community of lme4 users; we have attempted to describe many of these lessons here.
  - Computational limitations are especially important because mixed models are commonly applied to moderately large data sets (104–106 observations).
- Avoid when:
  - The cross-product matrix in Equation 17 can be Cholesky decomposed, ) Λ⊤ θZ⊤WZ Λθ +I Λ⊤ θZ⊤WX X⊤WZ Λθ X⊤WX ] = ) Lθ 0 R⊤ ZX R⊤ X ] ) L⊤ θ RZX 0 RX ] . (18) We may use this decomposition to rewrite the penalized weighted residual sum-of-squares as r2(θ,β,u) =r2(θ) + L⊤ θ (u−µU|Y =yobs) +RZX (β− ˆβθ)  2 + RX(β− ˆβθ)  2 , (19) where we have simpliﬁed notation by writingr2(θ, ˆβθ,µU|Y =yobs) as r2(θ).
  - Therefore, although the package does not provide them (except via parametric bootstrapping, Section 5.1), we have provided a help page to guide users in ﬁnding appropriate methods: R> help("pvalues") Journal of Statistical Software 35 This help page provides pointers to other packages that provide machinery for calculating p values associated with ‘merMod’ objects.
- Failure modes:
  - Because each Zi is generated from indicator columns, its cross-product, Z⊤ i Zi is blockdiagonal consisting ofℓi diagonal blocks each of sizepi.3 Note that this means that when 2Note that the original deﬁnition of the Khatri-Rao product is more general than the deﬁnition used in the Matrix package, which is the deﬁnition we use here.

# Metrics Mentioned
- No explicit named metric was extracted from this source; combine this source with complementary DR quality checks in workflow Step 3.

# Implementation Notes
- The appropriate criterion is optimized, using one of the constrained optimization functions inR, to provide the parameter estimates.
- It is convenient to express the model in terms of arelative covariance factor, Λθ, which is aq×q matrix, depending on the variance-component parameter,θ, and generating the symmetricq×q variance-covariance matrix, Σ, according to Σθ =σ2ΛθΛ⊤ θ, (4) where σ is the same scale factor as in the conditional distribution (2).
- Computing conﬁdence intervals As described above (Section 5.1), lme4 provides conﬁdence intervals (using confint) via Wald approximations (for ﬁxed-eﬀects parameters only), likelihood proﬁling, or parametric bootstrapping (the boot.type argument selects the bootstrap conﬁdence interval type).
- While panels above the diagonal show proﬁles with respect to the original parameters (with random-eﬀects parameters on the standard deviation/correlation scale, as for all proﬁle plots), the panels below the diagonal show plots on the(ζi,ζj) scale.
- Model reformulation for improved computational stability In our initial formulation of the linear mixed model (Equations 2, 3, and 4), the covariance parameter vector,θ, appears only in the marginal distribution of the random eﬀects (Equation 3).
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-018-C1 | stance: support | summary: In particular, the PLS problem is to minimize the penalized weighted residual sum-of-squares, r2(θ,β,u) =ρ2(θ,β,u) +∥u∥2, (14) 4N (µ,σ 2I) distributions are called “spherical” because contours of the probability density are spheres. | evidence_ids: PENDING-REF-018-E1, PENDING-REF-018-E2
- CLAIM-PENDING-REF-018-C2 | stance: support | summary: Therefore, although the package does not provide them (except via parametric bootstrapping, Section 5.1), we have provided a help page to guide users in ﬁnding appropriate methods: R> help("pvalues") Journal of Statistical Software 35 This help page provides pointers to other packages that provide machinery for calculating p values associated with ‘merMod’ objects. | evidence_ids: PENDING-REF-018-E3, PENDING-REF-018-E4
- CLAIM-PENDING-REF-018-C3 | stance: support | summary: The appropriate criterion is optimized, using one of the constrained optimization functions inR, to provide the parameter estimates. | evidence_ids: PENDING-REF-018-E5, PENDING-REF-018-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 4 | relevance: high | note: contains initialization sensitivity or control-policy evidence
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-REF-018-E1 | page: 13, section: extracted, quote: "In particular, the PLS problem is to minimize the penalized weighted residual sum-of-squares, r2(θ,β,u) =ρ2(θ,β,u) +∥u∥2, (14) 4N (µ,σ 2I) distributions are called “spherical” because contours of the probability density are spheres."
- PENDING-REF-018-E2 | page: 36, section: extracted, quote: "The below-diagonal panels allow us to see distortions from an elliptical shape due to nonlinearity of the traces, separately from the one-dimensional distortions caused by a poor choice of scale for the parameters."
- PENDING-REF-018-E3 | page: 35, section: extracted, quote: "It also suggests framing the inference problem as a likelihood ratio test, achieved by supplying multiple ‘merMod’ objects to theanova method, as well as alternatives top values such as conﬁdence intervals."
- PENDING-REF-018-E4 | page: 34, section: extracted, quote: "The absence of analytical results for null distributions of parameter estimates in complex situations (e.g., unbalanced or partially crossed designs) is a long-standing problem in mixed-model inference."
- PENDING-REF-018-E5 | page: 34, section: extracted, quote: "Therefore, although the package does not provide them (except via parametric bootstrapping, Section 5.1), we have provided a help page to guide users in ﬁnding appropriate methods: R> help('pvalues') Journal of Statistical Software 35 This help page provides pointers to other packages that provide machinery for calculating p values associated with ‘merMod’ objects."
- PENDING-REF-018-E6 | page: 37, section: extracted, quote: "The standard simulation method (based on a ‘merMod’ object) is the basis of parametric bootstrapping (Section 5.1) and posterior predictive simulation (Section 5.2);de novosimulation based on a formula provides a ﬂexible framework for power analysis."
- PENDING-REF-018-E7 | page: 36, section: extracted, quote: "Thefitted method retrieves ﬁtted values that are conditional on all of the modes of the random eﬀects; the predict method returns the same values by default, but also allows for predictions to be made conditional on diﬀerent sets of random eﬀects."
- PENDING-REF-018-E8 | page: 34, section: extracted, quote: "Thus approximate methods for computing the approximate degrees of freedom fort distributions, or the denominator degrees of freedom forF statistics (Satterthwaite 1946; Kenward and Roger 1997), are at bestad hocsolutions."
