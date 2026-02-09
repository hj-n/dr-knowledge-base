---
id: paper-2021-zadu-ref-19
title: "A Comparison for Dimensionality Reduction Methods of Single-Cell RNA-seq Data"
authors: "Ruizhi Xiang, Wencan Wang, Lei Yang, Shiyuan Wang, Chaohan Xu, Xiaowen Chen"
venue: "Frontiers in Genetics"
year: 2021
tags: [dr, zadu-table1-reference, c_evm, ivm]
source_pdf: papers/raw/zadu-table1-references/ref42_a_comparison_for_dimensionality_reduction_methods_of_single_cell_rna_seq_data.pdf
evidence_level: medium
updated_at: 2026-02-08
---
# Problem
- Pierson and Y au (2015) modiﬁed the factor analysis framework to solve the dropout problem and provided a method zero-inﬂated factor analysis (ZIFA) based on an additional zero-inﬂation modulation layer for reducing the dimension of single-cell gene expression data.
- It excels at revealing local structure in high-dimensional data. t-SNE is based on the SNE (Hinton and Roweis, 2002), which starts from converting the highdimensional Euclidean distances between data points into conditional probabilities that represent similarities.
- However, such analysis heavily relies on the accurate similarity assessment of a pair of cells, which poses unique challenges such as outlier cell populations, transcript ampliﬁcation noise, and dropout events.
- GrandPrix optimizes the coordinate position in the latent space by maximizing the joint density of the observation data, and then establishes a mapping from low-dimensional space to high-dimensional space.
- Therefore, dimensionality reduction is necessary to project high-dimensional data into low-dimensional space to visualize the cluster structures and development trajectory inference.

# Method Summary
- Single-cell interpretation via multikernel learning used the stochastic neighbor embedding (SNE) method (Maaten and Hinton, 2008) to dimension reduction based on the cellto-cell similarity S learned from the above optimization model.
- In addition, there are non-linear methods such as uniform manifold approximation and projection (UMAP) and t-distributed stochastic neighbor embedding (tSNE) to reduce dimension.
- Data Preprocessing of All Methods For the arithmetic design adapting to diﬀerent algorithms, we performed the corresponding normalization process for one raw single-cell RNA-seq data based on the description of the algorithm.
- In this study, we performed a comprehensive evaluation of 10 diﬀerent dimensionality reduction algorithms comprising the linear method, the non-linear method, the neural network, model-based method, and ensemble method.
- Compared with the above two linear methods, employing the zero-inﬂation model can give ZIFA more powerful projection capabilities but will pay a corresponding cost in computational complexity.
- To evaluate the overall stability of each method, we aggregated all the metrics across simulation datasets to obtain the overall stability score (see section “Materials and Methods”).
- We hope that this will be useful in providing and giving method users and algorithm developers an exhaustive evaluation of diﬀerent data and appropriate recommendation guidelines.

# When To Use / Not Use
- Use when:
  - We suggested that users adjust the hyperparameters when using these non-linear and neural network methods.
  - When calculating the running time, we used the function system.time() in R.
  - In addition, there are some new theoretical frameworks such as the multikernel learning [single-cell interpretation via multikernel learning (SIMLR)] based on the above methods that have been or are being developed to handle increasingly diverse scRNAseq data.
- Avoid when:
  - Single-cell interpretation via multikernel learning used the stochastic neighbor embedding (SNE) method (Maaten and Hinton, 2008) to dimension reduction based on the cellto-cell similarity S learned from the above optimization model.
  - Taking into account the randomness of k-means clustering when setting the initial cluster centroids, we performed k-means clustering 50 times to obtain a stable metric, and then set the cluster number k to the true cell type number.
- Failure modes:
  - ICA Independent component analysis (ICA) (Liebermeister, 2002), also known as blind source separation (BSS), is a statistical calculation technique used to reveal the factors behind random variables, measured values, and signals.
  - Although whole-transcriptome analyses avoid the bias of using a predeﬁned gene set (Jiang et al., 2015), the dimensionality of such datasets is typically too high for most modeling algorithms to process directly.

# Metrics Mentioned
- `nd`: neighbor-shape dissimilarity or neighbor distortion.
- `kl_div`: Kullback-Leibler divergence behavior.
- `pr`: pairwise-distance correlation behavior.
- `ivm`: internal clustering validation behavior.
- `c_evm`: external clustering validation against labels.
- `topo`: topology-related structure behavior.
- `proc`: Procrustes local shape agreement.

