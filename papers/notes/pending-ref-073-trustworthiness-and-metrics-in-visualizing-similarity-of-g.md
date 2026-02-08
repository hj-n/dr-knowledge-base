---
id: paper-2003-pending-ref-073
title: "Trustworthiness and metrics in visualizing similarity of gene expression"
authors: "S. Kaski, J. Nikkil €a, M. Oja, J. Venna, P. T €or€onen, and E. Castr /C19en"
venue: "BMC Bioinformatics"
year: 2003
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-073-2003-trustworthiness-and-metrics-in-visualizing-similarity-of-gene-expression.pdf
seed_note_id: "paper-2015-perception-based-projection-evaluation"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- Visualizing similarities in high-dimensional (from a few to hundreds of dimensions) data items is a difficult task since the displays can be at most three-dimensional in practice.
- The approximation has worked satisfactorily for nearestneighbor searches in empirical tests, particularly when complemented with a kind of regularization: in practice the metric will often be singular for very high-dimensional spaces, and hence we will add to it a portion of the Euclidean distance, (x, x + dx) ≡ dxT [λI + (1 - λ) J(x)] dx, (6) where I is the identity matrix.
- Visualization of functional similarity by learning metrics A main problem in comparing gene expression profiles is to choose which properties to compare, that is, how to define the similarity measure or, equivalently, the metric.
- These problems can be solved by defining the neighborhood to consist of the k nearest neighbors, where k is selected based on the number of nearby samples we are interested in analyzing.

# Method Summary
- The SOM algorithm computes such values for the model vectors that (i) the projection becomes ordered: proximate samples on the SOM display are similarly proximate in the data space, and (ii) the projection models the data distribution; each model vector becomes the centroid of all data samples mapped to it and to its neighborhood on the map display.
- Projection methods have been compared earlier for other kinds of data [1,2] but the criterion has been the capability of preserving (all) the actual distances instead of the proximities (neighborhoods).
- The learning metrics principle [14,15] is a new approach to finding important aspects of data, and expressing them in a way usable by standard data analysis and data mining methods.
- As with hierarchical clustering, the SOM can be used as both a nonlinear projection and a clustering method; clusters can be extracted from the computed SOM (see e.g. [20]).
- We compared the trustworthiness of four visualization methods: Sammon's projection, non-metric MDS, SOM, and hierarchical clustering (see the Methods Section).
- In summary, we use simple nonparametric definitions to avoid biases in favor of any of the projection methods.
- Expression in treatment 1 Expression in treatment 2 xxz y z y BMC Bioinformatics 2003, 4 http://www.biomedcentral.com/1471-2105/4/48 Page 4 of 13 (page number not for citation purposes) mapping and non-metric MDS were selected to represent MDS methods since they have beneficial properties; Sammon's mapping emphasizes the preservation of short distances which are the focus of our trustworthiness measure as well.

# When To Use / Not Use
- Use when:
  - To avoid biases in the comparison studies, we will use a simple non-parametric measure of whether samples within a set of closest samples on the display are in fact closest in the expression space as well.
  - We used this 'vanilla' version of the algorithm in its basic form and without any tricks not found in basic textbooks, to avoid biasing the study in favor of SOMs.
- Avoid when:
  - In summary, we use simple nonparametric definitions to avoid biases in favor of any of the projection methods.
  - Non-parametric measures were again used to avoid biases.
- Failure modes:
  - BioMed Central Page 1 of 13 (page number not for citation purposes) BMC Bioinformatics Open AccessResearch article Trustworthiness and metrics in visualizing similarity of gene expression Samuel Kaski*1, Janne Nikkilä1, Merja Oja1, Jarkko Venna1, Petri Törönen2 and Eero Castrén2,3 Address: 1Neural Networks Research Centre, Helsinki University of Technology P.O.

