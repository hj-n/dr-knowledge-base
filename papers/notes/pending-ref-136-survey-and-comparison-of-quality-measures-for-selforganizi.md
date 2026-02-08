---
id: paper-2004-pending-ref-136
title: "Survey and comparison of quality measures for selforganizing maps"
authors: "G. P €olzlbauer"
venue: "Annals of Data Science"
year: 2004
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-136-2004-survey-and-comparison-of-quality-measures-for-selforganizing-maps.pdf
seed_note_id: "paper-2021-quantitative-survey-dr-techniques"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- 5.5 Clustering Algorithm Based on Spectral Graph Theory The basic idea of this kind of clustering algorithms is to regard the object as the vertex and the similarity among objects as the weighted edge in order to transform the clustering problem into a graph partition problem.
- MMC tries to ﬁnd the hyperplane with the maximum margin to cluster and it can be promoted for the multi-label clustering problem.

# Method Summary
- Analysis: (1) The time complexity of this kind of algorithm is based on the speciﬁc method and algorithms involved in the algorithm; (2) Advantages: robust, scalable, able to be parallel and taking advantage of the strengths of the involved algorithms; (3) Disadvantages: inadequate understanding about the difference among the initial clustering results, existing deﬁciencies of the design of the consensus function.
- So 19 categories of the commonly used clustering algorithms, with high practical value and well studied, are selected and one or several typical algorithm(s) of each category is(are) discussed in detail so as to give readers a systematical and clear view of the important data analysis method, clustering.
- 5.2 Clustering Algorithm Based on Ensemble Clustering algorithm based on ensemble is also called ensemble clustering, of which the core idea is to generate a set of initial clustering results by a particular method and the ﬁnal clustering result is got by integrating the initial clustering results.
- The basic idea of kernel K-means, kernel SOM and kernel FCM is to take advantage of the kernel method and the original clustering algorithm, transforming the original data into a high dimensional feature space by nonlinear kernel function in order to carry out the original clustering algorithm.
- There are mainly two kinds of model-based clustering algorithms, one based on statistical learning method and the other based on neural network learning method.
- The external evaluation, which is called as the gold standard for testing method, takes the external data to test the validity of algorithm.
- The typical algorithms, based on neural network learning method, are SOM [ 65] and ART [66–69].

# When To Use / Not Use
- Use when:
  - Analysis: (1) The time complexity of this kind of algorithm is based on the speciﬁc method and algorithms involved in the algorithm; (2) Advantages: robust, scalable, able to be parallel and taking advantage of the strengths of the involved algorithms; (3) Disadvantages: inadequate understanding about the difference among the initial clustering results, existing deﬁciencies of the design of the consensus function.
  - Analysis: (1) The time complexity of AP is O(n ˆ2*logn); (2) Advantages: simply and clear algorithm idea, insensitive to the outliers and the number of clusters not needed to be preset; (3) Disadvantages: high time complexity, not suitable for very large data set, and the clustering result sensitive to the parameters involved in AP algorithm.
- Avoid when:
  - Analysis: (1) The time complexity of FC is O(n); (2) Advantages: clustering in high efﬁciency, high scalability, dealing with outliers effectively and suitable for data with arbitrary shape and high dimension; (3) Disadvantages: the premise not completely correct, the clustering result sensitive to the parameters.
  - So 19 categories of the commonly used clustering algorithms, with high practical value and well studied, are selected and one or several typical algorithm(s) of each category is(are) discussed in detail so as to give readers a systematical and clear view of the important data analysis method, clustering.
- Failure modes:
  - The core idea of the ABC_based algorithms is to simulate the foraging behavior of three types of bee, of which the duty is to determine the food source, in a bee population and making use of the exchange of local information and global information for clustering.

