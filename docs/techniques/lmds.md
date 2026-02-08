# LMDS (Local Multidimensional Scaling)

## Technique Summary
Localized MDS variant with stress design focused on neighborhood faithfulness.

In this repository, the technique description is intentionally task-centered: the method is not automatically good, and is only appropriate when its distortion profile matches the analytical objective. That framing keeps method choice aligned with user intent instead of popularity.

The summary should be read together with task alignment and tradeoff sections before implementation. When the same dataset supports multiple objectives, this technique may be suitable for one objective and unsuitable for another.

## I/O Contract
- Input: general high-dimensional feature data (labels optional for supervised variants).
- Output: low-dimensional projection coordinates for analysis/visualization.

Input should be treated as a high-dimensional feature representation after data-audit and preprocessing decisions are locked. If normalization, distance definition, or label usage changes during tuning, the effective input contract changes as well and comparisons become noisy.

Output coordinates are analysis artifacts, not ground-truth geometry. They should be consumed according to the declared task, with explicit caution against over-interpreting axes, absolute distances, or visual separations outside the validated use case.

## Core Objective
Optimize a localized stress objective emphasizing local neighborhoods while controlling nonlocal effects.

The objective function encodes which structural errors are cheap and which are expensive. Understanding that objective is essential because it predicts the kinds of distortions the method will tolerate when perfect preservation is impossible.

Method selection should therefore ask which distortions are acceptable for this task, and which are not. Choose this technique only when its objective-level priorities match that answer.

## Computation Outline
- Define localized stress objective over selected neighborhood relations.
- Introduce nonlocal repulsion to stabilize embedding.
- Tune parameters with local-faithfulness criteria and diagnostics.

Implementation quality depends on stable preprocessing, deterministic settings where possible, and explicit recording of optimization configuration. Most DR pipelines are sensitive to initialization or neighborhood construction choices, so hidden defaults can change conclusions.

For reproducible comparison, evaluate this technique under a fixed protocol and report parameter context with results. This converts the outline from a conceptual recipe into an auditable procedure for downstream agents and reviewers.

Detailed execution rule: run multiple seeds under the same initialization mode and compare structural consistency before accepting conclusions. For local stochastic methods, a single visually appealing run is not sufficient evidence.

## Hyperparameter Impact
- Repulsive-force strength changes local-vs-global balance.
- Neighborhood size directly changes localization scale and faithfulness profile.

Hyperparameters determine the local-vs-global balance, optimization stability, and visual behavior of the embedding. They should be tuned against task-aligned metrics rather than aesthetics alone, especially when outputs influence model or policy decisions.

A practical default is Bayesian optimization with guardrails: fixed seed schedule, bounded search space, and multi-metric objective checks. This reduces manual trial-and-error while preserving traceability for why a specific configuration was selected.

Decision-level tuning rule: tune local-scale controls and optimization controls jointly, then verify that gains remain under seed perturbation. If seed sensitivity is high, downgrade confidence and keep fallback candidates.

## Practical Reliability Notes
Local MDS families provide explicit local-structure control and are useful when neighborhood reliability is the primary objective. They are often sensitive to initialization and local neighborhood construction policies.

For reliable method comparison, treat initialization as an explicit factor and run controlled seed comparisons. If local metrics improve but global metrics collapse, document that as a task-specific tradeoff rather than a universal method improvement.

## Notable Properties
- Explicit tuning strategy for local structure preservation is a key strength.
- Can outperform global-only stress objectives on local tasks when tuned correctly.

Notable properties should be interpreted as operating characteristics, not guarantees. A property that is beneficial in one data regime can become a liability in another regime with different density, noise level, or manifold complexity.

Use these properties to narrow candidates early, then confirm with metric evidence and task-specific validation. That sequence keeps the workflow grounded in evidence instead of anecdotal method reputation.

## Strengths
This technique is strong for local multidimensional scaling behavior that emphasizes neighborhood-constrained geometry. It can improve local faithfulness compared with global-only MDS formulations.

It is useful when analysts need local-geometric preservation while maintaining an MDS-style optimization perspective.


## Task Alignment
- Inferred alignment: best-aligned tasks
  - Neighborhood identification
  - Outlier identification
  - Cluster identification

Task alignment indicates where this technique is expected to provide the most reliable utility under the current evidence base. Treat non-listed tasks as unsupported until new source-backed evidence is added.

When a project requires multiple task outcomes, combine this section with metric-level alignment and require agreement across both layers. If technique and metric recommendations diverge, collect more evidence before production use.

Operational alignment rule: method alignment should constrain candidate ranking, but final acceptance still requires agreement with task-aligned metric bundles and warning-gate status.

## Known Tradeoffs
- Over-localization may harm global coherence and distance readability.

Tradeoffs are expected and should be made explicit to users before final selection. A method that improves neighborhood fidelity may worsen global distance faithfulness, and vice versa, so optimization must reflect the task hierarchy.

In reporting, document which tradeoffs were accepted and why they were acceptable for the chosen task. This explanation step is part of the contract for trustworthy DR recommendations in this repository.

Communication rule: document one concrete downside that remained after tuning (for example global drift, local fragmentation, or runtime burden) so end users understand residual risk.

## Source Notes
- `papers/notes/zadu-ref-07-local-multidimensional-scaling-for-nonlinear-dimension-reduction-graph-drawing-a.md` (ZR07-E1, ZR07-E2, ZR07-E3, ZR07-E8)

- `papers/notes/pending-ref-019-local-multidimensional-scaling.md` (pending-reference evidence)
- `papers/notes/pending-ref-161-steering-distortions-to-preserve-classes-and-neighbors-in.md` (pending-reference evidence)
