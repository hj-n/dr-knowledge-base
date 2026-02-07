# Workflow Relevance Policy

This KB is workflow-first.
If new PDF content does not materially support the DR analysis workflow, it may be excluded from storage.

## Primary Criterion
A source is ingestible only if it contributes to at least one step in:
- `docs/workflow/dr-analysis-workflow.md`

## Step-Mapped Relevance Check
Accept only when the source provides actionable evidence for one or more:
1. Task clarification
2. Data audit + preprocessing
3. Technique/metric selection or warning gate
4. Hyperparameter optimization
5. Visualization policy
6. User-facing explanation strategy

## Exclusion Rule
Exclude (do not create/update metric/technique knowledge files) when the source is mostly:
- unrelated tooling details
- UI/interaction topics that do not change workflow decisions
- domain discussions without actionable impact on the workflow steps

Example exclusion:
- interactive DR explainability tool discussions that do not change task/metric/technique/hyperparameter/validation decisions.

## Minimum Ingestion Standard
For accepted sources, require:
- at least one new or updated `CLAIM-*` atom
- evidence IDs linked to that claim
- at least one affected workflow step reference

If this standard is not met, skip ingestion.
