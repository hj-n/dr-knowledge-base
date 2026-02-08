---
id: paper-2018-pending-ref-109
title: "Evaluating multi-dimensional visualizations for understanding fuzzy clusters"
authors: "Y . Zhao, F. Luo, M. Chen, Y . Wang, J. Xia, F. Zhou, Y . Wang, Y . Chen, and W. Chen"
venue: "BMC Bioinformatics"
year: 2018
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-109-2018-evaluating-multi-dimensional-visualizations-for-understanding-fuzzy-clusters.pdf
seed_note_id: "paper-2022-revisiting-dr-visual-cluster-analysis"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- Overview of functions included in the WGCNA package The WGCNA package contains a comprehensive set of functions for performing a correlation network analysis of large, high-dimensional data sets.
- The WGCNA package can also be used to describe the correlation structure between gene expression profiles, image data, genetic marker data, proteomics data, and other high-dimensional data.
- In practice, it is difficult to determine whether the modules underlying a meta-module are truly distinct or whether they should be merged.
- One drawback of hierarchical clustering is that it can be difficult to determine how many (if any) clusters are present in the data set.

# Method Summary
- While the methods development was motivated by gene expression data, the underlying data mining approach can be applied to a variety of different settings.
- The time and memory savings of the block-wise approach are substantial: a standard, singleblock network analysis of n nodes requires O(n 2) memory and O(n3) calculations, while the block-wise approach with block size nb requires only O( ) memory and O(n ) calculations, making an analysis of say 50 000 genes in blocks of 7 000 feasible on a standard computer.
- Weighted correlation network analysis (WGCNA) can be used for finding clusters (modules) of highly correlated genes, for summarizing such clusters using the module eigengene or an intramodular hub gene, for relating modules to one another and to external sample traits (using eigengene network methodology), and for calculating module membership measures.
- Kcor i blue , %0&%LRLQIRUPDWLFV 2008, :559 http://www.biomedcentral.com/1471-2105/9/559 Page 5 of 13 SDJHQXPEHUQRWIRUFLWDWLRQSXUSRVHV archical clustering dendrogram correspond to modules and can be identified using one of a number of available branch cutting methods, for example the constant-height cut or two Dynamic Branch Cut methods [29].
- Availability and requirements Project name: WGCNA R package Project home page: http://www.genetics.ucla.edu/labs/ horvath/CoexpressionNetwork/Rpackages/WGCNA Operating system(s): Platform independent Programming language: R Licence: GNU GPL 3 Authors' contributions Both authors jointly developed the methods and wrote the article.
- Third, Kcor i q , () %0&%LRLQIRUPDWLFV 2008, :559 http://www.biomedcentral.com/1471-2105/9/559 Page 12 of 13 SDJHQXPEHUQRWIRUFLWDWLRQSXUSRVHV although several co-expression module detection methods are implemented, the package does not provide means to determine which method is best.
- Although the height and shape parameters of the Dynamic Tree Cut method provide improved exibility for branch cutting and module detection, it remains an open research question how to choose optimal cutting parameters or how to estimate the number of clusters in the data set [30].

# When To Use / Not Use
- Use when:
  - For example, WGCNA can be used to explore the module (cluster) structure in a network, to measure the relationships between genes and modules (module membership information), to explore the relationships among modules (eigengene networks), and to rank-order genes or modules (e.g. with regard to their relationship with a sample trait).
  - The above incomplete enumeration of analysis goals shows that correlation networks can be used as a data exploratory technique (similar to cluster analysis, factor analysis, or other dimensional reduction techniques) and as a screening method.
- Avoid when:
  - Since correlation networks are based on correlations between quantitative variables, one can use a correlation test p-value [1] or a regression-based pvalue for assessing the statistical significance between pairs of variables.
  - Adjacency functions for both weighted and unweighted networks require the user to choose threshold parameters, for example by applying the approximate scale-free topology criterion [5].
- Failure modes:
  - For example, our R functions exportNetworkToVisANT and exportNetworkToCytoscape allow the user to export networks in a format suitable for VisANT [37] and Cytoscape [38], respectively.

