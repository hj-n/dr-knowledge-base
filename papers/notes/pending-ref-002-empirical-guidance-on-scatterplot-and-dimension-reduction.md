---
id: paper-2013-pending-ref-002
title: "Empirical Guidance on Scatterplot and Dimension Reduction Technique Choices"
authors: "M. Sedlmair, T. Munzner, and M. Tory"
venue: "IEEE Transactions on Visualization and Computer Graphics"
year: 2013
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-002-2013-empirical-guidance-on-scatterplot-and-dimension-reduction-technique-choices.pdf
seed_note_id: "paper-2014-brehmer-task-sequences"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- Empirical Guidance on Scatterplot and Dimension Reduction Technique Choices Michael Sedlmair, Member, IEEE, Tamara Munzner,Member, IEEE, and Melanie Tory Abstract—To verify cluster separation in high-dimensional data, analysts often reduce the data with a dimension reduction (DR) technique, and then visualize it with 2D Scatterplots, interactive 3D Scatterplots, or Scatterplot Matrices (SPLOMs).
- When conducting visual analysis of high-dimensional data, one typical approach is to transform the original dataset using a dimensionality reduction (DR) technique to create a lower-dimensional version that preserves as much information as possible from the original, and then visually encode only the reduced data [34].
- Given the limitations of linear DR techniques, we additionally included two non-linear techniques: Glimmer MDS [21] is a representative of the well-known family of multidimensional scaling techniques that seek to optimally map point distances from the high-dimensional space into a low-dimensional projection.
- In these situations, an analyst will often engage in an iterative process of investigating class separability from other DR and visual encoding perspectives [34], with the goal of building up more conﬁdence in the real high-dimensional class structure of a dataset step by step.

# Method Summary
- However, we found that a user study was not the right methodological approach for this research question; a pilot user study with ﬁve participants, six datasets and one DR technique, revealed that the results strongly depended on the characteristics of the data as viewed in the scatterplots and not on differences between participants.
- More recently, similar approaches have been proposed that were speciﬁcally designed for cluster veriﬁcation tasks, that is, to ﬁnd 2D projections that nicely separate points of given classes [1, 36, 38].
- The recent approach of t-Distributed Stochastic Neighbor Embedding (t-SNE) [44] is a non-linear DR approach speciﬁcally designed to separate clusters well—the task we are interested in.
- However, as shown above, the low-level classwise ratings were resistant to such subjective biases and provide therefore reliable and un-biased data for our methodological approach.
- Consistency among expert coders, orinter-coder reliability, is a crucial precondition for the methodological approach we took.
- As the most promising approach, our results suggest using 2D scatterplots to explore output of different DR algorithms.
- Our data analysis is thus in the spirit of mixed methods approaches [11].

# When To Use / Not Use
- Use when:
  - In contrast to other inter-coder measures, Krippendorff’s alpha can be used for any number of coders, is robust to missing values, and works with different data types such as nominal, ordinal or ratio; for our classwise ratings Krippendorff’s alpha was 0 .858 for ordinal data; a score of .8 or greater is considered acceptable in most situations [24].
  - For scatterplots of non-DR data, there is some limited evidence that 3D may be helpful for questions requiring integrated knowledge of 3 dimensions [52]. (The data set used in this study was tiny by modern standards, with only six data points.) However, we are interested only in scatterplots of DR data, where there is substantial empirical evidence that 3D scatterplots are ineffective.
- Avoid when:
  - However, we found that a user study was not the right methodological approach for this research question; a pilot user study with ﬁve participants, six datasets and one DR technique, revealed that the results strongly depended on the characteristics of the data as viewed in the scatterplots and not on differences between participants.
  - This ﬁnding suggested that it is imperative to include a broad set of dataset characteristics to make generalizable claims; subjective differences and timing costs, as mainly tested in traditional user studies with many users and few datasets, are only of marginal interest for studying class separability across DR and VE choices.
- Failure modes:
  - Given the limitations of linear DR techniques, we additionally included two non-linear techniques: Glimmer MDS [21] is a representative of the well-known family of multidimensional scaling techniques that seek to optimally map point distances from the high-dimensional space into a low-dimensional projection.

