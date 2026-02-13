# ca_tnc - Class-Aware Trustworthiness & Continuity

## Metric Definition
This metric extends trustworthiness and continuity using label-aware decomposition. It distinguishes class-preserving versus class-breaking neighborhood errors.

Operationally, treat this metric as a formal lens on one distortion family rather than a universal quality score. Two embeddings can rank differently depending on whether the task prioritizes local neighborhoods, global geometry, or class structure, so the definition should be interpreted together with explicit task intent.

For reproducible comparisons, keep preprocessing, distance definition, and evaluation protocol fixed while reading this metric. If those upstream choices change between runs, score differences often reflect evaluation drift rather than genuine embedding improvement.

## What It Quantifies
It quantifies class-conditioned neighborhood trust and continuity distortions. It exposes whether errors happen mostly within classes or across class boundaries.

In practical analysis, this score is most useful when you pair it with the failure mode you are trying to detect. A score increase is meaningful only if it reduces errors that matter for the declared analytical task, not just because the numeric value is higher.

This is why the metric should be read as task-conditioned evidence. Use it to answer a concrete question about neighborhood stability, class organization, distance behavior, or density behavior, then validate that interpretation with at least one complementary metric.

## Computation Outline
This outline describes the typical computational flow used in DR evaluation practice. Exact formula details may vary by implementation, but the structure below is stable across references.
- Require labels and choose class-aware neighborhood setup.
- Compute trustworthiness/continuity-style neighborhood errors.
- Decompose errors into within-class and cross-class components.
- Aggregate component scores for final class-aware interpretation.

The computation should be implemented with a stable protocol: identical sampling policy, consistent distance backend, and fixed tie-breaking behavior. Without these controls, the same embedding can yield materially different results across runs and tools.

When reporting values, record the full evaluation context including neighborhood scale, normalization policy, and whether labels were required. That metadata is part of the metric definition in practice because it determines what the reported number actually means.

Detailed protocol rule: compute under a fixed label policy (including unknown/missing labels) and fixed neighborhood scale. Label preprocessing changes can produce large score shifts that do not reflect embedding changes.

## Hyperparameter Impact
Class-aware neighborhood decomposition depends on `k` and class-partition assumptions. Class-noise and weak separation can destabilize the score meaning.
The label-separation gate is mandatory before strong interpretation in labeled settings.

Hyperparameters should be tuned against the declared task, not against a single metric in isolation. Otherwise, optimization can overfit one structural aspect and silently degrade other structure that downstream users care about.

A robust workflow evaluates sensitivity with Bayesian optimization under fixed search bounds and checks rank stability across seeds or folds. Large score variance indicates that the current configuration is not yet reliable enough for high-confidence method selection.

Decision-level tuning rule: label-conditioned settings must be checked with the label-separation gate before tuning-driven decisions. If separability is weak, down-weight this metric and raise uncertainty in the final recommendation.

## Practical Reliability Notes
Class-aware TNC is most useful when the analytical goal is explicitly tied to class-boundary reliability. It separates within-class and cross-class neighborhood errors, which helps explain whether quality loss is due to class mixing or local manifold noise.

Treat CA-TNC as label-conditional evidence only. If labels are weak, noisy, or only partially aligned with the current task, CA-TNC can dominate selection in the wrong direction. In those cases, keep CA-TNC as a secondary metric and require agreement with label-agnostic local metrics before final method ranking.

## Notable Properties
It clarifies whether local distortions are class-preserving or class-breaking. It is valuable for class-aware diagnostics but depends on label validity.

A strong property of this metric is that it provides a compact diagnostic that is easy to compare across methods. The limitation is that compactness hides where errors occur, so it should be supplemented by structure-level inspection when decisions are high impact.

In review workflows, this metric works best as one component in a bundle: local, global, and label-aware signals together. That bundle-based interpretation reduces the chance of selecting a method that is numerically strong but operationally misaligned.

## Strengths
This metric is strong for decomposing local distortions into class-preserving versus class-breaking components. It adds diagnostic depth beyond plain trustworthiness/continuity by showing where class boundaries are respected or violated.

It is particularly useful for class-centric analyses where local errors near boundaries have higher decision impact than within-class perturbations.

## Related Metrics
Class-Aware Trustworthiness and Continuity is closest to Neighborhood Hit and Label-Trustworthiness/Continuity because all three use class labels to evaluate projection reliability.

It differs from Label-T&C by staying in a neighborhood-rank decomposition framework. Label-T&C instead compares class-pair class-label matching matrices between original and embedding spaces.

## Task Alignment
This metric is best aligned to the task set implied by its structural role. The alignment basis is structural-granularity grouping from ZADU source note.
- Best-aligned tasks:
  - Neighborhood identification
  - Outlier identification
  - Cluster identification

Alignment here should be treated as a recommendation priority, not a hard constraint. If a project objective spans multiple task types, combine metrics from each relevant task family and require consistency before finalizing a method choice.

When alignment is uncertain, prefer conservative interpretation and run clarification questions again. The task decision should remain primary, and metric selection should follow that decision rather than drive it.

Operational alignment rule: this metric can prioritize candidates inside an already-selected main goal, but it must not redefine the task itself. If metric preference and user task conflict, keep task intent as the hard constraint.

## Interpretation Notes
Do not treat this metric as a standalone final decision criterion. Use it together with complementary metrics from other structural levels and keep preprocessing/seed policies fixed during comparison.

Use absolute values cautiously and prioritize relative comparisons under matched conditions. Threshold-style decisions without protocol control often produce false certainty, especially when datasets differ in scale, density, or class balance.

Before communicating a conclusion, cross-check this metric against the selected technique behavior and user-facing goal. A reliable recommendation should explain both why the score is good and why that goodness matters for the intended analytical action.

Failure-signaling rule: if this metric disagrees with other bundle metrics, report that disagreement explicitly and mark recommendation confidence as reduced instead of averaging away the conflict.

## Source Notes
The references below list paper sources used for this metric guidance.

- Classes are Not Clusters: Improving Label-Based Evaluation of Dimensionality Reduction (Hyeon Jeon, Yun-Hsin Kuo, Michaël Aupetit, Kwan-Liu Ma, Jinwook Seo, IEEE Transactions on Visualization and Computer Graphics, 2024)
