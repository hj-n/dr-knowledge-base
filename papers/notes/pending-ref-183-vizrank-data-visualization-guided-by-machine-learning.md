---
id: paper-2006-pending-ref-183
title: "Vizrank: Data visualization guided by machine learning"
authors: "Gregor Leban, Blaž Zupan, Gaj Vidmar, and Ivan Bratko"
venue: "Data Mining and Knowledge Discovery"
year: 2006
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-183-2006-vizrank-data-visualization-guided-by-machine-learning.pdf
seed_note_id: "paper-2025-jeon-reliable-va-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- However, considering the small size of each dataset, it is expected that presence or absence of a single sequence may have a significant effect on the BN structure, thus making unreliable any assertions regarding the specificity of interactions or dependencies among polymorphic nt sites of the 3 regions in the context of association to RFP.
- BNC models can handle problems of convergent evolution when estimating HCV resistance to treatment [23,24] and host-related features, such as, demographic characteristics of patients [23].

# Method Summary
- In addition, to validate LP models and viral parameters in selected projections, classification performance of LP models trained on a specific liver-transplant group dataset (see Patients and HCV 1b sequences in Materials and Methods) was measured using the opposite livertransplant group data as test sets.
- Linear projection graphs and models To uncover interactions among relevant viral features associated to RFP characteristics of patients and provide information about inter- and intra-RFP class similarities among HCV strains, a linear projection (LP) method [28] was used.
- To find the most useful projections comprising a subset of features (base vectors) that would optimally associate HCV variants to RFP characteristics of patients we used the VizRank search method [29].
- For each projection, the average probability ( P) assignment to the correct RPF-class was computed using a probabilistic k-nearest neighbors algorithm (k-NN), where the parameter k was set at 6.
- Given enough time, the VizRank search method will explore the entire search space, so it is common to limit the projections ’ size (subset of features) and/or to limit search times.
- Then, the FreeViz machinelearning method [28] was used to generate LP models of the projection.
- Bayesian network classifier (BNC) To examine how dependency in nt substitutions among relevant genomic sites associate HCV genetic heterogeneity of strains to RFP and to further explore inter- and intra-RFP-class similarities among HCV strains between TOH and IC patients, the learning Bayesian network (BN) approach [32] in the form of a BN classifier (BNC) was used.

# When To Use / Not Use
- Use when:
  - The Best-first greedy search strategy [26] was used in CFS iterations, which considers effects of adding (or removing) a feature to the current subset in order to find a better subset of interacting features.
  - Machine-learning techniques, linear projection (LP) and Bayesian Networks (BN), were used to assess and identify associations between the HCV sequences and RFP.
- Avoid when:
  - Because prediction performances of BNC models trained on randomizedlabeled data deteriorate duri ng validation tests, falling closely to the excepted classification accuracy of 50.0%, associations observed in data are not likely to be result of random correlations, thus, further providing evidence to support relevance of identified viral markers, accuracy of models performance and association to RFP.
  - The BNC model where all features depends on the class and any feature depends on k other features at most is described by the formula, p(c|f1, ..., fn) ∝ p(c)p(f1|fi, ...., fk, c) × .... × p(fn|fh , ...., fk, c) where c is the RFP-class and {f 1,f i,f h,f k, .... fn} are features, CFS-selected sites of the HCV genome used in this study whose values represent nt states (4-letter alphabetical code).
- Failure modes:
  - Bayesian network classifier (BNC) To examine how dependency in nt substitutions among relevant genomic sites associate HCV genetic heterogeneity of strains to RFP and to further explore inter- and intra-RFP-class similarities among HCV strains between TOH and IC patients, the learning Bayesian network (BN) approach [32] in the form of a BN classifier (BNC) was used.

