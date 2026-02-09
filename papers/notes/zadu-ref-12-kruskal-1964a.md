---
id: paper-1964-zadu-ref-12
title: "Multidimensional scaling by optimizing goodness of fit to a nonmetric hypothesis"
authors: "PSYCHOMETRIKA--VOL. ~, NO."
venue: "Psychometrika"
year: 1964
tags: [dr, zadu-table1-reference, stress]
source_pdf: papers/raw/zadu-table1-references/kruskal_1964a.pdf
evidence_level: medium
updated_at: 2026-02-08
---
# Problem
- The problem of minimizing a function of many variables is a standard problem in numerical analysis, and to solve it we adopt a widely used iterative technique known as the "method of gradients" or the "method of steepest descent." Finally, at the practical level, we give in a companion paper [12] all the important details necessary to perform this iterative technique successfully.
- (The literature reflects considerable confusion between the main problem of definition and the subsidiary problem of compu- tation.) In a companion paper [12] we present a practical method of computa- tion, so that our technique should be usable on many automatic computers.
- We view multidimensional scaling as a problem of statistical fit- ting--the dissimilarities are given, and we wish to find the configuration whose distances fit them best. "To fit them best" implies both a goal and a way of measuring how close we are to that goal.
- Multidimensional scaling is the problem of representing n objects: geometrically by n points, so that the interpoint distances correspond in some sense to experimental dissimilarities between objects.
- To create the 105 dissimilarities we applied a monotone distortion to the interpoint distances, and then added independent random normal deviates to the distorted distances.

# Method Summary
- The problem of minimizing a function of many variables is a standard problem in numerical analysis, and to solve it we adopt a widely used iterative technique known as the "method of gradients" or the "method of steepest descent." Finally, at the practical level, we give in a companion paper [12] all the important details necessary to perform this iterative technique successfully.
- S(xl , ... , x.) = stress of the fixed configuration xl , --- , x. = min numbe ra ~i i ~ -- ~ satisfying (Mon) We point out that this minimization is accomplished not by varying a trim set of values for the d~;, but rather by a rapid, efficient algorithm which is described in detail in the companion paper [12].
- 250), the methods in use up to the time of his book follow the general two-stage procedure of first using a one-dimen- sional scaling technique to convert the dissimilarities or similarities into distances, and then finding points whose interpoint distances have approxi- mately these values.
- Due to'the nature of the one-dimensional scaling techniques available, these methods either accept the averaged dissimilarities or some fixed transformation of them as 2 PSYCHOMETRIKA distances or else use the variability of the data as a critical element in forming the distances.
- (The literature reflects considerable confusion between the main problem of definition and the subsidiary problem of compu- tation.) In a companion paper [12] we present a practical method of computa- tion, so that our technique should be usable on many automatic computers.
- The place in which the difference between these two approaches actually takes effect is deep inside the algorithm for finding the d,.
- Our technique of multidimensional scaling is to compute that confi~xlration of points which optimizes the goodness of fit.

# When To Use / Not Use
- Use when:
  - One, which we call the primary approach because it seems preferable, is to say that when ~, = ~,z we do not care which of d, and dk~ is larger nor whether they are equal or not.
  - However, we point out here that while a configuration may be freely rotated when Euclidean distances are being used, it may not be when more general distances are used.
  - The problem of minimizing a function of many variables is a standard problem in numerical analysis, and to solve it we adopt a widely used iterative technique known as the "method of gradients" or the "method of steepest descent." Finally, at the practical level, we give in a companion paper [12] all the important details necessary to perform this iterative technique successfully.
- Avoid when:
  - (In a later section we state a theorem which further clarifies this situation.) Thus his technique avoids all the strong distributional assumptions which are necessary in variability-depend- ent techniques, and also avoids the assumption made by other techniques that dissimilarities and distances are related by some fixed formula.
  - It is special in only two ways: first, in the use of distance axis deviations; second, because of the fact that the fitted curve is chosen not from a "parametric" family of curves, such as polynomials or trigonometric series, but from a "nonparametric" family of curves, namely, all monotone ascending curves.
- Failure modes:
  - 250), the methods in use up to the time of his book follow the general two-stage procedure of first using a one-dimen- sional scaling technique to convert the dissimilarities or similarities into distances, and then finding points whose interpoint distances have approxi- mately these values.
  - Suppose that the measurement procedure is not inherently symmetrical, so that 5;; ~ ~i~ • If we are willing to assume that ~, and ~;~ are measure- ments of the same underlying quantity, and differ only because of statistical fluctuation, then two natural procedures are opei1 to us.

# Metrics Mentioned
- `nh`: label-based neighborhood hit.
- `nd`: neighbor-shape dissimilarity or neighbor distortion.
- `pr`: pairwise-distance correlation behavior.
- `proc`: Procrustes local shape agreement.
- `stress`: stress-based distance distortion.

