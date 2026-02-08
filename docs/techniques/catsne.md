# catSNE

## Technique Summary
Class-aware t-SNE variant that adapts neighborhood behavior using class distribution information.

In this repository, the technique description is intentionally task-centered: the method is not automatically good, and is only appropriate when its distortion profile matches the analytical objective. That framing keeps method choice aligned with user intent instead of popularity.

The summary should be read together with task alignment and tradeoff sections before implementation. When the same dataset supports multiple objectives, this technique may be suitable for one objective and unsuitable for another.

## I/O Contract
- Input: general high-dimensional feature data (labels optional for supervised variants).
- Output: low-dimensional projection coordinates for analysis/visualization.

Input should be treated as a high-dimensional feature representation after data-audit and preprocessing decisions are locked. If normalization, distance definition, or label usage changes during tuning, the effective input contract changes as well and comparisons become noisy.

Output coordinates are analysis artifacts, not ground-truth geometry. They should be consumed according to the declared task, with explicit caution against over-interpreting axes, absolute distances, or visual separations outside the validated use case.

## Core Objective
Preserve local neighborhood structure while explicitly prioritizing class-aware neighborhood consistency.

The objective function encodes which structural errors are cheap and which are expensive. Understanding that objective is essential because it predicts the kinds of distortions the method will tolerate when perfect preservation is impossible.

Method selection should therefore ask which distortions are acceptable for this task, and which are not. Choose this technique only when its objective-level priorities match that answer.

## Computation Outline
- Build class-aware neighborhood probability or weighting scheme.
- Run t-SNE-like optimization with class-aware local adaptation.
- Output low-dimensional coordinates balancing neighborhood fidelity and class-aware behavior.

Implementation quality depends on stable preprocessing, deterministic settings where possible, and explicit recording of optimization configuration. Most DR pipelines are sensitive to initialization or neighborhood construction choices, so hidden defaults can change conclusions.

For reproducible comparison, evaluate this technique under a fixed protocol and report parameter context with results. This converts the outline from a conceptual recipe into an auditable procedure for downstream agents and reviewers.

## Hyperparameter Impact
- Neighborhood-size adaptation policy controls class-locality emphasis.
- Optimization schedule still inherits t-SNE-style sensitivity (learning rate / iterations).

Hyperparameters determine the local-vs-global balance, optimization stability, and visual behavior of the embedding. They should be tuned against task-aligned metrics rather than aesthetics alone, especially when outputs influence model or policy decisions.

A practical default is Bayesian optimization with guardrails: fixed seed schedule, bounded search space, and multi-metric objective checks. This reduces manual trial-and-error while preserving traceability for why a specific configuration was selected.

## Notable Properties
- Useful when class-aware local structure is part of the analysis objective.
- Can overfit label assumptions when labels are noisy or weakly separated.

Notable properties should be interpreted as operating characteristics, not guarantees. A property that is beneficial in one data regime can become a liability in another regime with different density, noise level, or manifold complexity.

Use these properties to narrow candidates early, then confirm with metric evidence and task-specific validation. That sequence keeps the workflow grounded in evidence instead of anecdotal method reputation.

## Strengths
This technique is strong for class-aware local-neighborhood structure preservation in supervised contexts. It can provide better class-discriminative local organization than purely unsupervised neighborhood embeddings when labels are informative.

It is useful when analysts need local-structure fidelity while explicitly preserving class-relevant neighborhood behavior.


## Task Alignment
- Inferred alignment: best-aligned tasks
  - Class separability investigation
  - Cluster identification

Task alignment indicates where this technique is expected to provide the most reliable utility under the current evidence base. Treat non-listed tasks as unsupported until new source-backed evidence is added.

When a project requires multiple task outcomes, combine this section with metric-level alignment and require agreement across both layers. If technique and metric recommendations diverge, collect more evidence before production use.

## Known Tradeoffs
- Should be paired with label-agnostic metrics to avoid one-sided conclusions.

Tradeoffs are expected and should be made explicit to users before final selection. A method that improves neighborhood fidelity may worsen global distance faithfulness, and vice versa, so optimization must reflect the task hierarchy.

In reporting, document which tradeoffs were accepted and why they were acceptable for the chosen task. This explanation step is part of the contract for trustworthy DR recommendations in this repository.

## Source Notes
- `papers/notes/zadu-ref-14-ref06-steering-distortions-to-preserve-classes-and-neighbors-in-supervised-dimen.md` (ZR14-E6)
