# nh - Neighborhood Hit

## Metric Definition
This metric measures label agreement within local neighborhoods in the embedding. It is primarily useful when class labels are available and meaningful.

Operationally, treat this metric as a formal lens on one distortion family rather than a universal quality score. Two embeddings can rank differently depending on whether the task prioritizes local neighborhoods, global geometry, or class structure, so the definition should be interpreted together with explicit task intent.

For reproducible comparisons, keep preprocessing, distance definition, and evaluation protocol fixed while reading this metric. If those upstream choices change between runs, score differences often reflect evaluation drift rather than genuine embedding improvement.

## What It Quantifies
It quantifies local same-label neighbor purity in the embedding. Higher values indicate stronger class-consistent local neighborhoods.

In practical analysis, this score is most useful when you pair it with the failure mode you are trying to detect. A score increase is meaningful only if it reduces errors that matter for the declared analytical task, not just because the numeric value is higher.

This is why the metric should be read as task-conditioned evidence. Use it to answer a concrete question about neighborhood stability, class organization, distance behavior, or density behavior, then validate that interpretation with at least one complementary metric.

## Computation Outline
This outline describes the typical computational flow used in DR evaluation practice. Exact formula details may vary by implementation, but the structure below is stable across references.
- Require labels and choose neighborhood size `k`.
- Compute embedded-space kNN for each sample.
- Calculate same-label neighbor fraction per sample.
- Average fractions over all samples or classes.

The computation should be implemented with a stable protocol: identical sampling policy, consistent distance backend, and fixed tie-breaking behavior. Without these controls, the same embedding can yield materially different results across runs and tools.

When reporting values, record the full evaluation context including neighborhood scale, normalization policy, and whether labels were required. That metadata is part of the metric definition in practice because it determines what the reported number actually means.

Detailed protocol rule: compute under a fixed label policy (including unknown/missing labels) and fixed neighborhood scale. Label preprocessing changes can produce large score shifts that do not reflect embedding changes.

## Hyperparameter Impact
Neighborhood size `k` controls local class-purity sensitivity. Label quality, class imbalance, and label-separation validity strongly affect interpretation.
The label-separation gate is mandatory before strong interpretation in labeled settings.[^warn-label]

Hyperparameters should be tuned against the declared task, not against a single metric in isolation. Otherwise, optimization can overfit one structural aspect and silently degrade other structure that downstream users care about.

A robust workflow evaluates sensitivity with Bayesian optimization under fixed search bounds and checks rank stability across seeds or folds. Large score variance indicates that the current configuration is not yet reliable enough for high-confidence method selection.

Decision-level tuning rule: label-conditioned settings must be checked with the label-separation gate before tuning-driven decisions. If separability is weak, down-weight this metric and raise uncertainty in the final recommendation.

## Practical Reliability Notes
Neighborhood Hit is label-dependent and behaves like a local class-purity score over k-nearest neighbors in embedding space. It is high when neighbors share labels, but this is meaningful only if labels are already well-separated in the original space. If that assumption is weak, NH can reward visually clean but semantically misleading maps.

Use NH as supporting evidence, not a single gate. Pair it with at least one label-agnostic local metric and one global metric before final ranking. If NH improves while label-agnostic metrics degrade, report the tradeoff rather than claiming overall quality improvement.

## Notable Properties
It is highly interpretable in labeled settings and easy to communicate to end users. It can be misleading when labels are weakly separated in original space.

A strong property of this metric is that it provides a compact diagnostic that is easy to compare across methods. The limitation is that compactness hides where errors occur, so it should be supplemented by structure-level inspection when decisions are high impact.

In practice, use this metric together with local, global, and (when valid) label-based checks. This combined reading lowers the risk of choosing a method that scores well on one view but fails the actual analysis goal.

## Strengths
This metric is strong for label-aware local purity checks, because it directly measures how often neighbors share the same label. It is intuitive for users and easy to explain in supervised or semi-supervised settings.

It is most valuable when you need fast confirmation that local neighborhoods support class-oriented interpretations, but only after label-separation assumptions are validated.


## Task Alignment
This metric is best aligned to the task set implied by its structural role. The alignment basis is structural-granularity grouping from ZADU source note.[^cat]
- Best-aligned tasks:
  - Neighborhood identification
  - Outlier identification
  - Cluster identification

Alignment here should be treated as a recommendation priority, not a hard constraint. If a project objective spans multiple task types, combine metrics from each relevant task family and require consistency before finalizing a method choice.

When alignment is uncertain, prefer conservative interpretation and run clarification questions again. The task decision should remain primary, and metric selection should follow that decision rather than drive it.

Operational alignment rule: this metric can prioritize candidates inside an already-selected main goal, but it must not redefine the task itself. If metric preference and user task conflict, keep task intent as the hard constraint.

## Interpretation Notes
Do not treat this metric as a standalone final decision criterion. Use it together with complementary metrics from other structural levels and keep preprocessing/seed policies fixed during comparison.

Use absolute values cautiously and prioritize relative comparisons under matched conditions. Threshold-style decisions without protocol control often produce false certainty, especially when datasets differ in scale, density, or class balance.

Before communicating a conclusion, cross-check this metric against the selected technique behavior and user-facing goal. A reliable recommendation should explain both why the score is good and why that goodness matters for the intended analytical action.

If this metric disagrees with other reliability checks, report the disagreement clearly and lower confidence instead of averaging the conflict away.

## Source Notes
The references below list paper sources used for this metric guidance.

- How Scale Breaks “Normalized Stress” and KL Divergence: Rethinking Quality Metrics (Kiran Smelser et al., IEEE Transactions on Visualization and Computer Graphics, 2024)

[^cat]: ZADU: A Python Library for Evaluating the Reliability of Dimensionality Reduction Embeddings (Hyeon Jeon et al., 2023 IEEE Visualization and Visual Analytics (VIS), 2023)
[^warn-label]: ZADU README Operational Warning for Label-Separation-Sensitive Metrics (hj-n/zadu maintainers, GitHub README, 2026)
