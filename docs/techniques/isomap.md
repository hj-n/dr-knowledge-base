# Isomap

## Technique Summary
Graph-geodesic manifold projection using neighborhood graph shortest-path distances.

In practice, the technique description is intentionally task-centered: the method is not automatically good, and is only appropriate when its distortion profile matches the analytical objective. That framing keeps method choice aligned with user intent instead of popularity.

The summary should be read together with task alignment and tradeoff sections before implementation. When the same dataset supports multiple objectives, this technique may be suitable for one objective and unsuitable for another.

## I/O Contract
- Input: general high-dimensional feature data (labels optional for supervised variants).
- Output: low-dimensional projection coordinates for analysis/visualization.

Input should be treated as a high-dimensional feature representation after data-audit and preprocessing decisions are locked. If normalization, distance definition, or label usage changes during tuning, the effective input contract changes as well and comparisons become noisy.

Output coordinates are analysis artifacts, not ground-truth geometry. They should be consumed according to the declared task, with explicit caution against over-interpreting axes, absolute distances, or visual separations outside the validated use case.

## Core Objective
Preserve manifold geodesic structure in low-dimensional coordinates.

The objective function encodes which structural errors are cheap and which are expensive. Understanding that objective is essential because it predicts the kinds of distortions the method will tolerate when perfect preservation is impossible.

Method selection should therefore ask which distortions are acceptable for this task, and which are not. Choose this technique only when its objective-level priorities match that answer.

## Computation Outline
- Construct neighborhood graph in high-dimensional space.
- Estimate geodesic distances via shortest paths.
- Apply MDS-style embedding on geodesic distance matrix.

Implementation quality depends on stable preprocessing, deterministic settings where possible, and explicit recording of optimization configuration. Most DR pipelines are sensitive to initialization or neighborhood construction choices, so hidden defaults can change conclusions.

For reproducible comparison, evaluate this technique under a fixed protocol and report parameter context with results. This converts the outline from a conceptual recipe into an auditable procedure for downstream agents and reviewers.

Detailed execution rule: evaluate geodesic graph stability (connectivity and shortest-path robustness) before trusting global interpretation. Unstable geodesics produce fragile global claims.

## Hyperparameter Impact
- Neighborhood graph size (`k` or radius) controls connectivity and manifold approximation.
- Distance metric and graph-connectivity handling strongly affect output stability.

Hyperparameters determine the local-vs-global balance, optimization stability, and visual behavior of the embedding. They should be tuned against task-aligned metrics rather than aesthetics alone, especially when outputs influence model or policy decisions.

A practical default is Bayesian optimization with safety checks: fixed seed schedule, bounded search space, and multi-metric objective checks. This reduces manual trial-and-error while preserving traceability for why a specific configuration was selected.

Decision-level tuning rule: report both best score and stability behavior (seed variance / restart variance). A configuration that wins once but is unstable should not be the default recommendation.

## Practical Reliability Notes
Isomap relies on graph geodesics, so neighborhood graph connectivity is a first-order reliability condition. If the graph is fragmented, global geodesic estimates become unstable and downstream projection can create misleading long-range structure.

Before final selection, check graph connectivity diagnostics and sensitivity to neighborhood-size changes. If major topology changes occur across small neighborhood shifts, report reduced confidence for global-distance interpretation.

## Notable Properties
- Can recover global manifold geometry when sampling/connectivity are adequate.
- Sensitive to noise and disconnected graph artifacts.

Notable properties should be interpreted as operating characteristics, not guarantees. A property that is beneficial in one data regime can become a liability in another regime with different density, noise level, or manifold complexity.

Use these properties to narrow candidates early, then confirm with metric evidence and task-specific validation. That sequence keeps the workflow grounded in evidence instead of anecdotal method reputation.

## Strengths
This technique is strong for manifold-geodesic preservation and can reveal global nonlinear geometry beyond linear projections. It is particularly useful when geodesic relationships are important to the analytical question.

It often serves as a global-structure nonlinear baseline when local-neighbor-only methods are insufficient.


## Task Alignment
- Inferred alignment: best-aligned tasks
  - Neighborhood identification
  - Cluster identification
  - Outlier identification

Task alignment indicates where this technique is expected to provide the most reliable utility under the current evidence base. Treat non-listed tasks as unsupported until new source-backed evidence is added.

When a project requires multiple task outcomes, combine this section with metric-level alignment and require agreement across both layers. If technique and metric recommendations diverge, collect more evidence before production use.

Operational alignment rule: method alignment should constrain candidate ranking, but final acceptance still requires agreement with task-aligned reliability check sets and label-separation check status.

## Known Tradeoffs
- Graph construction failure can dominate embedding quality.

Tradeoffs are expected and should be made explicit to users before final selection. A method that improves neighborhood fidelity may worsen global distance faithfulness, and vice versa, so optimization must reflect the task hierarchy.

