# DR Reliability Cautions and Tips

Use this page to avoid common reliability failures when applying DR and to improve recommendation quality.
Similar claims from multiple papers are grouped into shared themes.

Related:
- Workflow anchor: [`docs/workflow/dr-analysis-workflow.md`](./workflow/dr-analysis-workflow.md)
- Selection policy: [`docs/metrics-and-libraries.md`](./metrics-and-libraries.md)
- Frequency ranking: [`docs/reference-coverage.md`](./reference-coverage.md)

## Grouped Cautions

### 1) Task-Method Mismatch
Do not select methods before clarifying the primary analytical task. Local methods are often misused for global-distance or density questions, which can produce convincing but invalid interpretations.

Reliability action:
- Lock one primary task first, then map method family and metrics to that task.

Source notes:
- `papers/notes/2506.08725v2-stop-misusing-tsne-umap.md`

### 2) Label-Separation Assumption Violations
Some class-aware metrics assume class labels are already well separated in the original high-dimensional space. If that assumption is weak, these metrics can become unreliable and overstate embedding quality.

Affected metrics:
- `dsc`, `ivm`, `c_evm`, `nh`, `ca_tnc`

Reliability action:
- Explicitly check label separability before using these metrics as decision-driving evidence.
- If separability is weak or unknown, down-weight these metrics and use additional label-agnostic measures.

Source notes:
- `papers/notes/2026-zadu-readme-warning.md`
- `papers/notes/zadu-ref-11-jeon23tvcg-4.md`
- `papers/notes/zadu-ref-05-computer-graphics-forum-2009-sips-selecting-good-views-of-high-e2-80-90dimension.md`
- `papers/notes/zadu-ref-18-ref18-measuring-and-explaining-the-inter-cluster-reliability-of-multidimensional.md`
- `papers/notes/zadu-ref-19-ref42-a-comparison-for-dimensionality-reduction-methods-of-single-cell-rna-seq-d.md`

### 3) Scale-Sensitive Metric Misinterpretation
Raw stress-like and KL-like scores can be distorted by embedding scale choices. Comparing methods without consistent scale handling can flip rankings and hide true quality differences.

Reliability action:
- Fix or optimize scale consistently before cross-method comparison.
- Prefer scale-aware or normalized variants when comparing multiple embeddings.

Source notes:
- `papers/notes/zadu-ref-03-2408-07724v2.md`
- `papers/notes/zadu-ref-04-2510-08660v1.md`
- `papers/notes/zadu-ref-12-kruskal-1964a.md`

### 4) Single-Metric Overconfidence
A single metric rarely captures all reliability dimensions. Over-relying on one score can optimize one structural property while silently degrading others.

Reliability action:
- Use a compact metric bundle across local, cluster-level, and global perspectives.
- Require consistency across the bundle before final recommendation.

Source notes:
- `papers/notes/2023-zadu-library.md`
- `papers/notes/zadu-ref-01-1-s2-0-s0893608006000724-main.md`
- `papers/notes/zadu-ref-06-least-square-projection-a-fast-high-precision-multidimensional-projection-techni.md`
- `papers/notes/zadu-ref-07-local-multidimensional-scaling-for-nonlinear-dimension-reduction-graph-drawing-a.md`
- `papers/notes/zadu-ref-10-download-2.md`
- `papers/notes/zadu-ref-13-ref03-geometric-inference-for-probability-measures.md`
- `papers/notes/zadu-ref-15-ref10-feature-learning-for-nonlinear-dimensionality-reduction-toward-maximal-ext.md`
- `papers/notes/zadu-ref-16-ref12-local-procrustes-for-manifold-embedding-a-measure-of-embedding-quality-and.md`
- `papers/notes/zadu-ref-17-ref13-stochastic-neighbor-embedding.md`

### 5) Reproducibility Drift (Preprocessing/Seed/Protocol)
Score comparisons are unreliable when preprocessing, random seeds, or evaluation settings change across runs. Apparent improvements may be protocol artifacts.

Reliability action:
- Fix preprocessing policy and seed policy before comparing methods.
- Keep identical evaluation protocol across candidate methods.

Source notes:
- `papers/notes/zadu-ref-01-1-s2-0-s0893608006000724-main.md`
- `papers/notes/zadu-ref-07-local-multidimensional-scaling-for-nonlinear-dimension-reduction-graph-drawing-a.md`
- `papers/notes/zadu-ref-09-supervised-nonlinear-dimensionality-reduction-for-visualization-and-classificati.md`
- `papers/notes/zadu-ref-13-ref03-geometric-inference-for-probability-measures.md`
- `papers/notes/zadu-ref-16-ref12-local-procrustes-for-manifold-embedding-a-measure-of-embedding-quality-and.md`

### 6) Hyperparameter and Optimization Pitfalls
Method behavior can change materially with hyperparameters and optimization path. Local optima, unstable settings, and undocumented search ranges reduce trustworthiness of final recommendations.

Reliability action:
- Use explicit hyperparameter optimization with recorded search space, seed schedule, and objective metrics.
- Treat convergence quality and stability as part of the recommendation evidence.

Source notes:
- `papers/notes/zadu-ref-11-jeon23tvcg-4.md`
- `papers/notes/zadu-ref-17-ref13-stochastic-neighbor-embedding.md`
- `papers/notes/zadu-ref-04-2510-08660v1.md`

### 7) Runtime-Quality Tradeoff Blind Spots
Some methods or evaluation procedures incur high runtime/complexity cost, and naive runtime assumptions can bias method choice.

Reliability action:
- Report runtime/complexity context together with reliability scores.
- Avoid ranking methods by quality without practical runtime feasibility checks.

Source notes:
- `papers/notes/zadu-ref-02-1-s2-0-s0925231209000101-main.md`
- `papers/notes/zadu-ref-08-local-affine-multidimensional-projection-1.md`
- `papers/notes/zadu-ref-15-ref10-feature-learning-for-nonlinear-dimensionality-reduction-toward-maximal-ext.md`
- `papers/notes/zadu-ref-17-ref13-stochastic-neighbor-embedding.md`
- `papers/notes/zadu-ref-19-ref42-a-comparison-for-dimensionality-reduction-methods-of-single-cell-rna-seq-d.md`

## Reliability Improvement Checklist

1. Confirm one primary analytical task before method selection.
2. Validate label separability before using class-aware metrics.
3. Use a multi-level metric bundle instead of a single metric.
4. Control scale when comparing stress/KL-related scores.
5. Freeze preprocessing and seeds for fair comparison.
6. Log hyperparameter search space and optimization trace.
7. Include runtime feasibility with quality evidence.
8. Explain residual uncertainty and limits in the final recommendation.