# Implementation Notes
- Thus S* ~ (d, -- (~,~)2 T* ~ d~, i<i is a measure of goodness of fit which has all the desirable properties of S*, and in addition is invariant under change of scale, that is, uniform stretching or shrinking.
- An obvious way to cure this defect in the raw stress is to divide it by a scaling factor, that is, a quantity which has the same quad- ratic dependence on the scale of the configuration that raw stress does.
- 26 PSYCHOMETRIKA It is interesting to read Bartholomew [4], who is concerned with testing whether parameters are equal, subject to the assumption that they are linearly ordered.
- 37.) His maximum-likelihood estimate of these parameters bears essentially the same relationship to the observations that our d, bear to d, .
- Keep preprocessing, initialization policy, and random-seed protocol fixed when comparing methods.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PAPER1964ZADUREF12-C1 | stance: support | summary: The problem of minimizing a function of many variables is a standard problem in numerical analysis, and to solve it we adopt a widely used iterative technique known as the "method of gradients" or the "method of steepest descent." Finally, at the practical level, we give in a companion paper [12] all the important details necessary to perform this iterative technique successfully. | evidence_ids: PAPER1964ZADUREF12-E1, PAPER1964ZADUREF12-E2
- CLAIM-PAPER1964ZADUREF12-C2 | stance: support | summary: The problem of minimizing a function of many variables is a standard problem in numerical analysis, and to solve it we adopt a widely used iterative technique known as the "method of gradients" or the "method of steepest descent." Finally, at the practical level, we give in a companion paper [12] all the important details necessary to perform this iterative technique successfully. | evidence_ids: PAPER1964ZADUREF12-E3, PAPER1964ZADUREF12-E4
- CLAIM-PAPER1964ZADUREF12-C3 | stance: support | summary: Thus S* ~ (d, -- (~,~)2 T* ~ d~, i<i is a measure of goodness of fit which has all the desirable properties of S*, and in addition is invariant under change of scale, that is, uniform stretching or shrinking. | evidence_ids: PAPER1964ZADUREF12-E5, PAPER1964ZADUREF12-E6
- CLAIM-METRIC-STRESS-SOURCE-12 | stance: support | summary: This source includes evidence relevant to `stress` in dimensionality-reduction reliability evaluation. | evidence_ids: PAPER1964ZADUREF12-E1, PAPER1964ZADUREF12-E2

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports task clarification before model selection
- step: 2 | relevance: medium | note: adds constraints for preprocessing and data-audit checks
- step: 3 | relevance: high | note: directly informs task-aligned technique/metric selection
- step: 7 | relevance: high | note: supports visualization interpretation and user explanation

# Evidence
- PAPER1964ZADUREF12-E1 | page: 10, section: extracted, quote: "The problem of minimizing a function of many variables is a standard problem in numerical analysis, and to solve it we adopt a widely used iterative technique known as the 'method of gradients' or the 'method of steepest descent.' Finally, at the practical level, we give in a companion paper [12] all the important details necessary to perform this iterative technique successfully."
- PAPER1964ZADUREF12-E2 | page: 3, section: extracted, quote: "(The literature reflects considerable confusion between the main problem of definition and the subsidiary problem of compu- tation.) In a companion paper [12] we present a practical method of computa- tion, so that our technique should be usable on many automatic computers."
- PAPER1964ZADUREF12-E3 | page: 2, section: extracted, quote: "We view multidimensional scaling as a problem of statistical fit- ting--the dissimilarities are given, and we wish to find the configuration whose distances fit them best. 'To fit them best' implies both a goal and a way of measuring how close we are to that goal."
- PAPER1964ZADUREF12-E4 | page: 1, section: extracted, quote: "Multidimensional scaling is the problem of representing n objects: geometrically by n points, so that the interpoint distances correspond in some sense to experimental dissimilarities between objects."
- PAPER1964ZADUREF12-E5 | page: 10, section: extracted, quote: "To create the 105 dissimilarities we applied a monotone distortion to the interpoint distances, and then added independent random normal deviates to the distorted distances."
- PAPER1964ZADUREF12-E6 | page: 1, section: extracted, quote: "The problem of multidimensional scaling, broadly stated, is to find n points whose interpoint distances match in some sense the experimental dissimilarities of n objects."
- PAPER1964ZADUREF12-E7 | page: 9, section: extracted, quote: "S(xl , ... , x.) = stress of the fixed configuration xl , --- , x. = min numbe ra ~i i ~ -- ~ satisfying (Mon) We point out that this minimization is accomplished not by varying a trim set of values for the d~;, but rather by a rapid, efficient algorithm which is described in detail in the companion paper [12]."
- PAPER1964ZADUREF12-E8 | page: 1, section: extracted, quote: "250), the methods in use up to the time of his book follow the general two-stage procedure of first using a one-dimen- sional scaling technique to convert the dissimilarities or similarities into distances, and then finding points whose interpoint distances have approxi- mately these values."
- PAPER1964ZADUREF12-E9 | page: 1, section: extracted, quote: "Due to'the nature of the one-dimensional scaling techniques available, these methods either accept the averaged dissimilarities or some fixed transformation of them as 2 PSYCHOMETRIKA distances or else use the variability of the data as a critical element in forming the distances."
- PAPER1964ZADUREF12-E10 | page: 22, section: extracted, quote: "The place in which the difference between these two approaches actually takes effect is deep inside the algorithm for finding the d,."
- PAPER1964ZADUREF12-E11 | page: 1, section: extracted, quote: "Our technique of multidimensional scaling is to compute that confi~xlration of points which optimizes the goodness of fit."
- PAPER1964ZADUREF12-E12 | page: 26, section: extracted, quote: "The desired configuration is the one with smallest stress, which we find by methods of numerical analysis."
- PAPER1964ZADUREF12-E13 | page: 2, section: extracted, quote: "First, he introduced as the central feature the goal of obtaining a monotone relationship between the experimental dissimilarities or similarities and the distances in the configuration."
- PAPER1964ZADUREF12-E14 | page: 3, section: extracted, quote: "(The literature reflects considerable confusion between the main problem of definition and the subsidiary problem of compu- tation.) In a companion paper [12] we present a practical method of computa- tion, so that our technique should be usable on many automatic computers."
