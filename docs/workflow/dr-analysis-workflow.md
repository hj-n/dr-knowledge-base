# DR Analysis Workflow

Use this sequence as the default execution order for reliable DR configuration.

## Step Map
1. Confirm the main analysis goal:
   [`docs/intake-question-tree.md`](../intake-question-tree.md),
   [`docs/workflow/task-confirmation-protocol.md`](./task-confirmation-protocol.md)
2. Audit data and keep one preprocessing policy:
   [`docs/workflow/preprocessing-profiles.md`](./preprocessing-profiles.md)
3. Build goal-aligned method and reliability-check candidates:
   [`docs/metrics-and-libraries.md`](../metrics-and-libraries.md),
   [`docs/metrics/README.md`](../metrics/README.md),
   [`docs/techniques/README.md`](../techniques/README.md),
   [`docs/execution-library-index.md`](../execution-library-index.md)
   -> after one method is selected, execute from its technique page execution card
   (for example `docs/techniques/umap.md` or `docs/techniques/pca.md`)
4. Rank candidates with one deterministic policy:
   [`docs/workflow/configuration-selection-policy.md`](./configuration-selection-policy.md),
   [`docs/reference-coverage.md`](../reference-coverage.md)
5. Decide initialization strategy:
   [`docs/workflow/task-aligned-initialization.md`](./task-aligned-initialization.md)
6. Tune with Bayesian optimization:
   [`docs/workflow/hyperparameter-optimization-protocol.md`](./hyperparameter-optimization-protocol.md),
   [`docs/workflow/bayesian-optimization-reference.md`](./bayesian-optimization-reference.md)
7. Visualize and explain results:
   [`docs/workflow/visualization-policy.md`](./visualization-policy.md),
   [`docs/workflow/communication-layer-policy.md`](./communication-layer-policy.md),
   [`docs/workflow/quick-answer-mode.md`](./quick-answer-mode.md),
   [`docs/workflow/reliability-report-contract.md`](./reliability-report-contract.md)

## 1) Confirm the main goal
- Start with one plain-language question.
- If ambiguous, ask one clarification question at a time.
- Confirm one goal before discussing methods.

Gate:
- Do not continue until goal confidence is high.

## 2) Data audit and preprocessing
- Check shape, missing values, sparsity, scale, and label quality.
- Choose one preprocessing setup and keep it fixed during comparison.
- Keep one distance definition fixed during comparison.

Gate:
- Do not compare methods under mixed preprocessing setups.

## 3) Candidate generation
- Build candidates aligned to the confirmed goal.
- Include both method candidates and reliability-check candidates.
- If labels are used, run a label-separation check first.
- As soon as one candidate is chosen for implementation, move to that file in
  `docs/techniques/` and use its execution card sections:
  - `Implementation Options`
  - `Recommended Library`
  - `Official API / GitHub / PyPI Links`
  - `Minimal Runnable Snippet`

Best/optimal mode:
- compare all aligned candidates before pruning
- prune only when hard failures are explicit and recorded

Gate:
- If label separation is weak or unknown, do not rely only on label-aware checks.

## 4) Deterministic selection
- Apply hard filters first.
- Score remaining candidates with the fixed policy.
- Keep tie handling explicit.

Gate:
- If no candidate passes acceptance rules, mark recommendation as provisional or exploratory.

## 5) Initialization decision
- Decide initialization after candidate selection.
- For initialization-sensitive methods, compare at least one informative and one neutral option.
- Record stability implications.

Gate:
- Do not start tuning before initialization strategy is fixed.

## 6) Bayesian hyperparameter optimization
- Use `bayes_opt` only.
- Tune under fixed preprocessing and initialization.
- Check stability across repeated seeds for top candidates.
- Use the canonical code pattern and metadata-aligned range table from:
  [`docs/workflow/bayesian-optimization-reference.md`](./bayesian-optimization-reference.md)

Gate:
- Do not replace Bayesian optimization with grid search, random search, or manual sweeps.

## 7) Visualization and explanation
- Produce visual artifacts that match the selected goal.
- Provide two layers of explanation:
  - technical record for audit
  - plain-language explanation for end users
- Always disclose final method and key settings.
- Keep default user answers concise; provide detailed rationale only when the user asks why.
- If references are requested, cite papers, not internal files.

Gate:
- If evidence conflicts materially, downgrade confidence and state residual risk.

## Internal Record Schema
Technical field names are maintained in:
- [`builder/evidence/internal-report-schema.md`](../../builder/evidence/internal-report-schema.md)

User-facing answers must not expose internal field names.
