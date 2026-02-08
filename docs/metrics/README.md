# Metrics Directory

This directory provides detailed metric guidance for DR reliability analysis.
Each metric file explains what is computed, how it is computed, major sensitivities, and notable properties.

Related:
- Workflow step anchor: [`docs/workflow/dr-analysis-workflow.md`](../workflow/dr-analysis-workflow.md) (Step 3)
- Selection policy: [`docs/metrics-and-libraries.md`](../metrics-and-libraries.md)
- Frequency ranking: [`docs/reference-coverage.md`](../reference-coverage.md)
- Technique catalog: [`docs/techniques/README.md`](../techniques/README.md)

## Required Sections
- Metric Definition
- What It Quantifies
- Computation Outline
- Hyperparameter Impact
- Notable Properties
- Task Alignment
- Interpretation Notes
- Source Notes

## Coverage
- Metrics tracked: 20
- Core set from ZADU paper: 17
- Additional tracked metrics: `l_tnc`, `sn_stress`, `nm_stress`

## Warning Gate
Label-separation-sensitive metrics (`dsc`, `ivm`, `c_evm`, `nh`, `ca_tnc`) require label-separation validation before strong interpretation.
