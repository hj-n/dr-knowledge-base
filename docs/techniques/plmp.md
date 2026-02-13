# PLMP

## Technique Summary
Linear mapping projection baseline emphasizing computational efficiency.

In practice, the technique description is intentionally task-centered: the method is not automatically good, and is only appropriate when its distortion profile matches the analytical objective. That framing keeps method choice aligned with user intent instead of popularity.

The summary should be read together with task alignment and tradeoff sections before implementation. When the same dataset supports multiple objectives, this technique may be suitable for one objective and unsuitable for another.

## I/O Contract
- Input: general high-dimensional feature data (labels optional for supervised variants).
- Output: low-dimensional projection coordinates for analysis/visualization.

Input should be treated as a high-dimensional feature representation after data-audit and preprocessing decisions are locked. If normalization, distance definition, or label usage changes during tuning, the effective input contract changes as well and comparisons become noisy.

Output coordinates are analysis artifacts, not ground-truth geometry. They should be consumed according to the declared task, with explicit caution against over-interpreting axes, absolute distances, or visual separations outside the validated use case.

## Core Objective
Produce low-dimensional mapping with lightweight linear transformation setup.

The objective function encodes which structural errors are cheap and which are expensive. Understanding that objective is essential because it predicts the kinds of distortions the method will tolerate when perfect preservation is impossible.

Method selection should therefore ask which distortions are acceptable for this task, and which are not. Choose this technique only when its objective-level priorities match that answer.

## Computation Outline
- Construct mapping from selected samples/control points.
- Solve linear mapping parameters.
- Project remaining data through learned linear map.

Implementation quality depends on stable preprocessing, deterministic settings where possible, and explicit recording of optimization configuration. Most DR pipelines are sensitive to initialization or neighborhood construction choices, so hidden defaults can change conclusions.

For reproducible comparison, evaluate this technique under a fixed protocol and report parameter context with results. This converts the outline from a conceptual recipe into an auditable procedure for downstream agents and reviewers.

Detailed execution rule: verify graph connectivity and neighborhood-policy stability before interpreting results. Graph fragmentation or unstable connectivity can invalidate downstream interpretation.

## Hyperparameter Impact
- Sample/control-point selection influences quality-runtime balance.
- Regularization/mapping constraints affect stability.

Hyperparameters determine the local-vs-global balance, optimization stability, and visual behavior of the embedding. They should be tuned against task-aligned metrics rather than aesthetics alone, especially when outputs influence model or policy decisions.

A practical default is Bayesian optimization with safety checks: fixed seed schedule, bounded search space, and multi-metric objective checks. This reduces manual trial-and-error while preserving traceability for why a specific configuration was selected.

Decision-level tuning rule: report both best score and stability behavior (seed variance / restart variance). A configuration that wins once but is unstable should not be the default recommendation.

## Practical Reliability Notes
PLMP methods can provide efficient local projection behavior for exploratory analysis, but they inherit sensitivity from piecewise graph/local model choices. Reliability depends on stable local partitioning and consistent preprocessing.

Use PLMP with fixed protocol comparisons and explicit sensitivity checks over partition/graph settings. If small setting changes cause large structural differences, do not over-commit to PLMP for high-stakes interpretation tasks.

## Notable Properties
- Useful baseline for efficiency-focused comparisons.
- Lower flexibility than richer local nonlinear mappings.

Notable properties should be interpreted as operating characteristics, not guarantees. A property that is beneficial in one data regime can become a liability in another regime with different density, noise level, or manifold complexity.

Use these properties to narrow candidates early, then confirm with metric evidence and task-specific validation. That sequence keeps the workflow grounded in evidence instead of anecdotal method reputation.

## Strengths
This technique is strong for linear-map-style projection with low computational overhead. It is useful for large-scale settings where fast approximation of projection behavior is needed.

It can be practical when repeated projection updates are required under runtime constraints.


## Task Alignment
- Inferred alignment: best-aligned tasks
  - Point distance investigation
  - Cluster identification

Task alignment indicates where this technique is expected to provide the most reliable utility under the current evidence base. Treat non-listed tasks as unsupported until new source-backed evidence is added.

When a project requires multiple task outcomes, combine this section with metric-level alignment and require agreement across both layers. If technique and metric recommendations diverge, collect more evidence before production use.

Operational alignment rule: method alignment should constrain candidate ranking, but final acceptance still requires agreement with task-aligned reliability check sets and label-separation check status.

## Known Tradeoffs
- Efficiency gains can reduce local-structure fidelity.

Tradeoffs are expected and should be made explicit to users before final selection. A method that improves neighborhood fidelity may worsen global distance faithfulness, and vice versa, so optimization must reflect the task hierarchy.

In reporting, document which tradeoffs were accepted and why they were acceptable for the chosen task. This explanation step is part of the contract for trustworthy DR recommendations in this guide.

Communication rule: explicitly state graph-dependence risk. If results change under small graph-parameter shifts, present that instability as residual uncertainty.

## Implementation Options
The source literature for this technique is retained, but the default execution path uses a practical fallback implementation because the mapped primary path is not production-ready in Python. Primary status: `risk`. Fallback status: `watch`.

Use the primary path when it is `active` or `watch`. If it is `risk`, execute the fallback path and keep the recommendation confidence conservative.

## Recommended Library
Recommended library: **lsp-python (practical Python fallback)**.

Current maintenance snapshot: **watch** (checked on 2026-02-11). This status is generated from the automated maintenance snapshot using the documented maintenance policy.

## Official API / GitHub / PyPI Links
Primary path links:
- Official API: Not available
- GitHub: Not available
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
- Local Affine Multidimensional Projection (Paulo Joia, Fernando V. Paulovich, Danilo Coimbra, Jose Alberto Cuminato, Luis Gustavo Nonato, IEEE Transactions on Visualization and Computer Graphics, 2011)

- High Performance Dimension Reduction and Visualization for Large High-Dimensional Data Analysis (D. Engel et al., 2010 10th IEEE/ACM International Conference on Cluster, Cloud and Grid Computing, 2012)
- Piecewise laplacian-based projection for interactive data exploration and organization (F. V. Paulovich et al., Information, 2011)
- Explaining three-dimensional dimensionality reduction plots (Danilo B. Coimbra et al., Information Visualization, 2016)
