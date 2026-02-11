# CCA (Curvilinear Components Analysis)

## Technique Summary
Nonlinear projection with explicit trustworthiness-continuity compromise control.

In practice, the technique description is intentionally task-centered: the method is not automatically good, and is only appropriate when its distortion profile matches the analytical objective. That framing keeps method choice aligned with user intent instead of popularity.

The summary should be read together with task alignment and tradeoff sections before implementation. When the same dataset supports multiple objectives, this technique may be suitable for one objective and unsuitable for another.

## I/O Contract
- Input: general high-dimensional feature data (labels optional for supervised variants).
- Output: low-dimensional projection coordinates for analysis/visualization.

Input should be treated as a high-dimensional feature representation after data-audit and preprocessing decisions are locked. If normalization, distance definition, or label usage changes during tuning, the effective input contract changes as well and comparisons become noisy.

Output coordinates are analysis artifacts, not ground-truth geometry. They should be consumed according to the declared task, with explicit caution against over-interpreting axes, absolute distances, or visual separations outside the validated use case.

## Core Objective
Map high-dimensional data to low-dimensional coordinates while controlling local neighborhood distortions via a compromise parameter.

The objective function encodes which structural errors are cheap and which are expensive. Understanding that objective is essential because it predicts the kinds of distortions the method will tolerate when perfect preservation is impossible.

Method selection should therefore ask which distortions are acceptable for this task, and which are not. Choose this technique only when its objective-level priorities match that answer.

## Computation Outline
- Define neighborhood-driven objective with trustworthiness/continuity tradeoff.
- Optimize projection coordinates to reduce objective error.
- Evaluate neighborhood preservation over selected neighborhood scales.

Implementation quality depends on stable preprocessing, deterministic settings where possible, and explicit recording of optimization configuration. Most DR pipelines are sensitive to initialization or neighborhood construction choices, so hidden defaults can change conclusions.

For reproducible comparison, evaluate this technique under a fixed protocol and report parameter context with results. This converts the outline from a conceptual recipe into an auditable procedure for downstream agents and reviewers.

Detailed execution rule: run multiple seeds under the same initialization mode and compare structural consistency before accepting conclusions. For local stochastic methods, a single visually appealing run is not sufficient evidence.

## Hyperparameter Impact
- Compromise parameter directly controls trustworthiness vs continuity emphasis.
- Neighborhood definition controls locality scale of preserved structure.

Hyperparameters determine the local-vs-global balance, optimization stability, and visual behavior of the embedding. They should be tuned against task-aligned metrics rather than aesthetics alone, especially when outputs influence model or policy decisions.

A practical default is Bayesian optimization with safety checks: fixed seed schedule, bounded search space, and multi-metric objective checks. This reduces manual trial-and-error while preserving traceability for why a specific configuration was selected.

Decision-level tuning rule: tune local-scale controls and optimization controls jointly, then verify that gains remain under seed perturbation. If seed sensitivity is high, downgrade confidence and keep fallback candidates.

## Practical Reliability Notes
CCA-family nonlinear mapping can be effective for preserving local continuity patterns, but it is sensitive to neighborhood and optimization settings. Treat it as a candidate requiring explicit local-scale validation rather than a default baseline.

For reliable use, report neighborhood policy and convergence behavior. If CCA performs well only in narrow parameter windows, prefer methods with broader stability unless the task strongly benefits from CCA-specific behavior.

## Notable Properties
- Explicit control of local distortion tradeoff is a notable strength.
- Different compromise settings may suit different analysis tasks.

Notable properties should be interpreted as operating characteristics, not guarantees. A property that is beneficial in one data regime can become a liability in another regime with different density, noise level, or manifold complexity.

Use these properties to narrow candidates early, then confirm with metric evidence and task-specific validation. That sequence keeps the workflow grounded in evidence instead of anecdotal method reputation.

## Strengths
This technique is strong for preserving correlation structure between paired views and extracting shared low-dimensional representations. It is useful when cross-view relationships are central to interpretation.

It can improve interpretability in multi-view settings by emphasizing components that explain shared variance across aligned feature spaces.


## Task Alignment
- Inferred alignment: best-aligned tasks
  - Neighborhood identification
  - Outlier identification
  - Cluster identification

Task alignment indicates where this technique is expected to provide the most reliable utility under the current evidence base. Treat non-listed tasks as unsupported until new source-backed evidence is added.

When a project requires multiple task outcomes, combine this section with metric-level alignment and require agreement across both layers. If technique and metric recommendations diverge, collect more evidence before production use.

