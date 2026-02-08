# l_tnc - Label Trustworthiness & Continuity

## Metric Definition
This metric focuses on label-structure reliability under trustworthiness/continuity principles. It compares how label-related neighborhood behavior changes across spaces.

Operationally, treat this metric as a formal lens on one distortion family rather than a universal quality score. Two embeddings can rank differently depending on whether the task prioritizes local neighborhoods, global geometry, or class structure, so the definition should be interpreted together with explicit task intent.

For reproducible comparisons, keep preprocessing, distance definition, and evaluation protocol fixed while reading this metric. If those upstream choices change between runs, score differences often reflect evaluation drift rather than genuine embedding improvement.

## What It Quantifies
It quantifies label-structure consistency across original and projected neighborhoods. It is useful when label-preserving reliability is a first-order requirement.

In practical analysis, this score is most useful when you pair it with the failure mode you are trying to detect. A score increase is meaningful only if it reduces errors that matter for the declared analytical task, not just because the numeric value is higher.

This is why the metric should be read as task-conditioned evidence. Use it to answer a concrete question about neighborhood stability, class organization, distance behavior, or density behavior, then validate that interpretation with at least one complementary metric.

## Computation Outline
This outline describes the typical computational flow used in DR evaluation practice. Exact formula details may vary by implementation, but the structure below is stable across references.
- Require labels and a neighborhood policy.
- Estimate label-conditioned neighborhood reliability in original space.
- Estimate corresponding reliability in projected space.
- Compute trust/continuity discrepancy between the two spaces.

The computation should be implemented with a stable protocol: identical sampling policy, consistent distance backend, and fixed tie-breaking behavior. Without these controls, the same embedding can yield materially different results across runs and tools.

When reporting values, record the full evaluation context including neighborhood scale, normalization policy, and whether labels were required. That metadata is part of the metric definition in practice because it determines what the reported number actually means.

## Hyperparameter Impact
Label-conditioned neighborhood policy is a major control. Label-structure estimation strategy affects calibration and between-run comparability.

Hyperparameters should be tuned against the declared task, not against a single metric in isolation. Otherwise, optimization can overfit one structural aspect and silently degrade other structure that downstream users care about.

A robust workflow evaluates sensitivity by sweeping key controls and checking rank stability across seeds or folds. Large score variance indicates that the current configuration is not yet reliable enough for high-confidence method selection.

## Notable Properties
It explicitly targets label-structure reliability across spaces. It should be interpreted together with label-agnostic metrics to avoid one-sided conclusions.

A strong property of this metric is that it provides a compact diagnostic that is easy to compare across methods. The limitation is that compactness hides where errors occur, so it should be supplemented by structure-level inspection when decisions are high impact.

In review workflows, this metric works best as one component in a bundle: local, global, and label-aware signals together. That bundle-based interpretation reduces the chance of selecting a method that is numerically strong but operationally misaligned.

## Strengths
This metric is strong for checking whether label-conditioned neighborhood reliability is preserved across spaces. It focuses on class-structure consistency directly, making it useful when label reliability is a first-order requirement.

It complements label-agnostic local metrics by highlighting whether local geometric quality also aligns with class semantics.


## Task Alignment
This metric is best aligned to the task set implied by its structural role. The alignment basis is label-structure source note for Label-T&C.[^cat]
- Best-aligned tasks:
  - Class separability investigation
  - Cluster identification

Alignment here should be treated as a recommendation priority, not a hard constraint. If a project objective spans multiple task types, combine metrics from each relevant task family and require consistency before finalizing a method choice.

When alignment is uncertain, prefer conservative interpretation and run clarification questions again. The task decision should remain primary, and metric selection should follow that decision rather than drive it.

## Interpretation Notes
Do not treat this metric as a standalone final decision criterion. Use it together with complementary metrics from other structural levels and keep preprocessing/seed policies fixed during comparison.

Use absolute values cautiously and prioritize relative comparisons under matched conditions. Threshold-style decisions without protocol control often produce false certainty, especially when datasets differ in scale, density, or class balance.

Before communicating a conclusion, cross-check this metric against the selected technique behavior and user-facing goal. A reliable recommendation should explain both why the score is good and why that goodness matters for the intended analytical action.

## Source Notes
The links below map this metric to claim-level evidence extracted from individual source notes. Use these links when tracing recommendations back to evidence.
- `papers/notes/zadu-ref-11-jeon23tvcg-4.md` -> `CLAIM-METRIC-L_TNC-SOURCE-11`

[^cat]: Label-structure source note: `papers/notes/zadu-ref-11-jeon23tvcg-4.md` (CLAIM-METRIC-L_TNC-SOURCE-11).
