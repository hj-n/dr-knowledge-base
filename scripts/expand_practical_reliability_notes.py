#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

MAPPING = {
    # metrics (missing set)
    "docs/metrics/ca_tnc.md": """Class-aware TNC is most useful when the analytical goal is explicitly tied to class-boundary reliability. It separates within-class and cross-class neighborhood errors, which helps explain whether quality loss is due to class mixing or local manifold noise.

Treat CA-TNC as label-conditional evidence only. If labels are weak, noisy, or only partially aligned with the current task, CA-TNC can dominate selection in the wrong direction. In those cases, keep CA-TNC as a secondary metric and require agreement with label-agnostic local metrics before final method ranking.

""",
    "docs/metrics/dtm.md": """DTM-style distances are sensitive to sampling density and neighborhood scale. In sparse regions, metric values can change more due to sample coverage than due to embedding quality itself, so interpretation should include data-density context.

For robust comparison, keep the same sample subset and distance backend across runs. If DTM disagrees with rank-based local metrics, do not collapse them into a single score immediately; inspect whether disagreement is concentrated in sparse tails, outliers, or class-boundary regions.

""",
    "docs/metrics/l_tnc.md": """Label TNC is useful for class-aware local trust analysis, but it should not be interpreted as a replacement for plain TNC. A high L-TNC can coexist with degraded geometry for unlabeled structure, especially when labels capture only one perspective of the data.

In practice, run L-TNC and TNC together and check divergence between them. Large divergence indicates that class semantics and geometric neighborhoods are pulling in different directions; this should be reported as a model-selection tradeoff, not hidden by averaging.

""",
    "docs/metrics/lcmc.md": """LCMC is sensitive to neighborhood scale selection and is best interpreted as a curve across scales rather than a single point estimate. Single-k reporting can overstate confidence by hiding where methods cross in quality.

Use LCMC as a ranking support metric after task clarification, especially for neighborhood/cluster exploration. For production recommendations, pair it with at least one global guardrail metric so local improvements do not mask global collapse.

""",
    "docs/metrics/mrre.md": """MRRE captures rank distortion magnitude and is useful for identifying how severely neighborhood order is perturbed by projection. It is often more interpretable when reported per-k band (very local, local, mid-range) than as one aggregate value.

When MRRE improves while trust-continuity balance worsens, avoid declaring a universal win. That pattern often indicates one distortion type is being traded for another; include both findings in the final explanation and align choice to the declared task.

""",
    "docs/metrics/nd.md": """Neighbor dissimilarity responds strongly to graph-construction policy. Small differences in kNN tie-breaking, metric backend, or duplicate handling can change ND values even on the same embedding.

For reliability-focused comparisons, freeze graph policy and run seed-stability checks for stochastic methods. If ND ranking is unstable across seeds while other local metrics are stable, treat ND as exploratory evidence and avoid over-weighting it in final selection.

""",
    "docs/metrics/nm_stress.md": """Normalized stress variants improve comparability across scales, but normalization choice itself is part of the model. Different normalization conventions can produce different rankings; document the exact variant and denominator policy.

Use NM-Stress when global-structure tasks require cross-method comparability under controlled scaling. Do not interpret NM-Stress alone for local tasks; combine it with local rank/neighborhood metrics before turning values into recommendations.

""",
    "docs/metrics/pr.md": """Pearson-style correlation is a coarse global trend indicator and can remain high even when local neighborhoods are heavily damaged. It is best for detecting monotonic global agreement, not for validating neighborhood-level interpretability.

In workflow decisions, treat PR as a guardrail for distance-oriented tasks. If PR is high but local metrics are poor, report that global trend is preserved while local reliability is not, and avoid using the embedding for neighborhood-sensitive analysis.

""",
    "docs/metrics/qnx.md": """QNX is useful for quantifying neighborhood retention across rank ranges with low implementation overhead. It is practical in iterative tuning loops where fast local-quality feedback is needed.

Because QNX can be sensitive to neighborhood-range definition, publish the evaluated range explicitly. If candidate methods are close on QNX, break ties using task-aligned secondary metrics and stability checks rather than tiny QNX deltas.

""",
    "docs/metrics/sn_stress.md": """SN-Stress focuses on stress behavior under scale-normalized settings and is helpful when comparing methods with different natural embedding scales. It reduces some scale artifacts but does not remove all preprocessing dependencies.

Use SN-Stress as part of global metric bundles for cluster-distance and density tasks. Pair it with topology or neighborhood metrics when decisions affect local interpretation, since stress-family metrics alone can hide local rearrangements.

""",
    "docs/metrics/snc.md": """SNC-style metrics target inter-cluster reliability and are useful when cluster relations are part of the explicit task. They often detect cluster-level distortions that neighborhood-only metrics can miss.

Cluster metrics can still be confounded by cluster-definition policy. Keep clustering or grouping assumptions fixed during comparison; otherwise SNC changes may reflect changing cluster extraction rather than projection reliability.

""",
    "docs/metrics/spectral_overlap.md": """Spectral-overlap metrics provide a structure-aware perspective that can complement rank-based local metrics, especially when manifold smoothness and neighborhood transitions matter. They are useful when simple distance errors do not explain observed visual behavior.

Interpret spectral overlap with caution when data graphs are noisy or under-connected. In those settings, spectral signals may amplify graph artifacts, so combine with robust local/global metrics and inspect whether conclusions remain stable.

""",
    "docs/metrics/srho.md": """Spearman correlation captures rank monotonicity of distances and is robust to some scale effects, making it a useful global-order signal. It is especially informative for tasks where relative ordering matters more than exact distance magnitude.

However, high SRHO does not guarantee good local neighborhoods. Keep SRHO in global bundles and require local checks for neighborhood/outlier tasks; otherwise ordering consistency can be mistaken for full structural reliability.

""",

    # techniques (missing set)
    "docs/techniques/catsne.md": """catSNE should be used when class-aware local organization is explicitly required, not as a universal replacement for unsupervised t-SNE. Its gains are most meaningful in class-separability and class-guided cluster workflows.

Because catSNE is label-conditioned, validate label quality and separability before using it as the primary recommendation. In ambiguous-label scenarios, run catSNE alongside unsupervised baselines and compare both label-aware and label-agnostic metric bundles.

""",
    "docs/techniques/cca.md": """CCA-family nonlinear mapping can be effective for preserving local continuity patterns, but it is sensitive to neighborhood and optimization settings. Treat it as a candidate requiring explicit local-scale validation rather than a default baseline.

For reliable use, report neighborhood policy and convergence behavior. If CCA performs well only in narrow parameter windows, prefer methods with broader stability unless the task strongly benefits from CCA-specific behavior.

""",
    "docs/techniques/kpca.md": """Kernel PCA depends heavily on kernel choice and kernel scale. Different kernel settings represent different geometry assumptions; method comparison is invalid if kernel policy is not controlled.

Use KPCA when nonlinear global structure is plausible and kernel assumptions are justified by the task. Always compare against linear PCA and at least one neighborhood-focused method to verify whether kernel-induced gains are truly task-relevant.

""",
    "docs/techniques/lamp.md": """LAMP quality depends on control-point design and local affine fitting stability. Poor control-point coverage can create visually plausible but structurally biased embeddings.

In reliable workflows, treat control-point policy as a first-class hyperparameter family. Evaluate sensitivity to control-point count and placement strategy, then report whether conclusions remain stable across reasonable control-point variants.

""",
    "docs/techniques/laplacian_eigenmaps.md": """Laplacian Eigenmaps is graph-first; neighborhood graph quality determines embedding quality. Before trusting outcomes, verify graph connectivity, component structure, and sensitivity to neighborhood-size changes.

LE is valuable both as a standalone local method and as an initialization context for other methods. When used in comparisons, keep graph policy fixed and document whether downstream method gains remain after controlling that initialization effect.

""",
    "docs/techniques/lsp.md": """LSP-style projections provide practical speed-quality tradeoffs and can work well in interactive settings. Their reliability depends on representative landmark/control selections and stable projection fitting.

When using LSP for recommendation, run robustness checks over landmark sampling seeds. If embedding narratives change across landmark sets, mark confidence as reduced and keep additional candidate methods in the final shortlist.

""",
    "docs/techniques/nerv.md": """NeRV is useful when you need explicit control over where neighborhood distortion is placed. This makes it valuable for task-conditioned tuning where local versus global error preference is known in advance.

Because distortion weights directly shape outcomes, NeRV should be tuned with explicit objective rationale. Record weight settings and show how weight changes alter task metrics; otherwise conclusions are hard to audit and reproduce.

""",
    "docs/techniques/plmp.md": """PLMP methods can provide efficient local projection behavior for exploratory analysis, but they inherit sensitivity from piecewise graph/local model choices. Reliability depends on stable local partitioning and consistent preprocessing.

Use PLMP with fixed protocol comparisons and explicit sensitivity checks over partition/graph settings. If small setting changes cause large structural differences, do not over-commit to PLMP for high-stakes interpretation tasks.

""",
    "docs/techniques/s-isomap.md": """Supervised Isomap variants are suitable when class information should influence geodesic structure preservation. They can improve class-oriented readability but also risk overfitting class assumptions.

Before production use, compare supervised and unsupervised Isomap under the same preprocessing and graph policies. If supervised gains disappear under label uncertainty tests, downgrade confidence and keep label-agnostic alternatives.

""",
    "docs/techniques/sne.md": """SNE is historically important and still useful as a conceptual baseline for probabilistic neighborhood embedding behavior. It helps interpret why later variants (for example t-SNE) change global/local behavior.

For modern workflows, use SNE mainly in comparative or methodological contexts rather than as a default production recommendation. If used, apply strong seed and optimization stability reporting because convergence behavior can vary substantially.

""",
    "docs/techniques/som.md": """SOM provides topology-aware organization that is useful for exploratory structure discovery and prototype-level interpretation. It can be effective when analysts need interpretable map organization rather than only scatterplot geometry.

SOM reliability depends on grid design, learning schedule, and neighborhood-decay policy. Treat these as task-level decisions and validate with external metrics; otherwise map aesthetics can be mistaken for trustworthy structure preservation.

""",
}


def insert_section(path: Path, body: str) -> bool:
    text = path.read_text(encoding="utf-8")
    if "## Practical Reliability Notes" in text:
        return False
    anchor = "## Notable Properties\n"
    idx = text.find(anchor)
    if idx == -1:
        return False
    section = "## Practical Reliability Notes\n" + body
    path.write_text(text[:idx] + section + text[idx:], encoding="utf-8")
    return True


def main() -> int:
    updated = 0
    missing = []
    for rel, body in MAPPING.items():
        p = ROOT / rel
        if not p.exists():
            missing.append(rel)
            continue
        if insert_section(p, body):
            updated += 1
    print(f"updated_files={updated}")
    if missing:
        print("missing_files")
        for m in missing:
            print(m)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
