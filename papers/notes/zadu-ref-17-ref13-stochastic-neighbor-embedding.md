---
id: paper-2002-zadu-ref-17
title: "Stochastic Neighbor Embedding"
authors: "Geoffrey E. Hinton, Sam T. Roweis"
venue: "Advances in Neural Information Processing Systems (NIPS 15)"
year: 2002
tags: [dr, zadu-table1-reference, kl_div, stress]
source_pdf: papers/raw/zadu-table1-references/ref13_stochastic_neighbor_embedding.pdf
evidence_level: medium
updated_at: 2026-02-08
---
# Problem
- 3 Application of SNE to image and document collections As a graphic illustration of the ability of SNE to model high-dimensional, near-neighbor relationships using only two dimensions, we ran the algorithm on a collection of bitmaps of handwritten digits and on a set of word-author counts taken from the scanned proceedings of NIPS conference papers.
- Notice that making 0  large when   is small wastes some of the probability mass in the 0 distribution so there is a cost for modeling a big distance in the high-dimensional space with a small distance in the low-dimensional space, though it is less than the cost of modeling a small distance with a big one.
- Most importantly, because of its probabilistic formulation, SNE has the ability to be extended to mixtures in which ambiguous high-dimensional objects (such as the word “bank”) can have several widely-separated images in the low-dimensional space.
- 4 A full mixture version of SNE The clean probabilistic formulation of SNE makes it easy to modify the cost function so that instead of a single image, each high-dimensional object can have several different versions of its low-dimensional image.
- Unlike self-organizing maps, in which the low-dimensional coordinates are ﬁxed to a grid and the high-dimensional ends are free to move, in SNE the high-dimensional coordinates are ﬁxed to the data and the low-dimensional points move.

# Method Summary
- Our algorithm, Stochastic Neighbor Embedding (SNE) tries to place the objects in a low-dimensional space so as to optimally preserve neighborhood identity, and can be naturally extended to allow multipledifferent low-d images of each object.
- 5 Practical optimization strategies Our current method of reducing the SNE cost is to use steepest descent with added jitter that is slowly reduced.
- 3 Application of SNE to image and document collections As a graphic illustration of the ability of SNE to model high-dimensional, near-neighbor relationships using only two dimensions, we ran the algorithm on a collection of bitmaps of handwritten digits and on a set of word-author counts taken from the scanned proceedings of NIPS conference papers.
- We also applied principal component analysis (PCA)[8] to the same data; the projection onto the ﬁrst two principal components does not separate classes nearly as cleanly as SNE because PCA is much more interested in getting the large separations right which causes it to jumble up some of the boundaries between similar classes.
- More work needs to be done before SNE is efﬁcient enough to cope with large matrices of document-word counts, but it is the only dimensionality reduction method we know of that promises to treat homonyms sensibly without going back to the original documents to disambiguate each occurrence of the homonym.
- Not all points are shown: to produce this display, digits are chosen in random order and are only displayed if a   x   region of the display centered on the 2-D location of the digit in the embedding does not overlap any of the   x   regions for digits that have already been displayed.
- The effect of changing    on the cost, C, is B 7 B      8  8    0  B 0  B    (9) Rather than optimizing the mixing proportions directly, it is easier to perform unconstrained optimization on “softmax weights” deﬁned by     4       4    .

# When To Use / Not Use
- Use when:
  - This type of “probability wormhole” seems like a good way to avoid local optima that arise because a cluster of low-dimensional points must move through a bad region of the space in order to reach a better one.
  - We also applied principal component analysis (PCA)[8] to the same data; the projection onto the ﬁrst two principal components does not separate classes nearly as cleanly as SNE because PCA is much more interested in getting the large separations right which causes it to jumble up some of the boundaries between similar classes.
  - Notice that making 0  large when   is small wastes some of the probability mass in the 0 distribution so there is a cost for modeling a big distance in the high-dimensional space with a small distance in the low-dimensional space, though it is less than the cost of modeling a small distance with a big one.
