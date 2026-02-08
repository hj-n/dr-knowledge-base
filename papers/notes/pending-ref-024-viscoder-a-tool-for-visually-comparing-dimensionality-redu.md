---
id: paper-2018-pending-ref-024
title: "VisCoDeR: A tool for visually comparing dimensionality reduction algorithms"
authors: "René Cutura, Stefan Holzer, Michaël Aupetit, and Michael Sedlmair"
venue: "UNKNOWN"
year: 2018
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-024-2018-viscoder-a-tool-for-visually-comparing-dimensionality-reduction-algorithms.pdf
seed_note_id: "paper-2019-mdp-visual-analytics-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- This problem occurs, because the high-dimensional euclidean distance makes less sense in such high dimensions, therefore high-dimensions points become more and more similar.
- For example, a DR technique can use the euclidean distance to measure the similarity of two data points, or the geodesic distance across the K-nearest neighbor graph in the data space. • Outliers or clustered data points in the high-dimensional dataset.
- 3.1 Motivation There are two kinds of people dealing with DR: DR-experts which improve existing DR techniques or create new techniques, and DR-na ¨ıve users who are new to DR, or use DR techniques to visualize high-dimensional data.
- 4.2.1 Principal Components Analysis Principal Components Analysis (PCA) projects the high-dimensional data in a way, that the variance from the high-dimensional data X gets preserved in the projected data Y.

# Method Summary
- To speed up algorithms, where the dimensionalityD is a time-limiting factor, the dimensionality d of the projection can have more than three dimensions.
- DIPLOMARBEIT / DIPLOMA THESIS Titel der Diplomarbeit / Title of the Diploma Thesis „ VisCoDeR: A tool for Visually Comparing Dimensionality Reduction Algorithms “ verfasst von / submitted by René Čutura angestrebter akademischer Grad / in partial fulfilment of the requirements for the degree of Magister der Naturwissenschaften (Mag.rer.nat.) Wien, 2018 / Vienna 2018 Studienkennzahl lt.
- The colored points represent results of t-SNE with various parameterization. (left): The darker the point, the higher the value of ε, the brighter the point, the lower the values of ε. (right): The darker the point, the higher the value of perplexity, the brighter the point, the lower the values of perplexity. respective results in the meta t-SNE projection.
- The stress gets computed based on the distances between xi to xj, and yi to yj, where i ̸= j ∈ {1, · · · , n} by stress(X) = √   ∑ i̸=j∈{1,...,n} [ δD(xi, xj) − δd(yi, yj) ]2   Where δD describes a metric in the D-dimensional data space and δd describes a metric in the d-dimensional projection space.
- 6 3 Introduction Dimensionality reduction (DR) is an actively researched, growing set of techniques to reduce the dimensionality of data by projecting the data points from the D-dimensional data space to d-dimensional projection space, where d < D.
- Disadvantages of this non-linear DR techniques are often the meaningless new dimensions these DR techniques produce, but they produce usually better projections than linear DR techniques.
- By examining the parameter space with the Explore Mode the users can learn about the differences between DR algorithms and their behaviors with respect to the parameterization.

# When To Use / Not Use
- Use when:
  - ISOMAP with number of neighbors K = 19 has better results than MDS, because the digits are better separated. t-SNE generated the best results, the digits are good separated, with few exceptions.
  - 7.2.3 Use Case 3: Optimization A common task with visual parameter space analysis [SHB +14] is to ﬁnd a result which ﬁts best to a user’s need.
- Avoid when:
  - The task in the partition use case can also be considered as an optimization task, where a user has to ﬁnd the best ﬁtting ISOMAP projection.
  - A local minimum should be avoided, because the projection could be better, but the minimizer did not ﬁnd it.
- Failure modes:
  - This shows users that the perplexity parameter is more sensitive than the ε parameter.

