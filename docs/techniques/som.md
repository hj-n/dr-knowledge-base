# SOM (Self-Organizing Map)

## Technique Summary
Topology-preserving map projection emphasizing neighborhood-order structure.

In practice, the technique description is intentionally task-centered: the method is not automatically good, and is only appropriate when its distortion profile matches the analytical objective. That framing keeps method choice aligned with user intent instead of popularity.

The summary should be read together with task alignment and tradeoff sections before implementation. When the same dataset supports multiple objectives, this technique may be suitable for one objective and unsuitable for another.

## I/O Contract
- Input: general high-dimensional feature data (labels optional for supervised variants).
- Output: low-dimensional projection coordinates for analysis/visualization.

Input should be treated as a high-dimensional feature representation after data-audit and preprocessing decisions are locked. If normalization, distance definition, or label usage changes during tuning, the effective input contract changes as well and comparisons become noisy.

Output coordinates are analysis artifacts, not ground-truth geometry. They should be consumed according to the declared task, with explicit caution against over-interpreting axes, absolute distances, or visual separations outside the validated use case.

## Core Objective
Map high-dimensional data to low-dimensional grid/space while preserving neighborhood topology.

The objective function encodes which structural errors are cheap and which are expensive. Understanding that objective is essential because it predicts the kinds of distortions the method will tolerate when perfect preservation is impossible.

Method selection should therefore ask which distortions are acceptable for this task, and which are not. Choose this technique only when its objective-level priorities match that answer.

## Computation Outline
- Initialize map/codebook structure.
- Iteratively update codebook units with neighborhood cooperation.
- Project points to map positions and evaluate topology preservation.

Implementation quality depends on stable preprocessing, deterministic settings where possible, and explicit recording of optimization configuration. Most DR pipelines are sensitive to initialization or neighborhood construction choices, so hidden defaults can change conclusions.

For reproducible comparison, evaluate this technique under a fixed protocol and report parameter context with results. This converts the outline from a conceptual recipe into an auditable procedure for downstream agents and reviewers.

Detailed execution rule: keep map/grid configuration and neighborhood-decay schedule explicit. Prototype-map methods can tell very different stories under different grid designs.

## Hyperparameter Impact
- Map dimensionality/resolution controls topological detail and distortion patterns.
- Neighborhood-update schedule controls training dynamics and smoothness.

Hyperparameters determine the local-vs-global balance, optimization stability, and visual behavior of the embedding. They should be tuned against task-aligned metrics rather than aesthetics alone, especially when outputs influence model or policy decisions.

A practical default is Bayesian optimization with safety checks: fixed seed schedule, bounded search space, and multi-metric objective checks. This reduces manual trial-and-error while preserving traceability for why a specific configuration was selected.

Decision-level tuning rule: report both best score and stability behavior (seed variance / restart variance). A configuration that wins once but is unstable should not be the default recommendation.

## Practical Reliability Notes
SOM provides topology-aware organization that is useful for exploratory structure discovery and prototype-level interpretation. It can be effective when analysts need interpretable map organization rather than only scatterplot geometry.

SOM reliability depends on grid design, learning schedule, and neighborhood-decay policy. Treat these as task-level decisions and validate with external metrics; otherwise map aesthetics can be mistaken for trustworthy structure preservation.

## Notable Properties
- Strong topology-oriented interpretability in neighborhood terms.
- Topographic diagnostics provide explicit order-preservation signal.

Notable properties should be interpreted as operating characteristics, not guarantees. A property that is beneficial in one data regime can become a liability in another regime with different density, noise level, or manifold complexity.

Use these properties to narrow candidates early, then confirm with metric evidence and task-specific validation. That sequence keeps the workflow grounded in evidence instead of anecdotal method reputation.

## Strengths
This technique is strong for topology-preserving map organization and neighborhood structure visualization. It is useful for structured map-based exploration where adjacency preservation is important.

It can provide interpretable map topology diagnostics beyond pure scatter-style embeddings.


## Task Alignment
- Inferred alignment: best-aligned tasks
  - Neighborhood identification
  - Cluster identification
  - Outlier identification

Task alignment indicates where this technique is expected to provide the most reliable utility under the current evidence base. Treat non-listed tasks as unsupported until new source-backed evidence is added.

When a project requires multiple task outcomes, combine this section with metric-level alignment and require agreement across both layers. If technique and metric recommendations diverge, collect more evidence before production use.

Operational alignment rule: method alignment should constrain candidate ranking, but final acceptance still requires agreement with task-aligned reliability check sets and label-separation check status.

## Known Tradeoffs
- Topology preservation does not guarantee metric distance preservation.

Tradeoffs are expected and should be made explicit to users before final selection. A method that improves neighborhood fidelity may worsen global distance faithfulness, and vice versa, so optimization must reflect the task hierarchy.

