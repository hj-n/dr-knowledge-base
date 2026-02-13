# lcmc - Local Continuity Meta-Criteria

## Metric Definition
This metric evaluates overlap between high-dimensional and low-dimensional neighborhood sets with a baseline correction. It is designed for local continuity analysis across neighborhood scales.

Operationally, treat this metric as a formal lens on one distortion family rather than a universal quality score. Two embeddings can rank differently depending on whether the task prioritizes local neighborhoods, global geometry, or class structure, so the definition should be interpreted together with explicit task intent.

For reproducible comparisons, keep preprocessing, distance definition, and evaluation protocol fixed while reading this metric. If those upstream choices change between runs, score differences often reflect evaluation drift rather than genuine embedding improvement.

## What It Quantifies
It quantifies neighborhood overlap quality after baseline correction. Higher values indicate better local continuity at the selected neighborhood scale.

In practical analysis, this score is most useful when you pair it with the failure mode you are trying to detect. A score increase is meaningful only if it reduces errors that matter for the declared analytical task, not just because the numeric value is higher.

This is why the metric should be read as task-conditioned evidence. Use it to answer a concrete question about neighborhood stability, class organization, distance behavior, or density behavior, then validate that interpretation with at least one complementary metric.

## Computation Outline
This outline describes the typical computational flow used in DR evaluation practice. Exact formula details may vary by implementation, but the structure below is stable across references.
- Select neighborhood size `k` and compute kNN sets in both spaces.
- Measure intersection size between high-space and low-space neighborhoods per point.
- Apply baseline correction to remove random-overlap effects.
- Average corrected overlap over the dataset.

The computation should be implemented with a stable protocol: identical sampling policy, consistent distance backend, and fixed tie-breaking behavior. Without these controls, the same embedding can yield materially different results across runs and tools.

When reporting values, record the full evaluation context including neighborhood scale, normalization policy, and whether labels were required. That metadata is part of the metric definition in practice because it determines what the reported number actually means.

Detailed protocol rule: evaluate multiple neighborhood scales (for example small/medium/local-range k values) and keep the same k schedule across methods. Local metrics should be read as scale-dependent curves, not single-point truths.

## Hyperparameter Impact
Neighborhood size `k` directly changes overlap regime and curve shape. Distance metric and kNN graph construction details influence comparability across runs.

Hyperparameters should be tuned against the declared task, not against a single metric in isolation. Otherwise, optimization can overfit one structural aspect and silently degrade other structure that downstream users care about.

A robust workflow evaluates sensitivity with Bayesian optimization under fixed search bounds and checks rank stability across seeds or folds. Large score variance indicates that the current configuration is not yet reliable enough for high-confidence method selection.

Decision-level tuning rule: optimize this metric together with other task-relevant reliability checks, and report stability across multiple seeds or folds. Treat single-run gains as tentative until rankings stay consistent.

## Practical Reliability Notes
LCMC is sensitive to neighborhood scale selection and is best interpreted as a curve across scales rather than a single point estimate. Single-k reporting can overstate confidence by hiding where methods cross in quality.

Use LCMC as a ranking support metric after task clarification, especially for neighborhood/cluster exploration. For production recommendations, pair it with at least one global safety check metric so local improvements do not mask global collapse.

## Notable Properties
It provides an intuitive overlap-centric local continuity signal. It is simple to explain, but it does not fully capture rank-order details within overlaps.

A strong property of this metric is that it provides a compact diagnostic that is easy to compare across methods. The limitation is that compactness hides where errors occur, so it should be supplemented by structure-level inspection when decisions are high impact.

In practice, use this metric together with local, global, and (when valid) label-based checks. This combined reading lowers the risk of choosing a method that scores well on one view but fails the actual analysis goal.

## Strengths
This metric is strong for measuring local-neighborhood overlap in an interpretable way. It provides a direct signal of whether nearby points remain nearby after projection, which is useful for practical neighborhood-preservation checks.

Because it is simple to interpret and easy to compare across runs, it works well as a baseline local-fidelity signal in multi-reliability check sets.

## Related Metrics
Local Continuity Meta-Criterion is closest to Trustworthiness and Continuity, MRRE, and QNX because all are derived from neighborhood co-ranking behavior. They are useful for local-preservation analysis across neighborhood scales.

LCMC differs by centering on overlap with baseline correction. It is less directional than T&C and less rank-displacement-focused than MRRE.

## Task Alignment
This metric is best aligned to the task set implied by its structural role. The alignment basis is structural-granularity grouping from ZADU source note.
- Best-aligned tasks:
  - Neighborhood identification
  - Outlier identification
  - Cluster identification

Alignment here should be treated as a recommendation priority, not a hard constraint. If a project objective spans multiple task types, combine metrics from each relevant task family and require consistency before finalizing a method choice.

When alignment is uncertain, prefer conservative interpretation and run clarification questions again. The task decision should remain primary, and metric selection should follow that decision rather than drive it.

Operational alignment rule: this metric is strongest for neighborhood, outlier, and cluster-local tasks. For point-distance or density-focused tasks, use it as secondary reliability evidence rather than the main ranking signal.

## Interpretation Notes
Do not treat this metric as a standalone final decision criterion. Use it together with complementary metrics from other structural levels and keep preprocessing/seed policies fixed during comparison.

Use absolute values cautiously and prioritize relative comparisons under matched conditions. Threshold-style decisions without protocol control often produce false certainty, especially when datasets differ in scale, density, or class balance.

Before communicating a conclusion, cross-check this metric against the selected technique behavior and user-facing goal. A reliable recommendation should explain both why the score is good and why that goodness matters for the intended analytical action.

If this metric disagrees with other reliability checks, report the disagreement clearly and lower confidence instead of averaging the conflict away.

## Source Notes
The references below list paper sources used for this metric guidance.

- Quality assessment of dimensionality reduction: Rank-based criteria (John A. Lee, Michel Verleysen, Neurocomputing, 2009)
- Measuring and Explaining the Inter-Cluster Reliability of Multidimensional Projections (Hyeon Jeon; Hyung-Kwon Ko; Jaemin Jo; Youngtaek Kim; Jinwook Seo, IEEE Transactions on Visualization and Computer Graphics, 2021)
