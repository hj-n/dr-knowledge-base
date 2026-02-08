#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
from typing import Dict, List

ROOT = Path(__file__).resolve().parents[1]

METRIC_CATS: Dict[str, str] = {
    # local
    "tnc": "local",
    "mrre": "local",
    "lcmc": "local",
    "nh": "local_label",
    "ca_tnc": "local_label",
    "l_tnc": "local_label",
    "nd": "local",
    "proc": "local",
    "qnx": "local",
    "spectral_overlap": "local",
    # cluster/class
    "snc": "cluster",
    "dsc": "cluster_label",
    "ivm": "cluster_label",
    "c_evm": "cluster_label",
    # global
    "stress": "global",
    "sn_stress": "global",
    "nm_stress": "global",
    "kl_div": "global",
    "dtm": "global",
    "topo": "global",
    "pr": "global",
    "srho": "global",
}

TECH_CATS: Dict[str, str] = {
    "t-sne": "stochastic_local",
    "umap": "stochastic_local",
    "sne": "stochastic_local",
    "nerv": "stochastic_local",
    "catsne": "supervised_local",
    "classnerv": "supervised_local",
    "classimap": "supervised_local",
    "lle": "stochastic_local",
    "laplacian_eigenmaps": "graph_local",
    "lmds": "stochastic_local",
    "lamp": "landmark_local",
    "lsp": "landmark_local",
    "plmp": "graph_local",
    "som": "prototype_local",
    "cca": "stochastic_local",
    "pca": "global_struct",
    "mds": "global_struct",
    "isomap": "graph_global",
    "s-isomap": "graph_global",
    "kpca": "kernel_global",
    "random_projection": "baseline_fast",
}


def append_to_section(text: str, section: str, marker: str, addition: str) -> str:
    heading = f"## {section}\n"
    i = text.find(heading)
    if i == -1:
        return text
    start = i + len(heading)
    j = text.find("\n## ", start)
    if j == -1:
        j = len(text)
    body = text[start:j]
    if marker in body:
        return text
    # ensure spacing
    body = body.rstrip() + "\n\n" + addition.strip() + "\n"
    return text[:start] + body + text[j:]


