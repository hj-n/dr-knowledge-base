# Metrics and Libraries

Related:
- Workflow step anchor: [`docs/workflow/dr-analysis-workflow.md`](./workflow/dr-analysis-workflow.md) (Step 3)
- Task clarification prerequisite: [`docs/intake-question-tree.md`](./intake-question-tree.md)
- Task axis/subtask policy: [`docs/task-taxonomy.md`](./task-taxonomy.md)
- Metric catalog: [`docs/metrics/README.md`](./metrics/README.md)
- Technique catalog: [`docs/techniques/README.md`](./techniques/README.md)
- Frequency ranking: [`docs/reference-coverage.md`](./reference-coverage.md)
- Grouped reliability cautions: [`docs/reliability-cautions-and-tips.md`](./reliability-cautions-and-tips.md)

## Default Library
- Use `zadu` as the default reliability-analysis library for DR embeddings.[^zadu-lib]
- Keep ZADU metric IDs exactly as defined in the library (no custom renaming).

## Non-ZADU Metric Extension Policy
Quality metrics not included in ZADU can still be added when they are useful for the declared task.

Rules:
1. Add only with explicit provenance:
   - clear source-note links in `papers/notes/*`
   - clear mapping to what the metric measures and when to use it
2. Keep a unique metric ID in `snake_case` and avoid collisions with existing IDs.
3. Document uncertainty level:
   - if evidence is limited, mark recommendation confidence as lower.
4. Keep task alignment and warning-gate logic unchanged:
   - axis alignment first, then subtask refinement.

## Task-First Rule
- Do not pick metrics before clarifying the user's primary task axis.
- If a subtask is defined, keep axis alignment as the hard constraint and use subtask only for refinement.
- After task clarification, choose a small metric set across local/cluster/global levels.

## Metric IDs (22)
1. `tnc`
2. `mrre`
3. `lcmc`
4. `nh`
5. `ca_tnc`
6. `l_tnc`
7. `nd`
8. `dtm`
9. `kl_div`
10. `dsc`
11. `pr`
12. `srho`
13. `ivm`
14. `c_evm`
15. `snc`
16. `topo`
17. `proc`
18. `stress`
19. `sn_stress`
20. `nm_stress`
21. `qnx` (non-ZADU extension)
22. `spectral_overlap` (non-ZADU extension)

## Structural Grouping (Core 17)
- Local: `tnc`, `mrre`, `lcmc`, `nh`, `nd`, `ca_tnc`, `proc`
- Cluster-level: `snc`, `dsc`, `ivm`, `c_evm`
- Global: `stress`, `kl_div`, `dtm`, `topo`, `pr`, `srho`
- Additional metrics: `l_tnc`, `sn_stress`, `nm_stress`, `qnx`, `spectral_overlap`

## Parameter-Light Extension Metrics
Two non-ZADU metrics are currently tracked as practical local-structure extensions:
- `qnx`
- `spectral_overlap`

Use these only after task clarification and as part of a bundle with at least one complementary global metric.
Primary source note:
- `papers/notes/2019-spectral-overlap-quality-metrics.md`

## Mandatory Warning Gate
Before relying on `dsc`, `ivm`, `c_evm`, `nh`, `ca_tnc`, verify that class labels are well-separated in the original space.[^warn]

## Recommendation Contract
Every final recommendation should include:
1. primary analytical task
2. selected technique family
3. selected metric IDs with short rationale (strengths + task-fit rationale)
4. selected initialization policy for initialization-sensitive methods
5. warning-gate result (pass/fail/unknown)
6. source-note links used for justification

## Reference-Frequency Priority
When multiple metrics are valid for the same task, prioritize them by PDF-backed support frequency.

1. Use `docs/reference-coverage.md` for ranking decisions.
   - builder-detail view: `builder/evidence/reference-coverage.md`
2. Filter candidates by task fit and warning-gate status first.
3. Rank remaining candidates by:
   - higher `source_pdf_count`
   - then higher `source_pdf_note_count`
4. Use `builder/evidence/conflict-register.md` as a downgrade gate:
   - if a key claim is `contested`, lower the priority by one tier unless exploratory comparison is explicitly requested.

[^zadu-lib]: Source note: `papers/notes/2023-zadu-library.md` (ZADU23-E1, ZADU23-E2).
[^warn]: Warning source note: `papers/notes/2026-zadu-readme-warning.md` (ZADU-RM-E1, ZADU-RM-E2).
