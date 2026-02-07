# Conflict Register

Use this table to track claim-level conflict decisions.

| claim_id | domain | support_evidence_ids | contradict_evidence_ids | S_score | C_score | decision | last_reviewed |
|---|---|---|---|---:|---:|---|---|
| CLAIM-TASK-7-TAXONOMY | task taxonomy | JEON25-E1 | - | 0.73 | 0.00 | accepted-support | 2026-02-07 |
| CLAIM-TECH-LOCAL-TSNE-UMAP | technique suitability | JEON25-E2 | - | 0.73 | 0.00 | accepted-support | 2026-02-07 |
| CLAIM-TECH-GLOBAL-PCA-MDS | technique suitability | JEON25-E3, JEON25-E4, JEON25-E5, JEON25-E6 | - | 0.73 | 0.00 | accepted-support | 2026-02-07 |
| CLAIM-ZADU-GRANULARITY-GROUPING | metric grouping | ZADU23-E2, ZADU23-E3, ZADU23-E4, ZADU23-E5 | - | 0.73 | 0.00 | accepted-support | 2026-02-07 |
| CLAIM-ZADU-LABEL-SEPARABILITY-WARNING | metric caveat | ZADU-RM-E1, ZADU-RM-E2 | - | 0.73 | 0.00 | accepted-support | 2026-02-07 |

Notes:
- Initial scores assume one high-confidence source family and no contradicting source.
- Recalculate with the policy formula when conflicting evidence is added.

<!-- AUTO_METRIC_COVERAGE_START -->
| CLAIM-METRIC-CA_TNC-LITERATURE-COVERAGE | metric behavior | ZR11 | - | 0.73 | 0.00 | accepted-support | 2026-02-08 |
| CLAIM-METRIC-C_EVM-LITERATURE-COVERAGE | metric behavior | ZR11, ZR19 | - | 0.73 | 0.00 | accepted-support | 2026-02-08 |
| CLAIM-METRIC-DSC-LITERATURE-COVERAGE | metric behavior | ZR03, ZR04, ZR05, ZR11 | - | 0.73 | 0.00 | accepted-support | 2026-02-08 |
| CLAIM-METRIC-DTM-LITERATURE-COVERAGE | metric behavior | ZR11, ZR13 | - | 0.73 | 0.00 | accepted-support | 2026-02-08 |
| CLAIM-METRIC-IVM-LITERATURE-COVERAGE | metric behavior | ZR08, ZR11, ZR18, ZR19 | - | 0.73 | 0.00 | accepted-support | 2026-02-08 |
| CLAIM-METRIC-KL_DIV-LITERATURE-COVERAGE | metric behavior | ZR03, ZR04, ZR11, ZR14, ZR17 | - | 0.73 | 0.00 | accepted-support | 2026-02-08 |
| CLAIM-METRIC-LCMC-LITERATURE-COVERAGE | metric behavior | ZR02, ZR18 | - | 0.73 | 0.00 | accepted-support | 2026-02-08 |
| CLAIM-METRIC-L_TNC-LITERATURE-COVERAGE | metric behavior | ZR11 | - | 0.73 | 0.00 | accepted-support | 2026-02-08 |
| CLAIM-METRIC-MRRE-LITERATURE-COVERAGE | metric behavior | ZR02, ZR03, ZR04, ZR11, ZR18 | - | 0.73 | 0.00 | accepted-support | 2026-02-08 |
| CLAIM-METRIC-ND-LITERATURE-COVERAGE | metric behavior | ZR15, ZR18 | - | 0.73 | 0.00 | accepted-support | 2026-02-08 |
| CLAIM-METRIC-NH-LITERATURE-COVERAGE | metric behavior | ZR04 | - | 0.73 | 0.00 | accepted-support | 2026-02-08 |
| CLAIM-METRIC-NM_STRESS-LITERATURE-COVERAGE | metric behavior | ZR04 | - | 0.73 | 0.00 | accepted-support | 2026-02-08 |
| CLAIM-METRIC-PR-LITERATURE-COVERAGE | metric behavior | ZR04, ZR14, ZR15, ZR18 | - | 0.73 | 0.00 | accepted-support | 2026-02-08 |
| CLAIM-METRIC-PROC-LITERATURE-COVERAGE | metric behavior | ZR08, ZR15, ZR16 | - | 0.73 | 0.00 | accepted-support | 2026-02-08 |
| CLAIM-METRIC-SNC-LITERATURE-COVERAGE | metric behavior | ZR03, ZR04, ZR11, ZR15, ZR18 | - | 0.73 | 0.00 | accepted-support | 2026-02-08 |
| CLAIM-METRIC-SN_STRESS-LITERATURE-COVERAGE | metric behavior | ZR03, ZR04 | - | 0.73 | 0.00 | accepted-support | 2026-02-08 |
| CLAIM-METRIC-SRHO-LITERATURE-COVERAGE | metric behavior | ZR03, ZR04, ZR15 | - | 0.73 | 0.00 | accepted-support | 2026-02-08 |
| CLAIM-METRIC-STRESS-LITERATURE-COVERAGE | metric behavior | ZR02, ZR03, ZR04, ZR06, ZR07, ZR08, ZR12, ZR13, ZR14, ZR17, ZR18 | - | 0.73 | 0.00 | accepted-support | 2026-02-08 |
| CLAIM-METRIC-TNC-LITERATURE-COVERAGE | metric behavior | ZR01, ZR02, ZR03, ZR04, ZR07, ZR08, ZR11, ZR14, ZR16, ZR18 | - | 0.73 | 0.00 | accepted-support | 2026-02-08 |
| CLAIM-METRIC-TOPO-LITERATURE-COVERAGE | metric behavior | ZR10 | - | 0.73 | 0.00 | accepted-support | 2026-02-08 |
<!-- AUTO_METRIC_COVERAGE_END -->
