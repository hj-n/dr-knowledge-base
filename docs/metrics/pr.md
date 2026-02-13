# pr - Pearson's Correlation Coefficient

## Metric Definition
This metric measures linear correlation between pairwise distance vectors from original and projected spaces. It evaluates global distance agreement under a linear relationship assumption.

Operationally, treat this metric as a formal lens on one distortion family rather than a universal quality score. Two embeddings can rank differently depending on whether the task prioritizes local neighborhoods, global geometry, or class structure, so the definition should be interpreted together with explicit task intent.

For reproducible comparisons, keep preprocessing, distance definition, and evaluation protocol fixed while reading this metric. If those upstream choices change between runs, score differences often reflect evaluation drift rather than genuine embedding improvement.

## What It Quantifies
It quantifies linear agreement of pairwise-distance patterns between spaces. Values closer to 1 indicate strong linear global agreement.

In practical analysis, this score is most useful when you pair it with the failure mode you are trying to detect. A score increase is meaningful only if it reduces errors that matter for the declared analytical task, not just because the numeric value is higher.

This is why the metric should be read as task-conditioned evidence. Use it to answer a concrete question about neighborhood stability, class organization, distance behavior, or density behavior, then validate that interpretation with at least one complementary metric.

## Computation Outline
This outline describes the typical computational flow used in DR evaluation practice. Exact formula details may vary by implementation, but the structure below is stable across references.
- Compute pairwise distances in original and projected spaces.
- Vectorize corresponding distance entries.
- Compute Pearson correlation between the two vectors.
- Report coefficient as global linear-agreement score.

The computation should be implemented with a stable protocol: identical sampling policy, consistent distance backend, and fixed tie-breaking behavior. Without these controls, the same embedding can yield materially different results across runs and tools.

When reporting values, record the full evaluation context including neighborhood scale, normalization policy, and whether labels were required. That metadata is part of the metric definition in practice because it determines what the reported number actually means.

Detailed protocol rule: apply consistent distance scaling and normalization policy before computing global metrics. Global score comparisons are invalid when scale handling differs across candidates.

## Hyperparameter Impact
Distance metric and preprocessing scale directly affect correlation. Pairwise sampling strategy (full vs subset) changes estimate variance.

Hyperparameters should be tuned against the declared task, not against a single metric in isolation. Otherwise, optimization can overfit one structural aspect and silently degrade other structure that downstream users care about.

A robust workflow evaluates sensitivity with Bayesian optimization under fixed search bounds and checks rank stability across seeds or folds. Large score variance indicates that the current configuration is not yet reliable enough for high-confidence method selection.

Decision-level tuning rule: tune this metric only inside a task-aligned bundle objective and report sensitivity across multiple seeds or folds. Single-run improvements should be treated as provisional until rank stability is confirmed.

## Practical Reliability Notes
Pearson-style correlation is a coarse global trend indicator and can remain high even when local neighborhoods are heavily damaged. It is best for detecting monotonic global agreement, not for validating neighborhood-level interpretability.

In workflow decisions, treat PR as a safety check for distance-oriented tasks. If PR is high but local metrics are poor, report that global trend is preserved while local reliability is not, and avoid using the embedding for neighborhood-sensitive analysis.

## Notable Properties
It is straightforward to interpret as global linear agreement. It does not capture non-linear monotonic agreement as well as rank-based alternatives.

A strong property of this metric is that it provides a compact diagnostic that is easy to compare across methods. The limitation is that compactness hides where errors occur, so it should be supplemented by structure-level inspection when decisions are high impact.

In review workflows, this metric works best as one component in a bundle: local, global, and label-aware signals together. That bundle-based interpretation reduces the chance of selecting a method that is numerically strong but operationally misaligned.

## Strengths
This metric is strong for linear agreement checks of pairwise relationships between spaces. It is simple, fast, and useful for detecting broad global trend preservation in distance behavior.

It works well as a coarse global sanity check before deeper non-linear or rank-based diagnostics.

## Related Metrics
Pearson correlation is closest to Spearman correlation and stress-family metrics as a global relationship check between original and embedded pairwise distances.

It differs from Spearman by measuring linear association rather than rank-order association.

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

Failure-signaling rule: if this metric disagrees with other bundle metrics, report that disagreement explicitly and mark recommendation confidence as reduced instead of averaging away the conflict.

## Source Notes
The references below list paper sources used for this metric guidance.

- Steering Distortions to Preserve Classes and Neighbors in Supervised Dimensionality Reduction (Benoit Colange, Jaakko Peltonen, Michael Aupetit, Denys Dutykh, Sylvain Lespinats, Advances in Neural Information Processing Systems (NeurIPS), 2020)
- Feature Learning for Nonlinear Dimensionality Reduction toward Maximal Extraction of Hidden Patterns (Takanori Fujiwara, Yun-Hsin Kuo, Anders Ynnerman, Kwan-Liu Ma, 2023 IEEE 16th Pacific Visualization Symposium (PacificVis), 2023)
- How Scale Breaks “Normalized Stress” and KL Divergence: Rethinking Quality Metrics (Kiran Smelser, Kaviru Gunaratne, Jacob Miller, Stephen Kobourov, IEEE Transactions on Visualization and Computer Graphics, 2024)
