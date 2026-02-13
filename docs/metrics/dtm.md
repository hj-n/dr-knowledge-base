# dtm - Distance-to-Measure

## Metric Definition
This metric uses measure-based distance geometry to evaluate global consistency under noisy sampling conditions. It is designed to remain informative under outliers and density irregularity.

Operationally, treat this metric as a formal lens on one distortion family rather than a universal quality score. Two embeddings can rank differently depending on whether the task prioritizes local neighborhoods, global geometry, or class structure, so the definition should be interpreted together with explicit task intent.

For reproducible comparisons, keep preprocessing, distance definition, and evaluation protocol fixed while reading this metric. If those upstream choices change between runs, score differences often reflect evaluation drift rather than genuine embedding improvement.

## What It Quantifies
It quantifies global geometric consistency under measure-based distance modeling. It is often interpreted with robustness emphasis when noise or outliers are present.

In practical analysis, this score is most useful when you pair it with the failure mode you are trying to detect. A score increase is meaningful only if it reduces errors that matter for the declared analytical task, not just because the numeric value is higher.

This is why the metric should be read as task-conditioned evidence. Use it to answer a concrete question about neighborhood stability, class organization, distance behavior, or density behavior, then validate that interpretation with at least one complementary metric.

## Computation Outline
This outline describes the typical computational flow used in DR evaluation practice. Exact formula details may vary by implementation, but the structure below is stable across references.
- Set measure/smoothing parameters for distance-to-measure computation.
- Compute distance-to-measure fields in original and projected spaces.
- Compare resulting global geometric structures.
- Aggregate discrepancy into a global robustness-oriented score.

The computation should be implemented with a stable protocol: identical sampling policy, consistent distance backend, and fixed tie-breaking behavior. Without these controls, the same embedding can yield materially different results across runs and tools.

When reporting values, record the full evaluation context including neighborhood scale, normalization policy, and whether labels were required. That metadata is part of the metric definition in practice because it determines what the reported number actually means.

Detailed protocol rule: apply consistent distance scaling and normalization policy before computing global metrics. Global score comparisons are invalid when scale handling differs across candidates.

## Hyperparameter Impact
Measure/smoothing parameters trade robustness against sensitivity. Distance-function choices can shift which global structures are emphasized.

Hyperparameters should be tuned against the declared task, not against a single metric in isolation. Otherwise, optimization can overfit one structural aspect and silently degrade other structure that downstream users care about.

A robust workflow evaluates sensitivity with Bayesian optimization under fixed search bounds and checks rank stability across seeds or folds. Large score variance indicates that the current configuration is not yet reliable enough for high-confidence method selection.

Decision-level tuning rule: optimize this metric together with other task-relevant reliability checks, and report stability across multiple seeds or folds. Treat single-run gains as tentative until rankings stay consistent.

## Practical Reliability Notes
DTM-style distances are sensitive to sampling density and neighborhood scale. In sparse regions, metric values can change more due to sample coverage than due to embedding quality itself, so interpretation should include data-density context.

For robust comparison, keep the same sample subset and distance backend across runs. If DTM disagrees with rank-based local metrics, do not collapse them into a single score immediately; inspect whether disagreement is concentrated in sparse tails, outliers, or class-boundary regions.

## Notable Properties
It is robustness-oriented and useful under outlier/noise conditions. It requires fixed parameterization to remain comparable across experiments.

A strong property of this metric is that it provides a compact diagnostic that is easy to compare across methods. The limitation is that compactness hides where errors occur, so it should be supplemented by structure-level inspection when decisions are high impact.

In practice, use this metric together with local, global, and (when valid) label-based checks. This combined reading lowers the risk of choosing a method that scores well on one view but fails the actual analysis goal.

## Strengths
This metric is strong for measure-based geometric reliability checks, especially when robustness to noise and irregular sampling matters. It can provide a more stable global-structure signal than raw pairwise-distance-only summaries in some regimes.

It is useful when analysts need a geometry-aware global diagnostic that is less tied to a single embedding-scale convention.


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

- Geometric Inference for Measures based on Distance Functions (Frédéric Chazal et al., Foundations of Computational Mathematics, 2010)
- Classes are Not Clusters: Improving Label-Based Evaluation of Dimensionality Reduction (Hyeon Jeon et al., IEEE Transactions on Visualization and Computer Graphics, 2024)

- Uniform manifold approximation with two-phase optimization (H. Jeon et al., 2022 IEEE Visualization and Visual Analytics (VIS), 2022)
- VisCoDeR: A tool for visually comparing dimensionality reduction algorithms (René Cutura et al., UNKNOWN, 2018)
- A Large-Scale Sensitivity Analysis on Latent Embeddings and Dimensionality Reductions for Text Spatializations (D. Atzberger et al., IEEE Transactions on Visualization and Computer Graphics, 2025)

[^cat]: ZADU: A Python Library for Evaluating the Reliability of Dimensionality Reduction Embeddings (Hyeon Jeon et al., 2023 IEEE Visualization and Visual Analytics (VIS), 2023)
