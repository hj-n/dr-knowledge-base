---
id: paper-2009-pending-ref-080
title: "iPCA: An Interactive System for PCA-based Visual Analytics"
authors: "Dong Hyun Jeong, Caroline Ziemkiewicz, Brian Fisher, William Ribarsky, and Remco Chang"
venue: "Artificial Intelligence in Medicine"
year: 2009
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-080-2009-ipca-an-interactive-system-for-pca-based-visual-analytics.pdf
seed_note_id: "paper-2019-mdp-visual-analytics-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- Consequently, AFB can be applied to any optimization problem that is deﬁned by a triplet of functions ( cost, ﬂy, walk), where cost is the cost function to minimize, ﬂy is a function that returns a totally random solution and walk is a function that returns a random solution close to another previous solution.
- AFB was chosen because it is very easy to adapt to new problems, including constrained combinatorial optimization, and we successfully used it previously for optimizing rainbow boxes [36] but also for quantitative preference learning [37].
- CBR has been applied to many domains, including medicine [3].I n a medical CBR system, a case usually corresponds to a patient and the problem to solve typically consists of classifying a new patient according to various classes.
- High-dimensional multivariate data visualization Many techniques exist for visualizing high-dimensional or multivariate data; we will focus on the two approaches relevant for the presented work.

# Method Summary
- In this paper, we propose a CBR method that can be both executed automatically as an algorithm and presented visually in a user interface for providing visual explanations or for visual reasoning.
- Since it is easier to formalize a visual approach than to translate an algorithm visually, we initially developed our method from the visual side, and here, we will present it in that way.
- Biran et al. [12] distinguish two approaches: (a) interpretable models, which rely on non-black box systems such as rule-based ones, and (b) prediction interpretation and justiﬁcation, which aim at generating explanations for a black box algorithm.
- We showed on three public datasets that our qualitative method has a classi ﬁcation accuracy comparable to k-Nearest Neighbors algorithms, but is better explainable.
- A preliminary version of this work was presented in a French workshop [18], proposing the general approach but without detailed methods or experiments.
- Here, we propose a 2-dimensional approach for MDS in polar coordinates. q is placed at the origin (0, 0).
- However, CBR is still an interesting approach for patients that are not covered by clinical practice guidelines (they can represent up to 45% of patients [5]), or when guideline's recommendations cannot be applied, e.g. due to contraindications or when the patient refuses the recommended therapy.

# When To Use / Not Use
- Use when:
  - Section 2 presents some related works on CBR and high-dimensional multivariate data visualization, and also introduces the optimization algorithm that we used.
  - CBR follows a cycle of four phases: retrieve from the case base the old cases that are the most similar to the query, reuse the information and knowledge embedded within similar resolved cases to produce a solution for the query case, revise the solution to adapt it to the query case, and retain the query case with the chosen solution in the case database.
- Avoid when:
  - For each case, the user had to indicate the treatment type he would choose on the basis of the presented data (4 possible values), and his level of con ﬁdence in his decision (5-value Likert scale: Not con ﬁdent, Rather not con ﬁdent, Mildly con ﬁdent, Rather con ﬁdent, Con ﬁdent, coded as a 1– 5 value with 5 being Con ﬁdent).
  - However, CBR is still an interesting approach for patients that are not covered by clinical practice guidelines (they can represent up to 45% of patients [5]), or when guideline's recommendations cannot be applied, e.g. due to contraindications or when the patient refuses the recommended therapy.
- Failure modes:
  - Finally, gray boxes might suggest arguments for not choosing a class, e.g. the tall gray box labeled “dim #5 = val #5 ″ could be an argument for not choosing the red class, because all cases belonging to this class have the given value in dimension #5, and q has not.