# Metrics Mentioned
- `trustworthiness`: referenced as part of projection-quality or reliability assessment.
- `continuity`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- Sammon's projection and non-metric multidimensional scaling do not have parameters to select, but the optimization can get caught in local minima, depending on the initialization.
- When the differences are measured by the Kullback-Leibler divergence DKL, the distances become locally (x, x + dx) ≡ DKL (p(c|x)||p(c|x + dx)) = dxT J(x) dx, (5) where J(x) is the Fisher information matrix with parameters x.
- The results shown in Figures 5 and 6 confirm that the new metric yielded more accurate results for the two data sets for a wide parameter range.
- The estimator has a free parameter called 'kernel width'; the value that produced the best results was selected for the subsequent experiments.
- Self-organizing map in the new metric In the first step of a SOM iteration, the best matching unit is sought in the new metric dL ( E q .
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-073-C1 | stance: support | summary: Visualizing similarities in high-dimensional (from a few to hundreds of dimensions) data items is a difficult task since the displays can be at most three-dimensional in practice. | evidence_ids: PENDING-REF-073-E1, PENDING-REF-073-E2
- CLAIM-PENDING-REF-073-C2 | stance: support | summary: The SOM algorithm computes such values for the model vectors that (i) the projection becomes ordered: proximate samples on the SOM display are similarly proximate in the data space, and (ii) the projection models the data distribution; each model vector becomes the centroid of all data samples mapped to it and to its neighborhood on the map display. | evidence_ids: PENDING-REF-073-E3, PENDING-REF-073-E4
- CLAIM-PENDING-REF-073-C3 | stance: support | summary: Sammon's projection and non-metric multidimensional scaling do not have parameters to select, but the optimization can get caught in local minima, depending on the initialization. | evidence_ids: PENDING-REF-073-E5, PENDING-REF-073-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 4 | relevance: high | note: contains initialization sensitivity or control-policy evidence

# Evidence
- PENDING-REF-073-E1 | page: 2, section: extracted, quote: "Visualizing similarities in high-dimensional (from a few to hundreds of dimensions) data items is a difficult task since the displays can be at most three-dimensional in practice."
- PENDING-REF-073-E2 | page: 12, section: extracted, quote: "The approximation has worked satisfactorily for nearestneighbor searches in empirical tests, particularly when complemented with a kind of regularization: in practice the metric will often be singular for very high-dimensional spaces, and hence we will add to it a portion of the Euclidean distance, (x, x + dx) ≡ dxT [λI + (1 - λ) J(x)] dx, (6) where I is the identity matrix."
- PENDING-REF-073-E3 | page: 5, section: extracted, quote: "Visualization of functional similarity by learning metrics A main problem in comparing gene expression profiles is to choose which properties to compare, that is, how to define the similarity measure or, equivalently, the metric."
- PENDING-REF-073-E4 | page: 11, section: extracted, quote: "These problems can be solved by defining the neighborhood to consist of the k nearest neighbors, where k is selected based on the number of nearby samples we are interested in analyzing."
- PENDING-REF-073-E5 | page: 10, section: extracted, quote: "The SOM algorithm computes such values for the model vectors that (i) the projection becomes ordered: proximate samples on the SOM display are similarly proximate in the data space, and (ii) the projection models the data distribution; each model vector becomes the centroid of all data samples mapped to it and to its neighborhood on the map display."
- PENDING-REF-073-E6 | page: 2, section: extracted, quote: "Projection methods have been compared earlier for other kinds of data [1,2] but the criterion has been the capability of preserving (all) the actual distances instead of the proximities (neighborhoods)."
- PENDING-REF-073-E7 | page: 2, section: extracted, quote: "The learning metrics principle [14,15] is a new approach to finding important aspects of data, and expressing them in a way usable by standard data analysis and data mining methods."
- PENDING-REF-073-E8 | page: 10, section: extracted, quote: "As with hierarchical clustering, the SOM can be used as both a nonlinear projection and a clustering method; clusters can be extracted from the computed SOM (see e.g. [20])."
