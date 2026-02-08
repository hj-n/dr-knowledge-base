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
- `docs/workflow/task-confirmation-protocol.md`
- `docs/workflow/preprocessing-profiles.md`
- `docs/workflow/configuration-selection-policy.md`
- `docs/workflow/task-aligned-initialization.md`
- `docs/workflow/hyperparameter-optimization-protocol.md`
- `docs/workflow/visualization-policy.md`
- `docs/workflow/communication-layer-policy.md`
- `docs/workflow/reliability-report-contract.md`
- `docs/overview.md`
- `docs/intake-question-tree.md`
- `docs/task-taxonomy.md`
- `docs/metrics-and-libraries.md`
- `docs/reference-coverage.md`
- `docs/reliability-cautions-and-tips.md`
- `docs/paper-catalog.md`
- `docs/paper-catalog.csv`
- `docs/metrics/`
- `docs/techniques/`
- `builder/evidence/conflict-policy.md`
- `builder/evidence/conflict-register.md`
- `builder/evidence/relevance-policy.md`
- `builder/evidence/canonicalization-policy.md`
- `builder/evidence/alias-register.md`
- `builder/evidence/reference-coverage.md`
- `builder/evidence/reference-coverage.json`
- `builder/evidence/pending-reference-papers.csv`
- `builder/evidence/pending-reference-papers.md`
- `builder/evidence/reference-group-map.json`
- `builder/evidence/paper-catalog.json`
- `papers/raw/`
- `papers/notes/`
- `templates/paper-note-template.md`
- `scripts/update_reference_coverage.py`
- `scripts/update_paper_catalog.py`
- `scripts/update_reference_backlog.py`
- `scripts/validate_reliability_report.py`

## Task Axis Contract
- Workflow anchor: `docs/workflow/dr-analysis-workflow.md`.
- Task lock protocol anchor: `docs/workflow/task-confirmation-protocol.md`.
- Initialization anchor: `docs/workflow/task-aligned-initialization.md` (must run after technique/metric selection and before hyperparameter optimization).
- Intake anchor: 7 analytical tasks from Jeon et al. (2025).
- 7 tasks are fixed primary axes; do not change or replace them.
- Subtask refinement is allowed under each axis per `docs/task-taxonomy.md`.
- Ask plain-language task questions first.
- Confirm one primary task axis before recommending techniques or metrics.
- Do not proceed to recommendation unless `axis_confidence = high` with explicit user confirmation quote.

## Metric Governance Contract
- Default reliability library: `zadu` (`/hj-n/zadu` via Context7).
- Use exact metric IDs from `docs/metrics-and-libraries.md` for ZADU metrics.
- Non-ZADU metrics are allowed when needed, but must include explicit provenance in source notes and metric docs.
- Apply label-separation warning gate for: `dsc`, `ivm`, `c_evm`, `nh`, `ca_tnc`.
- Final configuration ranking must follow `docs/workflow/configuration-selection-policy.md`; ad-hoc ranking prose is not sufficient.

## Ingestion Workflow
1. Confirm source file exists in `papers/raw/`.
2. Run relevance gate in `builder/evidence/relevance-policy.md`.
3. Parse with bounded runtime:
   - per-PDF processing timeout defaults to 90 seconds;
   - on timeout or parser corruption warnings, skip the file, log the reason in triage output, and continue batch processing.
   - never let one malformed PDF block the full ingestion run.
4. If relevant, create/update one individual note per source file in `papers/notes/`.
   - Seed-paper rule: every PDF directly under `papers/raw/` must have its own dedicated note file (no merged seed notes).
5. Run canonicalization gate in `builder/evidence/canonicalization-policy.md`:
   - decide `alias-existing`, `new-concept`, or `needs-review`
   - record decision in `builder/evidence/alias-register.md`
6. Use `templates/paper-note-template.md` contract.
7. Update affected docs:
   - `docs/metrics/<metric>.md` for metric-level changes.
   - `docs/techniques/<technique>.md` for technique-level changes.
   - `docs/metrics-and-libraries.md` for summary-level changes.
   - `docs/workflow/task-aligned-initialization.md` when initialization-policy evidence is added or changed.
   - `docs/reliability-cautions-and-tips.md` for grouped cautions/tips and mitigations.
