# l_tnc - Label Trustworthiness and Label Continuity

## Metric Definition
`l_tnc` evaluates whether class relationships in a low-dimensional embedding are faithful to class relationships in the original high-dimensional space. The metric family is explicitly designed to avoid the common mistake of rewarding embeddings only for visual class separation.

The core idea is to compare class-label matching in both spaces, then measure how much that matching is distorted by projection. This produces two complementary scores: one focused on false-group distortions (Label-Trustworthiness) and one focused on missing-group distortions (Label-Continuity).

## What It Quantifies
This metric quantifies class-pair distortion, not just class compactness in the embedding. A high score means class relationships in the embedding remain close to the class relationships observed in the original data.

It is therefore a reliability metric for class-based interpretation. It should be used when users want to make claims such as "class A is clearly separated from class B" and need that claim to be faithful to the original feature space, not only visually convenient in 2D.

## Computation Outline
`l_tnc` is computed in three explicit steps.

1. Build class-pairwise class-label-matching matrices in both spaces, `M(X)` and `M(Z)`, using a clustering-validation measure (CVM) for every class pair.
2. Compute a distortion matrix `M* = M(X) - M(Z)`, then split it into:
   - `MFG` for positive distortion entries (False Groups)
   - `MMG` for negative distortion magnitudes (Missing Groups)
3. Aggregate upper-triangular entries into two scores:
   - Label-Trustworthiness: `1 - avg(MFG)`
   - Label-Continuity: `1 - avg(MMG)`

Higher values indicate fewer class-relationship distortions. Both scores must be interpreted together, because improving one direction can degrade the other.

## Hyperparameter Impact
The most important hyperparameter choice is the CVM used inside the class-pair matrix construction. The paper defines explicit requirements for CVM validity in this framework: scale invariance, shift invariance, range invariance, and robustness to hyperparameter changes.

If a CVM violates these requirements, `l_tnc` can become unstable across datasets or dimensions. The source specifically positions Distance Consistency (with normalization) and CHbtwn as suitable CVM candidates under these constraints.

## Practical Reliability Notes
`l_tnc` should not be treated as "more class separation is always better." Its purpose is to evaluate fidelity of class structure relative to the original space. If classes overlap in the original space, forcing clean visual separation can be a reliability error, not a success.

In recommendation workflows, report Label-Trustworthiness and Label-Continuity together, and explicitly state which distortion type is being reduced. A single aggregated statement can hide tradeoffs and overstate confidence.

## Notable Properties
This metric family is asymmetry-aware with respect to distortion direction: false-group and missing-group distortions are separated rather than mixed into one value. That makes it useful for explaining why two embeddings that look similarly "clean" can still differ in reliability.

Another notable property is that it is class-pairwise by construction. This allows granular diagnosis of which class relationships are being preserved or broken, instead of collapsing all classes into one coarse score.

## Strengths
`l_tnc` is strong when the analysis objective is class-relation reliability and labels are trusted. It gives a direct answer to whether class patterns shown in the embedding are faithful to class patterns in the original data.

It is also strong for communicating risk: the two-score structure naturally supports explanations of what type of distortion remains and what downstream interpretation can become unreliable.

## Task Alignment
Best-aligned tasks:
- Class separability investigation
- Cluster identification (label-aware setting)
- Cluster distance investigation (label-aware setting)

For label-agnostic tasks such as pure neighborhood or outlier analysis without class semantics, use this metric as optional supporting evidence rather than primary ranking evidence.

## Interpretation Notes
Read `l_tnc` under a fixed preprocessing and distance policy. Changing preprocessing, scaling, or label filtering can change scores without any change in embedding method quality.

When this metric disagrees with label-agnostic local/global metrics, report the disagreement explicitly. Do not average away the conflict; disagreement is itself important reliability information.

## Source Notes
- Classes are Not Clusters: Improving Label-Based Evaluation of Dimensionality Reduction (Hyeon Jeon et al., IEEE Transactions on Visualization and Computer Graphics, 2024)
- ZADU README Operational Warning for Label-Separation-Sensitive Metrics (hj-n/zadu maintainers, GitHub README, 2026)

[^z11]: Classes are Not Clusters: Improving Label-Based Evaluation of Dimensionality Reduction (Hyeon Jeon et al., IEEE Transactions on Visualization and Computer Graphics, 2024)