def metric_additions(cat: str, metric_id: str) -> Dict[str, str]:
    shared = {
        "Computation Outline": (
            "Detailed protocol rule:",
            "Detailed protocol rule: run the same computation pipeline across all candidate embeddings (same distance backend, same neighborhood construction policy, and same tie-handling policy). If protocol settings differ between runs, treat score changes as non-comparable and do not use them for final ranking.",
        ),
        "Hyperparameter Impact": (
            "Decision-level tuning rule:",
            "Decision-level tuning rule: tune this metric only inside a task-aligned bundle objective and report sensitivity across multiple seeds or folds. Single-run improvements should be treated as provisional until rank stability is confirmed.",
        ),
        "Task Alignment": (
            "Operational alignment rule:",
            "Operational alignment rule: this metric can prioritize candidates inside an already-selected task axis, but it must not redefine the task itself. If metric preference and user task conflict, keep task intent as the hard constraint.",
        ),
        "Interpretation Notes": (
            "Failure-signaling rule:",
            "Failure-signaling rule: if this metric disagrees with other bundle metrics, report that disagreement explicitly and mark recommendation confidence as reduced instead of averaging away the conflict.",
        ),
    }

    if cat == "local":
        shared["Computation Outline"] = (
            "Detailed protocol rule:",
            "Detailed protocol rule: evaluate multiple neighborhood scales (for example small/medium/local-range k values) and keep the same k schedule across methods. Local metrics should be read as scale-dependent curves, not single-point truths.",
        )
        shared["Task Alignment"] = (
            "Operational alignment rule:",
            "Operational alignment rule: this metric is strongest for neighborhood, outlier, and cluster-local tasks. For point-distance or density-dominant tasks, keep it as guardrail evidence rather than primary ranking evidence.",
        )
    elif cat == "local_label":
        shared["Computation Outline"] = (
            "Detailed protocol rule:",
            "Detailed protocol rule: compute under a fixed label policy (including unknown/missing labels) and fixed neighborhood scale. Label preprocessing changes can produce large score shifts that do not reflect embedding changes.",
        )
        shared["Hyperparameter Impact"] = (
            "Decision-level tuning rule:",
            "Decision-level tuning rule: label-conditioned settings must be checked with the label-separation gate before tuning-driven decisions. If separability is weak, down-weight this metric and raise uncertainty in the final recommendation.",
        )
    elif cat == "cluster":
        shared["Computation Outline"] = (
            "Detailed protocol rule:",
            "Detailed protocol rule: keep cluster definition policy fixed (including grouping thresholds or extraction logic) during comparison. Changes in cluster policy can dominate this metric more than projection changes.",
        )
        shared["Task Alignment"] = (
            "Operational alignment rule:",
            "Operational alignment rule: treat this metric as primary evidence for cluster-relationship tasks and as secondary evidence for neighborhood-only tasks.",
        )
    elif cat == "cluster_label":
        shared["Computation Outline"] = (
            "Detailed protocol rule:",
            "Detailed protocol rule: keep class labels and class-balance handling fixed across runs. Reweighting classes or filtering minority classes can substantially alter class metrics independently of embedding quality.",
        )
        shared["Interpretation Notes"] = (
            "Failure-signaling rule:",
            "Failure-signaling rule: when class-aware metrics improve but label-agnostic local/global metrics worsen, report a class-specific gain with structural tradeoff instead of claiming unconditional quality improvement.",
        )
    elif cat == "global":
        shared["Computation Outline"] = (
            "Detailed protocol rule:",
            "Detailed protocol rule: apply consistent distance scaling and normalization policy before computing global metrics. Global score comparisons are invalid when scale handling differs across candidates.",
        )
        shared["Task Alignment"] = (
            "Operational alignment rule:",
            "Operational alignment rule: use this metric as primary evidence for point-distance, cluster-distance, or density tasks; use as secondary guardrail for neighborhood tasks.",
        )

    return {k: v[1] for k, v in shared.items()}


