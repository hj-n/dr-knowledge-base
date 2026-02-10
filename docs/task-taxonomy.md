# Task Taxonomy

This guide keeps a stable 7-goal taxonomy and allows optional subgoal refinement.

Related:
- Intake flow: [`docs/intake-question-tree.md`](./intake-question-tree.md)
- Task confirmation: [`docs/workflow/task-confirmation-protocol.md`](./workflow/task-confirmation-protocol.md)
- Workflow anchor: [`docs/workflow/dr-analysis-workflow.md`](./workflow/dr-analysis-workflow.md)
- Metrics and techniques: [`docs/metrics-and-libraries.md`](./metrics-and-libraries.md)

## Fixed Goal Set
Always map to exactly one of the following:
1. Neighborhood identification
2. Outlier identification
3. Cluster identification
4. Point distance investigation
5. Class separability investigation
6. Cluster distance investigation
7. Cluster density investigation

## Subgoal Refinement
Subgoals are optional and help with finer guidance.
Rules:
- a subgoal never replaces the main goal
- a subgoal must be nested under one main goal
- if subgoal evidence is weak, fall back to main-goal guidance

## Example Subgoals
1. Neighborhood identification
- nearest-neighbor sanity check
- local continuity check

2. Outlier identification
- isolated-point screening
- small-island inspection

3. Cluster identification
- boundary verification
- ambiguous membership review

4. Point distance investigation
- pairwise distance comparison
- local-vs-global distance consistency check

5. Class separability investigation
- overlap investigation for known classes
- class-to-cluster correspondence check

6. Cluster distance investigation
- inter-cluster spacing comparison
- spacing-order stability check

7. Cluster density investigation
- compactness and spread comparison
- density-rank stability check

## Update Policy
You may add subgoals when evidence supports them.
Do not add or remove the seven main goals without repository-level decision.