# Metrics Mentioned
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- Analysis: (1) The time complexity of this kind of algorithm is based on the speciﬁc method and algorithms involved in the algorithm; (2) Advantages: robust, scalable, able to be parallel and taking advantage of the strengths of the involved algorithms; (3) Disadvantages: inadequate understanding about the difference among the initial clustering results, existing deﬁciencies of the design of the consensus function.
- Analysis: (1) The time complexity of AP is O(n ˆ2*logn); (2) Advantages: simply and clear algorithm idea, insensitive to the outliers and the number of clusters not needed to be preset; (3) Disadvantages: high time complexity, not suitable for very large data set, and the clustering result sensitive to the parameters involved in AP algorithm.
- Analysis: (1) The time complexity of FC is O(n); (2) Advantages: clustering in high efﬁciency, high scalability, dealing with outliers effectively and suitable for data with arbitrary shape and high dimension; (3) Disadvantages: the premise not completely correct, the clustering result sensitive to the parameters.
- In the following sections, especially in the analysis of time complexity, n stands for the number of total objects/data points, k stands for the number of clusters, s stands for the number of sample objects/data points, and t stands for the number of iterations.
- In the process of Mean-shift, the mean of offset of current data point is calculated at ﬁrst, the next data point is ﬁgured out based on the current data point and the offset then, and last, the iteration will be continued until some criteria are met.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-136-C1 | stance: support | summary: 5.5 Clustering Algorithm Based on Spectral Graph Theory The basic idea of this kind of clustering algorithms is to regard the object as the vertex and the similarity among objects as the weighted edge in order to transform the clustering problem into a graph partition problem. | evidence_ids: PENDING-REF-136-E1, PENDING-REF-136-E2
- CLAIM-PENDING-REF-136-C2 | stance: support | summary: Analysis: (1) The time complexity of this kind of algorithm is based on the speciﬁc method and algorithms involved in the algorithm; (2) Advantages: robust, scalable, able to be parallel and taking advantage of the strengths of the involved algorithms; (3) Disadvantages: inadequate understanding about the difference among the initial clustering results, existing deﬁciencies of the design of the consensus function. | evidence_ids: PENDING-REF-136-E3, PENDING-REF-136-E4
- CLAIM-PENDING-REF-136-C3 | stance: support | summary: Analysis: (1) The time complexity of this kind of algorithm is based on the speciﬁc method and algorithms involved in the algorithm; (2) Advantages: robust, scalable, able to be parallel and taking advantage of the strengths of the involved algorithms; (3) Disadvantages: inadequate understanding about the difference among the initial clustering results, existing deﬁciencies of the design of the consensus function. | evidence_ids: PENDING-REF-136-E5, PENDING-REF-136-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-REF-136-E1 | page: 16, section: extracted, quote: "5.5 Clustering Algorithm Based on Spectral Graph Theory The basic idea of this kind of clustering algorithms is to regard the object as the vertex and the similarity among objects as the weighted edge in order to transform the clustering problem into a graph partition problem."
- PENDING-REF-136-E2 | page: 13, section: extracted, quote: "MMC tries to ﬁnd the hyperplane with the maximum margin to cluster and it can be promoted for the multi-label clustering problem."
- PENDING-REF-136-E3 | page: 14, section: extracted, quote: "Analysis: (1) The time complexity of this kind of algorithm is based on the speciﬁc method and algorithms involved in the algorithm; (2) Advantages: robust, scalable, able to be parallel and taking advantage of the strengths of the involved algorithms; (3) Disadvantages: inadequate understanding about the difference among the initial clustering results, existing deﬁciencies of the design of the consensus function."
- PENDING-REF-136-E4 | page: 19, section: extracted, quote: "So 19 categories of the commonly used clustering algorithms, with high practical value and well studied, are selected and one or several typical algorithm(s) of each category is(are) discussed in detail so as to give readers a systematical and clear view of the important data analysis method, clustering."
- PENDING-REF-136-E5 | page: 13, section: extracted, quote: "5.2 Clustering Algorithm Based on Ensemble Clustering algorithm based on ensemble is also called ensemble clustering, of which the core idea is to generate a set of initial clustering results by a particular method and the ﬁnal clustering result is got by integrating the initial clustering results."
- PENDING-REF-136-E6 | page: 13, section: extracted, quote: "The basic idea of kernel K-means, kernel SOM and kernel FCM is to take advantage of the kernel method and the original clustering algorithm, transforming the original data into a high dimensional feature space by nonlinear kernel function in order to carry out the original clustering algorithm."
- PENDING-REF-136-E7 | page: 11, section: extracted, quote: "There are mainly two kinds of model-based clustering algorithms, one based on statistical learning method and the other based on neural network learning method."
- PENDING-REF-136-E8 | page: 3, section: extracted, quote: "The external evaluation, which is called as the gold standard for testing method, takes the external data to test the validity of algorithm."
