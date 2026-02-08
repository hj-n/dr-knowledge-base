---
id: paper-2026-pending-extra-friedman-exploratory
title: "Friedman-ExploratoryProjectionPursuit-1987"
authors: "Exploratory Projection Pursuit"
venue: "UNKNOWN"
year: 1987
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/Friedman-ExploratoryProjectionPursuit-1987.pdf
seed_note_id: "paper-2025-jeon-reliable-va-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- This problem is difficult owing to high dimensionality (of the haystack) and the small cardinality of the needle.
- This content downloaded from 58.121.83.133 on Sun, 08 Feb 2026 09:13:04 UTC All use subject to https://about.jstor.org/terms 260 Journal of the American Statistical Association, March 1987 other hand, it finds several pseudomaxima (which are subsequently deflated by structure removal) before finding the real structured projection, this is an indication of some difficulty.
- Since (by design) the projection pursuit algorithm has some difficulty at these (threshold) sample sizes, a measure of that difficulty is the iteration number (projection pursuit followed by structure removal) at which the algorithm discovers the known structure as opposed to spurious structure (pseudomaxima) induced by the small sample size and/or high dimensionality.
- 2a, 3a, 4a) is a smaller sample size at which the algorithm seems to be having some difficulty and thus represents a minimal cardinality for finding the true structured projection at the corresponding dimensions.

# Method Summary
- FRIEDMAN* A new projection pursuit algorithm for exploring multivariate data is presented that has both statistical and computational advantages over previous methods.
- This projection pursuit algorithm has potential advantages over other dimensionality reduction methods that are commonly used for data exploration.
- EXAMPLES In this section we present the results of running the oneand two-dimensional projection pursuit algorithms on data.
- As reThis content downloaded from 58.121.83.133 on Sun, 08 Feb 2026 09:13:04 UTC All use subject to https://about.jstor.org/terms Friedman: Exploratory Projection Pursuit 257 marked earlier, the covariance structure (linear associations) often does not align with the nonlinear structure (clustering, nonlinear relationships) that we are seeking with our projection pursuit algorithm.
- Since (by design) the projection pursuit algorithm has some difficulty at these (threshold) sample sizes, a measure of that difficulty is the iteration number (projection pursuit followed by structure removal) at which the algorithm discovers the known structure as opposed to spurious structure (pseudomaxima) induced by the small sample size and/or high dimensionality.
- They termed this method "projection pursuit." Since all (density) estimation is performed in a univariate (or bivariate) setting this method has the potential of overcoming the "curse of dimensionality" (Bellman 1961) that afflicts such nonlinear methods as parametric mapping (multidimensional scaling) and cluster analysis that are based on interpoint ?
- The statistical power of the method is reflected in its ability (for a given sample size and data dimension) to find substantive maxima of This content downloaded from 58.121.83.133 on Sun, 08 Feb 2026 09:13:04 UTC All use subject to https://about.jstor.org/terms 256 Journal of the American Statistical Association, March 1987 the projection index.

# When To Use / Not Use
- Use when:
  - In a two-dimensional projection pursuit the visual impact of the projected data density is insensitive to a particular orientation (within the plane) of the orthogonal axes used to define the solution plane.
  - Nevertheless it seems sensible to use robust sphering when possible.
- Avoid when:
  - This content downloaded from 58.121.83.133 on Sun, 08 Feb 2026 09:13:04 UTC All use subject to https://about.jstor.org/terms Friedman: Exploratory Projection Pursuit 259 7.1 Single Clustered Projection in Several Dimensionalities The purpose of this study is to get an idea of how the sample size requirements for finding a single structured projection increase with the dimensionality of the data sample.
  - As reThis content downloaded from 58.121.83.133 on Sun, 08 Feb 2026 09:13:04 UTC All use subject to https://about.jstor.org/terms Friedman: Exploratory Projection Pursuit 257 marked earlier, the covariance structure (linear associations) often does not align with the nonlinear structure (clustering, nonlinear relationships) that we are seeking with our projection pursuit algorithm.
