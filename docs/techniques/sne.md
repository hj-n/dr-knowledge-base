# SNE

## Technique Summary
Probabilistic neighborhood projection minimizing KL divergence between high- and low-dimensional neighbor distributions.

In this repository, the technique description is intentionally task-centered: the method is not automatically good, and is only appropriate when its distortion profile matches the analytical objective. That framing keeps method choice aligned with user intent instead of popularity.

The summary should be read together with task alignment and tradeoff sections before implementation. When the same dataset supports multiple objectives, this technique may be suitable for one objective and unsuitable for another.

## I/O Contract
- Input: general high-dimensional feature data (labels optional for supervised variants).
- Output: low-dimensional projection coordinates for analysis/visualization.

Input should be treated as a high-dimensional feature representation after data-audit and preprocessing decisions are locked. If normalization, distance definition, or label usage changes during tuning, the effective input contract changes as well and comparisons become noisy.

Output coordinates are analysis artifacts, not ground-truth geometry. They should be consumed according to the declared task, with explicit caution against over-interpreting axes, absolute distances, or visual separations outside the validated use case.

## Core Objective
Preserve neighborhood identities probabilistically via divergence minimization.

The objective function encodes which structural errors are cheap and which are expensive. Understanding that objective is essential because it predicts the kinds of distortions the method will tolerate when perfect preservation is impossible.

Method selection should therefore ask which distortions are acceptable for this task, and which are not. Choose this technique only when its objective-level priorities match that answer.

## Computation Outline
- Construct high-dimensional neighbor probability distributions.
- Construct low-dimensional neighbor probability distributions.
- Optimize embedding by minimizing KL-divergence objective.

Implementation quality depends on stable preprocessing, deterministic settings where possible, and explicit recording of optimization configuration. Most DR pipelines are sensitive to initialization or neighborhood construction choices, so hidden defaults can change conclusions.

For reproducible comparison, evaluate this technique under a fixed protocol and report parameter context with results. This converts the outline from a conceptual recipe into an auditable procedure for downstream agents and reviewers.

Detailed execution rule: run multiple seeds under the same initialization mode and compare structural consistency before accepting conclusions. For local stochastic methods, a single visually appealing run is not sufficient evidence.

## Hyperparameter Impact
- `perplexity` sets effective local-neighbor scale.
- `learning rate` and jitter/noise schedule influence convergence and local minima.

Hyperparameters determine the local-vs-global balance, optimization stability, and visual behavior of the embedding. They should be tuned against task-aligned metrics rather than aesthetics alone, especially when outputs influence model or policy decisions.

A practical default is Bayesian optimization with guardrails: fixed seed schedule, bounded search space, and multi-metric objective checks. This reduces manual trial-and-error while preserving traceability for why a specific configuration was selected.

Decision-level tuning rule: tune local-scale controls and optimization controls jointly, then verify that gains remain under seed perturbation. If seed sensitivity is high, downgrade confidence and keep fallback candidates.

## Practical Reliability Notes
SNE is historically important and still useful as a conceptual baseline for probabilistic neighborhood embedding behavior. It helps interpret why later variants (for example t-SNE) change global/local behavior.

For modern workflows, use SNE mainly in comparative or methodological contexts rather than as a default production recommendation. If used, apply strong seed and optimization stability reporting because convergence behavior can vary substantially.

## Notable Properties
- Probability-based neighborhood modeling is a notable conceptual strength.
- Optimization can be slow and schedule-sensitive.

Notable properties should be interpreted as operating characteristics, not guarantees. A property that is beneficial in one data regime can become a liability in another regime with different density, noise level, or manifold complexity.

Use these properties to narrow candidates early, then confirm with metric evidence and task-specific validation. That sequence keeps the workflow grounded in evidence instead of anecdotal method reputation.

## Strengths
This technique is strong for probabilistic neighborhood-preservation formulations that capture local similarity behavior. It provides a foundational local-probability perspective for neighborhood embeddings.

It is useful when local similarity distributions are the core fidelity target.


## Task Alignment
- Inferred alignment: best-aligned tasks
  - Neighborhood identification
  - Outlier identification
  - Cluster identification

Task alignment indicates where this technique is expected to provide the most reliable utility under the current evidence base. Treat non-listed tasks as unsupported until new source-backed evidence is added.

When a project requires multiple task outcomes, combine this section with metric-level alignment and require agreement across both layers. If technique and metric recommendations diverge, collect more evidence before production use.

Operational alignment rule: method alignment should constrain candidate ranking, but final acceptance still requires agreement with task-aligned metric bundles and warning-gate status.

## Known Tradeoffs
- Needs careful optimization configuration for stable reproducible results.

Tradeoffs are expected and should be made explicit to users before final selection. A method that improves neighborhood fidelity may worsen global distance faithfulness, and vice versa, so optimization must reflect the task hierarchy.

In reporting, document which tradeoffs were accepted and why they were acceptable for the chosen task. This explanation step is part of the contract for trustworthy DR recommendations in this repository.

Communication rule: document one concrete downside that remained after tuning (for example global drift, local fragmentation, or runtime burden) so end users understand residual risk.

## Source Notes
- `papers/notes/zadu-ref-17-ref13-stochastic-neighbor-embedding.md` (ZR17-E1, ZR17-E3, ZR17-E4, ZR17-E7, ZR17-E8, ZR17-E9)

- `papers/notes/pending-ref-002-empirical-guidance-on-scatterplot-and-dimension-reduction.md` (pending-reference evidence)
- `papers/notes/pending-ref-004-information-retrieval-perspective-to-nonlinear-dimensional.md` (pending-reference evidence)
- `papers/notes/pending-ref-009-uniform-manifold-approximation-with-two-phase-optimization.md` (pending-reference evidence)
- `papers/notes/pending-ref-015-feature-learning-for-nonlinear-dimensionality-reduction-to.md` (pending-reference evidence)
- `papers/notes/pending-ref-024-viscoder-a-tool-for-visually-comparing-dimensionality-redu.md` (pending-reference evidence)
- `papers/notes/pending-ref-026-umap-uniform-manifold-approximation-and-projection-for-dim.md` (pending-reference evidence)
- `papers/notes/pending-ref-029-stability-comparison-of-dimensionality-reduction-technique.md` (pending-reference evidence)
- `papers/notes/pending-ref-032-dimensionality-reduction-for-visualizing-single-cell-data.md` (pending-reference evidence)