- Avoid when:
  - During the search, SNE will use the extra dimensions to go around lower-dimensional barriers but as the penalty on using these dimensions is increased, they will cease to be used, effectively constraining the embedding to the original dimensionality.
  - Most importantly, because of its probabilistic formulation, SNE has the ability to be extended to mixtures in which ambiguous high-dimensional objects (such as the word “bank”) can have several widely-separated images in the low-dimensional space.
- Failure modes:
  - A Gaussian is centered on each object in the high-dimensional space and the densities under this Gaussian (or the given dissimilarities) are used to deﬁne a probability distribution over all the potential neighbors of the object.
  - This raises the question of what SNE is doing when the variance, )   , of the Gaussian centered on each high-dimensional point is very big so that the distribution across neighbors is almost uniform.

# Metrics Mentioned
- `nh`: label-based neighborhood hit.
- `nd`: neighbor-shape dissimilarity or neighbor distortion.
- `kl_div`: Kullback-Leibler divergence behavior.
- `pr`: pairwise-distance correlation behavior.
- `topo`: topology-related structure behavior.
- `proc`: Procrustes local shape agreement.
- `stress`: stress-based distance distortion.

# Implementation Notes
- 6 Discussion and Conclusions Preliminary experiments show that we can ﬁnd good optima by ﬁrst annealing the perplexities )   (using high jitter) and only reducing the jitter after the ﬁnal perplexity has been reached.
- Conclusions Preliminary experiments show that we can ﬁnd good optima by ﬁrst annealing the perplexities )   (using high jitter) and only reducing the jitter after the ﬁnal perplexity has been reached.
- For this example we used a perplexity of   in deﬁning the local neighborhoods, a step size of for each position update of  times the gradient, and used a constant jitter of    .
- The variance of the Gaussian around each point in the (  -dimensional raw pixel image space was set to achieve a perplexity of 15 in the distribution over high-dimensional neighbors.
- For other parameter settings, however, the circle may fragment into two or more smaller line-segments, each of which is topologically correct but which may not be linked to each other.
- Computational physics has attacked exactly this same complexity when performing multibody gravitational or electrostatic simulations using, for example, the fast multipole method.
- Keep preprocessing, initialization policy, and random-seed protocol fixed when comparing methods.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PAPER2002ZADUREF17-C1 | stance: support | summary: 3 Application of SNE to image and document collections As a graphic illustration of the ability of SNE to model high-dimensional, near-neighbor relationships using only two dimensions, we ran the algorithm on a collection of bitmaps of handwritten digits and on a set of word-author counts taken from the scanned proceedings of NIPS conference papers. | evidence_ids: PAPER2002ZADUREF17-E1, PAPER2002ZADUREF17-E2
- CLAIM-PAPER2002ZADUREF17-C2 | stance: support | summary: Our algorithm, Stochastic Neighbor Embedding (SNE) tries to place the objects in a low-dimensional space so as to optimally preserve neighborhood identity, and can be naturally extended to allow multipledifferent low-d images of each object. | evidence_ids: PAPER2002ZADUREF17-E3, PAPER2002ZADUREF17-E4
- CLAIM-PAPER2002ZADUREF17-C3 | stance: support | summary: 6 Discussion and Conclusions Preliminary experiments show that we can ﬁnd good optima by ﬁrst annealing the perplexities )   (using high jitter) and only reducing the jitter after the ﬁnal perplexity has been reached. | evidence_ids: PAPER2002ZADUREF17-E5, PAPER2002ZADUREF17-E6
- CLAIM-METRIC-KL_DIV-SOURCE-17 | stance: support | summary: This source includes evidence relevant to `kl_div` in dimensionality-reduction reliability evaluation. | evidence_ids: PAPER2002ZADUREF17-E1, PAPER2002ZADUREF17-E2
- CLAIM-METRIC-STRESS-SOURCE-17 | stance: support | summary: This source includes evidence relevant to `stress` in dimensionality-reduction reliability evaluation. | evidence_ids: PAPER2002ZADUREF17-E1, PAPER2002ZADUREF17-E2

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports task clarification before model selection
- step: 2 | relevance: medium | note: adds constraints for preprocessing and data-audit checks
- step: 3 | relevance: high | note: directly informs task-aligned technique/metric selection
- step: 6 | relevance: high | note: adds hyperparameter sensitivity or optimization guidance
- step: 7 | relevance: high | note: supports visualization interpretation and user explanation

