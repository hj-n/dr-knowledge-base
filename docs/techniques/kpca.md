# KPCA (Kernel PCA)

## Technique Summary
Kernelized PCA projection for nonlinear structure capture via implicit feature space.

In practice, the technique description is intentionally task-centered: the method is not automatically good, and is only appropriate when its distortion profile matches the analytical objective. That framing keeps method choice aligned with user intent instead of popularity.

The summary should be read together with task alignment and tradeoff sections before implementation. When the same dataset supports multiple objectives, this technique may be suitable for one objective and unsuitable for another.

## I/O Contract
- Input: general high-dimensional feature data (labels optional for supervised variants).
- Output: low-dimensional projection coordinates for analysis/visualization.

Input should be treated as a high-dimensional feature representation after data-audit and preprocessing decisions are locked. If normalization, distance definition, or label usage changes during tuning, the effective input contract changes as well and comparisons become noisy.

Output coordinates are analysis artifacts, not ground-truth geometry. They should be consumed according to the declared task, with explicit caution against over-interpreting axes, absolute distances, or visual separations outside the validated use case.

## Core Objective
Perform linear projection in kernel-induced feature space to obtain nonlinear low-dimensional projections.

The objective function encodes which structural errors are cheap and which are expensive. Understanding that objective is essential because it predicts the kinds of distortions the method will tolerate when perfect preservation is impossible.

Method selection should therefore ask which distortions are acceptable for this task, and which are not. Choose this technique only when its objective-level priorities match that answer.

## Computation Outline
- Choose kernel function and kernel parameters.
- Compute centered kernel matrix.
- Eigen-decompose kernel matrix and project onto leading components.

Implementation quality depends on stable preprocessing, deterministic settings where possible, and explicit recording of optimization configuration. Most DR pipelines are sensitive to initialization or neighborhood construction choices, so hidden defaults can change conclusions.

For reproducible comparison, evaluate this technique under a fixed protocol and report parameter context with results. This converts the outline from a conceptual recipe into an auditable procedure for downstream agents and reviewers.

Detailed execution rule: run this method under a fixed preprocessing contract and log all stochastic controls (seed, restart index, initialization metadata) so comparison runs are auditable.

## Hyperparameter Impact
- Kernel type/parameters determine geometry of captured nonlinear structure.
- Number of components controls information retained in projection.

Hyperparameters determine the local-vs-global balance, optimization stability, and visual behavior of the embedding. They should be tuned against task-aligned metrics rather than aesthetics alone, especially when outputs influence model or policy decisions.

A practical default is Bayesian optimization with safety checks: fixed seed schedule, bounded search space, and multi-metric objective checks. This reduces manual trial-and-error while preserving traceability for why a specific configuration was selected.

Decision-level tuning rule: kernel family and kernel scale are first-order assumptions, not minor tweaks. Log chosen kernel rationale and compare against linear/global baselines under the same protocol.

## Practical Reliability Notes
Kernel PCA depends heavily on kernel choice and kernel scale. Different kernel settings represent different geometry assumptions; method comparison is invalid if kernel policy is not controlled.

Use KPCA when nonlinear global structure is plausible and kernel assumptions are justified by the task. Always compare against linear PCA and at least one neighborhood-focused method to verify whether kernel-induced gains are truly task-relevant.

## Notable Properties
- Can represent nonlinear structure with linear algebra pipeline in kernel space.
- Interpretability depends on kernel choice.

Notable properties should be interpreted as operating characteristics, not guarantees. A property that is beneficial in one data regime can become a liability in another regime with different density, noise level, or manifold complexity.

Use these properties to narrow candidates early, then confirm with metric evidence and task-specific validation. That sequence keeps the workflow grounded in evidence instead of anecdotal method reputation.

## Strengths
This technique is strong for capturing nonlinear variance structure through kernel mappings while keeping a PCA-like framework. It is useful when linear PCA underfits curvature or nonlinear separability patterns.

It can provide a practical nonlinear global representation with familiar component-style interpretation workflow.


## Task Alignment
- Inferred alignment: best-aligned tasks
  - Neighborhood identification
  - Cluster identification
  - Point distance investigation

Task alignment indicates where this technique is expected to provide the most reliable utility under the current evidence base. Treat non-listed tasks as unsupported until new source-backed evidence is added.

When a project requires multiple task outcomes, combine this section with metric-level alignment and require agreement across both layers. If technique and metric recommendations diverge, collect more evidence before production use.

Operational alignment rule: method alignment should constrain candidate ranking, but final acceptance still requires agreement with task-aligned reliability check sets and label-separation check status.

## Known Tradeoffs
- Kernel tuning is critical and may be unstable without validation metrics.

