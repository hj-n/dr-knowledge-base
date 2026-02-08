# Visualization Policy

Use this policy to communicate DR outcomes without overstating reliability.
This page defines current minimum rules only. Additional paper-backed visualization rules can be added later.

Related:
- Workflow anchor: [`docs/workflow/dr-analysis-workflow.md`](./dr-analysis-workflow.md)
- Reliability report contract: [`docs/workflow/reliability-report-contract.md`](./reliability-report-contract.md)

## Current Minimum Rules
- Keep visualization in 2D unless a paper-backed rule explicitly approves another mode for the same task.
- Treat axes as embedding coordinates, not semantic feature axes.
- Report visualization as supportive evidence, not sole decision evidence.

## Required Visual Artifacts
Provide at least two artifacts:
1. final selected embedding with key annotations
2. comparison artifact (alternative method, seed, or initialization)

## Annotation Contract
Each artifact must include:
- `method` and key hyperparameters
- initialization method
- seed (for stochastic methods)
- metric bundle summary
- explicit caveat note

## Reliability Guardrails
- If comparison artifact contradicts the selected narrative, mark recommendation status as `provisional` or `exploratory`.
- Do not remove contradictory visual evidence from the report.

## Output Contract
Step 6 must output:
- `visual_artifacts`
- `visual_notes`
- `visual_consistency_check`
