---
id: note-2026-zadu-readme-warning
title: "ZADU README Operational Warning for Label-Separation-Sensitive Metrics"
authors: "hj-n/zadu maintainers"
venue: "GitHub README"
year: 2026
tags: [dr, zadu, warning, labels]
source_pdf: https://github.com/hj-n/zadu/blob/master/README.md
seed_note_id: ""
evidence_level: high
updated_at: 2026-02-13
---

# Problem
- Some label-aware reliability checks can become misleading when class labels are not clearly separated in the original high-dimensional space.
- In real projects, this assumption is often unstated. Analysts may trust class-aware scores even when the data geometry does not support those interpretations.
- The README warning addresses this operational risk directly and should be treated as a mandatory caution in recommendation logic.

# Method Summary
- The ZADU README includes an explicit warning block naming five label-sensitive measures.
- The warning states that these measures assume well-separated labels in the original space and may produce unreliable results if that assumption fails.
- It also requires user confidence in label separation before using those measures and points readers to related papers for methodological detail.

# When To Use / Not Use
- Use these measures when:
  - class labels exist and are semantically meaningful for the analysis goal,
  - baseline checks in original space indicate clear label separation.
- Avoid using these measures as primary decision evidence when:
  - class overlap is substantial,
  - label quality is noisy/ambiguous,
  - label separation has not been checked.
- Failure mode: class-aware scores can reward visually separated layouts even when original-space class structure is mixed, leading to overconfident conclusions.

# Metrics Mentioned
- Distance Consistency
- Internal Validation Measure
- Clustering-plus-External Validation Measure
- Neighborhood Hit
- Class-Aware Trustworthiness and Continuity

These measures are useful only under the stated label-separation assumption. At least one label-agnostic reliability check should accompany them in final comparison.

# Implementation Notes
- Surface this warning whenever any of the five listed measures appears in candidate scoring.
- Add an explicit pre-check: verify whether class labels are well separated in original space before trusting class-aware reliability conclusions.
- If this pre-check is weak/unknown, downgrade confidence and prioritize label-agnostic checks for final ranking.
- In user-facing explanations, describe this as a label-quality/separation caution in plain language rather than internal policy jargon.

# Claim Atoms (For Conflict Resolution)
- CLAIM-ZADU-RM-C1 | stance: support | summary: The warning explicitly names dsc, ivm, c_evm, nh, and ca_tnc as label-separation-sensitive measures. | evidence_ids: ZADU-RM-E1
- CLAIM-ZADU-RM-C2 | stance: support | summary: The warning states that these measures assume well-separated class labels in original space. | evidence_ids: ZADU-RM-E2
- CLAIM-ZADU-RM-C3 | stance: support | summary: The warning states that reliability can fail when labels are not well separated. | evidence_ids: ZADU-RM-E3
- CLAIM-ZADU-RM-C4 | stance: support | summary: The warning requires confidence in label separation before use and directs users to paper-level detail. | evidence_ids: ZADU-RM-E4, ZADU-RM-E5

# Workflow Relevance Map
- step: 3 | relevance: high | note: adds a mandatory label-separation pre-check before class-aware reliability interpretation.
- step: 4 | relevance: high | note: prevents overconfident ranking when class-aware scores conflict with label-agnostic checks.
- step: 7 | relevance: high | note: requires explicit user-facing caution whenever label-separation confidence is limited.

# Evidence
- ZADU-RM-E1 | source: README warning block, quote: "While using dsc, ivm, c_evm, nh, and ca_tnc"
- ZADU-RM-E2 | source: README warning block, quote: "these measures assume that class labels are well-separated in the original high-dimensional space."
- ZADU-RM-E3 | source: README warning block, quote: "If the class labels are not well-separated, the measures may produce unreliable results."
- ZADU-RM-E4 | source: README warning block, quote: "Use the measure only if you are confident that the class labels are well-separated."
- ZADU-RM-E5 | source: README warning block, quote: "Please refer to the related academic paper for more detail."
