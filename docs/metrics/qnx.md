# qnx - Qnx Neighborhood Overlap

## Metric Definition
`qnx` measures neighborhood-overlap fidelity between original and embedded spaces without requiring many extra tuning choices. It is designed to capture whether nearest-neighbor relationships are preserved after dimensionality reduction.

In practice, treat `qnx` as a local-structure reliability metric that is especially useful when the analytical objective depends on neighborhood integrity. It should not be interpreted as a full replacement for global-structure metrics.

## What It Quantifies
This metric quantifies how strongly the embedding retains nearest-neighbor membership from high-dimensional space. Higher values indicate that local neighborhoods in the embedding better match neighborhoods in the source space.

The practical interpretation is task-conditioned. A high `qnx` value is most meaningful for neighborhood-oriented tasks and less decisive for tasks that require faithful global distance geometry.

## Computation Outline
A typical computation compares neighborhood sets across spaces and scores overlap consistency over defined neighborhood scopes. The implementation details can vary, but the core mechanism is overlap between local neighbor relations before and after projection.

Because neighborhood metrics can still be sensitive to protocol choices (distance backend, preprocessing policy, sampling), keep evaluation settings fixed when comparing methods or hyperparameters.

Detailed protocol rule: evaluate multiple neighborhood scales (for example small/medium/local-range k values) and keep the same k schedule across methods. Local metrics should be read as scale-dependent curves, not single-point truths.

## Hyperparameter Impact
`qnx` is often used as a parameter-light objective compared with many older DR quality metrics. That makes it attractive for hyperparameter optimization loops where objective instability is a practical risk.

Even with parameter-light behavior, protocol controls still matter: changes in normalization, distance metric, or neighborhood construction can alter scores. Keep those controls explicit in optimization logs.

Decision-level tuning rule: tune this metric only inside a task-aligned bundle objective and report sensitivity across multiple seeds or folds. Single-run improvements should be treated as provisional until rank stability is confirmed.

## Practical Reliability Notes
QNX is useful for quantifying neighborhood retention across rank ranges with low implementation overhead. It is practical in iterative tuning loops where fast local-quality feedback is needed.

Because QNX can be sensitive to neighborhood-range definition, publish the evaluated range explicitly. If candidate methods are close on QNX, break ties using task-aligned secondary metrics and stability checks rather than tiny QNX deltas.

## Notable Properties
A notable property is robust behavior in benchmarked optimization contexts where metrics are used to choose DR hyperparameters. In the cited study, overlap-based metrics were consistently strong for 2D and higher-dimensional cases.

Another important property is interpretability: `qnx` directly reflects neighborhood agreement, which is easy to explain to users when the task is local-structure exploration.

## Strengths
This metric is strong for validating neighborhood-preservation objectives and for guiding hyperparameter search in local-structure tasks. It can reduce objective-function brittleness relative to heavily tuned alternatives.

It is useful when you need a reliable local-structure signal early in model selection, especially before introducing more specialized or costly evaluation criteria.

## Related Metrics
QNX is closest to LCMC because both are co-ranking/neighbor-overlap based criteria aggregated over neighborhood scales.

QNX differs by emphasizing parameter-free cumulative behavior over K, which changes how single-scale anomalies affect the final score.

## Task Alignment
Best-aligned tasks are local structure tasks in the repository taxonomy:
- Neighborhood identification
- Outlier identification
- Cluster identification (as a secondary local-neighborhood lens)

For global-distance or density-dominant tasks, `qnx` should be paired with global metrics instead of used alone.

Operational alignment rule: this metric is strongest for neighborhood, outlier, and cluster-local tasks. For point-distance or density-dominant tasks, keep it as safety check evidence rather than primary ranking evidence.

## Interpretation Notes
Do not treat `qnx` as a universal quality score. It validates local neighborhood retention, not complete geometric faithfulness.

For production recommendations, combine `qnx` with at least one global metric and one task-specific caveat check. This avoids overfitting to local fidelity while missing global distortions.

Failure-signaling rule: if this metric disagrees with other bundle metrics, report that disagreement explicitly and mark recommendation confidence as reduced instead of averaging away the conflict.

## Source Notes
The references below list paper sources used for this metric guidance.

- Spectral Overlap and a Comparison of Parameter-Free, Dimensionality Reduction Quality Metrics (Jonathan Johannemann; Robert Tibshirani, arXiv, 2019)