8. Recompute conflict status using `builder/evidence/conflict-policy.md` and update `builder/evidence/conflict-register.md`.
9. Recompute reference frequency index with `python scripts/update_reference_coverage.py`.
10. Recompute paper catalog with `python scripts/update_paper_catalog.py`.
11. Recompute pending reference backlog from seed-paper bibliographies with `python scripts/update_reference_backlog.py`.
12. Run consistency checks (section completeness, metadata completeness, workflow-step sync).

## Seed Reference Harvesting Rule
- When seed papers (PDFs directly under `papers/raw/`) are added or updated, extract bibliography candidates that can improve reliable DR usage for visual analytics.
- Candidate extraction must be guided by both:
  - bibliography title relevance, and
  - body citation context relevance to reliability/task/quality/visual-analytics concerns.
- Keep only references that are not yet backed by local PDFs in `papers/raw/` (seed or subdirectory references).
- Write backlog outputs to:
  - `builder/evidence/pending-reference-papers.csv`
  - `builder/evidence/pending-reference-papers.md`

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
- Missing catalog metadata in frontmatter:
  - `authors`
  - `venue`
  - `year`
  - `source_pdf`
  - `authors`/`venue` may be `UNKNOWN` only when unavailable from source, but keys must be present.
- For reference papers (`papers/raw/<subdirectory>/...`), missing `seed_note_id` when no mapping exists in `builder/evidence/reference-group-map.json`.
- Metadata normalization gate:
  - `title` must not be filename-like (`1-s2...`, DOI-only strings, raw stem fragments, or parser garbage).
  - `authors` must not contain affiliation/address-only lines (for example, department addresses or correspondence markers).
  - if PDF extraction yields noisy metadata, re-check with DOI/arXiv/Crossref before finalizing frontmatter.
  - if venue cannot be resolved with high confidence, keep `venue: "UNKNOWN"` rather than writing a guessed venue.

## Documentation Quality Gate
- `docs/` must be concise and user-operational.
- `docs/` should explain what to do, when to use it, and what to avoid.
- `docs/` user-facing guidance must be understandable to DR novices:
  - do not rely on unexplained internal jargon.
  - if technical terms are required, define them in one sentence near first use.
  - final recommendation output must explicitly disclose final method and key parameter settings for end users.
  - enforce dual-layer outputs for recommendations:
    - internal technical layer (for code/audit)
    - user explanation layer (for non-experts)
  - in user layer, avoid standalone terms such as:
    - `task axis`, `metric bundle`, `warning gate`, `preprocessing signature`, `guardrail metric`
- Source-note links in `docs/` should map claims to `papers/notes/*`.
- Detailed quote-level evidence stays in `papers/notes/*`.
- Workflow-scope filter is mandatory:
  - Do not promote workflow-unrelated topics to guidance rules or policy defaults.
  - Examples to exclude from rule promotion unless directly tied to workflow decisions: pure perception studies, generic explainable-AI discussions, unrelated interactive-tool design details, and UI-only explainability tool behavior.
  - Such content may remain in source notes, but must not become recommendation rules in `docs/workflow/*`, `docs/metrics-and-libraries.md`, or policy text.
- `docs/` must keep a drill-down link chain:
  - `docs/overview.md` -> `docs/workflow/dr-analysis-workflow.md`
  - `docs/workflow/dr-analysis-workflow.md` -> `docs/workflow/task-confirmation-protocol.md`
  - `docs/workflow/dr-analysis-workflow.md` -> `docs/workflow/preprocessing-profiles.md`
  - `docs/workflow/dr-analysis-workflow.md` -> `docs/workflow/configuration-selection-policy.md`
  - `docs/workflow/dr-analysis-workflow.md` -> `docs/workflow/task-aligned-initialization.md`
  - `docs/workflow/dr-analysis-workflow.md` -> `docs/workflow/hyperparameter-optimization-protocol.md`
  - `docs/workflow/dr-analysis-workflow.md` -> `docs/workflow/visualization-policy.md`
  - `docs/workflow/dr-analysis-workflow.md` -> `docs/workflow/communication-layer-policy.md`
  - workflow step links -> step-relevant docs (`intake-question-tree`, `task-taxonomy`, `metrics-and-libraries`, `metrics/README`, `techniques/README`, `reference-coverage`, `reliability-cautions-and-tips`)
  - `docs/overview.md` should link to `docs/paper-catalog.md` and `docs/paper-catalog.csv` for source transparency
