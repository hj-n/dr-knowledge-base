# SNE

## Technique Summary
Probabilistic neighborhood projection minimizing KL divergence between high- and low-dimensional neighbor distributions.

In practice, the technique description is intentionally task-centered: the method is not automatically good, and is only appropriate when its distortion profile matches the analytical objective. That framing keeps method choice aligned with user intent instead of popularity.

The summary should be read together with task alignment and tradeoff sections before implementation. When the same dataset supports multiple objectives, this technique may be suitable for one objective and unsuitable for another.

## I/O Contract
- Input: general high-dimensional feature data (labels optional for supervised variants).
- Output: low-dimensional projection coordinates for analysis/visualization.

Input should be treated as a high-dimensional feature representation after data-audit and preprocessing decisions are locked. If normalization, distance definition, or label usage changes during tuning, the effective input contract changes as well and comparisons become noisy.

Output coordinates are analysis artifacts, not ground-truth geometry. They should be consumed according to the declared task, with explicit caution against over-interpreting axes, absolute distances, or visual separations outside the validated use case.

## Core Objective
Preserve neighborhood identities probabilistically via divergence minimization.

The objective function encodes which structural errors are cheap and which are expensive. Understanding that objective is essential because it predicts the kinds of distortions the method will tolerate when perfect preservation is impossible.

Method selection should therefore ask which distortions are acceptable for this task, and which are not. Choose this technique only when its objective-level priorities match that answer.

## Computation Outline
- Construct high-dimensional neighbor probability distributions.
- Construct low-dimensional neighbor probability distributions.
- Optimize embedding by minimizing KL-divergence objective.

Implementation quality depends on stable preprocessing, deterministic settings where possible, and explicit recording of optimization configuration. Most DR pipelines are sensitive to initialization or neighborhood construction choices, so hidden defaults can change conclusions.

For reproducible comparison, evaluate this technique under a fixed protocol and report parameter context with results. This converts the outline from a conceptual recipe into an auditable procedure for downstream agents and reviewers.

Detailed execution rule: run multiple seeds under the same initialization mode and compare structural consistency before accepting conclusions. For local stochastic methods, a single visually appealing run is not sufficient evidence.

## Hyperparameter Impact
- `perplexity` sets effective local-neighbor scale.
- `learning rate` and jitter/noise schedule influence convergence and local minima.

Hyperparameters determine the local-vs-global balance, optimization stability, and visual behavior of the embedding. They should be tuned against task-aligned metrics rather than aesthetics alone, especially when outputs influence model or policy decisions.

A practical default is Bayesian optimization with safety checks: fixed seed schedule, bounded search space, and multi-metric objective checks. This reduces manual trial-and-error while preserving traceability for why a specific configuration was selected.

Decision-level tuning rule: tune local-scale controls and optimization controls jointly, then verify that gains remain under seed perturbation. If seed sensitivity is high, downgrade confidence and keep fallback candidates.

## Practical Reliability Notes
SNE is historically important and still useful as a conceptual baseline for probabilistic neighborhood embedding behavior. It helps interpret why later variants (for example t-SNE) change global/local behavior.

For modern workflows, use SNE mainly in comparative or methodological contexts rather than as a default production recommendation. If used, apply strong seed and optimization stability reporting because convergence behavior can vary substantially.

## Notable Properties
- Probability-based neighborhood modeling is a notable conceptual strength.
- Optimization can be slow and schedule-sensitive.

Notable properties should be interpreted as operating characteristics, not guarantees. A property that is beneficial in one data regime can become a liability in another regime with different density, noise level, or manifold complexity.

Use these properties to narrow candidates early, then confirm with metric evidence and task-specific validation. That sequence keeps the workflow grounded in evidence instead of anecdotal method reputation.

## Strengths
This technique is strong for probabilistic neighborhood-preservation formulations that capture local similarity behavior. It provides a foundational local-probability perspective for neighborhood embeddings.

It is useful when local similarity distributions are the core fidelity target.


## Task Alignment
- Inferred alignment: best-aligned tasks
  - Neighborhood identification
  - Outlier identification
  - Cluster identification

Task alignment indicates where this technique is expected to provide the most reliable utility under the current evidence base. Treat non-listed tasks as unsupported until new source-backed evidence is added.

When a project requires multiple task outcomes, combine this section with metric-level alignment and require agreement across both layers. If technique and metric recommendations diverge, collect more evidence before production use.

Operational alignment rule: method alignment should constrain candidate ranking, but final acceptance still requires agreement with task-aligned reliability check sets and label-separation check status.

## Known Tradeoffs
- Needs careful optimization configuration for stable reproducible results.

Tradeoffs are expected and should be made explicit to users before final selection. A method that improves neighborhood fidelity may worsen global distance faithfulness, and vice versa, so optimization must reflect the task hierarchy.

