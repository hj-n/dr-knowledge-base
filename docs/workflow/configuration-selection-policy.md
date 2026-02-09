# Configuration Selection Policy

Use this policy to produce a deterministic DR configuration recommendation.
The policy converts task-aligned candidates into a ranked decision with explicit scoring.

Related:
- Workflow anchor: [`docs/workflow/dr-analysis-workflow.md`](./dr-analysis-workflow.md)
- Metrics/techniques policy: [`docs/metrics-and-libraries.md`](../metrics-and-libraries.md)
- Reference coverage: [`docs/reference-coverage.md`](../reference-coverage.md)
- Conflict policy (builder): [`builder/evidence/conflict-policy.md`](../../builder/evidence/conflict-policy.md)

## Candidate Generation
1. Start from task-aligned starter candidates in `docs/metrics-and-libraries.md`.
2. For best/optimal selection requests, keep the full task-aligned candidate set for initial scoring.
3. Remove candidates only when hard gates fail, with explicit rejection reason.
4. Keep remaining candidates for scoring.

## Hard Gates (Mandatory)
Reject candidate if any condition fails:
- not aligned to `primary_task_axis`
- label-separation check is `fail` for class-aware metric usage
- missing source-note provenance for core claim
- conflict status is `contested` and no fallback candidate exists

## Scoring Model (0 to 100)
For each technique+metric candidate:

`score = 30*task_fit + 20*evidence_support + 20*stability + 15*safety_check_consistency + 10*runtime_feasibility + 5*interpretability`

Each component is normalized to `[0,1]`.

### Component Definitions
- `task_fit`:
  - 1.0 direct task evidence
  - 0.75 inferred but consistent
  - 0.5 weak alignment
  - 0.0 mismatch
- `evidence_support`:
  - derived from `docs/reference-coverage.md` support tier and conflict status
  - down-weight by 0.2 if conflict is `unknown`
- `stability`:
  - based on seed/init consistency and metric rank consistency
- `safety_check_consistency`:
  - whether main and safety check metrics agree on candidate rank direction
- `runtime_feasibility`:
  - fit to dataset size and runtime constraints
- `interpretability`:
  - suitability for required user explanation depth

## Acceptance Thresholds
- `accepted`: score >= 75 and no hard-gate failure
- `provisional`: score 60-74 and no hard-gate failure
- `exploratory`: score < 60 or unresolved hard-gate item

Selection rule:
- choose top `accepted` candidate
- if none, choose top `provisional` and report uncertainty
- if only `exploratory`, do not finalize production recommendation

## Tie-Break Rules
If score difference < 3 points:
1. prefer higher `stability`
2. then prefer higher `evidence_support`
3. then prefer lower runtime cost
4. if still tied, keep two candidates and mark `recommendation_status = exploratory`

## Required Decision Output
- `candidate_score_table`
- `selected_configuration`
- `selection_status` (`accepted|provisional|exploratory`)
- `selection_reasoning_summary`
- `rejected_candidates_with_reason`
- `aligned_candidate_coverage` (`full|partial_with_reason`)

## Candidate Score Table Format
```text
candidate_id,task_fit,evidence_support,stability,safety_check_consistency,runtime_feasibility,interpretability,total_score,status
umap+tnc_snc_stress,0.90,0.80,0.78,0.85,0.90,0.70,83.8,accepted
```
