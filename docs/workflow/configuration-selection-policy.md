# Configuration Selection Policy

Use this policy to produce a deterministic DR recommendation from aligned candidates.

Related:
- Workflow anchor: [`docs/workflow/dr-analysis-workflow.md`](./dr-analysis-workflow.md)
- Metrics and techniques guide: [`docs/metrics-and-libraries.md`](../metrics-and-libraries.md)
- Coverage ranking: [`docs/reference-coverage.md`](../reference-coverage.md)
- Conflict policy (builder): [`builder/evidence/conflict-policy.md`](../../builder/evidence/conflict-policy.md)

## Candidate Set Rule
1. Start from goal-aligned candidates.
2. For best/optimal requests, evaluate the full aligned set before pruning.
3. Remove candidates only with explicit hard-failure reasons.
4. Keep rejected-candidate reasons in the technical record.

## Hard Filters
Reject a candidate when any of the following holds:
- method behavior does not match the confirmed goal
- label assumptions fail for label-aware evaluation
- candidate is supervised/label-dependent but the confirmed goal is not class separability investigation
- core claims lack paper-backed evidence
- method is justified only by popularity/convention without task-fit and reliability evidence
- conflict status is contested and no stable fallback exists

## Deterministic Scoring Model
Use one fixed weighted score in the range 0-100:

`score = 30*goal_fit + 20*evidence_support + 20*stability + 15*safety_check_consistency + 10*runtime_feasibility + 5*interpretability`

Each component is normalized to `[0,1]`.

## Acceptance Bands
- accepted: score >= 75 and no hard-filter failure
- provisional: score 60-74 and no hard-filter failure
- exploratory: score < 60 or unresolved hard-filter issue

Selection rule:
- choose top accepted candidate
- if none, choose top provisional candidate and include uncertainty
- if only exploratory candidates remain, do not provide a definitive final recommendation

## Tie-Break Rule
If score gap is under 3 points:
1. prefer higher stability
2. then higher evidence support
3. then lower runtime cost
4. if still tied, return two candidates and mark as exploratory

## Coverage Priority Rule
Use PDF-backed coverage ranking as a tie-break layer:
1. higher source PDF count
2. higher source-note count
3. stronger average evidence quality
4. if still tied, keep both and state the tie explicitly

## Internal Record Schema
Technical field names are maintained in:
- [`builder/evidence/internal-report-schema.md`](../../builder/evidence/internal-report-schema.md)
