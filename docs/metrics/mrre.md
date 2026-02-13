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

Decision-level tuning rule: optimize this metric together with other task-relevant reliability checks, and report stability across multiple seeds or folds. Treat single-run gains as tentative until rankings stay consistent.

## Practical Reliability Notes
MRRE captures rank distortion magnitude and is useful for identifying how severely neighborhood order is perturbed by projection. It is often more interpretable when reported per-k band (very local, local, mid-range) than as one aggregate value.

When MRRE improves while trust-continuity balance worsens, avoid declaring a universal win. That pattern often indicates one distortion type is being traded for another; include both findings in the final explanation and align choice to the declared task.

## Notable Properties
It is sensitive to ordering mistakes that overlap-based metrics may miss. It is useful for distinguishing subtle rank-quality differences across embeddings.

A strong property of this metric is that it provides a compact diagnostic that is easy to compare across methods. The limitation is that compactness hides where errors occur, so it should be supplemented by structure-level inspection when decisions are high impact.

In practice, use this metric together with local, global, and (when valid) label-based checks. This combined reading lowers the risk of choosing a method that scores well on one view but fails the actual analysis goal.

## Strengths
This metric is strong for quantifying rank-order errors in neighborhood structure across scales. It captures how far local ordering is displaced, which makes it useful when the analysis depends on nearest-neighbor ranking quality rather than only overlap counts.

It also helps surface instability across `k` schedules, so it is practical for tuning local-fidelity behavior and for spotting methods that look visually good but reorder neighbors heavily.

## Related Metrics
Mean Relative Rank Error is closest to Trustworthiness and Continuity and Local Continuity Meta-Criterion in the local rank-preservation family. All three rely on comparing neighborhood structure before and after projection.

MRRE differs by explicitly weighting rank displacement magnitude. That makes MRRE more sensitive to how far neighbor order moved, not only whether neighbors were kept or lost.

## Task Alignment
This metric is best aligned to the task set implied by its structural role. The alignment basis is structural-granularity grouping from ZADU source note.
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

- Quality assessment of dimensionality reduction: Rank-based criteria (John A. Lee, Michel Verleysen, Neurocomputing, 2009)
- Measuring and Explaining the Inter-Cluster Reliability of Multidimensional Projections (Hyeon Jeon; Hyung-Kwon Ko; Jaemin Jo; Youngtaek Kim; Jinwook Seo, IEEE Transactions on Visualization and Computer Graphics, 2021)
- Classes are Not Clusters: Improving Label-Based Evaluation of Dimensionality Reduction (Hyeon Jeon, Yun-Hsin Kuo, Michaël Aupetit, Kwan-Liu Ma, Jinwook Seo, IEEE Transactions on Visualization and Computer Graphics, 2024)
- How Scale Breaks “Normalized Stress” and KL Divergence: Rethinking Quality Metrics (Kiran Smelser, Kaviru Gunaratne, Jacob Miller, Stephen Kobourov, IEEE Transactions on Visualization and Computer Graphics, 2024)
- “Normalized Stress” is Not Normalized: How to Interpret Stress Correctly (Kiran Smelser, Jacob Miller, Stephen Kobourov, 2024 IEEE Evaluation and Beyond - Methodological Approaches for Visualization (BELIV), 2025)
