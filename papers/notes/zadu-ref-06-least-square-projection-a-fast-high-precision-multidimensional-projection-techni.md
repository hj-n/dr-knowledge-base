---
id: paper-2008-zadu-ref-06
title: "Least Square Projection: A Fast High-Precision Multidimensional Projection Technique and Its Application to Document Mapping"
authors: "F.V. Paulovich, L.G. Nonato, R. Minghim, H. Levkowitz"
venue: "IEEE Transactions on Visualization and Computer Graphics"
year: 2008
tags: [dr, zadu-table1-reference, stress]
source_pdf: papers/raw/zadu-table1-references/Least_Square_Projection_A_Fast_High-Precision_Multidimensional_Projection_Technique_and_Its_Application_to_Document_Mapping.pdf
evidence_level: medium
updated_at: 2026-02-08
---
# Problem
- For the precision tests, we have used distances based on vector representations and also a new stream-based similarity measure based on the approximation by compression of the Kolmogorov Complexity [38] slightly modified to accommodate problems related with compressor accuracy [39], called Scaled Normalized Compression PAULOVICH ET AL.: LEAST SQUARE PROJECTION: A FAST HIGH-PRECISION MULTIDIMENSIONAL PROJECTION TECHNIQUE AND ITS...
- Conventional methods for multidimensional data visualization such as scatterplots, parallel coordinates, or pixel-oriented methods, which are normally employed to assist data interpretation, can fail if they are directly applied to high-dimensional data (a good review of data visualization methods can be found in [1]).
- Paulovich, Luis Gustavo Nonato, Rosane Minghim, and Haim Levkowitz, Member, IEEE Abstract—The problem of projecting multidimensional data into lower dimensions has been pursued by many researchers due to its potential application to data analyses of various kinds.
- 5C ONCLUSIONS AND FUTURE WORK We have presented LSP, a multidimensional projection technique that is able to project high-dimensional large data sets in a satisfactory computational time, reconstructing well similarity measures given for a data set.
- The problem of multidimensional projection has been the concern of many researchers due to the large variety of applications that could benefit from visual representations of data sets with large number of dimensions.

# Method Summary
- It starts by defining a function that indicates the amount of information lost in the projection and then applies an iterative nonlinear optimization method based on the gradient of this function to find a (local) minimum.
- One aspect that should be further investigated is how the parameters involved in LSP can be refined and whether that can help customize the projection method for particular applications, for example, how the optimal number of neighbors and control points for a given data set can be found.
- 3L EAST SQUARE PROJECTION Given a set of points S ¼f p1; ... ;p ng in IRm,t h eL S P algorithm aims at representing the points of S in a lower dimensional space IRd, d /C20 m, so as to preserve the neighborhood relationship among the points as much as possible.
- Since that positioning is normally based on an optimization process, two projections are similar if the amount of information lost during control point placement is the same for both (for instance, in terms of stress).
- In fact, the choice of the control points affects significantly the quality of the projection, making it an interesting challenge to design an efficient algorithm to perform such a task.
- This paper presents a novel multidimensional projection technique, called Least Square Projection (LSP), that encompasses good features of both linear and nonlinear projection methods.
- Although this is not discussed here, LSP can also be used as an interpolation method for any kind of dimensionality reduction method and not only for projection techniques.

# When To Use / Not Use
- Use when:
  - The total time spent was 227.672 s, indicating an added degree of scalability when compared to MDS and other techniques that can be used to create effective multidimensional projections.
  - For the precision tests, we have used distances based on vector representations and also a new stream-based similarity measure based on the approximation by compression of the Kolmogorov Complexity [38] slightly modified to accommodate problems related with compressor accuracy [39], called Scaled Normalized Compression PAULOVICH ET AL.: LEAST SQUARE PROJECTION: A FAST HIGH-PRECISION MULTIDIMENSIONAL PROJECTION TECHNIQUE AND ITS...
  - The stress function defined by Kruskal [36] is presented as follows: stress ¼ ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ ﬃ P i<j ðdðfðxiÞ;f ðxjÞÞ /C0 /C14ðxi;x jÞÞ2 P i<j dðfðxiÞ;f ðxjÞÞ2 vuu u u t : ð5Þ Although the stress can be useful in assessing different projections, it is common to find examples of incompatibility between the stress and the visual interpretation of layouts.
