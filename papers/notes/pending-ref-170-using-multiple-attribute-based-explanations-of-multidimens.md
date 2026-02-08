---
id: paper-2021-pending-ref-170
title: "Using multiple attribute-based explanations of multidimensional projections to explore high-dimensional data"
authors: "Zonglin Tian, Xiaorui Zhai, Daan van Driel, Gijs van Steenpaal, Mateus Espadoto, and Alexandru Telea"
venue: "Frontiers in Systems Neuroscience"
year: 2021
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-170-2021-using-multiple-attribute-based-explanations-of-multidimensional-projections-to-explor.pdf
seed_note_id: "paper-2025-jeon-reliable-va-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- This novel visualization of fMRI response-pattern information combines (A) a multidimensional-scaling arrangement of activity-pattern similarity (as introduced to fMRI by Edelman et al., 1998), (B) a novel rubberband-graph depiction of inevitable distortions, and (C) the results of statistical tests of a patterninformation analysis (for details on the test, see Kriegeskorte et al., 2007).
- A major problem in relating such models to brain-activity data is the spatial correspondency problem: Which single-cell recording or functional magnetic resonance imaging (fMRI) voxel corresponds to which unit of the computational model?
- Naively: The representation is a replication of the object, i.e., identical with it. (Problem: A chair does not ﬁ t into the human skull.) More reasonably, we may interpret ﬁ rst-order isomorphism as a mere similarity of some sort.
- We assume (1) that the activity-patterns are high-dimensional (hundreds or thousands of values in each activity pattern), and (2) that the activity pattern noise is additive, independent of the activity patterns, and isotropic.

# Method Summary
- Popular techniques include MDS ( Kruskal and Wish, 1978; Shepard, 1980; T orgerson, 1958) and clustering algorithms (e.g., Johnson, 1967; von Luxburg, 2007), as well as nonlinear manifold-learning techniques such as isomap (T enenbaum et al., 2000) and locally linear embedding (Roweis and Saul, 2000 ).
- The event sequence was optimized for estimation of the contrasts between the responses to the four original images by a method based on a genetic algorithm ( Wager and Nichols, 2003).
- They suggest that this approach could be used as a general method for comparing representations and discuss the philosophical implications.
- One example of such a design is the 96-object-image experiment we presented to demonstrate the approach.
- Building on a rich psychological and mathematical literature on similarity analysis, we propose a new experimental and data-analytical framework called representational similarity analysis (RSA), in which multi-channel measures of neural activity are quantitatively related to each other and to computational theory and behavior by comparing RDMs.
- STEP 6: VISUALIZING THE SIMILARITY STRUCTURE OF REPRESENTATIONAL DISSIMILARITY MATRICES BY MDS MDS provides a general method for arranging entities in a lowdimensional space (e.g., the 2D of a ﬁ gure on paper), such that their distances reﬂ ect their similarities: Similar entities will be placed together, dissimilar entities apart.
- We discuss the broad potential of RSA, including novel approaches to experimental design, and argue that these ideas, which have deep roots in psychology and neuroscience, will allow the integrated quantitative analysis of data from all three branches, thus contributing to a more uniﬁ ed systems neuroscience.

# When To Use / Not Use
- Use when:
  - Early visual orientation information is likely to be attenuated in fMRI data because of its ﬁ ne-scale spatial organization and pooling of columns of all orientation-preferences in each fMRI voxel. • Among the complex computational models, the V1 model ﬁ ts the EVC data best, but only the “smoothed” version, where we simulated local pooling of orientation-speciﬁ c responses in fMRI voxels.
  - The absolute activation difference is sensitive only to the overall level of activation and has been included only because regional-average activation is conventionally targeted in fMRI analysis.
- Avoid when:
  - Conventionally, different subjects in an fMRI experiment are related by transforming the data into a common 6Note that Kay et al. (2008) used stimuli of about 20 ° visual angle (in contrast to the 2.9° stimuli used here) thus driving a more extended retinotopic representation, which may provide more power for detecting the subtler orientation information present in the fMRI signals.
  - Meaningful statistical summaries In order to learn from the massive amounts of brain-activity data we can acquire today with techniques including fMRI as well as scalp and invasive multi-channel electrophysiological techniques and voltage-sensitive dye imaging, we need meaningful statistical summaries that relate a complex data set to systems-level theory.
- Failure modes:
  - A MOTIVATION FOR THE USE OF RANK-CORRELATION DISTANCE IN COMPARING REPRESENTATIONAL DISSIMILARITY MATRICES Given the nature of the computational and conceptual models and the noise affecting the brain dissimilarity matrices, we cannot in general rely on a direct match of the dissimilarity magnitudes between models and regions.

