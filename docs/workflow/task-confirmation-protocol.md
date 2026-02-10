# Task Confirmation Protocol

Use this protocol to turn ambiguous requests into one confirmed analysis goal.

Related:
- Intake questions: [`docs/intake-question-tree.md`](../intake-question-tree.md)
- Task taxonomy: [`docs/task-taxonomy.md`](../task-taxonomy.md)
- Workflow anchor: [`docs/workflow/dr-analysis-workflow.md`](./dr-analysis-workflow.md)

## Plain-Language Rule
In user-facing answers, use `main analysis goal`.
Avoid internal labels and status keys.

## Procedure
1. Ask one open question first.
   - Example: "What do you want to learn from this 2D view?"
2. Extract intent phrases from the answer.
3. Map intent to one or more goals in the 7-goal taxonomy.
4. If more than one goal remains plausible, ask one clarification question.
5. Confirm the selected goal in plain language.

## Confidence Rule
Use three levels:
- high: one goal is clearly confirmed by the user
- medium: one goal is likely, but one competitor remains
- low: multiple goals remain plausible or the user statement is contradictory

Hard gate:
- do not recommend methods until confidence is high

## Clarification Question Rule
- Do not show all seven goal names in the first prompt.
- Use novice-friendly wording.
- Ask one discriminating question at a time.
- Avoid advanced jargon unless the user already uses it.

## If Confidence Stays Low
After three clarification turns:
- provide two plausible goals with uncertainty notes
- stop at exploratory guidance
- do not provide a definitive final ranking

## Internal Record Schema
Technical field names are maintained in:
- [`builder/evidence/internal-report-schema.md`](../../builder/evidence/internal-report-schema.md)
