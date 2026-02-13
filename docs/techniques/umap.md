# UMAP

## Technique Summary
Manifold-learning projection emphasizing local neighborhood structure with scalable optimization.

In practice, the technique description is intentionally task-centered: the method is not automatically good, and is only appropriate when its distortion profile matches the analytical objective. That framing keeps method choice aligned with user intent instead of popularity.

The summary should be read together with task alignment and tradeoff sections before implementation. When the same dataset supports multiple objectives, this technique may be suitable for one objective and unsuitable for another.

## I/O Contract
- Input: general high-dimensional feature data (labels optional for supervised variants).
- Output: low-dimensional projection coordinates for analysis/visualization.

Input should be treated as a high-dimensional feature representation after data-audit and preprocessing decisions are locked. If normalization, distance definition, or label usage changes during tuning, the effective input contract changes as well and comparisons become noisy.

Output coordinates are analysis artifacts, not ground-truth geometry. They should be consumed according to the declared task, with explicit caution against over-interpreting axes, absolute distances, or visual separations outside the validated use case.

## Core Objective
Build and optimize a low-dimensional representation that preserves fuzzy local neighborhood graph structure.

The objective function encodes which structural errors are cheap and which are expensive. Understanding that objective is essential because it predicts the kinds of distortions the method will tolerate when perfect preservation is impossible.

Method selection should therefore ask which distortions are acceptable for this task, and which are not. Choose this technique only when its objective-level priorities match that answer.

## Computation Outline
- Construct high-dimensional neighborhood graph.
- Transform to fuzzy simplicial-set style objective.
- Optimize low-dimensional coordinates to preserve graph structure.

Implementation quality depends on stable preprocessing, deterministic settings where possible, and explicit recording of optimization configuration. Most DR pipelines are sensitive to initialization or neighborhood construction choices, so hidden defaults can change conclusions.

For reproducible comparison, evaluate this technique under a fixed protocol and report parameter context with results. This converts the outline from a conceptual recipe into an auditable procedure for downstream agents and reviewers.

Detailed execution rule: run multiple seeds under the same initialization mode and compare structural consistency before accepting conclusions. For local stochastic methods, a single visually appealing run is not sufficient evidence.

## Hyperparameter Impact
- neighborhood and optimization settings remain key controls for local-vs-global behavior.
- initialization policy can strongly affect global-structure interpretation and reproducibility in comparisons.
- Operationally, neighborhood-scale and optimization settings should be tuned with task-aligned metrics and recorded assumptions.

Hyperparameters determine the local-vs-global balance, optimization stability, and visual behavior of the embedding. They should be tuned against task-aligned metrics rather than aesthetics alone, especially when outputs influence model or policy decisions.

A practical default is Bayesian optimization with safety checks: fixed seed schedule, bounded search space, and multi-metric objective checks. This reduces manual trial-and-error while preserving traceability for why a specific configuration was selected.

Decision-level tuning rule: tune local-scale controls and optimization controls jointly, then verify that gains remain under seed perturbation. If seed sensitivity is high, downgrade confidence and keep fallback candidates.

## Practical Reliability Notes
UMAP behavior is strongly controlled by neighborhood size and minimum-distance style controls, which jointly define local packing and cluster spacing. Bayesian optimization trials should be interpreted as task-conditional model choices, not cosmetic tuning.

When UMAP is used for decision support, compare at least one local metric and one global metric under fixed preprocessing and fixed initialization policy. This guards against selecting configurations that look visually clean but are unstable or misaligned to the declared analytical task.

## Notable Properties
- Strong local-structure embeddings for many exploratory tasks.
- Task fit should still be checked before treating as default method.

Notable properties should be interpreted as operating characteristics, not guarantees. A property that is beneficial in one data regime can become a liability in another regime with different density, noise level, or manifold complexity.

Use these properties to narrow candidates early, then confirm with metric evidence and task-specific validation. That sequence keeps the workflow grounded in evidence instead of anecdotal method reputation.

## Strengths
This technique is strong for scalable local-neighborhood manifold embeddings with good practical performance. It often yields strong local-structure organization while handling larger datasets efficiently.

It is useful for neighborhood/outlier/cluster exploration under runtime constraints compared with heavier local methods.


## Task Alignment
- Direct evidence: best-aligned tasks
  - Neighborhood identification
  - Outlier identification
  - Cluster identification

Task alignment indicates where this technique is expected to provide the most reliable utility under the current evidence base. Treat non-listed tasks as unsupported until new source-backed evidence is added.

When a project requires multiple task outcomes, combine this section with metric-level alignment and require agreement across both layers. If technique and metric recommendations diverge, collect more evidence before production use.

Operational alignment rule: method alignment should constrain candidate ranking, but final acceptance still requires agreement with task-aligned reliability check sets and label-separation check status.

## Known Tradeoffs
- Not default for global distance/density tasks in the 7-task taxonomy.

Tradeoffs are expected and should be made explicit to users before final selection. A method that improves neighborhood fidelity may worsen global distance faithfulness, and vice versa, so optimization must reflect the task hierarchy.

In reporting, document which tradeoffs were accepted and why they were acceptable for the chosen task. This explanation step is part of the contract for trustworthy DR recommendations in this guide.

Communication rule: document one concrete downside that remained after tuning (for example global drift, local fragmentation, or runtime burden) so end users understand residual risk.

