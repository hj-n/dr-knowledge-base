---
id: paper-2011-pending-ref-126
title: "Quality metrics in highdimensional data visualization: An overview and systematization"
authors: "E. Bertini, A. Tatu, and D. Keim"
venue: "Frontiers in Bioengineering and Biotechnology"
year: 2011
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-126-2011-quality-metrics-in-highdimensional-data-visualization-an-overview-and-systematization.pdf
seed_note_id: "paper-2019-mdp-visual-analytics-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- Conventional ML In this section, we begin reporting on the articles in which the authors described the application of certain conventiona l ML techniques to an orthopedic problem, aimed at developing the models belonging to the following families: decision tr ees, random forests, nearest neighbors, linear regression and s upport vector machines (and others).
- Nearest Neighbors (NN) In Ashinsky et al. (2015) and Ashinsky et al. (2017) , a weighted neighbor distance method was used with a compound hierarchy of algorithms ﬁrst introduced in Shamir et al. (2008) representing morphology (a technique abbreviated with the acronym WNDCHRM) and applied to the problem of OA detection in MRIs of articular cartilage scans.
- The study of Dam et al. (2015) used a freely available knee image data set resulting from a challenge initiative ca lled “Segmentation of Knee Images 2010” (SKI10), MRIs from the OA initiative (OAI), and MRIs from the Center for Clinical and Basic Research (CCBR) to perform automatic bone and cartilage segmentation from MRIs for OA detection.
- Rather, in this paper, we shed some light on the extent to which computational techniques and methods that can be put under the above-mentioned evocative rubric of “Machine Learning” (ML) have been used thus far and r eported in the specialist literature with regard to musculoskeletal problems and related health co nditions.

# Method Summary
- Nearest Neighbors (NN) In Ashinsky et al. (2015) and Ashinsky et al. (2017) , a weighted neighbor distance method was used with a compound hierarchy of algorithms ﬁrst introduced in Shamir et al. (2008) representing morphology (a technique abbreviated with the acronym WNDCHRM) and applied to the problem of OA detection in MRIs of articular cartilage scans.
- We describe the papers that have been divided according to the ML approach for the sake of reference, beginning from the numerous model families that can be considered under the rubric of conventional (or traditional) ML, and then conclude with t he most recent ones that employ deep learning methods (usually a multi-layered artiﬁcial neural network).
- By searching both in the Scopus and Medline databases, we ret rieved, screened and analyzed the content of 70 journal articles, and coded these resources following an iterative method within a Grounded Theory approach.
- With regard to the techniques surveyed, we are aware that in the past, certain techniques that are nowadays considered to be “ML ” (and denoted as such in the specialist articles) once were not denoted as such (but rather considered “statistical learning, ” or merely statistical methods wit hout a speciﬁc common denotation, as mentioned in section 2).
- Rather, in this paper, we shed some light on the extent to which computational techniques and methods that can be put under the above-mentioned evocative rubric of “Machine Learning” (ML) have been used thus far and r eported in the specialist literature with regard to musculoskeletal problems and related health co nditions.
- We intend ML as the study of how computer algorithms (i.e., mach ines) can “learn” complex relationships or patterns from empirical data ( Wang and Summers, 2012 ) and, hence, produce (mathematical) models linking an even large number of covari ates to some target variable of interest ( Obermeyer and Emanuel, 2016 ).
- Diﬀerent factors were advocated for this diﬀerence: in the ﬁrs t study, the data set was less generic in describing OA subject s and OARSI score provided an objective measurement; in the last Frontiers in Bioengineering and Biotechnology | www.front iersin.org 5 June 2018 | Volume 6 | Article 75 Cabitza et al.

# When To Use / Not Use
- Use when:
  - A third study Nagarajan et al. (2014) used phase-contrast X-Ray CT images to detect geometric features that best characterized condrocyte structures in OA, healthy patient s ROIs as well as gray-level statistical features from manually annotated ROIs of the same set of images.
  - The extracted features were used to train an LDA classiﬁer able to select the best combination of them for relating the bone structure markers to the prediction of cartilage volume loss.
- Avoid when:
  - We distinguish between pape rs that discuss deep learning models and conventional ML mod els. classiﬁcation task was tested with 16 diﬀerent classiﬁers: L ogistic Regression (both linear and quadratic), Linear Discriminan t Analysis (LDA), Quadratic Discriminant Analysis (QDA), kNearest Neighbors (kNN), Naive Bayes (NB), Neural Networks (NN), Support Vector Machines (SVM), Decision Trees (DT), and Tree Bagging.
  - In this manner, it was possible to detect population subnetworks, in which subgroups of OA patients could be analyzed in their “syndromic spaces.” The TDA was also tested for its capacity to generate hypotheses and for modelin g selective conﬁgurations obtained by ﬁltering out diﬀerent k inds Frontiers in Bioengineering and Biotechnology | www.front iersin.org 6 June 2018 | Volume 6 | Article 75 Cabitza et al.
- Failure modes:
  - The combination of both (11 variables for women and 9 variables for men) aimed at achieving a trade-oﬀ between discriminability powe r (evaluated in terms of ROC) and best calibration of probabilit ies (a technique to retain the output of a discrimination result also as a probability prediction of that result, such that the probability value can be interpreted as belonging to a 95% conﬁdence interval–CI).

