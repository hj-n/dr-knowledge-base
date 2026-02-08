# qnx - Qnx Neighborhood Overlap

## Metric Definition
`qnx` measures neighborhood-overlap fidelity between original and embedded spaces without requiring many extra tuning choices. It is designed to capture whether nearest-neighbor relationships are preserved after dimensionality reduction.

In this repository, treat `qnx` as a local-structure reliability metric that is especially useful when the analytical objective depends on neighborhood integrity. It should not be interpreted as a full replacement for global-structure metrics.

## What It Quantifies
This metric quantifies how strongly the embedding retains nearest-neighbor membership from high-dimensional space. Higher values indicate that local neighborhoods in the embedding better match neighborhoods in the source space.

The practical interpretation is task-conditioned. A high `qnx` value is most meaningful for neighborhood-oriented tasks and less decisive for tasks that require faithful global distance geometry.

## Computation Outline
A typical computation compares neighborhood sets across spaces and scores overlap consistency over defined neighborhood scopes. The implementation details can vary, but the core mechanism is overlap between local neighbor relations before and after projection.

Because neighborhood metrics can still be sensitive to protocol choices (distance backend, preprocessing policy, sampling), keep evaluation settings fixed when comparing methods or hyperparameters.

## Hyperparameter Impact
`qnx` is often used as a parameter-light objective compared with many older DR quality metrics. That makes it attractive for hyperparameter optimization loops where objective instability is a practical risk.

Even with parameter-light behavior, protocol controls still matter: changes in normalization, distance metric, or neighborhood construction can alter scores. Keep those controls explicit in optimization logs.

## Notable Properties
A notable property is robust behavior in benchmarked optimization contexts where metrics are used to choose DR hyperparameters. In the cited study, overlap-based metrics were consistently strong for 2D and higher-dimensional cases.

Another important property is interpretability: `qnx` directly reflects neighborhood agreement, which is easy to explain to users when the task is local-structure exploration.

## Strengths
This metric is strong for validating neighborhood-preservation objectives and for guiding hyperparameter search in local-structure tasks. It can reduce objective-function brittleness relative to heavily tuned alternatives.

It is useful when you need a reliable local-structure signal early in model selection, especially before introducing more specialized or costly evaluation criteria.

## Task Alignment
Best-aligned tasks are local structure tasks in the repository taxonomy:
- Neighborhood identification
- Outlier identification
- Cluster identification (as a secondary local-neighborhood lens)

For global-distance or density-dominant tasks, `qnx` should be paired with global metrics instead of used alone.

## Interpretation Notes
Do not treat `qnx` as a universal quality score. It validates local neighborhood retention, not complete geometric faithfulness.

For production recommendations, combine `qnx` with at least one global metric and one task-specific caveat check. This avoids overfitting to local fidelity while missing global distortions.

## Source Notes
- `papers/notes/2019-spectral-overlap-quality-metrics.md` -> `CLAIM-JT19-C3`
- `papers/notes/2021-quantitative-survey-dr-techniques.md` -> `CLAIM-QSUR21-C2`
