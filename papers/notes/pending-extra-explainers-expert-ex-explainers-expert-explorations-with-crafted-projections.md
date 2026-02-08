---
id: paper-2026-pending-extra-explainers-expert-ex
title: "Explainers: Expert Explorations with Crafted Projections"
authors: "Michael Gleicher"
venue: "IEEE Transactions on Visualization and Computer Graphics"
year: 2013
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/Explainers_Expert_Explorations_with_Crafted_Projections.pdf
seed_note_id: "paper-2025-critical-analysis-dr-four-domains"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- For information on obtaining reprints of this article, please send e-mail to: tvcg@computer.org. to the exploration of high-dimensional spaces that allows a viewer to create sets of projection functions that deﬁne dimensions that are meaningful to them, have useful relationships with the variables, and work together to provide diversity or agreement as necessary.
- Explainers: Expert Explorations with Crafted Projections Michael Gleicher, Member, IEEE Abstract—This paper introduces an approach to exploration and discovery in high-dimensional data that incorporates a user’s knowledge and questions to craft sets of projection functions meaningful to them.
- While such an approach may need to solve a very large number of SVM problems (to determine the weights for each combination of variables), each of these problems is very small (just a few variables) and can be solved quickly.
- 4.2 Feature Selection The problem of ﬁnding w can be viewed as having two parts: selecting which weights will be non-zero (e.g. which variables will participate), and then determining the values of these weights.

# Method Summary
- Central to our approach is to consider the different roles that projection functions may serve in exploration, the qualities that projection functions need to have in order to serve these roles, and the kinds of methods available to create and assess the functions.
- Unlike methods that select axis-parallel projections, our approach can use more complex functions to provide ﬂexibility in the kinds of dimensions created, allowing it to represent user-deﬁned properties.
- A related approach is to apply a projection pursuit style algorithm: computing a linear function, factoring it out of the data matrix, and then repeating the process on the rank-reduced matrix.
- Explainers: Expert Explorations with Crafted Projections Michael Gleicher, Member, IEEE Abstract—This paper introduces an approach to exploration and discovery in high-dimensional data that incorporates a user’s knowledge and questions to craft sets of projection functions meaningful to them.
- By generating projection functions that align with user speciﬁcations, and by considering tradeoffs in correctness, simplicity, and diversity, our approach creates derived dimensions that serve to both organize the data, as well as show its connection to properties of interest.
- The user can mark the cities in the U.S. and the system generates derived dimensions that correspond to “Americanness.” Given the speciﬁed binary predicate, the methods of this paper can generate a set of projection functions that are aligned with it.
- Abstract—This paper introduces an approach to exploration and discovery in high-dimensional data that incorporates a user’s knowledge and questions to craft sets of projection functions meaningful to them.

# When To Use / Not Use
- Use when:
  - Computing all these functions (up to 7 variables) takes about as long as the fully exhaustive search, but has the advantage that it also produces the best classiﬁers with smaller numbers of variables in the process, allowing the user to make a decision as to how much of a tradeoff to make between correctness and simplicity.
  - To provide control over the tradeoff between simplicity (in terms of sparsity) and correctness, we use the different results of feature selection, and compute the weights that achieve the best correctness given each set of variables.
- Avoid when:
  - We generate a collection of possible functions, and then either choose those that best satisfy the constraints, or use a threshold to cull those that do not meet the constraints well enough.
  - Even with its limitations, our approach to crafting projection functions has proven useful to our collaborators, and shows promise in other application domains.
- Failure modes:
  - Our default settings use the top 25 variables to determine the best pairs, and the top 30 pairs and 30 variables to determine the triples to consider.

