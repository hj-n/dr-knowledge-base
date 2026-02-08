---
id: paper-2012-pending-ref-045
title: "A behavioral investigation of dimensionality reduction"
authors: "J. Lewis, L. van der Maaten, and V. de Sa"
venue: "UNKNOWN"
year: 2012
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-045-2012-a-behavioral-investigation-of-dimensionality-reduction.pdf
seed_note_id: "paper-2015-perception-based-projection-evaluation"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- As described in the introduction, one of the key problems of dimensionality reduction is that it lacks a widely agreed upon evaluation measure (Venna et al., 2010).
- Such information could be useful for determining whether humans are appropriate for an evaluation task with a known structure (e.g. if they naturally prefer embedding characteristics appropriate to the structure), or for developing techniques that are tailored towards producing results that humans will ﬁnd helpful (e.g. algorithms that selectively emphasize informative data structure).
- Also, there is a lot of debate within the ﬁeld on what a good objective for dimensionality reduction is: for instance, a latent variable model approach to dimensionality reduction suggests one should focus on preserving global data structure (Lawrence, 2005), whereas a manifold learning viewpoint deems preservation of local data structure more important (Roweis & Saul, 2000).
- Though there is no standard signiﬁcance test for Fleiss’ kappa, based on the Landis and Koch scale (Landis & Koch, 1977), experts exhibited fair to moderate agreement, while both groups of novices 4Note that if the distribution of points in the embedding is Gaussian, the point distribution in each of the random projections has to be Gaussian as well.

# Method Summary
- Such information could be useful for determining whether humans are appropriate for an evaluation task with a known structure (e.g. if they naturally prefer embedding characteristics appropriate to the structure), or for developing techniques that are tailored towards producing results that humans will ﬁnd helpful (e.g. algorithms that selectively emphasize informative data structure).
- Also, there is a lot of debate within the ﬁeld on what a good objective for dimensionality reduction is: for instance, a latent variable model approach to dimensionality reduction suggests one should focus on preserving global data structure (Lawrence, 2005), whereas a manifold learning viewpoint deems preservation of local data structure more important (Roweis & Saul, 2000).
- Though there is no standard signiﬁcance test for Fleiss’ kappa, based on the Landis and Koch scale (Landis & Koch, 1977), experts exhibited fair to moderate agreement, while both groups of novices 4Note that if the distribution of points in the embedding is Gaussian, the point distribution in each of the random projections has to be Gaussian as well.
- The ﬁrst presents subjects with a selection of embeddings derived from nine distinct dimensionality reduction algorithms; the second uses embeddings from a single algorithm with several different parameter settings for a more controlled comparison between “clustered” and “gradual” embeddings.
- If one is interested in applying a dimensionality reduction algorithm to visualize a dataset, is this a valid way to select from the wide range of techniques?1 To answer this question, we need to evaluate whether humans are good at evaluating embeddings.
- The ﬁrst experiment uses stimuli generated from the dimensionality reduction algorithms described above to determine whether humans are consistent in their evaluations when the embeddings are fairly distinct (the ﬁrst aim of the study).
- Isomap constructs an embedding by performing classical scaling on a geodesic distance matrix that is obtained by running a shortest-path algorithm on the nearest neighbor graph of the data (Tenenbaum et al., 2000).

# When To Use / Not Use
- Use when:
  - Do the best you can to choose useful plots based on whatever criteria you deem appropriate.
  - Such information could be useful for determining whether humans are appropriate for an evaluation task with a known structure (e.g. if they naturally prefer embedding characteristics appropriate to the structure), or for developing techniques that are tailored towards producing results that humans will ﬁnd helpful (e.g. algorithms that selectively emphasize informative data structure).
- Avoid when:
  - After describing what a scatter plot is and emphasizing that each set of nine plots is a different perspective on the same dataset, we gave subjects the following instructions: For each trial, please examine all the scatter plots and choose the two that you ﬁnd most useful and the one that you ﬁnd least useful.
  - The ﬁrst presents subjects with a selection of embeddings derived from nine distinct dimensionality reduction algorithms; the second uses embeddings from a single algorithm with several different parameter settings for a more controlled comparison between “clustered” and “gradual” embeddings.
- Failure modes:
  - To ensure that dimensionality reduction techniques are applied wisely, authors should strive to explicate the dataset characteristics that favor their algorithms (e.g., tSNE is useful if the data is expected to have cluster structure, Isomap if the data lie on a convex manifold).

