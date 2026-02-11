# LAMP

## Technique Summary
Local Affine Multidimensional Projection using control points and local affine mappings.

In practice, the technique description is intentionally task-centered: the method is not automatically good, and is only appropriate when its distortion profile matches the analytical objective. That framing keeps method choice aligned with user intent instead of popularity.

The summary should be read together with task alignment and tradeoff sections before implementation. When the same dataset supports multiple objectives, this technique may be suitable for one objective and unsuitable for another.

## I/O Contract
- Input: general high-dimensional feature data (labels optional for supervised variants).
- Output: low-dimensional projection coordinates for analysis/visualization.

Input should be treated as a high-dimensional feature representation after data-audit and preprocessing decisions are locked. If normalization, distance definition, or label usage changes during tuning, the effective input contract changes as well and comparisons become noisy.

Output coordinates are analysis artifacts, not ground-truth geometry. They should be consumed according to the declared task, with explicit caution against over-interpreting axes, absolute distances, or visual separations outside the validated use case.

## Core Objective
Produce low-dimensional projection by combining control-point placement with local affine transformations.

The objective function encodes which structural errors are cheap and which are expensive. Understanding that objective is essential because it predicts the kinds of distortions the method will tolerate when perfect preservation is impossible.

Method selection should therefore ask which distortions are acceptable for this task, and which are not. Choose this technique only when its objective-level priorities match that answer.

## Computation Outline
- Select or compute control points and their low-dimensional positions.
- Estimate local affine transforms from control points.
- Project remaining points through local affine mapping and alignment.

Implementation quality depends on stable preprocessing, deterministic settings where possible, and explicit recording of optimization configuration. Most DR pipelines are sensitive to initialization or neighborhood construction choices, so hidden defaults can change conclusions.

For reproducible comparison, evaluate this technique under a fixed protocol and report parameter context with results. This converts the outline from a conceptual recipe into an auditable procedure for downstream agents and reviewers.

Detailed execution rule: treat control-point/landmark selection as a controlled factor and run sensitivity checks across multiple selections. Landmark policy drift can dominate method comparisons.

## Hyperparameter Impact
- Control-point ratio/selection strongly affects quality and runtime.
- Local alignment configuration influences stress and geometry preservation.

Hyperparameters determine the local-vs-global balance, optimization stability, and visual behavior of the embedding. They should be tuned against task-aligned metrics rather than aesthetics alone, especially when outputs influence model or policy decisions.

A practical default is Bayesian optimization with safety checks: fixed seed schedule, bounded search space, and multi-metric objective checks. This reduces manual trial-and-error while preserving traceability for why a specific configuration was selected.

Decision-level tuning rule: optimize both landmark ratio and local fitting settings under the same task reliability check set; report whether conclusions persist across reasonable landmark policies.

## Practical Reliability Notes
LAMP quality depends on control-point design and local affine fitting stability. Poor control-point coverage can create visually plausible but structurally biased embeddings.

In reliable workflows, treat control-point policy as a first-class hyperparameter family. Evaluate sensitivity to control-point count and placement strategy, then report whether conclusions remain stable across reasonable control-point variants.

## Notable Properties
- Practical quality-runtime tradeoff for interactive projection settings.
- Local control offers flexibility beyond global-only mappings.

Notable properties should be interpreted as operating characteristics, not guarantees. A property that is beneficial in one data regime can become a liability in another regime with different density, noise level, or manifold complexity.

Use these properties to narrow candidates early, then confirm with metric evidence and task-specific validation. That sequence keeps the workflow grounded in evidence instead of anecdotal method reputation.

## Strengths
This technique is strong for balancing projection quality and runtime through control-point-driven local affine mapping. It supports interactive or iterative projection workflows where fast updates are valuable.

It is useful when local geometric quality is needed but full global optimization cost is impractical.


## Task Alignment
- Inferred alignment: best-aligned tasks
  - Neighborhood identification
  - Cluster identification
  - Point distance investigation

Task alignment indicates where this technique is expected to provide the most reliable utility under the current evidence base. Treat non-listed tasks as unsupported until new source-backed evidence is added.

When a project requires multiple task outcomes, combine this section with metric-level alignment and require agreement across both layers. If technique and metric recommendations diverge, collect more evidence before production use.

