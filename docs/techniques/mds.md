# MDS

## Technique Summary
Distance-fitting projection family minimizing stress-type distance distortion objectives.

In this repository, the technique description is intentionally task-centered: the method is not automatically good, and is only appropriate when its distortion profile matches the analytical objective. That framing keeps method choice aligned with user intent instead of popularity.

The summary should be read together with task alignment and tradeoff sections before implementation. When the same dataset supports multiple objectives, this technique may be suitable for one objective and unsuitable for another.

## I/O Contract
- Input: general high-dimensional feature data (labels optional for supervised variants).
- Output: low-dimensional projection coordinates for analysis/visualization.

Input should be treated as a high-dimensional feature representation after data-audit and preprocessing decisions are locked. If normalization, distance definition, or label usage changes during tuning, the effective input contract changes as well and comparisons become noisy.

Output coordinates are analysis artifacts, not ground-truth geometry. They should be consumed according to the declared task, with explicit caution against over-interpreting axes, absolute distances, or visual separations outside the validated use case.

## Core Objective
Place points in low-dimensional space such that pairwise distances best match original-space distances.

The objective function encodes which structural errors are cheap and which are expensive. Understanding that objective is essential because it predicts the kinds of distortions the method will tolerate when perfect preservation is impossible.

Method selection should therefore ask which distortions are acceptable for this task, and which are not. Choose this technique only when its objective-level priorities match that answer.

## Computation Outline
- Compute pairwise dissimilarity matrix in original space.
- Choose metric/non-metric stress formulation.
- Optimize low-dimensional coordinates to minimize stress.

Implementation quality depends on stable preprocessing, deterministic settings where possible, and explicit recording of optimization configuration. Most DR pipelines are sensitive to initialization or neighborhood construction choices, so hidden defaults can change conclusions.

For reproducible comparison, evaluate this technique under a fixed protocol and report parameter context with results. This converts the outline from a conceptual recipe into an auditable procedure for downstream agents and reviewers.

Detailed execution rule: run this method under a fixed preprocessing contract and log all stochastic controls (seed, restart index, initialization metadata) so comparison runs are auditable.

## Hyperparameter Impact
- Stress variant and weighting policy change local-vs-global emphasis.
- Initialization and optimization schedule affect convergence and local minima behavior.

Hyperparameters determine the local-vs-global balance, optimization stability, and visual behavior of the embedding. They should be tuned against task-aligned metrics rather than aesthetics alone, especially when outputs influence model or policy decisions.

A practical default is Bayesian optimization with guardrails: fixed seed schedule, bounded search space, and multi-metric objective checks. This reduces manual trial-and-error while preserving traceability for why a specific configuration was selected.

Decision-level tuning rule: report both best score and stability behavior (seed variance / restart variance). A configuration that wins once but is unstable should not be the default recommendation.

## Practical Reliability Notes
MDS variants optimize distance-fitting objectives and therefore can be effective for point-distance and cluster-distance tasks when scale handling is controlled. However, iterative MDS variants can converge to different local minima depending on initialization.

For fair comparisons, run a fixed restart protocol and report best-value plus variability, not only a single best run. If variability is high, avoid using one embedding snapshot as sole evidence for structural claims.

## Notable Properties
- Canonical baseline for global distance-faithfulness tasks.
- Objective is explicit and directly tied to distance distortion.

Notable properties should be interpreted as operating characteristics, not guarantees. A property that is beneficial in one data regime can become a liability in another regime with different density, noise level, or manifold complexity.

Use these properties to narrow candidates early, then confirm with metric evidence and task-specific validation. That sequence keeps the workflow grounded in evidence instead of anecdotal method reputation.

## Strengths
This technique is strong for global distance-structure preservation and is directly aligned with distance-investigation tasks. It is a robust baseline for analyses where pairwise geometry interpretation is central.

It is useful when the objective prioritizes faithful global distance relationships over local cluster aesthetics.


## Task Alignment
- Direct evidence: best-aligned tasks
  - Point distance investigation
  - Class separability investigation
  - Cluster distance investigation
  - Cluster density investigation

Task alignment indicates where this technique is expected to provide the most reliable utility under the current evidence base. Treat non-listed tasks as unsupported until new source-backed evidence is added.

When a project requires multiple task outcomes, combine this section with metric-level alignment and require agreement across both layers. If technique and metric recommendations diverge, collect more evidence before production use.

Operational alignment rule: prioritize for distance and density tasks; for neighborhood-centric tasks use as baseline or guardrail, not as sole recommendation evidence.

## Known Tradeoffs
- Stress values can be misread without consistent scale-handling policy.

Tradeoffs are expected and should be made explicit to users before final selection. A method that improves neighborhood fidelity may worsen global distance faithfulness, and vice versa, so optimization must reflect the task hierarchy.

In reporting, document which tradeoffs were accepted and why they were acceptable for the chosen task. This explanation step is part of the contract for trustworthy DR recommendations in this repository.

Communication rule: explain what local structure may be sacrificed to preserve global trends, and confirm this with local metrics before finalization.

## Source Notes
- `papers/notes/2506.08725v2-stop-misusing-tsne-umap.md` (JEON25-E3, JEON25-E4, JEON25-E5, JEON25-E6)
- `papers/notes/zadu-ref-07-local-multidimensional-scaling-for-nonlinear-dimension-reduction-graph-drawing-a.md` (ZR07-E2, ZR07-E8)
- `papers/notes/zadu-ref-03-2408-07724v2.md` (ZR03-E6, ZR03-E7)
- `papers/notes/2019-mdp-visual-analytics-survey.md` (CLAIM-MDP19-C1, CLAIM-MDP19-C2)
- `papers/notes/2015-gisbrecht-nonlinear-dr-visualization.md` (CLAIM-GIS15-C1)

- `papers/notes/pending-ref-002-empirical-guidance-on-scatterplot-and-dimension-reduction.md` (pending-reference evidence)
- `papers/notes/pending-ref-004-information-retrieval-perspective-to-nonlinear-dimensional.md` (pending-reference evidence)
- `papers/notes/pending-ref-013-a-survey-of-dimension-reduction-methods-for-high-dimension.md` (pending-reference evidence)
- `papers/notes/pending-ref-014-charting-a-manifold.md` (pending-reference evidence)
- `papers/notes/pending-ref-016-visual-interaction-with-dimensionality-reduction-a-structu.md` (pending-reference evidence)
- `papers/notes/pending-ref-019-local-multidimensional-scaling.md` (pending-reference evidence)
- `papers/notes/pending-ref-024-viscoder-a-tool-for-visually-comparing-dimensionality-redu.md` (pending-reference evidence)
- `papers/notes/pending-ref-026-umap-uniform-manifold-approximation-and-projection-for-dim.md` (pending-reference evidence)