# Metrics Mentioned
- `trustworthiness`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- The ﬁrst presents subjects with a selection of embeddings derived from nine distinct dimensionality reduction algorithms; the second uses embeddings from a single algorithm with several different parameter settings for a more controlled comparison between “clustered” and “gradual” embeddings.
- We ran each technique for a reasonable range of parameter settings, and we selected the embedding that was best in terms of the trustworthiness 2 (Venna & Kaski, 2006) for presentation to the subjects.
- The second experiment uses stimuli that are all generated by tSNE, but with different parameter settings that affect how clustered the resulting embedding appears.
- Parameter values are in rows; datasets are in columns. exhibited poor agreement.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-045-C1 | stance: support | summary: As described in the introduction, one of the key problems of dimensionality reduction is that it lacks a widely agreed upon evaluation measure (Venna et al., 2010). | evidence_ids: PENDING-REF-045-E1, PENDING-REF-045-E2
- CLAIM-PENDING-REF-045-C2 | stance: support | summary: Such information could be useful for determining whether humans are appropriate for an evaluation task with a known structure (e.g. if they naturally prefer embedding characteristics appropriate to the structure), or for developing techniques that are tailored towards producing results that humans will ﬁnd helpful (e.g. algorithms that selectively emphasize informative data structure). | evidence_ids: PENDING-REF-045-E3, PENDING-REF-045-E4
- CLAIM-PENDING-REF-045-C3 | stance: support | summary: The ﬁrst presents subjects with a selection of embeddings derived from nine distinct dimensionality reduction algorithms; the second uses embeddings from a single algorithm with several different parameter settings for a more controlled comparison between “clustered” and “gradual” embeddings. | evidence_ids: PENDING-REF-045-E5, PENDING-REF-045-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-REF-045-E1 | page: 3, section: extracted, quote: "As described in the introduction, one of the key problems of dimensionality reduction is that it lacks a widely agreed upon evaluation measure (Venna et al., 2010)."
- PENDING-REF-045-E2 | page: 2, section: extracted, quote: "Such information could be useful for determining whether humans are appropriate for an evaluation task with a known structure (e.g. if they naturally prefer embedding characteristics appropriate to the structure), or for developing techniques that are tailored towards producing results that humans will ﬁnd helpful (e.g. algorithms that selectively emphasize informative data structure)."
- PENDING-REF-045-E3 | page: 3, section: extracted, quote: "Also, there is a lot of debate within the ﬁeld on what a good objective for dimensionality reduction is: for instance, a latent variable model approach to dimensionality reduction suggests one should focus on preserving global data structure (Lawrence, 2005), whereas a manifold learning viewpoint deems preservation of local data structure more important (Roweis & Saul, 2000)."
- PENDING-REF-045-E4 | page: 5, section: extracted, quote: "Though there is no standard signiﬁcance test for Fleiss’ kappa, based on the Landis and Koch scale (Landis & Koch, 1977), experts exhibited fair to moderate agreement, while both groups of novices 4Note that if the distribution of points in the embedding is Gaussian, the point distribution in each of the random projections has to be Gaussian as well."
- PENDING-REF-045-E5 | page: 2, section: extracted, quote: "The ﬁrst presents subjects with a selection of embeddings derived from nine distinct dimensionality reduction algorithms; the second uses embeddings from a single algorithm with several different parameter settings for a more controlled comparison between “clustered” and “gradual” embeddings."
- PENDING-REF-045-E6 | page: 2, section: extracted, quote: "If one is interested in applying a dimensionality reduction algorithm to visualize a dataset, is this a valid way to select from the wide range of techniques?1 To answer this question, we need to evaluate whether humans are good at evaluating embeddings."
- PENDING-REF-045-E7 | page: 3, section: extracted, quote: "The ﬁrst experiment uses stimuli generated from the dimensionality reduction algorithms described above to determine whether humans are consistent in their evaluations when the embeddings are fairly distinct (the ﬁrst aim of the study)."
- PENDING-REF-045-E8 | page: 3, section: extracted, quote: "Isomap constructs an embedding by performing classical scaling on a geodesic distance matrix that is obtained by running a shortest-path algorithm on the nearest neighbor graph of the data (Tenenbaum et al., 2000)."
