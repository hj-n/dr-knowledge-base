# topo - Topographic Product

## Metric Definition
This metric evaluates neighborhood-order preservation in topology-oriented projections. It is sensitive to order distortions that may not appear in raw distance scores.

Operationally, treat this metric as a formal lens on one distortion family rather than a universal quality score. Two embeddings can rank differently depending on whether the task prioritizes local neighborhoods, global geometry, or class structure, so the definition should be interpreted together with explicit task intent.

For reproducible comparisons, keep preprocessing, distance definition, and evaluation protocol fixed while reading this metric. If those upstream choices change between runs, score differences often reflect evaluation drift rather than genuine embedding improvement.

## What It Quantifies
It quantifies neighborhood-order topology distortion and preservation strength. It is particularly useful for topological faithfulness diagnostics.

In practical analysis, this score is most useful when you pair it with the failure mode you are trying to detect. A score increase is meaningful only if it reduces errors that matter for the declared analytical task, not just because the numeric value is higher.

This is why the metric should be read as task-conditioned evidence. Use it to answer a concrete question about neighborhood stability, class organization, distance behavior, or density behavior, then validate that interpretation with at least one complementary metric.

## Computation Outline
This outline describes the typical computational flow used in DR evaluation practice. Exact formula details may vary by implementation, but the structure below is stable across references.
- Construct neighborhood-order relationships for original and projected data.
- Compute topographic-product statistic from ordering distortions.
- Interpret sign and magnitude with respect to order-preservation behavior.
- Use complementary metrics for broader reliability context.

The computation should be implemented with a stable protocol: identical sampling policy, consistent distance backend, and fixed tie-breaking behavior. Without these controls, the same embedding can yield materially different results across runs and tools.

When reporting values, record the full evaluation context including neighborhood scale, normalization policy, and whether labels were required. That metadata is part of the metric definition in practice because it determines what the reported number actually means.

Detailed protocol rule: apply consistent distance scaling and normalization policy before computing global metrics. Global score comparisons are invalid when scale handling differs across candidates.

## Hyperparameter Impact
Neighborhood-order configuration and output dimensionality are important controls. Order-definition details change sensitivity to topology distortions.

Hyperparameters should be tuned against the declared task, not against a single metric in isolation. Otherwise, optimization can overfit one structural aspect and silently degrade other structure that downstream users care about.

A robust workflow evaluates sensitivity with Bayesian optimization under fixed search bounds and checks rank stability across seeds or folds. Large score variance indicates that the current configuration is not yet reliable enough for high-confidence method selection.

Decision-level tuning rule: optimize this metric together with other task-relevant reliability checks, and report stability across multiple seeds or folds. Treat single-run gains as tentative until rankings stay consistent.

## Practical Reliability Notes
Topology-focused metrics capture structural events such as disconnected groups, bridges, or holes that may be invisible in average distance scores. They are especially useful when analysts care about cluster connectivity or separation order.

Topological signals are sensitive to neighborhood graph construction. Keep graph policy (k, radius, distance backend) fixed across comparisons; otherwise changes in topology metrics may reflect graph construction drift instead of embedding quality differences.

## Notable Properties
It targets order-preservation topology behavior explicitly. It should be combined with other metrics for a complete reliability diagnosis.

A strong property of this metric is that it provides a compact diagnostic that is easy to compare across methods. The limitation is that compactness hides where errors occur, so it should be supplemented by structure-level inspection when decisions are high impact.

In practice, use this metric together with local, global, and (when valid) label-based checks. This combined reading lowers the risk of choosing a method that scores well on one view but fails the actual analysis goal.

## Strengths
This metric is strong for topological neighborhood-preservation checks in map-like embeddings. It helps quantify topology quality beyond visual inspection alone.

It is particularly useful when preserving adjacency organization is more important than exact metric-distance calibration.


## Task Alignment
This metric is best aligned to the task set implied by its structural role. The alignment basis is structural-granularity grouping from ZADU source note.[^cat]
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

- Quantifying the Neighborhood Preservation of Self-Organizing Feature Maps (of Self/-Organizing F eature Maps, IEEE Transactions on Neural Networks, 1992)

- Charting a manifold (M. Brand, UNKNOWN, 2002)
- UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction (Leland McInnes et al., Journal of Open Source Software, 2020)
- High-dimensional labeled data analysis with topology representing graphs (Michaël Aupetit and Thibaud Catz, Proceedings of the IEEE, 2005)
- Nonlinear dimensionality reduction and data visualization: a review (Hujun Yin, International Journal of Automation and Computing, 2007)
- Evaluating multi-dimensional visualizations for understanding fuzzy clusters (Y . Zhao et al., BMC Bioinformatics, 2018)
- A methodology to compare Dimensionality Reduction algorithms in terms of loss of quality (A. Gracia et al., Information Sciences, 2014)

[^cat]: ZADU: A Python Library for Evaluating the Reliability of Dimensionality Reduction Embeddings (Hyeon Jeon et al., 2023 IEEE Visualization and Visual Analytics (VIS), 2023)