- Avoid when:
  - Exploring similarity in neighborhoods allows a user to accomplish interesting tasks such as searching for topics of interest among the coherent groups mapped (see [42] for instance), searching for similar documents to the ones he/ she already knows, having an idea of the main structure and frequency of certain concepts, and relating concepts that are seemingly not associated.
  - Once the similarity is compatible with a user’s requirements (in other words, if a proper similarity measure is fit to a certain application), LSP is bound to reflect that in the final map in the form of groups of similar data points, allowing exploration in overview (the whole map) and detail (focusing on groups) of that data set.
- Failure modes:
  - Conventional methods for multidimensional data visualization such as scatterplots, parallel coordinates, or pixel-oriented methods, which are normally employed to assist data interpretation, can fail if they are directly applied to high-dimensional data (a good review of data visualization methods can be found in [1]).
  - Aside from being able to create projections of different types of data, the software that implements LSP (PEx) has some mechanisms to help the user interact with the projections and extract useful information from them, particularly for displays of document collections.

# Metrics Mentioned
- `nh`: label-based neighborhood hit.
- `nd`: neighbor-shape dissimilarity or neighbor distortion.
- `pr`: pairwise-distance correlation behavior.
- `topo`: topology-related structure behavior.
- `proc`: Procrustes local shape agreement.
- `stress`: stress-based distance distortion.

# Implementation Notes
- For the precision tests, we have used distances based on vector representations and also a new stream-based similarity measure based on the approximation by compression of the Kolmogorov Complexity [38] slightly modified to accommodate problems related with compressor accuracy [39], called Scaled Normalized Compression PAULOVICH ET AL.: LEAST SQUARE PROJECTION: A FAST HIGH-PRECISION MULTIDIMENSIONAL PROJECTION TECHNIQUE AND ITS...
- The process for the interpolation is the one that makes this technique Oðn 3 2Þ; therefore, Morrison and Chalmers [21] suggest a modification of this interpolation, reducing the final complexity to Oðn 5 4Þ, whereas Jourdan and Melancon [22] suggest a further approach to reduce it to Oðn log n Þ.
- One aspect that should be further investigated is how the parameters involved in LSP can be refined and whether that can help customize the projection method for particular applications, for example, how the optimal number of neighbors and control points for a given data set can be found.
- Aiming at reducing this complexity, Paulovich and Minghim [17] proposed a new method, where the instances are first clustered, and Force is applied, considering the instances of each separated cluster, defining a model whose complexity is Oðn 3 2Þ.
- The overall complexity of LSP can be calculated as OðC þ N þ SÞ, where C is the complexity for choosing the control points, N is the complexity for defining the neighborhood, and S is the complexity for solving the linear system.
- We have presented an initial version of LSP before [4], now significantly extended to employ automatically defined weights to improve control-point definition and to reduce the computational complexity.
- Keep preprocessing, initialization policy, and random-seed protocol fixed when comparing methods.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PAPER2008ZADUREF06-C1 | stance: support | summary: For the precision tests, we have used distances based on vector representations and also a new stream-based similarity measure based on the approximation by compression of the Kolmogorov Complexity [38] slightly modified to accommodate problems related with compressor accuracy [39], called Scaled Normalized Compression PAULOVICH ET AL.: LEAST SQUARE PROJECTION: A FAST HIGH-PRECISION MULTIDIMENSIONAL PROJECTION TECHNIQUE AND ITS... | evidence_ids: PAPER2008ZADUREF06-E1, PAPER2008ZADUREF06-E2
- CLAIM-PAPER2008ZADUREF06-C2 | stance: support | summary: It starts by defining a function that indicates the amount of information lost in the projection and then applies an iterative nonlinear optimization method based on the gradient of this function to find a (local) minimum. | evidence_ids: PAPER2008ZADUREF06-E3, PAPER2008ZADUREF06-E4
- CLAIM-PAPER2008ZADUREF06-C3 | stance: support | summary: For the precision tests, we have used distances based on vector representations and also a new stream-based similarity measure based on the approximation by compression of the Kolmogorov Complexity [38] slightly modified to accommodate problems related with compressor accuracy [39], called Scaled Normalized Compression PAULOVICH ET AL.: LEAST SQUARE PROJECTION: A FAST HIGH-PRECISION MULTIDIMENSIONAL PROJECTION TECHNIQUE AND ITS... | evidence_ids: PAPER2008ZADUREF06-E5, PAPER2008ZADUREF06-E6
- CLAIM-METRIC-STRESS-SOURCE-06 | stance: support | summary: This source includes evidence relevant to `stress` in dimensionality-reduction reliability evaluation. | evidence_ids: PAPER2008ZADUREF06-E1, PAPER2008ZADUREF06-E2

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports task clarification before model selection
- step: 2 | relevance: medium | note: adds constraints for preprocessing and data-audit checks
- step: 3 | relevance: high | note: directly informs task-aligned technique/metric selection
- step: 6 | relevance: high | note: adds hyperparameter sensitivity or optimization guidance
- step: 7 | relevance: high | note: supports visualization interpretation and user explanation