Operational alignment rule: method alignment should constrain candidate ranking, but final acceptance still requires agreement with task-aligned reliability check sets and label-separation check status.

## Known Tradeoffs
- Poor control-point design can degrade both fidelity and stability.

Tradeoffs are expected and should be made explicit to users before final selection. A method that improves neighborhood fidelity may worsen global distance faithfulness, and vice versa, so optimization must reflect the task hierarchy.

In reporting, document which tradeoffs were accepted and why they were acceptable for the chosen task. This explanation step is part of the contract for trustworthy DR recommendations in this guide.

Communication rule: document one concrete downside that remained after tuning (for example global drift, local fragmentation, or runtime burden) so end users understand residual risk.

## Implementation Options
The source literature for this technique is retained, but the default execution path uses a practical fallback implementation because the mapped primary path is not production-ready in Python. Primary status: `risk`. Fallback status: `watch`.

Use the primary path when it is `active` or `watch`. If it is `risk`, execute the fallback path and keep the recommendation confidence conservative.

## Recommended Library
Recommended library: **lsp-python (practical Python fallback)**.

Current maintenance snapshot: **watch** (checked on 2026-02-11). This status is generated from the automated maintenance snapshot using the documented maintenance policy.

## Official API / GitHub / PyPI Links
Primary path links:
- Official API: [https://github.com/gnavvy/Lamp](https://github.com/gnavvy/Lamp)
- GitHub: [https://github.com/gnavvy/Lamp](https://github.com/gnavvy/Lamp)
- PyPI: Not available

Fallback path links:
- Official API: [https://github.com/lvcarx/pyLSP](https://github.com/lvcarx/pyLSP)
- GitHub: [https://github.com/lvcarx/pyLSP](https://github.com/lvcarx/pyLSP)
- PyPI: [https://pypi.org/project/lsp-python/](https://pypi.org/project/lsp-python/)

## Minimal Python API Pattern
```python
from lsp_python.lsp import LSP
idx = np.random.default_rng(7).choice(len(X), size=128, replace=False)
model = LSP()
X_init = model.fit(X[idx])
Z = model.transform(X_init, idx, X)
```

## Key Parameters for Bayesian Optimization
- `control_points`: number of anchor points used to construct the projection.
- `seed`: controls reproducible anchor sampling in Python workflows.

Search bounds used in the minimal snippet:
- `{"control_points": (16, 512)}`

## Initialization in Practice
Anchor/control-point selection acts as the main initialization lever. Keep sampling seed fixed during optimization and compare seed variants afterward.

## Runtime and Memory Notes
Control-point methods are usually faster than full pairwise solvers, but quality depends strongly on anchor representativeness.

## Common Failure Signs and Fixes
- Projection quality swings with anchor samples -> increase control points or stratify anchor selection.
- Local neighborhoods tear around sparse regions -> validate with local reliability checks.
- Very large datasets still slow -> optimize on subset and re-project full data.

## Minimal Runnable Snippet
```python
import numpy as np
from bayes_opt import BayesianOptimization
from zadu import ZADU
from lsp_python.lsp import LSP

X = ...  # shape: (n_samples, n_features)

def zadu_score(hd, ld):
    spec = [{"id": "tnc", "params": {"k": 20}}]
    result = ZADU(spec, hd).measure(ld)[0]
    vals = [float(v) for v in result.values() if isinstance(v, (int, float))]
    return float(np.mean(vals))

def embed(control_points):
    cp = int(max(16, min(len(X) - 1, round(control_points))))
    idx = np.random.default_rng(7).choice(len(X), size=cp, replace=False)
    model = LSP()
    x_init = model.fit(X[idx])
    return model.transform(x_init, idx, X)

def objective(*args, **kwargs):
    z = embed(*args, **kwargs)
    return zadu_score(X, z)

optimizer = BayesianOptimization(f=objective, pbounds={"control_points": (16, 512)}, random_state=7, verbose=0)
optimizer.maximize(init_points=4, n_iter=16)
Z_best = embed(**optimizer.max["params"])
```

## Source Notes
- Local Affine Multidimensional Projection (theory to build accurate local transformations that can be dynamically modiﬁed according to user knowledge. The accuracy et al., IEEE Transactions on Visualization and Computer Graphics, 2011)

- Deep learning multidimensional projections (M. Espadoto et al., Information Visualization, 2020)
