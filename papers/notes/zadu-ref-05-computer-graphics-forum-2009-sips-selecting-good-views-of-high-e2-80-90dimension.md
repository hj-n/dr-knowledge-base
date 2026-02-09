---
id: paper-2009-zadu-ref-05
title: "Selecting good views of high‐dimensional data using class consistency"
authors: "Mike Sips, Boris Neubert, John P. Lewis, Pat Hanrahan"
venue: "Computer Graphics Forum"
year: 2009
tags: [dr, zadu-table1-reference, dsc]
source_pdf: papers/raw/zadu-table1-references/Computer Graphics Forum - 2009 - Sips - Selecting good views of high%E2%80%90dimensional data using class consistency.pdf
evidence_level: medium
updated_at: 2026-02-08
---
# Problem
- Selecting Good Views in Large SPLOM The challenge in exploratory data analysis is to ﬁnd the highly revealing views of a high-dimensional data space.
- Lewis3 and Pat Hanrahan4 1 Max Planck Center for Visual Computing Stanford/Saarbruecken, 2 University of Konstanz, 3 Massey University, 4 Stanford University Abstract Many visualization techniques involve mapping high-dimensional data spaces to lower-dimensional views.
- Hanrahan / Selecting good views of high-dimensional data using class consistency 833 14678659, 2009, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/j.1467-8659.2009.01467.x by Yonsei University, Wiley Online Library on [07/02/2026].
- Hanrahan / Selecting good views of high-dimensional data using class consistency 835 14678659, 2009, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/j.1467-8659.2009.01467.x by Yonsei University, Wiley Online Library on [07/02/2026].
- Hanrahan / Selecting good views of high-dimensional data using class consistency 837 14678659, 2009, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/j.1467-8659.2009.01467.x by Yonsei University, Wiley Online Library on [07/02/2026].

