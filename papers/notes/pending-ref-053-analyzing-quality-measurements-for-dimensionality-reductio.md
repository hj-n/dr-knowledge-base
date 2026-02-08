---
id: paper-2023-pending-ref-053
title: "Analyzing quality measurements for dimensionality reduction"
authors: "M. C. Thrun, J. Märte, and Q. Stier"
venue: "Proceedings of the IEEE"
year: 2023
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-053-2023-analyzing-quality-measurements-for-dimensionality-reduction.pdf
seed_note_id: "paper-2025-critical-analysis-dr-four-domains"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- If we consider an image as a point in a high-dimensional pixel space (where the dimensionality equals the number of pixels), then an evolving distortion of a character traces out a curve in pixel space.
- Finding the support vectors and the coefﬁcients amounts to solving a high-dimensional quadratic minimization problem with linear inequality constraints.
- Unfortunately, they are impractical for high-dimensional problems because the number of product terms is prohibitive.
- The ﬁrst module, called the feature extractor, transforms the input patterns so that they can be represented by low-dimensional vectors or short strings of symbols that: 1) can be easily matched or compared and 2) are relatively invariant with respect to transformations and distortions of the input patterns that do not change their nature.

# Method Summary
- The literature abounds with recommendations [118] for classical second-order methods such as the Gauss–Newton or Levenberg–Marquardt algorithms for quasi-Newton methods such as Broyden–Fletcher–Goldfarb–Shanno, limited-storage Broyden–Fletcher–Goldfarb–Shanno, or for various versions of the conjugate gradients method.
- Our update algorithm is dubbed the stochastic diagonal Levenberg–Marquardt method where an individual learning rate (step size) is computed for each parameter (weight) before each pass through the training set [20], [34], [121].
- First, the availability of low-cost machines with fast arithmetic units allows for reliance on more brute-force “numerical” methods than on algorithmic reﬁnements.
- The bprop method is the basis of the back-propagation algorithm for generic GT’s.
- In the most common instance of it, is updated on the basis of a single sample (3) With this procedure the parameter vector ﬂuctuates around an average trajectory, but usually it converges considerably faster than regular gradient descent and second-order methods on large training sets with redundant samples (such as those encountered in speech or character recognition).
- Proceedings of the IEEE, 1998, 86 (11), pp.2278-2324. ￿10.1109/5.726791￿. ￿hal03926082￿ Gradient-Based Learning Applied to Document Recognition YANN LECUN, MEMBER, IEEE, L´ EON BOTTOU, YOSHUA BENGIO, AND PATRICK HAFFNER Multilayer neural networks trained with the back-propagation algorithm constitute the best example of a successful gradientbased learning technique.
- Error rate on the test set (%) for various classiﬁcation methods. [deslant] indicates that the classiﬁer was trained and tested on the deslanted version of the database. [dist] indicates that the training set was augmented with artiﬁcially distorted examples. [16 /216] indicates that the system used the 16 /216 pixel images.

# When To Use / Not Use
- Use when:
  - The Lagrange formalism used in the control theory literature provides perhaps the best rigorous method for deriving back propagation [20] and for deriving generalizations of back propagation to recurrent networks [21] and networks of heterogeneous modules [22].
  - Proceedings of the IEEE, 1998, 86 (11), pp.2278-2324. ￿10.1109/5.726791￿. ￿hal03926082￿ Gradient-Based Learning Applied to Document Recognition YANN LECUN, MEMBER, IEEE, L´ EON BOTTOU, YOSHUA BENGIO, AND PATRICK HAFFNER Multilayer neural networks trained with the back-propagation algorithm constitute the best example of a successful gradientbased learning technique.
- Avoid when:
  - The best NN’s, called convolutional networks, are designed to learn to extract relevant features directly from pixel images (see Section II).
  - This algorithm is particularly useful for sharedweight networks because the weight sharing creates ill conditioning of the error surface.
- Failure modes:
  - Saturation of the sigmoids must be avoided because it is known to lead to slow convergence and ill-conditioning of the loss function.

