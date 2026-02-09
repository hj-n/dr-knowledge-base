# ClassiMap

## Technique Summary
Class-aware projection method with stress optimization that penalizes false/missed neighbors using labels.

In this repository, the technique description is intentionally task-centered: the method is not automatically good, and is only appropriate when its distortion profile matches the analytical objective. That framing keeps method choice aligned with user intent instead of popularity.

The summary should be read together with task alignment and tradeoff sections before implementation. When the same dataset supports multiple objectives, this technique may be suitable for one objective and unsuitable for another.

## I/O Contract
- Input: general high-dimensional feature data (labels optional for supervised variants).
- Output: low-dimensional projection coordinates for analysis/visualization.

Input should be treated as a high-dimensional feature representation after data-audit and preprocessing decisions are locked. If normalization, distance definition, or label usage changes during tuning, the effective input contract changes as well and comparisons become noisy.

Output coordinates are analysis artifacts, not ground-truth geometry. They should be consumed according to the declared task, with explicit caution against over-interpreting axes, absolute distances, or visual separations outside the validated use case.

## Core Objective
Produce an embedding that preserves neighborhood structure while prioritizing class-aware distortion control.

The objective function encodes which structural errors are cheap and which are expensive. Understanding that objective is essential because it predicts the kinds of distortions the method will tolerate when perfect preservation is impossible.

Method selection should therefore ask which distortions are acceptable for this task, and which are not. Choose this technique only when its objective-level priorities match that answer.

## Computation Outline
- Define class-aware stress penalties for false and missed neighbors.
- Optimize embedding coordinates under this class-aware stress.
- Inspect class-separation and neighborhood-faithfulness jointly.

Implementation quality depends on stable preprocessing, deterministic settings where possible, and explicit recording of optimization configuration. Most DR pipelines are sensitive to initialization or neighborhood construction choices, so hidden defaults can change conclusions.

For reproducible comparison, evaluate this technique under a fixed protocol and report parameter context with results. This converts the outline from a conceptual recipe into an auditable procedure for downstream agents and reviewers.

Detailed execution rule: keep label policy fixed and record how missing/noisy labels were handled. Supervised local methods can shift behavior dramatically with label cleaning choices.

## Hyperparameter Impact
- Penalty weighting between false and missed neighbors changes class-preservation behavior.
- Neighborhood scale influences which class-structure errors dominate.

Hyperparameters determine the local-vs-global balance, optimization stability, and visual behavior of the embedding. They should be tuned against task-aligned metrics rather than aesthetics alone, especially when outputs influence model or policy decisions.

A practical default is Bayesian optimization with safety checks: fixed seed schedule, bounded search space, and multi-metric objective checks. This reduces manual trial-and-error while preserving traceability for why a specific configuration was selected.

Decision-level tuning rule: report both best score and stability behavior (seed variance / restart variance). A configuration that wins once but is unstable should not be the default recommendation.

## Practical Reliability Notes
ClassiMap uses label information to influence projection structure, typically improving class-separation readability when labels are coherent. It can be effective for class-focused exploratory analysis and annotation review workflows.

As with other supervised projections, do not generalize class-oriented gains to unrelated tasks such as faithful global distance investigation. Keep task declaration explicit and pair ClassiMap with non-label metrics when reporting final recommendations.

## Notable Properties
- Can expose class-structure distortions more directly than label-agnostic stress.
- Label quality directly impacts interpretability.

Notable properties should be interpreted as operating characteristics, not guarantees. A property that is beneficial in one data regime can become a liability in another regime with different density, noise level, or manifold complexity.

Use these properties to narrow candidates early, then confirm with metric evidence and task-specific validation. That sequence keeps the workflow grounded in evidence instead of anecdotal method reputation.

## Strengths
This technique is strong for class-aware distance and neighborhood organization, especially when class labels should influence map layout. It can make class-structured patterns clearer than class-agnostic projections in supervised exploration.

It is useful when class-sensitive embedding behavior is required and label assumptions are explicitly validated.


## Task Alignment
- Inferred alignment: best-aligned tasks
  - Class separability investigation
  - Cluster identification

Task alignment indicates where this technique is expected to provide the most reliable utility under the current evidence base. Treat non-listed tasks as unsupported until new source-backed evidence is added.

When a project requires multiple task outcomes, combine this section with metric-level alignment and require agreement across both layers. If technique and metric recommendations diverge, collect more evidence before production use.

Operational alignment rule: use as primary candidates only for class-separability-oriented tasks; for non-class tasks, keep these methods as optional comparisons and require label-agnostic corroboration.

## Known Tradeoffs
- Not appropriate when label assumptions are weak or unavailable.

Tradeoffs are expected and should be made explicit to users before final selection. A method that improves neighborhood fidelity may worsen global distance faithfulness, and vice versa, so optimization must reflect the task hierarchy.

In reporting, document which tradeoffs were accepted and why they were acceptable for the chosen task. This explanation step is part of the contract for trustworthy DR recommendations in this repository.

Communication rule: document one concrete downside that remained after tuning (for example global drift, local fragmentation, or runtime burden) so end users understand residual risk.

## Source Notes
- `papers/notes/zadu-ref-14-ref06-steering-distortions-to-preserve-classes-and-neighbors-in-supervised-dimen.md` (ZR14-E7, ZR14-E8)

- `papers/notes/pending-ref-044-classimap-a-new-dimension-reduction-technique-for-explorat.md` (pending-reference evidence)
- `papers/notes/pending-ref-161-steering-distortions-to-preserve-classes-and-neighbors-in.md` (pending-reference evidence)
