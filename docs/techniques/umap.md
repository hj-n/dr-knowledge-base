# UMAP

## Technique Summary
Manifold-learning projection emphasizing local neighborhood structure with scalable optimization.

In this repository, the technique description is intentionally task-centered: the method is not automatically good, and is only appropriate when its distortion profile matches the analytical objective. That framing keeps method choice aligned with user intent instead of popularity.

The summary should be read together with task alignment and tradeoff sections before implementation. When the same dataset supports multiple objectives, this technique may be suitable for one objective and unsuitable for another.

## I/O Contract
- Input: general high-dimensional feature data (labels optional for supervised variants).
- Output: low-dimensional projection coordinates for analysis/visualization.

Input should be treated as a high-dimensional feature representation after data-audit and preprocessing decisions are locked. If normalization, distance definition, or label usage changes during tuning, the effective input contract changes as well and comparisons become noisy.

Output coordinates are analysis artifacts, not ground-truth geometry. They should be consumed according to the declared task, with explicit caution against over-interpreting axes, absolute distances, or visual separations outside the validated use case.

## Core Objective
Build and optimize a low-dimensional representation that preserves fuzzy local neighborhood graph structure.

The objective function encodes which structural errors are cheap and which are expensive. Understanding that objective is essential because it predicts the kinds of distortions the method will tolerate when perfect preservation is impossible.

Method selection should therefore ask which distortions are acceptable for this task, and which are not. Choose this technique only when its objective-level priorities match that answer.

## Computation Outline
- Construct high-dimensional neighborhood graph.
- Transform to fuzzy simplicial-set style objective.
- Optimize low-dimensional coordinates to preserve graph structure.

Implementation quality depends on stable preprocessing, deterministic settings where possible, and explicit recording of optimization configuration. Most DR pipelines are sensitive to initialization or neighborhood construction choices, so hidden defaults can change conclusions.

For reproducible comparison, evaluate this technique under a fixed protocol and report parameter context with results. This converts the outline from a conceptual recipe into an auditable procedure for downstream agents and reviewers.

Detailed execution rule: run multiple seeds under the same initialization mode and compare structural consistency before accepting conclusions. For local stochastic methods, a single visually appealing run is not sufficient evidence.

## Hyperparameter Impact
- neighborhood and optimization settings remain key controls for local-vs-global behavior.
- initialization policy can strongly affect global-structure interpretation and reproducibility in comparisons.
- Operationally, neighborhood-scale and optimization settings should be tuned with task-aligned metrics and recorded assumptions.

Hyperparameters determine the local-vs-global balance, optimization stability, and visual behavior of the embedding. They should be tuned against task-aligned metrics rather than aesthetics alone, especially when outputs influence model or policy decisions.

A practical default is Bayesian optimization with guardrails: fixed seed schedule, bounded search space, and multi-metric objective checks. This reduces manual trial-and-error while preserving traceability for why a specific configuration was selected.

Decision-level tuning rule: tune local-scale controls and optimization controls jointly, then verify that gains remain under seed perturbation. If seed sensitivity is high, downgrade confidence and keep fallback candidates.

## Practical Reliability Notes
UMAP behavior is strongly controlled by neighborhood size and minimum-distance style controls, which jointly define local packing and cluster spacing. Bayesian optimization trials should be interpreted as task-conditional model choices, not cosmetic tuning.

When UMAP is used for decision support, compare at least one local metric and one global metric under fixed preprocessing and fixed initialization policy. This guards against selecting configurations that look visually clean but are unstable or misaligned to the declared analytical task.

## Notable Properties
- Strong local-structure embeddings for many exploratory tasks.
- Task fit should still be checked before treating as default method.

Notable properties should be interpreted as operating characteristics, not guarantees. A property that is beneficial in one data regime can become a liability in another regime with different density, noise level, or manifold complexity.

Use these properties to narrow candidates early, then confirm with metric evidence and task-specific validation. That sequence keeps the workflow grounded in evidence instead of anecdotal method reputation.

## Strengths
This technique is strong for scalable local-neighborhood manifold embeddings with good practical performance. It often yields strong local-structure organization while handling larger datasets efficiently.

It is useful for neighborhood/outlier/cluster exploration under runtime constraints compared with heavier local methods.


## Task Alignment
- Direct evidence: best-aligned tasks
  - Neighborhood identification
  - Outlier identification
  - Cluster identification

Task alignment indicates where this technique is expected to provide the most reliable utility under the current evidence base. Treat non-listed tasks as unsupported until new source-backed evidence is added.

When a project requires multiple task outcomes, combine this section with metric-level alignment and require agreement across both layers. If technique and metric recommendations diverge, collect more evidence before production use.

Operational alignment rule: method alignment should constrain candidate ranking, but final acceptance still requires agreement with task-aligned metric bundles and warning-gate status.

## Known Tradeoffs
- Not default for global distance/density tasks in the 7-task taxonomy.

Tradeoffs are expected and should be made explicit to users before final selection. A method that improves neighborhood fidelity may worsen global distance faithfulness, and vice versa, so optimization must reflect the task hierarchy.

In reporting, document which tradeoffs were accepted and why they were acceptable for the chosen task. This explanation step is part of the contract for trustworthy DR recommendations in this repository.

Communication rule: document one concrete downside that remained after tuning (for example global drift, local fragmentation, or runtime burden) so end users understand residual risk.

## Source Notes
- `papers/notes/2506.08725v2-stop-misusing-tsne-umap.md` (JEON25-E2, JEON25-E3, JEON25-E4, JEON25-E5, JEON25-E6)
- `papers/notes/2020-kobak-initialization-tsne-umap.md` (CLAIM-KOBAK20-C1, CLAIM-KOBAK20-C2, CLAIM-KOBAK20-C3)
- `papers/notes/2022-revisiting-dr-visual-cluster-analysis.md` (CLAIM-REV22-C2)

- `papers/notes/pending-ref-009-uniform-manifold-approximation-with-two-phase-optimization.md` (pending-reference evidence)
- `papers/notes/pending-ref-015-feature-learning-for-nonlinear-dimensionality-reduction-to.md` (pending-reference evidence)
- `papers/notes/pending-ref-026-umap-uniform-manifold-approximation-and-projection-for-dim.md` (pending-reference evidence)
- `papers/notes/pending-ref-032-dimensionality-reduction-for-visualizing-single-cell-data.md` (pending-reference evidence)
- `papers/notes/pending-ref-039-assessing-singlecell-transcriptomic-variability-through-de.md` (pending-reference evidence)
- `papers/notes/pending-ref-041-quantitative-evaluation-of-time-dependent-multidimensional.md` (pending-reference evidence)
- `papers/notes/pending-ref-055-hypernp-interactive-visual-exploration-of-multidimensional.md` (pending-reference evidence)
- `papers/notes/pending-ref-077-assessing-single-cell-transcriptomic-variability-through-d.md` (pending-reference evidence)