# Implementation Notes
- For those methods with multiple adjustable hyperparameters including GrandPrix, scvis, UMAP , and V AE, we noticed a dramatic change in the results when choosing diﬀerent hyperparameter settings ( Figures 6D–G ).
- Here, we performed a comprehensive evaluation of 10 dimensionality reduction methods using simulation and real dataset to examine the stability, accuracy, computing cost, and sensitivity to hyperparameters.
- In addition, it is worth noting that users need to set the hyperparameters according to the speciﬁc situation before using the dimensionality reduction methods based on non-linear model and neural network.
- Sensitivity of Methods to Hyperparameters The hyperparameters play a crucial part of the dimension reduction algorithm, especially the deep machine learning model.
- Therefore, we examined the eﬀect of the hyperparameter settings on the dimensionality reduction in order to guide the user in making a reasonable choice.
- To decrease time consumption, we used the datasets of Deng to investigate the eﬀect of the hyperparameters to the performance of these seven methods.
- Keep preprocessing, initialization policy, and random-seed protocol fixed when comparing methods.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PAPER2021ZADUREF19-C1 | stance: support | summary: Pierson and Y au (2015) modiﬁed the factor analysis framework to solve the dropout problem and provided a method zero-inﬂated factor analysis (ZIFA) based on an additional zero-inﬂation modulation layer for reducing the dimension of single-cell gene expression data. | evidence_ids: PAPER2021ZADUREF19-E1, PAPER2021ZADUREF19-E2
- CLAIM-PAPER2021ZADUREF19-C2 | stance: support | summary: Single-cell interpretation via multikernel learning used the stochastic neighbor embedding (SNE) method (Maaten and Hinton, 2008) to dimension reduction based on the cellto-cell similarity S learned from the above optimization model. | evidence_ids: PAPER2021ZADUREF19-E3, PAPER2021ZADUREF19-E4
- CLAIM-PAPER2021ZADUREF19-C3 | stance: support | summary: For those methods with multiple adjustable hyperparameters including GrandPrix, scvis, UMAP , and V AE, we noticed a dramatic change in the results when choosing diﬀerent hyperparameter settings ( Figures 6D–G ). | evidence_ids: PAPER2021ZADUREF19-E5, PAPER2021ZADUREF19-E6
- CLAIM-METRIC-C_EVM-SOURCE-19 | stance: support | summary: This source includes evidence relevant to `c_evm` in dimensionality-reduction reliability evaluation. | evidence_ids: PAPER2021ZADUREF19-E1, PAPER2021ZADUREF19-E2
- CLAIM-METRIC-IVM-SOURCE-19 | stance: support | summary: This source includes evidence relevant to `ivm` in dimensionality-reduction reliability evaluation. | evidence_ids: PAPER2021ZADUREF19-E1, PAPER2021ZADUREF19-E2

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports task clarification before model selection
- step: 2 | relevance: medium | note: adds constraints for preprocessing and data-audit checks
- step: 3 | relevance: high | note: directly informs task-aligned technique/metric selection
- step: 6 | relevance: high | note: adds hyperparameter sensitivity or optimization guidance
- step: 7 | relevance: high | note: supports visualization interpretation and user explanation

# Evidence
- PAPER2021ZADUREF19-E1 | page: 2, section: extracted, quote: "Pierson and Y au (2015) modiﬁed the factor analysis framework to solve the dropout problem and provided a method zero-inﬂated factor analysis (ZIFA) based on an additional zero-inﬂation modulation layer for reducing the dimension of single-cell gene expression data."
- PAPER2021ZADUREF19-E2 | page: 4, section: extracted, quote: "It excels at revealing local structure in high-dimensional data. t-SNE is based on the SNE (Hinton and Roweis, 2002), which starts from converting the highdimensional Euclidean distances between data points into conditional probabilities that represent similarities."
- PAPER2021ZADUREF19-E3 | page: 1, section: extracted, quote: "However, such analysis heavily relies on the accurate similarity assessment of a pair of cells, which poses unique challenges such as outlier cell populations, transcript ampliﬁcation noise, and dropout events."
- PAPER2021ZADUREF19-E4 | page: 2, section: extracted, quote: "GrandPrix optimizes the coordinate position in the latent space by maximizing the joint density of the observation data, and then establishes a mapping from low-dimensional space to high-dimensional space."
- PAPER2021ZADUREF19-E5 | page: 2, section: extracted, quote: "Therefore, dimensionality reduction is necessary to project high-dimensional data into low-dimensional space to visualize the cluster structures and development trajectory inference."
- PAPER2021ZADUREF19-E6 | page: 5, section: extracted, quote: "The optimization problem has three variables: the similarity matrix S, the weight vector w, and an N× C rank-enforcing matrix L."
- PAPER2021ZADUREF19-E7 | page: 5, section: extracted, quote: "Single-cell interpretation via multikernel learning used the stochastic neighbor embedding (SNE) method (Maaten and Hinton, 2008) to dimension reduction based on the cellto-cell similarity S learned from the above optimization model."
- PAPER2021ZADUREF19-E8 | page: 2, section: extracted, quote: "In addition, there are non-linear methods such as uniform manifold approximation and projection (UMAP) and t-distributed stochastic neighbor embedding (tSNE) to reduce dimension."
- PAPER2021ZADUREF19-E9 | page: 8, section: extracted, quote: "Data Preprocessing of All Methods For the arithmetic design adapting to diﬀerent algorithms, we performed the corresponding normalization process for one raw single-cell RNA-seq data based on the description of the algorithm."
- PAPER2021ZADUREF19-E10 | page: 2, section: extracted, quote: "In this study, we performed a comprehensive evaluation of 10 diﬀerent dimensionality reduction algorithms comprising the linear method, the non-linear method, the neural network, model-based method, and ensemble method."
- PAPER2021ZADUREF19-E11 | page: 2, section: extracted, quote: "Compared with the above two linear methods, employing the zero-inﬂation model can give ZIFA more powerful projection capabilities but will pay a corresponding cost in computational complexity."
- PAPER2021ZADUREF19-E12 | page: 6, section: extracted, quote: "To evaluate the overall stability of each method, we aggregated all the metrics across simulation datasets to obtain the overall stability score (see section “Materials and Methods”)."
- PAPER2021ZADUREF19-E13 | page: 2, section: extracted, quote: "Dimensionality Reduction Method Comparison dimensions: one denotes how far it has progressed in its diﬀerentiation toward a particular cell type, and at least another dimension denotes its current cell-cycle stage."
- PAPER2021ZADUREF19-E14 | page: 3, section: extracted, quote: "Dimensionality Reduction Method Comparison FIGURE 1 / An overview for benchmarking dimensionality reduction methods."
