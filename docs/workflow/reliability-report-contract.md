# Reliability Report Contract

Use this contract to keep DR recommendations reproducible while keeping user output easy to read.

Related:
- Workflow: [`docs/workflow/dr-analysis-workflow.md`](./dr-analysis-workflow.md)
- Communication policy: [`docs/workflow/communication-layer-policy.md`](./communication-layer-policy.md)
- Quick answer mode: [`docs/workflow/quick-answer-mode.md`](./quick-answer-mode.md)

## Two Output Layers
Every run should produce:
1. technical record for audit and reproducibility
2. user-facing answer in plain language

User-facing answers must not expose internal field names.
Detailed rationale can stay in the technical record and be shown in user-facing text when the user asks why.

## User-Facing Answer Structure
Default:
1. What you asked
2. What we selected
3. Final settings you can reuse
4. Risk note
5. Concise code

On request:
1. What we compared (for comparative or best/optimal questions)
2. Why this selection fits the goal
3. Why this code

## User-Layer Constraints
- plain language for DR novices
- no internal workflow labels
- no metric ID shorthand in prose
- no key/value mapping-table prose in user explanations
- no popularity-only method rationale
- if references are requested, cite papers (title, authors, venue, year, URL)
- do not cite internal files as user references

## User Code Contract
Code must include:
- selected DR library fit step
- `bayes_opt` tuning
- `zadu` reliability scoring

Code must also:
- stay minimal (target: <= 25 non-empty lines)
- avoid internal-policy variable names
- avoid internal jargon in comments

If `bayes_opt` is unavailable:
- mark output as `BLOCKED: bayes_opt unavailable`
- include concrete fix command(s)
- do not provide fallback recommendations using grid/random/manual sweep

## Final Settings Disclosure
Always include:
- method
- optimizer (`bayes_opt`)
- selected implementation library
- implementation links (official API, GitHub, PyPI when available)
- key hyperparameters
- preprocessing summary
- initialization summary
- reproducibility summary

## Internal Record Schema
Technical field names are maintained in:
- [`builder/evidence/internal-report-schema.md`](../../builder/evidence/internal-report-schema.md)
