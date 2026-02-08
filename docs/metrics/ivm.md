# ivm - Internal Validation Measure

## Metric Definition
This metric uses internal clustering validation behavior as an embedding reliability signal. It reflects compactness/separation quality under a chosen clustering protocol.

Operationally, treat this metric as a formal lens on one distortion family rather than a universal quality score. Two embeddings can rank differently depending on whether the task prioritizes local neighborhoods, global geometry, or class structure, so the definition should be interpreted together with explicit task intent.

For reproducible comparisons, keep preprocessing, distance definition, and evaluation protocol fixed while reading this metric. If those upstream choices change between runs, score differences often reflect evaluation drift rather than genuine embedding improvement.

## What It Quantifies
It quantifies clustering quality signal under internal validation criteria. Interpretation depends on the exact internal index used by the pipeline.

In practical analysis, this score is most useful when you pair it with the failure mode you are trying to detect. A score increase is meaningful only if it reduces errors that matter for the declared analytical task, not just because the numeric value is higher.

This is why the metric should be read as task-conditioned evidence. Use it to answer a concrete question about neighborhood stability, class organization, distance behavior, or density behavior, then validate that interpretation with at least one complementary metric.

## Computation Outline
This outline describes the typical computational flow used in DR evaluation practice. Exact formula details may vary by implementation, but the structure below is stable across references.
- Cluster embedded points using a fixed clustering setup.
- Compute internal validation index on resulting clusters.
- Map index value to reliability interpretation under the chosen convention.
- Use identical clustering settings for fair method comparison.

The computation should be implemented with a stable protocol: identical sampling policy, consistent distance backend, and fixed tie-breaking behavior. Without these controls, the same embedding can yield materially different results across runs and tools.

When reporting values, record the full evaluation context including neighborhood scale, normalization policy, and whether labels were required. That metadata is part of the metric definition in practice because it determines what the reported number actually means.

## Hyperparameter Impact
Clustering algorithm settings and number-of-clusters policy are primary controls. Internal validation index choice changes score semantics and thresholds.
The label-separation gate is mandatory before strong interpretation in labeled settings.[^warn-label]

Hyperparameters should be tuned against the declared task, not against a single metric in isolation. Otherwise, optimization can overfit one structural aspect and silently degrade other structure that downstream users care about.

A robust workflow evaluates sensitivity by sweeping key controls and checking rank stability across seeds or folds. Large score variance indicates that the current configuration is not yet reliable enough for high-confidence method selection.

## Notable Properties
It can summarize cluster-quality behavior compactly. It is highly dependent on clustering setup and should not be treated as method-intrinsic in isolation.

A strong property of this metric is that it provides a compact diagnostic that is easy to compare across methods. The limitation is that compactness hides where errors occur, so it should be supplemented by structure-level inspection when decisions are high impact.

In review workflows, this metric works best as one component in a bundle: local, global, and label-aware signals together. That bundle-based interpretation reduces the chance of selecting a method that is numerically strong but operationally misaligned.

## Strengths
This metric is strong for embedding quality assessment through internal clustering validity behavior. It helps evaluate whether projected cluster structure is compact and separable under a fixed clustering protocol.

It is useful when cluster recoverability is a primary decision criterion and clustering settings are controlled consistently.


## Task Alignment
This metric is best aligned to the task set implied by its structural role. The alignment basis is structural-granularity grouping from ZADU source note.[^cat]
- Best-aligned tasks:
  - Cluster identification
  - Class separability investigation
  - Cluster distance investigation

Alignment here should be treated as a recommendation priority, not a hard constraint. If a project objective spans multiple task types, combine metrics from each relevant task family and require consistency before finalizing a method choice.

When alignment is uncertain, prefer conservative interpretation and run clarification questions again. The task decision should remain primary, and metric selection should follow that decision rather than drive it.

## Interpretation Notes
Do not treat this metric as a standalone final decision criterion. Use it together with complementary metrics from other structural levels and keep preprocessing/seed policies fixed during comparison.

Use absolute values cautiously and prioritize relative comparisons under matched conditions. Threshold-style decisions without protocol control often produce false certainty, especially when datasets differ in scale, density, or class balance.

Before communicating a conclusion, cross-check this metric against the selected technique behavior and user-facing goal. A reliable recommendation should explain both why the score is good and why that goodness matters for the intended analytical action.

## Source Notes
The links below map this metric to claim-level evidence extracted from individual source notes. Use these links when tracing recommendations back to evidence.
- `papers/notes/zadu-ref-18-ref18-measuring-and-explaining-the-inter-cluster-reliability-of-multidimensional.md` -> `CLAIM-METRIC-IVM-SOURCE-18`
- `papers/notes/zadu-ref-19-ref42-a-comparison-for-dimensionality-reduction-methods-of-single-cell-rna-seq-d.md` -> `CLAIM-METRIC-IVM-SOURCE-19`
- `papers/notes/zadu-ref-08-local-affine-multidimensional-projection-1.md` -> `CLAIM-METRIC-IVM-SOURCE-08`
- `papers/notes/zadu-ref-11-jeon23tvcg-4.md` -> `CLAIM-METRIC-IVM-SOURCE-11`

[^cat]: Category source note: `papers/notes/2023-zadu-library.md` (ZADU23-E4).
[^warn-label]: Warning source note: `papers/notes/2026-zadu-readme-warning.md` (ZADU-RM-E1, ZADU-RM-E2).