# Metrics Mentioned
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- Furthermore, two hyperparameters were selected in the study instead of one in order to regularize the trade-oﬀ between error minimization and margin maximization of both positive and negative examples.
- We did this because we deem it counter-productive in ﬁelds other than computer science (where metaphors are often used as a note of color to sophisticated mathematical models) to associ ate automatic procedures of incremental function optimization, which is what ML is all about, with an anthropomorphic element that can suggest something about the inner functioning of ML-based decision support systems 1.
- This process, far from being confused as learning by something, like a machine, was technically considered a broad family of statistical metho ds by which a discriminative function could improve its detection accuracy over time, by changing some of its parameters so that a cost score (anyhow deﬁned) becomes minimized as well.
- The most informative GRF parameters were computed by summing up the prediction error of the observations that were eliminated along the three paths, so that the ﬁnal outcome of the ensemble could be appropriately averaged by also considering the error-bias.
- The authors collected kinematic data from patients which comprised ground reaction forces parameters (GRF), and extracted features for each of the three paths axes –X, Y , and Z.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-126-C1 | stance: support | summary: Conventional ML In this section, we begin reporting on the articles in which the authors described the application of certain conventiona l ML techniques to an orthopedic problem, aimed at developing the models belonging to the following families: decision tr ees, random forests, nearest neighbors, linear regression and s upport vector machines (and others). | evidence_ids: PENDING-REF-126-E1, PENDING-REF-126-E2
- CLAIM-PENDING-REF-126-C2 | stance: support | summary: Nearest Neighbors (NN) In Ashinsky et al. (2015) and Ashinsky et al. (2017) , a weighted neighbor distance method was used with a compound hierarchy of algorithms ﬁrst introduced in Shamir et al. (2008) representing morphology (a technique abbreviated with the acronym WNDCHRM) and applied to the problem of OA detection in MRIs of articular cartilage scans. | evidence_ids: PENDING-REF-126-E3, PENDING-REF-126-E4
- CLAIM-PENDING-REF-126-C3 | stance: support | summary: Furthermore, two hyperparameters were selected in the study instead of one in order to regularize the trade-oﬀ between error minimization and margin maximization of both positive and negative examples. | evidence_ids: PENDING-REF-126-E5, PENDING-REF-126-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 4 | relevance: high | note: contains initialization sensitivity or control-policy evidence

# Evidence
- PENDING-REF-126-E1 | page: 4, section: extracted, quote: "Conventional ML In this section, we begin reporting on the articles in which the authors described the application of certain conventiona l ML techniques to an orthopedic problem, aimed at developing the models belonging to the following families: decision tr ees, random forests, nearest neighbors, linear regression and s upport vector machines (and others)."
- PENDING-REF-126-E2 | page: 5, section: extracted, quote: "Nearest Neighbors (NN) In Ashinsky et al. (2015) and Ashinsky et al. (2017) , a weighted neighbor distance method was used with a compound hierarchy of algorithms ﬁrst introduced in Shamir et al. (2008) representing morphology (a technique abbreviated with the acronym WNDCHRM) and applied to the problem of OA detection in MRIs of articular cartilage scans."
- PENDING-REF-126-E3 | page: 10, section: extracted, quote: "The study of Dam et al. (2015) used a freely available knee image data set resulting from a challenge initiative ca lled “Segmentation of Knee Images 2010” (SKI10), MRIs from the OA initiative (OAI), and MRIs from the Center for Clinical and Basic Research (CCBR) to perform automatic bone and cartilage segmentation from MRIs for OA detection."
- PENDING-REF-126-E4 | page: 1, section: extracted, quote: "Rather, in this paper, we shed some light on the extent to which computational techniques and methods that can be put under the above-mentioned evocative rubric of “Machine Learning” (ML) have been used thus far and r eported in the specialist literature with regard to musculoskeletal problems and related health co nditions."
- PENDING-REF-126-E5 | page: 3, section: extracted, quote: "We describe the papers that have been divided according to the ML approach for the sake of reference, beginning from the numerous model families that can be considered under the rubric of conventional (or traditional) ML, and then conclude with t he most recent ones that employ deep learning methods (usually a multi-layered artiﬁcial neural network)."
- PENDING-REF-126-E6 | page: 1, section: extracted, quote: "By searching both in the Scopus and Medline databases, we ret rieved, screened and analyzed the content of 70 journal articles, and coded these resources following an iterative method within a Grounded Theory approach."
- PENDING-REF-126-E7 | page: 3, section: extracted, quote: "With regard to the techniques surveyed, we are aware that in the past, certain techniques that are nowadays considered to be “ML ” (and denoted as such in the specialist articles) once were not denoted as such (but rather considered “statistical learning, ” or merely statistical methods wit hout a speciﬁc common denotation, as mentioned in section 2)."
- PENDING-REF-126-E8 | page: 1, section: extracted, quote: "We intend ML as the study of how computer algorithms (i.e., mach ines) can “learn” complex relationships or patterns from empirical data ( Wang and Summers, 2012 ) and, hence, produce (mathematical) models linking an even large number of covari ates to some target variable of interest ( Obermeyer and Emanuel, 2016 )."
