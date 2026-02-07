# Canonicalization Policy (Metric/Technique)

Use this policy before creating a new file in `docs/metrics/` or `docs/techniques/`.
Goal: avoid duplicate docs for the same concept under different names.

## Scope
- New metric names extracted from source notes
- New technique names extracted from source notes
- Variant spellings, abbreviations, and renamed reintroductions

## Canonicalization Workflow
1. Extract candidate tuple from source note:
   - name string(s)
   - objective/function meaning
   - required inputs
   - hyperparameter semantics
   - task alignment meaning
2. Compare against existing canonical docs.
3. Score semantic match with 4 checks:
   - Objective equivalence
   - Input equivalence
   - Hyperparameter-role equivalence
   - Task-alignment equivalence
4. Apply scope filter first (for `docs/techniques/`):
   - include only general-purpose high-dimensional -> low-dimensional projection techniques
   - do not reject only because a method is less popular
   - reject meta-frameworks and domain-specific methods
   - if rejected by scope filter, decision is `out-of-scope`
5. Decision (if in scope):
   - `alias-existing` if 3/4+ checks match
   - `new-concept` if 0-1 checks match
   - `needs-review` if exactly 2 checks match or evidence is weak
6. Apply action:
   - `out-of-scope`: do not create a technique doc; log reason in alias register.
   - `alias-existing`: update existing canonical doc; add alias mention and new source-note links.
   - `new-concept`: create new doc with required sections.
   - `needs-review`: do not silently create duplicate. Record and escalate in alias register.

## Lexical Normalization Rules
- Lowercase, strip punctuation, unify separators (`-`, `_`, space).
- Expand common abbreviations where evidence supports mapping:
  - `t&c` -> `trustworthiness & continuity`
  - `c+evm` -> `c_evm`
  - `catSNE` -> class-aware t-SNE (candidate alias, not automatic)
- Handle spelling variants:
  - `nonmetric` == `non-metric`
  - `k nearest` == `k-nearest` == `kNN` (context dependent)

## Non-Automatic Cases (Require Evidence)
Do not auto-merge if any of these differ:
- Objective function form differs
- Input definition differs (e.g., label-aware vs label-agnostic)
- Hyperparameter has different semantic role
- Claimed task alignment differs in source

## Required Logging
Every alias/new decision must be appended to:
- `builder/evidence/alias-register.md`

Log format:
- candidate name
- canonical id/file
- decision (`alias-existing|new-concept|needs-review|out-of-scope`)
- evidence ids
- rationale (short)
- reviewed date

## Definition of Done for Canonicalization
- Candidate checked with 4 semantic checks
- Decision logged in alias register
- Docs updated according to decision
- No duplicate concept files left unresolved
