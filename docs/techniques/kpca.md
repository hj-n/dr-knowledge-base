# KPCA (Kernel PCA)

## Technique Summary
Kernelized PCA projection for nonlinear structure capture via implicit feature space.

In this repository, the technique description is intentionally task-centered: the method is not automatically good, and is only appropriate when its distortion profile matches the analytical objective. That framing keeps method choice aligned with user intent instead of popularity.

The summary should be read together with task alignment and tradeoff sections before implementation. When the same dataset supports multiple objectives, this technique may be suitable for one objective and unsuitable for another.

## I/O Contract
- Input: general high-dimensional feature data (labels optional for supervised variants).
- Output: low-dimensional projection coordinates for analysis/visualization.

Input should be treated as a high-dimensional feature representation after data-audit and preprocessing decisions are locked. If normalization, distance definition, or label usage changes during tuning, the effective input contract changes as well and comparisons become noisy.

Output coordinates are analysis artifacts, not ground-truth geometry. They should be consumed according to the declared task, with explicit caution against over-interpreting axes, absolute distances, or visual separations outside the validated use case.

## Core Objective
Perform linear projection in kernel-induced feature space to obtain nonlinear low-dimensional projections.

The objective function encodes which structural errors are cheap and which are expensive. Understanding that objective is essential because it predicts the kinds of distortions the method will tolerate when perfect preservation is impossible.

Method selection should therefore ask which distortions are acceptable for this task, and which are not. Choose this technique only when its objective-level priorities match that answer.

## Computation Outline
- Choose kernel function and kernel parameters.
- Compute centered kernel matrix.
- Eigen-decompose kernel matrix and project onto leading components.

Implementation quality depends on stable preprocessing, deterministic settings where possible, and explicit recording of optimization configuration. Most DR pipelines are sensitive to initialization or neighborhood construction choices, so hidden defaults can change conclusions.

For reproducible comparison, evaluate this technique under a fixed protocol and report parameter context with results. This converts the outline from a conceptual recipe into an auditable procedure for downstream agents and reviewers.

Detailed execution rule: run this method under a fixed preprocessing contract and log all stochastic controls (seed, restart index, initialization metadata) so comparison runs are auditable.

## Hyperparameter Impact
- Kernel type/parameters determine geometry of captured nonlinear structure.
- Number of components controls information retained in projection.

Hyperparameters determine the local-vs-global balance, optimization stability, and visual behavior of the embedding. They should be tuned against task-aligned metrics rather than aesthetics alone, especially when outputs influence model or policy decisions.

A practical default is Bayesian optimization with safety checks: fixed seed schedule, bounded search space, and multi-metric objective checks. This reduces manual trial-and-error while preserving traceability for why a specific configuration was selected.

Decision-level tuning rule: kernel family and kernel scale are first-order assumptions, not minor tweaks. Log chosen kernel rationale and compare against linear/global baselines under the same protocol.

## Practical Reliability Notes
Kernel PCA depends heavily on kernel choice and kernel scale. Different kernel settings represent different geometry assumptions; method comparison is invalid if kernel policy is not controlled.

Use KPCA when nonlinear global structure is plausible and kernel assumptions are justified by the task. Always compare against linear PCA and at least one neighborhood-focused method to verify whether kernel-induced gains are truly task-relevant.

## Notable Properties
- Can represent nonlinear structure with linear algebra pipeline in kernel space.
- Interpretability depends on kernel choice.

Notable properties should be interpreted as operating characteristics, not guarantees. A property that is beneficial in one data regime can become a liability in another regime with different density, noise level, or manifold complexity.

Use these properties to narrow candidates early, then confirm with metric evidence and task-specific validation. That sequence keeps the workflow grounded in evidence instead of anecdotal method reputation.

## Strengths
This technique is strong for capturing nonlinear variance structure through kernel mappings while keeping a PCA-like framework. It is useful when linear PCA underfits curvature or nonlinear separability patterns.

It can provide a practical nonlinear global representation with familiar component-style interpretation workflow.


## Task Alignment
- Inferred alignment: best-aligned tasks
  - Neighborhood identification
  - Cluster identification
  - Point distance investigation

Task alignment indicates where this technique is expected to provide the most reliable utility under the current evidence base. Treat non-listed tasks as unsupported until new source-backed evidence is added.

When a project requires multiple task outcomes, combine this section with metric-level alignment and require agreement across both layers. If technique and metric recommendations diverge, collect more evidence before production use.

Operational alignment rule: method alignment should constrain candidate ranking, but final acceptance still requires agreement with task-aligned reliability check sets and label-separation check status.

## Known Tradeoffs
- Kernel tuning is critical and may be unstable without validation metrics.

Tradeoffs are expected and should be made explicit to users before final selection. A method that improves neighborhood fidelity may worsen global distance faithfulness, and vice versa, so optimization must reflect the task hierarchy.

In reporting, document which tradeoffs were accepted and why they were acceptable for the chosen task. This explanation step is part of the contract for trustworthy DR recommendations in this repository.

Communication rule: document one concrete downside that remained after tuning (for example global drift, local fragmentation, or runtime burden) so end users understand residual risk.

## Source Notes
- `papers/notes/zadu-ref-07-local-multidimensional-scaling-for-nonlinear-dimension-reduction-graph-drawing-a.md` (ZR07-E4)

- `papers/notes/pending-ref-031-interactive-visual-cluster-analysis-by-contrastive-dimensi.md` (pending-reference evidence)
- `papers/notes/pending-ref-048-linear-dimensionality-reduction-survey-insights-and-genera.md` (pending-reference evidence)
- `papers/notes/pending-ref-089-a-new-method-of-generalizing-sammon-mapping-with-applicati.md` (pending-reference evidence)
- `papers/notes/pending-ref-108-dimred-and-coranking-unifying-dimensionality-reduction-in.md` (pending-reference evidence)
- `papers/notes/pending-extra-weinberger05a-weinberger05a.md` (pending-reference evidence)