# Metrics Mentioned
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- In addition, to validate LP models and viral parameters in selected projections, classification performance of LP models trained on a specific liver-transplant group dataset (see Patients and HCV 1b sequences in Materials and Methods) was measured using the opposite livertransplant group data as test sets.
- The Best-first greedy search strategy [26] was used in CFS iterations, which considers effects of adding (or removing) a feature to the current subset in order to find a better subset of interacting features.
- Computational models parameterized using the identified sites accurately associated HCV strains with RFP in 70/30 split cross-validation (90-95% accuracy) and in validation tests (85-90% accuracy).
- For each projection, the average probability ( P) assignment to the correct RPF-class was computed using a probabilistic k-nearest neighbors algorithm (k-NN), where the parameter k was set at 6.
- The second task, parameter estimation, which consists of estimating the conditional probability tables of nodes in BNC, was directly estimated from data and based on frequency counts.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-183-C1 | stance: support | summary: However, considering the small size of each dataset, it is expected that presence or absence of a single sequence may have a significant effect on the BN structure, thus making unreliable any assertions regarding the specificity of interactions or dependencies among polymorphic nt sites of the 3 regions in the context of association to RFP. | evidence_ids: PENDING-REF-183-E1, PENDING-REF-183-E2
- CLAIM-PENDING-REF-183-C2 | stance: support | summary: In addition, to validate LP models and viral parameters in selected projections, classification performance of LP models trained on a specific liver-transplant group dataset (see Patients and HCV 1b sequences in Materials and Methods) was measured using the opposite livertransplant group data as test sets. | evidence_ids: PENDING-REF-183-E3, PENDING-REF-183-E4
- CLAIM-PENDING-REF-183-C3 | stance: support | summary: In addition, to validate LP models and viral parameters in selected projections, classification performance of LP models trained on a specific liver-transplant group dataset (see Patients and HCV 1b sequences in Materials and Methods) was measured using the opposite livertransplant group data as test sets. | evidence_ids: PENDING-REF-183-E5, PENDING-REF-183-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance
- step: 6 | relevance: high | note: guides reliable interpretation of projected views

# Evidence
- PENDING-REF-183-E1 | page: 5, section: extracted, quote: "However, considering the small size of each dataset, it is expected that presence or absence of a single sequence may have a significant effect on the BN structure, thus making unreliable any assertions regarding the specificity of interactions or dependencies among polymorphic nt sites of the 3 regions in the context of association to RFP."
- PENDING-REF-183-E2 | page: 3, section: extracted, quote: "BNC models can handle problems of convergent evolution when estimating HCV resistance to treatment [23,24] and host-related features, such as, demographic characteristics of patients [23]."
- PENDING-REF-183-E3 | page: 3, section: extracted, quote: "In addition, to validate LP models and viral parameters in selected projections, classification performance of LP models trained on a specific liver-transplant group dataset (see Patients and HCV 1b sequences in Materials and Methods) was measured using the opposite livertransplant group data as test sets."
- PENDING-REF-183-E4 | page: 3, section: extracted, quote: "Linear projection graphs and models To uncover interactions among relevant viral features associated to RFP characteristics of patients and provide information about inter- and intra-RFP class similarities among HCV strains, a linear projection (LP) method [28] was used."
- PENDING-REF-183-E5 | page: 3, section: extracted, quote: "To find the most useful projections comprising a subset of features (base vectors) that would optimally associate HCV variants to RFP characteristics of patients we used the VizRank search method [29]."
- PENDING-REF-183-E6 | page: 3, section: extracted, quote: "For each projection, the average probability ( P) assignment to the correct RPF-class was computed using a probabilistic k-nearest neighbors algorithm (k-NN), where the parameter k was set at 6."
- PENDING-REF-183-E7 | page: 3, section: extracted, quote: "Given enough time, the VizRank search method will explore the entire search space, so it is common to limit the projections ’ size (subset of features) and/or to limit search times."
- PENDING-REF-183-E8 | page: 3, section: extracted, quote: "Then, the FreeViz machinelearning method [28] was used to generate LP models of the projection."
