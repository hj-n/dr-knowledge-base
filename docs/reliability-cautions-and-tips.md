# DR Reliability Cautions and Tips

Use this page to avoid common reliability failures when applying DR and to improve recommendation quality.
Similar claims from multiple papers are grouped into shared themes.

Related:
- Workflow anchor: [`docs/workflow/dr-analysis-workflow.md`](./workflow/dr-analysis-workflow.md)
- Task lock protocol: [`docs/workflow/task-confirmation-protocol.md`](./workflow/task-confirmation-protocol.md)
- Preprocessing profiles: [`docs/workflow/preprocessing-profiles.md`](./workflow/preprocessing-profiles.md)
- Deterministic selection policy: [`docs/workflow/configuration-selection-policy.md`](./workflow/configuration-selection-policy.md)
- Task-aligned initialization rules: [`docs/workflow/task-aligned-initialization.md`](./workflow/task-aligned-initialization.md)
- Selection policy: [`docs/metrics-and-libraries.md`](./metrics-and-libraries.md)
- Frequency ranking: [`docs/reference-coverage.md`](./reference-coverage.md)

## Grouped Cautions

### 1) Task-Method Mismatch
Do not select methods before clarifying the primary analytical task. Local methods are often misused for global-distance or density questions, which can produce convincing but invalid interpretations.

Reliability action:
- Lock one primary task first, then map method family and metrics to that task.

Source notes:
- `papers/notes/2506.08725v2-stop-misusing-tsne-umap.md`
- `papers/notes/2014-brehmer-task-sequences.md`
- `papers/notes/2012-sedlmair-dr-in-the-wild.md`

### 2) Hidden Task-Sequence Drift
Even when a high-level task is stated, analysts often switch to a different subtask sequence during exploration (for example, cluster verification to class matching). If the workflow does not detect this drift, metric/technique choices become misaligned.

Reliability action:
- Re-confirm the active task whenever users switch from one interpretive action to another.
- Keep one main goal fixed, and track sequence transitions as optional subtask updates.

Source notes:
- `papers/notes/2014-brehmer-task-sequences.md`
- `papers/notes/2012-sedlmair-dr-in-the-wild.md`

### 3) Label-Separation Assumption Violations
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

### 4) Scale-Sensitive Metric Misinterpretation
Raw stress-like and KL-like scores can be distorted by embedding scale choices. Comparing methods without consistent scale handling can flip rankings and hide true quality differences.

Reliability action:
- Fix or optimize scale consistently before cross-method comparison.
- Prefer scale-aware or normalized variants when comparing multiple embeddings.

Source notes:
- `papers/notes/zadu-ref-03-2408-07724v2.md`
- `papers/notes/zadu-ref-04-2510-08660v1.md`
- `papers/notes/zadu-ref-12-kruskal-1964a.md`

### 5) Single-Metric Overconfidence
A single metric rarely captures all reliability dimensions. Over-relying on one score can optimize one structural property while silently degrading others.

Reliability action:
- Use a compact reliability check set across local, cluster-level, and global perspectives.
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

### 6) Initialization Confounding in Method Comparisons
Method-comparison claims can be invalid when initialization policies differ across algorithms. This is especially critical for t-SNE/UMAP global-structure interpretations.

Reliability action:
- Hold all settings constant except the factor being tested.
- Log initialization policy as mandatory experiment metadata.
- Prefer informative initialization when global structure is part of the decision.

Source notes:
- `papers/notes/2020-kobak-initialization-tsne-umap.md`
- `papers/notes/2025-jeon-reliable-va-survey.md`

### 7) Reproducibility Drift (Preprocessing/Seed/Protocol)
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

### 8) Hyperparameter and Optimization Pitfalls
Method behavior can change materially with hyperparameters and optimization path. Local optima, unstable settings, and undocumented search ranges reduce trustworthiness of final recommendations.

Reliability action:
- Use explicit hyperparameter optimization with recorded search space, seed schedule, and objective metrics.
- Treat convergence quality and stability as part of the recommendation evidence.

Source notes:
- `papers/notes/zadu-ref-11-jeon23tvcg-4.md`
- `papers/notes/zadu-ref-17-ref13-stochastic-neighbor-embedding.md`
- `papers/notes/zadu-ref-04-2510-08660v1.md`
- `papers/notes/2019-spectral-overlap-quality-metrics.md`
- `papers/notes/2024-large-scale-text-spatialization.md`
- `papers/notes/pending-ref-029-stability-comparison-of-dimensionality-reduction-technique.md`
- `papers/notes/pending-ref-054-a-large-scale-sensitivity-analysis-on-latent-embeddings-an.md`
- `papers/notes/pending-ref-055-hypernp-interactive-visual-exploration-of-multidimensional.md`
- `papers/notes/pending-ref-121-understanding-how-dimension-reduction-tools-work-an-empiri.md`
- `papers/notes/pending-ref-130-mountaineer-topology-driven-visual-analytics-for-comparing.md`

### 9) Initialization/Seed Instability Hidden by Single Runs
Single-run screenshots can hide large initialization/seed variance in stochastic DR methods. A method may look reliable in one run while producing conflicting structure in another run under the same data and nominal settings.

Reliability action:
- Always report multi-seed stability when using initialization-sensitive methods.
- Keep initialization mode fixed during hyperparameter search, then separately evaluate initialization effect.
- If multi-seed rankings disagree, mark recommendation confidence as reduced and keep alternatives.

Source notes:
- `papers/notes/2020-kobak-initialization-tsne-umap.md`
- `papers/notes/pending-ref-029-stability-comparison-of-dimensionality-reduction-technique.md`
- `papers/notes/pending-ref-054-a-large-scale-sensitivity-analysis-on-latent-embeddings-an.md`
- `papers/notes/pending-ref-101-trimap-large-scale-dimensionality-reduction-using-triplets.md`
- `papers/notes/pending-ref-129-ens-t-sne-embedding-neighborhoods-simultaneously-t-sne.md`
- `papers/notes/pending-ref-142-umato-bridging-local-and-global-structures-for-reliable-vi.md`

### 10) Runtime-Quality Tradeoff Blind Spots
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
- `papers/notes/2017-random-projection-survey.md`

## Reliability Improvement Checklist

1. Confirm one primary analytical task before method selection.
2. Re-check task sequence when the analysis intent shifts.
3. Validate label separability before using class-aware metrics.
4. Use a multi-level reliability check set instead of a single metric.
5. Control scale when comparing stress/KL-related scores.
6. Freeze preprocessing, seeds, and initialization policy for fair comparison.
7. Log hyperparameter search space and optimization trace.
8. Include runtime feasibility with quality evidence.
9. Explain residual uncertainty and limits in the final recommendation.
10. Add an initialization/seed stability statement for stochastic methods.
