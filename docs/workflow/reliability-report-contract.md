# Reliability Report Contract

Use this contract to keep DR recommendations reproducible while keeping user output simple.

Related:
- Workflow: [`docs/workflow/dr-analysis-workflow.md`](./dr-analysis-workflow.md)
- Communication policy: [`docs/workflow/communication-layer-policy.md`](./communication-layer-policy.md)
- Validator: `scripts/validate_reliability_report.py`

## Output Split (Mandatory)
Every run has two artifacts:
1. Internal report artifact (technical, for audit/validation)
2. User-facing answer (plain language, concise code)

The user-facing answer must not expose internal report keys.

## Internal Report Artifact Rule
- Must satisfy `scripts/validate_reliability_report.py`.
- Optimizer must be `bayes_opt`.
- Non-`bayes_opt` optimization (`grid search`, `random search`, sweep loops) is invalid.

## User-Facing Answer Rule
Required content:
1. `What you asked`
2. `What we tested`
3. `What we found`
4. `Why this is reliable enough`
5. `Final settings you can reuse`
6. `Concise code`
7. `Why this code`

User wording constraints:
- plain language for DR novices
- no internal workflow vocabulary
- no metric abbreviations in explanation text; use full names

## User Code Contract
User code must include all three:
- selected DR library call (fit step)
- `bayes_opt` tuning block
- `zadu` reliability scoring block

User code must also:
- be minimal (target: <= 35 non-empty lines)
- avoid internal-policy variable names/dictionaries
- avoid internal jargon in comments

## Final Settings Disclosure (Mandatory)
Include a compact section with:
- `method`
- `key_hyperparameters`
- `preprocessing_summary`
- `initialization_summary`
- `reproducibility_summary`

## User-Facing Example Template
```text
What you asked:
- You want to compare class relationships in 2D.

What we tested:
- We compared a few DR methods with the same data preparation.
- We checked neighborhood and distance reliability scores.

What we found:
- Method A gave the most stable class relationship pattern across repeated runs.

Why this is reliable enough:
- The result stayed consistent across repeated runs.
- Reliability checks were better than alternatives.
- Risk: nearby classes may still overlap in 2D.

Final settings you can reuse:
- method: <selected_method>
- key_hyperparameters: {...}
- preprocessing_summary: <...>
- initialization_summary: <...>
- reproducibility_summary: <...>

Concise code:
- selected DR method + bayes_opt + zadu

Why this code:
- Short, reproducible, and aligned with your goal.
```

## Completion Checklist
1. Internal artifact passes validator.
2. User answer uses plain language.
3. User code includes DR fit + `bayes_opt` + `zadu`.
4. User code is minimal and practical.
5. Final settings are explicitly disclosed.
