# Quick Answer Mode

Use this page to keep user-facing DR answers helpful, concise, and actionable.

Related:
- Communication policy: [`docs/workflow/communication-layer-policy.md`](./communication-layer-policy.md)
- Report contract: [`docs/workflow/reliability-report-contract.md`](./reliability-report-contract.md)
- Workflow anchor: [`docs/workflow/dr-analysis-workflow.md`](./dr-analysis-workflow.md)

## Purpose
When users ask practical DR questions, answer in a way that is:
- easy to understand for non-specialists,
- short enough to execute quickly,
- explicit about final settings and residual risk.

## Depth Selection Rule
Choose depth by user intent:
- Simple request:
  - one short clarification question if needed,
  - one direct recommendation,
  - one concise code snippet,
  - no detailed rationale unless the user asks why.
- Comparative request:
  - brief comparison of candidates,
  - final selection,
  - final settings and one concise code path.
- Research/deep request:
  - structured explanation,
  - references only when asked,
  - still keep code minimal and runnable.

## Default Required User-Facing Blocks
Always include:
1. What you understood
2. What you selected
3. Final settings
4. Risk note
5. Concise runnable code

## On-Request Blocks
Add these only when explicitly requested:
- What was compared (for comparative or best/optimal questions)
- Why this selection fits the goal
- Why this code is structured this way
- Paper references

## Wording Rule
Prefer:
- `main goal`
- `reliability checks`
- `final settings`
- `remaining risk`

Avoid:
- internal workflow labels
- mapping-table prose
- platform/internal interface references

## Code Simplicity Rule
User-facing code should be:
- one preprocessing block,
- one embedding function,
- one `bayes_opt` objective,
- one `zadu` reliability call,
- one final run with selected parameters.

Code should not include:
- policy bookkeeping objects,
- internal key-like variable names,
- extra orchestration layers not needed to run.

## Example (Class Relationship Request)
User request:
- "I want to inspect class relationships in MNIST."

Good concise answer shape:
- Clarify that the main goal is class relationship inspection.
- Explain that a global-distance-preserving baseline and one local method are compared under the same preprocessing.
- State final settings explicitly.

Minimal code shape:
```python
import numpy as np
from bayes_opt import BayesianOptimization
from zadu import ZADU
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

X = ...  # features
X = StandardScaler().fit_transform(X)

def score(z):
    spec = [{"id": "stress", "params": {}}]
    out = ZADU(spec, X).measure(z)[0]
    return float(np.mean([v for v in out.values() if isinstance(v, (int, float))]))

def embed(n_components):
    return PCA(n_components=int(round(n_components))).fit_transform(X)

def objective(n_components):
    return score(embed(n_components))

opt = BayesianOptimization(f=objective, pbounds={"n_components": (2, 20)}, random_state=7, verbose=0)
opt.maximize(init_points=4, n_iter=16)
Z_best = embed(**opt.max["params"])
```

## Reference Rule
If the user asks for sources:
- cite papers (title, authors, venue, year, URL),
- do not cite internal files or repository paths.
