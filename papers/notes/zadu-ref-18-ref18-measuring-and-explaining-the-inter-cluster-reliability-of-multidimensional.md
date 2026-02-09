---
id: paper-2021-zadu-ref-18
title: "Measuring and Explaining the Inter-Cluster Reliability of Multidimensional Projections"
authors: "Hyeon Jeon, Hyung-Kwon Ko, Jaemin Jo, Youngtaek Kim, Jinwook Seo"
venue: "IEEE Transactions on Visualization and Computer Graphics"
year: 2021
tags: [dr, zadu-table1-reference, ivm, lcmc, mrre, nd, pr, snc, stress, tnc]
source_pdf: papers/raw/zadu-table1-references/ref18_measuring_and_explaining_the_inter_cluster_reliability_of_multidimensional_projections.pdf
evidence_level: medium
updated_at: 2026-02-08
---
# Problem
- Experiment B: Identifying Missing Groups To evaluate Cohesiveness and previous local metrics’ (Trustworthiness, MRRE [Missing]) ability to measure Missing Groups distortion, we used the same high-dimensional dataset as Experiment A, but this time, we synthesized the initial projection consisting of 12 equally distant circles, where each consists of 250 points.
- 4.4 Visualizing Steadiness and Cohesiveness To overcome the limitation of metrics in that they describe the overall distortion in a single or two numeric values, we developed a complementary visualization: a reliability map (Fig.
- 2.1.3 Distortion Visualizations To overcome the inherent limitation of metrics that describe only the overall distortions with one or two representative numerical values, complementary visualizations are proposed [49].
- Distortion-guided structuredriven interactive exploration of high-dimensional data.
- This work was motivated by the following issue: although intercluster tasks, which investigate the inter-cluster structures of a given dataset (i.e., how clusters are located and related) through its 2D projection, have been regarded as the core tasks [37,59] for using MDP, only a few previous metrics have tried to explain the distortions of inter-cluster structure represented in MDP thus far.

# Method Summary
- Experiment B: Identifying Missing Groups To evaluate Cohesiveness and previous local metrics’ (Trustworthiness, MRRE [Missing]) ability to measure Missing Groups distortion, we used the same high-dimensional dataset as Experiment A, but this time, we synthesized the initial projection consisting of 12 equally distant circles, where each consists of 250 points.
- Abstract— We propose Steadiness and Cohesiveness, two novel metrics to measure the inter-cluster reliability of multidimensional projection (MDP), speciﬁcally how well the inter-cluster structures are preserved between the original high-dimensional space and the low-dimensional projection space.
- We designed the ﬁrst two experiments (A, B) to evaluate our metrics’ ability to quantify the inter-cluster distortion using the projections with synthetically generated False Groups (Experiment A) or Missing Groups (Experiment B) distortions respectively.
- Experiment D: Identifying the effect of projection hyperparameters The ﬁnal experiment was conducted to evaluate the capability of our metrics to capture the inter-cluster reliability differences caused by the hyperparameter choices of an MDP technique.
- In this paper, we propose Steadiness and Cohesiveness, two metrics that quantitatively evaluate inter-cluster reliability.
- Steadiness and Cohesiveness evaluate how well projections avoid False and Missing Groups, respectively (C2).
- Perception-based evaluation of projection methods for multidimensional data visualization.

# When To Use / Not Use
- Use when:
  - 2 B ACKGROUND AND RELATED WORK 2.1 MDP Distortions Many MDP techniques, such as t-SNE [36], Isomap [65], and UMAP [41], have been proposed to understand and visualize highdimensional data1; however, every MDP produces distortions because information loss is inevitable when dimensionality is reduced.
  - This is because when clustering the extracted clusters in the opposite space, the inter-cluster structure composed of arbitrary shapes and sizes can be better represented by the ﬁne-grainedK-Means clustering result than the coarse-grained result.
  - 6.1.3 Discussion The result of Experiment A suggests that our metrics could identify a loss of the inter-cluster reliability caused by False Groups distortion, as Steadiness decreased when the overlap of circle pairs increased.
- Avoid when:
  - Discussion The result of Experiment A suggests that our metrics could identify a loss of the inter-cluster reliability caused by False Groups distortion, as Steadiness decreased when the overlap of circle pairs increased.
  - This is because he usually works with data with welldistributed vector representations processed by a deep neural network, where no inter-cluster structure exists.
- Failure modes:
  - Users can have misconceptions when comparing clusters (T3) if the projected clusters’ size and density do not reﬂect those in the original space.
  - When performing these inter-cluster tasks, users must be aware of the preservation of the inter-cluster structure in the MDP.

# Metrics Mentioned
- `tnc`: Trustworthiness and Continuity behavior.
- `mrre`: mean relative rank errors across neighborhood scales.
- `lcmc`: local continuity meta-criterion for neighborhood overlap.
- `nh`: label-based neighborhood hit.
- `nd`: neighbor-shape dissimilarity or neighbor distortion.
- `pr`: pairwise-distance correlation behavior.
- `ivm`: internal clustering validation behavior.
- `snc`: Steadiness/Cohesiveness inter-cluster reliability.
- `topo`: topology-related structure behavior.
- `proc`: Procrustes local shape agreement.

# Implementation Notes
- The result of quantitative experiments A-D; the scores measured by our metrics (Steadiness and Cohesiveness) and baseline local distortion metrics (MRREs, T&C). inspired by an analysis from the UMAP paper [41] where the authors assessed the impact of a hyperparameter, the number ofnearest neighbors n, on the projection quality.
- The case study showed that our metrics and the reliability map supports users in 1) selecting adequate projection techniques or hyperparameter settings that match the dataset and 2) preventing users’ misinterpretation that could potentially occur while conducting inter-cluster tasks (Sect.
- A case study also demonstrates that our metrics and the reliability map 1) support users in selecting the proper projection techniques or hyperparameters and 2) prevent misinterpretation while performing inter-cluster tasks, thus allow an adequate identiﬁcation of inter-cluster structure.
- The qualitative case studies showed that our metrics can also help users select proper projection techniques or hyperparameter settings and perform inter-cluster tasks with fewer misperceptions, assisting them in interpreting the original space’s inter-cluster structure.
- Experiment D: Identifying the effect of projection hyperparameters The ﬁnal experiment was conducted to evaluate the capability of our metrics to capture the inter-cluster reliability differences caused by the hyperparameter choices of an MDP technique.
- 4.3 Designing Hyperparameter Functions 4.3.1 Parameterizing Hyperparameter Functions The workﬂow of computing Steadiness and Cohesiveness requires four hyperparameter functions: dist, dist cluster, clustering, and extract cluster.
- Keep preprocessing, initialization policy, and random-seed protocol fixed when comparing methods.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PAPER2021ZADUREF18-C1 | stance: support | summary: Experiment B: Identifying Missing Groups To evaluate Cohesiveness and previous local metrics’ (Trustworthiness, MRRE [Missing]) ability to measure Missing Groups distortion, we used the same high-dimensional dataset as Experiment A, but this time, we synthesized the initial projection consisting of 12 equally distant circles, where each consists of 250 points. | evidence_ids: PAPER2021ZADUREF18-E1, PAPER2021ZADUREF18-E2
- CLAIM-PAPER2021ZADUREF18-C2 | stance: support | summary: Experiment B: Identifying Missing Groups To evaluate Cohesiveness and previous local metrics’ (Trustworthiness, MRRE [Missing]) ability to measure Missing Groups distortion, we used the same high-dimensional dataset as Experiment A, but this time, we synthesized the initial projection consisting of 12 equally distant circles, where each consists of 250 points. | evidence_ids: PAPER2021ZADUREF18-E3, PAPER2021ZADUREF18-E4
- CLAIM-PAPER2021ZADUREF18-C3 | stance: support | summary: The result of quantitative experiments A-D; the scores measured by our metrics (Steadiness and Cohesiveness) and baseline local distortion metrics (MRREs, T&C). inspired by an analysis from the UMAP paper [41] where the authors assessed the impact of a hyperparameter, the number ofnearest neighbors n, on the projection quality. | evidence_ids: PAPER2021ZADUREF18-E5, PAPER2021ZADUREF18-E6
- CLAIM-METRIC-IVM-SOURCE-18 | stance: support | summary: This source includes evidence relevant to `ivm` in dimensionality-reduction reliability evaluation. | evidence_ids: PAPER2021ZADUREF18-E1, PAPER2021ZADUREF18-E2
- CLAIM-METRIC-LCMC-SOURCE-18 | stance: support | summary: This source includes evidence relevant to `lcmc` in dimensionality-reduction reliability evaluation. | evidence_ids: PAPER2021ZADUREF18-E1, PAPER2021ZADUREF18-E2
- CLAIM-METRIC-MRRE-SOURCE-18 | stance: support | summary: This source includes evidence relevant to `mrre` in dimensionality-reduction reliability evaluation. | evidence_ids: PAPER2021ZADUREF18-E1, PAPER2021ZADUREF18-E2
- CLAIM-METRIC-ND-SOURCE-18 | stance: support | summary: This source includes evidence relevant to `nd` in dimensionality-reduction reliability evaluation. | evidence_ids: PAPER2021ZADUREF18-E1, PAPER2021ZADUREF18-E2
- CLAIM-METRIC-PR-SOURCE-18 | stance: support | summary: This source includes evidence relevant to `pr` in dimensionality-reduction reliability evaluation. | evidence_ids: PAPER2021ZADUREF18-E1, PAPER2021ZADUREF18-E2
- CLAIM-METRIC-SNC-SOURCE-18 | stance: support | summary: This source includes evidence relevant to `snc` in dimensionality-reduction reliability evaluation. | evidence_ids: PAPER2021ZADUREF18-E1, PAPER2021ZADUREF18-E2
- CLAIM-METRIC-STRESS-SOURCE-18 | stance: support | summary: This source includes evidence relevant to `stress` in dimensionality-reduction reliability evaluation. | evidence_ids: PAPER2021ZADUREF18-E1, PAPER2021ZADUREF18-E2
- CLAIM-METRIC-TNC-SOURCE-18 | stance: support | summary: This source includes evidence relevant to `tnc` in dimensionality-reduction reliability evaluation. | evidence_ids: PAPER2021ZADUREF18-E1, PAPER2021ZADUREF18-E2

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports task clarification before model selection
- step: 2 | relevance: medium | note: adds constraints for preprocessing and data-audit checks
- step: 3 | relevance: high | note: directly informs task-aligned technique/metric selection
- step: 5 | relevance: medium | note: adds initialization sensitivity guidance
- step: 6 | relevance: high | note: adds hyperparameter sensitivity or optimization guidance