# Method Summary
- Class Consistency Algorithms In this section we propose two methods for calculating class consistency, the centroid distance metric and distribution consistency.
- One problem with general projections and embeddings is that users may have trouble interpreting the display axes (which may be arbitrary linear or nonlinear combinations of the original variables), or the reconstructed 2–D plane (e.g.
- Summary and Conclusion In this paper we introduced class consistency as a criterion for automatically ranking and selecting good views to a class model from among the numerous possible projections of a high-dimensional data set.
- For unclassiﬁed data we applied a clustering algorithm to generate a high dimensional class structure, and applied the consistency measure to analyze the consistency of the 2–D projections.
- Although the combination of these two methods is powerful, it is still time consuming to manually explore the space of all 2–D projections in a reasonable amount of time.
- In our scenario a clustering algorithm or a supervised classiﬁcation method is an external data preprocessing step that assigns labels to data points.
- This method can be applied to data with preexisting categorical labels, or to data that has been organized into classes with a clustering algorithm.

# When To Use / Not Use
- Use when:
  - Thus, class consistency can be used as a warning sign that suggests other techniques should be tried.
  - Clumpiness works well when data points are clustered around cluster centers.
  - These methods create in general convex cluster models, because they aim to partition the data space into k clusters in a way that the quadratic distance of all cluster members to the centroid (the scatter around the centroid) is minimized.
- Avoid when:
  - Since the number of 2–D scatterplots of real world data is much higher than a human analyst can look at, we want the computer to sortout consistent views which corresponds to choosing the best scatterplots from the matrix of scatterplots.
  - One problem with general projections and embeddings is that users may have trouble interpreting the display axes (which may be arbitrary linear or nonlinear combinations of the original variables), or the reconstructed 2–D plane (e.g.
- Failure modes:
  - Because graphical displays are composed of two spatial coordinates and a limited number of visual variables such as color, texture, etc., the maximum number of dimensions that can be shown in any one view is roughly 3-8 [Ber84].
  - To demonstrate the usefulness of our measure we chose the pre-classiﬁed UCI [NHBM98] wine data set which has 3 distinct clusters deﬁned by 3 different kinds of wine and 13 attributes describing their chemical properties.

# Metrics Mentioned
- `nh`: label-based neighborhood hit.
- `nd`: neighbor-shape dissimilarity or neighbor distortion.
- `dsc`: distance consistency for class separation.
- `pr`: pairwise-distance correlation behavior.
- `proc`: Procrustes local shape agreement.

# Implementation Notes
- The correlation between these measures is reasonably strong and is not sensitive to the kernel width ( σ) parameter in the optimal region.
- Introduction Today’s scientiﬁc and business applications produce large datasets with increasing complexity and dimensionality.
- (d) Classes are spatially interleaved on a ﬁne scale.
- Summary and Conclusion In this paper we introduced class consistency as a criterion for automatically ranking and selecting good views to a class model from among the numerous possible projections of a high-dimensional data set.
- For unclassiﬁed data we applied a clustering algorithm to generate a high dimensional class structure, and applied the consistency measure to analyze the consistency of the 2–D projections.
- Although the combination of these two methods is powerful, it is still time consuming to manually explore the space of all 2–D projections in a reasonable amount of time.
- Keep preprocessing, initialization policy, and random-seed protocol fixed when comparing methods.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PAPER2009ZADUREF05-C1 | stance: support | summary: Selecting Good Views in Large SPLOM The challenge in exploratory data analysis is to ﬁnd the highly revealing views of a high-dimensional data space. | evidence_ids: PAPER2009ZADUREF05-E1, PAPER2009ZADUREF05-E2
- CLAIM-PAPER2009ZADUREF05-C2 | stance: support | summary: Class Consistency Algorithms In this section we propose two methods for calculating class consistency, the centroid distance metric and distribution consistency. | evidence_ids: PAPER2009ZADUREF05-E3, PAPER2009ZADUREF05-E4
- CLAIM-PAPER2009ZADUREF05-C3 | stance: support | summary: The correlation between these measures is reasonably strong and is not sensitive to the kernel width ( σ) parameter in the optimal region. | evidence_ids: PAPER2009ZADUREF05-E5, PAPER2009ZADUREF05-E6
- CLAIM-METRIC-DSC-SOURCE-05 | stance: support | summary: This source includes evidence relevant to `dsc` in dimensionality-reduction reliability evaluation. | evidence_ids: PAPER2009ZADUREF05-E1, PAPER2009ZADUREF05-E2

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports task clarification before model selection
- step: 2 | relevance: medium | note: adds constraints for preprocessing and data-audit checks
- step: 3 | relevance: high | note: directly informs task-aligned technique/metric selection
- step: 7 | relevance: high | note: supports visualization interpretation and user explanation

# Evidence
- PAPER2009ZADUREF05-E1 | page: 6, section: extracted, quote: "Selecting Good Views in Large SPLOM The challenge in exploratory data analysis is to ﬁnd the highly revealing views of a high-dimensional data space."
- PAPER2009ZADUREF05-E2 | page: 1, section: extracted, quote: "Lewis3 and Pat Hanrahan4 1 Max Planck Center for Visual Computing Stanford/Saarbruecken, 2 University of Konstanz, 3 Massey University, 4 Stanford University Abstract Many visualization techniques involve mapping high-dimensional data spaces to lower-dimensional views."
- PAPER2009ZADUREF05-E3 | page: 3, section: extracted, quote: "Hanrahan / Selecting good views of high-dimensional data using class consistency 833 14678659, 2009, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/j.1467-8659.2009.01467.x by Yonsei University, Wiley Online Library on [07/02/2026]."
- PAPER2009ZADUREF05-E4 | page: 5, section: extracted, quote: "Hanrahan / Selecting good views of high-dimensional data using class consistency 835 14678659, 2009, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/j.1467-8659.2009.01467.x by Yonsei University, Wiley Online Library on [07/02/2026]."
- PAPER2009ZADUREF05-E5 | page: 7, section: extracted, quote: "Hanrahan / Selecting good views of high-dimensional data using class consistency 837 14678659, 2009, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/j.1467-8659.2009.01467.x by Yonsei University, Wiley Online Library on [07/02/2026]."
- PAPER2009ZADUREF05-E6 | page: 2, section: extracted, quote: "Hanrahan / Selecting good views of high-dimensional data using class consistency832 14678659, 2009, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/j.1467-8659.2009.01467.x by Yonsei University, Wiley Online Library on [07/02/2026]."
- PAPER2009ZADUREF05-E7 | page: 4, section: extracted, quote: "Class Consistency Algorithms In this section we propose two methods for calculating class consistency, the centroid distance metric and distribution consistency."
- PAPER2009ZADUREF05-E8 | page: 3, section: extracted, quote: "One problem with general projections and embeddings is that users may have trouble interpreting the display axes (which may be arbitrary linear or nonlinear combinations of the original variables), or the reconstructed 2–D plane (e.g."
- PAPER2009ZADUREF05-E9 | page: 8, section: extracted, quote: "Summary and Conclusion In this paper we introduced class consistency as a criterion for automatically ranking and selecting good views to a class model from among the numerous possible projections of a high-dimensional data set."
- PAPER2009ZADUREF05-E10 | page: 6, section: extracted, quote: "For unclassiﬁed data we applied a clustering algorithm to generate a high dimensional class structure, and applied the consistency measure to analyze the consistency of the 2–D projections."
- PAPER2009ZADUREF05-E11 | page: 2, section: extracted, quote: "Although the combination of these two methods is powerful, it is still time consuming to manually explore the space of all 2–D projections in a reasonable amount of time."
- PAPER2009ZADUREF05-E12 | page: 3, section: extracted, quote: "In our scenario a clustering algorithm or a supervised classiﬁcation method is an external data preprocessing step that assigns labels to data points."
- PAPER2009ZADUREF05-E13 | page: 2, section: extracted, quote: "Distribution based class consistency is more general, but more expensive to compute. • We evaluate class consistency over a range of data sets with different dimensionality."
- PAPER2009ZADUREF05-E14 | page: 3, section: extracted, quote: "The classes are separated in this view and most data points are located close to class centers, resulting in a consistent view."