- For `docs/metrics/*` and `docs/techniques/*`, each required section must contain substantial prose:
  - target depth: at least one full paragraph, preferably two paragraphs for core sections
  - avoid one-line placeholders or bullet-only sections for core explanations
  - adding source-note links alone is not considered a valid content update
  - updating only `Practical Reliability Notes` is not considered a valid content update
  - when new evidence changes guidance, update at least one of: computation details, hyperparameter impact, task alignment rationale, or known tradeoffs

## Metric Sync Gate (Mandatory)
- Every metric file must include:
  - `Metric Definition`
  - `What It Quantifies`
  - `Computation Outline`
  - `Task Alignment`
  - `Hyperparameter Impact`
  - `Practical Reliability Notes`
  - `Notable Properties`
  - `Strengths`
  - `Interpretation Notes`
  - `Source Notes`
- Metric task alignment should be expressed in the 7-task axis vocabulary.
- If subtask refinement is used, map the subtask back to one axis in the note and recommendation rationale.
- Hyperparameter-impact statements must be evidence-backed or explicitly marked as unavailable.
- Label-separation-sensitive metrics (`dsc`, `ivm`, `c_evm`, `nh`, `ca_tnc`) must keep the warning gate text.
- Non-ZADU metrics may be added, but must satisfy provenance clarity:
  - `Source Notes` must include explicit `papers/notes/*` links for definition/use/caveat claims
  - metric ID must be unique `snake_case` and not collide with existing IDs
  - if evidence is thin, mark recommendation confidence conservatively in docs
- Before creating a new metric file, run canonicalization check to avoid alias duplicates.
- Minimum prose depth for each metric section:
  - `Metric Definition`, `What It Quantifies`, `Computation Outline`, `Hyperparameter Impact`, `Notable Properties`, `Strengths`, `Task Alignment`, and `Interpretation Notes` must each include at least one full paragraph.
  - At least three of those sections should include two paragraphs when evidence supports deeper detail.
- Partial-update prohibition:
  - A metric update is invalid if it modifies only `Source Notes` and/or only `Practical Reliability Notes`.
  - Each metric update must also revise at least one of `Computation Outline`, `Hyperparameter Impact`, `Task Alignment`, or `Interpretation Notes` when new evidence is added.

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
  - `Practical Reliability Notes`
  - `Notable Properties`
  - `Strengths`
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
- If subtask refinement is used, keep axis-level task alignment as the primary label and document subtask-level refinement as secondary rationale.
- Hyperparameter claims must be traceable to source-note evidence IDs.
- If no parameter evidence exists for a technique in current sources, state that explicitly instead of inventing defaults.
- Before creating a new technique file, run canonicalization check to avoid alias duplicates.
- Minimum prose depth for each technique section:
  - `Technique Summary`, `I/O Contract`, `Core Objective`, `Computation Outline`, `Hyperparameter Impact`, `Notable Properties`, `Strengths`, `Task Alignment`, and `Known Tradeoffs` must each include at least one full paragraph.
  - At least three of those sections should include two paragraphs when evidence supports deeper detail.
- Partial-update prohibition:
  - A technique update is invalid if it modifies only `Source Notes` and/or only `Practical Reliability Notes`.
  - Each technique update must also revise at least one of `Computation Outline`, `Hyperparameter Impact`, `Task Alignment`, or `Known Tradeoffs` when new evidence is added.

