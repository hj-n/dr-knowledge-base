# Metric Relationships and Similarities

This page records which metrics are genuinely similar, which are only partially related, and what distinguishes them.
The goal is to avoid false substitutions during method selection and explanation.

Related:
- Metric catalog: [`docs/metrics/README.md`](./README.md)
- Summary policy: [`docs/metrics-and-libraries.md`](../metrics-and-libraries.md)

## Similarity Rules
- Two metrics are marked **close** only when they measure the same distortion family with closely related computation logic.
- Two metrics are marked **partial overlap** when they share one signal (for example neighborhood overlap) but differ in objective or aggregation.
- If a relation is inferred from formulas but not explicitly claimed by paper authors, it is labeled **inferred**.

## Family View
- Local rank/neighborhood family: `tnc`, `mrre`, `lcmc`, `nd`, `qnx`, `spectral_overlap`
- Label-aware local/class family: `nh`, `ca_tnc`, `l_tnc`, `dsc`, `ivm`, `c_evm`
- Cluster-level distortion family: `snc`
- Global distance/order family: `stress`, `sn_stress`, `nm_stress`, `pr`, `srho`, `kl_div`, `dtm`, `proc`, `topo`

## Per-Metric Similarity Map
| Metric | Closest Metrics | Relationship Type | Why Similar | Key Difference |
|---|---|---|---|---|
| `tnc` | `mrre`, `lcmc` | close | All are co-ranking/neighborhood-rank measures for local preservation. | `tnc` separates trustworthiness (intrusions) and continuity (extrusions). |
| `mrre` | `tnc`, `lcmc` | close | Built on the same neighborhood-rank comparison setting as T&C. | Adds relative rank-error magnitude terms instead of only overlap-style penalties. |
| `lcmc` | `tnc`, `mrre`, `qnx` | close | Uses neighborhood-overlap counts with baseline correction from co-ranking structure. | Emphasizes true-neighbor overlap rather than directional intrusion/extrusion decomposition. |
| `nd` | `tnc`, `mrre`, `snc` | partial overlap (inferred) | Compares neighborhood-change behavior and bidirectional distortion patterns. | Uses matrix/neighbor-dissimilarity representation rather than canonical co-ranking formulas. |
| `qnx` | `lcmc`, `tnc` | close | Aggregates co-ranking neighborhood-preservation terms over K. | Designed as a parameter-free summary over neighborhood scales. |
| `spectral_overlap` | `qnx`, `lcmc` | partial overlap | Both rely on KNN-graph neighborhood preservation behavior. | Spectral Overlap aggregates overlap through a spectral/graph-overlap framing. |
| `nh` | `ca_tnc`, `dsc` | partial overlap | All use label information to evaluate class-related embedding behavior. | NH is local same-label neighborhood purity only. |
| `ca_tnc` | `nh`, `l_tnc` | partial overlap | All are label-aware and direction-sensitive to class distortions. | CA-TNC is neighborhood-based class-aware T&C variant, not class-pair CLM matrix comparison. |
| `l_tnc` | `ca_tnc`, `dsc` | partial overlap | All evaluate class-related reliability with distortion direction awareness. | Label-T&C compares class-label matching between original and embedded spaces via class-pair matrices. |
| `dsc` | `ivm`, `c_evm`, `nh` | partial overlap | All are used for class-separation-oriented evaluation. | DSC is nearest-centroid/class-consistency style and can be used as a CVM inside Label-T&C. |
| `ivm` | `c_evm`, `dsc` | partial overlap | All evaluate cluster/class separability quality. | IVM uses internal cluster validity criteria (for example silhouette/DB style) without external label agreement objective. |
| `c_evm` | `ivm`, `dsc` | partial overlap | Same class/cluster quality space as IVM and DSC. | Requires clustering output and external label agreement (for example ARI/NMI style). |
| `snc` | `tnc`, `mrre`, `l_tnc` | partial overlap | All are directional distortion diagnostics. | SNC is explicitly inter-cluster reliability (Missing/False Groups), not point-neighbor rank distortion. |
| `stress` | `sn_stress`, `nm_stress`, `pr` | close/partial overlap | All target global distance/order faithfulness. | Raw/normalized stress uses distance residuals; PR is correlation, not squared residual fit. |
| `sn_stress` | `stress`, `nm_stress` | close | Same stress family with normalization variants. | Scale sensitivity differs; normalized forms are not automatically scale-invariant. |
| `nm_stress` | `stress`, `srho` | partial overlap | Both evaluate monotonic/global order consistency. | Non-metric stress optimizes monotonic fit function; SRHO is rank-correlation statistic. |
| `pr` | `srho`, `stress` | partial overlap | All compare pairwise-distance relationships between spaces. | PR is linear correlation; SRHO is rank-based; stress is residual-based. |
| `srho` | `pr`, `nm_stress` | partial overlap | All compare order/relationship of pairwise distances globally. | SRHO is rank-order monotonicity only, insensitive to linear scaling magnitude. |
| `kl_div` | `tnc`, `stress` | partial overlap (inferred) | KL-based embedding quality is sensitive to neighborhood-probability mismatch and global distortions under scale changes. | Asymmetric divergence on probability neighborhoods, not symmetric rank or residual distance metric. |
| `dtm` | `stress`, `kl_div` | partial overlap (inferred) | Used as a global distortion reliability signal in DR metric benchmark settings. | Built from distance-to-measure geometric robustness framework rather than pairwise residual/correlation forms. |
| `proc` | `tnc`, `stress`, `pr` | partial overlap | Uses geometric agreement between original and embedded local structures. | Procrustes aligns local neighborhoods with rigid transforms before scoring residuals. |
| `topo` | `tnc`, `nd` | partial overlap | All diagnose neighborhood-order preservation. | Topographic Product is SOM/topology-oriented and additionally signals output-dimension mismatch direction. |

## Core Evidence Base
- Lee & Verleysen (2009), *Quality assessment of dimensionality reduction: Rank-based criteria*.
- Jeon et al. (2021), *Measuring and Explaining the Inter-Cluster Reliability of Multidimensional Projections*.
- Jeon et al. (2024), *Classes are Not Clusters: Improving Label-Based Evaluation of Dimensionality Reduction*.
- Sips et al. (2009), *Selecting good views of high-dimensional data using class consistency*.
- Goldberg & Ritov (2009), *Local procrustes for manifold embedding*.
- Bauer & Pawelzik (1992), *Quantifying the Neighborhood Preservation of Self-Organizing Feature Maps*.
- Smelser et al. (2024/2025), stress scale-sensitivity analyses.
- Johannemann & Tibshirani (2019), *Spectral Overlap and a Comparison of Parameter-Free DR Quality Metrics*.

## Usage Policy
- Do not replace one metric with another only because they are in the same family.
- For final selection, combine at least one local signal and one global signal; add class-aware metrics only when labels are valid for the user’s goal.
- When two close metrics disagree materially, report both and lower confidence instead of averaging away the conflict.