# Evidence
- PAPER2021ZADUREF18-E1 | page: 6, section: extracted, quote: "Experiment B: Identifying Missing Groups To evaluate Cohesiveness and previous local metrics’ (Trustworthiness, MRRE [Missing]) ability to measure Missing Groups distortion, we used the same high-dimensional dataset as Experiment A, but this time, we synthesized the initial projection consisting of 12 equally distant circles, where each consists of 250 points."
- PAPER2021ZADUREF18-E2 | page: 5, section: extracted, quote: "4.4 Visualizing Steadiness and Cohesiveness To overcome the limitation of metrics in that they describe the overall distortion in a single or two numeric values, we developed a complementary visualization: a reliability map (Fig."
- PAPER2021ZADUREF18-E3 | page: 2, section: extracted, quote: "2.1.3 Distortion Visualizations To overcome the inherent limitation of metrics that describe only the overall distortions with one or two representative numerical values, complementary visualizations are proposed [49]."
- PAPER2021ZADUREF18-E4 | page: 10, section: extracted, quote: "Distortion-guided structuredriven interactive exploration of high-dimensional data."
- PAPER2021ZADUREF18-E5 | page: 1, section: extracted, quote: "This work was motivated by the following issue: although intercluster tasks, which investigate the inter-cluster structures of a given dataset (i.e., how clusters are located and related) through its 2D projection, have been regarded as the core tasks [37,59] for using MDP, only a few previous metrics have tried to explain the distortions of inter-cluster structure represented in MDP thus far."
- PAPER2021ZADUREF18-E6 | page: 4, section: extracted, quote: "Let’s denote the set as follows: • (mcompress 1 ,w1),··· , (mcompress nSt ,wnSt ) where nSt denotes the number of total cluster pairs generated throughout the entire partial distortion measurement of Steadiness. • (mstretch 1 ,w1),··· , (mstretchnCo ,wnCo) where nCo denotes the number of total cluster pairs generated throughout the entire partial distortion measurement of Cohesiveness."
- PAPER2021ZADUREF18-E7 | page: 1, section: extracted, quote: "Abstract— We propose Steadiness and Cohesiveness, two novel metrics to measure the inter-cluster reliability of multidimensional projection (MDP), speciﬁcally how well the inter-cluster structures are preserved between the original high-dimensional space and the low-dimensional projection space."
- PAPER2021ZADUREF18-E8 | page: 6, section: extracted, quote: "We designed the ﬁrst two experiments (A, B) to evaluate our metrics’ ability to quantify the inter-cluster distortion using the projections with synthetically generated False Groups (Experiment A) or Missing Groups (Experiment B) distortions respectively."
- PAPER2021ZADUREF18-E9 | page: 6, section: extracted, quote: "Experiment D: Identifying the effect of projection hyperparameters The ﬁnal experiment was conducted to evaluate the capability of our metrics to capture the inter-cluster reliability differences caused by the hyperparameter choices of an MDP technique."
- PAPER2021ZADUREF18-E10 | page: 1, section: extracted, quote: "In this paper, we propose Steadiness and Cohesiveness, two metrics that quantitatively evaluate inter-cluster reliability."
- PAPER2021ZADUREF18-E11 | page: 3, section: extracted, quote: "Steadiness and Cohesiveness evaluate how well projections avoid False and Missing Groups, respectively (C2)."
- PAPER2021ZADUREF18-E12 | page: 10, section: extracted, quote: "Perception-based evaluation of projection methods for multidimensional data visualization."
