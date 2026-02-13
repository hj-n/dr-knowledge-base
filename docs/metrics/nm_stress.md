# nm_stress - Non-Metric Stress

## Metric Definition
This metric emphasizes monotonic/rank-consistent fit rather than strict metric-distance fit. It is useful when ordering preservation is more important than absolute distance matching.

Operationally, treat this metric as a formal lens on one distortion family rather than a universal quality score. Two embeddings can rank differently depending on whether the task prioritizes local neighborhoods, global geometry, or class structure, so the definition should be interpreted together with explicit task intent.

For reproducible comparisons, keep preprocessing, distance definition, and evaluation protocol fixed while reading this metric. If those upstream choices change between runs, score differences often reflect evaluation drift rather than genuine embedding improvement.

## What It Quantifies
It quantifies monotonic fitting distortion between dissimilarities and projected distances. Lower values indicate better order-consistent fit.

In practical analysis, this score is most useful when you pair it with the failure mode you are trying to detect. A score increase is meaningful only if it reduces errors that matter for the declared analytical task, not just because the numeric value is higher.

This is why the metric should be read as task-conditioned evidence. Use it to answer a concrete question about neighborhood stability, class organization, distance behavior, or density behavior, then validate that interpretation with at least one complementary metric.

## Computation Outline
This outline describes the typical computational flow used in DR evaluation practice. Exact formula details may vary by implementation, but the structure below is stable across references.
- Estimate monotonic transform between original dissimilarities and projected distances.
- Compute non-metric stress under monotonic/rank-consistent fit.
- Aggregate transformed fitting errors.
- Interpret with attention to rank-oriented, not absolute-distance, fidelity.

The computation should be implemented with a stable protocol: identical sampling policy, consistent distance backend, and fixed tie-breaking behavior. Without these controls, the same embedding can yield materially different results across runs and tools.

When reporting values, record the full evaluation context including neighborhood scale, normalization policy, and whether labels were required. That metadata is part of the metric definition in practice because it determines what the reported number actually means.

Detailed protocol rule: apply consistent distance scaling and normalization policy before computing global metrics. Global score comparisons are invalid when scale handling differs across candidates.

## Hyperparameter Impact
Monotonic-fit procedure and smoothing choices control stability. Scale and tie-handling policies influence reproducibility and comparability.
Scale policy must be explicit when comparing values across runs or methods.

Hyperparameters should be tuned against the declared task, not against a single metric in isolation. Otherwise, optimization can overfit one structural aspect and silently degrade other structure that downstream users care about.

A robust workflow evaluates sensitivity with Bayesian optimization under fixed search bounds and checks rank stability across seeds or folds. Large score variance indicates that the current configuration is not yet reliable enough for high-confidence method selection.

Decision-level tuning rule: optimize this metric together with other task-relevant reliability checks, and report stability across multiple seeds or folds. Treat single-run gains as tentative until rankings stay consistent.

## Practical Reliability Notes
Normalized stress variants improve comparability across scales, but normalization choice itself is part of the model. Different normalization conventions can produce different rankings; document the exact variant and denominator policy.

Use NM-Stress when global-structure tasks require cross-method comparability under controlled scaling. Do not interpret NM-Stress alone for local tasks; combine it with local rank/neighborhood metrics before turning values into recommendations.

## Notable Properties
It is well-suited for rank/ordering preservation perspectives. It should not be read as strict absolute-distance fidelity by default.

A strong property of this metric is that it provides a compact diagnostic that is easy to compare across methods. The limitation is that compactness hides where errors occur, so it should be supplemented by structure-level inspection when decisions are high impact.

In practice, use this metric together with local, global, and (when valid) label-based checks. This combined reading lowers the risk of choosing a method that scores well on one view but fails the actual analysis goal.

## Strengths
This metric is strong when preserving distance ordering is more important than preserving exact distances. It supports non-metric evaluation scenarios where monotonic relationships are the primary fidelity target.

It is useful for global-structure audits under non-linear scale transformations or ordinal-distance interpretation contexts.

## Related Metrics
Non-Metric Stress is closest to Stress in family and to Spearman correlation in order-preservation intent.

It differs from metric stress by optimizing monotonic fit of distance ordering instead of strict metric-distance residuals.

## Task Alignment
This metric is best aligned to the task set implied by its structural role. The alignment basis is structural-granularity grouping from ZADU source note.
- Best-aligned tasks:
  - Point distance investigation
  - Class separability investigation
  - Cluster distance investigation
  - Cluster density investigation

Alignment here should be treated as a recommendation priority, not a hard constraint. If a project objective spans multiple task types, combine metrics from each relevant task family and require consistency before finalizing a method choice.

When alignment is uncertain, prefer conservative interpretation and run clarification questions again. The task decision should remain primary, and metric selection should follow that decision rather than drive it.

Operational alignment rule: use this metric as primary evidence for point-distance, cluster-distance, or density tasks; use as secondary safety check for neighborhood tasks.

## Interpretation Notes
Do not treat this metric as a standalone final decision criterion. Use it together with complementary metrics from other structural levels and keep preprocessing/seed policies fixed during comparison.

Use absolute values cautiously and prioritize relative comparisons under matched conditions. Threshold-style decisions without protocol control often produce false certainty, especially when datasets differ in scale, density, or class balance.

Before communicating a conclusion, cross-check this metric against the selected technique behavior and user-facing goal. A reliable recommendation should explain both why the score is good and why that goodness matters for the intended analytical action.

If this metric disagrees with other reliability checks, report the disagreement clearly and lower confidence instead of averaging the conflict away.

## Source Notes
The references below list paper sources used for this metric guidance.

- How Scale Breaks “Normalized Stress” and KL Divergence: Rethinking Quality Metrics (Kiran Smelser, Kaviru Gunaratne, Jacob Miller, Stephen Kobourov, IEEE Transactions on Visualization and Computer Graphics, 2024)