# Metrics Mentioned
- `stress`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- In order to estimate the variability of each model deviation expected if a similar experiment were to be performed with different stimuli (from the same population of stimuli), we computed each model deviation 100 times over for bootstrap resamplings of the condition set (i.e., 96 conditions chosen with replacement from the original set of 96 on each iteration) 4.
- The pulse-sequence parameters were as follows: in-plane resolution: 2 × 2 mm 2, slice thickness: 2 mm (no gap), slice acquisition order: interleaved, ﬁ eld of view (FoV): 256 × 256 mm2, acquisition matrix: 128 × 128, TR: 1.5 s, time to echo (TE): 32 ms, ﬂ ip angle (FA): 75 °.
- For each run, the design matrix included these stimulus predictors along with six headmotion-parameter time courses, a linear-trend predictor, a 6-predictor Fourier basis for nonlinear trends (sines and cosines of up to three cycles per run) and a confound-mean predictor.
- The Levenberg–Marquardt algorithm was used to determine translation and rotation parameters (six parameters) that minimize the sum of squares of the voxelwise intensity differences between each volume and the ﬁ rst volume of the ﬁ rst run of each session.
- Consider for example the 96-image experiment we discuss, where the matrix has (96 2 − 96)/2 = 4,560 parameters. (B) This panel illustrates in greater detail what different representations can be related via the quantitative interface provided by the RDM.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-170-C1 | stance: support | summary: This novel visualization of fMRI response-pattern information combines (A) a multidimensional-scaling arrangement of activity-pattern similarity (as introduced to fMRI by Edelman et al., 1998), (B) a novel rubberband-graph depiction of inevitable distortions, and (C) the results of statistical tests of a patterninformation analysis (for details on the test, see Kriegeskorte et al., 2007). | evidence_ids: PENDING-REF-170-E1, PENDING-REF-170-E2
- CLAIM-PENDING-REF-170-C2 | stance: support | summary: Popular techniques include MDS ( Kruskal and Wish, 1978; Shepard, 1980; T orgerson, 1958) and clustering algorithms (e.g., Johnson, 1967; von Luxburg, 2007), as well as nonlinear manifold-learning techniques such as isomap (T enenbaum et al., 2000) and locally linear embedding (Roweis and Saul, 2000 ). | evidence_ids: PENDING-REF-170-E3, PENDING-REF-170-E4
- CLAIM-PENDING-REF-170-C3 | stance: support | summary: In order to estimate the variability of each model deviation expected if a similar experiment were to be performed with different stimuli (from the same population of stimuli), we computed each model deviation 100 times over for bootstrap resamplings of the condition set (i.e., 96 conditions chosen with replacement from the original set of 96 on each iteration) 4. | evidence_ids: PENDING-REF-170-E5, PENDING-REF-170-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-REF-170-E1 | page: 2, section: extracted, quote: "This novel visualization of fMRI response-pattern information combines (A) a multidimensional-scaling arrangement of activity-pattern similarity (as introduced to fMRI by Edelman et al., 1998), (B) a novel rubberband-graph depiction of inevitable distortions, and (C) the results of statistical tests of a patterninformation analysis (for details on the test, see Kriegeskorte et al., 2007)."
- PENDING-REF-170-E2 | page: 1, section: extracted, quote: "A major problem in relating such models to brain-activity data is the spatial correspondency problem: Which single-cell recording or functional magnetic resonance imaging (fMRI) voxel corresponds to which unit of the computational model?"
- PENDING-REF-170-E3 | page: 4, section: extracted, quote: "Naively: The representation is a replication of the object, i.e., identical with it. (Problem: A chair does not ﬁ t into the human skull.) More reasonably, we may interpret ﬁ rst-order isomorphism as a mere similarity of some sort."
- PENDING-REF-170-E4 | page: 23, section: extracted, quote: "We assume (1) that the activity-patterns are high-dimensional (hundreds or thousands of values in each activity pattern), and (2) that the activity pattern noise is additive, independent of the activity patterns, and isotropic."
- PENDING-REF-170-E5 | page: 23, section: extracted, quote: "Popular techniques include MDS ( Kruskal and Wish, 1978; Shepard, 1980; T orgerson, 1958) and clustering algorithms (e.g., Johnson, 1967; von Luxburg, 2007), as well as nonlinear manifold-learning techniques such as isomap (T enenbaum et al., 2000) and locally linear embedding (Roweis and Saul, 2000 )."
- PENDING-REF-170-E6 | page: 24, section: extracted, quote: "The event sequence was optimized for estimation of the contrasts between the responses to the four original images by a method based on a genetic algorithm ( Wager and Nichols, 2003)."
- PENDING-REF-170-E7 | page: 4, section: extracted, quote: "They suggest that this approach could be used as a general method for comparing representations and discuss the philosophical implications."
- PENDING-REF-170-E8 | page: 17, section: extracted, quote: "One example of such a design is the 96-object-image experiment we presented to demonstrate the approach."
