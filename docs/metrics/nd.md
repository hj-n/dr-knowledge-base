# nd - Neighbor Dissimilarity

## Metric Definition
This metric quantifies neighborhood-structure change as a dissimilarity signal. It is useful when the main concern is whether local graph structure has shifted.

Operationally, treat this metric as a formal lens on one distortion family rather than a universal quality score. Two embeddings can rank differently depending on whether the task prioritizes local neighborhoods, global geometry, or class structure, so the definition should be interpreted together with explicit task intent.

For reproducible comparisons, keep preprocessing, distance definition, and evaluation protocol fixed while reading this metric. If those upstream choices change between runs, score differences often reflect evaluation drift rather than genuine embedding improvement.

## What It Quantifies
It quantifies how strongly neighborhood membership and shape change under projection. Higher dissimilarity implies larger local-structure drift.

In practical analysis, this score is most useful when you pair it with the failure mode you are trying to detect. A score increase is meaningful only if it reduces errors that matter for the declared analytical task, not just because the numeric value is higher.

This is why the metric should be read as task-conditioned evidence. Use it to answer a concrete question about neighborhood stability, class organization, distance behavior, or density behavior, then validate that interpretation with at least one complementary metric.

## Computation Outline
This outline describes the typical computational flow used in DR evaluation practice. Exact formula details may vary by implementation, but the structure below is stable across references.
- Construct neighborhood graphs (typically kNN) in both spaces.
- Compare adjacency/membership patterns for each sample.
- Compute dissimilarity score per sample.
- Aggregate to dataset-level neighbor dissimilarity.

The computation should be implemented with a stable protocol: identical sampling policy, consistent distance backend, and fixed tie-breaking behavior. Without these controls, the same embedding can yield materially different results across runs and tools.

When reporting values, record the full evaluation context including neighborhood scale, normalization policy, and whether labels were required. That metadata is part of the metric definition in practice because it determines what the reported number actually means.

Detailed protocol rule: evaluate multiple neighborhood scales (for example small/medium/local-range k values) and keep the same k schedule across methods. Local metrics should be read as scale-dependent curves, not single-point truths.

## Hyperparameter Impact
kNN construction policy determines sensitivity to local graph changes. Distance metric choice affects absolute score scale and cross-method comparisons.

Hyperparameters should be tuned against the declared task, not against a single metric in isolation. Otherwise, optimization can overfit one structural aspect and silently degrade other structure that downstream users care about.

A robust workflow evaluates sensitivity with Bayesian optimization under fixed search bounds and checks rank stability across seeds or folds. Large score variance indicates that the current configuration is not yet reliable enough for high-confidence method selection.

Decision-level tuning rule: tune this metric only inside a task-aligned bundle objective and report sensitivity across multiple seeds or folds. Single-run improvements should be treated as provisional until rank stability is confirmed.

## Practical Reliability Notes
Neighbor dissimilarity responds strongly to graph-construction policy. Small differences in kNN tie-breaking, metric backend, or duplicate handling can change ND values even on the same embedding.

For reliability-focused comparisons, freeze graph policy and run seed-stability checks for stochastic methods. If ND ranking is unstable across seeds while other local metrics are stable, treat ND as exploratory evidence and avoid over-weighting it in final selection.

## Notable Properties
It directly reflects neighborhood-graph distortion behavior. It complements global metrics by exposing local structural drift patterns.

A strong property of this metric is that it provides a compact diagnostic that is easy to compare across methods. The limitation is that compactness hides where errors occur, so it should be supplemented by structure-level inspection when decisions are high impact.

In review workflows, this metric works best as one component in a bundle: local, global, and label-aware signals together. That bundle-based interpretation reduces the chance of selecting a method that is numerically strong but operationally misaligned.

## Strengths
This metric is strong for detecting neighbor-composition changes that may not be obvious from aggregate distance statistics. It helps identify whether local neighborhood membership is drifting even when broad global structure appears stable.

It is useful as a safety check metric in local/cluster workflows where subtle neighbor swaps can alter downstream interpretation.

## Related Metrics
Neighbor Dissimilarity is partially aligned with Trustworthiness/Continuity and MRRE because it tracks neighborhood-change behavior. In workflow practice it is often used with other local metrics rather than alone.

Its computation style is matrix/distribution dissimilarity based, so it should not be treated as a direct substitute for co-ranking formulas such as T&C or LCMC.

## Task Alignment
This metric is best aligned to the task set implied by its structural role. The alignment basis is structural-granularity grouping from ZADU source note.
- Best-aligned tasks:
  - Neighborhood identification
  - Outlier identification
  - Cluster identification

Alignment here should be treated as a recommendation priority, not a hard constraint. If a project objective spans multiple task types, combine metrics from each relevant task family and require consistency before finalizing a method choice.

When alignment is uncertain, prefer conservative interpretation and run clarification questions again. The task decision should remain primary, and metric selection should follow that decision rather than drive it.

Operational alignment rule: this metric is strongest for neighborhood, outlier, and cluster-local tasks. For point-distance or density-dominant tasks, keep it as safety check evidence rather than primary ranking evidence.

## Interpretation Notes
Do not treat this metric as a standalone final decision criterion. Use it together with complementary metrics from other structural levels and keep preprocessing/seed policies fixed during comparison.

Use absolute values cautiously and prioritize relative comparisons under matched conditions. Threshold-style decisions without protocol control often produce false certainty, especially when datasets differ in scale, density, or class balance.

Before communicating a conclusion, cross-check this metric against the selected technique behavior and user-facing goal. A reliable recommendation should explain both why the score is good and why that goodness matters for the intended analytical action.

Failure-signaling rule: if this metric disagrees with other bundle metrics, report that disagreement explicitly and mark recommendation confidence as reduced instead of averaging away the conflict.

## Source Notes
The references below list paper sources used for this metric guidance.

- Feature Learning for Nonlinear Dimensionality Reduction toward Maximal Extraction of Hidden Patterns (Takanori Fujiwara, Yun-Hsin Kuo, Anders Ynnerman, Kwan-Liu Ma, 2023 IEEE 16th Pacific Visualization Symposium (PacificVis), 2023)
