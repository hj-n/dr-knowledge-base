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

Detailed protocol rule: evaluate multiple neighborhood scales (for example small/medium/local-range k values) and keep the same k schedule across methods. Local metrics should be read as scale-dependent curves, not single-point truths.

## Hyperparameter Impact
Neighborhood size `k` is the primary control and strongly changes locality scale. Distance metric, tie-handling, and neighborhood construction policy can also alter score stability.

Hyperparameters should be tuned against the declared task, not against a single metric in isolation. Otherwise, optimization can overfit one structural aspect and silently degrade other structure that downstream users care about.

A robust workflow evaluates sensitivity with Bayesian optimization under fixed search bounds and checks rank stability across seeds or folds. Large score variance indicates that the current configuration is not yet reliable enough for high-confidence method selection.

Decision-level tuning rule: tune this metric only inside a task-aligned bundle objective and report sensitivity across multiple seeds or folds. Single-run improvements should be treated as provisional until rank stability is confirmed.

## Practical Reliability Notes
TNC is most informative when it is measured on a k schedule instead of a single k. In practice, k values such as 5, 10, 20, 50 often reveal whether a method is only good at very local neighborhoods or robust across local scales. If two methods cross over by k, report that crossover explicitly instead of reporting only a single aggregate value.

When using TNC for model selection, compare trustworthiness and continuity separately before averaging. A method with high trustworthiness but low continuity often removes true neighbors (over-fragmentation), while the opposite often introduces false neighbors (over-crowding). These failure modes map to different analyst risks and should be kept visible in the final explanation.

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

Operational alignment rule: this metric is strongest for neighborhood, outlier, and cluster-local tasks. For point-distance or density-dominant tasks, keep it as safety check evidence rather than primary ranking evidence.

## Interpretation Notes
Do not treat this metric as a standalone final decision criterion. Use it together with complementary metrics from other structural levels and keep preprocessing/seed policies fixed during comparison.

Use absolute values cautiously and prioritize relative comparisons under matched conditions. Threshold-style decisions without protocol control often produce false certainty, especially when datasets differ in scale, density, or class balance.

Before communicating a conclusion, cross-check this metric against the selected technique behavior and user-facing goal. A reliable recommendation should explain both why the score is good and why that goodness matters for the intended analytical action.

Failure-signaling rule: if this metric disagrees with other bundle metrics, report that disagreement explicitly and mark recommendation confidence as reduced instead of averaging away the conflict.

## Source Notes
The references below list paper sources used for this metric guidance.

- “Normalized Stress” is Not Normalized: How to Interpret Stress Correctly (Kiran Smelser et al., 2024 IEEE Evaluation and Beyond - Methodological Approaches for Visualization (BELIV), 2025)
- Measuring and Explaining the Inter-Cluster Reliability of Multidimensional Projections (Hyeon Jeon et al., IEEE Transactions on Visualization and Computer Graphics, 2021)
- Local Multidimensional Scaling for Nonlinear Dimension Reduction, Graph Drawing, and Proximity Analysis (Lisha Chen et al., Journal of the American Statistical Association, 2009)
- Local multidimensional scaling (Jarkko Venna et al., Neural Networks, 2006)
- Quality assessment of dimensionality reduction: Rank-based criteria (John A. Lee et al., Neurocomputing, 2009)
- Local Affine Multidimensional Projection (theory to build accurate local transformations that can be dynamically modiﬁed according to user knowledge. The accuracy et al., IEEE Transactions on Visualization and Computer Graphics, 2011)
- Additional supporting notes: 4 more

- Information retrieval perspective to nonlinear dimensionality reduction for data visualization (J. V enna et al., UNKNOWN, 2010)
- Uniform manifold approximation with two-phase optimization (H. Jeon et al., 2022 IEEE Visualization and Visual Analytics (VIS), 2022)
- Visual Interaction with Dimensionality Reduction: A Structured Literature Analysis (D. Sacha et al, IEEE Transactions on Visualization and Computer Graphics, 2017)
- Local multidimensional scaling (Jarkko Venna and Samuel Kaski, Journal of the American Statistical Association, 2006)
- Visualizing the quality of dimensionality reduction (Bassam Mokbel et al., Neurocomputing, 2013)
- Stability Comparison of Dimensionality Reduction Techniques Attending to Data and Parameter Variations (Francisco J. García-Fernández et al., UNKNOWN, 2013)

[^cat]: ZADU: A Python Library for Evaluating the Reliability of Dimensionality Reduction Embeddings (Hyeon Jeon et al., 2023 IEEE Visualization and Visual Analytics (VIS), 2023)
