# proc - Procrustes Measure

## Metric Definition
This metric measures local shape agreement using Procrustes alignment residuals. It captures geometric neighborhood distortion beyond set overlap counts.

Operationally, treat this metric as a formal lens on one distortion family rather than a universal quality score. Two embeddings can rank differently depending on whether the task prioritizes local neighborhoods, global geometry, or class structure, so the definition should be interpreted together with explicit task intent.

For reproducible comparisons, keep preprocessing, distance definition, and evaluation protocol fixed while reading this metric. If those upstream choices change between runs, score differences often reflect evaluation drift rather than genuine embedding improvement.

## What It Quantifies
It quantifies local-shape mismatch after optimal alignment of corresponding neighborhoods. Lower residual error generally indicates stronger local geometric preservation.

In practical analysis, this score is most useful when you pair it with the failure mode you are trying to detect. A score increase is meaningful only if it reduces errors that matter for the declared analytical task, not just because the numeric value is higher.

This is why the metric should be read as task-conditioned evidence. Use it to answer a concrete question about neighborhood stability, class organization, distance behavior, or density behavior, then validate that interpretation with at least one complementary metric.

## Computation Outline
This outline describes the typical computational flow used in DR evaluation practice. Exact formula details may vary by implementation, but the structure below is stable across references.
- Define corresponding local neighborhoods in both spaces.
- Align local neighborhoods via Procrustes transformation.
- Compute residual alignment error per neighborhood.
- Aggregate residuals into final local-shape reliability score.

The computation should be implemented with a stable protocol: identical sampling policy, consistent distance backend, and fixed tie-breaking behavior. Without these controls, the same embedding can yield materially different results across runs and tools.

When reporting values, record the full evaluation context including neighborhood scale, normalization policy, and whether labels were required. That metadata is part of the metric definition in practice because it determines what the reported number actually means.

Detailed protocol rule: evaluate multiple neighborhood scales (for example small/medium/local-range k values) and keep the same k schedule across methods. Local metrics should be read as scale-dependent curves, not single-point truths.

## Hyperparameter Impact
Neighborhood size and alignment settings determine local-shape sensitivity. Normalization policy affects absolute residual magnitude and comparison fairness.

Hyperparameters should be tuned against the declared task, not against a single metric in isolation. Otherwise, optimization can overfit one structural aspect and silently degrade other structure that downstream users care about.

A robust workflow evaluates sensitivity with Bayesian optimization under fixed search bounds and checks rank stability across seeds or folds. Large score variance indicates that the current configuration is not yet reliable enough for high-confidence method selection.

Decision-level tuning rule: optimize this metric together with other task-relevant reliability checks, and report stability across multiple seeds or folds. Treat single-run gains as tentative until rankings stay consistent.

## Practical Reliability Notes
Procrustes-based metrics compare structures after optimal rigid alignment (translation, rotation, scaling). They are useful for checking shape-level agreement independent of axis orientation, which is valuable when embeddings are compared across runs or methods.

Because Procrustes suppresses orientation differences, it may hide local neighborhood defects. Use it together with local rank-based metrics when the analytical task depends on neighborhood identity, not only coarse shape similarity.

## Notable Properties
It captures local geometric-shape distortion beyond neighbor membership overlap. It complements rank/membership metrics with shape-aware information.

A strong property of this metric is that it provides a compact diagnostic that is easy to compare across methods. The limitation is that compactness hides where errors occur, so it should be supplemented by structure-level inspection when decisions are high impact.

In practice, use this metric together with local, global, and (when valid) label-based checks. This combined reading lowers the risk of choosing a method that scores well on one view but fails the actual analysis goal.

## Strengths
This metric is strong for local shape-consistency analysis through Procrustes-style alignment. It detects local geometric deformation patterns that simple neighbor overlap measures may miss.

It is useful when local manifold shape fidelity matters for interpretation, not only neighborhood membership.


## Task Alignment
This metric is best aligned to the task set implied by its structural role. The alignment basis is structural-granularity grouping from ZADU source note.[^cat]
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

- Feature Learning for Nonlinear Dimensionality Reduction toward Maximal Extraction of Hidden Patterns (Takanori Fujiwara et al., 2023 IEEE 16th Pacific Visualization Symposium (PacificVis), 2023)
- Local Affine Multidimensional Projection (theory to build accurate local transformations that can be dynamically modiﬁed according to user knowledge. The accuracy et al., IEEE Transactions on Visualization and Computer Graphics, 2011)
- Mach Learn (2009) 77: 1–25 (Yair Goldberg et al., Machine Learning, 2009)

- Feature Learning for Nonlinear Dimensionality Reduction toward Maximal Extraction of Hidden Patterns (Takanori Fujiwara et al., 2023 IEEE 16th Pacific Visualization Symposium (PacificVis), 2023)
- Stability Comparison of Dimensionality Reduction Techniques Attending to Data and Parameter Variations (Francisco J. García-Fernández et al., UNKNOWN, 2013)
- Interactive Dimensionality Reduction for Comparative Analysis (Takanori Fujiwara et al., IEEE Transactions on Visualization and Computer Graphics, 2022)
- t-viSNE: Interactive Assessment and Interpretation of t-SNE Projections (Angelos Chatzimparmpas et al., IEEE Transactions on Visualization and Computer Graphics, 2020)
- Local procrustes for manifold embedding: A measure of embedding quality and embedding algorithms (Y. Goldberg and Y. Ritov, Machine Learning, 2009)
- ClassiMap: A new dimension reduction technique for exploratory data analysis of labeled data (S. Lespinats et al., International Journal of Pattern Recognition and Artificial Intelligence, 2015)

[^cat]: ZADU: A Python Library for Evaluating the Reliability of Dimensionality Reduction Embeddings (Hyeon Jeon et al., 2023 IEEE Visualization and Visual Analytics (VIS), 2023)
