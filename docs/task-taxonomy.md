# Task Taxonomy

This repository keeps a stable 7-task axis and allows optional subtask refinement when needed.

Related:
- Intake flow: [`docs/intake-question-tree.md`](./intake-question-tree.md)
- Workflow anchor: [`docs/workflow/dr-analysis-workflow.md`](./workflow/dr-analysis-workflow.md)
- Selection policy: [`docs/metrics-and-libraries.md`](./metrics-and-libraries.md)

## Stable Primary Task Axis (Fixed)
The primary task must always map to exactly one of these seven:
1. Neighborhood identification
2. Outlier identification
3. Cluster identification
4. Point distance investigation
5. Class separability investigation
6. Cluster distance investigation
7. Cluster density investigation

## Subtask Refinement (Extensible)
When user intent requires finer granularity, add an optional subtask label under the chosen primary axis.

Rules:
- A subtask never replaces the primary axis.
- A subtask must be nested under exactly one primary axis.
- Method and metric recommendation logic is anchored to the primary axis first, then refined by subtask.
- If subtask evidence is weak, fall back to axis-level guidance.

## Subtask Examples (Seeded)
The examples below are suggested refinements observed in task-sequence and usage studies.
They do not replace the fixed 7-axis contract.

1. Neighborhood identification:
   - nearest-neighbor sanity check
   - local neighborhood continuity check
2. Outlier identification:
   - isolated-point screening
   - suspicious small-island inspection
3. Cluster identification:
   - verify visible cluster boundaries
   - membership assignment for ambiguous points
   - naming discovered clusters
4. Point distance investigation:
   - pairwise distance comparison between selected points
   - local-vs-global distance consistency check
5. Class separability investigation:
   - match clusters to known class labels
   - investigate overlap between known classes
6. Cluster distance investigation:
   - compare inter-cluster spacing under multiple methods
   - test whether cluster-distance order is stable
7. Cluster density investigation:
   - compare compactness/spread across clusters
   - density-rank comparison under projection changes

## Dimension-Focused Clarification Cue
If the user speaks in terms of dimensions/features (not points/clusters), keep the same 7-axis mapping but add a subtask note that captures dimension-focused intent.
Example:
- `primary_task_axis`: `Cluster identification`
- `task_subtype`: `map synthesized dimension back to original dimensions`

## Suggested Output Contract
Record task decisions with two fields:
- `primary_task_axis`: one of the fixed 7 tasks
- `task_subtype`: optional free-text or controlled label under that axis

Example:
- `primary_task_axis`: `Cluster identification`
- `task_subtype`: `small-cluster retrieval under class imbalance`

## Update Policy
You may add new subtask labels at any time if they improve recommendation quality.

Do not:
- add or remove primary axis categories without explicit repository-level decision
- create a subtask that maps to multiple primary axes at once
