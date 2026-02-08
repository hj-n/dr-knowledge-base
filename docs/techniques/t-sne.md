# t-SNE

## Technique Summary
Stochastic neighborhood-preserving projection widely used for local structure exploration.

In this repository, the technique description is intentionally task-centered: the method is not automatically good, and is only appropriate when its distortion profile matches the analytical objective. That framing keeps method choice aligned with user intent instead of popularity.

The summary should be read together with task alignment and tradeoff sections before implementation. When the same dataset supports multiple objectives, this technique may be suitable for one objective and unsuitable for another.

## I/O Contract
- Input: general high-dimensional feature data (labels optional for supervised variants).
- Output: low-dimensional projection coordinates for analysis/visualization.

Input should be treated as a high-dimensional feature representation after data-audit and preprocessing decisions are locked. If normalization, distance definition, or label usage changes during tuning, the effective input contract changes as well and comparisons become noisy.

Output coordinates are analysis artifacts, not ground-truth geometry. They should be consumed according to the declared task, with explicit caution against over-interpreting axes, absolute distances, or visual separations outside the validated use case.

## Core Objective
Preserve local neighbor probabilities in low-dimensional space with heavy-tailed low-space similarity model.

The objective function encodes which structural errors are cheap and which are expensive. Understanding that objective is essential because it predicts the kinds of distortions the method will tolerate when perfect preservation is impossible.

Method selection should therefore ask which distortions are acceptable for this task, and which are not. Choose this technique only when its objective-level priorities match that answer.

## Computation Outline
- Compute high-dimensional neighbor probabilities (scale via perplexity).
- Initialize low-dimensional coordinates.
- Optimize KL-divergence objective via gradient-based updates.

Implementation quality depends on stable preprocessing, deterministic settings where possible, and explicit recording of optimization configuration. Most DR pipelines are sensitive to initialization or neighborhood construction choices, so hidden defaults can change conclusions.

For reproducible comparison, evaluate this technique under a fixed protocol and report parameter context with results. This converts the outline from a conceptual recipe into an auditable procedure for downstream agents and reviewers.

Detailed execution rule: run multiple seeds under the same initialization mode and compare structural consistency before accepting conclusions. For local stochastic methods, a single visually appealing run is not sufficient evidence.

## Hyperparameter Impact
- `perplexity` controls effective neighborhood scale.
- `learning rate`, iteration schedule, and noise/jitter handling affect convergence and stability.
- initialization policy (random vs informative) can materially change global-structure behavior and comparison outcomes.
- Scale handling policy matters for downstream stress/KL-based evaluation comparisons.

Hyperparameters determine the local-vs-global balance, optimization stability, and visual behavior of the embedding. They should be tuned against task-aligned metrics rather than aesthetics alone, especially when outputs influence model or policy decisions.

A practical default is Bayesian optimization with guardrails: fixed seed schedule, bounded search space, and multi-metric objective checks. This reduces manual trial-and-error while preserving traceability for why a specific configuration was selected.

Decision-level tuning rule: tune local-scale controls and optimization controls jointly, then verify that gains remain under seed perturbation. If seed sensitivity is high, downgrade confidence and keep fallback candidates.

## Practical Reliability Notes
t-SNE should be treated as a local-neighborhood optimizer, not a global-distance map. Perplexity controls effective neighborhood scale, so the same dataset can yield different cluster granularity under different perplexity values. Always report perplexity together with seed and initialization policy.

For reliable comparison workflows, keep initialization fixed (PCA baseline for global-sensitive contexts) and evaluate multiple seeds. If conclusions about cluster relationship or outlier identity change across seeds, mark confidence as reduced and keep alternative candidates in the final recommendation.

## Notable Properties
- Excellent local grouping/separation visualization behavior when tuned appropriately.
- Not designed for faithful global distance interpretation.

Notable properties should be interpreted as operating characteristics, not guarantees. A property that is beneficial in one data regime can become a liability in another regime with different density, noise level, or manifold complexity.

Use these properties to narrow candidates early, then confirm with metric evidence and task-specific validation. That sequence keeps the workflow grounded in evidence instead of anecdotal method reputation.

## Strengths
This technique is strong for local neighborhood and cluster pattern visualization when tuned appropriately. It frequently produces clear local grouping behavior for exploratory local-structure tasks.

It is useful when local relationship interpretation dominates, and global distance reading is explicitly de-emphasized.


## Task Alignment
- Direct evidence: best-aligned tasks
  - Neighborhood identification
  - Outlier identification
  - Cluster identification

Task alignment indicates where this technique is expected to provide the most reliable utility under the current evidence base. Treat non-listed tasks as unsupported until new source-backed evidence is added.

When a project requires multiple task outcomes, combine this section with metric-level alignment and require agreement across both layers. If technique and metric recommendations diverge, collect more evidence before production use.

Operational alignment rule: method alignment should constrain candidate ranking, but final acceptance still requires agreement with task-aligned metric bundles and warning-gate status.

## Known Tradeoffs
- Global distance and density conclusions can be misleading without task-aware caution.

Tradeoffs are expected and should be made explicit to users before final selection. A method that improves neighborhood fidelity may worsen global distance faithfulness, and vice versa, so optimization must reflect the task hierarchy.

In reporting, document which tradeoffs were accepted and why they were acceptable for the chosen task. This explanation step is part of the contract for trustworthy DR recommendations in this repository.

Communication rule: document one concrete downside that remained after tuning (for example global drift, local fragmentation, or runtime burden) so end users understand residual risk.

## Source Notes
- `papers/notes/2506.08725v2-stop-misusing-tsne-umap.md` (JEON25-E2)
- `papers/notes/zadu-ref-04-2510-08660v1.md` (ZR04-E9, ZR04-E10)
- `papers/notes/zadu-ref-17-ref13-stochastic-neighbor-embedding.md` (ZR17-E7, ZR17-E8, ZR17-E9)
- `papers/notes/2020-kobak-initialization-tsne-umap.md` (CLAIM-KOBAK20-C1, CLAIM-KOBAK20-C2, CLAIM-KOBAK20-C3)
- `papers/notes/2022-revisiting-dr-visual-cluster-analysis.md` (CLAIM-REV22-C2)

- `papers/notes/pending-ref-002-empirical-guidance-on-scatterplot-and-dimension-reduction.md` (pending-reference evidence)
- `papers/notes/pending-ref-004-information-retrieval-perspective-to-nonlinear-dimensional.md` (pending-reference evidence)
- `papers/notes/pending-ref-009-uniform-manifold-approximation-with-two-phase-optimization.md` (pending-reference evidence)
- `papers/notes/pending-ref-015-feature-learning-for-nonlinear-dimensionality-reduction-to.md` (pending-reference evidence)
- `papers/notes/pending-ref-024-viscoder-a-tool-for-visually-comparing-dimensionality-redu.md` (pending-reference evidence)
- `papers/notes/pending-ref-026-umap-uniform-manifold-approximation-and-projection-for-dim.md` (pending-reference evidence)
- `papers/notes/pending-ref-029-stability-comparison-of-dimensionality-reduction-technique.md` (pending-reference evidence)
- `papers/notes/pending-ref-039-assessing-singlecell-transcriptomic-variability-through-de.md` (pending-reference evidence)
