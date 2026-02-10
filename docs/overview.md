# Overview

## Goal
Enable an LLM to do three things reliably:
1. identify and confirm the user's main DR goal from plain-language input,
2. generate a high-quality task-aligned configuration,
3. explain the decision with explicit evidence and residual risk.

## Core Axis
This KB uses a fixed 7-goal taxonomy:
- Neighborhood identification
- Outlier identification
- Cluster identification
- Point distance investigation
- Class separability investigation
- Cluster distance investigation
- Cluster density investigation

Subtask refinement is allowed but never replaces the primary axis.
See: [`docs/task-taxonomy.md`](./task-taxonomy.md)

## Primary Navigation
- Workflow: [`docs/workflow/dr-analysis-workflow.md`](./workflow/dr-analysis-workflow.md)
- Task confirmation protocol: [`docs/workflow/task-confirmation-protocol.md`](./workflow/task-confirmation-protocol.md)
- Preprocessing profiles: [`docs/workflow/preprocessing-profiles.md`](./workflow/preprocessing-profiles.md)
- Selection scoring policy: [`docs/workflow/configuration-selection-policy.md`](./workflow/configuration-selection-policy.md)
- Initialization rules: [`docs/workflow/task-aligned-initialization.md`](./workflow/task-aligned-initialization.md)
- Hyperparameter optimization protocol: [`docs/workflow/hyperparameter-optimization-protocol.md`](./workflow/hyperparameter-optimization-protocol.md)
- Visualization policy: [`docs/workflow/visualization-policy.md`](./workflow/visualization-policy.md)
- Communication layer policy: [`docs/workflow/communication-layer-policy.md`](./workflow/communication-layer-policy.md)
- Report contract: [`docs/workflow/reliability-report-contract.md`](./workflow/reliability-report-contract.md)
- Metric/technique policy: [`docs/metrics-and-libraries.md`](./metrics-and-libraries.md)
- Reliability cautions: [`docs/reliability-cautions-and-tips.md`](./reliability-cautions-and-tips.md)
- Coverage ranking: [`docs/reference-coverage.md`](./reference-coverage.md)
- Paper catalog guide: [`docs/paper-catalog.md`](./paper-catalog.md)
- Paper list (CSV): [`docs/paper-catalog.csv`](./paper-catalog.csv)

## Drill-Down Path
1. Confirm task:
   [`docs/intake-question-tree.md`](./intake-question-tree.md) +
   [`docs/workflow/task-confirmation-protocol.md`](./workflow/task-confirmation-protocol.md)
2. Freeze preprocessing:
   [`docs/workflow/preprocessing-profiles.md`](./workflow/preprocessing-profiles.md)
3. Select candidates:
   [`docs/metrics-and-libraries.md`](./metrics-and-libraries.md)
4. Score and decide:
   [`docs/workflow/configuration-selection-policy.md`](./workflow/configuration-selection-policy.md)
5. Set initialization:
   [`docs/workflow/task-aligned-initialization.md`](./workflow/task-aligned-initialization.md)
6. Optimize and stress-test:
   [`docs/workflow/hyperparameter-optimization-protocol.md`](./workflow/hyperparameter-optimization-protocol.md)
7. Visualize safely:
   [`docs/workflow/visualization-policy.md`](./workflow/visualization-policy.md)
8. Split explanation layers:
   [`docs/workflow/communication-layer-policy.md`](./workflow/communication-layer-policy.md)
9. Deliver explanation contract:
   [`docs/workflow/reliability-report-contract.md`](./workflow/reliability-report-contract.md)

## Non-Negotiable Rules
- Task-first: no recommendation before task is confirmed with high confidence.
- Deterministic decisioning: use the scoring policy, not ad-hoc preference.
- Evidence-first explanation: every final claim must map to source notes.
- Dual-layer communication: keep a technical layer for implementation and a separate novice-friendly user layer.
- Final-configuration disclosure: always show users the exact final method and key parameter settings.
- User-facing language must be simple: assume the user is not a DR expert.
- User-facing code must be concise: show a minimal runnable path, not orchestration internals.
- Hyperparameter tuning policy is fixed: use Bayesian optimization (`bayes_opt`) only.
- Do not use grid search, random search, or manual sweep loops for final recommendations.
- Do not expose internal policy wiring in user outputs (for example task-routing tables, label-separation check state keys, or internal scoring keys).
- Do not use metric abbreviations in user explanation (for example `tnc`, `nh`, `nd`); use full names.
- Do not expose platform or internal interface names in user explanation.
- Do not use internal workflow labels in user explanation; always rewrite into plain language.
- If references are requested, cite papers (title/authors/venue/year), not internal KB files or repo links.
- Prefer plain user wording:
  - say `main goal`
  - say `reliability checks`
  - say `confirm the goal`
  - say `scored for reliability`

## User-Facing Output Standard
Every final user answer should satisfy all three:
1. Easy explanation:
   - short sentences, plain words, no internal jargon as standalone terms.
2. Simple code:
   - minimal runnable snippet focused on the selected method/configuration.
3. Hidden internals:
   - internal selection logic and policy keys stay in technical records, not in user snippet.

If any of these fail, treat the output as incomplete and revise before finalizing.