# Metrics Mentioned
- `stress`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- Although the height and shape parameters of the Dynamic Tree Cut method provide improved exibility for branch cutting and module detection, it remains an open research question how to choose optimal cutting parameters or how to estimate the number of clusters in the data set [30].
- The package provides functions pickSoftThreshold, pickHardThreshold that assist in choosing the parameters, as well as the function scaleFreePlot for evaluating whether the network exhibits a scale free topology.
- An unweighted network adjacency a ij between gene expression profiles xi and xj can be defined by hard thresholding the co-expression similarity sij as where W is the "hard" threshold parameter.
- Adjacency functions for both weighted and unweighted networks require the user to choose threshold parameters, for example by applying the approximate scale-free topology criterion [5].
- Module genes are simulated to exhibit progressively lower correlations with the seed which leads to genes with progressively lower intramodular connectivity.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-109-C1 | stance: support | summary: Overview of functions included in the WGCNA package The WGCNA package contains a comprehensive set of functions for performing a correlation network analysis of large, high-dimensional data sets. | evidence_ids: PENDING-REF-109-E1, PENDING-REF-109-E2
- CLAIM-PENDING-REF-109-C2 | stance: support | summary: While the methods development was motivated by gene expression data, the underlying data mining approach can be applied to a variety of different settings. | evidence_ids: PENDING-REF-109-E3, PENDING-REF-109-E4
- CLAIM-PENDING-REF-109-C3 | stance: support | summary: Although the height and shape parameters of the Dynamic Tree Cut method provide improved exibility for branch cutting and module detection, it remains an open research question how to choose optimal cutting parameters or how to estimate the number of clusters in the data set [30]. | evidence_ids: PENDING-REF-109-E5, PENDING-REF-109-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 4 | relevance: high | note: contains initialization sensitivity or control-policy evidence

# Evidence
- PENDING-REF-109-E1 | page: 3, section: extracted, quote: "Overview of functions included in the WGCNA package The WGCNA package contains a comprehensive set of functions for performing a correlation network analysis of large, high-dimensional data sets."
- PENDING-REF-109-E2 | page: 12, section: extracted, quote: "The WGCNA package can also be used to describe the correlation structure between gene expression profiles, image data, genetic marker data, proteomics data, and other high-dimensional data."
- PENDING-REF-109-E3 | page: 11, section: extracted, quote: "In practice, it is difficult to determine whether the modules underlying a meta-module are truly distinct or whether they should be merged."
- PENDING-REF-109-E4 | page: 5, section: extracted, quote: "One drawback of hierarchical clustering is that it can be difficult to determine how many (if any) clusters are present in the data set."
- PENDING-REF-109-E5 | page: 1, section: extracted, quote: "While the methods development was motivated by gene expression data, the underlying data mining approach can be applied to a variety of different settings."
- PENDING-REF-109-E6 | page: 7, section: extracted, quote: "The time and memory savings of the block-wise approach are substantial: a standard, singleblock network analysis of n nodes requires O(n 2) memory and O(n3) calculations, while the block-wise approach with block size nb requires only O( ) memory and O(n ) calculations, making an analysis of say 50 000 genes in blocks of 7 000 feasible on a standard computer."
- PENDING-REF-109-E7 | page: 1, section: extracted, quote: "Weighted correlation network analysis (WGCNA) can be used for finding clusters (modules) of highly correlated genes, for summarizing such clusters using the module eigengene or an intramodular hub gene, for relating modules to one another and to external sample traits (using eigengene network methodology), and for calculating module membership measures."
- PENDING-REF-109-E8 | page: 1, section: extracted, quote: "Kcor i blue , %0&%LRLQIRUPDWLFV 2008, :559 http://www.biomedcentral.com/1471-2105/9/559 Page 5 of 13 SDJHQXPEHUQRWIRUFLWDWLRQSXUSRVHV archical clustering dendrogram correspond to modules and can be identified using one of a number of available branch cutting methods, for example the constant-height cut or two Dynamic Branch Cut methods [29]."
