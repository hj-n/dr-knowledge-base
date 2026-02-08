#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

INSERTIONS = {
    # metrics
    "docs/metrics/tnc.md": {
        "anchor": "## Notable Properties\n",
        "title": "## Practical Reliability Notes\n",
        "body": "TNC is most informative when it is measured on a k schedule instead of a single k. In practice, k values such as 5, 10, 20, 50 often reveal whether a method is only good at very local neighborhoods or robust across local scales. If two methods cross over by k, report that crossover explicitly instead of reporting only a single aggregate value.\n\nWhen using TNC for model selection, compare trustworthiness and continuity separately before averaging. A method with high trustworthiness but low continuity often removes true neighbors (over-fragmentation), while the opposite often introduces false neighbors (over-crowding). These failure modes map to different analyst risks and should be kept visible in the final explanation.\n\n",
    },
    "docs/metrics/stress.md": {
        "anchor": "## Notable Properties\n",
        "title": "## Practical Reliability Notes\n",
        "body": "Stress values are only comparable under identical scale handling and distance preprocessing. If one run applies implicit rescaling and another does not, stress ranking can reverse even when the embedding geometry is otherwise similar. Keep scale policy fixed across all candidates and report that policy explicitly.\n\nFor workflow use, stress should be paired with at least one local metric (for example TNC or NH-family metrics) because low global stress can still hide local neighborhood breakage. A low-stress embedding is not automatically valid for neighborhood or outlier tasks unless local structure checks agree.\n\n",
    },
    "docs/metrics/kl_div.md": {
        "anchor": "## Notable Properties\n",
        "title": "## Practical Reliability Notes\n",
        "body": "KL-style objectives are asymmetric: the direction of comparison determines which distortion type is penalized more. In DR practice this means the same embedding can look better or worse depending on whether false-neighbor or missed-neighbor errors are emphasized. Keep objective direction fixed when benchmarking methods.\n\nBecause KL is sensitive to small-probability neighborhoods, optimization noise and early exaggeration style settings can materially alter outcomes. Treat KL-driven tuning as a stability problem: compare multiple seeds and avoid accepting single-run wins that are not reproduced.\n\n",
    },
    "docs/metrics/nh.md": {
        "anchor": "## Notable Properties\n",
        "title": "## Practical Reliability Notes\n",
        "body": "Neighborhood Hit is label-dependent and behaves like a local class-purity score over k-nearest neighbors in embedding space. It is high when neighbors share labels, but this is meaningful only if labels are already well-separated in the original space. If that assumption is weak, NH can reward visually clean but semantically misleading maps.\n\nUse NH as supporting evidence, not a single gate. Pair it with at least one label-agnostic local metric and one global metric before final ranking. If NH improves while label-agnostic metrics degrade, report the tradeoff rather than claiming overall quality improvement.\n\n",
    },
    "docs/metrics/dsc.md": {
        "anchor": "## Notable Properties\n",
        "title": "## Practical Reliability Notes\n",
        "body": "Distance Consistency reflects whether points remain closer to their own class prototypes than to other classes after projection. It is useful for class-separability analysis, but can become overly optimistic when classes overlap in original space or when class imbalance is severe.\n\nBefore relying on DSC for recommendation decisions, run the label-separation warning gate and verify class overlap in the original feature space. If overlap is high, down-weight DSC and prioritize mixed bundles including non-label metrics and task-specific technique constraints.\n\n",
    },
    "docs/metrics/ivm.md": {
        "anchor": "## Notable Properties\n",
        "title": "## Practical Reliability Notes\n",
        "body": "IVM-style class metrics are sensitive to class geometry assumptions and sampling density. Sparse classes or long-tail classes can cause unstable values that look like model effects but are actually sampling artifacts. Keep class support diagnostics in the same report as metric values.\n\nIn comparative studies, evaluate IVM under repeated subsampling or seed changes to test rank stability. If rankings change across minor protocol changes, treat IVM output as exploratory and avoid making it the primary driver of technique selection.\n\n",
    },
    "docs/metrics/c_evm.md": {
        "anchor": "## Notable Properties\n",
        "title": "## Practical Reliability Notes\n",
        "body": "Class-EVM style measures emphasize class-level embedding consistency and therefore amplify label quality issues. Noisy labels, weak supervision, or merged semantic classes can produce confident but unreliable scores.\n\nOperationally, only treat C-EVM as decision-driving when label validity and separability are both supported. Otherwise, retain it as an auxiliary indicator and keep recommendations anchored to task-fit plus label-agnostic reliability checks.\n\n",
    },
    "docs/metrics/proc.md": {
        "anchor": "## Notable Properties\n",
        "title": "## Practical Reliability Notes\n",
        "body": "Procrustes-based metrics compare structures after optimal rigid alignment (translation, rotation, scaling). They are useful for checking shape-level agreement independent of axis orientation, which is valuable when embeddings are compared across runs or methods.\n\nBecause Procrustes suppresses orientation differences, it may hide local neighborhood defects. Use it together with local rank-based metrics when the analytical task depends on neighborhood identity, not only coarse shape similarity.\n\n",
    },
    "docs/metrics/topo.md": {
        "anchor": "## Notable Properties\n",
        "title": "## Practical Reliability Notes\n",
        "body": "Topology-focused metrics capture structural events such as disconnected groups, bridges, or holes that may be invisible in average distance scores. They are especially useful when analysts care about cluster connectivity or separation order.\n\nTopological signals are sensitive to neighborhood graph construction. Keep graph policy (k, radius, distance backend) fixed across comparisons; otherwise changes in topology metrics may reflect graph construction drift instead of embedding quality differences.\n\n",
    },
    # techniques
    "docs/techniques/t-sne.md": {
        "anchor": "## Notable Properties\n",
        "title": "## Practical Reliability Notes\n",
        "body": "t-SNE should be treated as a local-neighborhood optimizer, not a global-distance map. Perplexity controls effective neighborhood scale, so the same dataset can yield different cluster granularity under different perplexity values. Always report perplexity together with seed and initialization policy.\n\nFor reliable comparison workflows, keep initialization fixed (PCA baseline for global-sensitive contexts) and evaluate multiple seeds. If conclusions about cluster relationship or outlier identity change across seeds, mark confidence as reduced and keep alternative candidates in the final recommendation.\n\n",
    },
    "docs/techniques/umap.md": {
        "anchor": "## Notable Properties\n",
        "title": "## Practical Reliability Notes\n",
        "body": "UMAP behavior is strongly controlled by neighborhood size and minimum-distance style controls, which jointly define local packing and cluster spacing. Parameter sweeps should be interpreted as task-conditional model choices, not cosmetic tuning.\n\nWhen UMAP is used for decision support, compare at least one local metric and one global metric under fixed preprocessing and fixed initialization policy. This guards against selecting configurations that look visually clean but are unstable or misaligned to the declared analytical task.\n\n",
    },
    "docs/techniques/pca.md": {
        "anchor": "## Notable Properties\n",
        "title": "## Practical Reliability Notes\n",
        "body": "PCA is deterministic under a fixed preprocessing policy and is therefore a strong baseline for reproducibility checks. If nonlinear methods do not outperform PCA on task-aligned metric bundles, prefer PCA for simpler and more auditable deployment.\n\nComponent count is not only a compression choice; it changes what downstream neighborhood and distance claims are plausible. For 2D visualization, keep a separate check in higher retained dimension when decisions depend on subtle class or distance structure.\n\n",
    },
    "docs/techniques/mds.md": {
        "anchor": "## Notable Properties\n",
        "title": "## Practical Reliability Notes\n",
        "body": "MDS variants optimize distance-fitting objectives and therefore can be effective for point-distance and cluster-distance tasks when scale handling is controlled. However, iterative MDS variants can converge to different local minima depending on initialization.\n\nFor fair comparisons, run a fixed restart protocol and report best-value plus variability, not only a single best run. If variability is high, avoid using one embedding snapshot as sole evidence for structural claims.\n\n",
    },
    "docs/techniques/isomap.md": {
        "anchor": "## Notable Properties\n",
        "title": "## Practical Reliability Notes\n",
        "body": "Isomap relies on graph geodesics, so neighborhood graph connectivity is a first-order reliability condition. If the graph is fragmented, global geodesic estimates become unstable and downstream projection can create misleading long-range structure.\n\nBefore final selection, check graph connectivity diagnostics and sensitivity to neighborhood-size changes. If major topology changes occur across small neighborhood shifts, report reduced confidence for global-distance interpretation.\n\n",
    },
    "docs/techniques/lle.md": {
        "anchor": "## Notable Properties\n",
        "title": "## Practical Reliability Notes\n",
        "body": "LLE preserves local linear reconstruction weights and is sensitive to neighborhood quality and noise. Poorly conditioned neighborhoods can propagate instability through global embedding solving steps.\n\nUse LLE with explicit preprocessing checks and neighborhood-size sweeps. If reconstruction quality drops for small parameter changes, prefer methods with more stable local behavior for production-facing analysis.\n\n",
    },
    "docs/techniques/random_projection.md": {
        "anchor": "## Notable Properties\n",
        "title": "## Practical Reliability Notes\n",
        "body": "Random projection is useful as a fast baseline and stress-test method because it exposes whether downstream conclusions are robust to coarse geometry preservation. It should not be assumed to preserve fine neighborhood semantics without explicit checks.\n\nWhen using random projection in a reliability workflow, report projection dimension and random seed protocol. Compare across multiple random matrices to estimate variance; single-matrix results can be misleading for small or highly structured datasets.\n\n",
    },
    "docs/techniques/classnerv.md": {
        "anchor": "## Notable Properties\n",
        "title": "## Practical Reliability Notes\n",
        "body": "ClassNeRV is intended for supervised settings where class labels are operationally trusted and class preservation is a primary goal. It explicitly trades distortion placement to retain class structure while keeping neighborhood signals usable.\n\nBecause it is label-conditioned, apply the label-separation warning gate before treating class-focused improvements as global quality gains. If class assumptions fail, keep supervised variants as exploratory candidates rather than default recommendations.\n\n",
    },
    "docs/techniques/classimap.md": {
        "anchor": "## Notable Properties\n",
        "title": "## Practical Reliability Notes\n",
        "body": "ClassiMap uses label information to influence projection structure, typically improving class-separation readability when labels are coherent. It can be effective for class-focused exploratory analysis and annotation review workflows.\n\nAs with other supervised projections, do not generalize class-oriented gains to unrelated tasks such as faithful global distance investigation. Keep task declaration explicit and pair ClassiMap with non-label metrics when reporting final recommendations.\n\n",
    },
    "docs/techniques/lmds.md": {
        "anchor": "## Notable Properties\n",
        "title": "## Practical Reliability Notes\n",
        "body": "Local MDS families provide explicit local-structure control and are useful when neighborhood reliability is the primary objective. They are often sensitive to initialization and local neighborhood construction policies.\n\nFor reliable method comparison, treat initialization as an explicit factor and run controlled seed comparisons. If local metrics improve but global metrics collapse, document that as a task-specific tradeoff rather than a universal method improvement.\n\n",
    },
}


def insert_block(path: Path, anchor: str, title: str, body: str) -> bool:
    text = path.read_text(encoding="utf-8")
    if title.strip() in text:
        return False
    idx = text.find(anchor)
    if idx == -1:
        return False
    block = title + body
    new_text = text[:idx] + block + text[idx:]
    path.write_text(new_text, encoding="utf-8")
    return True


def main() -> int:
    updated = 0
    missing = []
    for rel, cfg in INSERTIONS.items():
        p = ROOT / rel
        if not p.exists():
            missing.append(rel)
            continue
        ok = insert_block(p, cfg["anchor"], cfg["title"], cfg["body"])
        if ok:
            updated += 1
    print(f"updated_files={updated}")
    if missing:
        print("missing_files=")
        for m in missing:
            print(m)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
