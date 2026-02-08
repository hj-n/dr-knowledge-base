# Overview

## Goal
Help LLMs run a consistent DR analysis workflow:
1. clarify the user's primary task,
2. choose technique/metrics aligned to that task,
3. explain the recommendation in user language.

## Core Axis
This KB is centered on seven analytical tasks:
- Neighborhood identification
- Outlier identification
- Cluster identification
- Point distance investigation
- Class separability investigation
- Cluster distance investigation
- Cluster density investigation

These seven tasks are fixed as the primary axis.
Subtask refinement is allowed under each axis when needed:
[`docs/task-taxonomy.md`](./task-taxonomy.md)

## Navigation
- Start workflow: [`docs/workflow/dr-analysis-workflow.md`](./workflow/dr-analysis-workflow.md)
- Task-aligned initialization rules: [`docs/workflow/task-aligned-initialization.md`](./workflow/task-aligned-initialization.md)
- Final reporting contract: [`docs/workflow/reliability-report-contract.md`](./workflow/reliability-report-contract.md)
- Intake questions first: [`docs/intake-question-tree.md`](./intake-question-tree.md)
- Task axis and subtask policy: [`docs/task-taxonomy.md`](./task-taxonomy.md)
- Metric policy and warning gate: [`docs/metrics-and-libraries.md`](./metrics-and-libraries.md)
- Task-to-metric starter bundles: [`docs/metrics-and-libraries.md`](./metrics-and-libraries.md) (`Task-to-Metric Starter Bundles`)
- Frequency-based priority (user-facing): [`docs/reference-coverage.md`](./reference-coverage.md)
- Reliability cautions and tips: [`docs/reliability-cautions-and-tips.md`](./reliability-cautions-and-tips.md)
- Paper catalog guide: [`docs/paper-catalog.md`](./paper-catalog.md)
- Paper list (CSV): [`docs/paper-catalog.csv`](./paper-catalog.csv)
- Metric details: [`docs/metrics/README.md`](./metrics/README.md)
- Technique details: [`docs/techniques/README.md`](./techniques/README.md)

## Drill-Down Path
Use this order when an LLM starts from this file.

1. Task clarification:
   [`docs/intake-question-tree.md`](./intake-question-tree.md)
2. Task axis/subtask lock:
   [`docs/task-taxonomy.md`](./task-taxonomy.md)
3. Data audit + preprocessing:
   [`docs/workflow/dr-analysis-workflow.md`](./workflow/dr-analysis-workflow.md) (Step 2)
4. Technique/metric selection:
   [`docs/metrics-and-libraries.md`](./metrics-and-libraries.md),
   [`docs/techniques/README.md`](./techniques/README.md),
   [`docs/metrics/README.md`](./metrics/README.md)
   and per-method/per-metric `Practical Reliability Notes` sections.
5. Task-aligned initialization decision:
   [`docs/workflow/task-aligned-initialization.md`](./workflow/task-aligned-initialization.md)
6. Candidate prioritization:
   [`docs/reference-coverage.md`](./reference-coverage.md)
7. Reliability caution check:
   [`docs/reliability-cautions-and-tips.md`](./reliability-cautions-and-tips.md)
8. Source transparency:
   [`docs/paper-catalog.md`](./paper-catalog.md),
   [`docs/paper-catalog.csv`](./paper-catalog.csv)
9. Final explanation contract:
   [`docs/workflow/dr-analysis-workflow.md`](./workflow/dr-analysis-workflow.md) (Step 7),
   [`docs/workflow/reliability-report-contract.md`](./workflow/reliability-report-contract.md)

## Design Rules
- Task-first: no method recommendation before task clarification.
- Library-default: use ZADU metric IDs for reliability checks.
- Consumer-first docs: concise guidance in `docs/`; detailed source extraction stays in `papers/notes/`.
