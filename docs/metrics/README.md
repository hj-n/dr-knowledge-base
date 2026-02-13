# Metrics Directory

This directory provides detailed metric guidance for DR reliability analysis.
Each metric file explains what is computed, how it is computed, major sensitivities, and notable properties.

Related:
- Workflow step anchor: [`docs/workflow/dr-analysis-workflow.md`](../workflow/dr-analysis-workflow.md) (Step 3)
- Task categories and subtasks: [`docs/task-taxonomy.md`](../task-taxonomy.md)
- Selection policy: [`docs/metrics-and-libraries.md`](../metrics-and-libraries.md)
- Deterministic scoring policy: [`docs/workflow/configuration-selection-policy.md`](../workflow/configuration-selection-policy.md)
- Frequency ranking: [`docs/reference-coverage.md`](../reference-coverage.md)
- Grouped reliability cautions: [`docs/reliability-cautions-and-tips.md`](../reliability-cautions-and-tips.md)
- Technique catalog: [`docs/techniques/README.md`](../techniques/README.md)
- Similarity map: [`docs/metrics/metric-relationships.md`](./metric-relationships.md)

## Required Sections
- Metric Definition
- What It Quantifies
- Computation Outline
- Hyperparameter Impact
- Practical Reliability Notes
- Notable Properties
- Strengths
- Related Metrics
- Task Alignment
- Interpretation Notes
- Source Notes

Expectation:
- `Practical Reliability Notes` should contain operation-level guidance tied to failure modes, not generic boilerplate.

## Coverage
- Metrics tracked: 22
- Core set from ZADU paper: 17
- Additional tracked metrics: `l_tnc`, `sn_stress`, `nm_stress`, `qnx`, `spectral_overlap`
- ZADU is the default set, but non-ZADU metrics may be added with explicit source-note provenance.

## Non-ZADU Metric Onboarding
When adding a metric not present in ZADU:
- Create `docs/metrics/<metric-id>.md` with all required sections.
- In `Source Notes`, include the source-note links that justify:
  - metric definition
  - intended use scope
  - caveats/limitations
- Use a unique `snake_case` metric ID and avoid collisions with existing IDs.

## Warning Gate
Label-separation-sensitive metrics (`dsc`, `ivm`, `c_evm`, `nh`, `ca_tnc`) require label-separation validation before strong interpretation.
