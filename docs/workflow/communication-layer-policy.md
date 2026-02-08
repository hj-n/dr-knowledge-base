# Communication Layer Policy

Use two separate explanation layers in every final DR report.

Related:
- Workflow: [`docs/workflow/dr-analysis-workflow.md`](./dr-analysis-workflow.md)
- Final report contract: [`docs/workflow/reliability-report-contract.md`](./reliability-report-contract.md)

## Layer A: Internal Technical Record (Builder-facing)
Purpose:
- Preserve full technical detail for implementation, debugging, and audit.

Allowed content:
- technical keys such as task axis, metric bundle, warning gate, score table, and initialization stability.
- formulas, thresholds, and protocol details.

Audience:
- engineers and agents implementing DR code.

## Layer B: User Explanation (End-user-facing)
Purpose:
- Explain the decision so a DR novice with basic CS background can understand and act.

Required style:
- short sentences and concrete wording.
- explain what was done, why it matters, and what remains uncertain.
- always show final settings in copyable form.
- provide a concise runnable code snippet plus a short explanation of why this code was selected.

Forbidden standalone jargon in user layer:
- `task axis`
- `metric bundle`
- `warning gate`
- `preprocessing signature`
- `guardrail metric`
- `candidate score table`
- `selection_status`
- `axis_confidence`

If a technical term is unavoidable:
- use `term (plain meaning: ...)` once, then continue with plain words.

## Term Mapping Guide
- `task axis` -> `main analysis goal`
- `metric bundle` -> `set of quality checks`
- `warning gate` -> `safety check`
- `preprocessing signature` -> `same data preparation rules`
- `guardrail metric` -> `secondary safety-check score`
- `initialization stability` -> `whether repeated runs give similar conclusions`

## Minimum User Explanation Structure
1. `What you asked`
2. `What we compared`
3. `What we selected and why`
4. `Final settings you can reuse`
5. `What could still go wrong`

## User Deliverable Contract (Mandatory)
Every user-facing final answer must include both:
1. `Concise code`:
   - minimal runnable snippet focused on the chosen configuration
   - avoid exposing internal policy plumbing in user code
2. `Why this code`:
   - 3-5 short bullets explaining why the selected code matches the user's goal
   - include one line on residual risk
