# Intake Question Tree

The first objective is to confirm one main analysis goal.
Do not recommend techniques before this confirmation.

Related:
- Task confirmation protocol: [`docs/workflow/task-confirmation-protocol.md`](./workflow/task-confirmation-protocol.md)
- Workflow anchor: [`docs/workflow/dr-analysis-workflow.md`](./workflow/dr-analysis-workflow.md)
- Goal taxonomy: [`docs/task-taxonomy.md`](./task-taxonomy.md)

## Step 1: Open Prompt
Ask one plain-language question:
- "What do you want to learn from this projection?"

Do not list all goal labels in the first turn.

## Step 2: One Clarification Question (If Needed)
If intent is ambiguous, ask one discriminating question.
Examples:
- "Do you care more about finding similar points, or comparing distances between groups?"
- "Is your goal to find unusual points, or to check class separation?"

## Step 3: Map to One Goal
Map the confirmed intent to one of the seven goals:
1. Neighborhood identification
2. Outlier identification
3. Cluster identification
4. Point distance investigation
5. Class separability investigation
6. Cluster distance investigation
7. Cluster density investigation

## Step 4: Confirm in Plain Language
Before moving on, confirm with the user:
- "To confirm: your main goal is <plain restatement>. Is that correct?"

## Step 5: Optional Subgoal
If helpful, add one subgoal under the selected main goal.
Subgoal cannot replace the main goal.

## Hard Gate
Do not proceed to method recommendation until the goal is confirmed with high confidence.

## Internal Record Schema
Technical field names are maintained in:
- [`builder/evidence/internal-report-schema.md`](../builder/evidence/internal-report-schema.md)
