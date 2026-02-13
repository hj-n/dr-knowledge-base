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
Scale policy must be explicit when comparing values across runs or methods.

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

## Related Metrics
Stress is closest to Scale-Normalized Stress and Non-Metric Stress in the stress family, and partially aligned with Pearson/Spearman distance-correlation metrics for global structure checks.

Stress differs by residual-distance fit interpretation. It is sensitive to scale policy unless a scale-invariant variant is explicitly used and controlled.

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

- Multidimensional scaling by optimizing goodness of fit to a nonmetric hypothesis (J. B. Kruskal, Psychometrika, 1964)
- Stochastic Neighbor Embedding (Geoffrey E. Hinton, Sam T. Roweis, Advances in Neural Information Processing Systems (NIPS 15), 2002)
- Least Square Projection: A Fast High-Precision Multidimensional Projection Technique and Its Application to Document Mapping (F.V. Paulovich, L.G. Nonato, R. Minghim, H. Levkowitz, IEEE Transactions on Visualization and Computer Graphics, 2008)
- Local Multidimensional Scaling for Nonlinear Dimension Reduction, Graph Drawing, and Proximity Analysis (Lisha Chen, Andreas Buja, Journal of the American Statistical Association, 2009)
- Quality assessment of dimensionality reduction: Rank-based criteria (John A. Lee, Michel Verleysen, Neurocomputing, 2009)
- Geometric Inference for Measures based on Distance Functions (Frédéric Chazal, David Cohen-Steiner, Quentin Mérigot, Foundations of Computational Mathematics, 2010)
- Local Affine Multidimensional Projection (Paulo Joia, Fernando V. Paulovich, Danilo Coimbra, Jose Alberto Cuminato, Luis Gustavo Nonato, IEEE Transactions on Visualization and Computer Graphics, 2011)
- On the Exploration of Dimension Reduction Techniques for Visual Data Mining (Bernd Hamann (survey context), VLUDS 2011 (OASIcs), 2011)
- Steering Distortions to Preserve Classes and Neighbors in Supervised Dimensionality Reduction (Benoit Colange, Jaakko Peltonen, Michael Aupetit, Denys Dutykh, Sylvain Lespinats, Advances in Neural Information Processing Systems (NeurIPS), 2020)
- How Scale Breaks “Normalized Stress” and KL Divergence: Rethinking Quality Metrics (Kiran Smelser, Kaviru Gunaratne, Jacob Miller, Stephen Kobourov, IEEE Transactions on Visualization and Computer Graphics, 2024)
- “Normalized Stress” is Not Normalized: How to Interpret Stress Correctly (Kiran Smelser, Jacob Miller, Stephen Kobourov, 2024 IEEE Evaluation and Beyond - Methodological Approaches for Visualization (BELIV), 2025)
