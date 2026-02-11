# Task-Aligned Initialization Rules

Use this page to choose initialization strategy after candidate selection and before Bayesian tuning.

Related:
- Workflow anchor: [`docs/workflow/dr-analysis-workflow.md`](./dr-analysis-workflow.md)
- Selection policy: [`docs/workflow/configuration-selection-policy.md`](./configuration-selection-policy.md)
- Technique details: [`docs/techniques/README.md`](../techniques/README.md)

## Required Inputs
- confirmed main goal
- selected method candidate
- selected reliability checks
- data constraints
- fixed preprocessing setup

## Method Groups
### Group A: Stochastic methods sensitive to initialization
Examples:
- t-SNE, UMAP, SNE, TriMap, PaCMAP, UMATO, catSNE, ClassNeRV, Classimap

Default policy:
- use informative initialization as default
- use random initialization for comparison, not as production default

### Group B: Graph/manifold methods with optional initialization choices
Examples:
- Isomap, S-Isomap, LLE, Laplacian Eigenmaps, LMDS, LAMP, PLMP, LSP

Default policy:
- use deterministic or graph-consistent informative initialization when available
- keep graph construction settings fixed while comparing initialization choices

### Group C: Deterministic or initialization-light methods
Examples:
- PCA and most direct linear transforms

Default policy:
- initialization is usually not a decision variable
- document that initialization had no meaningful effect

## Goal-Sensitive Guidance
### Global-structure goals
- point distance investigation
- class separability investigation
- cluster distance investigation
- cluster density investigation

Guidance:
- informative initialization is strongly preferred for stochastic methods
- random-only evidence is insufficient for final production recommendation

### Local-structure goals
- neighborhood identification
- outlier identification
- cluster identification

Guidance:
- informative initialization remains default for reproducibility
- random restarts are useful as variability probes

## Mandatory Comparison Protocol
When initialization can change outcomes:
1. keep all non-initialization settings fixed
2. compare at least two initialization choices when supported
3. evaluate each choice with at least three seeds
4. report both score consistency and visual consistency

## Stability Threshold
- stable: top candidate remains unchanged in at least 80% of seed runs
- unstable: top candidate flips in more than 20% of seed runs

If unstable:
- downgrade confidence level
- keep at least one fallback configuration

## Internal Record Schema
Technical field names are maintained in:
- [`builder/evidence/internal-report-schema.md`](../../builder/evidence/internal-report-schema.md)
