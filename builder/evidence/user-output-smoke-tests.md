# User Output Smoke Tests

Purpose:
- sanity-check whether an agent that reads this KB produces useful user-facing DR guidance and concise runnable code.
- catch regressions where internal jargon leaks into user responses or code becomes policy-heavy.

## Scenario 1: Ambiguous Intent
Prompt:
- `I want to do DR.`

Pass criteria:
- asks one plain clarification question first.
- does not recommend a method before the goal is confirmed.
- uses novice-friendly wording.

Fail signals:
- immediate method recommendation without clarification.
- internal jargon in user-facing text.

## Scenario 2: MNIST Class Relationship
Prompt:
- `I want to inspect relationships between MNIST classes.`

Pass criteria:
- confirms class-relationship intent explicitly.
- compares at least one global-distance-friendly candidate and one local candidate under the same preprocessing.
- includes final settings (method, key params, preprocessing, optimizer).
- provides concise runnable code with `bayes_opt` + `zadu`.

Fail signals:
- popularity-only rationale.
- no final settings disclosure.
- grid/random/manual sweep suggestions.

## Scenario 3: Best Configuration Request
Prompt:
- `Find the best DR configuration for cluster-density analysis.`

Pass criteria:
- compares all goal-aligned candidates before pruning.
- rejects candidates only with explicit hard-failure reasons.
- explains residual risk and tradeoffs.

Fail signals:
- single-method recommendation without comparison.
- unexplained pruning decisions.

## Scenario 4: Label-Aware Metric Safety
Prompt:
- `Use label-based reliability checks to score this embedding.`

Pass criteria:
- checks/mentions label-separation assumption first.
- lowers confidence or adds label-agnostic checks when assumption is weak.
- explains caution in plain language.

Fail signals:
- class-aware scores used as definitive evidence with no assumption check.

## Scenario 5: Source Request
Prompt:
- `What papers support this recommendation?`

Pass criteria:
- cites paper bibliography entries (title, authors, venue, year, URL).
- does not cite internal file paths or repository-internal links as user references.

Fail signals:
- references to internal markdown files as user citations.
- mapping-table style explanation without paper references.

## Scenario 6: Permissive Optimization Prompt
Prompt:
- `Any optimization is allowed. Use whatever search strategy you want.`

Pass criteria:
- still uses Bayesian optimization as the only optimizer family.
- interprets permissive wording as trial-budget flexibility, not optimizer-family freedom.
- avoids grid/random/manual sweep logic in final user code.

Fail signals:
- switches to grid search, random search, or hardcoded candidate sweeps.
- omits `bayes_opt` from final runnable code.
