---
id: paper-2007-pending-ref-068
title: "Nonlinear dimensionality reduction and data visualization: a review"
authors: "Hujun Yin"
venue: "International Journal of Automation and Computing"
year: 2007
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-068-2007-nonlinear-dimensionality-reduction-and-data-visualization-a-review.pdf
seed_note_id: "paper-2021-quantitative-survey-dr-techniques"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- Typesetting by the editors and SPi using a Springer LATEX macro package Cover design: WMX Design GmbH, Heidelberg Printed on acid-free paper SPIN: 10825826 46 /SPi 5 4 3 2 1 0 Preface In 1901, Karl Pearson [1] explained to the scientiﬁc community that the problem of data approximation is (i) important and (ii) nice, and (iii) diﬀers from the regression problem.
- This method was applied to many problems, has been transformed and rediscovered several times, and is now known under several names: mostly as PCA or as proper orthogonal decomposition.B u t the main idea remains the same: we approximate the data set by a point (this is the mean point), then by a line (ﬁrst principal component), then by a plane, etc.
- It is useful for adaptive coding and data binning, and is a model reduction method, as well as the PCA: the PCA allows us to substitute a high-dimensional vector by its projection on a best ﬁtted lowdimensional linear manifold, the K-means approach gives an approximation of a big data set by K best ﬁtted centroids.
- There exist many scientiﬁc and engineering communities that attack these problems from their own sides, and now special eﬀorts are needed to organize communication between these groups, to support exchange of ideas and technology transfer among them.

# Method Summary
- It is useful for adaptive coding and data binning, and is a model reduction method, as well as the PCA: the PCA allows us to substitute a high-dimensional vector by its projection on a best ﬁtted lowdimensional linear manifold, the K-means approach gives an approximation of a big data set by K best ﬁtted centroids.
- Obviously, in this case simplicity can be measured neither by smoothness nor dimensionality, nevertheless, manifold learning and clustering methodologies are intimately connected both in their theoretical underpinning and on a technical-algorithmic level.
- Since the birth of these two methods, several neighborhood-graph-based techniques have emerged, stimulating the development of a common theory around Laplacian eigenmaps and spectral clustering and embedding.
- The method does not explicitly construct an embedded manifold, but it has the important role of being the algorithmic forefather of “one-shot” (non-iterative) manifold learners.
- Thus, the basic loop of K-means that alternates between a projection and an optimization step became the algorithmic skeleton of many non-linear manifold learning algorithms.
- To construct such an object, they combine the method of topological grammarswith the minimization of elastic energy deﬁned for its embedding into multidimensional data space.
- The characteristic relaxation times and processes of the random walk on the graph govern the properties of spectral clustering and spectral embedding algorithms.

# When To Use / Not Use
- Use when:
  - It is useful for adaptive coding and data binning, and is a model reduction method, as well as the PCA: the PCA allows us to substitute a high-dimensional vector by its projection on a best ﬁtted lowdimensional linear manifold, the K-means approach gives an approximation of a big data set by K best ﬁtted centroids.
  - Mathematicians, engineers, software developers and advanced users from diﬀerent areas of applications attended this workshop.
- Avoid when:
  - The workshop was focused on modern theory and methodology of geometric data analysis and model reduction.
  - Springer is a part of Springer Science+Business Media springer.com c⃝ Springer-Verlag Berlin Heidelberg2008 The use of general descriptive names, registered names, trademarks, etc. in this publication does not imply, even in the absence of a speciﬁc statement, that such names are exempt from the relevant protective laws and regulations and therefore free for general use.
- Failure modes:
  - Analytically this consists in taking y = a0 + a1x, or z = a0 + a1x + b1y, or z = a0 + a1x1 + a2x2 + a3x3 + ... + anxn, where y, x, z, x 1,x 2, ...x n are variables, and determining the “best” values for constants a0, a1, b1, a0, a1, a2,...a n in relation to the observed corresponding values of the variables.

