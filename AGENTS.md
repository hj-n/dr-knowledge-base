# AGENTS.md

## Role
This file is for repository-maintenance agents.
It defines how to ingest new sources, update docs, and keep quality consistent.

## Consumer vs Builder Separation
- Consumer-facing guidance lives in `docs/`.
- Builder-only extraction details live in `papers/notes/` and `builder/evidence/`.
- In `docs/`, do not paste raw quote blocks or parsing logs.
- In `docs/`, link to source notes instead of raw files in `papers/raw/`.

## Repository Language Rule
- All repository content must be written in English.
- Do not add non-English prose to `docs/`, `papers/notes/`, `builder/`, `README.md`, `AGENTS.md`, or templates.
- If a source quote is non-English or mixed, keep the original quote in `papers/notes` evidence, but write all surrounding explanations in English.

## Required Structure
- `docs/workflow/dr-analysis-workflow.md`
- `docs/overview.md`
- `docs/intake-question-tree.md`
- `docs/metrics-and-libraries.md`
- `docs/metrics/`
- `docs/techniques/`
- `builder/evidence/conflict-policy.md`
- `builder/evidence/conflict-register.md`
- `builder/evidence/relevance-policy.md`
- `builder/evidence/canonicalization-policy.md`
- `builder/evidence/alias-register.md`
- `papers/raw/`
- `papers/notes/`
- `templates/paper-note-template.md`

## Task Axis Contract
- Workflow anchor: `docs/workflow/dr-analysis-workflow.md`.
- Intake anchor: 7 analytical tasks from Jeon et al. (2025).
- Ask plain-language task questions first.
- Confirm one primary task before recommending techniques or metrics.

## Metric Governance Contract
- Default reliability library: `zadu` (`/hj-n/zadu` via Context7).
- Use exact metric IDs from `docs/metrics-and-libraries.md`.
- Apply label-separation warning gate for: `dsc`, `ivm`, `c_evm`, `nh`, `ca_tnc`.

## Ingestion Workflow
1. Confirm source file exists in `papers/raw/`.
2. Run relevance gate in `builder/evidence/relevance-policy.md`.
3. If relevant, create/update one individual note per source file in `papers/notes/`.
4. Run canonicalization gate in `builder/evidence/canonicalization-policy.md`:
   - decide `alias-existing`, `new-concept`, or `needs-review`
   - record decision in `builder/evidence/alias-register.md`
5. Use `templates/paper-note-template.md` contract.
6. Update affected docs:
   - `docs/metrics/<metric>.md` for metric-level changes.
   - `docs/techniques/<technique>.md` for technique-level changes.
   - `docs/metrics-and-libraries.md` for summary-level changes.
7. Recompute conflict status using `builder/evidence/conflict-policy.md` and update `builder/evidence/conflict-register.md`.

## Non-Negotiable Note Quality Gate
Reject a note as incomplete if any condition fails:
- Contains placeholder phrasing such as:
  - "parsed automatically"
  - "workflow-relevant evidence" without concrete claim
  - "manual follow-up recommended" as a substitute for summary
- Missing concrete method detail in `Method Summary`.
- Missing concrete usage boundaries in `When To Use / Not Use`.
- Fewer than 5 evidence entries, unless the source text is genuinely short.
- Claim atoms are generic and not tied to metric or method behavior.

## Documentation Quality Gate
- `docs/` must be concise and user-operational.
- `docs/` should explain what to do, when to use it, and what to avoid.
- Source-note links in `docs/` should map claims to `papers/notes/*`.
- Detailed quote-level evidence stays in `papers/notes/*`.
- For `docs/metrics/*` and `docs/techniques/*`, each required section must contain substantial prose:
  - target depth: at least one full paragraph, preferably two paragraphs for core sections
  - avoid one-line placeholders or bullet-only sections for core explanations

## Metric Sync Gate (Mandatory)
- Every metric file must include:
  - `Metric Definition`
  - `What It Quantifies`
  - `Computation Outline`
  - `Task Alignment`
  - `Hyperparameter Impact`
  - `Notable Properties`
  - `Interpretation Notes`
  - `Source Notes`
- Metric task alignment should be expressed in the 7-task vocabulary.
- Hyperparameter-impact statements must be evidence-backed or explicitly marked as unavailable.
- Label-separation-sensitive metrics (`dsc`, `ivm`, `c_evm`, `nh`, `ca_tnc`) must keep the warning gate text.
- Before creating a new metric file, run canonicalization check to avoid alias duplicates.
- Minimum prose depth for each metric section:
  - `Metric Definition`, `What It Quantifies`, `Computation Outline`, `Hyperparameter Impact`, `Notable Properties`, `Task Alignment`, and `Interpretation Notes` must each include at least one full paragraph.
  - At least three of those sections should include two paragraphs when evidence supports deeper detail.

## Technique Sync Gate (Mandatory)
- If a new or updated source note contains technique-level information, update `docs/techniques/` in the same turn.
- Do not leave technique mentions stranded in `papers/notes/` without a corresponding technique doc update.
- Every technique file must include:
  - `Technique Summary`
  - `I/O Contract`
  - `Core Objective`
  - `Computation Outline`
  - `Task Alignment`
  - `Hyperparameter Impact`
  - `Notable Properties`
  - `Known Tradeoffs`
  - `Source Notes`
- Technique inclusion scope:
  - include only general-purpose methods that map high-dimensional input to low-dimensional projections
  - exclude meta-frameworks and orchestration methods
  - exclude domain-specific methods
  - do not exclude methods solely because they are less popular
- Task alignment claims must be labeled:
  - `Direct evidence` when the source explicitly maps technique to tasks.
  - `Inferred alignment` when mapped by structure/behavior and not stated directly.
- Hyperparameter claims must be traceable to source-note evidence IDs.
- If no parameter evidence exists for a technique in current sources, state that explicitly instead of inventing defaults.
- Before creating a new technique file, run canonicalization check to avoid alias duplicates.
- Minimum prose depth for each technique section:
  - `Technique Summary`, `I/O Contract`, `Core Objective`, `Computation Outline`, `Hyperparameter Impact`, `Notable Properties`, `Task Alignment`, and `Known Tradeoffs` must each include at least one full paragraph.
  - At least three of those sections should include two paragraphs when evidence supports deeper detail.

## Alias Safety Rule
- If two names look similar, do not merge by string similarity alone.
- Merge only when objective/input/hyperparameter-role/task-alignment checks match per canonicalization policy.
- If uncertain, log `needs-review` in alias register and keep canonical docs unchanged until resolved.

## Context7 Maintenance
- Keep `context7.json` indexing scope limited to:
  - `docs`
  - `papers/notes`
- Exclude `papers/raw` from indexing.
- Refresh Context7 after meaningful doc updates.

## Definition of Done
- Individual source note created/updated with quality gate passed.
- Affected metric/technique docs updated.
- Conflict register refreshed.
- `docs/` and `papers/notes/` remain role-separated and consistent.
