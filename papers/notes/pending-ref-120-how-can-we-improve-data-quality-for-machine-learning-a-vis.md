---
id: paper-2023-pending-ref-120
title: "How Can We Improve Data Quality for Machine Learning? A Visual Analytics System using Data and Process-driven Strategies"
authors: "Hyein Hong, Sangbong Yoo, Yejin Jin, and Yun Jang"
venue: "Systematic Reviews"
year: 2023
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-120-2023-how-can-we-improve-data-quality-for-machine-learning-a-visual-analytics-system-using.pdf
seed_note_id: "paper-2025-stop-misusing-tsne-umap"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- While it is difficult to generalize what number of
- Abstract Background: Synthesis ofmultiplerandomizedcontrolledtrials(RCTs)inasystematicreviewcansummarizethe effectsofindividualoutcomesandprovidenumericalanswersabouttheeffectivenessofinterventions.Filteringof searchesistimeconsuming,andnosinglemethodfulfillstheprincipalrequirementsofspeedwithaccuracy.
- This process has clearly designated steps to identify primary studies and the methods which will be employed to assess their methodological quality, the way in which data will be extracted, and the statistical techniques that will be used in the synthesis and reporting of that data [2].
- A systematic review is a summary of the medical literature that uses explicit methods to systematically search, critically appraise, and synthesize the data on a specific topic.