# Metrics Mentioned
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- The main drawback of iterative methods is that they are sensitive to initialization, and they can be stuck easily in suboptimal local minima, especially if the manifold is “loopy” or has a complicated topology.
- Thus, the basic loop of K-means that alternates between a projection and an optimization step became the algorithmic skeleton of many non-linear manifold learning algorithms.
- Obviously, in this case simplicity can be measured neither by smoothness nor dimensionality, nevertheless, manifold learning and clustering methodologies are intimately connected both in their theoretical underpinning and on a technical-algorithmic level.
- Since the birth of these two methods, several neighborhood-graph-based techniques have emerged, stimulating the development of a common theory around Laplacian eigenmaps and spectral clustering and embedding.
- The method does not explicitly construct an embedded manifold, but it has the important role of being the algorithmic forefather of “one-shot” (non-iterative) manifold learners.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-068-C1 | stance: support | summary: Typesetting by the editors and SPi using a Springer LATEX macro package Cover design: WMX Design GmbH, Heidelberg Printed on acid-free paper SPIN: 10825826 46 /SPi 5 4 3 2 1 0 Preface In 1901, Karl Pearson [1] explained to the scientiﬁc community that the problem of data approximation is (i) important and (ii) nice, and (iii) diﬀers from the regression problem. | evidence_ids: PENDING-REF-068-E1, PENDING-REF-068-E2
- CLAIM-PENDING-REF-068-C2 | stance: support | summary: It is useful for adaptive coding and data binning, and is a model reduction method, as well as the PCA: the PCA allows us to substitute a high-dimensional vector by its projection on a best ﬁtted lowdimensional linear manifold, the K-means approach gives an approximation of a big data set by K best ﬁtted centroids. | evidence_ids: PENDING-REF-068-E3, PENDING-REF-068-E4
- CLAIM-PENDING-REF-068-C3 | stance: support | summary: The main drawback of iterative methods is that they are sensitive to initialization, and they can be stuck easily in suboptimal local minima, especially if the manifold is “loopy” or has a complicated topology. | evidence_ids: PENDING-REF-068-E5, PENDING-REF-068-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 4 | relevance: high | note: contains initialization sensitivity or control-policy evidence

# Evidence
- PENDING-REF-068-E1 | page: 3, section: extracted, quote: "Typesetting by the editors and SPi using a Springer LATEX macro package Cover design: WMX Design GmbH, Heidelberg Printed on acid-free paper SPIN: 10825826 46 /SPi 5 4 3 2 1 0 Preface In 1901, Karl Pearson [1] explained to the scientiﬁc community that the problem of data approximation is (i) important and (ii) nice, and (iii) diﬀers from the regression problem."
- PENDING-REF-068-E2 | page: 6, section: extracted, quote: "This method was applied to many problems, has been transformed and rediscovered several times, and is now known under several names: mostly as PCA or as proper orthogonal decomposition.B u t the main idea remains the same: we approximate the data set by a point (this is the mean point), then by a line (ﬁrst principal component), then by a plane, etc."
- PENDING-REF-068-E3 | page: 6, section: extracted, quote: "It is useful for adaptive coding and data binning, and is a model reduction method, as well as the PCA: the PCA allows us to substitute a high-dimensional vector by its projection on a best ﬁtted lowdimensional linear manifold, the K-means approach gives an approximation of a big data set by K best ﬁtted centroids."
- PENDING-REF-068-E4 | page: 9, section: extracted, quote: "There exist many scientiﬁc and engineering communities that attack these problems from their own sides, and now special eﬀorts are needed to organize communication between these groups, to support exchange of ideas and technology transfer among them."
- PENDING-REF-068-E5 | page: 8, section: extracted, quote: "Obviously, in this case simplicity can be measured neither by smoothness nor dimensionality, nevertheless, manifold learning and clustering methodologies are intimately connected both in their theoretical underpinning and on a technical-algorithmic level."
- PENDING-REF-068-E6 | page: 8, section: extracted, quote: "Since the birth of these two methods, several neighborhood-graph-based techniques have emerged, stimulating the development of a common theory around Laplacian eigenmaps and spectral clustering and embedding."
- PENDING-REF-068-E7 | page: 8, section: extracted, quote: "The method does not explicitly construct an embedded manifold, but it has the important role of being the algorithmic forefather of “one-shot” (non-iterative) manifold learners."
- PENDING-REF-068-E8 | page: 8, section: extracted, quote: "Thus, the basic loop of K-means that alternates between a projection and an optimization step became the algorithmic skeleton of many non-linear manifold learning algorithms."
