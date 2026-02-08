# PCA

## Technique Summary
Linear projection using principal axes of maximum variance.

In this repository, the technique description is intentionally task-centered: the method is not automatically good, and is only appropriate when its distortion profile matches the analytical objective. That framing keeps method choice aligned with user intent instead of popularity.

The summary should be read together with task alignment and tradeoff sections before implementation. When the same dataset supports multiple objectives, this technique may be suitable for one objective and unsuitable for another.

## I/O Contract
- Input: general high-dimensional feature data (labels optional for supervised variants).
- Output: low-dimensional projection coordinates for analysis/visualization.

Input should be treated as a high-dimensional feature representation after data-audit and preprocessing decisions are locked. If normalization, distance definition, or label usage changes during tuning, the effective input contract changes as well and comparisons become noisy.

Output coordinates are analysis artifacts, not ground-truth geometry. They should be consumed according to the declared task, with explicit caution against over-interpreting axes, absolute distances, or visual separations outside the validated use case.

## Core Objective
Project data onto orthogonal components capturing maximal variance in descending order.

The objective function encodes which structural errors are cheap and which are expensive. Understanding that objective is essential because it predicts the kinds of distortions the method will tolerate when perfect preservation is impossible.

Method selection should therefore ask which distortions are acceptable for this task, and which are not. Choose this technique only when its objective-level priorities match that answer.

## Computation Outline
- Center (and optionally scale) features.
- Compute covariance matrix (or SVD).
- Select top components and project data onto them.

Implementation quality depends on stable preprocessing, deterministic settings where possible, and explicit recording of optimization configuration. Most DR pipelines are sensitive to initialization or neighborhood construction choices, so hidden defaults can change conclusions.

For reproducible comparison, evaluate this technique under a fixed protocol and report parameter context with results. This converts the outline from a conceptual recipe into an auditable procedure for downstream agents and reviewers.

## Hyperparameter Impact
- Number of components controls information retained and projection granularity.
- Scaling/preprocessing policy materially changes principal directions.

Hyperparameters determine the local-vs-global balance, optimization stability, and visual behavior of the embedding. They should be tuned against task-aligned metrics rather than aesthetics alone, especially when outputs influence model or policy decisions.

A practical default is Bayesian optimization with guardrails: fixed seed schedule, bounded search space, and multi-metric objective checks. This reduces manual trial-and-error while preserving traceability for why a specific configuration was selected.

## Notable Properties
- Fast, stable, and interpretable linear baseline.
- Global variance-oriented; may miss nonlinear manifold structure.

Notable properties should be interpreted as operating characteristics, not guarantees. A property that is beneficial in one data regime can become a liability in another regime with different density, noise level, or manifold complexity.

Use these properties to narrow candidates early, then confirm with metric evidence and task-specific validation. That sequence keeps the workflow grounded in evidence instead of anecdotal method reputation.

## Strengths
This technique is strong as a stable, fast, and interpretable global linear baseline. It is often the first method to test for distance-related and variance-structure tasks.

It is useful for establishing a trustworthy baseline before adopting more complex nonlinear methods.


## Task Alignment
- Direct evidence: best-aligned tasks
  - Point distance investigation
  - Class separability investigation
  - Cluster distance investigation
  - Cluster density investigation

Task alignment indicates where this technique is expected to provide the most reliable utility under the current evidence base. Treat non-listed tasks as unsupported until new source-backed evidence is added.

When a project requires multiple task outcomes, combine this section with metric-level alignment and require agreement across both layers. If technique and metric recommendations diverge, collect more evidence before production use.

## Known Tradeoffs
- Low-dimensional variance capture does not guarantee local neighborhood preservation.

Tradeoffs are expected and should be made explicit to users before final selection. A method that improves neighborhood fidelity may worsen global distance faithfulness, and vice versa, so optimization must reflect the task hierarchy.

In reporting, document which tradeoffs were accepted and why they were acceptable for the chosen task. This explanation step is part of the contract for trustworthy DR recommendations in this repository.

## Source Notes
- `papers/notes/2506.08725v2-stop-misusing-tsne-umap.md` (JEON25-E3, JEON25-E4, JEON25-E5, JEON25-E6)
