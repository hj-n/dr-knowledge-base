# Intake Question Tree

The first goal is to lock exactly one primary analytical task.
No technique or metric recommendation is allowed before this lock.

Related:
- Task confirmation protocol: [`docs/workflow/task-confirmation-protocol.md`](./workflow/task-confirmation-protocol.md)
- Workflow anchor: [`docs/workflow/dr-analysis-workflow.md`](./workflow/dr-analysis-workflow.md)
- Axis/subtask policy: [`docs/task-taxonomy.md`](./task-taxonomy.md)

## Step 1: Open Goal Prompt (Required)
Ask in plain language first:
- "What are you trying to learn from this projection?"

Do not list all task labels in the first question.

## Step 2: One-Question Clarification (Only If Needed)
If intent is ambiguous, ask one discriminating question at a time.
Examples:
- "Do you care more about finding similar points or comparing distances between groups?"
- "Is your goal to find unusual points, or to verify class separation?"

## Step 3: Internal Mapping to 7 Tasks
Map confirmed intent to exactly one axis:
1. Neighborhood identification
2. Outlier identification
3. Cluster identification
4. Point distance investigation
5. Class separability investigation
6. Cluster distance investigation
7. Cluster density investigation

## Step 4: Plain-Language Confirmation (Required)
Before moving forward, confirm in user wording:
- "To confirm: your main goal is `<plain-language restatement>`. Is that right?"

## Step 5: Optional Subtask Refinement
If useful, add one subtask under the selected axis.

Rules:
- Keep one primary axis only.
- Subtask is optional and cannot replace primary axis.

## Hard Gate
Do not proceed to Step 2+ of workflow unless:
- `primary_task_axis` is set
- `axis_confidence = high`
- user confirmation quote is captured

## Required Output
- `primary_task_axis`
- `task_subtype` (optional)
- `axis_confidence`
- `task_confirmation_quote`
- `success_criteria`
