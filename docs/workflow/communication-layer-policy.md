# Communication Layer Policy

Use two outputs for each analysis run:
1. Internal technical record (for audit and reproducibility)
2. User-facing answer (for analysts)

Related:
- Workflow: [`docs/workflow/dr-analysis-workflow.md`](./dr-analysis-workflow.md)
- Report contract: [`docs/workflow/reliability-report-contract.md`](./reliability-report-contract.md)

## User-Facing Answer: Writing Rules
- Use plain words and short sentences.
- Explain: what was compared, what was selected, why it fits the goal, and what risk remains.
- Show final settings in a copyable form.
- Do not expose internal key names or policy labels.

## User-Facing Answer: Word Choice
Use these preferred words:
- `main goal`
- `reliability checks`
- `safety check`
- `same data preparation`

Avoid internal wording in user output. Examples:
- Bad: `task axis`, `metric bundle`, `warning gate`
- Good: `main goal`, `reliability checks`, `safety check`

## User-Facing Code Rule
User code must be practical analysis code, not policy scaffolding.

Required pattern:
- selected DR library fit step
- `bayes_opt` for tuning
- `zadu` for reliability scoring

Code quality constraints:
- minimal runnable snippet (target: <= 35 non-empty lines)
- no internal policy objects or key-like variables
- comments explain practical intent, not internal workflow terms

## Minimum User Answer Structure
1. `What you asked`
2. `What we compared`
3. `What we selected and why`
4. `Final settings`
5. `Risk note`
6. `Concise code`
7. `Why this code`

## Enforcement
- Use `scripts/validate_user_explanation_text.py` for user-language leakage checks.
- Use `scripts/validate_reliability_report.py` when a report artifact is produced.