In reporting, document which tradeoffs were accepted and why they were acceptable for the chosen task. This explanation step is part of the contract for trustworthy DR recommendations in this guide.

Communication rule: document one concrete downside that remained after tuning (for example global drift, local fragmentation, or runtime burden) so end users understand residual risk.

## Implementation Options
The default execution path uses the mapped primary Python implementation for this technique. Implementation mode: `direct`. Primary status: `active`.

Use the primary path when it is `active` or `watch`. If it is `risk`, execute the fallback path and keep the recommendation confidence conservative.

## Recommended Library
Recommended library: **TorchDR SNE**.

Current maintenance snapshot: **active** (checked on 2026-02-11). This status is generated from the automated maintenance snapshot using the documented maintenance policy.

## Official API / GitHub / PyPI Links
Primary path links:
- Official API: [https://torchdr.github.io/dev/gen_modules/torchdr.SNE.html](https://torchdr.github.io/dev/gen_modules/torchdr.SNE.html)
- GitHub: [https://github.com/TorchDR/TorchDR](https://github.com/TorchDR/TorchDR)
- PyPI: [https://pypi.org/project/torchdr/](https://pypi.org/project/torchdr/)

Fallback path links:
- Official API: [https://opentsne.readthedocs.io/en/latest/](https://opentsne.readthedocs.io/en/latest/)
- GitHub: [https://github.com/pavlin-policar/openTSNE](https://github.com/pavlin-policar/openTSNE)
- PyPI: [https://pypi.org/project/openTSNE/](https://pypi.org/project/openTSNE/)

Additional reference implementation:
- SNE/NeRV experimental R package: [https://github.com/jlmelville/sneer](https://github.com/jlmelville/sneer)

## Minimal Python API Pattern
```python
from torchdr import SNE
Z = np.asarray(SNE(n_components=2, perplexity=30).fit_transform(X))
```

## Key Parameters for Bayesian Optimization
- `perplexity`: neighborhood scale in probability matching.
- `n_components`: embedding dimensionality (typically 2 for visualization).

Search bounds used in the minimal snippet:
- `{"perplexity": (5, 80)}`

## Initialization in Practice
SNE-family methods are sensitive to initialization and optimization behavior. Use repeated seeds after selecting best parameters.

## Runtime and Memory Notes
Quadratic behavior can appear on larger datasets. Use representative subsets during optimization when needed.

## Common Failure Signs and Fixes
- Optimization stalls early -> broaden learning settings or reduce sample size for search.
- Layout heavily changes across repeats -> mark recommendation as provisional.
- Class conclusions depend on one run -> require repeated reliability checks.

## Minimal Runnable Snippet
```python
import numpy as np
from bayes_opt import BayesianOptimization
from zadu import ZADU
from torchdr import SNE

X = ...  # shape: (n_samples, n_features)

def zadu_score(hd, ld):
    spec = [{"id": "tnc", "params": {"k": 20}}]
    result = ZADU(spec, hd).measure(ld)[0]
    vals = [float(v) for v in result.values() if isinstance(v, (int, float))]
    return float(np.mean(vals))

def embed(perplexity):
    model = SNE(n_components=2, perplexity=float(perplexity))
    return np.asarray(model.fit_transform(X))

def objective(*args, **kwargs):
    z = embed(*args, **kwargs)
    return zadu_score(X, z)

optimizer = BayesianOptimization(f=objective, pbounds={"perplexity": (5, 80)}, random_state=7, verbose=0)
optimizer.maximize(init_points=4, n_iter=16)
Z_best = embed(**optimizer.max["params"])
```

## Source Notes
- Stochastic Neighbor Embedding (Geoffrey E. Hinton et al., Advances in Neural Information Processing Systems (NIPS 15), 2002)

- Empirical Guidance on Scatterplot and Dimension Reduction Technique Choices (M. Sedlmair et al., IEEE Transactions on Visualization and Computer Graphics, 2013)
- Information retrieval perspective to nonlinear dimensionality reduction for data visualization (J. V enna et al., UNKNOWN, 2010)
- Uniform manifold approximation with two-phase optimization (H. Jeon et al., 2022 IEEE Visualization and Visual Analytics (VIS), 2022)
- Feature Learning for Nonlinear Dimensionality Reduction toward Maximal Extraction of Hidden Patterns (Takanori Fujiwara et al., 2023 IEEE 16th Pacific Visualization Symposium (PacificVis), 2023)
- VisCoDeR: A tool for visually comparing dimensionality reduction algorithms (René Cutura et al., UNKNOWN, 2018)
- UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction (Leland McInnes et al., Journal of Open Source Software, 2020)
- Stability Comparison of Dimensionality Reduction Techniques Attending to Data and Parameter Variations (Francisco J. García-Fernández et al., UNKNOWN, 2013)
- Dimensionality reduction for visualizing single-cell data using UMAP (E. Becht et al, Nature Biotechnology, 2019)
