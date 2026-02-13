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

Detailed protocol rule: apply consistent distance scaling and normalization policy before computing global metrics. Global score comparisons are invalid when scale handling differs across candidates.

## Hyperparameter Impact
Neighborhood probability construction parameters strongly affect divergence behavior. Scale handling and probability calibration policy are critical for fair comparisons.
Scale policy must be explicit when comparing values across runs or methods.

Hyperparameters should be tuned against the declared task, not against a single metric in isolation. Otherwise, optimization can overfit one structural aspect and silently degrade other structure that downstream users care about.

A robust workflow evaluates sensitivity with Bayesian optimization under fixed search bounds and checks rank stability across seeds or folds. Large score variance indicates that the current configuration is not yet reliable enough for high-confidence method selection.

Decision-level tuning rule: tune this metric only inside a task-aligned bundle objective and report sensitivity across multiple seeds or folds. Single-run improvements should be treated as provisional until rank stability is confirmed.

## Practical Reliability Notes
KL-style objectives are asymmetric: the direction of comparison determines which distortion type is penalized more. In DR practice this means the same embedding can look better or worse depending on whether false-neighbor or missed-neighbor errors are emphasized. Keep objective direction fixed when benchmarking methods.

Because KL is sensitive to small-probability neighborhoods, optimization noise and early exaggeration style settings can materially alter outcomes. Treat KL-driven tuning as a stability problem: compare multiple seeds and avoid accepting single-run wins that are not reproduced.

## Notable Properties
It captures probability-level neighborhood mismatch, not only distance mismatch. It can be optimization-sensitive and should be interpreted with scale policy documented.

A strong property of this metric is that it provides a compact diagnostic that is easy to compare across methods. The limitation is that compactness hides where errors occur, so it should be supplemented by structure-level inspection when decisions are high impact.

In review workflows, this metric works best as one component in a bundle: local, global, and label-aware signals together. That bundle-based interpretation reduces the chance of selecting a method that is numerically strong but operationally misaligned.

## Strengths
This metric is strong for probability-structure mismatch analysis between high- and low-dimensional neighbor distributions. It is sensitive to local probabilistic distortion patterns that distance-only metrics can miss.

It is particularly informative when comparing neighborhood-probability-preserving techniques or when auditing optimization behavior tied to divergence objectives.

## Related Metrics
Kullback-Leibler divergence is partially aligned with local-neighborhood reliability metrics because it penalizes mismatch in neighborhood probability structure.

It differs from rank- or residual-based metrics by using asymmetric probability divergence, so direction and scale handling must be interpreted carefully.

## Task Alignment
This metric is best aligned to the task set implied by its structural role. The alignment basis is structural-granularity grouping from ZADU source note.
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
The references below list paper sources used for this metric guidance.

- Stochastic Neighbor Embedding (Geoffrey E. Hinton, Sam T. Roweis, Advances in Neural Information Processing Systems (NIPS 15), 2002)
- Steering Distortions to Preserve Classes and Neighbors in Supervised Dimensionality Reduction (Benoit Colange, Jaakko Peltonen, Michael Aupetit, Denys Dutykh, Sylvain Lespinats, Advances in Neural Information Processing Systems (NeurIPS), 2020)
- Classes are Not Clusters: Improving Label-Based Evaluation of Dimensionality Reduction (Hyeon Jeon, Yun-Hsin Kuo, Michaël Aupetit, Kwan-Liu Ma, Jinwook Seo, IEEE Transactions on Visualization and Computer Graphics, 2024)
- How Scale Breaks “Normalized Stress” and KL Divergence: Rethinking Quality Metrics (Kiran Smelser, Kaviru Gunaratne, Jacob Miller, Stephen Kobourov, IEEE Transactions on Visualization and Computer Graphics, 2024)
- “Normalized Stress” is Not Normalized: How to Interpret Stress Correctly (Kiran Smelser, Jacob Miller, Stephen Kobourov, 2024 IEEE Evaluation and Beyond - Methodological Approaches for Visualization (BELIV), 2025)
