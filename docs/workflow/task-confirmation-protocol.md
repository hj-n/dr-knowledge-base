# Task Confirmation Protocol

Use this protocol to convert ambiguous user language into exactly one primary analytical task axis.
The goal is to prevent premature technique selection and ensure stable downstream configuration.

Related:
- Intake questions: [`docs/intake-question-tree.md`](../intake-question-tree.md)
- Task taxonomy: [`docs/task-taxonomy.md`](../task-taxonomy.md)
- Workflow anchor: [`docs/workflow/dr-analysis-workflow.md`](./dr-analysis-workflow.md)

## Required Inputs
- `user_goal_text`: user statement in plain language
- `analysis_context`: optional constraints (labels, runtime, interpretability)

## Decision Procedure
1. Ask one open plain-language question first.
   - Example: "What do you want to learn from this embedding?"
2. Extract candidate intent phrases from the response.
3. Map each phrase to one or more of the 7 task axes.
4. If more than one axis remains plausible, ask one clarification question at a time.
5. Confirm the selected axis in plain language before moving on.

## Confidence Rubric
Assign `axis_confidence` from evidence in the user response.

- `high`:
  - one axis clearly dominates,
  - user confirmation is explicit,
  - no unresolved competing axis.
- `medium`:
  - top axis is plausible,
  - one competing axis remains,
  - user confirmation is indirect or partial.
- `low`:
  - multiple axes remain equally plausible,
  - user confirmation is missing or contradictory.

Hard gate:
- Do not proceed to technique/metric recommendation unless `axis_confidence = high`.

## Clarification Question Rules
- Do not expose all 7 task names at the first prompt.
- Use plain language that a DR novice can understand.
- Ask exactly one discriminating question per turn.
- Prefer contrastive question format:
  - "Are you trying to find similar points around each point, or compare distances between whole clusters?"
- Avoid jargon in questions (`manifold`, `embedding topology`, `local-global tradeoff`) unless the user already used those terms.

## Required Output Contract
Step 1 must produce:
- `primary_task_axis`
- `task_subtype` (optional)
- `axis_confidence`
- `task_confirmation_quote` (user wording that confirms intent)
- `task_mapping_rationale` (1-3 lines)

## Failure Handling
If confidence remains below `high` after 3 clarification turns:
- set `recommendation_status = exploratory`
- output two candidate axes with uncertainty note
- defer hard method ranking

## Example
```text
user_goal_text: "I need to know whether nearby customers in feature space stay nearby after projection."
primary_task_axis: Neighborhood identification
task_subtype: local-neighbor consistency check
axis_confidence: high
task_confirmation_quote: "nearby customers stay nearby"
task_mapping_rationale: user intent is local-neighborhood preservation, not global distance ordering.
```