# Metrics Mentioned
- `stress`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- Like the Explore mode visualizes the projections of different sets of DR technique and parameterization, the individual iteration steps could also be visualized.
- 7.2.3 Use Case 3: Optimization A common task with visual parameter space analysis [SHB +14] is to ﬁnd a result which ﬁts best to a user’s need.
- Der Play Mode erlaubt es interaktiv die Parameter w ¨ahrend der Iterationen zu ¨andern um die Auswirkungen am Verhalten beobachten zu k¨onnen.
- In this case, the goal of the optimization task is to ﬁnd the best ﬁtting combination of DR type and parameterization.
- The colored points represent results of t-SNE with various parameterization. (left): The darker the point, the higher the value of ε, the brighter the point, the lower the values of ε. (right): The darker the point, the higher the value of perplexity, the brighter the point, the lower the values of perplexity. respective results in the meta t-SNE projection.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-024-C1 | stance: support | summary: This problem occurs, because the high-dimensional euclidean distance makes less sense in such high dimensions, therefore high-dimensions points become more and more similar. | evidence_ids: PENDING-REF-024-E1, PENDING-REF-024-E2
- CLAIM-PENDING-REF-024-C2 | stance: support | summary: To speed up algorithms, where the dimensionalityD is a time-limiting factor, the dimensionality d of the projection can have more than three dimensions. | evidence_ids: PENDING-REF-024-E3, PENDING-REF-024-E4
- CLAIM-PENDING-REF-024-C3 | stance: support | summary: Like the Explore mode visualizes the projections of different sets of DR technique and parameterization, the individual iteration steps could also be visualized. | evidence_ids: PENDING-REF-024-E5, PENDING-REF-024-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-REF-024-E1 | page: 17, section: extracted, quote: "This problem occurs, because the high-dimensional euclidean distance makes less sense in such high dimensions, therefore high-dimensions points become more and more similar."
- PENDING-REF-024-E2 | page: 8, section: extracted, quote: "For example, a DR technique can use the euclidean distance to measure the similarity of two data points, or the geodesic distance across the K-nearest neighbor graph in the data space. • Outliers or clustered data points in the high-dimensional dataset."
- PENDING-REF-024-E3 | page: 8, section: extracted, quote: "3.1 Motivation There are two kinds of people dealing with DR: DR-experts which improve existing DR techniques or create new techniques, and DR-na ¨ıve users who are new to DR, or use DR techniques to visualize high-dimensional data."
- PENDING-REF-024-E4 | page: 13, section: extracted, quote: "4.2.1 Principal Components Analysis Principal Components Analysis (PCA) projects the high-dimensional data in a way, that the variance from the high-dimensional data X gets preserved in the projected data Y."
- PENDING-REF-024-E5 | page: 13, section: extracted, quote: "To speed up algorithms, where the dimensionalityD is a time-limiting factor, the dimensionality d of the projection can have more than three dimensions."
- PENDING-REF-024-E6 | page: 1, section: extracted, quote: "DIPLOMARBEIT / DIPLOMA THESIS Titel der Diplomarbeit / Title of the Diploma Thesis „ VisCoDeR: A tool for Visually Comparing Dimensionality Reduction Algorithms “ verfasst von / submitted by René Čutura angestrebter akademischer Grad / in partial fulfilment of the requirements for the degree of Magister der Naturwissenschaften (Mag.rer.nat.) Wien, 2018 / Vienna 2018 Studienkennzahl lt."
- PENDING-REF-024-E7 | page: 20, section: extracted, quote: "The colored points represent results of t-SNE with various parameterization. (left): The darker the point, the higher the value of ε, the brighter the point, the lower the values of ε. (right): The darker the point, the higher the value of perplexity, the brighter the point, the lower the values of perplexity. respective results in the meta t-SNE projection."
- PENDING-REF-024-E8 | page: 14, section: extracted, quote: "The stress gets computed based on the distances between xi to xj, and yi to yj, where i ̸= j ∈ {1, · · · , n} by stress(X) = √   ∑ i̸=j∈{1,...,n} [ δD(xi, xj) − δd(yi, yj) ]2   Where δD describes a metric in the D-dimensional data space and δd describes a metric in the d-dimensional projection space."