In reporting, document which tradeoffs were accepted and why they were acceptable for the chosen task. This explanation step is part of the contract for trustworthy DR recommendations in this guide.

Communication rule: document one concrete downside that remained after tuning (for example global drift, local fragmentation, or runtime burden) so end users understand residual risk.

## Implementation Options
The default execution path uses the mapped primary Python implementation for this technique. Implementation mode: `direct`. Primary status: `watch`.

Use the primary path when it is `active` or `watch`. If it is `risk`, execute the fallback path and keep the recommendation confidence conservative.

## Recommended Library
Recommended library: **MiniSom**.

Current maintenance snapshot: **watch** (checked on 2026-02-11). This status is generated from the automated maintenance snapshot using the documented maintenance policy.

## Official API / GitHub / PyPI Links
Primary path links:
- Official API: [https://github.com/JustGlowing/minisom](https://github.com/JustGlowing/minisom)
- GitHub: [https://github.com/JustGlowing/minisom](https://github.com/JustGlowing/minisom)
- PyPI: [https://pypi.org/project/minisom/](https://pypi.org/project/minisom/)

Fallback path links:
- Official API: [https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)
- GitHub: [https://github.com/scikit-learn/scikit-learn](https://github.com/scikit-learn/scikit-learn)
- PyPI: [https://pypi.org/project/scikit-learn/](https://pypi.org/project/scikit-learn/)

## Minimal Python API Pattern
```python
from minisom import MiniSom
som = MiniSom(x=30, y=30, input_len=X.shape[1], sigma=1.0, learning_rate=0.5, random_seed=7)
som.train_random(X, 2000)
Z = np.array([som.winner(xi) for xi in X], dtype=float)
```

## Key Parameters for Bayesian Optimization
- `sigma`: neighborhood radius in SOM training.
- `learning_rate`: adaptation speed.
- `train_steps`: number of random training updates.

Search bounds used in the minimal snippet:
- `{"sigma": (0.3, 3.0), "learning_rate": (0.05, 1.0), "train_steps": (500, 5000)}`

## Initialization in Practice
SOM starts from random prototype vectors. Keep random seed fixed during tuning and evaluate robustness with extra seeds.

## Runtime and Memory Notes
Training cost depends on grid size and train steps. Large grids can increase runtime without proportional analytic gains.

## Common Failure Signs and Fixes
- Projection heavily depends on one random seed -> run additional seeds and report spread.
- Map folding in dense regions -> tune sigma and train steps together.
- Weak class organization -> adjust grid resolution or compare with manifold methods.

## Minimal Runnable Snippet
```python
import numpy as np
from bayes_opt import BayesianOptimization
from zadu import ZADU
from minisom import MiniSom

X = ...  # shape: (n_samples, n_features)

def zadu_score(hd, ld):
    spec = [{"id": "tnc", "params": {"k": 20}}]
    result = ZADU(spec, hd).measure(ld)[0]
    vals = [float(v) for v in result.values() if isinstance(v, (int, float))]
    return float(np.mean(vals))

def embed(sigma, learning_rate, train_steps):
    som = MiniSom(x=30, y=30, input_len=X.shape[1], sigma=float(sigma), learning_rate=float(learning_rate), random_seed=7)
    som.train_random(X, int(round(train_steps)))
    z = np.array([som.winner(xi) for xi in X], dtype=float)
    z -= z.mean(axis=0, keepdims=True)
    z /= z.std(axis=0, keepdims=True) + 1e-9
    return z

def objective(*args, **kwargs):
    z = embed(*args, **kwargs)
    return zadu_score(X, z)

optimizer = BayesianOptimization(f=objective, pbounds={"sigma": (0.3, 3.0), "learning_rate": (0.05, 1.0), "train_steps": (500, 5000)}, random_state=7, verbose=0)
optimizer.maximize(init_points=4, n_iter=16)
Z_best = embed(**optimizer.max["params"])
```

## Source Notes
- Quantifying the Neighborhood Preservation of Self-Organizing Feature Maps (of Self/-Organizing F eature Maps, IEEE Transactions on Neural Networks, 1992)
- Quality assessment of dimensionality reduction: Rank-based criteria (John A. Lee et al., Neurocomputing, 2009)

- ClassiMap: A new dimension reduction technique for exploratory data analysis of labeled data (S. Lespinats et al., International Journal of Pattern Recognition and Artificial Intelligence, 2015)
- Trustworthiness and metrics in visualizing similarity of gene expression (S. Kaski et al., BMC Bioinformatics, 2003)
- A methodology to compare Dimensionality Reduction algorithms in terms of loss of quality (A. Gracia et al., Information Sciences, 2014)
- Survey and comparison of quality measures for selforganizing maps (G. P €olzlbauer, Annals of Data Science, 2004)
- Nonlinear Dimensionality Reduction and Manifold Learning (A. Wism €uller et al., Springer Texts in Statistics, 2010)