In reporting, document which tradeoffs were accepted and why they were acceptable for the chosen task. This explanation step is part of the contract for trustworthy DR recommendations in this guide.

Communication rule: document one concrete downside that remained after tuning (for example global drift, local fragmentation, or runtime burden) so end users understand residual risk.

## Implementation Options
The default execution path uses the mapped primary Python implementation for this technique. Implementation mode: `direct`. Primary status: `active`.

Use the primary path when it is `active` or `watch`. If it is `risk`, execute the fallback path and keep the recommendation confidence conservative.

## Recommended Library
Recommended library: **scikit-learn Isomap**.

Current maintenance snapshot: **active** (checked on 2026-02-11). This status is generated from the automated maintenance snapshot using the documented maintenance policy.

## Official API / GitHub / PyPI Links
Primary path links:
- Official API: [https://scikit-learn.org/stable/modules/generated/sklearn.manifold.Isomap.html](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.Isomap.html)
- GitHub: [https://github.com/scikit-learn/scikit-learn](https://github.com/scikit-learn/scikit-learn)
- PyPI: [https://pypi.org/project/scikit-learn/](https://pypi.org/project/scikit-learn/)

Fallback path links:
- Official API: [https://torchdr.github.io/dev/gen_modules/torchdr.UMAP.html](https://torchdr.github.io/dev/gen_modules/torchdr.UMAP.html)
- GitHub: [https://github.com/TorchDR/TorchDR](https://github.com/TorchDR/TorchDR)
- PyPI: [https://pypi.org/project/torchdr/](https://pypi.org/project/torchdr/)

## Minimal Python API Pattern
```python
from sklearn.manifold import Isomap
Z = Isomap(n_neighbors=15, n_components=2).fit_transform(X)
```

## Key Parameters for Bayesian Optimization
- `n_neighbors`: graph connectivity and locality scale.
- `n_components`: output dimensionality.

Search bounds used in the minimal snippet:
- `{"n_neighbors": (5, 80)}`

## Initialization in Practice
Isomap is graph-construction sensitive rather than initialization sensitive. Keep distance metric and preprocessing fixed.

## Runtime and Memory Notes
Graph construction and shortest-path steps dominate runtime. Very sparse neighborhoods can disconnect the graph.

## Common Failure Signs and Fixes
- Disconnected graph warnings -> increase neighbors or review scaling.
- Global geometry looks folded -> adjust neighbor range and inspect geodesic stability.
- Large memory growth -> use smaller candidate subsets for optimization.

## Minimal Runnable Snippet
```python
import numpy as np
from bayes_opt import BayesianOptimization
from zadu import ZADU
from sklearn.manifold import Isomap

X = ...  # shape: (n_samples, n_features)

def zadu_score(hd, ld):
    spec = [{"id": "tnc", "params": {"k": 20}}]
    result = ZADU(spec, hd).measure(ld)[0]
    vals = [float(v) for v in result.values() if isinstance(v, (int, float))]
    return float(np.mean(vals))

def embed(n_neighbors):
    model = Isomap(n_neighbors=int(round(n_neighbors)), n_components=2)
    return model.fit_transform(X)

def objective(*args, **kwargs):
    z = embed(*args, **kwargs)
    return zadu_score(X, z)

optimizer = BayesianOptimization(f=objective, pbounds={"n_neighbors": (5, 80)}, random_state=7, verbose=0)
optimizer.maximize(init_points=4, n_iter=16)
Z_best = embed(**optimizer.max["params"])
```

## Source Notes
- Local multidimensional scaling (Jarkko Venna et al., Neural Networks, 2006)
- Supervised Nonlinear Dimensionality Reduction for Visualization and Classification (X. Geng et al., IEEE Transactions on Systems, Man and Cybernetics, Part B (Cybernetics), 2005)

- Information retrieval perspective to nonlinear dimensionality reduction for data visualization (J. V enna et al., UNKNOWN, 2010)
- Visual Interaction with Dimensionality Reduction: A Structured Literature Analysis (D. Sacha et al, IEEE Transactions on Visualization and Computer Graphics, 2017)
- Local multidimensional scaling (Jarkko Venna and Samuel Kaski, Journal of the American Statistical Association, 2006)
- VisCoDeR: A tool for visually comparing dimensionality reduction algorithms (René Cutura et al., UNKNOWN, 2018)
- Stability Comparison of Dimensionality Reduction Techniques Attending to Data and Parameter Variations (Francisco J. García-Fernández et al., UNKNOWN, 2013)
- Local procrustes for manifold embedding: A measure of embedding quality and embedding algorithms (Y. Goldberg and Y. Ritov, Machine Learning, 2009)
- A behavioral investigation of dimensionality reduction (J. Lewis et al., UNKNOWN, 2012)
- Linear dimensionality reduction: Survey, insights, and generalizations (John P Cunningham and Zoubin Ghahramani, UNKNOWN, 2015)
