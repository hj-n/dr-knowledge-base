# tnc - Trustworthiness & Continuity

## Metric Definition
This metric evaluates local neighborhood fidelity in both directions, not just one side of the mapping. It penalizes false neighbors introduced in the embedding and true neighbors that were lost from the original space.

Operationally, treat this metric as a formal lens on one distortion family rather than a universal quality score. Two embeddings can rank differently depending on whether the task prioritizes local neighborhoods, global geometry, or class structure, so the definition should be interpreted together with explicit task intent.

For reproducible comparisons, keep preprocessing, distance definition, and evaluation protocol fixed while reading this metric. If those upstream choices change between runs, score differences often reflect evaluation drift rather than genuine embedding improvement.

## What It Quantifies
It quantifies bidirectional neighborhood rank distortion and balances intrusion versus omission errors. A high-quality embedding typically shows high trustworthiness and high continuity over the task-relevant neighborhood scales.

In practical analysis, this score is most useful when you pair it with the failure mode you are trying to detect. A score increase is meaningful only if it reduces errors that matter for the declared analytical task, not just because the numeric value is higher.

This is why the metric should be read as task-conditioned evidence. Use it to answer a concrete question about neighborhood stability, class organization, distance behavior, or density behavior, then validate that interpretation with at least one complementary metric.

## Computation Outline
This outline describes the typical computational flow used in DR evaluation practice. Exact formula details may vary by implementation, but the structure below is stable across references.
- Choose neighborhood size `k` (or a range of `k` values).
- Compute neighborhood ranks in high- and low-dimensional spaces.
- Apply trustworthiness penalties for low-space intrusions and continuity penalties for missed high-space neighbors.
- Average scores across points and optionally aggregate across the `k` schedule.

The computation should be implemented with a stable protocol: identical sampling policy, consistent distance backend, and fixed tie-breaking behavior. Without these controls, the same embedding can yield materially different results across runs and tools.

When reporting values, record the full evaluation context including neighborhood scale, normalization policy, and whether labels were required. That metadata is part of the metric definition in practice because it determines what the reported number actually means.

## Hyperparameter Impact
Neighborhood size `k` is the primary control and strongly changes locality scale. Distance metric, tie-handling, and neighborhood construction policy can also alter score stability.

Hyperparameters should be tuned against the declared task, not against a single metric in isolation. Otherwise, optimization can overfit one structural aspect and silently degrade other structure that downstream users care about.

A robust workflow evaluates sensitivity by sweeping key controls and checking rank stability across seeds or folds. Large score variance indicates that the current configuration is not yet reliable enough for high-confidence method selection.

## Notable Properties
It offers a bidirectional local-fidelity view instead of a single-direction error. It is typically more diagnostic than one-sided neighborhood metrics when tuning local structure behavior.

A strong property of this metric is that it provides a compact diagnostic that is easy to compare across methods. The limitation is that compactness hides where errors occur, so it should be supplemented by structure-level inspection when decisions are high impact.

In review workflows, this metric works best as one component in a bundle: local, global, and label-aware signals together. That bundle-based interpretation reduces the chance of selecting a method that is numerically strong but operationally misaligned.

## Strengths
This metric is strong at detecting bidirectional local-neighborhood distortions, because it penalizes both false neighbors introduced in the embedding and true neighbors that were dropped. It is usually more diagnostic than one-sided neighborhood scores when local structure quality is the core concern.

It is especially useful during model comparison, because it exposes whether a method is trading trustworthiness for continuity (or vice versa) across neighborhood scales rather than preserving both consistently.


## Task Alignment
This metric is best aligned to the task set implied by its structural role. The alignment basis is structural-granularity grouping from ZADU source note.[^cat]
- Best-aligned tasks:
  - Neighborhood identification
  - Outlier identification
  - Cluster identification

Alignment here should be treated as a recommendation priority, not a hard constraint. If a project objective spans multiple task types, combine metrics from each relevant task family and require consistency before finalizing a method choice.

When alignment is uncertain, prefer conservative interpretation and run clarification questions again. The task decision should remain primary, and metric selection should follow that decision rather than drive it.

## Interpretation Notes
Do not treat this metric as a standalone final decision criterion. Use it together with complementary metrics from other structural levels and keep preprocessing/seed policies fixed during comparison.

Use absolute values cautiously and prioritize relative comparisons under matched conditions. Threshold-style decisions without protocol control often produce false certainty, especially when datasets differ in scale, density, or class balance.

Before communicating a conclusion, cross-check this metric against the selected technique behavior and user-facing goal. A reliable recommendation should explain both why the score is good and why that goodness matters for the intended analytical action.

## Source Notes
The links below map this metric to claim-level evidence extracted from individual source notes. Use these links when tracing recommendations back to evidence.
- `papers/notes/zadu-ref-03-2408-07724v2.md` -> `CLAIM-METRIC-TNC-SOURCE-03`
- `papers/notes/zadu-ref-18-ref18-measuring-and-explaining-the-inter-cluster-reliability-of-multidimensional.md` -> `CLAIM-METRIC-TNC-SOURCE-18`
- `papers/notes/zadu-ref-07-local-multidimensional-scaling-for-nonlinear-dimension-reduction-graph-drawing-a.md` -> `CLAIM-METRIC-TNC-SOURCE-07`
- `papers/notes/zadu-ref-01-1-s2-0-s0893608006000724-main.md` -> `CLAIM-METRIC-TNC-SOURCE-01`
- `papers/notes/zadu-ref-02-1-s2-0-s0925231209000101-main.md` -> `CLAIM-METRIC-TNC-SOURCE-02`
- `papers/notes/zadu-ref-08-local-affine-multidimensional-projection-1.md` -> `CLAIM-METRIC-TNC-SOURCE-08`
- Additional supporting notes: 4 more

[^cat]: Category source note: `papers/notes/2023-zadu-library.md` (ZADU23-E3).
