---
id: paper-2024-pending-ref-130
title: "Mountaineer: Topology-Driven Visual Analytics for Comparing Local Explanations"
authors: "Parikshit Solunke, Vitoria Guardieiro, João Rulff, Peter Xenopoulos, Gromit YeukYin Chan, Brian Barr, Luis Gustavo Nonato, and Claudio Silva"
venue: "IEEE Transactions on Visualization and Computer Graphics"
year: 2024
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-130-2024-mountaineer-topology-driven-visual-analytics-for-comparing-local-explanations.pdf
seed_note_id: "paper-2025-stop-misusing-tsne-umap"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- Owing to an ever-increasing number of local explainability methods at their disposal, practitioners are often faced with the challenge of assessing and selecting the most appropriate method for the problem at hand.
- Additionally, there have been numerous works [38], [48] addressing the problem of Mapper parameter selection; We believe we can further build upon our work and introduce a metric to quantify the quality of the Mapper parameter search as well as improve the runtime of the parameter search.
- This raises two important questions - 1) How do we evaluate the local explanations and compare different techniques at a global level? and 2) Given a set of explanations- how do we determine which are most suited for the problem on hand ?
- If we were indeed building models for decision-making (such as credit analysis), this find would indicate a case of model discrimination, sparking a further development of fairnessaware models for the cognitive difficulty characteristic.

# Method Summary
- Finally, although we presented a comprehensive strategy for Mapper parameter tuning, the fine-tuning of hyperparameters for explanation methods remains unexplored in our current work, which represents an important direction for future investigation.
- Our motivation for employing this clustering method is that it 6 enables us to automatically select the appropriate parameter, as discussed in Section V-B, where we present our parameter selection strategy.
- This method takes the input space, lens function, resolution, gain, and clustering algorithm as arguments and returns an object detailing the node clusters and the links between these clusters.
- In this work, we present M OUNTAINEER , a visual analytics framework to analyze and compare ML explanation methods using techniques from Topological Data Analysis.
- We create our graphs using the create mapper method of the GALE library, which implements the Mapper algorithm [11] [31] to create topological graphs.
- In this work, we propose an automatic parameter selection approach based on the stability of the resulting graph, which is presented in Section V-B.
- As a consequence, there is a pressing need for approaches to compare explanations of different XAI methodologies.

# When To Use / Not Use
- Use when:
  - Furthermore, we intend to address the aforementioned visual limitations of our current system, making it easier for users to explore datasets with a high number of features, and also allow the user to compare multiple graphs at once as recommended by expert P3.
  - Our topology-driven framework focuses on improving the workflow of black-box model interpretations, in which practitioners need to evaluate different explanation methods to choose the best one for achieving their goals.
- Avoid when:
  - Therefore, for most real-world use cases, this limitation should suffice in terms of the number of explanations to be evaluated.
  - Mapper Parameters In addition to the input space and the scalar lens function, the Mapper algorithm requires three parameters - 1) the resolution specifies the number of intervals the range of the scalar function is divided into, 2) the gain defines the amount of overlap between consecutive ranges, and 3) the clustering algorithm (which may need its own hyperparameters) used to perform clustering.
- Failure modes:
  - Additionally, there have been numerous works [38], [48] addressing the problem of Mapper parameter selection; We believe we can further build upon our work and introduce a metric to quantify the quality of the Mapper parameter search as well as improve the runtime of the parameter search.

# Metrics Mentioned
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- Harer et al., “Hyperparameter optimization of topological features for machine learning applications,” in 2019 18th IEEE international conference on machine learning and applications (ICMLA).
- Mapper Parameters In addition to the input space and the scalar lens function, the Mapper algorithm requires three parameters - 1) the resolution specifies the number of intervals the range of the scalar function is divided into, 2) the gain defines the amount of overlap between consecutive ranges, and 3) the clustering algorithm (which may need its own hyperparameters) used to perform clustering.
- Additionally, there have been numerous works [38], [48] addressing the problem of Mapper parameter selection; We believe we can further build upon our work and introduce a metric to quantify the quality of the Mapper parameter search as well as improve the runtime of the parameter search.
- Finally, although we presented a comprehensive strategy for Mapper parameter tuning, the fine-tuning of hyperparameters for explanation methods remains unexplored in our current work, which represents an important direction for future investigation.
- First, many local explanation methods often have their own hyperparameters that can significantly impact the resulting explanations.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-130-C1 | stance: support | summary: Owing to an ever-increasing number of local explainability methods at their disposal, practitioners are often faced with the challenge of assessing and selecting the most appropriate method for the problem at hand. | evidence_ids: PENDING-REF-130-E1, PENDING-REF-130-E2
- CLAIM-PENDING-REF-130-C2 | stance: support | summary: Finally, although we presented a comprehensive strategy for Mapper parameter tuning, the fine-tuning of hyperparameters for explanation methods remains unexplored in our current work, which represents an important direction for future investigation. | evidence_ids: PENDING-REF-130-E3, PENDING-REF-130-E4
- CLAIM-PENDING-REF-130-C3 | stance: support | summary: Harer et al., “Hyperparameter optimization of topological features for machine learning applications,” in 2019 18th IEEE international conference on machine learning and applications (ICMLA). | evidence_ids: PENDING-REF-130-E5, PENDING-REF-130-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-REF-130-E1 | page: 4, section: extracted, quote: "Owing to an ever-increasing number of local explainability methods at their disposal, practitioners are often faced with the challenge of assessing and selecting the most appropriate method for the problem at hand."
- PENDING-REF-130-E2 | page: 12, section: extracted, quote: "Additionally, there have been numerous works [38], [48] addressing the problem of Mapper parameter selection; We believe we can further build upon our work and introduce a metric to quantify the quality of the Mapper parameter search as well as improve the runtime of the parameter search."
- PENDING-REF-130-E3 | page: 3, section: extracted, quote: "This raises two important questions - 1) How do we evaluate the local explanations and compare different techniques at a global level? and 2) Given a set of explanations- how do we determine which are most suited for the problem on hand ?"
- PENDING-REF-130-E4 | page: 11, section: extracted, quote: "If we were indeed building models for decision-making (such as credit analysis), this find would indicate a case of model discrimination, sparking a further development of fairnessaware models for the cognitive difficulty characteristic."
- PENDING-REF-130-E5 | page: 12, section: extracted, quote: "Finally, although we presented a comprehensive strategy for Mapper parameter tuning, the fine-tuning of hyperparameters for explanation methods remains unexplored in our current work, which represents an important direction for future investigation."
- PENDING-REF-130-E6 | page: 5, section: extracted, quote: "Our motivation for employing this clustering method is that it 6 enables us to automatically select the appropriate parameter, as discussed in Section V-B, where we present our parameter selection strategy."
- PENDING-REF-130-E7 | page: 8, section: extracted, quote: "This method takes the input space, lens function, resolution, gain, and clustering algorithm as arguments and returns an object detailing the node clusters and the links between these clusters."
- PENDING-REF-130-E8 | page: 2, section: extracted, quote: "In this work, we present M OUNTAINEER , a visual analytics framework to analyze and compare ML explanation methods using techniques from Topological Data Analysis."
