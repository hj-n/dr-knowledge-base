---
id: paper-YYYY-short-key
title: "Paper Title"
authors: "Author A; Author B; Author C"
venue: "Conference or Journal"
year: 2025
tags: [dr, manifold, evaluation]
source_pdf: papers/raw/paper-file.pdf
seed_note_id: ""
evidence_level: high
updated_at: 2026-02-07
---

Frontmatter guidance:
- `authors`: semicolon-separated full author list if available.
- `venue`: publication venue name; use `UNKNOWN` only if not available from source.
- `seed_note_id`:
  - seed paper note: leave as empty string.
  - reference note from a seed paper's subdirectory source: set to the parent seed note ID (for example `paper-2023-zadu-library`).

# Problem
- State the concrete analysis problem in 2-4 bullets.
- State key assumptions (labels, scale, noise, task scope).
- Do not use placeholder text.

# Method Summary
- Core idea in 3-6 concrete bullets.
- Include at least one method/mechanism detail (objective, loss, criterion, or algorithmic step).
- Include important hyperparameters/defaults if present in source.

# When To Use / Not Use
- Use when: at least 2 concrete conditions.
- Avoid when: at least 1 concrete condition.
- Failure modes: at least 1 realistic failure mode tied to assumptions.

# Metrics Mentioned
- List metric IDs or metric names explicitly.
- For each metric, state what it validates.
- Add caveats (label assumptions, scale sensitivity, etc.) when present.

# Implementation Notes
- Practical setup details for coding.
- Runtime or memory notes (if available).
- Reproducibility notes (seed, deterministic setting, search space).

# Claim Atoms (For Conflict Resolution)
- CLAIM-<id> | stance: support|contradict | summary: <atomic claim> | evidence_ids: <E-ID list>
- CLAIM-<id> | stance: support|contradict | summary: <atomic claim> | evidence_ids: <E-ID list>

# Workflow Relevance Map
- Step legend:
  - 1: Task clarification and lock
  - 2: Data audit + preprocessing freeze
  - 3: Task-aligned candidate generation
  - 4: Deterministic configuration scoring and selection
  - 5: Task-aligned initialization decision
  - 6: Bayesian hyperparameter optimization
  - 7: Visualization + user explanation
- step: 1|2|3|4|5|6|7 | relevance: high|medium|low | note: <how this source changes workflow decisions>
- step: 1|2|3|4|5|6|7 | relevance: high|medium|low | note: <how this source changes workflow decisions>

# Evidence
- <E-ID> | page: <n-n>, section: <name>, quote: "..."
- <E-ID> | page: <n-n>, section: <name>, quote: "..."
- Minimum 5 evidence entries unless source text is genuinely short.
- At least one evidence entry should cover each available part: problem/method/evaluation/limitation.