# Metrics Mentioned
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- In that sense, our work is similar in spirit to DimStiller [20], a system that provides workﬂows to guide steps in the high-dimensional data analysis process including choices on selecting and parameterizing DR techniques.
- Trying speciﬁc DR techniques with different parameterizations might also be a promising approach.
- More recently, similar approaches have been proposed that were speciﬁcally designed for cluster veriﬁcation tasks, that is, to ﬁnd 2D projections that nicely separate points of given classes [1, 36, 38].
- The recent approach of t-Distributed Stochastic Neighbor Embedding (t-SNE) [44] is a non-linear DR approach speciﬁcally designed to separate clusters well—the task we are interested in.
- However, as shown above, the low-level classwise ratings were resistant to such subjective biases and provide therefore reliable and un-biased data for our methodological approach.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-002-C1 | stance: support | summary: Empirical Guidance on Scatterplot and Dimension Reduction Technique Choices Michael Sedlmair, Member, IEEE, Tamara Munzner,Member, IEEE, and Melanie Tory Abstract—To verify cluster separation in high-dimensional data, analysts often reduce the data with a dimension reduction (DR) technique, and then visualize it with 2D Scatterplots, interactive 3D Scatterplots, or Scatterplot Matrices (SPLOMs). | evidence_ids: PENDING-REF-002-E1, PENDING-REF-002-E2
- CLAIM-PENDING-REF-002-C2 | stance: support | summary: However, we found that a user study was not the right methodological approach for this research question; a pilot user study with ﬁve participants, six datasets and one DR technique, revealed that the results strongly depended on the characteristics of the data as viewed in the scatterplots and not on differences between participants. | evidence_ids: PENDING-REF-002-E3, PENDING-REF-002-E4
- CLAIM-PENDING-REF-002-C3 | stance: support | summary: In that sense, our work is similar in spirit to DimStiller [20], a system that provides workﬂows to guide steps in the high-dimensional data analysis process including choices on selecting and parameterizing DR techniques. | evidence_ids: PENDING-REF-002-E5, PENDING-REF-002-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-REF-002-E1 | page: 1, section: extracted, quote: "Empirical Guidance on Scatterplot and Dimension Reduction Technique Choices Michael Sedlmair, Member, IEEE, Tamara Munzner,Member, IEEE, and Melanie Tory Abstract—To verify cluster separation in high-dimensional data, analysts often reduce the data with a dimension reduction (DR) technique, and then visualize it with 2D Scatterplots, interactive 3D Scatterplots, or Scatterplot Matrices (SPLOMs)."
- PENDING-REF-002-E2 | page: 1, section: extracted, quote: "When conducting visual analysis of high-dimensional data, one typical approach is to transform the original dataset using a dimensionality reduction (DR) technique to create a lower-dimensional version that preserves as much information as possible from the original, and then visually encode only the reduced data [34]."
- PENDING-REF-002-E3 | page: 3, section: extracted, quote: "Given the limitations of linear DR techniques, we additionally included two non-linear techniques: Glimmer MDS [21] is a representative of the well-known family of multidimensional scaling techniques that seek to optimally map point distances from the high-dimensional space into a low-dimensional projection."
- PENDING-REF-002-E4 | page: 9, section: extracted, quote: "In these situations, an analyst will often engage in an iterative process of investigating class separability from other DR and visual encoding perspectives [34], with the goal of building up more conﬁdence in the real high-dimensional class structure of a dataset step by step."
- PENDING-REF-002-E5 | page: 3, section: extracted, quote: "However, we found that a user study was not the right methodological approach for this research question; a pilot user study with ﬁve participants, six datasets and one DR technique, revealed that the results strongly depended on the characteristics of the data as viewed in the scatterplots and not on differences between participants."
- PENDING-REF-002-E6 | page: 3, section: extracted, quote: "More recently, similar approaches have been proposed that were speciﬁcally designed for cluster veriﬁcation tasks, that is, to ﬁnd 2D projections that nicely separate points of given classes [1, 36, 38]."
- PENDING-REF-002-E7 | page: 3, section: extracted, quote: "The recent approach of t-Distributed Stochastic Neighbor Embedding (t-SNE) [44] is a non-linear DR approach speciﬁcally designed to separate clusters well—the task we are interested in."
- PENDING-REF-002-E8 | page: 4, section: extracted, quote: "However, as shown above, the low-level classwise ratings were resistant to such subjective biases and provide therefore reliable and un-biased data for our methodological approach."