# Evidence
- PAPER2002ZADUREF17-E1 | page: 3, section: extracted, quote: "3 Application of SNE to image and document collections As a graphic illustration of the ability of SNE to model high-dimensional, near-neighbor relationships using only two dimensions, we ran the algorithm on a collection of bitmaps of handwritten digits and on a set of word-author counts taken from the scanned proceedings of NIPS conference papers."
- PAPER2002ZADUREF17-E2 | page: 2, section: extracted, quote: "Notice that making 0  large when   is small wastes some of the probability mass in the 0 distribution so there is a cost for modeling a big distance in the high-dimensional space with a small distance in the low-dimensional space, though it is less than the cost of modeling a small distance with a big one."
- PAPER2002ZADUREF17-E3 | page: 8, section: extracted, quote: "Most importantly, because of its probabilistic formulation, SNE has the ability to be extended to mixtures in which ambiguous high-dimensional objects (such as the word “bank”) can have several widely-separated images in the low-dimensional space."
- PAPER2002ZADUREF17-E4 | page: 3, section: extracted, quote: "4 A full mixture version of SNE The clean probabilistic formulation of SNE makes it easy to modify the cost function so that instead of a single image, each high-dimensional object can have several different versions of its low-dimensional image."
- PAPER2002ZADUREF17-E5 | page: 8, section: extracted, quote: "Unlike self-organizing maps, in which the low-dimensional coordinates are ﬁxed to a grid and the high-dimensional ends are free to move, in SNE the high-dimensional coordinates are ﬁxed to the data and the low-dimensional points move."
- PAPER2002ZADUREF17-E6 | page: 1, section: extracted, quote: "A Gaussian is centered on each object in the high-dimensional space and the densities under this Gaussian (or the given dissimilarities) are used to deﬁne a probability distribution over all the potential neighbors of the object."
- PAPER2002ZADUREF17-E7 | page: 1, section: extracted, quote: "Our algorithm, Stochastic Neighbor Embedding (SNE) tries to place the objects in a low-dimensional space so as to optimally preserve neighborhood identity, and can be naturally extended to allow multipledifferent low-d images of each object."
- PAPER2002ZADUREF17-E8 | page: 7, section: extracted, quote: "5 Practical optimization strategies Our current method of reducing the SNE cost is to use steepest descent with added jitter that is slowly reduced."
- PAPER2002ZADUREF17-E9 | page: 3, section: extracted, quote: "We also applied principal component analysis (PCA)[8] to the same data; the projection onto the ﬁrst two principal components does not separate classes nearly as cleanly as SNE because PCA is much more interested in getting the large separations right which causes it to jumble up some of the boundaries between similar classes."
- PAPER2002ZADUREF17-E10 | page: 6, section: extracted, quote: "More work needs to be done before SNE is efﬁcient enough to cope with large matrices of document-word counts, but it is the only dimensionality reduction method we know of that promises to treat homonyms sensibly without going back to the original documents to disambiguate each occurrence of the homonym."
- PAPER2002ZADUREF17-E11 | page: 4, section: extracted, quote: "Not all points are shown: to produce this display, digits are chosen in random order and are only displayed if a   x   region of the display centered on the 2-D location of the digit in the embedding does not overlap any of the   x   regions for digits that have already been displayed."
- PAPER2002ZADUREF17-E12 | page: 6, section: extracted, quote: "The effect of changing    on the cost, C, is B 7 B      8  8    0  B 0  B    (9) Rather than optimizing the mixing proportions directly, it is easier to perform unconstrained optimization on “softmax weights” deﬁned by     4       4    ."
