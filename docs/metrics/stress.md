# stress - Stress

## Metric Definition
This metric measures pairwise-distance fitting error between original and projected spaces. It is a canonical objective and evaluation measure in the MDS family.

Operationally, treat this metric as a formal lens on one distortion family rather than a universal quality score. Two embeddings can rank differently depending on whether the task prioritizes local neighborhoods, global geometry, or class structure, so the definition should be interpreted together with explicit task intent.

For reproducible comparisons, keep preprocessing, distance definition, and evaluation protocol fixed while reading this metric. If those upstream choices change between runs, score differences often reflect evaluation drift rather than genuine embedding improvement.

## What It Quantifies
It quantifies global pairwise-distance distortion energy. Lower stress typically indicates better global distance fitting.

In practical analysis, this score is most useful when you pair it with the failure mode you are trying to detect. A score increase is meaningful only if it reduces errors that matter for the declared analytical task, not just because the numeric value is higher.

This is why the metric should be read as task-conditioned evidence. Use it to answer a concrete question about neighborhood stability, class organization, distance behavior, or density behavior, then validate that interpretation with at least one complementary metric.

## Computation Outline
This outline describes the typical computational flow used in DR evaluation practice. Exact formula details may vary by implementation, but the structure below is stable across references.
- Compute pairwise dissimilarities/distances in original space.
- Compute corresponding distances in projected space.
- Calculate squared fitting error with chosen normalization/weighting.
- Aggregate over all pairs to obtain stress value.

The computation should be implemented with a stable protocol: identical sampling policy, consistent distance backend, and fixed tie-breaking behavior. Without these controls, the same embedding can yield materially different results across runs and tools.

When reporting values, record the full evaluation context including neighborhood scale, normalization policy, and whether labels were required. That metadata is part of the metric definition in practice because it determines what the reported number actually means.

Detailed protocol rule: apply consistent distance scaling and normalization policy before computing global metrics. Global score comparisons are invalid when scale handling differs across candidates.

## Hyperparameter Impact
Normalization and pair weighting are dominant controls. Scale policy must be fixed, otherwise cross-run comparisons can be misleading.
Scale policy must be explicit when comparing values across runs or methods.[^warn-scale]

Hyperparameters should be tuned against the declared task, not against a single metric in isolation. Otherwise, optimization can overfit one structural aspect and silently degrade other structure that downstream users care about.

A robust workflow evaluates sensitivity with Bayesian optimization under fixed search bounds and checks rank stability across seeds or folds. Large score variance indicates that the current configuration is not yet reliable enough for high-confidence method selection.

Decision-level tuning rule: tune this metric only inside a task-aligned bundle objective and report sensitivity across multiple seeds or folds. Single-run improvements should be treated as provisional until rank stability is confirmed.

## Practical Reliability Notes
Stress values are only comparable under identical scale handling and distance preprocessing. If one run applies implicit rescaling and another does not, stress ranking can reverse even when the embedding geometry is otherwise similar. Keep scale policy fixed across all candidates and report that policy explicitly.

For workflow use, stress should be paired with at least one local metric (for example TNC or NH-family metrics) because low global stress can still hide local neighborhood breakage. A low-stress embedding is not automatically valid for neighborhood or outlier tasks unless local structure checks agree.

## Notable Properties
It is a canonical global distortion objective with a long methodological history. It can be misinterpreted when normalization and scale policies are inconsistent.

A strong property of this metric is that it provides a compact diagnostic that is easy to compare across methods. The limitation is that compactness hides where errors occur, so it should be supplemented by structure-level inspection when decisions are high impact.

In review workflows, this metric works best as one component in a bundle: local, global, and label-aware signals together. That bundle-based interpretation reduces the chance of selecting a method that is numerically strong but operationally misaligned.

## Strengths
This metric is strong for global distance-fitting diagnostics across the full configuration. It is a standard, well-understood global metric for assessing how well pairwise geometry is reproduced.

It is useful for comparing methods on distance-faithfulness objectives, especially when evaluation scale is controlled consistently.


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

Failure-signaling rule: if this metric disagrees with other bundle metrics, report that disagreement explicitly and mark recommendation confidence as reduced instead of averaging away the conflict.

## Source Notes
The links below map this metric to claim-level evidence extracted from individual source notes. Use these links when tracing recommendations back to evidence.

- `papers/notes/zadu-ref-06-least-square-projection-a-fast-high-precision-multidimensional-projection-techni.md` -> `CLAIM-METRIC-STRESS-SOURCE-06`
- `papers/notes/zadu-ref-03-2408-07724v2.md` -> `CLAIM-METRIC-STRESS-SOURCE-03`
- `papers/notes/zadu-ref-13-ref03-geometric-inference-for-probability-measures.md` -> `CLAIM-METRIC-STRESS-SOURCE-13`
- `papers/notes/zadu-ref-17-ref13-stochastic-neighbor-embedding.md` -> `CLAIM-METRIC-STRESS-SOURCE-17`
- `papers/notes/zadu-ref-18-ref18-measuring-and-explaining-the-inter-cluster-reliability-of-multidimensional.md` -> `CLAIM-METRIC-STRESS-SOURCE-18`
- `papers/notes/zadu-ref-07-local-multidimensional-scaling-for-nonlinear-dimension-reduction-graph-drawing-a.md` -> `CLAIM-METRIC-STRESS-SOURCE-07`
- Additional supporting notes: 5 more

- `papers/notes/pending-ref-004-information-retrieval-perspective-to-nonlinear-dimensional.md` (pending-reference evidence)
- `papers/notes/pending-ref-013-a-survey-of-dimension-reduction-methods-for-high-dimension.md` (pending-reference evidence)
- `papers/notes/pending-ref-019-local-multidimensional-scaling.md` (pending-reference evidence)
- `papers/notes/pending-ref-024-viscoder-a-tool-for-visually-comparing-dimensionality-redu.md` (pending-reference evidence)
- `papers/notes/pending-ref-035-stress-maps-analysing-local-phenomena-in-dimensionality-re.md` (pending-reference evidence)
- `papers/notes/pending-ref-037-attribute-based-visual-explanation-of-multidimensional-pro.md` (pending-reference evidence)

[^cat]: Category source note: `papers/notes/2023-zadu-library.md` (ZADU23-E5).
[^warn-scale]: Scale-sensitivity notes: `papers/notes/zadu-ref-03-2408-07724v2.md` (CLAIM-SOURCE-03-CORE), `papers/notes/zadu-ref-04-2510-08660v1.md` (CLAIM-SOURCE-04-CORE).
