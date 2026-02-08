---
id: paper-2014-brehmer-task-sequences
title: "Visualizing Dimensionally-Reduced Data: Interviews with Analysts and a Characterization of Task Sequences"
authors: "Matthew Brehmer; Michael Sedlmair; Stephen Ingram; Tamara Munzner"
venue: "BELIV 2014"
year: 2014
tags: [dr, tasks, interview, visual_analytics]
source_pdf: papers/raw/2669557.2669559.pdf
seed_note_id: ""
evidence_level: high
updated_at: 2026-02-08
---

# Problem
- DR systems were being designed around techniques, but explicit descriptions of real analyst task sequences were missing.
- Without task-sequence models, method/tool evaluations cannot map clearly to what users actually do in analytical workflows.
- The paper addresses this by grounding DR usage in observed analyst practice across multiple domains.

# Method Summary
- The authors combine interview data from ten analysts across six domains with literature analysis.
- They synthesize five recurring task sequences for DR-based visual analysis instead of proposing a new DR algorithm.
- The task-sequence model includes both representation-oriented tasks and class/cluster interpretation tasks.
- The framework is positioned for requirements elicitation, controlled studies, and field evaluation of DR tools.

# When To Use / Not Use
- Use when designing intake/question flows and evaluation protocols for DR systems.
- Use when translating analyst language into concrete DR task sequences before selecting techniques or metrics.
- Avoid using this paper as a direct ranking of DR algorithms; its contribution is task characterization, not algorithmic superiority.
- Failure mode: skipping task-sequence clarification and jumping directly to projection choice.

# Metrics Mentioned
- No single DR quality metric is introduced; the paper is task/evaluation-methodology focused.
- It contributes task semantics that should drive metric and method selection downstream.
- It highlights evaluation methodology as a core requirement for reliable DR use.

# Implementation Notes
- Run task-sequence clarification before recommending methods, especially for non-expert users.
- Capture whether users are naming dimensions, verifying clusters, or matching clusters to known classes, because each requires different evidence.
- Use the five-task-sequence framing to build structured prompts and explain decisions transparently.
- Integrate this task framing with the repository 7-axis taxonomy by mapping each sequence to one primary axis and optional subtype.

# Claim Atoms (For Conflict Resolution)
- CLAIM-BELIV14-C1 | stance: support | summary: DR visual analysis requires explicit task-sequence characterization grounded in analyst practice. | evidence_ids: BEL14-E1, BEL14-E2
- CLAIM-BELIV14-C2 | stance: support | summary: Five task sequences provide a practical bridge between methods and real analytic workflows. | evidence_ids: BEL14-E3, BEL14-E4
- CLAIM-BELIV14-C3 | stance: support | summary: Task-sequence models improve design and evaluation of DR tools. | evidence_ids: BEL14-E5, BEL14-E6

# Workflow Relevance Map
- step: 1 | relevance: high | note: directly informs task clarification and follow-up questioning strategy.
- step: 3 | relevance: medium | note: improves task-to-technique mapping precision.
- step: 6 | relevance: high | note: supports user-facing explanations tied to concrete analyst intents.

# Evidence
- BEL14-E1 | page: 2, section: Abstract, quote: "We characterize five task sequences"
- BEL14-E2 | page: 2, section: Abstract, quote: "drawing from data collected from interviews"
- BEL14-E3 | page: 2, section: Contribution, quote: "fills a gap ... abundance of proposed techniques and tools"
- BEL14-E4 | page: 2, section: Contribution, quote: "naming synthesized dimensions ... matching clusters and classes"
- BEL14-E5 | page: 2, section: Motivation, quote: "better understanding of these tasks is essential"
- BEL14-E6 | page: 8-9, section: Conclusion, quote: "consider these task abstractions ... in field evaluations"
