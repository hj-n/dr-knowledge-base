# Communication Layer Policy

Use two outputs for each analysis run:
1. Internal technical record (for audit and reproducibility)
2. User-facing answer (for analysts)

Related:
- Workflow: [`docs/workflow/dr-analysis-workflow.md`](./dr-analysis-workflow.md)
- Quick answer mode: [`docs/workflow/quick-answer-mode.md`](./quick-answer-mode.md)
- Report contract: [`docs/workflow/reliability-report-contract.md`](./reliability-report-contract.md)
- Canonical Bayesian optimization code: [`docs/workflow/bayesian-optimization-reference.md`](./bayesian-optimization-reference.md)

## User-Facing Answer: Writing Rules
- Use plain words and short sentences.
- Explain default essentials first: what was selected, final settings, and remaining risk.
- Provide detailed "why" rationale only when the user explicitly asks why.
- Show final settings in a copyable form.
- Do not expose internal key names or policy labels.
- Do not justify selection with popularity-only wording (for example: "commonly used", "standard default") without task-fit and reliability evidence.
- Match response length to question complexity.
  - For simple questions: answer briefly first, then add only essential details.
  - For complex requests: provide structured detail, but avoid unnecessary expansion.
- Do not introduce supervised or label-dependent methods unless the user explicitly confirmed a class-separability goal.
- When the user asks for references/evidence:
  - cite papers (title, authors, venue, year) as the reference unit.
  - include DOI/arXiv/open-access URL when available.
  - do not cite internal knowledge files or repository paths.
- When the user asks how to run the selected technique:
  - provide implementation links from official API docs, GitHub, and PyPI.
  - keep method-justification references separate and paper-based.

## User-Facing Answer: Word Choice
Use these preferred words:
- `main goal`
- `reliability checks`
- `safety check`
- `same data preparation`

Avoid internal wording in user output. Examples:
- Bad: `goal category label`, `reliability check set`, `label-separation check state`, `safety check objective`
- Good: `main goal`, `reliability checks`, `safety check`

## Narrative Rewrite Rule (User Layer)
- Do not describe recommendations as internal mapping entries.
- Avoid key/value-style phrasing such as:
  - internal mapping-table wording
  - assignment-like table wording
  - JSON-like arrays in prose
- Rewrite into natural language:
  - good style example:
    - `For cluster-density analysis, methods and reliability checks that preserve distance and density structure are usually a better fit, such as Stress and Kullback-Leibler Divergence.`
  - then list paper references as bibliography entries.

## User-Facing Code Rule
User code must be practical analysis code, not policy scaffolding.

Required pattern:
- selected DR library fit step
- `bayes_opt` for tuning
- `zadu` for reliability scoring

Code quality constraints:
- minimal runnable snippet (target: <= 25 non-empty lines)
- no internal policy objects or key-like variables
- comments explain practical intent, not internal workflow terms
- if `bayes_opt` cannot run, return `BLOCKED` with the exact fix command; do not provide grid/random/manual-sweep fallback code

## Minimum User Answer Structure
Default:
1. `What you asked`
2. `What we selected`
3. `Final settings`
4. `Risk note`
5. `Concise code`

On request:
1. `What we compared` (for comparative or best/optimal questions)
2. `Why this selection`
3. `Why this code`

## Reference Citation Rule (User Layer)
- If the user asks "what is the source?" or "give references", return paper citations only.
- Do not present internal source locations as user references.
- Internal traceability can remain in technical records, but user-facing references must be paper-level bibliographic citations.

## Implementation Link Rule (User Layer)
- If the user asks for setup or runnable code details, include:
  - official API documentation link
  - GitHub repository link
  - PyPI package link (when available)
- Do not mix these implementation links with paper references in one list.

## Enforcement
- Use `scripts/validate_user_explanation_text.py` for user-language leakage checks.
- Use `scripts/validate_reliability_report.py` when a report artifact is produced.
- Treat over-verbose responses to simple question-like prompts as rewrite warnings, not automatic failures.
