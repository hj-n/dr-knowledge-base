# ClassNeRV

## Technique Summary
Supervised projection method that steers neighborhood distortions to preserve class structure.

In practice, the technique description is intentionally task-centered: the method is not automatically good, and is only appropriate when its distortion profile matches the analytical objective. That framing keeps method choice aligned with user intent instead of popularity.

The summary should be read together with task alignment and tradeoff sections before implementation. When the same dataset supports multiple objectives, this technique may be suitable for one objective and unsuitable for another.

## I/O Contract
- Input: general high-dimensional feature data (labels optional for supervised variants).
- Output: low-dimensional projection coordinates for analysis/visualization.

Input should be treated as a high-dimensional feature representation after data-audit and preprocessing decisions are locked. If normalization, distance definition, or label usage changes during tuning, the effective input contract changes as well and comparisons become noisy.

Output coordinates are analysis artifacts, not ground-truth geometry. They should be consumed according to the declared task, with explicit caution against over-interpreting axes, absolute distances, or visual separations outside the validated use case.

## Core Objective
Optimize a class-aware stress objective so unavoidable distortions are placed where they least harm class structure.

The objective function encodes which structural errors are cheap and which are expensive. Understanding that objective is essential because it predicts the kinds of distortions the method will tolerate when perfect preservation is impossible.

Method selection should therefore ask which distortions are acceptable for this task, and which are not. Choose this technique only when its objective-level priorities match that answer.

## Computation Outline
- Build class-aware objective from NeRV-style formulation.
- Penalize class-relevant false/missed neighbors during optimization.
- Output embedding optimized for class-aware exploratory analysis.

Implementation quality depends on stable preprocessing, deterministic settings where possible, and explicit recording of optimization configuration. Most DR pipelines are sensitive to initialization or neighborhood construction choices, so hidden defaults can change conclusions.

For reproducible comparison, evaluate this technique under a fixed protocol and report parameter context with results. This converts the outline from a conceptual recipe into an auditable procedure for downstream agents and reviewers.

Detailed execution rule: keep label policy fixed and record how missing/noisy labels were handled. Supervised local methods can shift behavior dramatically with label cleaning choices.

## Hyperparameter Impact
- Class-aware penalty weighting changes distortion placement behavior.
- Neighborhood scale settings affect class-local fidelity vs global arrangement.

Hyperparameters determine the local-vs-global balance, optimization stability, and visual behavior of the embedding. They should be tuned against task-aligned metrics rather than aesthetics alone, especially when outputs influence model or policy decisions.

A practical default is Bayesian optimization with safety checks: fixed seed schedule, bounded search space, and multi-metric objective checks. This reduces manual trial-and-error while preserving traceability for why a specific configuration was selected.

Decision-level tuning rule: report both best score and stability behavior (seed variance / restart variance). A configuration that wins once but is unstable should not be the default recommendation.

## Practical Reliability Notes
ClassNeRV is intended for supervised settings where class labels are operationally trusted and class preservation is a primary goal. It explicitly trades distortion placement to retain class structure while keeping neighborhood signals usable.

Because it is label-conditioned, apply the label-separation check before treating class-focused improvements as global quality gains. If class assumptions fail, keep supervised variants as exploratory candidates rather than default recommendations.

## Notable Properties
- Strong for labeled class-structure diagnostics.
- Requires explicit label-quality checks before strong conclusions.

Notable properties should be interpreted as operating characteristics, not guarantees. A property that is beneficial in one data regime can become a liability in another regime with different density, noise level, or manifold complexity.

Use these properties to narrow candidates early, then confirm with metric evidence and task-specific validation. That sequence keeps the workflow grounded in evidence instead of anecdotal method reputation.

## Strengths
This technique is strong for steering neighborhood distortions to preserve class and neighbor constraints jointly. It gives explicit control over class-aware neighborhood behavior in supervised DR objectives.

It is useful when the analysis must balance neighborhood faithfulness with class-consistent local structures.


## Task Alignment
- Inferred alignment: best-aligned tasks
  - Class separability investigation
  - Cluster identification

Task alignment indicates where this technique is expected to provide the most reliable utility under the current evidence base. Treat non-listed tasks as unsupported until new source-backed evidence is added.

When a project requires multiple task outcomes, combine this section with metric-level alignment and require agreement across both layers. If technique and metric recommendations diverge, collect more evidence before production use.

Operational alignment rule: use as primary candidates only for class-separability-oriented tasks; for non-class tasks, keep these methods as optional comparisons and require label-agnostic corroboration.

