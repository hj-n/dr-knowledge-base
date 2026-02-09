---
id: paper-2019-mdp-visual-analytics-survey
title: "Multidimensional Projection for Visual Analytics: Linking Techniques with Distortions, Tasks, and Layout Enrichment"
authors: "Luis Gustavo Nonato; Michael Aupetit"
venue: "IEEE Transactions on Visualization and Computer Graphics"
year: 2019
tags: [dr, mdp, distortions, task_alignment, survey]
source_pdf: papers/raw/Multidimensional_Projection_for_Visual_Analytics_Linking_Techniques_with_Distortions_Tasks_and_Layout_Enrichment (1).pdf
seed_note_id: ""
evidence_level: high
updated_at: 2026-02-08
---

# Problem
- Multidimensional projections (MDP) are central for DR visualization but inevitably introduce distortions that can mislead analysis.
- Technique surveys often focus on algorithms while under-specifying distortion impact on user tasks.
- Practitioners need task-aware guidance on method choice, distortion interpretation, and enrichment strategies.

# Method Summary
- The survey builds taxonomies linking MDP techniques, distortion types, quantitative distortion evaluation, and analytic task impact.
- It analyzes visual-perception implications and human-factor considerations that influence whether projected patterns are trustworthy.
- It provides guideline-style mappings from intended task to suitable MDP choices and caution areas.
- It also reviews layout-enrichment approaches that augment scatterplots when raw projection is insufficient.

# When To Use / Not Use
- Use when selecting projection techniques under explicit reliability constraints, not just visual appeal.
- Use when communicating distortion risks and choosing complementary enrichment overlays.
- Avoid treating scatterplot patterns as directly trustworthy without distortion-aware validation.
- Failure mode: selecting MDP by default similarity preservation claims without checking task-specific distortion impact.

# Metrics Mentioned
- The paper emphasizes quantitative distortion-evaluation mechanisms as a required complement to visual inspection.
- It separates distortion analysis by task impact, reinforcing that one distortion score cannot answer every analytic question.
- It positions distortion metrics as decision support for technique selection and explanation.

# Implementation Notes
- At selection time, map user task first, then choose MDP candidates whose known distortion profile is acceptable.
- Attach distortion diagnostics and enrichment cues (when needed) to each projection shown to users.
- Document which distortions remain unresolved after technique choice and why they are acceptable for the current task.
- Prefer workflow-level evidence (task + distortion + enrichment) over single-technique narratives.

# Claim Atoms (For Conflict Resolution)
- CLAIM-MDP19-C1 | stance: support | summary: MDP distortions are unavoidable and materially affect trustworthiness of visual inference. | evidence_ids: MDP19-E1, MDP19-E2
- CLAIM-MDP19-C2 | stance: support | summary: Distortion analysis should be linked to analytic tasks, not treated as context-free. | evidence_ids: MDP19-E3, MDP19-E4
- CLAIM-MDP19-C3 | stance: support | summary: Task-targeted guidelines and layout enrichment improve practical DR visual analytics. | evidence_ids: MDP19-E5, MDP19-E6

# Workflow Relevance Map
- step: 3 | relevance: high | note: links task definitions to projection-family selection rules.
- step: 5 | relevance: high | note: supports visualization-stage distortion diagnostics and enrichment decisions.
- step: 6 | relevance: high | note: improves user explanations of limits and mitigation actions.

# Evidence
- MDP19-E1 | page: 1, section: Abstract, quote: "MDP come with distortions ... visual patterns not trustworthy"
- MDP19-E2 | page: 1, section: Abstract, quote: "hindering users to infer actual data characteristics"
- MDP19-E3 | page: 1, section: Abstract, quote: "different types of distortions ... quantitatively evaluate"
- MDP19-E4 | page: 1, section: Abstract, quote: "impact of distortions on the different analytic tasks"
- MDP19-E5 | page: 1, section: Abstract, quote: "Guidelines for choosing the best MDP for an intended task"
- MDP19-E6 | page: 1, section: Abstract, quote: "layout enrichment schemes to debunk MDP distortions"
- MDP19-E7 | page: 2, section: extracted, quote: "of methods also produce point-base layouts, they are not designed to directly preserve similarity between instances, even though some variants bear such property [2]."
- MDP19-E8 | page: 3, section: extracted, quote: "A cluster can be formed by items perceived as nearby each other in the visual space M,o rb y running an automatic clustering algorithm in the data space D."