Operational alignment rule: method alignment should constrain candidate ranking, but final acceptance still requires agreement with task-aligned reliability check sets and label-separation check status.

## Known Tradeoffs
- One fixed parameter setting rarely fits all analytical goals.

Tradeoffs are expected and should be made explicit to users before final selection. A method that improves neighborhood fidelity may worsen global distance faithfulness, and vice versa, so optimization must reflect the task hierarchy.

In reporting, document which tradeoffs were accepted and why they were acceptable for the chosen task. This explanation step is part of the contract for trustworthy DR recommendations in this guide.

Communication rule: document one concrete downside that remained after tuning (for example global drift, local fragmentation, or runtime burden) so end users understand residual risk.

## Implementation Options
The default execution path uses the mapped primary Python implementation for this technique. Implementation mode: `direct`. Primary status: `active`.

Use the primary path when it is `active` or `watch`. If it is `risk`, execute the fallback path and keep the recommendation confidence conservative.

## Recommended Library
Recommended library: **scikit-learn CCA**.

Current maintenance snapshot: **active** (checked on 2026-02-11). This status is generated from the automated maintenance snapshot using the documented maintenance policy.

## Official API / GitHub / PyPI Links
Primary path links:
- Official API: [https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.CCA.html](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.CCA.html)
- GitHub: [https://github.com/scikit-learn/scikit-learn](https://github.com/scikit-learn/scikit-learn)
- PyPI: [https://pypi.org/project/scikit-learn/](https://pypi.org/project/scikit-learn/)

Fallback path links:
- Official API: [https://torchdr.github.io/dev/gen_modules/torchdr.PCA.html](https://torchdr.github.io/dev/gen_modules/torchdr.PCA.html)
- GitHub: [https://github.com/TorchDR/TorchDR](https://github.com/TorchDR/TorchDR)
- PyPI: [https://pypi.org/project/torchdr/](https://pypi.org/project/torchdr/)

## Minimal Python API Pattern
```python
from sklearn.cross_decomposition import CCA
X_left, X_right = np.split(X, 2, axis=1)
Z, _ = CCA(n_components=2).fit_transform(X_left, X_right)
```

## Key Parameters for Bayesian Optimization
- `n_components`: number of canonical dimensions to keep.
- `max_iter`: convergence budget for iterative solver.

Search bounds used in the minimal snippet:
- `{"n_components": (1, 10)}`

## Initialization in Practice
CCA is deterministic under fixed preprocessing and fixed view split. Keep view construction fixed before optimization.

## Runtime and Memory Notes
Runtime is moderate for dense matrices. The main risk is unstable results when view split or scaling changes.

## Common Failure Signs and Fixes
- Odd feature counts break naive view split -> define views explicitly.
- Convergence warnings -> increase `max_iter` and standardize both views.
- Low canonical correlation -> CCA may not be the right DR path for this task.

## Minimal Runnable Snippet
```python
import numpy as np
from bayes_opt import BayesianOptimization
from zadu import ZADU
from sklearn.cross_decomposition import CCA

X = ...  # shape: (n_samples, n_features)
X = X[:, : (X.shape[1] // 2) * 2]  # CCA needs two aligned views

def zadu_score(hd, ld):
    spec = [{"id": "tnc", "params": {"k": 20}}]
    result = ZADU(spec, hd).measure(ld)[0]
    vals = [float(v) for v in result.values() if isinstance(v, (int, float))]
    return float(np.mean(vals))

def embed(n_components):
    x_left, x_right = np.split(X, 2, axis=1)
    z, _ = CCA(n_components=int(round(n_components)), max_iter=500).fit_transform(x_left, x_right)
    return z[:, :2]

def objective(n_components):
    z = embed(n_components)
    x_left, _ = np.split(X, 2, axis=1)
    return zadu_score(x_left, z)

optimizer = BayesianOptimization(f=objective, pbounds={"n_components": (1, 10)}, random_state=7, verbose=0)
optimizer.maximize(init_points=4, n_iter=16)
Z_best = embed(**optimizer.max["params"])
```

## Source Notes
- Local multidimensional scaling (Jarkko Venna et al., Neural Networks, 2006)

- Linear dimensionality reduction: Survey, insights, and generalizations (John P Cunningham and Zoubin Ghahramani, UNKNOWN, 2015)
- A methodology to compare Dimensionality Reduction algorithms in terms of loss of quality (A. Gracia et al., Information Sciences, 2014)
- Sanity check for class-coloring-based evaluation of dimension reduction techniques (Michaël Aupetit, Proceedings of the Fifth Workshop on Beyond Time and Errors: Novel Evaluation Methods for Visualization, 2014)
