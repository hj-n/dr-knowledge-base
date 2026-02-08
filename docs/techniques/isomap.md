# Isomap

## Technique Summary
Graph-geodesic manifold projection using neighborhood graph shortest-path distances.

In this repository, the technique description is intentionally task-centered: the method is not automatically good, and is only appropriate when its distortion profile matches the analytical objective. That framing keeps method choice aligned with user intent instead of popularity.

The summary should be read together with task alignment and tradeoff sections before implementation. When the same dataset supports multiple objectives, this technique may be suitable for one objective and unsuitable for another.

## I/O Contract
- Input: general high-dimensional feature data (labels optional for supervised variants).
- Output: low-dimensional projection coordinates for analysis/visualization.

Input should be treated as a high-dimensional feature representation after data-audit and preprocessing decisions are locked. If normalization, distance definition, or label usage changes during tuning, the effective input contract changes as well and comparisons become noisy.

Output coordinates are analysis artifacts, not ground-truth geometry. They should be consumed according to the declared task, with explicit caution against over-interpreting axes, absolute distances, or visual separations outside the validated use case.

## Core Objective
Preserve manifold geodesic structure in low-dimensional coordinates.

The objective function encodes which structural errors are cheap and which are expensive. Understanding that objective is essential because it predicts the kinds of distortions the method will tolerate when perfect preservation is impossible.

Method selection should therefore ask which distortions are acceptable for this task, and which are not. Choose this technique only when its objective-level priorities match that answer.

## Computation Outline
- Construct neighborhood graph in high-dimensional space.
- Estimate geodesic distances via shortest paths.
- Apply MDS-style embedding on geodesic distance matrix.

Implementation quality depends on stable preprocessing, deterministic settings where possible, and explicit recording of optimization configuration. Most DR pipelines are sensitive to initialization or neighborhood construction choices, so hidden defaults can change conclusions.

For reproducible comparison, evaluate this technique under a fixed protocol and report parameter context with results. This converts the outline from a conceptual recipe into an auditable procedure for downstream agents and reviewers.

Detailed execution rule: evaluate geodesic graph stability (connectivity and shortest-path robustness) before trusting global interpretation. Unstable geodesics produce fragile global claims.

## Hyperparameter Impact
- Neighborhood graph size (`k` or radius) controls connectivity and manifold approximation.
- Distance metric and graph-connectivity handling strongly affect output stability.

Hyperparameters determine the local-vs-global balance, optimization stability, and visual behavior of the embedding. They should be tuned against task-aligned metrics rather than aesthetics alone, especially when outputs influence model or policy decisions.

A practical default is Bayesian optimization with guardrails: fixed seed schedule, bounded search space, and multi-metric objective checks. This reduces manual trial-and-error while preserving traceability for why a specific configuration was selected.

Decision-level tuning rule: report both best score and stability behavior (seed variance / restart variance). A configuration that wins once but is unstable should not be the default recommendation.

## Practical Reliability Notes
Isomap relies on graph geodesics, so neighborhood graph connectivity is a first-order reliability condition. If the graph is fragmented, global geodesic estimates become unstable and downstream projection can create misleading long-range structure.

Before final selection, check graph connectivity diagnostics and sensitivity to neighborhood-size changes. If major topology changes occur across small neighborhood shifts, report reduced confidence for global-distance interpretation.

## Notable Properties
- Can recover global manifold geometry when sampling/connectivity are adequate.
- Sensitive to noise and disconnected graph artifacts.

Notable properties should be interpreted as operating characteristics, not guarantees. A property that is beneficial in one data regime can become a liability in another regime with different density, noise level, or manifold complexity.

Use these properties to narrow candidates early, then confirm with metric evidence and task-specific validation. That sequence keeps the workflow grounded in evidence instead of anecdotal method reputation.

## Strengths
This technique is strong for manifold-geodesic preservation and can reveal global nonlinear geometry beyond linear projections. It is particularly useful when geodesic relationships are important to the analytical question.

It often serves as a global-structure nonlinear baseline when local-neighbor-only methods are insufficient.


## Task Alignment
- Inferred alignment: best-aligned tasks
  - Neighborhood identification
  - Cluster identification
  - Outlier identification

Task alignment indicates where this technique is expected to provide the most reliable utility under the current evidence base. Treat non-listed tasks as unsupported until new source-backed evidence is added.

When a project requires multiple task outcomes, combine this section with metric-level alignment and require agreement across both layers. If technique and metric recommendations diverge, collect more evidence before production use.

Operational alignment rule: method alignment should constrain candidate ranking, but final acceptance still requires agreement with task-aligned metric bundles and warning-gate status.

## Known Tradeoffs
- Graph construction failure can dominate embedding quality.

Tradeoffs are expected and should be made explicit to users before final selection. A method that improves neighborhood fidelity may worsen global distance faithfulness, and vice versa, so optimization must reflect the task hierarchy.

In reporting, document which tradeoffs were accepted and why they were acceptable for the chosen task. This explanation step is part of the contract for trustworthy DR recommendations in this repository.

Communication rule: document one concrete downside that remained after tuning (for example global drift, local fragmentation, or runtime burden) so end users understand residual risk.

## Source Notes
- `papers/notes/zadu-ref-01-1-s2-0-s0893608006000724-main.md` (ZR01-E7, ZR01-E8)
- `papers/notes/zadu-ref-09-supervised-nonlinear-dimensionality-reduction-for-visualization-and-classificati.md` (ZR09-E1, ZR09-E3, ZR09-E4)

- `papers/notes/pending-ref-004-information-retrieval-perspective-to-nonlinear-dimensional.md` (pending-reference evidence)
- `papers/notes/pending-ref-016-visual-interaction-with-dimensionality-reduction-a-structu.md` (pending-reference evidence)
- `papers/notes/pending-ref-019-local-multidimensional-scaling.md` (pending-reference evidence)
- `papers/notes/pending-ref-024-viscoder-a-tool-for-visually-comparing-dimensionality-redu.md` (pending-reference evidence)
- `papers/notes/pending-ref-029-stability-comparison-of-dimensionality-reduction-technique.md` (pending-reference evidence)
- `papers/notes/pending-ref-043-local-procrustes-for-manifold-embedding-a-measure-of-embed.md` (pending-reference evidence)
- `papers/notes/pending-ref-045-a-behavioral-investigation-of-dimensionality-reduction.md` (pending-reference evidence)
- `papers/notes/pending-ref-048-linear-dimensionality-reduction-survey-insights-and-genera.md` (pending-reference evidence)