def technique_additions(cat: str, tech_id: str) -> Dict[str, str]:
    shared = {
        "Computation Outline": "Detailed execution rule: run this method under a fixed preprocessing contract and log all stochastic controls (seed, restart index, initialization metadata) so comparison runs are auditable.",
        "Hyperparameter Impact": "Decision-level tuning rule: report both best score and stability behavior (seed variance / restart variance). A configuration that wins once but is unstable should not be the default recommendation.",
        "Task Alignment": "Operational alignment rule: method alignment should constrain candidate ranking, but final acceptance still requires agreement with task-aligned metric bundles and warning-gate status.",
        "Known Tradeoffs": "Communication rule: document one concrete downside that remained after tuning (for example global drift, local fragmentation, or runtime burden) so end users understand residual risk.",
    }

    if cat == "stochastic_local":
        shared["Computation Outline"] = "Detailed execution rule: run multiple seeds under the same initialization mode and compare structural consistency before accepting conclusions. For local stochastic methods, a single visually appealing run is not sufficient evidence."
        shared["Hyperparameter Impact"] = "Decision-level tuning rule: tune local-scale controls and optimization controls jointly, then verify that gains remain under seed perturbation. If seed sensitivity is high, downgrade confidence and keep fallback candidates."
    elif cat == "supervised_local":
        shared["Computation Outline"] = "Detailed execution rule: keep label policy fixed and record how missing/noisy labels were handled. Supervised local methods can shift behavior dramatically with label cleaning choices."
        shared["Task Alignment"] = "Operational alignment rule: use as primary candidates only for class-separability-oriented tasks; for non-class tasks, keep these methods as optional comparisons and require label-agnostic corroboration."
    elif cat == "graph_local":
        shared["Computation Outline"] = "Detailed execution rule: verify graph connectivity and neighborhood-policy stability before interpreting results. Graph fragmentation or unstable connectivity can invalidate downstream interpretation."
        shared["Known Tradeoffs"] = "Communication rule: explicitly state graph-dependence risk. If results change under small graph-parameter shifts, present that instability as residual uncertainty."
    elif cat == "landmark_local":
        shared["Computation Outline"] = "Detailed execution rule: treat control-point/landmark selection as a controlled factor and run sensitivity checks across multiple selections. Landmark policy drift can dominate method comparisons."
        shared["Hyperparameter Impact"] = "Decision-level tuning rule: optimize both landmark ratio and local fitting settings under the same task metric bundle; report whether conclusions persist across reasonable landmark policies."
    elif cat == "prototype_local":
        shared["Computation Outline"] = "Detailed execution rule: keep map/grid configuration and neighborhood-decay schedule explicit. Prototype-map methods can tell very different stories under different grid designs."
    elif cat == "global_struct":
        shared["Task Alignment"] = "Operational alignment rule: prioritize for distance and density tasks; for neighborhood-centric tasks use as baseline or guardrail, not as sole recommendation evidence."
        shared["Known Tradeoffs"] = "Communication rule: explain what local structure may be sacrificed to preserve global trends, and confirm this with local metrics before finalization."
    elif cat == "graph_global":
        shared["Computation Outline"] = "Detailed execution rule: evaluate geodesic graph stability (connectivity and shortest-path robustness) before trusting global interpretation. Unstable geodesics produce fragile global claims."
    elif cat == "kernel_global":
        shared["Hyperparameter Impact"] = "Decision-level tuning rule: kernel family and kernel scale are first-order assumptions, not minor tweaks. Log chosen kernel rationale and compare against linear/global baselines under the same protocol."
    elif cat == "baseline_fast":
        shared["Known Tradeoffs"] = "Communication rule: present this method as a speed/reference baseline unless task metrics clearly validate its adequacy. Runtime gains do not substitute for reliability evidence."

    return shared


def main() -> int:
    updated = 0

    # metrics
    metrics_dir = ROOT / "docs" / "metrics"
    for p in sorted(metrics_dir.glob("*.md")):
        if p.name == "README.md":
            continue
        metric_id = p.stem
        cat = METRIC_CATS.get(metric_id, "local")
        adds = metric_additions(cat, metric_id)
        text = p.read_text(encoding="utf-8")
        orig = text
        text = append_to_section(text, "Computation Outline", "Detailed protocol rule:", adds["Computation Outline"])
        text = append_to_section(text, "Hyperparameter Impact", "Decision-level tuning rule:", adds["Hyperparameter Impact"])
        text = append_to_section(text, "Task Alignment", "Operational alignment rule:", adds["Task Alignment"])
        text = append_to_section(text, "Interpretation Notes", "Failure-signaling rule:", adds["Interpretation Notes"])
        if text != orig:
            p.write_text(text, encoding="utf-8")
            updated += 1

    # techniques
    tech_dir = ROOT / "docs" / "techniques"
    for p in sorted(tech_dir.glob("*.md")):
        if p.name == "README.md":
            continue
        tech_id = p.stem
        cat = TECH_CATS.get(tech_id, "stochastic_local")
        adds = technique_additions(cat, tech_id)
        text = p.read_text(encoding="utf-8")
        orig = text
        text = append_to_section(text, "Computation Outline", "Detailed execution rule:", adds["Computation Outline"])
        text = append_to_section(text, "Hyperparameter Impact", "Decision-level tuning rule:", adds["Hyperparameter Impact"])
        text = append_to_section(text, "Task Alignment", "Operational alignment rule:", adds["Task Alignment"])
        text = append_to_section(text, "Known Tradeoffs", "Communication rule:", adds["Known Tradeoffs"])
        if text != orig:
            p.write_text(text, encoding="utf-8")
            updated += 1

    print(f"updated_files={updated}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
