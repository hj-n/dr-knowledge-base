# Metrics and Libraries

Related:
- Workflow step anchor: [`docs/workflow/dr-analysis-workflow.md`](./workflow/dr-analysis-workflow.md) (Step 3)
- Task clarification prerequisite: [`docs/intake-question-tree.md`](./intake-question-tree.md)
- Metric catalog: [`docs/metrics/README.md`](./metrics/README.md)
- Technique catalog: [`docs/techniques/README.md`](./techniques/README.md)
- Frequency ranking: [`docs/reference-coverage.md`](./reference-coverage.md)

## Default Library
- Use `zadu` as the default reliability-analysis library for DR embeddings.[^zadu-lib]
- Keep metric IDs exactly as defined in the library (no custom renaming).

## Task-First Rule
- Do not pick metrics before clarifying the user's primary analytical task.
- After task clarification, choose a small metric set across local/cluster/global levels.

## Metric IDs (20)
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

## Structural Grouping (Core 17)
- Local: `tnc`, `mrre`, `lcmc`, `nh`, `nd`, `ca_tnc`, `proc`
- Cluster-level: `snc`, `dsc`, `ivm`, `c_evm`
- Global: `stress`, `kl_div`, `dtm`, `topo`, `pr`, `srho`
- Additional metrics: `l_tnc`, `sn_stress`, `nm_stress`

## Mandatory Warning Gate
Before relying on `dsc`, `ivm`, `c_evm`, `nh`, `ca_tnc`, verify that class labels are well-separated in the original space.[^warn]

## Recommendation Contract
Every final recommendation should include:
1. primary analytical task
2. selected technique family
3. selected metric IDs with short rationale
4. warning-gate result (pass/fail/unknown)
5. source-note links used for justification

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
