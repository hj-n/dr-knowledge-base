# SOM (Self-Organizing Map)

## Technique Summary
Topology-preserving map projection emphasizing neighborhood-order structure.

In this repository, the technique description is intentionally task-centered: the method is not automatically good, and is only appropriate when its distortion profile matches the analytical objective. That framing keeps method choice aligned with user intent instead of popularity.

The summary should be read together with task alignment and tradeoff sections before implementation. When the same dataset supports multiple objectives, this technique may be suitable for one objective and unsuitable for another.

## I/O Contract
- Input: general high-dimensional feature data (labels optional for supervised variants).
- Output: low-dimensional projection coordinates for analysis/visualization.

Input should be treated as a high-dimensional feature representation after data-audit and preprocessing decisions are locked. If normalization, distance definition, or label usage changes during tuning, the effective input contract changes as well and comparisons become noisy.

Output coordinates are analysis artifacts, not ground-truth geometry. They should be consumed according to the declared task, with explicit caution against over-interpreting axes, absolute distances, or visual separations outside the validated use case.

## Core Objective
Map high-dimensional data to low-dimensional grid/space while preserving neighborhood topology.

The objective function encodes which structural errors are cheap and which are expensive. Understanding that objective is essential because it predicts the kinds of distortions the method will tolerate when perfect preservation is impossible.

Method selection should therefore ask which distortions are acceptable for this task, and which are not. Choose this technique only when its objective-level priorities match that answer.

## Computation Outline
- Initialize map/codebook structure.
- Iteratively update codebook units with neighborhood cooperation.
- Project points to map positions and evaluate topology preservation.

Implementation quality depends on stable preprocessing, deterministic settings where possible, and explicit recording of optimization configuration. Most DR pipelines are sensitive to initialization or neighborhood construction choices, so hidden defaults can change conclusions.

For reproducible comparison, evaluate this technique under a fixed protocol and report parameter context with results. This converts the outline from a conceptual recipe into an auditable procedure for downstream agents and reviewers.

Detailed execution rule: keep map/grid configuration and neighborhood-decay schedule explicit. Prototype-map methods can tell very different stories under different grid designs.

## Hyperparameter Impact
- Map dimensionality/resolution controls topological detail and distortion patterns.
- Neighborhood-update schedule controls training dynamics and smoothness.

Hyperparameters determine the local-vs-global balance, optimization stability, and visual behavior of the embedding. They should be tuned against task-aligned metrics rather than aesthetics alone, especially when outputs influence model or policy decisions.

A practical default is Bayesian optimization with safety checks: fixed seed schedule, bounded search space, and multi-metric objective checks. This reduces manual trial-and-error while preserving traceability for why a specific configuration was selected.

Decision-level tuning rule: report both best score and stability behavior (seed variance / restart variance). A configuration that wins once but is unstable should not be the default recommendation.

## Practical Reliability Notes
SOM provides topology-aware organization that is useful for exploratory structure discovery and prototype-level interpretation. It can be effective when analysts need interpretable map organization rather than only scatterplot geometry.

SOM reliability depends on grid design, learning schedule, and neighborhood-decay policy. Treat these as task-level decisions and validate with external metrics; otherwise map aesthetics can be mistaken for trustworthy structure preservation.

## Notable Properties
- Strong topology-oriented interpretability in neighborhood terms.
- Topographic diagnostics provide explicit order-preservation signal.

Notable properties should be interpreted as operating characteristics, not guarantees. A property that is beneficial in one data regime can become a liability in another regime with different density, noise level, or manifold complexity.

Use these properties to narrow candidates early, then confirm with metric evidence and task-specific validation. That sequence keeps the workflow grounded in evidence instead of anecdotal method reputation.

## Strengths
This technique is strong for topology-preserving map organization and neighborhood structure visualization. It is useful for structured map-based exploration where adjacency preservation is important.

It can provide interpretable map topology diagnostics beyond pure scatter-style embeddings.


## Task Alignment
- Inferred alignment: best-aligned tasks
  - Neighborhood identification
  - Cluster identification
  - Outlier identification

Task alignment indicates where this technique is expected to provide the most reliable utility under the current evidence base. Treat non-listed tasks as unsupported until new source-backed evidence is added.

When a project requires multiple task outcomes, combine this section with metric-level alignment and require agreement across both layers. If technique and metric recommendations diverge, collect more evidence before production use.

Operational alignment rule: method alignment should constrain candidate ranking, but final acceptance still requires agreement with task-aligned reliability check sets and label-separation check status.

## Known Tradeoffs
- Topology preservation does not guarantee metric distance preservation.

Tradeoffs are expected and should be made explicit to users before final selection. A method that improves neighborhood fidelity may worsen global distance faithfulness, and vice versa, so optimization must reflect the task hierarchy.

In reporting, document which tradeoffs were accepted and why they were acceptable for the chosen task. This explanation step is part of the contract for trustworthy DR recommendations in this repository.

Communication rule: document one concrete downside that remained after tuning (for example global drift, local fragmentation, or runtime burden) so end users understand residual risk.

## Source Notes
- `papers/notes/zadu-ref-10-download-2.md` (ZR10-E2, ZR10-E3, ZR10-E4, ZR10-E5)
- `papers/notes/zadu-ref-02-1-s2-0-s0925231209000101-main.md` (ZR02-E4)

- `papers/notes/pending-ref-044-classimap-a-new-dimension-reduction-technique-for-explorat.md` (pending-reference evidence)
- `papers/notes/pending-ref-073-trustworthiness-and-metrics-in-visualizing-similarity-of-g.md` (pending-reference evidence)
- `papers/notes/pending-ref-125-a-methodology-to-compare-dimensionality-reduction-algorith.md` (pending-reference evidence)
- `papers/notes/pending-ref-136-survey-and-comparison-of-quality-measures-for-selforganizi.md` (pending-reference evidence)
- `papers/notes/pending-ref-154-recent-advances-in-nonlinear-dimensionality-reduction-mani.md` (pending-reference evidence)
