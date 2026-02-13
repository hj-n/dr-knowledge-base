# MDS

## Technique Summary
Distance-fitting projection family minimizing stress-type distance distortion objectives.

In practice, the technique description is intentionally task-centered: the method is not automatically good, and is only appropriate when its distortion profile matches the analytical objective. That framing keeps method choice aligned with user intent instead of popularity.

The summary should be read together with task alignment and tradeoff sections before implementation. When the same dataset supports multiple objectives, this technique may be suitable for one objective and unsuitable for another.

## I/O Contract
- Input: general high-dimensional feature data (labels optional for supervised variants).
- Output: low-dimensional projection coordinates for analysis/visualization.

Input should be treated as a high-dimensional feature representation after data-audit and preprocessing decisions are locked. If normalization, distance definition, or label usage changes during tuning, the effective input contract changes as well and comparisons become noisy.

Output coordinates are analysis artifacts, not ground-truth geometry. They should be consumed according to the declared task, with explicit caution against over-interpreting axes, absolute distances, or visual separations outside the validated use case.

## Core Objective
Place points in low-dimensional space such that pairwise distances best match original-space distances.

The objective function encodes which structural errors are cheap and which are expensive. Understanding that objective is essential because it predicts the kinds of distortions the method will tolerate when perfect preservation is impossible.

Method selection should therefore ask which distortions are acceptable for this task, and which are not. Choose this technique only when its objective-level priorities match that answer.

## Computation Outline
- Compute pairwise dissimilarity matrix in original space.
- Choose metric/non-metric stress formulation.
- Optimize low-dimensional coordinates to minimize stress.

Implementation quality depends on stable preprocessing, deterministic settings where possible, and explicit recording of optimization configuration. Most DR pipelines are sensitive to initialization or neighborhood construction choices, so hidden defaults can change conclusions.

For reproducible comparison, evaluate this technique under a fixed protocol and report parameter context with results. This converts the outline from a conceptual recipe into an auditable procedure for downstream agents and reviewers.

Detailed execution rule: run this method under a fixed preprocessing contract and log all stochastic controls (seed, restart index, initialization metadata) so comparison runs are auditable.

## Hyperparameter Impact
- Stress variant and weighting policy change local-vs-global emphasis.
- Initialization and optimization schedule affect convergence and local minima behavior.

Hyperparameters determine the local-vs-global balance, optimization stability, and visual behavior of the embedding. They should be tuned against task-aligned metrics rather than aesthetics alone, especially when outputs influence model or policy decisions.

A practical default is Bayesian optimization with safety checks: fixed seed schedule, bounded search space, and multi-metric objective checks. This reduces manual trial-and-error while preserving traceability for why a specific configuration was selected.

Decision-level tuning rule: report both best score and stability behavior (seed variance / restart variance). A configuration that wins once but is unstable should not be the default recommendation.

## Practical Reliability Notes
MDS variants optimize distance-fitting objectives and therefore can be effective for point-distance and cluster-distance tasks when scale handling is controlled. However, iterative MDS variants can converge to different local minima depending on initialization.

For fair comparisons, run a fixed restart protocol and report best-value plus variability, not only a single best run. If variability is high, avoid using one embedding snapshot as sole evidence for structural claims.

## Notable Properties
- Canonical baseline for global distance-faithfulness tasks.
- Objective is explicit and directly tied to distance distortion.

Notable properties should be interpreted as operating characteristics, not guarantees. A property that is beneficial in one data regime can become a liability in another regime with different density, noise level, or manifold complexity.

Use these properties to narrow candidates early, then confirm with metric evidence and task-specific validation. That sequence keeps the workflow grounded in evidence instead of anecdotal method reputation.

## Strengths
This technique is strong for global distance-structure preservation and is directly aligned with distance-investigation tasks. It is a robust baseline for analyses where pairwise geometry interpretation is central.

It is useful when the objective prioritizes faithful global distance relationships over local cluster aesthetics.


## Task Alignment
- Direct evidence: best-aligned tasks
  - Point distance investigation
  - Class separability investigation
  - Cluster distance investigation
  - Cluster density investigation

Task alignment indicates where this technique is expected to provide the most reliable utility under the current evidence base. Treat non-listed tasks as unsupported until new source-backed evidence is added.

When a project requires multiple task outcomes, combine this section with metric-level alignment and require agreement across both layers. If technique and metric recommendations diverge, collect more evidence before production use.

Operational alignment rule: prioritize for distance and density tasks; for neighborhood-centric tasks use as baseline or safety check, not as sole recommendation evidence.

## Known Tradeoffs
- Stress values can be misread without consistent scale-handling policy.

Tradeoffs are expected and should be made explicit to users before final selection. A method that improves neighborhood fidelity may worsen global distance faithfulness, and vice versa, so optimization must reflect the task hierarchy.

In reporting, document which tradeoffs were accepted and why they were acceptable for the chosen task. This explanation step is part of the contract for trustworthy DR recommendations in this guide.

Communication rule: explain what local structure may be sacrificed to preserve global trends, and confirm this with local metrics before finalization.

## Implementation Options
The default execution path uses the mapped primary Python implementation for this technique. Implementation mode: `direct`. Primary status: `active`.