## Implementation Options
The default execution path uses the mapped primary Python implementation for this technique. Implementation mode: `direct`. Primary status: `active`.

Use the primary path when it is `active` or `watch`. If it is `risk`, execute the fallback path and keep the recommendation confidence conservative.

## Recommended Library
Recommended library: **umap-learn**.

Current maintenance snapshot: **active** (checked on 2026-02-11). This status is generated from the automated maintenance snapshot using the documented maintenance policy.

## Official API / GitHub / PyPI Links
Primary path links:
- Official API: [https://umap-learn.readthedocs.io/en/latest/](https://umap-learn.readthedocs.io/en/latest/)
- GitHub: [https://github.com/lmcinnes/umap](https://github.com/lmcinnes/umap)
- PyPI: [https://pypi.org/project/umap-learn/](https://pypi.org/project/umap-learn/)

Fallback path links:
- Official API: [https://torchdr.github.io/dev/gen_modules/torchdr.UMAP.html](https://torchdr.github.io/dev/gen_modules/torchdr.UMAP.html)
- GitHub: [https://github.com/TorchDR/TorchDR](https://github.com/TorchDR/TorchDR)
- PyPI: [https://pypi.org/project/torchdr/](https://pypi.org/project/torchdr/)

## Minimal Python API Pattern
```python
import umap
Z = umap.UMAP(n_neighbors=30, min_dist=0.1, spread=1.0, random_state=7).fit_transform(X)
```

## Key Parameters for Bayesian Optimization
- `n_neighbors`: local neighborhood scale.
- `min_dist`: minimum spacing in the low-dimensional layout.
- `spread`: global expansion control paired with `min_dist`.

Search bounds used in the minimal snippet:
- `{"n_neighbors": (5, 120), "min_dist": (0.0, 0.8), "spread": (0.5, 3.0)}`

## Initialization in Practice
Use informative initialization for global-sensitive tasks and keep seeds fixed during optimization. Validate with repeated seeds after tuning.

## Runtime and Memory Notes
UMAP scales well for many datasets, but tuning cost still grows with sample count and repeated seed checks.

## Common Failure Signs and Fixes
- Local structure looks unstable across runs -> increase seed checks and narrow search bounds.
- Clusters overlap unexpectedly -> tune `n_neighbors` and `spread` jointly.
- Over-compressed embedding -> increase `min_dist` and retest reliability.

## Minimal Runnable Snippet
```python
import numpy as np
from bayes_opt import BayesianOptimization
from zadu import ZADU
import umap

X = ...  # shape: (n_samples, n_features)

def zadu_score(hd, ld):
    spec = [{"id": "tnc", "params": {"k": 20}}]
    result = ZADU(spec, hd).measure(ld)[0]
    vals = [float(v) for v in result.values() if isinstance(v, (int, float))]
    return float(np.mean(vals))

def embed(n_neighbors, min_dist, spread):
    model = umap.UMAP(n_components=2, n_neighbors=int(round(n_neighbors)), min_dist=float(min_dist), spread=float(spread), random_state=7)
    return model.fit_transform(X)

def objective(*args, **kwargs):
    z = embed(*args, **kwargs)
    return zadu_score(X, z)

optimizer = BayesianOptimization(f=objective, pbounds={"n_neighbors": (5, 120), "min_dist": (0.0, 0.8), "spread": (0.5, 3.0)}, random_state=7, verbose=0)
optimizer.maximize(init_points=4, n_iter=16)
Z_best = embed(**optimizer.max["params"])
```

## Source Notes
- Stop Misusing t-SNE and UMAP for Visual Analytics (Hyeon Jeon, arXiv, 2025)
- Initialization Is Critical for Preserving Global Data Structure in Both t-SNE and UMAP (Dmitry Kobak; George C. Linderman, Nature Biotechnology, 2020)
- Revisiting Dimensionality Reduction Techniques for Visual Cluster Analysis: An Empirical Study (Jiazhi Xia; Yuchen Zhang; Jie Song; Yang Chen; Yunhai Wang; Shixia Liu, IEEE Transactions on Visualization and Computer Graphics, 2022)

- Uniform manifold approximation with two-phase optimization (H. Jeon et al., 2022 IEEE Visualization and Visual Analytics (VIS), 2022)
- Feature Learning for Nonlinear Dimensionality Reduction toward Maximal Extraction of Hidden Patterns (Takanori Fujiwara et al., 2023 IEEE 16th Pacific Visualization Symposium (PacificVis), 2023)
- UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction (Leland McInnes et al., Journal of Open Source Software, 2020)
- Dimensionality reduction for visualizing single-cell data using UMAP (E. Becht et al, Nature Biotechnology, 2019)
- Assessing singlecell transcriptomic variability through density-preserving data visualization (Ashwin Narayan et al., Molecular Systems Biology, 2021)
- Quantitative evaluation of time-dependent multidimensional projection techniques (E. F. V ernier et al., Computer Graphics Forum, 2020)
- HyperNP: Interactive Visual Exploration of Multidimensional Projection Hyperparameters (G. Appleby et al., Computer Graphics Forum, 2022)
- Assessing single-cell transcriptomic variability through density-preserving data visualization (A. Narayan et al., Nature Biotechnology, 2020)