# Method Summary
- Abstract Background: Synthesis ofmultiplerandomizedcontrolledtrials(RCTs)inasystematicreviewcansummarizethe effectsofindividualoutcomesandprovidenumericalanswersabouttheeffectivenessofinterventions.Filteringof searchesistimeconsuming,andnosinglemethodfulfillstheprincipalrequirementsofspeedwithaccuracy.
- This process has clearly designated steps to identify primary studies and the methods which will be employed to assess their methodological quality, the way in which data will be extracted, and the statistical techniques that will be used in the synthesis and reporting of that data [2].
- A systematic review is a summary of the medical literature that uses explicit methods to systematically search, critically appraise, and synthesize the data on a specific topic.
- Automationofsystematicreviewsisdrivenbyanecessitytoexpeditetheavailabilityofcurrentbestevidencefor policyandclinicaldecision-making.
- WedevelopedRayyan(http://rayyan.qcri.org),afreewebandmobileapp,thathelpsexpeditetheinitialscreeningof abstractsandtitlesusingaprocessofsemi-automationwhileincorporatingahighlevelofusability.Forthebeta testingphase,weusedtwopublishedCochranereviewsinwhichincludedstudieshadbeenselectedmanually.
- Theirsearches,with1030recordsand273records,wereuploadedtoRayyan.DifferentfeaturesofRayyanweretested usingthesetworeviews.WealsoconductedasurveyofRayyan’susersandcollectedfeedbackthroughabuilt-in feature.
- Conclusions: Rayyanisresponsiveandintuitiveinusewithsignificantpotentialtolightentheloadofreviewers.

# When To Use / Not Use
- Use when:
  - WedevelopedRayyan(http://rayyan.qcri.org),afreewebandmobileapp,thathelpsexpeditetheinitialscreeningof abstractsandtitlesusingaprocessofsemi-automationwhileincorporatingahighlevelofusability.Forthebeta testingphase,weusedtwopublishedCochranereviewsinwhichincludedstudieshadbeenselectedmanually.
  - This process has clearly designated steps to identify primary studies and the methods which will be employed to assess their methodological quality, the way in which data will be extracted, and the statistical techniques that will be used in the synthesis and reporting of that data [2].
- Avoid when:
  - Although the initial searches for trials for a systematic review may in some cases identify up to, and possibly extend beyond, 1000 citations, this will depend in part on the level of sensitivity and specificity built into the search strategy used to search the individual databases.
  - Experiments on a set of 15 reviews showed that the prediction embedded in Rayyan can reduce the time for screeningarticles.Inaddition,oursurveyshowedthatour users reported time savings in the order of 40% on average compared to other tools they have been using in the past.
- Failure modes:
  - Rayyan wouldbenefitfromseveralimprovementsincludingabetterhandlingofduplicates,automaticdataextractionfrom fulltext,automaticriskofbiasanalysis,andseamlessintegration with Review Manager (RevMan), the Cochrane software used for preparing and maintaining Cochrane reviews.

# Metrics Mentioned
- No explicit named metric was extracted from this source; combine this source with complementary DR quality checks in workflow Step 3.

# Implementation Notes
- This process has clearly designated steps to identify primary studies and the methods which will be employed to assess their methodological quality, the way in which data will be extracted, and the statistical techniques that will be used in the synthesis and reporting of that data [2].
- A systematic review is a summary of the medical literature that uses explicit methods to systematically search, critically appraise, and synthesize the data on a specific topic.
- Automationofsystematicreviewsisdrivenbyanecessitytoexpeditetheavailabilityofcurrentbestevidencefor policyandclinicaldecision-making.
- WedevelopedRayyan(http://rayyan.qcri.org),afreewebandmobileapp,thathelpsexpeditetheinitialscreeningof abstractsandtitlesusingaprocessofsemi-automationwhileincorporatingahighlevelofusability.Forthebeta testingphase,weusedtwopublishedCochranereviewsinwhichincludedstudieshadbeenselectedmanually.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-120-C1 | stance: support | summary: While it is difficult to generalize what number of | evidence_ids: PENDING-REF-120-E1, PENDING-REF-120-E2
- CLAIM-PENDING-REF-120-C2 | stance: support | summary: Abstract Background: Synthesis ofmultiplerandomizedcontrolledtrials(RCTs)inasystematicreviewcansummarizethe effectsofindividualoutcomesandprovidenumericalanswersabouttheeffectivenessofinterventions.Filteringof searchesistimeconsuming,andnosinglemethodfulfillstheprincipalrequirementsofspeedwithaccuracy. | evidence_ids: PENDING-REF-120-E3, PENDING-REF-120-E4
- CLAIM-PENDING-REF-120-C3 | stance: support | summary: This process has clearly designated steps to identify primary studies and the methods which will be employed to assess their methodological quality, the way in which data will be extracted, and the statistical techniques that will be used in the synthesis and reporting of that data [2]. | evidence_ids: PENDING-REF-120-E5, PENDING-REF-120-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 4 | relevance: high | note: contains initialization sensitivity or control-policy evidence

# Evidence
- PENDING-REF-120-E1 | page: 2, section: extracted, quote: "While it is difficult to generalize what number of"
- PENDING-REF-120-E2 | page: 1, section: extracted, quote: "Abstract Background: Synthesis ofmultiplerandomizedcontrolledtrials(RCTs)inasystematicreviewcansummarizethe effectsofindividualoutcomesandprovidenumericalanswersabouttheeffectivenessofinterventions.Filteringof searchesistimeconsuming,andnosinglemethodfulfillstheprincipalrequirementsofspeedwithaccuracy."
- PENDING-REF-120-E3 | page: 2, section: extracted, quote: "This process has clearly designated steps to identify primary studies and the methods which will be employed to assess their methodological quality, the way in which data will be extracted, and the statistical techniques that will be used in the synthesis and reporting of that data [2]."
- PENDING-REF-120-E4 | page: 2, section: extracted, quote: "A systematic review is a summary of the medical literature that uses explicit methods to systematically search, critically appraise, and synthesize the data on a specific topic."
- PENDING-REF-120-E5 | page: 1, section: extracted, quote: "Automationofsystematicreviewsisdrivenbyanecessitytoexpeditetheavailabilityofcurrentbestevidencefor policyandclinicaldecision-making."
- PENDING-REF-120-E6 | page: 1, section: extracted, quote: "WedevelopedRayyan(http://rayyan.qcri.org),afreewebandmobileapp,thathelpsexpeditetheinitialscreeningof abstractsandtitlesusingaprocessofsemi-automationwhileincorporatingahighlevelofusability.Forthebeta testingphase,weusedtwopublishedCochranereviewsinwhichincludedstudieshadbeenselectedmanually."
- PENDING-REF-120-E7 | page: 1, section: extracted, quote: "Theirsearches,with1030recordsand273records,wereuploadedtoRayyan.DifferentfeaturesofRayyanweretested usingthesetworeviews.WealsoconductedasurveyofRayyan’susersandcollectedfeedbackthroughabuilt-in feature."
- PENDING-REF-120-E8 | page: 1, section: extracted, quote: "Conclusions: Rayyanisresponsiveandintuitiveinusewithsignificantpotentialtolightentheloadofreviewers."
