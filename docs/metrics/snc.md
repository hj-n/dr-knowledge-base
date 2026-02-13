# snc - Steadiness & Cohesiveness

## Metric Definition
This metric pair evaluates inter-cluster reliability with two complementary directions. It is explicitly designed for cluster-level structural analysis rather than point-local distortion only.

Operationally, treat this metric as a formal lens on one distortion family rather than a universal quality score. Two embeddings can rank differently depending on whether the task prioritizes local neighborhoods, global geometry, or cluster organization, so the definition should be interpreted together with explicit task intent.

For reproducible comparisons, keep preprocessing, distance definition, and evaluation protocol fixed while reading this metric. If those upstream choices change between runs, score differences often reflect evaluation drift rather than genuine embedding improvement.

## What It Quantifies
It quantifies cluster-level reliability in two complementary components. Joint interpretation of both components is more informative than collapsing to one scalar.

In practical analysis, this score is most useful when you pair it with the failure mode you are trying to detect. A score increase is meaningful only if it reduces errors that matter for the declared analytical task, not just because the numeric value is higher.

This is why the metric should be read as task-conditioned evidence. Use it to answer a concrete question about neighborhood stability, cluster organization, distance behavior, or density behavior, then validate that interpretation with at least one complementary metric.

## Computation Outline
This outline describes the typical computational flow used in DR evaluation practice. Exact formula details may vary by implementation, but the structure below is stable across references.
- Build cluster-level relational representations in both spaces.
- Compute steadiness component (projection-to-original reliability view).
- Compute cohesiveness component (original-to-projection reliability view).
- Interpret both components jointly for cluster-level reliability.

The computation should be implemented with a stable protocol: identical sampling policy, consistent distance backend, and fixed tie-breaking behavior. Without these controls, the same embedding can yield materially different results across runs and tools.

When reporting values, record the full evaluation context including neighborhood scale, normalization policy, and clustering policy. That metadata is part of the metric definition in practice because it determines what the reported number actually means.

Detailed protocol rule: keep cluster definition policy fixed (including grouping thresholds or extraction logic) during comparison. Changes in cluster policy can dominate this metric more than projection changes.

## Hyperparameter Impact
Cluster construction and distance settings change both components. Normalization and threshold policies alter steadiness/cohesiveness balance.

Hyperparameters should be tuned against the declared task, not against a single metric in isolation. Otherwise, optimization can overfit one structural aspect and silently degrade other structure that downstream users care about.

A robust workflow evaluates sensitivity with Bayesian optimization under fixed search bounds and checks rank stability across seeds or folds. Large score variance indicates that the current configuration is not yet reliable enough for high-confidence method selection.

Decision-level tuning rule: tune this metric together with other reliability checks aligned to the confirmed goal and report sensitivity across multiple seeds or folds. Single-run improvements should be treated as provisional until rank stability is confirmed.

## Practical Reliability Notes
SNC-style metrics target inter-cluster reliability and are useful when cluster relations are part of the explicit task. They often detect cluster-level distortions that neighborhood-only metrics can miss.

Cluster metrics can still be confounded by cluster-definition policy. Keep clustering or grouping assumptions fixed during comparison; otherwise SNC changes may reflect changing cluster extraction rather than projection reliability.

## Notable Properties
It provides directional cluster-level reliability decomposition rather than one opaque scalar. It is especially useful for inter-cluster analysis tasks.

A strong property of this metric is that it provides a compact diagnostic that is easy to compare across methods. The limitation is that compactness hides where errors occur, so it should be supplemented by structure-level inspection when decisions are high impact.

In review workflows, this metric works best when combined with at least one local-structure check and one global-structure check. This reduces the chance of selecting a method that looks strong on one distortion family while failing on another.

## Strengths
This metric is strong for inter-cluster reliability analysis, including steadiness/cohesiveness-style behavior. It helps determine whether cluster-level organization remains credible after projection.

It is especially useful in workflows where cluster-level interpretation drives downstream decisions beyond local-neighbor exploration.

## Related Metrics
Steadiness and Cohesiveness is closest to directional local metrics (such as T&C and MRRE) only in the sense that all are distortion-direction diagnostics.

The key difference is level of analysis: SNC is an inter-cluster reliability metric for Missing Groups and False Groups, while T&C/MRRE are point-neighborhood metrics.

## Task Alignment
This metric is best aligned to the task set implied by its structural role. The alignment basis is structural-granularity grouping from ZADU source note.
- Best-aligned tasks:
  - Cluster identification
  - Cluster distance investigation
  - Cluster density investigation

Alignment here should be treated as a recommendation priority, not a hard constraint. If a project objective spans multiple task types, combine metrics from each relevant task family and require consistency before finalizing a method choice.

When alignment is uncertain, prefer conservative interpretation and run clarification questions again. The task decision should remain primary, and metric selection should follow that decision rather than drive it.

Operational alignment rule: treat this metric as primary evidence for cluster-relationship tasks and as secondary evidence for neighborhood-only tasks.
SNC is label-agnostic by default and should not, by itself, trigger supervised or label-dependent technique selection.

## Interpretation Notes
Do not treat this metric as a standalone final decision criterion. Use it together with complementary metrics from other structural levels and keep preprocessing/seed policies fixed during comparison.

Use absolute values cautiously and prioritize relative comparisons under matched conditions. Threshold-style decisions without protocol control often produce false certainty, especially when datasets differ in scale, density, or cluster balance.

Before communicating a conclusion, cross-check this metric against the selected technique behavior and user-facing goal. A reliable recommendation should explain both why the score is good and why that goodness matters for the intended analytical action.

Failure-signaling rule: if this metric disagrees with other selected reliability checks, report that disagreement explicitly and mark recommendation confidence as reduced instead of averaging away the conflict.

## Source Notes
The references below list paper sources used for this metric guidance.

- Measuring and Explaining the Inter-Cluster Reliability of Multidimensional Projections (Hyeon Jeon; Hyung-Kwon Ko; Jaemin Jo; Youngtaek Kim; Jinwook Seo, IEEE Transactions on Visualization and Computer Graphics, 2021)
- Feature Learning for Nonlinear Dimensionality Reduction toward Maximal Extraction of Hidden Patterns (Takanori Fujiwara, Yun-Hsin Kuo, Anders Ynnerman, Kwan-Liu Ma, 2023 IEEE 16th Pacific Visualization Symposium (PacificVis), 2023)
- Classes are Not Clusters: Improving Label-Based Evaluation of Dimensionality Reduction (Hyeon Jeon, Yun-Hsin Kuo, Michaël Aupetit, Kwan-Liu Ma, Jinwook Seo, IEEE Transactions on Visualization and Computer Graphics, 2024)
- How Scale Breaks “Normalized Stress” and KL Divergence: Rethinking Quality Metrics (Kiran Smelser, Kaviru Gunaratne, Jacob Miller, Stephen Kobourov, IEEE Transactions on Visualization and Computer Graphics, 2024)
- “Normalized Stress” is Not Normalized: How to Interpret Stress Correctly (Kiran Smelser, Jacob Miller, Stephen Kobourov, 2024 IEEE Evaluation and Beyond - Methodological Approaches for Visualization (BELIV), 2025)