- Failure modes:
  - The coefficients are given by aj= 2 J| P1(R)pR(R) dR - 2 [P() This content downloaded from 58.121.83.133 on Sun, 08 Feb 2026 09:13:04 UTC All use subject to https://about.jstor.org/terms 252 Journal of the American Statistical Association, March 1987 so that 3 p2(R) dR - = (2j + 1)E2[Pj(R)JI2. (8)-1 3~~~~~=1 For a uniform distribution U(- 1, 1), E[Pj(R)J = 0 for j >0.

# Metrics Mentioned
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- The computational expense would be somewhat greater owing to the increased complexity of the product Legendre polynomial expansion and the increased number of optimization parameters.
- KEY WORDS: Exploratory data analysis; Multivariate analysis; Density estimation; Data mapping; Statistical graphics; Multiparameter numerical optimization.
- Since the projection index serves as the objective function for a multiparameter optimization, its computational properties are crucial.
- This index was then maximized (via numerical optimization) with respect to the parameters defining the projections.
- In addition, the optimization is with respect to twice as many parameters.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-EXTRA-C1 | stance: support | summary: This problem is difficult owing to high dimensionality (of the haystack) and the small cardinality of the needle. | evidence_ids: PENDING-EXTRA-E1, PENDING-EXTRA-E2
- CLAIM-PENDING-EXTRA-C2 | stance: support | summary: FRIEDMAN* A new projection pursuit algorithm for exploring multivariate data is presented that has both statistical and computational advantages over previous methods. | evidence_ids: PENDING-EXTRA-E3, PENDING-EXTRA-E4
- CLAIM-PENDING-EXTRA-C3 | stance: support | summary: The computational expense would be somewhat greater owing to the increased complexity of the product Legendre polynomial expansion and the increased number of optimization parameters. | evidence_ids: PENDING-EXTRA-E5, PENDING-EXTRA-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-EXTRA-E1 | page: 13, section: extracted, quote: "This problem is difficult owing to high dimensionality (of the haystack) and the small cardinality of the needle."
- PENDING-EXTRA-E2 | page: 1, section: extracted, quote: "This content downloaded from 58.121.83.133 on Sun, 08 Feb 2026 09:13:04 UTC All use subject to https://about.jstor.org/terms 260 Journal of the American Statistical Association, March 1987 other hand, it finds several pseudomaxima (which are subsequently deflated by structure removal) before finding the real structured projection, this is an indication of some difficulty."
- PENDING-EXTRA-E3 | page: 12, section: extracted, quote: "Since (by design) the projection pursuit algorithm has some difficulty at these (threshold) sample sizes, a measure of that difficulty is the iteration number (projection pursuit followed by structure removal) at which the algorithm discovers the known structure as opposed to spurious structure (pseudomaxima) induced by the small sample size and/or high dimensionality."
- PENDING-EXTRA-E4 | page: 13, section: extracted, quote: "2a, 3a, 4a) is a smaller sample size at which the algorithm seems to be having some difficulty and thus represents a minimal cardinality for finding the true structured projection at the corresponding dimensions."
- PENDING-EXTRA-E5 | page: 2, section: extracted, quote: "FRIEDMAN* A new projection pursuit algorithm for exploring multivariate data is presented that has both statistical and computational advantages over previous methods."
- PENDING-EXTRA-E6 | page: 2, section: extracted, quote: "This projection pursuit algorithm has potential advantages over other dimensionality reduction methods that are commonly used for data exploration."
- PENDING-EXTRA-E7 | page: 11, section: extracted, quote: "EXAMPLES In this section we present the results of running the oneand two-dimensional projection pursuit algorithms on data."
- PENDING-EXTRA-E8 | page: 9, section: extracted, quote: "As reThis content downloaded from 58.121.83.133 on Sun, 08 Feb 2026 09:13:04 UTC All use subject to https://about.jstor.org/terms Friedman: Exploratory Projection Pursuit 257 marked earlier, the covariance structure (linear associations) often does not align with the nonlinear structure (clustering, nonlinear relationships) that we are seeking with our projection pursuit algorithm."
