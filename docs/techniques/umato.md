# UMATO

## Technique Summary
UMATO is a two-phase manifold-learning method designed to preserve both local neighborhoods and global manifold structure for reliable visual analytics.

The method separates representative hub points from non-hub points and optimizes in two phases. This strategy targets a more stable global arrangement while retaining useful local structure.

## I/O Contract
- Input: high-dimensional feature matrix `X` with shape `(n_samples, n_features)`.
- Output: low-dimensional projection `Z` with shape `(n_samples, n_components)`, typically 2D.

UMATO is available as a Python package with a familiar `fit`/`fit_transform` interface. For method comparisons, keep preprocessing, distance choice, and seed protocol fixed.

## Core Objective
UMATO aims to bridge local and global structure preservation in one projection workflow by combining global hub-layout optimization with local refinement.

This objective is useful for visual-analytics workflows where users need both neighborhood readability and trustworthy large-scale layout.

## Computation Outline
UMATO first establishes a global skeletal structure using hub points, then places and refines non-hub points in a local optimization phase.

The objective includes negative sampling and phase-specific optimization controls. Initialization choice (notably PCA) and phase hyperparameters materially affect both runtime and stability.

## Hyperparameter Impact
`n_neighbors` and `hub_num` govern neighborhood construction and global skeleton quality. `global_n_epochs`/`local_n_epochs` and corresponding learning rates control optimization strength in each phase.

`min_dist`, `spread`, `gamma`, and `negative_sample_rate` affect local packing and repulsion behavior. Tune these controls with Bayesian optimization and verify selected settings across repeated seeds.

## Practical Reliability Notes
UMATO is appropriate when users ask for balanced local/global interpretation and reliable visual-analytics projections. It should be compared against other methods under identical preprocessing and evaluation protocols.

Because UMATO is phase-based, unstable hub selection or over-aggressive local refinement can still distort interpretation. Always validate with both local and global reliability checks and include residual-risk notes in final reporting.

## Notable Properties
UMATO emphasizes global-structure robustness while keeping local structure competitive, and source notes report strong scalability characteristics.

Its two-phase design also supports better initialization stability than purely single-phase local optimizers in many settings.

## Strengths
UMATO is strong for workflows where both inter-cluster arrangement and local-neighborhood readability are required.

It is also practical for larger datasets, with explicit phase-level controls that can be tuned for runtime-quality tradeoffs.

## Task Alignment
- Direct evidence: Cluster distance investigation
- Direct evidence: Cluster density investigation
- Inferred alignment: Point distance investigation

The source notes describe UMATO as a method for reliable visual analytics with explicit local/global balancing, which aligns directly to global-structure-sensitive tasks.

## Known Tradeoffs
UMATO has more phase-specific controls than simpler methods, so untuned defaults may not transfer reliably across datasets.

If hub-related settings are poorly chosen, global layout can become brittle or expensive to optimize. Treat parameter search and seed validation as mandatory.

## Implementation Options
The default path is the official Python `umato` package.

If UMATO is unavailable or unstable in a given environment, use UMAP as a fallback and report that the method family changed.

## Recommended Library
Recommended library: **umato**.

## Official API / GitHub / PyPI Links
Primary path links:
- Official API: [https://github.com/hyungkwonko/umato/wiki/API](https://github.com/hyungkwonko/umato/wiki/API)
- GitHub: [https://github.com/hyungkwonko/umato](https://github.com/hyungkwonko/umato)
- PyPI: [https://pypi.org/project/umato/](https://pypi.org/project/umato/)

Fallback path links:
- Official API: [https://umap-learn.readthedocs.io/en/latest/](https://umap-learn.readthedocs.io/en/latest/)
- GitHub: [https://github.com/lmcinnes/umap](https://github.com/lmcinnes/umap)
- PyPI: [https://pypi.org/project/umap-learn/](https://pypi.org/project/umap-learn/)

## Minimal Python API Pattern
```python
import umato
Z = umato.UMATO(n_components=2, n_neighbors=50, hub_num=300, init="pca", random_state=42).fit_transform(X)
```

## Key Parameters for Bayesian Optimization
- `n_neighbors`: neighborhood size for graph construction.
- `hub_num`: number of representative hub points.
- `min_dist`: compactness/spacing control.
- `gamma`: local repulsion strength.

Search bounds used in the minimal snippet:
- `{"n_neighbors": (15, 120), "hub_num": (50, 600), "min_dist": (0.0, 0.8), "gamma": (0.01, 0.5)}`

## Initialization in Practice
Use `init="pca"` as the default unless evidence for a different initializer is explicit for the task and dataset.

Run repeated seeds for finalists and keep the initialization policy fixed during optimization so comparisons remain interpretable.

## Runtime and Memory Notes
UMATO is designed for scalable two-phase optimization, but runtime still depends on dataset size, hub count, and epoch settings.

For large datasets, constrain Bayesian-optimization budgets and then re-evaluate top settings with repeated-seed checks.

## Common Failure Signs and Fixes
- Global layout unstable across repeats: adjust `hub_num` and increase seed checks.
- Local over-compression: increase `min_dist` or lower `gamma`.
- Runtime too high: reduce phase-epoch budgets and narrow search bounds.

## Minimal Runnable Snippet
```python
import numpy as np
from bayes_opt import BayesianOptimization
from zadu import ZADU
import umato

X = ...  # shape: (n_samples, n_features)

def score(hd, ld):
    vals = ZADU([{"id": "stress"}, {"id": "tnc", "params": {"k": 20}}], hd).measure(ld)[0].values()
    nums = [float(v) for v in vals if isinstance(v, (int, float))]
    return float(np.mean(nums))

def embed(n_neighbors, hub_num, min_dist, gamma):
    model = umato.UMATO(n_components=2, n_neighbors=int(round(n_neighbors)), hub_num=int(round(hub_num)), min_dist=float(min_dist), gamma=float(gamma), init="pca", random_state=42)
    return model.fit_transform(X)

def objective(n_neighbors, hub_num, min_dist, gamma):
    return score(X, embed(n_neighbors, hub_num, min_dist, gamma))

optimizer = BayesianOptimization(f=objective, pbounds={"n_neighbors": (15, 120), "hub_num": (50, 600), "min_dist": (0.0, 0.8), "gamma": (0.01, 0.5)}, random_state=7, verbose=0)
optimizer.maximize(init_points=4, n_iter=16)
Z_best = embed(**optimizer.max["params"])
```

## Source Notes
- Uniform Manifold Approximation with Two-phase Optimization (Hyeon Jeon et al., IEEE VIS, 2022)
- UMATO: Bridging Local and Global Structures for Reliable Visual Analytics With Dimensionality Reduction (Hyeon Jeon et al., IEEE Transactions on Visualization and Computer Graphics, 2025)
