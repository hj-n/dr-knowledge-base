# Reliability Report Contract

Use this contract to keep DR recommendations reproducible while keeping user output easy to read.

Related:
- Workflow: [`docs/workflow/dr-analysis-workflow.md`](./dr-analysis-workflow.md)
- Communication policy: [`docs/workflow/communication-layer-policy.md`](./communication-layer-policy.md)

## Two Output Layers
Every run should produce:
1. technical record for audit and reproducibility
2. user-facing answer in plain language

User-facing answers must not expose internal field names.

## User-Facing Answer Structure
1. What you asked
2. What we compared
3. What we selected and why
4. Final settings you can reuse
5. Risk note
6. Concise code
7. Why this code

## User-Layer Constraints
- plain language for DR novices
- no internal workflow labels
- no metric ID shorthand in prose
- no key/value mapping-table prose in user explanations
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

## Final Settings Disclosure
Always include:
- method
- selected implementation library
- implementation links (official API, GitHub, PyPI when available)
- key hyperparameters
- preprocessing summary
- initialization summary
- reproducibility summary

## Internal Record Schema
Technical field names are maintained in:
- [`builder/evidence/internal-report-schema.md`](../../builder/evidence/internal-report-schema.md)