Tradeoffs are expected and should be made explicit to users before final selection. A method that improves neighborhood fidelity may worsen global distance faithfulness, and vice versa, so optimization must reflect the task hierarchy.

In reporting, document which tradeoffs were accepted and why they were acceptable for the chosen task. This explanation step is part of the contract for trustworthy DR recommendations in this guide.

Communication rule: document one concrete downside that remained after tuning (for example global drift, local fragmentation, or runtime burden) so end users understand residual risk.

## Implementation Options
The default execution path uses the mapped primary Python implementation for this technique. Implementation mode: `direct`. Primary status: `active`.

Use the primary path when it is `active` or `watch`. If it is `risk`, execute the fallback path and keep the recommendation confidence conservative.

## Recommended Library
Recommended library: **scikit-learn KernelPCA**.

Current maintenance snapshot: **active** (checked on 2026-02-11). This status is generated from the automated maintenance snapshot using the documented maintenance policy.

## Official API / GitHub / PyPI Links
Primary path links:
- Official API: [https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html)
- GitHub: [https://github.com/scikit-learn/scikit-learn](https://github.com/scikit-learn/scikit-learn)
- PyPI: [https://pypi.org/project/scikit-learn/](https://pypi.org/project/scikit-learn/)

Fallback path links:
- Official API: [https://torchdr.github.io/dev/gen_modules/torchdr.KernelPCA.html](https://torchdr.github.io/dev/gen_modules/torchdr.KernelPCA.html)
- GitHub: [https://github.com/TorchDR/TorchDR](https://github.com/TorchDR/TorchDR)
- PyPI: [https://pypi.org/project/torchdr/](https://pypi.org/project/torchdr/)

## Minimal Python API Pattern
```python
from sklearn.decomposition import KernelPCA
Z = KernelPCA(n_components=2, kernel="rbf", gamma=0.1).fit_transform(X)
```

## Key Parameters for Bayesian Optimization
- `gamma`: controls kernel locality for RBF kernels.
- `n_components`: output dimension used by downstream analysis.

Search bounds used in the minimal snippet:
- `{"n_components": (2, 20), "gamma": (1e-4, 1.0)}`

## Initialization in Practice
Kernel PCA does not use stochastic initialization. Keep kernel type fixed before tuning gamma to avoid mixed objective behavior.

## Runtime and Memory Notes
Kernel matrix operations can become expensive at larger sample counts. Memory cost grows quickly with `n_samples`.

## Common Failure Signs and Fixes
- Embedding collapses into near-line shape -> widen gamma search and verify scaling.
- Large runtime spikes -> reduce sample size for optimization phase, then re-fit on full data.
- Highly fragmented local neighborhoods -> add local reliability checks before selection.

## Minimal Runnable Snippet
```python
import numpy as np
from bayes_opt import BayesianOptimization
from zadu import ZADU
from sklearn.decomposition import KernelPCA

X = ...  # shape: (n_samples, n_features)

def zadu_score(hd, ld):
    spec = [{"id": "tnc", "params": {"k": 20}}]
    result = ZADU(spec, hd).measure(ld)[0]
    vals = [float(v) for v in result.values() if isinstance(v, (int, float))]
    return float(np.mean(vals))

def embed(n_components, gamma):
    model = KernelPCA(n_components=int(round(n_components)), kernel="rbf", gamma=float(gamma))
    return model.fit_transform(X)

def objective(*args, **kwargs):
    z = embed(*args, **kwargs)
    return zadu_score(X, z)

optimizer = BayesianOptimization(f=objective, pbounds={"n_components": (2, 20), "gamma": (1e-4, 1.0)}, random_state=7, verbose=0)
optimizer.maximize(init_points=4, n_iter=16)
Z_best = embed(**optimizer.max["params"])
```

## Source Notes
- Local Multidimensional Scaling for Nonlinear Dimension Reduction, Graph Drawing, and Proximity Analysis (Lisha Chen et al., Journal of the American Statistical Association, 2009)

- Interactive Visual Cluster Analysis by Contrastive Dimensionality Reduction (Jiazhi Xia et al., IEEE Transactions on Visualization and Computer Graphics, 2022)
- Linear dimensionality reduction: Survey, insights, and generalizations (John P Cunningham and Zoubin Ghahramani, UNKNOWN, 2015)
- A new method of generalizing Sammon mapping with application to algorithm speed-up (E. Pekalska et al., IEEE Transactions on Pattern Analysis and Machine Intelligence, 1999)
- dimRed and coRanking—Unifying Dimensionality Reduction in R (G. Kraemer et al., The R Journal, 2018)
- Nonlinear Dimensionality Reduction by Semideﬁnite Programming and Kernel Matrix Factorization (Programming and Kernel Matrix Factorization, UNKNOWN, 2000)
