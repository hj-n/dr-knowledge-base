# TriMap

## Technique Summary
TriMap is a triplet-based dimensionality-reduction method that emphasizes global structure while keeping local neighborhoods usable.

The core idea is to preserve relative ordering constraints of the form "point *i* should be closer to *j* than to *k*". This makes TriMap a practical option when users care about inter-cluster layout and large-scale structure, not only local cluster compactness.

## I/O Contract
- Input: high-dimensional feature matrix `X` with shape `(n_samples, n_features)`.
- Output: low-dimensional projection `Z` with shape `(n_samples, n_components)`, usually 2D for visual analytics.

TriMap can also use a precomputed distance matrix or precomputed nearest-neighbor tuples. For reliable comparisons, keep preprocessing and distance settings fixed across all candidate methods.

## Core Objective
TriMap optimizes a weighted triplet objective so that informative triplet constraints from the original space are respected in the embedding.

Compared with methods that mostly optimize local neighborhoods, TriMap is designed to keep global arrangement more interpretable. This is useful for tasks where cluster-to-cluster spacing and coarse manifold organization matter.

## Computation Outline
TriMap builds triplets from nearest neighbors, outliers, and random samples, assigns weights, and optimizes embedding coordinates to satisfy these constraints.

In practice, initialization and triplet sampling hyperparameters strongly affect behavior. A stable run therefore needs explicit initialization choice, bounded parameter search, and repeated-seed checks for the top candidates.

## Hyperparameter Impact
`n_inliers`, `n_outliers`, and `n_random` define how triplets are sampled and how much local versus broader structure is emphasized. `weight_temp` changes embedding compactness by reshaping triplet weights.

Optimization settings such as `lr` and `n_iters` affect convergence quality and runtime. For production recommendations, tune triplet-sampling and optimization settings jointly using Bayesian optimization, then validate the selected configuration across repeated seeds.

## Practical Reliability Notes
TriMap is a strong candidate when the user explicitly wants a faithful global layout, but it should still be evaluated with both local and global reliability checks. Over-optimizing for global layout can hide local distortions.

Use fixed preprocessing, fixed initialization policy, and a repeated-seed protocol. If top configurations change frequently across seeds, keep confidence conservative and include a fallback method.

## Notable Properties
TriMap is often effective for preserving global relationships, including cluster ordering and large-scale manifold arrangement. It is also designed to scale to large datasets.

Its triplet-based design gives a different distortion profile than neighborhood-only objectives. That difference is useful for comparative runs when decisions depend on global structure.

## Strengths
TriMap provides a practical global-structure-oriented nonlinear baseline with a Python API close to familiar `fit_transform` workflows.

It is particularly useful for point-distance, cluster-distance, and cluster-density investigations where global arrangement fidelity is part of the user goal.

## Task Alignment
- Direct evidence: Point distance investigation
- Direct evidence: Cluster distance investigation
- Inferred alignment: Cluster density investigation

TriMap paper evidence and follow-up empirical studies both emphasize global structure preservation. That maps directly to global-layout tasks in this KB.

## Known Tradeoffs
Triplet sampling and optimization can increase runtime on large datasets, and poor sampling settings may hurt local readability. Parameter tuning is not optional for reliable deployment.

TriMap may not be the best single method for purely local-neighborhood tasks. In those cases, compare it against local-first methods and use task-aligned reliability checks before final selection.

## Implementation Options
The default path is the official Python `trimap` package and reference repository.

If TriMap fails operational constraints (runtime/memory/stability), use a global-structure fallback such as Isomap under the same preprocessing and tuning protocol.

## Recommended Library
Recommended library: **trimap** (Python package from `eamid/trimap`).

## Official API / GitHub / PyPI Links
Primary path links:
- Official API: [https://github.com/eamid/trimap/blob/master/README.rst](https://github.com/eamid/trimap/blob/master/README.rst)
- GitHub: [https://github.com/eamid/trimap](https://github.com/eamid/trimap)
- PyPI: [https://pypi.org/project/trimap/](https://pypi.org/project/trimap/)

Fallback path links:
- Official API: [https://scikit-learn.org/stable/modules/generated/sklearn.manifold.Isomap.html](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.Isomap.html)
- GitHub: [https://github.com/scikit-learn/scikit-learn](https://github.com/scikit-learn/scikit-learn)
- PyPI: [https://pypi.org/project/scikit-learn/](https://pypi.org/project/scikit-learn/)

## Minimal Python API Pattern
```python
import trimap
Z = trimap.TRIMAP(n_dims=2, n_inliers=12, n_outliers=4, n_random=3).fit_transform(X)
```

## Key Parameters for Bayesian Optimization
- `n_inliers`: nearest-neighbor triplets per point.
- `n_outliers`: outlier triplets per inlier.
- `n_random`: random triplets per point.
- `weight_temp`: triplet-weight temperature.

Search bounds used in the minimal snippet:
- `{"n_inliers": (6, 30), "n_outliers": (2, 12), "n_random": (1, 12), "weight_temp": (0.1, 1.0)}`

## Initialization in Practice
Use `init="pca"` as the default for global-structure tasks, then verify with additional seed runs.

If global conclusions change under small initialization perturbations, downgrade confidence and keep alternate candidates in the final comparison.

## Runtime and Memory Notes
TriMap is designed for large-scale usage, but runtime still grows with sample size and triplet counts.

When datasets are very large, use bounded Bayesian-optimization budgets and then re-check finalists with repeated seeds.

## Common Failure Signs and Fixes
- Global layout unstable across seeds: increase seed checks and narrow search bounds.
- Local neighborhoods look fragmented: reduce `n_outliers` or increase `n_inliers`.
- Runtime too high: reduce `n_random` and tune with smaller candidate budgets first.

## Minimal Runnable Snippet
```python
import numpy as np
from bayes_opt import BayesianOptimization
from zadu import ZADU
import trimap

X = ...  # shape: (n_samples, n_features)

def score(hd, ld):
    vals = ZADU([{"id": "stress"}], hd).measure(ld)[0].values()
    nums = [float(v) for v in vals if isinstance(v, (int, float))]
    return float(np.mean(nums))

def embed(n_inliers, n_outliers, n_random, weight_temp):
    model = trimap.TRIMAP(n_dims=2, n_inliers=int(round(n_inliers)), n_outliers=int(round(n_outliers)), n_random=int(round(n_random)), weight_temp=float(weight_temp))
    return model.fit_transform(X)

def objective(n_inliers, n_outliers, n_random, weight_temp):
    return score(X, embed(n_inliers, n_outliers, n_random, weight_temp))

optimizer = BayesianOptimization(f=objective, pbounds={"n_inliers": (6, 30), "n_outliers": (2, 12), "n_random": (1, 12), "weight_temp": (0.1, 1.0)}, random_state=7, verbose=0)
optimizer.maximize(init_points=4, n_iter=16)
Z_best = embed(**optimizer.max["params"])
```

## Source Notes
- TriMap: Large-scale Dimensionality Reduction Using Triplets (Ehsan Amid; Manfred K. Warmuth, arXiv, 2019/2022 version used in KB)
- Understanding How Dimension Reduction Tools Work: An Empirical Approach to Deciphering t-SNE, UMAP, TriMap, and PaCMAP for Data Visualization (Yingfan Wang et al., Journal of Machine Learning Research, 2021)