# Evidence
- PAPER2008ZADUREF06-E1 | page: 8, section: extracted, quote: "For the precision tests, we have used distances based on vector representations and also a new stream-based similarity measure based on the approximation by compression of the Kolmogorov Complexity [38] slightly modified to accommodate problems related with compressor accuracy [39], called Scaled Normalized Compression PAULOVICH ET AL.: LEAST SQUARE PROJECTION: A FAST HIGH-PRECISION MULTIDIMENSIONAL PROJECTION TECHNIQUE AND ITS..."
- PAPER2008ZADUREF06-E2 | page: 1, section: extracted, quote: "Conventional methods for multidimensional data visualization such as scatterplots, parallel coordinates, or pixel-oriented methods, which are normally employed to assist data interpretation, can fail if they are directly applied to high-dimensional data (a good review of data visualization methods can be found in [1])."
- PAPER2008ZADUREF06-E3 | page: 1, section: extracted, quote: "Paulovich, Luis Gustavo Nonato, Rosane Minghim, and Haim Levkowitz, Member, IEEE Abstract—The problem of projecting multidimensional data into lower dimensions has been pursued by many researchers due to its potential application to data analyses of various kinds."
- PAPER2008ZADUREF06-E4 | page: 10, section: extracted, quote: "5C ONCLUSIONS AND FUTURE WORK We have presented LSP, a multidimensional projection technique that is able to project high-dimensional large data sets in a satisfactory computational time, reconstructing well similarity measures given for a data set."
- PAPER2008ZADUREF06-E5 | page: 1, section: extracted, quote: "The problem of multidimensional projection has been the concern of many researchers due to the large variety of applications that could benefit from visual representations of data sets with large number of dimensions."
- PAPER2008ZADUREF06-E6 | page: 1, section: extracted, quote: "Moreover, identification of patterns and models grows more difficult as dimensionality increases (the dimensionality curse [2]), and the lack of proper representations can severely impair interpretation."
- PAPER2008ZADUREF06-E7 | page: 2, section: extracted, quote: "It starts by defining a function that indicates the amount of information lost in the projection and then applies an iterative nonlinear optimization method based on the gradient of this function to find a (local) minimum."
- PAPER2008ZADUREF06-E8 | page: 11, section: extracted, quote: "One aspect that should be further investigated is how the parameters involved in LSP can be refined and whether that can help customize the projection method for particular applications, for example, how the optimal number of neighbors and control points for a given data set can be found."
- PAPER2008ZADUREF06-E9 | page: 3, section: extracted, quote: "3L EAST SQUARE PROJECTION Given a set of points S ¼f p1; ... ;p ng in IRm,t h eL S P algorithm aims at representing the points of S in a lower dimensional space IRd, d /C20 m, so as to preserve the neighborhood relationship among the points as much as possible."
- PAPER2008ZADUREF06-E10 | page: 7, section: extracted, quote: "Since that positioning is normally based on an optimization process, two projections are similar if the amount of information lost during control point placement is the same for both (for instance, in terms of stress)."
- PAPER2008ZADUREF06-E11 | page: 11, section: extracted, quote: "In fact, the choice of the control points affects significantly the quality of the projection, making it an interesting challenge to design an efficient algorithm to perform such a task."
- PAPER2008ZADUREF06-E12 | page: 2, section: extracted, quote: "This paper presents a novel multidimensional projection technique, called Least Square Projection (LSP), that encompasses good features of both linear and nonlinear projection methods."
- PAPER2008ZADUREF06-E13 | page: 2, section: extracted, quote: "This paper presents a novel multidimensional projection technique, called Least Square Projection (LSP), that encompasses good features of both linear and nonlinear projection methods."
- PAPER2008ZADUREF06-E14 | page: 3, section: extracted, quote: "In the general case, where each instance is connected to all other instances, the iteration of the FDP model’s complexity is Oðn2Þ."
