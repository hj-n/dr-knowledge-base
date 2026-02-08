# Intake Question Tree

The only mandatory goal of intake is to identify one primary analytical task.
Do not recommend DR techniques or metrics before this is fixed.

Related:
- Workflow anchor: [`docs/workflow/dr-analysis-workflow.md`](./workflow/dr-analysis-workflow.md)
- Post-intake selection rules: [`docs/metrics-and-libraries.md`](./metrics-and-libraries.md)
- Axis/subtask policy: [`docs/task-taxonomy.md`](./task-taxonomy.md)

## Step 1: Plain-Language Goal Question (Required)
Ask first without task labels:
- "What do you want to figure out from this embedding?"
- "Are you trying to find similar items, outliers, groups, distance patterns, or density patterns?"

## Step 2: Clarify One Task (Only If Needed)
If the answer is vague, ask one short confirmation at a time:
- "Do you want to find points similar to a target point?"
- "Do you want to detect unusual/outlier points?"
- "Do you want to identify groups or clusters?"
- "Do you want to compare distances between individual points?"
- "Do you want to check whether classes are well separated?"
- "Do you want to compare distances between clusters?"
- "Do you want to compare how dense or spread clusters are?"

## Step 3: Internal Mapping to the 7 Tasks
After confirmation, map to exactly one primary task:
1. Neighborhood identification
2. Outlier identification
3. Cluster identification
4. Point distance investigation
5. Class separability investigation
6. Cluster distance investigation
7. Cluster density investigation

## Step 4: Optional Subtask Refinement
If needed, define a more specific subtask under the selected primary task.

Rules:
- Keep exactly one primary task axis.
- Subtask is optional and cannot replace the primary axis.
- If subtask is unclear, proceed with axis-level guidance.

## Gate
- If multiple goals exist, ask for one primary goal first.
- If still unclear, do not proceed to technique/metric selection.
- If clear, proceed to Step 3 in
  [`docs/workflow/dr-analysis-workflow.md`](./workflow/dr-analysis-workflow.md).