Use the primary path when it is `active` or `watch`. If it is `risk`, execute the fallback path and keep the recommendation confidence conservative.

## Recommended Library
Recommended library: **scikit-learn MDS**.

Current maintenance snapshot: **active** (checked on 2026-02-11). This status is generated from the automated maintenance snapshot using the documented maintenance policy.

## Official API / GitHub / PyPI Links
Primary path links:
- Official API: [https://scikit-learn.org/stable/modules/generated/sklearn.manifold.MDS.html](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.MDS.html)
- GitHub: [https://github.com/scikit-learn/scikit-learn](https://github.com/scikit-learn/scikit-learn)
- PyPI: [https://pypi.org/project/scikit-learn/](https://pypi.org/project/scikit-learn/)

Fallback path links:
- Official API: [https://torchdr.github.io/dev/gen_modules/torchdr.TSNEkhorn.html](https://torchdr.github.io/dev/gen_modules/torchdr.TSNEkhorn.html)
- GitHub: [https://github.com/TorchDR/TorchDR](https://github.com/TorchDR/TorchDR)
- PyPI: [https://pypi.org/project/torchdr/](https://pypi.org/project/torchdr/)

## Minimal Python API Pattern
```python
from sklearn.manifold import MDS
Z = MDS(n_components=2, n_init=4, max_iter=300, random_state=7).fit_transform(X)
```

## Key Parameters for Bayesian Optimization
- `n_init`: number of restarts for stress minimization stability.
- `max_iter`: optimization budget per restart.

Search bounds used in the minimal snippet:
- `{"n_init": (2, 8), "max_iter": (150, 600)}`

## Initialization in Practice
MDS is restart-sensitive. Keep random state fixed for reproducible comparisons, then validate with multi-seed stress checks.

## Runtime and Memory Notes
Pairwise-distance optimization can be expensive on large datasets. Subsampling during optimization is often necessary.

## Common Failure Signs and Fixes
- Stress does not improve across evaluations -> widen iteration range.
- Embedding changes heavily across runs -> increase restarts and report variability.
- Runtime too high -> optimize on representative subset, then re-fit.

## Minimal Runnable Snippet
```python
import numpy as np
from bayes_opt import BayesianOptimization
from zadu import ZADU
from sklearn.manifold import MDS

X = ...  # shape: (n_samples, n_features)

def zadu_score(hd, ld):
    spec = [{"id": "tnc", "params": {"k": 20}}]
    result = ZADU(spec, hd).measure(ld)[0]
    vals = [float(v) for v in result.values() if isinstance(v, (int, float))]
    return float(np.mean(vals))

def embed(n_init, max_iter):
    model = MDS(n_components=2, n_init=int(round(n_init)), max_iter=int(round(max_iter)), random_state=7)
    return model.fit_transform(X)

def objective(*args, **kwargs):
    z = embed(*args, **kwargs)
    return zadu_score(X, z)

optimizer = BayesianOptimization(f=objective, pbounds={"n_init": (2, 8), "max_iter": (150, 600)}, random_state=7, verbose=0)
optimizer.maximize(init_points=4, n_iter=16)
Z_best = embed(**optimizer.max["params"])
```

## Source Notes
- Stop Misusing t-SNE and UMAP for Visual Analytics (Hyeon Jeon, arXiv, 2025)
- Local Multidimensional Scaling for Nonlinear Dimension Reduction, Graph Drawing, and Proximity Analysis (Lisha Chen et al., Journal of the American Statistical Association, 2009)
- “Normalized Stress” is Not Normalized: How to Interpret Stress Correctly (Kiran Smelser et al., 2024 IEEE Evaluation and Beyond - Methodological Approaches for Visualization (BELIV), 2025)
- Multidimensional Projection for Visual Analytics: Linking Techniques with Distortions, Tasks, and Layout Enrichment (Luis Gustavo Nonato; Michael Aupetit, IEEE Transactions on Visualization and Computer Graphics, 2019)
- Data Visualization by Nonlinear Dimensionality Reduction (Andrej Gisbrecht; Barbara Hammer, WIREs Data Mining and Knowledge Discovery, 2015)

- Empirical Guidance on Scatterplot and Dimension Reduction Technique Choices (M. Sedlmair et al., IEEE Transactions on Visualization and Computer Graphics, 2013)
- Information retrieval perspective to nonlinear dimensionality reduction for data visualization (J. V enna et al., UNKNOWN, 2010)
- High Performance Dimension Reduction and Visualization for Large High-Dimensional Data Analysis (D. Engel et al., 2010 10th IEEE/ACM International Conference on Cluster, Cloud and Grid Computing, 2012)
- Charting a manifold (M. Brand, UNKNOWN, 2002)
- Visual Interaction with Dimensionality Reduction: A Structured Literature Analysis (D. Sacha et al, IEEE Transactions on Visualization and Computer Graphics, 2017)
- Local multidimensional scaling (Jarkko Venna and Samuel Kaski, Journal of the American Statistical Association, 2006)
- VisCoDeR: A tool for visually comparing dimensionality reduction algorithms (René Cutura et al., UNKNOWN, 2018)
- UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction (Leland McInnes et al., Journal of Open Source Software, 2020)
