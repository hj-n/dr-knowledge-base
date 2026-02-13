---
id: paper-2021-zadu-ref-18
title: "Measuring and Explaining the Inter-Cluster Reliability of Multidimensional Projections"
authors: "Hyeon Jeon; Hyung-Kwon Ko; Jaemin Jo; Youngtaek Kim; Jinwook Seo"
venue: "IEEE Transactions on Visualization and Computer Graphics"
year: 2021
tags: [dr, zadu-table1-reference, snc, tnc, mrre, lcmc]
source_pdf: papers/raw/zadu-table1-references/ref18_measuring_and_explaining_the_inter_cluster_reliability_of_multidimensional_projections.pdf
seed_note_id: "paper-2023-zadu-library"
evidence_level: high
updated_at: 2026-02-13
---

# Problem
- Existing DR quality measures were strong for point-level neighborhood distortions, but weak for inter-cluster tasks (cluster separation, cluster-to-cluster relation, and size/density comparison).
- The paper argues that users can misread inter-cluster structure when metrics do not capture cluster-level distortion types.
- It formalizes cluster-level distortion types (Missing Groups, False Groups) and targets metrics that directly measure how these distortions affect analysis tasks.

# Method Summary
- The paper introduces two metrics: **Steadiness** and **Cohesiveness** (S&C), designed to quantify inter-cluster reliability.
- Steadiness measures whether clusters seen in the projection are valid in the original space; Cohesiveness measures whether original clusters stay coherent in the projection.
- The computation pipeline has three major parts: construct dissimilarity matrices (`D+`, `D-`), iteratively extract random clusters in one space and evaluate their dispersion in the other space, then aggregate weighted partial distortions.
- The method requires four configurable functions: point distance `dist`, cluster distance `dist_cluster`, cluster extraction `extract_cluster`, and clustering `clustering`.
- The paper also introduces a **reliability map** to localize where inter-cluster distortion occurs, not only a global scalar score.

# When To Use / Not Use
- Use when:
  - your main goal is inter-cluster interpretation (cluster separation, cluster relation, cluster size/density comparison),
  - you need explicit diagnostics for Missing Groups and False Groups,
  - local-neighborhood scores alone are insufficient for the analysis decision.
- Avoid when:
  - your task is strictly pointwise neighborhood retrieval with no cluster-level interpretation,
  - the clustering policy cannot be kept stable across candidate comparisons.
- Failure modes:
  - unstable choices of `dist`, `extract_cluster`, or clustering settings can dominate score changes and reduce comparability between runs.

# Metrics Mentioned
- `snc`: Steadiness and Cohesiveness; core inter-cluster reliability measure pair.
- `tnc`: baseline local-neighborhood reliability metric used as a comparison baseline.
- `mrre`: baseline rank-based local distortion metric used as a comparison baseline.
- `lcmc`: neighborhood-overlap local metric discussed in related-work comparisons.

# Implementation Notes
- Keep `dist`, `dist_cluster`, clustering algorithm, and extraction policy fixed when comparing DR methods.
- The default design in the paper uses Shared Nearest Neighbors (SNN)-based point dissimilarity to better represent high-dimensional structure.
- For tuning studies, the paper demonstrates sensitivity testing against DR hyperparameters (for example UMAP `n_neighbors`) and checks whether metric trends match known distortion behavior.
- Use S&C together with local metrics (for example T&C, MRRE) to separate point-level and cluster-level reliability effects.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PAPER2021ZADUREF18-C1 | stance: support | summary: Steadiness and Cohesiveness are introduced as dedicated inter-cluster reliability measures between original and projected spaces. | evidence_ids: PAPER2021ZADUREF18-E1, PAPER2021ZADUREF18-E2
- CLAIM-PAPER2021ZADUREF18-C2 | stance: support | summary: Prior local metrics such as T&C and MRRE do not directly measure inter-cluster reliability for cluster-level tasks. | evidence_ids: PAPER2021ZADUREF18-E3, PAPER2021ZADUREF18-E4
- CLAIM-PAPER2021ZADUREF18-C3 | stance: support | summary: The S&C workflow depends on configurable distance/clustering/extraction functions and computes weighted partial distortions. | evidence_ids: PAPER2021ZADUREF18-E5, PAPER2021ZADUREF18-E6
- CLAIM-PAPER2021ZADUREF18-C4 | stance: support | summary: Quantitative experiments show S&C captures synthetic Missing/False Groups distortions and hyperparameter-driven inter-cluster reliability changes. | evidence_ids: PAPER2021ZADUREF18-E7, PAPER2021ZADUREF18-E8

# Workflow Relevance Map
- step: 3 | relevance: high | note: adds cluster-level reliability criteria that should be selected when the task is inter-cluster analysis.
- step: 4 | relevance: high | note: prevents selecting methods based only on local metrics when cluster-level reliability is the actual goal.
- step: 6 | relevance: medium | note: supports hyperparameter sensitivity analysis with explicit inter-cluster reliability signals.
- step: 7 | relevance: high | note: reliability map supports explanation of where distortions remain in the embedding.

# Evidence
- PAPER2021ZADUREF18-E1 | page: 1, section: abstract, quote: "We propose Steadiness and Cohesiveness, two novel metrics to measure the inter-cluster reliability of multidimensional projection (MDP)."
- PAPER2021ZADUREF18-E2 | page: 1, section: abstract, quote: "Steadiness measures the extent to which clusters in the projected space form clusters in the original space, and Cohesiveness measures the opposite."
- PAPER2021ZADUREF18-E3 | page: 1, section: abstract, quote: "we found that previous metrics, such as Trustworthiness and Continuity, fail to measure inter-cluster reliability."
- PAPER2021ZADUREF18-E4 | page: 2, section: distortion metrics, quote: "Trustworthiness and Continuity (T&C) [67] locally measure how Missing and False Neighbors distort the ranks of each point’s neighbors."
- PAPER2021ZADUREF18-E5 | page: 4, section: workflow, quote: "The workflow requires four functions as hyperparameters: dist, dist_cluster, extract_cluster, clustering."
- PAPER2021ZADUREF18-E6 | page: 4, section: step 1, quote: "We begin the measurement by constructing dissimilarity matrices D+ and D−."
- PAPER2021ZADUREF18-E7 | page: 6, section: sensitivity analysis, quote: "We designed the first two experiments (A, B) to evaluate our metrics’ ability to quantify the inter-cluster distortion using ... False Groups ... or Missing Groups."
- PAPER2021ZADUREF18-E8 | page: 7, section: experiment D, quote: "the number of nearest neighbors n ... Lower n values drive UMAP to more local structures, while higher values make the projection preserve global structures rather than local details."
- PAPER2021ZADUREF18-E9 | page: 5, section: default functions, quote: "we defined distance as the dissimilarity of the points based on the Shared-Nearest Neighbors (SNN) similarity."
- PAPER2021ZADUREF18-E10 | page: 1, section: abstract, quote: "our metrics can quantify pointwise distortions, allowing for the visualization of inter-cluster reliability in a projection, which we call a reliability map."
