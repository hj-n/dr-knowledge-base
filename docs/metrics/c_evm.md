# c_evm - Clustering + External Validation Measure

## Metric Definition
This metric combines clustering outputs with label-based external validation. It evaluates whether embedding-derived cluster structure agrees with supervised class information.

Operationally, treat this metric as a formal lens on one distortion family rather than a universal quality score. Two embeddings can rank differently depending on whether the task prioritizes local neighborhoods, global geometry, or class structure, so the definition should be interpreted together with explicit task intent.

For reproducible comparisons, keep preprocessing, distance definition, and evaluation protocol fixed while reading this metric. If those upstream choices change between runs, score differences often reflect evaluation drift rather than genuine embedding improvement.

## What It Quantifies
It quantifies agreement between projected clustering and supervised labels. Strong scores indicate embedding structures aligned with labeled class partitions.

In practical analysis, this score is most useful when you pair it with the failure mode you are trying to detect. A score increase is meaningful only if it reduces errors that matter for the declared analytical task, not just because the numeric value is higher.

This is why the metric should be read as task-conditioned evidence. Use it to answer a concrete question about neighborhood stability, class organization, distance behavior, or density behavior, then validate that interpretation with at least one complementary metric.

## Computation Outline
This outline describes the typical computational flow used in DR evaluation practice. Exact formula details may vary by implementation, but the structure below is stable across references.
- Cluster embedded points with fixed clustering settings.
- Compare cluster assignments with labels using external validation measure.
- Compute agreement score as reliability indicator.
- Repeat consistently across runs/methods for comparable evaluation.

The computation should be implemented with a stable protocol: identical sampling policy, consistent distance backend, and fixed tie-breaking behavior. Without these controls, the same embedding can yield materially different results across runs and tools.

When reporting values, record the full evaluation context including neighborhood scale, normalization policy, and whether labels were required. That metadata is part of the metric definition in practice because it determines what the reported number actually means.

Detailed protocol rule: keep class labels and class-balance handling fixed across runs. Reweighting classes or filtering minority classes can substantially alter class metrics independently of embedding quality.

## Hyperparameter Impact
Clustering pipeline design and external index choice are core controls. Label noise and class granularity can dominate score behavior.
The label-separation gate is mandatory before strong interpretation in labeled settings.[^warn-label]

Hyperparameters should be tuned against the declared task, not against a single metric in isolation. Otherwise, optimization can overfit one structural aspect and silently degrade other structure that downstream users care about.

A robust workflow evaluates sensitivity with Bayesian optimization under fixed search bounds and checks rank stability across seeds or folds. Large score variance indicates that the current configuration is not yet reliable enough for high-confidence method selection.

Decision-level tuning rule: tune this metric only inside a task-aligned bundle objective and report sensitivity across multiple seeds or folds. Single-run improvements should be treated as provisional until rank stability is confirmed.

## Practical Reliability Notes
Class-EVM style measures emphasize class-level embedding consistency and therefore amplify label quality issues. Noisy labels, weak supervision, or merged semantic classes can produce confident but unreliable scores.

Operationally, only treat C-EVM as decision-driving when label validity and separability are both supported. Otherwise, retain it as an auxiliary indicator and keep recommendations anchored to task-fit plus label-agnostic reliability checks.

## Notable Properties
It connects unsupervised clustering outcomes with supervised consistency checks. It is sensitive to label quality and external index definition.

A strong property of this metric is that it provides a compact diagnostic that is easy to compare across methods. The limitation is that compactness hides where errors occur, so it should be supplemented by structure-level inspection when decisions are high impact.

In review workflows, this metric works best as one component in a bundle: local, global, and label-aware signals together. That bundle-based interpretation reduces the chance of selecting a method that is numerically strong but operationally misaligned.

## Strengths
This metric is strong for checking agreement between embedding-derived clusters and known labels. It bridges unsupervised cluster formation and supervised external validation in one signal.

It is useful when the target question is whether projection structure aligns with labeled class partitions, not just whether clusters exist visually.


## Task Alignment
This metric is best aligned to the task set implied by its structural role. The alignment basis is structural-granularity grouping from ZADU source note.[^cat]
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

- A Comparison for Dimensionality Reduction Methods of Single-Cell RNA-seq Data (Ruizhi Xiang et al., Frontiers in Genetics, 2021)
- Classes are Not Clusters: Improving Label-Based Evaluation of Dimensionality Reduction (Hyeon Jeon et al., IEEE Transactions on Visualization and Computer Graphics, 2024)

[^cat]: ZADU: A Python Library for Evaluating the Reliability of Dimensionality Reduction Embeddings (Hyeon Jeon et al., 2023 IEEE Visualization and Visual Analytics (VIS), 2023)
[^warn-label]: ZADU README Operational Warning for Label-Separation-Sensitive Metrics (hj-n/zadu maintainers, GitHub README, 2026)
