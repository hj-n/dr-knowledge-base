---
id: paper-2011-zadu-ref-08
title: "Local Affine Multidimensional Projection"
year: 2011
tags: [dr, zadu-table1-reference, ivm, proc, stress, tnc]
source_pdf: papers/raw/zadu-table1-references/Local_Affine_Multidimensional_Projection (1).pdf
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- —Multidimensional projection techniques have experienced many improvements lately , mainly regarding computational times and accuracy .
- However, existing methods do not yet provide ﬂexible enough mechanisms for visualization-oriented fully in- teractive applications.

# Method Summary
- As we show in Section 4, besides resulting in highly accurate mappings, the mathematical con- struction described above turns out to be also competitive in terms of computational times.
- First proposed by Kruskal [21], nonlinear-optimization-based tech- niques comprise the class of global methods that accomplish the map- ping to visual space by ﬁnding a minimum for an energy function, usually called stress function.
- [27] proposed a technique that ﬁrst embeds a subset of samples in the visual space by optimizing a stress function and then places the remaining instances using a global linear mapping, resulting in an O(k 3 + kn) al- gorithm.
- The same limitation can be observed in the recent linear mapping called PLMP [26] (whose complexity is linear), which also makes use of a subset of samples to deﬁne a global linear map.

# When To Use / Not Use
- Use when:
  - Use when selecting DR reliability checks in workflow Step 3.
  - Use with complementary local/cluster/global metrics rather than a single score.
- Avoid when:
  - Avoid using this source as the only decision signal without task constraints.
- Failure modes:
  - Overconfident conclusions when class labels are not well-separated in original space.

# Metrics Mentioned
- `ivm`: internal validation view of cluster structure (label-separation-sensitive)
- `proc`: local shape agreement via Procrustes
- `stress`: distance-fitting distortion objective/metric
- `tnc`: local neighborhood trustworthiness/continuity balance

# Implementation Notes
- Runtime/complexity signal: The same limitation can be observed in the recent linear mapping called PLMP [26] (whose complexity is linear), which also makes use of a subset of samples to deﬁne a global linear map.
- If labels are weakly separated in original space, down-weight label-separation-sensitive metrics in final justification.

# Claim Atoms (For Conflict Resolution)
- CLAIM-SOURCE-08-CORE | stance: support | summary: This source introduces local Procrustes-style neighborhood shape agreement for embedding quality. | evidence_ids: ZR08-E1
- CLAIM-METRIC-IVM-SOURCE-08 | stance: support | summary: This source uses or discusses `ivm` for internal validation view of cluster structure in dimensionality-reduction evaluation. | evidence_ids: ZR08-E2
- CLAIM-METRIC-PROC-SOURCE-08 | stance: support | summary: This source uses or discusses `proc` for local shape agreement via Procrustes in dimensionality-reduction evaluation. | evidence_ids: ZR08-E2
- CLAIM-METRIC-STRESS-SOURCE-08 | stance: support | summary: This source uses or discusses `stress` for distance-fitting distortion objective/metric in dimensionality-reduction evaluation. | evidence_ids: ZR08-E2
- CLAIM-METRIC-TNC-SOURCE-08 | stance: support | summary: This source uses or discusses `tnc` for local neighborhood trustworthiness/continuity balance in dimensionality-reduction evaluation. | evidence_ids: ZR08-E2

# Workflow Relevance Map
- step: 3 | relevance: high | note: Informs task-aligned metric/technique selection and metric trust calibration.
- step: 6 | relevance: high | note: Provides rationale that can be translated for end users.

# Evidence
- ZR08-E1 | page: 2, section: extracted, quote: "First proposed by Kruskal [21], nonlinear-optimization-based tech- niques comprise the class of global methods that accomplish the map- ping to visual space by ﬁnding a minimum for an energy function, usually called stress function."
- ZR08-E2 | page: 2, section: extracted, quote: "[27] proposed a technique that ﬁrst embeds a subset of samples in the visual space by optimizing a stress function and then places the remaining instances using a global linear mapping, resulting in an O(k 3 + kn) al- gorithm."
- ZR08-E3 | page: 2, section: extracted, quote: "The same limitation can be observed in the recent linear mapping called PLMP [26] (whose complexity is linear), which also makes use of a subset of samples to deﬁne a global linear map."
- ZR08-E4 | page: 2, section: extracted, quote: "The approach proposed by Chalmers [6] and its hybrid variants [19, 22, 32] ﬁrst map the subset of samples to the visual space through a force-based scheme inspired in an analogy between stress function minimization and mass-spring systems."
- ZR08-E5 | page: 3, section: extracted, quote: "Finally, in contrast to “as-rigid-as-possible” image deformation applications, we do not need to ensure continuity for the overall transformation, on the contrary, discontinuities may be highly desirable to better keep apart uncorrelated data instances dur- ing projection."
- ZR08-E6 | page: 3, section: extracted, quote: "The stress produced by LAMP when the number of control points ranges from 1% to 25% of the total of instances in the data set (see T able 1 for details about the data sets)."
- ZR08-E7 | page: 3, section: extracted, quote: "The minimization problem (5) is a typical example of the so called Orthogonal Procrustes Problem [17], whose solution is known to be M = UV, AT B = UD V (7) where UD V is the singular value decomposition (SVD) of AT B."
- ZR08-E8 | page: 3, section: extracted, quote: "However, A T B is indeed a m× 2 matrix (only two columns), so it can be decomposed very quickly with compact SVD packages [2] ( O(k) operations), resulting in an algorithm with computational complexity equal to O(kn)."
