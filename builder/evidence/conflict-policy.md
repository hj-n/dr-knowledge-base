# Evidence Conflict Resolution Policy

This policy defines how to resolve conflicting claims across multiple papers.
It follows two primary principles:
1. higher support from multiple sources -> higher weight
2. stronger justification and validation -> higher weight

## Scope
Apply this policy when two or more sources make incompatible claims about:
- metric behavior
- technique suitability
- reliability caveats
- task-method alignment

## Claim Unit
A decision is made per atomic claim (`claim_id`).
Example:
- `CLAIM-TECH-LOCAL-TSNE`: "t-SNE is suitable for neighborhood identification"

## Scoring Model
For each side (`support`, `contradict`), compute:

1. `SourceSupportScore` (0 to 1)
- `WeightedSourceCount = sum(source_weight_i)`
- `SourceSupportScore = min(1.0, WeightedSourceCount / 3.0)`

Where:
- `source_weight_i = evidence_level_weight * independence_weight`
- `evidence_level_weight`: `high=1.0`, `medium=0.7`, `low=0.4`
- `independence_weight`:
  - `1.0` independent paper/team
  - `0.8` partial overlap (author/team/benchmark overlap)
  - `0.6` heavy overlap

2. `JustificationValidationScore` (0 to 1)
- Per source, assign `rigor_score`:
  - `1.0` theorem/proof or very strong validation with broad reproducibility
  - `0.85` multi-dataset benchmark with clear baselines and statistical validation
  - `0.7` controlled empirical study with baselines but limited breadth
  - `0.5` narrow case study / partial validation
  - `0.3` weakly justified claim / no clear validation
- `JustificationValidationScore = average(rigor_score_i)`

3. `SideScore` (0 to 1)
- `SideScore = 0.6 * SourceSupportScore + 0.4 * JustificationValidationScore`

## Decision Rule
Given `S = SideScore(support)` and `C = SideScore(contradict)`:

- `Accepted (support)`: `S >= 0.65` and `(S - C) >= 0.15`
- `Accepted (contradict)`: `C >= 0.65` and `(C - S) >= 0.15`
- `Contested`: both sides >= 0.5 and absolute gap < 0.15
- `Insufficient`: otherwise

## Documentation Rule
For every contested or high-impact accepted claim in `docs/*.md`, include:
- claim ID
- decision status (`accepted`, `contested`, `insufficient`)
- linked supporting evidence IDs
- linked contradicting evidence IDs (if any)
- last reviewed date

## Operational Workflow
When adding a new paper:
1. Extract claim atoms and map to existing `claim_id`s.
2. Add new evidence IDs in `papers/notes/*.md`.
3. Update `builder/evidence/conflict-register.md`.
4. Recompute side scores and decision.
5. Update affected docs:
   - `docs/metrics/*.md`
   - `docs/techniques/*.md`
   - `docs/metrics-and-libraries.md` (if summary guidance changes)

## Tie-Break Rule
If decision remains `Contested`:
- keep both views visible
- prefer conservative recommendation
- explicitly request user validation context