# Metrics Mentioned
- `stress`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- Using the SVM (or equivalent) machinery, the two primary ways we generate families of functions are to vary the parameter (c, as discussed in the section on L1 feature selection below), or to select different subsets of the columns of the data matrix and compute SVMs for each (as used in the section on exhaustive feature selection, below).
- Combining parameter search for L1 SVMs, near-exhaustive search of 1- 2- and 3-variable functions, and possibly solving for several different combinations of additional constraints, leads to a collection of a few hundred candidate functions.
- 4.1 Function Creation as Constrained Optimization The basic form of explainer speciﬁcation gives a binary predicate of some elements being in the positive set P and others to be in the negative set N .
- All examples in this paper do this posthoc optimization of accuracy, although we typically prefer to use nonthreshold metrics so the offset does not matter.
- For the examples in this paper, loss functions are considered only internally to the optimization algorithms for determining projection functions.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-EXTRA-C1 | stance: support | summary: For information on obtaining reprints of this article, please send e-mail to: tvcg@computer.org. to the exploration of high-dimensional spaces that allows a viewer to create sets of projection functions that deﬁne dimensions that are meaningful to them, have useful relationships with the variables, and work together to provide diversity or agreement as necessary. | evidence_ids: PENDING-EXTRA-E1, PENDING-EXTRA-E2
- CLAIM-PENDING-EXTRA-C2 | stance: support | summary: Central to our approach is to consider the different roles that projection functions may serve in exploration, the qualities that projection functions need to have in order to serve these roles, and the kinds of methods available to create and assess the functions. | evidence_ids: PENDING-EXTRA-E3, PENDING-EXTRA-E4
- CLAIM-PENDING-EXTRA-C3 | stance: support | summary: Using the SVM (or equivalent) machinery, the two primary ways we generate families of functions are to vary the parameter (c, as discussed in the section on L1 feature selection below), or to select different subsets of the columns of the data matrix and compute SVMs for each (as used in the section on exhaustive feature selection, below). | evidence_ids: PENDING-EXTRA-E5, PENDING-EXTRA-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-EXTRA-E1 | page: 1, section: extracted, quote: "For information on obtaining reprints of this article, please send e-mail to: tvcg@computer.org. to the exploration of high-dimensional spaces that allows a viewer to create sets of projection functions that deﬁne dimensions that are meaningful to them, have useful relationships with the variables, and work together to provide diversity or agreement as necessary."
- PENDING-EXTRA-E2 | page: 1, section: extracted, quote: "Explainers: Expert Explorations with Crafted Projections Michael Gleicher, Member, IEEE Abstract—This paper introduces an approach to exploration and discovery in high-dimensional data that incorporates a user’s knowledge and questions to craft sets of projection functions meaningful to them."
- PENDING-EXTRA-E3 | page: 6, section: extracted, quote: "While such an approach may need to solve a very large number of SVM problems (to determine the weights for each combination of variables), each of these problems is very small (just a few variables) and can be solved quickly."
- PENDING-EXTRA-E4 | page: 6, section: extracted, quote: "4.2 Feature Selection The problem of ﬁnding w can be viewed as having two parts: selecting which weights will be non-zero (e.g. which variables will participate), and then determining the values of these weights."
- PENDING-EXTRA-E5 | page: 1, section: extracted, quote: "Central to our approach is to consider the different roles that projection functions may serve in exploration, the qualities that projection functions need to have in order to serve these roles, and the kinds of methods available to create and assess the functions."
- PENDING-EXTRA-E6 | page: 1, section: extracted, quote: "Unlike methods that select axis-parallel projections, our approach can use more complex functions to provide ﬂexibility in the kinds of dimensions created, allowing it to represent user-deﬁned properties."
- PENDING-EXTRA-E7 | page: 6, section: extracted, quote: "A related approach is to apply a projection pursuit style algorithm: computing a linear function, factoring it out of the data matrix, and then repeating the process on the rank-reduced matrix."
- PENDING-EXTRA-E8 | page: 9, section: extracted, quote: "By generating projection functions that align with user speciﬁcations, and by considering tradeoffs in correctness, simplicity, and diversity, our approach creates derived dimensions that serve to both organize the data, as well as show its connection to properties of interest."
