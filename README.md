# DR Knowledge Base

Task-first knowledge base for reliable dimensionality-reduction (DR) configuration.
The goal is for an agent to: confirm the user's main analysis goal, produce a strong DR configuration, and explain why it was selected.

## Start Here
- [`docs/overview.md`](docs/overview.md)
- [`docs/workflow/dr-analysis-workflow.md`](docs/workflow/dr-analysis-workflow.md)
- [`docs/workflow/task-confirmation-protocol.md`](docs/workflow/task-confirmation-protocol.md)
- [`docs/workflow/preprocessing-profiles.md`](docs/workflow/preprocessing-profiles.md)
- [`docs/workflow/configuration-selection-policy.md`](docs/workflow/configuration-selection-policy.md)
- [`docs/workflow/task-aligned-initialization.md`](docs/workflow/task-aligned-initialization.md)
- [`docs/workflow/hyperparameter-optimization-protocol.md`](docs/workflow/hyperparameter-optimization-protocol.md)
- [`docs/workflow/visualization-policy.md`](docs/workflow/visualization-policy.md)
- [`docs/workflow/communication-layer-policy.md`](docs/workflow/communication-layer-policy.md)
- [`docs/workflow/reliability-report-contract.md`](docs/workflow/reliability-report-contract.md)
- [`docs/metrics-and-libraries.md`](docs/metrics-and-libraries.md)

## Execution Intent
1. Confirm one primary analysis goal from user language.
2. Freeze preprocessing profile and distance policy.
3. Build task-aligned technique and metric candidates.
4. Score candidates with deterministic selection policy.
5. Set task-aligned initialization policy.
6. Optimize hyperparameters with `bayes_opt` only.
7. Produce visualization artifacts, concise runnable user code, and dual-layer explanations (technical + user-friendly).

Optimization hard rule:
- Do not use `grid search`, `random search`, or manual parameter sweep loops for final recommendations.
- Use `bayes_opt` for tuning and `zadu` for reliability scoring in final analysis code.
- Final user code should include: selected DR method fit + `bayes_opt` tuning + `zadu` reliability evaluation.

## Key Directories
- `docs/`: consumer-facing operational guidance.
- `papers/notes/`: evidence notes with claim-level support.
- `papers/raw/`: raw PDFs.
- `builder/evidence/`: builder-only conflict/relevance/canonicalization policy and indices.

## Source Note Contract
Each `papers/notes/*.md` file must include frontmatter:
- `id`
- `title`
- `authors`
- `venue`
- `year`
- `tags`
- `source_pdf`
- `evidence_level`
- `updated_at`

And required sections:
1. Problem
2. Method Summary
3. When To Use / Not Use
4. Metrics Mentioned
5. Implementation Notes
6. Claim Atoms (For Conflict Resolution)
7. Workflow Relevance Map
8. Evidence

Template: `templates/paper-note-template.md`

## Maintenance Commands
- `python scripts/update_paper_catalog.py`
- `python scripts/update_reference_coverage.py`
- `python scripts/update_reference_backlog.py`
- `python scripts/audit_note_quality.py`
- `python scripts/verify_note_pdf_grounding.py`
- `python scripts/validate_user_explanation_text.py <user-text-file>`

## Prevent Internal Jargon Leakage (Mandatory)
When generating end-user answers:
1. Draft technical reasoning internally.
2. Rewrite to novice-friendly wording.
3. Remove blocked internal terms:
   - `preprocessing freeze`, `primary metric`, `guardrail metric`, `task axis`, `task lock`, `metric bundle`, `bundle scoring`, `warning gate`
4. Remove internal key names:
   - `primary_task_axis`, `warning_gate_result`, `candidate_score_table`, `selection_status`, etc.
5. Run `scripts/validate_user_explanation_text.py` before finalizing if an answer artifact is produced.
6. Ensure optimization method is `bayes_opt` only (no `grid search`, `random search`, or sweep loops).
7. Keep `user_code_snippet` minimal (target: <= 35 non-empty lines) and avoid internal jargon in code/comments (`guardrail`, `metric bundle`, `task axis`, `warning gate`).

## Context7 Instruction Snippets (for AGENTS.md / CLAUDE.md)
Use this single snippet in both `AGENTS.md` and `CLAUDE.md`:

### Shared snippet
```md
## Context7 KB Read Rule
- Before coding, load this repository knowledge base from Context7:
  1) `query-docs(libraryId="/hj-n/dr-knowledge-base", query="<task-specific workflow and reporting rules>")`
- Then follow local docs in order:
  1) `docs/overview.md`
  2) `docs/workflow/dr-analysis-workflow.md`
  3) `docs/workflow/reliability-report-contract.md`
- If external library API details are needed (for example ZADU), query that library after loading this KB.
- Implement code using retrieved API shape and KB workflow rules.
- Validate output against:
  - `docs/workflow/dr-analysis-workflow.md`
  - `docs/workflow/reliability-report-contract.md`
- Do not rely only on memory when Context7 coverage exists.
- User-facing wording rule (mandatory):
  - never expose internal terms such as `task axis`, `task lock`, `metric bundle`, `bundle scoring`, `warning gate`, `preprocessing freeze`, `primary metric`, `guardrail metric`
  - never expose internal key names (`primary_task_axis`, `warning_gate_result`, `candidate_score_table`, etc.)
  - always rewrite into plain user language before final answer
```

### Recommended query examples
- `"query-docs(libraryId='/hj-n/dr-knowledge-base', query='MNIST class-distance task workflow and final report fields')"`
- `"minimal python example for ZADU(spec, hd).measure(ld, label=...)"`.
- `"how to define make_spec(MEASURE.STRESS|PR|SNC|TNC) and parse score keys"`.
