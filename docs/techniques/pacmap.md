# PaCMAP

## Technique Summary
PaCMAP is a pairwise-manifold method designed to preserve both local neighborhoods and broader global arrangement in one embedding.

It uses three pair types (neighbor, mid-near, and further pairs) and staged optimization behavior to avoid collapsing into purely local or purely global distortion patterns. This makes it a useful candidate when users need balanced visual analytics.

## I/O Contract
- Input: high-dimensional feature matrix `X` with shape `(n_samples, n_features)`.
- Output: low-dimensional projection `Z` with shape `(n_samples, n_components)`, typically 2D.

The implementation follows a scikit-learn-like API and supports `fit`/`fit_transform`. For reliable comparison, keep preprocessing and distance assumptions constant across all candidate methods.

## Core Objective
PaCMAP optimizes embedding coordinates with controlled pairwise constraints to preserve structure at multiple scales.

The method explicitly manages local and global behavior via pair composition rather than relying on a single neighborhood control. That design is useful when the task needs interpretable local clusters without losing broad cluster-to-cluster geometry.

## Computation Outline
PaCMAP builds neighbor, mid-near, and further pair sets, then optimizes the embedding so that these pairwise relations are respected over iterations.

Initialization and pair-ratio parameters can materially change outcomes. For operational reliability, use fixed preprocessing, documented initialization choice, and seed-based stability checks after optimization.

## Hyperparameter Impact
`n_neighbors` sets neighborhood scale, while `MN_ratio` and `FP_ratio` control the contribution of mid-near and far pairs. These parameters directly shape local/global balance.

The `init` choice (`pca` vs `random`) and optimizer settings (`lr`, iterations) affect stability and convergence. Tune key parameters with Bayesian optimization and keep repeated-seed validation for finalists.

## Practical Reliability Notes
PaCMAP can be strong when the user asks for both local readability and global context. It should still be evaluated with multiple reliability checks, because pair-ratio settings can bias the embedding toward one side.

Keep one preprocessing setup and one distance definition across candidate methods. If reliability rankings flip often across seeds or nearby parameter settings, report lower confidence and keep fallback candidates.

## Notable Properties
PaCMAP is frequently used as a balanced nonlinear baseline in visual analytics comparisons. It is available as an easy-to-run Python package.

Its pairwise design gives controllable behavior across scales, which is useful for analyses that need both neighborhood detail and global layout cues.

## Strengths
PaCMAP provides a practical compromise between local and global structure preservation and is straightforward to integrate into Python analysis pipelines.

It is a good candidate for mixed-goal exploratory workflows where users need interpretable cluster organization without discarding global context.

## Task Alignment
- Direct evidence: Cluster identification
- Direct evidence: Neighborhood identification
- Inferred alignment: Cluster distance investigation

Empirical evidence in the source notes compares PaCMAP directly with t-SNE, UMAP, and TriMap and shows its role as a balanced method rather than a single-scale specialist.

## Known Tradeoffs
PaCMAP still requires parameter tuning; default settings are not universally optimal across datasets and tasks.

If pair-ratio settings are poorly chosen, embeddings can under-emphasize either local detail or global arrangement. Always check task-aligned reliability scores and stability before finalizing.

## Implementation Options
The default path is the official Python `pacmap` package.

If PaCMAP cannot satisfy runtime or reliability constraints, use UMAP as a fallback and keep the same preprocessing/tuning protocol for fair comparison.

## Recommended Library
Recommended library: **pacmap**.

## Official API / GitHub / PyPI Links
Primary path links:
- Official API: [https://github.com/YingfanWang/PaCMAP](https://github.com/YingfanWang/PaCMAP)
- GitHub: [https://github.com/YingfanWang/PaCMAP](https://github.com/YingfanWang/PaCMAP)
- PyPI: [https://pypi.org/project/pacmap/](https://pypi.org/project/pacmap/)

Fallback path links:
- Official API: [https://umap-learn.readthedocs.io/en/latest/](https://umap-learn.readthedocs.io/en/latest/)
- GitHub: [https://github.com/lmcinnes/umap](https://github.com/lmcinnes/umap)
- PyPI: [https://pypi.org/project/umap-learn/](https://pypi.org/project/umap-learn/)

## Minimal Python API Pattern
```python
import pacmap
Z = pacmap.PaCMAP(n_components=2, n_neighbors=10, MN_ratio=0.5, FP_ratio=2.0).fit_transform(X, init="pca")
```

## Key Parameters for Bayesian Optimization
- `n_neighbors`: number of nearest neighbors.
- `MN_ratio`: mid-near pair ratio.
- `FP_ratio`: further-pair ratio.

Search bounds used in the minimal snippet:
- `{"n_neighbors": (5, 60), "MN_ratio": (0.1, 1.5), "FP_ratio": (0.5, 4.0)}`

## Initialization in Practice
Use `init="pca"` as the default for reproducible comparisons, and include repeated-seed checks for selected configurations.

If the selected configuration is highly seed-sensitive, treat the recommendation as provisional and include a fallback method in reporting.

## Runtime and Memory Notes
PaCMAP is practical for medium and large datasets, but optimization cost still increases with sample count and parameter-search budget.

For large data, use bounded Bayesian-optimization budgets and then re-run only top configurations with seed repeats.

## Common Failure Signs and Fixes
- Over-fragmented clusters: increase `n_neighbors` or lower `FP_ratio`.
- Over-smoothed local structure: lower `n_neighbors` or raise `MN_ratio`.
- Inconsistent ranking across repeats: narrow search bounds and increase seed checks.

## Minimal Runnable Snippet
```python
import numpy as np
from bayes_opt import BayesianOptimization
from zadu import ZADU
import pacmap

X = ...  # shape: (n_samples, n_features)

def score(hd, ld):
    vals = ZADU([{"id": "tnc", "params": {"k": 20}}], hd).measure(ld)[0].values()
    nums = [float(v) for v in vals if isinstance(v, (int, float))]
    return float(np.mean(nums))

def embed(n_neighbors, MN_ratio, FP_ratio):
    model = pacmap.PaCMAP(n_components=2, n_neighbors=int(round(n_neighbors)), MN_ratio=float(MN_ratio), FP_ratio=float(FP_ratio))
    return model.fit_transform(X, init="pca")

def objective(n_neighbors, MN_ratio, FP_ratio):
    return score(X, embed(n_neighbors, MN_ratio, FP_ratio))

optimizer = BayesianOptimization(f=objective, pbounds={"n_neighbors": (5, 60), "MN_ratio": (0.1, 1.5), "FP_ratio": (0.5, 4.0)}, random_state=7, verbose=0)
optimizer.maximize(init_points=4, n_iter=16)
Z_best = embed(**optimizer.max["params"])
```

## Source Notes
- Understanding How Dimension Reduction Tools Work: An Empirical Approach to Deciphering t-SNE, UMAP, TriMap, and PaCMAP for Data Visualization (Yingfan Wang et al., Journal of Machine Learning Research, 2021)
- UMATO: Bridging Local and Global Structures for Reliable Visual Analytics With Dimensionality Reduction (Hyeon Jeon et al., IEEE Transactions on Visualization and Computer Graphics, 2025)