# Metrics Mentioned
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- The parameter prevents the step size from becoming too 42 large when the second derivative is small, very much like the “model-trust” methods, and the Levenberg–Marquardt methods in nonlinear optimization [8].
- This optimization operates on all the parameters in the system, most notably the network weights and the RBF centers.
- In the most common instance of it, is updated on the basis of a single sample (3) With this procedure the parameter vector ﬂuctuates around an average trajectory, but usually it converges considerably faster than regular gradient descent and second-order methods on large training sets with redundant samples (such as those encountered in speech or character recognition).
- For example, let us consider a system built as a cascade of modules, each of which implements a function where is a vector representing the output of the module, is the vector of tunable parameters in the module (a subset of and is the module’s input vector (as well as the previous module’s output vector).
- With classical HMM’s with ﬁxed preprocessing, this problem does not occur because the parameters of the emission and transition probability models are forced to satisfy certain probabilistic constraints: the sum or the integral of the probabilities of a random variable over its possible values must be one.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-053-C1 | stance: support | summary: If we consider an image as a point in a high-dimensional pixel space (where the dimensionality equals the number of pixels), then an evolving distortion of a character traces out a curve in pixel space. | evidence_ids: PENDING-REF-053-E1, PENDING-REF-053-E2
- CLAIM-PENDING-REF-053-C2 | stance: support | summary: The literature abounds with recommendations [118] for classical second-order methods such as the Gauss–Newton or Levenberg–Marquardt algorithms for quasi-Newton methods such as Broyden–Fletcher–Goldfarb–Shanno, limited-storage Broyden–Fletcher–Goldfarb–Shanno, or for various versions of the conjugate gradients method. | evidence_ids: PENDING-REF-053-E3, PENDING-REF-053-E4
- CLAIM-PENDING-REF-053-C3 | stance: support | summary: The parameter prevents the step size from becoming too 42 large when the second derivative is small, very much like the “model-trust” methods, and the Levenberg–Marquardt methods in nonlinear optimization [8]. | evidence_ids: PENDING-REF-053-E5, PENDING-REF-053-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 4 | relevance: high | note: contains initialization sensitivity or control-policy evidence

# Evidence
- PENDING-REF-053-E1 | page: 15, section: extracted, quote: "If we consider an image as a point in a high-dimensional pixel space (where the dimensionality equals the number of pixels), then an evolving distortion of a character traces out a curve in pixel space."
- PENDING-REF-053-E2 | page: 15, section: extracted, quote: "Finding the support vectors and the coefﬁcients amounts to solving a high-dimensional quadratic minimization problem with linear inequality constraints."
- PENDING-REF-053-E3 | page: 15, section: extracted, quote: "Unfortunately, they are impractical for high-dimensional problems because the number of product terms is prohibitive."
- PENDING-REF-053-E4 | page: 3, section: extracted, quote: "The ﬁrst module, called the feature extractor, transforms the input patterns so that they can be represented by low-dimensional vectors or short strings of symbols that: 1) can be easily matched or compared and 2) are relatively invariant with respect to transformations and distortions of the input patterns that do not change their nature."
- PENDING-REF-053-E5 | page: 25, section: extracted, quote: "The literature abounds with recommendations [118] for classical second-order methods such as the Gauss–Newton or Levenberg–Marquardt algorithms for quasi-Newton methods such as Broyden–Fletcher–Goldfarb–Shanno, limited-storage Broyden–Fletcher–Goldfarb–Shanno, or for various versions of the conjugate gradients method."
- PENDING-REF-053-E6 | page: 25, section: extracted, quote: "Our update algorithm is dubbed the stochastic diagonal Levenberg–Marquardt method where an individual learning rate (step size) is computed for each parameter (weight) before each pass through the training set [20], [34], [121]."
- PENDING-REF-053-E7 | page: 3, section: extracted, quote: "First, the availability of low-cost machines with fast arithmetic units allows for reliance on more brute-force “numerical” methods than on algorithmic reﬁnements."
- PENDING-REF-053-E8 | page: 17, section: extracted, quote: "The bprop method is the basis of the back-propagation algorithm for generic GT’s."
