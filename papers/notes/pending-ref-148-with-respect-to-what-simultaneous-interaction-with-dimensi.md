---
id: paper-2020-pending-ref-148
title: "With Respect to What? Simultaneous Interaction with Dimension Reduction and Clustering Projections"
authors: "John Wenskovitch, Michelle Dowling, and Chris North"
venue: "The Annals of Statistics"
year: 2020
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-148-2020-with-respect-to-what-simultaneous-interaction-with-dimension-reduction-and-clustering.pdf
seed_note_id: "paper-2025-jeon-reliable-va-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- The Stagewise procedure has its potential generality as an a dvantage over LARS and Lasso: it is easy to deﬁne forward Stagewise methods for a wide variety of nonlinear ﬁtting problems, as in Hastie, Tibshirani and Friedman [(2001), Chapter 10, which begins with a Stagewise analysis of “boo sting”].
- Since one-at-a-time computations, perhaps with some added y jitter, apply to all practical situations, the LARS algorithm described in Section 7 is not equipped to handle many-at-a-time problems.

# Method Summary
- In this case the current correlations ( 1.6) depend only on the projection ¯y2 of y into the linear space L(X) spanned by x1 and x2, c( ˆµ) = X ′(y − ˆµ) = X ′(¯y2 − ˆµ).(2.1) The algorithm begins at ˆµ0 = 0 [remembering that the response has had its mean subtracted oﬀ, as in ( 1.1)].
- Besides improved computational eﬃciency, these rel ationships elucidate the methods’ rationale: all three algorithms can be vie wed as moderately greedy forward stepwise procedures whose forward pro gress is determined by compromise among the currently most correlated covariates.
- The geometry of the algorithm, described in Section 2, suggests the name “Least Angle Regression.” It then happens that this same geometry applies to ano ther, seemingly quite diﬀerent, selection method called the Lasso [ Tibshirani (1996)].
- It closely parallels the homotopy method in the papers by Osborne, Presnell and Turlach ( 2000a, b), though the LARS approach is somewhat more direct.
- Least Angle Regression (LARS), a new model selection algorithm, is a useful and less greedy version of traditional forward selection methods.
- The LARS algorithm in the case of m = 2 covariates; ¯y2 is the projection of y into L(x1, x2).
- 2, 407–451 DOI: 10.1214/009053604000000067 c⃝ Institute of Mathematical Statistics , 2004 LEAST ANGLE REGRESSION By Bradley Efron 1, Trevor Hastie 2, Iain Johnstone 3 and Robert Tibshirani 4 Stanford University The purpose of model selection algorithms such as All Subsets , Forward Selection and Backward Elimination is to choose a linear model on the basis of the same set of data to which the model wil l be applied.

# When To Use / Not Use
- Use when:
  - Automatic model-building algorithms are familiar, and sometimes notorious, in the linear model literature: Forwa rd Selection, Backward Elimination, All Subsets regression and various combi nations are used to automatically produce “good” linear models for predicti ng a response y on the basis of some measured covariates x1, x 2, . . . , x m.
  - In this case LARS terminates at the saturated least squares ﬁ t after n − 1 variables have entered the active set [at a cost of O(n3) operations]. (This number is n − 1 rather than n, because the columns of X have been mean centered, and hence it has row-rank n − 1.) We make a few more remarks about the m ≫ n case in the lasso state: 1.
- Avoid when:
  - The Lasso chooses ˆβ by minimizing S(ˆβ) subject to a bound t on T (ˆβ), Lasso: minimize S(ˆβ) subject to T (ˆβ) ≤ t.(1.5) Quadratic programming techniques can be used to solve ( 1.5) though we will present an easier method here, closely related to the “homot opy method” of Osborne, Presnell and Turlach (2000a).
  - Hastie, Tibshirani and Friedman (2001) noted the the striking similarity between Forward Stagewise regression and the Lasso, and con jectured that this may help explain the success of the Forward Stagewise pr ocess used in least squares boosting.
- Failure modes:
  - With many correlated variables, the stagewise version can take many more steps than LARS because of frequen t dropping and adding of variables, increasing the computations by a fa ctor up to 5 or more in extreme cases.

