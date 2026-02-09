# mrre - Mean Relative Rank Error

## Metric Definition
This metric measures how much neighborhood rank order changes after projection. It captures rank displacement magnitude rather than simple membership overlap.

Operationally, treat this metric as a formal lens on one distortion family rather than a universal quality score. Two embeddings can rank differently depending on whether the task prioritizes local neighborhoods, global geometry, or class structure, so the definition should be interpreted together with explicit task intent.

For reproducible comparisons, keep preprocessing, distance definition, and evaluation protocol fixed while reading this metric. If those upstream choices change between runs, score differences often reflect evaluation drift rather than genuine embedding improvement.

## What It Quantifies
It quantifies relative neighbor-rank displacement after projection. Lower values indicate that projected neighborhoods preserve rank order more faithfully.

In practical analysis, this score is most useful when you pair it with the failure mode you are trying to detect. A score increase is meaningful only if it reduces errors that matter for the declared analytical task, not just because the numeric value is higher.

This is why the metric should be read as task-conditioned evidence. Use it to answer a concrete question about neighborhood stability, class organization, distance behavior, or density behavior, then validate that interpretation with at least one complementary metric.

## Computation Outline
This outline describes the typical computational flow used in DR evaluation practice. Exact formula details may vary by implementation, but the structure below is stable across references.
- Define the rank range to evaluate for each point.
- Compute corresponding high-space and low-space neighbor ranks.
- Calculate relative rank error terms per neighbor relation.
- Aggregate errors across points to obtain the final metric value.

The computation should be implemented with a stable protocol: identical sampling policy, consistent distance backend, and fixed tie-breaking behavior. Without these controls, the same embedding can yield materially different results across runs and tools.

When reporting values, record the full evaluation context including neighborhood scale, normalization policy, and whether labels were required. That metadata is part of the metric definition in practice because it determines what the reported number actually means.

Detailed protocol rule: evaluate multiple neighborhood scales (for example small/medium/local-range k values) and keep the same k schedule across methods. Local metrics should be read as scale-dependent curves, not single-point truths.

## Hyperparameter Impact
Rank-window definition and normalization choice are major controls. The selected rank region determines whether ultra-local or broader ordering errors dominate.

Hyperparameters should be tuned against the declared task, not against a single metric in isolation. Otherwise, optimization can overfit one structural aspect and silently degrade other structure that downstream users care about.

A robust workflow evaluates sensitivity with Bayesian optimization under fixed search bounds and checks rank stability across seeds or folds. Large score variance indicates that the current configuration is not yet reliable enough for high-confidence method selection.

Decision-level tuning rule: tune this metric only inside a task-aligned bundle objective and report sensitivity across multiple seeds or folds. Single-run improvements should be treated as provisional until rank stability is confirmed.

## Practical Reliability Notes
MRRE captures rank distortion magnitude and is useful for identifying how severely neighborhood order is perturbed by projection. It is often more interpretable when reported per-k band (very local, local, mid-range) than as one aggregate value.

When MRRE improves while trust-continuity balance worsens, avoid declaring a universal win. That pattern often indicates one distortion type is being traded for another; include both findings in the final explanation and align choice to the declared task.

## Notable Properties
It is sensitive to ordering mistakes that overlap-based metrics may miss. It is useful for distinguishing subtle rank-quality differences across embeddings.

A strong property of this metric is that it provides a compact diagnostic that is easy to compare across methods. The limitation is that compactness hides where errors occur, so it should be supplemented by structure-level inspection when decisions are high impact.

In review workflows, this metric works best as one component in a bundle: local, global, and label-aware signals together. That bundle-based interpretation reduces the chance of selecting a method that is numerically strong but operationally misaligned.

## Strengths
This metric is strong for quantifying rank-order errors in neighborhood structure across scales. It captures how far local ordering is displaced, which makes it useful when the analysis depends on nearest-neighbor ranking quality rather than only overlap counts.

It also helps surface instability across `k` schedules, so it is practical for tuning local-fidelity behavior and for spotting methods that look visually good but reorder neighbors heavily.


## Task Alignment
This metric is best aligned to the task set implied by its structural role. The alignment basis is structural-granularity grouping from ZADU source note.[^cat]
- Best-aligned tasks:
  - Neighborhood identification
  - Outlier identification
  - Cluster identification

Alignment here should be treated as a recommendation priority, not a hard constraint. If a project objective spans multiple task types, combine metrics from each relevant task family and require consistency before finalizing a method choice.

When alignment is uncertain, prefer conservative interpretation and run clarification questions again. The task decision should remain primary, and metric selection should follow that decision rather than drive it.

Operational alignment rule: this metric is strongest for neighborhood, outlier, and cluster-local tasks. For point-distance or density-dominant tasks, keep it as guardrail evidence rather than primary ranking evidence.

## Interpretation Notes
Do not treat this metric as a standalone final decision criterion. Use it together with complementary metrics from other structural levels and keep preprocessing/seed policies fixed during comparison.

Use absolute values cautiously and prioritize relative comparisons under matched conditions. Threshold-style decisions without protocol control often produce false certainty, especially when datasets differ in scale, density, or class balance.

Before communicating a conclusion, cross-check this metric against the selected technique behavior and user-facing goal. A reliable recommendation should explain both why the score is good and why that goodness matters for the intended analytical action.

Failure-signaling rule: if this metric disagrees with other bundle metrics, report that disagreement explicitly and mark recommendation confidence as reduced instead of averaging away the conflict.

## Source Notes
The links below map this metric to claim-level evidence extracted from individual source notes. Use these links when tracing recommendations back to evidence.

- `papers/notes/zadu-ref-03-2408-07724v2.md` -> `CLAIM-METRIC-MRRE-SOURCE-03`
- `papers/notes/zadu-ref-18-ref18-measuring-and-explaining-the-inter-cluster-reliability-of-multidimensional.md` -> `CLAIM-METRIC-MRRE-SOURCE-18`
- `papers/notes/zadu-ref-02-1-s2-0-s0925231209000101-main.md` -> `CLAIM-METRIC-MRRE-SOURCE-02`
- `papers/notes/zadu-ref-11-jeon23tvcg-4.md` -> `CLAIM-METRIC-MRRE-SOURCE-11`
- `papers/notes/zadu-ref-04-2510-08660v1.md` -> `CLAIM-METRIC-MRRE-SOURCE-04`

- `papers/notes/pending-ref-009-uniform-manifold-approximation-with-two-phase-optimization.md` (pending-reference evidence)

[^cat]: Category source note: `papers/notes/2023-zadu-library.md` (ZADU23-E3).
