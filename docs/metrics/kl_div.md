# kl_div - Kullback-Leibler Divergence

## Metric Definition
This metric measures divergence between neighborhood probability distributions across spaces. It is central in probabilistic neighborhood embedding objectives.

Operationally, treat this metric as a formal lens on one distortion family rather than a universal quality score. Two embeddings can rank differently depending on whether the task prioritizes local neighborhoods, global geometry, or class structure, so the definition should be interpreted together with explicit task intent.

For reproducible comparisons, keep preprocessing, distance definition, and evaluation protocol fixed while reading this metric. If those upstream choices change between runs, score differences often reflect evaluation drift rather than genuine embedding improvement.

## What It Quantifies
It quantifies divergence between high-space and low-space neighborhood probability distributions. Lower divergence generally indicates better probabilistic neighborhood preservation.

In practical analysis, this score is most useful when you pair it with the failure mode you are trying to detect. A score increase is meaningful only if it reduces errors that matter for the declared analytical task, not just because the numeric value is higher.

This is why the metric should be read as task-conditioned evidence. Use it to answer a concrete question about neighborhood stability, class organization, distance behavior, or density behavior, then validate that interpretation with at least one complementary metric.

## Computation Outline
This outline describes the typical computational flow used in DR evaluation practice. Exact formula details may vary by implementation, but the structure below is stable across references.
- Build high-space neighborhood probability distribution `P`.
- Build low-space neighborhood probability distribution `Q`.
- Compute divergence term (typically `KL(P||Q)` or objective-equivalent form).
- Aggregate as global score or optimization objective.

The computation should be implemented with a stable protocol: identical sampling policy, consistent distance backend, and fixed tie-breaking behavior. Without these controls, the same embedding can yield materially different results across runs and tools.

When reporting values, record the full evaluation context including neighborhood scale, normalization policy, and whether labels were required. That metadata is part of the metric definition in practice because it determines what the reported number actually means.

## Hyperparameter Impact
Neighborhood probability construction parameters strongly affect divergence behavior. Scale handling and probability calibration policy are critical for fair comparisons.
Scale policy must be explicit when comparing values across runs or methods.[^warn-scale]

Hyperparameters should be tuned against the declared task, not against a single metric in isolation. Otherwise, optimization can overfit one structural aspect and silently degrade other structure that downstream users care about.

A robust workflow evaluates sensitivity by sweeping key controls and checking rank stability across seeds or folds. Large score variance indicates that the current configuration is not yet reliable enough for high-confidence method selection.

## Notable Properties
It captures probability-level neighborhood mismatch, not only distance mismatch. It can be optimization-sensitive and should be interpreted with scale policy documented.

A strong property of this metric is that it provides a compact diagnostic that is easy to compare across methods. The limitation is that compactness hides where errors occur, so it should be supplemented by structure-level inspection when decisions are high impact.

In review workflows, this metric works best as one component in a bundle: local, global, and label-aware signals together. That bundle-based interpretation reduces the chance of selecting a method that is numerically strong but operationally misaligned.

## Strengths
This metric is strong for probability-structure mismatch analysis between high- and low-dimensional neighbor distributions. It is sensitive to local probabilistic distortion patterns that distance-only metrics can miss.

It is particularly informative when comparing neighborhood-probability-preserving techniques or when auditing optimization behavior tied to divergence objectives.


## Task Alignment
This metric is best aligned to the task set implied by its structural role. The alignment basis is structural-granularity grouping from ZADU source note.[^cat]
- Best-aligned tasks:
  - Point distance investigation
  - Class separability investigation
  - Cluster distance investigation
  - Cluster density investigation

Alignment here should be treated as a recommendation priority, not a hard constraint. If a project objective spans multiple task types, combine metrics from each relevant task family and require consistency before finalizing a method choice.

When alignment is uncertain, prefer conservative interpretation and run clarification questions again. The task decision should remain primary, and metric selection should follow that decision rather than drive it.

## Interpretation Notes
Do not treat this metric as a standalone final decision criterion. Use it together with complementary metrics from other structural levels and keep preprocessing/seed policies fixed during comparison.

Use absolute values cautiously and prioritize relative comparisons under matched conditions. Threshold-style decisions without protocol control often produce false certainty, especially when datasets differ in scale, density, or class balance.

Before communicating a conclusion, cross-check this metric against the selected technique behavior and user-facing goal. A reliable recommendation should explain both why the score is good and why that goodness matters for the intended analytical action.

## Source Notes
The links below map this metric to claim-level evidence extracted from individual source notes. Use these links when tracing recommendations back to evidence.
- `papers/notes/zadu-ref-03-2408-07724v2.md` -> `CLAIM-METRIC-KL_DIV-SOURCE-03`
- `papers/notes/zadu-ref-17-ref13-stochastic-neighbor-embedding.md` -> `CLAIM-METRIC-KL_DIV-SOURCE-17`
- `papers/notes/zadu-ref-11-jeon23tvcg-4.md` -> `CLAIM-METRIC-KL_DIV-SOURCE-11`
- `papers/notes/zadu-ref-14-ref06-steering-distortions-to-preserve-classes-and-neighbors-in-supervised-dimen.md` -> `CLAIM-METRIC-KL_DIV-SOURCE-14`
- `papers/notes/zadu-ref-04-2510-08660v1.md` -> `CLAIM-METRIC-KL_DIV-SOURCE-04`

[^cat]: Category source note: `papers/notes/2023-zadu-library.md` (ZADU23-E5).
[^warn-scale]: Scale-sensitivity notes: `papers/notes/zadu-ref-03-2408-07724v2.md` (CLAIM-SOURCE-03-CORE), `papers/notes/zadu-ref-04-2510-08660v1.md` (CLAIM-SOURCE-04-CORE).