## Alias Safety Rule
- If two names look similar, do not merge by string similarity alone.
- Merge only when objective/input/hyperparameter-role/task-alignment checks match per canonicalization policy.
- If uncertain, log `needs-review` in alias register and keep canonical docs unchanged until resolved.

## Reference-Frequency Priority Rule
- Recommendation priority must use PDF-backed reference frequency from `docs/reference-coverage.md` (user-facing) and `builder/evidence/reference-coverage.md` (builder detail).
- Count only PDF sources for ranking; non-PDF sources are supporting context and do not increase frequency rank.
- Ranking order inside a task-aligned candidate set:
  1. higher `source_pdf_count`
  2. higher `source_pdf_note_count`
  3. higher average evidence level of linked source notes
  4. if still tied, keep both and mark tie explicitly in rationale
- If `builder/evidence/conflict-register.md` marks a claim as `contested`, down-rank by one tier unless user explicitly requests exploratory comparison.

## Reliability Cautions Sync Gate
- When new paper notes add reliability caveats or operational tips, update `docs/reliability-cautions-and-tips.md` in the same turn.
- Group semantically similar cautions into one theme instead of duplicating near-identical bullets.
- Each caution group must include:
  - what can go wrong
  - what to do to mitigate it
  - source-note links

## Context7 Maintenance
- Keep `context7.json` indexing scope limited to:
  - `docs`
  - `papers/notes`
- Exclude `papers/raw` from indexing.
- Refresh Context7 after meaningful doc updates.

## Workflow-Step Sync Rule
- If workflow step count/order changes, update all synchronized docs in the same turn:
  - `docs/workflow/dr-analysis-workflow.md`
  - `docs/workflow/task-confirmation-protocol.md`
  - `docs/workflow/preprocessing-profiles.md`
  - `docs/workflow/configuration-selection-policy.md`
  - `docs/workflow/hyperparameter-optimization-protocol.md`
  - `docs/workflow/visualization-policy.md`
  - `docs/workflow/communication-layer-policy.md`
  - `docs/workflow/reliability-report-contract.md`
  - `docs/overview.md`
  - `README.md`
  - `templates/paper-note-template.md` (`Workflow Relevance Map` step numbering)
- Do not leave mixed step numbering across files.

## Pre-Completion Self-Check (Mandatory)
Before ending a doc-update turn, verify:
1. Every edited/created note includes all required sections:
   - `Problem`
   - `Method Summary`
   - `When To Use / Not Use`
   - `Metrics Mentioned`
   - `Implementation Notes`
   - `Claim Atoms (For Conflict Resolution)`
   - `Workflow Relevance Map`
   - `Evidence`
2. Every edited/created note has at least 5 evidence entries unless the source is genuinely short.
3. Every note has `authors` and `venue` keys in frontmatter.
4. `docs/reference-coverage.md` includes conflict status columns for ranking transparency.
5. `python scripts/update_reference_coverage.py` and `python scripts/update_paper_catalog.py` run successfully.
6. If a recommendation report artifact is produced, validate it with:
   - `python scripts/validate_reliability_report.py <report-file>`
7. If a recommendation explanation is produced, verify novice readability:
   - includes `user_goal_restatement`
   - includes `user_what_was_compared`
   - includes `user_why_selected`
   - includes `user_risk_note`
   - avoids unexplained shorthand-only phrasing
8. If a recommendation report artifact is produced, verify final configuration disclosure:
   - includes `final_configuration_for_users`
   - includes method name and key hyperparameter values
9. If a recommendation explanation artifact is produced, verify dual-layer communication:
   - includes both internal technical explanation and user explanation sections
   - user section avoids forbidden standalone jargon
10. If a recommendation explanation artifact is produced, verify concise code deliverable:
   - includes `user_code_snippet`
   - includes `user_code_reason`
   - user code snippet does not expose internal policy keys as top-level API

## Definition of Done
- Individual source note created/updated with quality gate passed.
- Affected metric/technique docs updated.
- Conflict register refreshed.
- Paper catalog refreshed (`docs/paper-catalog.csv`, `builder/evidence/paper-catalog.json`).
- `docs/` and `papers/notes/` remain role-separated and consistent.
