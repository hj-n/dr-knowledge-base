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

A robust workflow evaluates sensitivity by sweeping key controls and checking rank stability across seeds or folds. Large score variance indicates that the current configuration is not yet reliable enough for high-confidence method selection.

Decision-level tuning rule: tune this metric only inside a task-aligned bundle objective and report sensitivity across multiple seeds or folds. Single-run improvements should be treated as provisional until rank stability is confirmed.

## Practical Reliability Notes
DTM-style distances are sensitive to sampling density and neighborhood scale. In sparse regions, metric values can change more due to sample coverage than due to embedding quality itself, so interpretation should include data-density context.

For robust comparison, keep the same sample subset and distance backend across runs. If DTM disagrees with rank-based local metrics, do not collapse them into a single score immediately; inspect whether disagreement is concentrated in sparse tails, outliers, or class-boundary regions.

## Notable Properties
It is robustness-oriented and useful under outlier/noise conditions. It requires fixed parameterization to remain comparable across experiments.

A strong property of this metric is that it provides a compact diagnostic that is easy to compare across methods. The limitation is that compactness hides where errors occur, so it should be supplemented by structure-level inspection when decisions are high impact.

In review workflows, this metric works best as one component in a bundle: local, global, and label-aware signals together. That bundle-based interpretation reduces the chance of selecting a method that is numerically strong but operationally misaligned.

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

Operational alignment rule: use this metric as primary evidence for point-distance, cluster-distance, or density tasks; use as secondary guardrail for neighborhood tasks.

## Interpretation Notes
Do not treat this metric as a standalone final decision criterion. Use it together with complementary metrics from other structural levels and keep preprocessing/seed policies fixed during comparison.

Use absolute values cautiously and prioritize relative comparisons under matched conditions. Threshold-style decisions without protocol control often produce false certainty, especially when datasets differ in scale, density, or class balance.

Before communicating a conclusion, cross-check this metric against the selected technique behavior and user-facing goal. A reliable recommendation should explain both why the score is good and why that goodness matters for the intended analytical action.

Failure-signaling rule: if this metric disagrees with other bundle metrics, report that disagreement explicitly and mark recommendation confidence as reduced instead of averaging away the conflict.

## Source Notes
The links below map this metric to claim-level evidence extracted from individual source notes. Use these links when tracing recommendations back to evidence.

- `papers/notes/zadu-ref-13-ref03-geometric-inference-for-probability-measures.md` -> `CLAIM-METRIC-DTM-SOURCE-13`
- `papers/notes/zadu-ref-11-jeon23tvcg-4.md` -> `CLAIM-METRIC-DTM-SOURCE-11`

- `papers/notes/pending-ref-009-uniform-manifold-approximation-with-two-phase-optimization.md` (pending-reference evidence)
- `papers/notes/pending-ref-024-viscoder-a-tool-for-visually-comparing-dimensionality-redu.md` (pending-reference evidence)
- `papers/notes/pending-ref-054-a-large-scale-sensitivity-analysis-on-latent-embeddings-an.md` (pending-reference evidence)

[^cat]: Category source note: `papers/notes/2023-zadu-library.md` (ZADU23-E5).