# Metrics Mentioned
- `continuity`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- The computations can be reduced further by recognizing that the inner products above can be updated at each iteration using the cro ss-product matrix X ′X and the current directions.
- For the stagewise modiﬁcation of LARS, we need to check at each iteration that the components o f w are 40 EFRON, HASTIE, JOHNSTONE AND TIBSHIRANI all positive.
- After k steps this results in a set of predictors xj1, x j2, . . . , x jk that are then used in the usual way to construct a k-parameter linear model.
- Then we update ˆy to ˆy + ε · t1, r to y − ˆy and continue for many iterations.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-148-C1 | stance: support | summary: The Stagewise procedure has its potential generality as an a dvantage over LARS and Lasso: it is easy to deﬁne forward Stagewise methods for a wide variety of nonlinear ﬁtting problems, as in Hastie, Tibshirani and Friedman [(2001), Chapter 10, which begins with a Stagewise analysis of “boo sting”]. | evidence_ids: PENDING-REF-148-E1, PENDING-REF-148-E2
- CLAIM-PENDING-REF-148-C2 | stance: support | summary: In this case the current correlations ( 1.6) depend only on the projection ¯y2 of y into the linear space L(X) spanned by x1 and x2, c( ˆµ) = X ′(y − ˆµ) = X ′(¯y2 − ˆµ).(2.1) The algorithm begins at ˆµ0 = 0 [remembering that the response has had its mean subtracted oﬀ, as in ( 1.1)]. | evidence_ids: PENDING-REF-148-E3, PENDING-REF-148-E4
- CLAIM-PENDING-REF-148-C3 | stance: support | summary: The computations can be reduced further by recognizing that the inner products above can be updated at each iteration using the cro ss-product matrix X ′X and the current directions. | evidence_ids: PENDING-REF-148-E5, PENDING-REF-148-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance
- step: 6 | relevance: high | note: guides reliable interpretation of projected views

# Evidence
- PENDING-REF-148-E1 | page: 38, section: extracted, quote: "The Stagewise procedure has its potential generality as an a dvantage over LARS and Lasso: it is easy to deﬁne forward Stagewise methods for a wide variety of nonlinear ﬁtting problems, as in Hastie, Tibshirani and Friedman [(2001), Chapter 10, which begins with a Stagewise analysis of “boo sting”]."
- PENDING-REF-148-E2 | page: 34, section: extracted, quote: "Since one-at-a-time computations, perhaps with some added y jitter, apply to all practical situations, the LARS algorithm described in Section 7 is not equipped to handle many-at-a-time problems."
- PENDING-REF-148-E3 | page: 7, section: extracted, quote: "In this case the current correlations ( 1.6) depend only on the projection ¯y2 of y into the linear space L(X) spanned by x1 and x2, c( ˆµ) = X ′(y − ˆµ) = X ′(¯y2 − ˆµ).(2.1) The algorithm begins at ˆµ0 = 0 [remembering that the response has had its mean subtracted oﬀ, as in ( 1.1)]."
- PENDING-REF-148-E4 | page: 11, section: extracted, quote: "Besides improved computational eﬃciency, these rel ationships elucidate the methods’ rationale: all three algorithms can be vie wed as moderately greedy forward stepwise procedures whose forward pro gress is determined by compromise among the currently most correlated covariates."
- PENDING-REF-148-E5 | page: 2, section: extracted, quote: "The geometry of the algorithm, described in Section 2, suggests the name “Least Angle Regression.” It then happens that this same geometry applies to ano ther, seemingly quite diﬀerent, selection method called the Lasso [ Tibshirani (1996)]."
- PENDING-REF-148-E6 | page: 11, section: extracted, quote: "It closely parallels the homotopy method in the papers by Osborne, Presnell and Turlach ( 2000a, b), though the LARS approach is somewhat more direct."
- PENDING-REF-148-E7 | page: 1, section: extracted, quote: "Least Angle Regression (LARS), a new model selection algorithm, is a useful and less greedy version of traditional forward selection methods."
- PENDING-REF-148-E8 | page: 6, section: extracted, quote: "The LARS algorithm in the case of m = 2 covariates; ¯y2 is the projection of y into L(x1, x2)."
