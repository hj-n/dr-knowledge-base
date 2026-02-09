# Metrics and Libraries

Related:
- Workflow anchor: [`docs/workflow/dr-analysis-workflow.md`](./workflow/dr-analysis-workflow.md)
- Task confirmation prerequisite: [`docs/workflow/task-confirmation-protocol.md`](./workflow/task-confirmation-protocol.md)
- Selection scoring policy: [`docs/workflow/configuration-selection-policy.md`](./workflow/configuration-selection-policy.md)
- Task taxonomy: [`docs/task-taxonomy.md`](./task-taxonomy.md)
- Metric catalog: [`docs/metrics/README.md`](./metrics/README.md)
- Technique catalog: [`docs/techniques/README.md`](./techniques/README.md)
- Coverage ranking: [`docs/reference-coverage.md`](./reference-coverage.md)

## Default Library
- Use `zadu` as the default reliability-analysis metric set.
- Keep metric IDs exactly as documented in this page.

## User-Layer Wording Rule
- In end-user explanations, do not expose internal terms from this page.
- Prefer plain wording:
  - `main goal`
  - `reliability checks`
  - `safety check`

## Task-First Rule
- Do not pick metrics before task confirmation (`axis_confidence = high`).
- Use one primary axis; optional subtask only refines within axis-valid candidates.

## Optimal Selection Mode (Mandatory for "best/optimal" requests)
When the user asks for the best/optimal DR configuration:
- compare all techniques listed under the selected task in this document
- compare all task-aligned metrics listed for that task (primary + safety check metrics)
- do not skip aligned candidates unless a hard-gate failure is recorded
- record excluded candidates with explicit reasons

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
21. `qnx`
22. `spectral_overlap`

## Structural Grouping
- Local: `tnc`, `mrre`, `lcmc`, `nh`, `nd`, `ca_tnc`, `proc`
- Cluster-level: `snc`, `dsc`, `ivm`, `c_evm`
- Global: `stress`, `kl_div`, `dtm`, `topo`, `pr`, `srho`
- Additional: `l_tnc`, `sn_stress`, `nm_stress`, `qnx`, `spectral_overlap`

## Mandatory Label-Separation Check
Before relying on class-aware metrics (`dsc`, `ivm`, `c_evm`, `nh`, `ca_tnc`), validate class separability in the original space.

If the check is `fail` or `unknown`:
- class-aware metrics cannot be main scoring metrics
- keep at least one local and one global label-agnostic metric in the comparison set

## Task-Aligned Metric Set Contract
Each comparison set must include:
- one main metric aligned to the main goal
- one safety check metric from a different structural level
- optional third metric for tie-break

## Task-to-Metric Starter Bundles
1. Neighborhood identification:
   - primary: `tnc`, `nh`, `nd`
   - safety check: `stress`
2. Outlier identification:
   - primary: `tnc`, `nd`, `lcmc`
   - safety check: `stress`
3. Cluster identification:
   - primary: `tnc`, `snc`, `nh`
   - safety check: `topo` or `stress`
4. Point distance investigation:
   - primary: `stress`, `kl_div`, `pr`
   - safety check: `tnc` or `proc`
5. Class separability investigation:
   - primary: `dsc`, `ivm`, `c_evm`
   - safety check: `tnc` or `proc`
6. Cluster distance investigation:
   - primary: `snc`, `stress`, `pr`
   - safety check: `topo`
7. Cluster density investigation:
   - primary: `stress`, `kl_div`, `topo`
   - safety check: `tnc` or `proc`

## Task-to-Technique Starter Candidates
1. Neighborhood identification:
   - primary: `t-sne`, `umap`, `lle`, `laplacian_eigenmaps`
2. Outlier identification:
   - primary: `umap`, `t-sne`, `lle`
3. Cluster identification:
   - primary: `umap`, `t-sne`, `som`, `classimap`
4. Point distance investigation:
   - primary: `pca`, `mds`, `isomap`
5. Class separability investigation:
   - primary: `classnerv`, `classimap`, `catsne`
6. Cluster distance investigation:
   - primary: `pca`, `mds`, `isomap`
7. Cluster density investigation:
   - primary: `pca`, `mds`, `isomap`

## Deterministic Selection Rule
Candidate selection must follow `docs/workflow/configuration-selection-policy.md`.
No ad-hoc final ranking is allowed.

Minimum acceptance for production recommendation:
- `selection_status = accepted`
- label-separation check resolved
- initialization stability reported
- safety check consistency reported

## Coverage Priority Rule
When candidates remain valid after hard gates:
1. rank by deterministic total score
2. if tied, prefer higher PDF support frequency
3. down-rank `unknown` conflict status by one tier
4. down-rank `contested` by one additional tier

## Non-ZADU Metric Extension Policy
Non-ZADU metrics are allowed only when:
- task requires behavior not covered by current ZADU set
- definition/use/caveat claims have explicit `papers/notes/*` provenance
- metric ID is unique `snake_case`
- confidence is marked conservatively when evidence is thin
