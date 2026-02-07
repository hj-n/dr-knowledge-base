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

## Key Documents
- `docs/workflow/dr-analysis-workflow.md`
- `docs/intake-question-tree.md`
- `docs/metrics-and-libraries.md`
- `docs/metrics/`
- `docs/techniques/`

## Design Rules
- Task-first: no method recommendation before task clarification.
- Library-default: use ZADU metric IDs for reliability checks.
- Consumer-first docs: concise guidance in `docs/`; detailed source extraction stays in `papers/notes/`.