## Known Tradeoffs
- Can bias embeddings toward labels when labels are noisy or not structurally meaningful.

Tradeoffs are expected and should be made explicit to users before final selection. A method that improves neighborhood fidelity may worsen global distance faithfulness, and vice versa, so optimization must reflect the task hierarchy.

In reporting, document which tradeoffs were accepted and why they were acceptable for the chosen task. This explanation step is part of the contract for trustworthy DR recommendations in this guide.

Communication rule: document one concrete downside that remained after tuning (for example global drift, local fragmentation, or runtime burden) so end users understand residual risk.

## Implementation Options
The default execution path uses the mapped primary Python implementation for this technique. Implementation mode: `approximation`. Primary status: `active`.

Use the primary path when it is `active` or `watch`. If it is `risk`, execute the fallback path and keep the recommendation confidence conservative.

## Recommended Library
Recommended library: **umap-learn (supervised)**.

Current maintenance snapshot: **active** (checked on 2026-02-11). This status is generated from the automated maintenance snapshot using the documented maintenance policy.

## Official API / GitHub / PyPI Links
Primary path links:
- Official API: [https://umap-learn.readthedocs.io/en/latest/supervised.html](https://umap-learn.readthedocs.io/en/latest/supervised.html)
- GitHub: [https://github.com/lmcinnes/umap](https://github.com/lmcinnes/umap)
- PyPI: [https://pypi.org/project/umap-learn/](https://pypi.org/project/umap-learn/)

Fallback path links:
- Official API: [https://torchdr.github.io/dev/gen_modules/torchdr.COSNE.html](https://torchdr.github.io/dev/gen_modules/torchdr.COSNE.html)
- GitHub: [https://github.com/TorchDR/TorchDR](https://github.com/TorchDR/TorchDR)
- PyPI: [https://pypi.org/project/torchdr/](https://pypi.org/project/torchdr/)

## Minimal Python API Pattern
```python
import umap
Z = umap.UMAP(n_neighbors=30, min_dist=0.1, spread=1.0, random_state=7).fit_transform(X, y)
```

## Key Parameters for Bayesian Optimization
- `n_neighbors`: local neighborhood scale.
- `min_dist`: minimum spacing in the low-dimensional layout.
- `spread`: global expansion control paired with `min_dist`.

Search bounds used in the minimal snippet:
- `{"n_neighbors": (5, 120), "min_dist": (0.0, 0.8), "spread": (0.5, 3.0)}`

## Initialization in Practice
For class-aware approximations, use fixed labels and fixed preprocessing before tuning neighborhood controls. Re-check label quality before final reporting.

## Runtime and Memory Notes
UMAP scales well for many datasets, but tuning cost still grows with sample count and repeated seed checks.

## Common Failure Signs and Fixes
- Label noise causes unstable separation -> inspect class quality before optimization.
- Over-tight clusters with weak global context -> raise `min_dist` and validate with distance checks.
- Inconsistent class layout across seeds -> keep fallback candidates.

## Minimal Runnable Snippet
```python
import numpy as np
from bayes_opt import BayesianOptimization
from zadu import ZADU
import umap

X = ...  # shape: (n_samples, n_features)
y = ...  # class labels for supervised execution

def zadu_score(hd, ld):
    spec = [{"id": "tnc", "params": {"k": 20}}]
    result = ZADU(spec, hd).measure(ld)[0]
    vals = [float(v) for v in result.values() if isinstance(v, (int, float))]
    return float(np.mean(vals))

def embed(n_neighbors, min_dist, spread):
    model = umap.UMAP(n_components=2, n_neighbors=int(round(n_neighbors)), min_dist=float(min_dist), spread=float(spread), random_state=7)
    return model.fit_transform(X, y)

def objective(*args, **kwargs):
    z = embed(*args, **kwargs)
    return zadu_score(X, z)

optimizer = BayesianOptimization(f=objective, pbounds={"n_neighbors": (5, 120), "min_dist": (0.0, 0.8), "spread": (0.5, 3.0)}, random_state=7, verbose=0)
optimizer.maximize(init_points=4, n_iter=16)
Z_best = embed(**optimizer.max["params"])
```

## Source Notes
- Steering Distortions to Preserve Classes and Neighbors in Supervised Dimensionality Reduction (Benoit Colange et al., Advances in Neural Information Processing Systems (NeurIPS), 2020)

- Steering Distortions to Preserve Classes and Neighbors in Supervised Dimensionality Reduction (Benoît Colange et al., UNKNOWN, 2020)