# Metrics Mentioned
- `stress`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- Consequently, AFB can be applied to any optimization problem that is deﬁned by a triplet of functions ( cost, ﬂy, walk), where cost is the cost function to minimize, ﬂy is a function that returns a totally random solution and walk is a function that returns a random solution close to another previous solution.
- These functions correspond to the one proposed previously for global non-linear optimization [36], but we modi ﬁed the walk functions to take into account the cyclic nature of angles: when the new value is outside the expected range [0, 2 π[, we apply a modulo 2π .
- AFB was chosen because it is very easy to adapt to new problems, including constrained combinatorial optimization, and we successfully used it previously for optimizing rainbow boxes [36] but also for quantitative preference learning [37].
- It takes 2 parameters: n, the total number of cases displayed in the interface (the ﬁrst one being q, thus n − 1 similar cases are retrieved from X), and m, the maximum number of qualitative boxes to display in rainbow boxes.
- The column order is computed using a heuristic optimization algorithm, which tries to order the columns so as the elements belonging to similar sets are contiguous.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-080-C1 | stance: support | summary: Consequently, AFB can be applied to any optimization problem that is deﬁned by a triplet of functions ( cost, ﬂy, walk), where cost is the cost function to minimize, ﬂy is a function that returns a totally random solution and walk is a function that returns a random solution close to another previous solution. | evidence_ids: PENDING-REF-080-E1, PENDING-REF-080-E2
- CLAIM-PENDING-REF-080-C2 | stance: support | summary: In this paper, we propose a CBR method that can be both executed automatically as an algorithm and presented visually in a user interface for providing visual explanations or for visual reasoning. | evidence_ids: PENDING-REF-080-E3, PENDING-REF-080-E4
- CLAIM-PENDING-REF-080-C3 | stance: support | summary: Consequently, AFB can be applied to any optimization problem that is deﬁned by a triplet of functions ( cost, ﬂy, walk), where cost is the cost function to minimize, ﬂy is a function that returns a totally random solution and walk is a function that returns a random solution close to another previous solution. | evidence_ids: PENDING-REF-080-E5, PENDING-REF-080-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance
- step: 6 | relevance: high | note: guides reliable interpretation of projected views

# Evidence
- PENDING-REF-080-E1 | page: 4, section: extracted, quote: "Consequently, AFB can be applied to any optimization problem that is deﬁned by a triplet of functions ( cost, ﬂy, walk), where cost is the cost function to minimize, ﬂy is a function that returns a totally random solution and walk is a function that returns a random solution close to another previous solution."
- PENDING-REF-080-E2 | page: 4, section: extracted, quote: "AFB was chosen because it is very easy to adapt to new problems, including constrained combinatorial optimization, and we successfully used it previously for optimizing rainbow boxes [36] but also for quantitative preference learning [37]."
- PENDING-REF-080-E3 | page: 2, section: extracted, quote: "CBR has been applied to many domains, including medicine [3].I n a medical CBR system, a case usually corresponds to a patient and the problem to solve typically consists of classifying a new patient according to various classes."
- PENDING-REF-080-E4 | page: 4, section: extracted, quote: "High-dimensional multivariate data visualization Many techniques exist for visualizing high-dimensional or multivariate data; we will focus on the two approaches relevant for the presented work."
- PENDING-REF-080-E5 | page: 2, section: extracted, quote: "In this paper, we propose a CBR method that can be both executed automatically as an algorithm and presented visually in a user interface for providing visual explanations or for visual reasoning."
- PENDING-REF-080-E6 | page: 3, section: extracted, quote: "Since it is easier to formalize a visual approach than to translate an algorithm visually, we initially developed our method from the visual side, and here, we will present it in that way."
- PENDING-REF-080-E7 | page: 3, section: extracted, quote: "Biran et al. [12] distinguish two approaches: (a) interpretable models, which rely on non-black box systems such as rule-based ones, and (b) prediction interpretation and justiﬁcation, which aim at generating explanations for a black box algorithm."
- PENDING-REF-080-E8 | page: 2, section: extracted, quote: "We showed on three public datasets that our qualitative method has a classi ﬁcation accuracy comparable to k-Nearest Neighbors algorithms, but is better explainable."
