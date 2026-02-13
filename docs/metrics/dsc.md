# dsc - Distance Consistency

## Metric Definition
This metric measures class or cluster separation consistency in the embedding. It is commonly interpreted as a structure-preservation signal for separability tasks.

Operationally, treat this metric as a formal lens on one distortion family rather than a universal quality score. Two embeddings can rank differently depending on whether the task prioritizes local neighborhoods, global geometry, or class structure, so the definition should be interpreted together with explicit task intent.

For reproducible comparisons, keep preprocessing, distance definition, and evaluation protocol fixed while reading this metric. If those upstream choices change between runs, score differences often reflect evaluation drift rather than genuine embedding improvement.

## What It Quantifies
It quantifies class/cluster distance consistency in the projected space. Higher consistency generally indicates better separability preservation.

In practical analysis, this score is most useful when you pair it with the failure mode you are trying to detect. A score increase is meaningful only if it reduces errors that matter for the declared analytical task, not just because the numeric value is higher.

This is why the metric should be read as task-conditioned evidence. Use it to answer a concrete question about neighborhood stability, class organization, distance behavior, or density behavior, then validate that interpretation with at least one complementary metric.

## Computation Outline
This outline describes the typical computational flow used in DR evaluation practice. Exact formula details may vary by implementation, but the structure below is stable across references.
- Require labels or cluster assignments.
- Construct class/cluster distance-consistency criterion in projected space.
- Count or score consistency/violation behavior per point.
- Aggregate across points/classes to produce final value.

The computation should be implemented with a stable protocol: identical sampling policy, consistent distance backend, and fixed tie-breaking behavior. Without these controls, the same embedding can yield materially different results across runs and tools.

When reporting values, record the full evaluation context including neighborhood scale, normalization policy, and whether labels were required. That metadata is part of the metric definition in practice because it determines what the reported number actually means.

Detailed protocol rule: keep class labels and class-balance handling fixed across runs. Reweighting classes or filtering minority classes can substantially alter class metrics independently of embedding quality.

## Hyperparameter Impact
Cluster/label definition choices dominate this metric. Label-separation assumptions should be validated before treating score differences as decisive.
The label-separation gate is mandatory before strong interpretation in labeled settings.

Hyperparameters should be tuned against the declared task, not against a single metric in isolation. Otherwise, optimization can overfit one structural aspect and silently degrade other structure that downstream users care about.

A robust workflow evaluates sensitivity with Bayesian optimization under fixed search bounds and checks rank stability across seeds or folds. Large score variance indicates that the current configuration is not yet reliable enough for high-confidence method selection.

Decision-level tuning rule: optimize this metric together with other task-relevant reliability checks, and report stability across multiple seeds or folds. Treat single-run gains as tentative until rankings stay consistent.

## Practical Reliability Notes
Distance Consistency reflects whether points remain closer to their own class prototypes than to other classes after projection. It is useful for class-separability analysis, but can become overly optimistic when classes overlap in original space or when class imbalance is severe.

Before relying on DSC for recommendation decisions, run the label-separation check and verify class overlap in the original feature space. If overlap is high, down-weight DSC and prioritize a mixed set of label-free metrics plus task-specific technique constraints.

## Notable Properties
It is aligned with separability-focused tasks and cluster-structure questions. It requires strong caution when label-separation assumptions do not hold.

A strong property of this metric is that it provides a compact diagnostic that is easy to compare across methods. The limitation is that compactness hides where errors occur, so it should be supplemented by structure-level inspection when decisions are high impact.

In practice, use this metric together with local, global, and (when valid) label-based checks. This combined reading lowers the risk of choosing a method that scores well on one view but fails the actual analysis goal.

## Strengths
This metric is strong for class/cluster consistency checks in labeled settings. It provides a direct signal of whether embedding geometry supports class-oriented separation expectations.

It is effective for screening class-separability claims, but interpretation must remain conditional on original-space label separability.

## Related Metrics
Distance Consistency is close to Internal Validation and Clustering-plus-External Validation metrics in class-separability evaluation workflows. All can score whether class-related structures look separated.

Distance Consistency differs by using centroid-consistency style logic and is also used as a CVM inside Label-T&C with invariance constraints.

## Task Alignment
This metric is best aligned to the task set implied by its structural role. The alignment basis is structural-granularity grouping from ZADU source note.
- Best-aligned tasks:
  - Cluster identification
  - Class separability investigation
  - Cluster distance investigation

Alignment here should be treated as a recommendation priority, not a hard constraint. If a project objective spans multiple task types, combine metrics from each relevant task family and require consistency before finalizing a method choice.

When alignment is uncertain, prefer conservative interpretation and run clarification questions again. The task decision should remain primary, and metric selection should follow that decision rather than drive it.

Operational alignment rule: this metric can prioritize candidates inside an already-selected main goal, but it must not redefine the task itself. If metric preference and user task conflict, keep task intent as the hard constraint.

## Interpretation Notes
Do not treat this metric as a standalone final decision criterion. Use it together with complementary metrics from other structural levels and keep preprocessing/seed policies fixed during comparison.

Use absolute values cautiously and prioritize relative comparisons under matched conditions. Threshold-style decisions without protocol control often produce false certainty, especially when datasets differ in scale, density, or class balance.

Before communicating a conclusion, cross-check this metric against the selected technique behavior and user-facing goal. A reliable recommendation should explain both why the score is good and why that goodness matters for the intended analytical action.

Failure-signaling rule: when class-aware metrics improve but label-agnostic local/global metrics worsen, report a class-specific gain with structural tradeoff instead of claiming unconditional quality improvement.

## Source Notes
The references below list paper sources used for this metric guidance.

- Selecting good views of high-dimensional data using class consistency (Mike Sips; Boris Neubert; John P. Lewis; Pat Hanrahan, Computer Graphics Forum, 2009)
- Classes are Not Clusters: Improving Label-Based Evaluation of Dimensionality Reduction (Hyeon Jeon, Yun-Hsin Kuo, Michaël Aupetit, Kwan-Liu Ma, Jinwook Seo, IEEE Transactions on Visualization and Computer Graphics, 2024)
- How Scale Breaks “Normalized Stress” and KL Divergence: Rethinking Quality Metrics (Kiran Smelser, Kaviru Gunaratne, Jacob Miller, Stephen Kobourov, IEEE Transactions on Visualization and Computer Graphics, 2024)
- “Normalized Stress” is Not Normalized: How to Interpret Stress Correctly (Kiran Smelser, Jacob Miller, Stephen Kobourov, 2024 IEEE Evaluation and Beyond - Methodological Approaches for Visualization (BELIV), 2025)
