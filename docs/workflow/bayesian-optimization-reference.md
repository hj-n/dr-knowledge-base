# Bayesian Optimization Reference

Use this page as the default implementation card for Bayesian optimization in DR workflows.

Related:
- Workflow step: [`docs/workflow/dr-analysis-workflow.md`](./dr-analysis-workflow.md)
- Optimization policy: [`docs/workflow/hyperparameter-optimization-protocol.md`](./hyperparameter-optimization-protocol.md)
- Technique cards: [`docs/techniques/README.md`](../techniques/README.md)

Implementation source references:
- UMATO experiment runner style: [01_accuracy.py](https://github.com/hj-n/umato_exp/blob/master/_final_exp/01_accuracy.py)
- Technique bound metadata: [_metadata.json](https://github.com/hj-n/umato_exp/blob/master/_final_exp/_metadata.json)

## Canonical Python Pattern (Copy First)
```python
import numpy as np
from bayes_opt import BayesianOptimization
from zadu import ZADU


def clamp_bounds(bounds: dict, n_samples: int) -> dict:
    b = dict(bounds)
    if "n_neighbors" in b:
        b["n_neighbors"] = (max(2, b["n_neighbors"][0]), min(b["n_neighbors"][1], n_samples - 2))
    if "n_inliers" in b:
        b["n_inliers"] = (max(2, b["n_inliers"][0]), min(b["n_inliers"][1], n_samples - 2))
    if "n_outliers" in b:
        b["n_outliers"] = (max(2, b["n_outliers"][0]), min(b["n_outliers"][1], n_samples - 2))
    if "hub_num" in b:
        b["hub_num"] = (max(2, b["hub_num"][0]), min(b["hub_num"][1], max(4, n_samples // 4)))
    return b


def optimize_embedding(run_fn, X: np.ndarray, bounds: dict) -> tuple[dict, float]:
    zadu_obj = ZADU([{"id": "tnc", "params": {"k": 10}}], X)
    pbounds = clamp_bounds(bounds, X.shape[0])

    def objective(**params):
        try:
            Z = run_fn(X, **params)
            m = zadu_obj.measure(Z)[0]
            tw = float(m["trustworthiness"])
            co = float(m["continuity"])
            return (2.0 * tw * co) / (tw + co + 1e-12)
        except Exception:
            return 0.0

    opt = BayesianOptimization(
        f=objective,
        pbounds=pbounds,
        random_state=7,
        verbose=0,
        allow_duplicate_points=True,
    )
    opt.maximize(init_points=10, n_iter=20)
    return opt.max["params"], float(opt.max["target"])
```

## Why This Helps Raise Metric Scores
- Bayesian optimization targets high-potential regions of the parameter space early, instead of spending equal effort on low-value regions.
- For score-oriented DR tuning, this adaptive allocation typically improves the best achieved metric value compared with fixed candidate sweeps under similar trial budgets.
- This is the reason the KB policy keeps optimizer family fixed to `bayes_opt` for final recommendations.

## Metadata-Aligned Bounds For Major Techniques
The following bounds come from [`_metadata.json`](https://github.com/hj-n/umato_exp/blob/master/_final_exp/_metadata.json) and should be used as default starting ranges.

| Technique | Parameter | Default Bound |
|---|---|---|
| `tsne` | `perplexity` | `[5, 50]` |
| `isomap` | `n_neighbors` | `[2, 100]` |
| `umap` | `n_neighbors`, `min_dist` | `[2, 100]`, `[0.01, 0.99]` |
| `umap_pca` | `n_neighbors`, `min_dist` | `[2, 100]`, `[0.01, 0.99]` |
| `umato` | `n_neighbors`, `min_dist`, `hub_num` | `[2, 100]`, `[0.01, 0.99]`, `[20, 400]` |
| `pacmap` | `n_neighbors`, `MN_ratio`, `FP_ratio` | `[2, 100]`, `[0.1, 5]`, `[0.1, 5]` |
| `trimap` | `n_inliers`, `n_outliers` | `[2, 100]`, `[2, 10]` |
| `lle` | `n_neighbors` | `[2, 100]` |
| `lmds` | `hub_num` | `[20, 400]` |

Notes:
- `pca` and `lamp` are listed with empty bound sets in the metadata. Treat them as zero- or low-tuning methods unless a task requires explicit parameter search.
- Always apply dataset-size clamping before running the optimizer.

## Wide-Range Rule For Techniques Not In Metadata
If a technique is not covered by `_metadata.json`, start with wide bounds and narrow only after early trials.

Recommended wide starting ranges:
- neighborhood size: `n_neighbors in [5, min(200, n_samples - 2)]`
- distance packing: `min_dist in [0.0, 0.99]`
- perplexity-like controls: `perplexity in [5, min(80, (n_samples - 1) / 3)]`
- learning-rate controls: `learning_rate in [10, 2000]`
- spread/repulsion controls: `spread in [0.5, 5.0]`, `gamma in [1e-4, 10.0]`
- hub/landmark controls: `hub_num in [20, min(800, n_samples / 4)]`

Protocol:
1. Start wide for the first budget (`init_points + first n_iter` block).
2. Narrow around top-performing regions only after score stabilization.
3. Keep optimizer family fixed to `bayes_opt`.

## Do Not Replace Optimizer Family
Even under permissive prompts (for example, "any optimization is allowed"), keep optimizer family fixed to Bayesian optimization.
Do not switch to grid search, random search, or manual parameter sweeps in final recommendation code.
