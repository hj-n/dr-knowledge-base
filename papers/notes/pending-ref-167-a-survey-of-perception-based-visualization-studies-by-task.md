---
id: paper-2022-pending-ref-167
title: "A Survey of Perception-Based Visualization Studies by Task"
authors: "Ghulam Jilani Quadri and Paul Rosen"
venue: "IEEE Transactions on Visualization and Computer Graphics"
year: 2022
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-167-2022-a-survey-of-perception-based-visualization-studies-by-task.pdf
seed_note_id: "paper-2025-jeon-reliable-va-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- Comparing a visualization to a mental image is similar to statistical analysis, and thus repeated interpretation of visualization is sensitive to the multiple comparison problem—the probability of discovering false insights when visualization is examined more times or compared [132].
- Recent suggestions for mitigating this problem revolve around tightly coupling original research with replication studies [12], [143], though this approach does not address the lack of incentives.
- One of the key challenges with many graphical perception studies is their limited scope and reproducibility [12], caused in part by the difﬁculty of constructing human studies.
- The problem is further exacerbated by the limited scope of visualization studies, speciﬁcity of experiments, and difﬁcult logistics required for reproducing a study.

# Method Summary
- As the research objectives and methodologies have evolved, insights have become more ﬁne-grained and nuanced, e.g., Chung et al. observed that color saturation with size could be used as an ordering variable [37].
- An optimizationbased method introduced and evaluated an approach to generate “spot-the-difference” alternatives [156].
- They used a method of color assignment to design scatterplots that optimized class separability perception taking into account densityrelated factors, such as spatial relationship, density, degree of overlaps between points and cluster, and background color [99], which could not be achieved by the default colormapping.
- Seeing that the vast majority of perceptual studies in visualization had a speciﬁc low-level task as the main study objective or a low-level task was used in the evaluation, we centered on that as the main category of the taxonomy.
- In particular, we focus on how perception is used to evaluate the effectiveness of visualizations, to help readers understand and apply the principles of perception of their visualization designs through a task-optimized approach.
- In particular, we focus on how perception is used to evaluate the quality of visualizations, to help readers understand and apply the principles of perception to their visualization designs through a task-optimized approach.
- Recent work by Elliott et al. introduced a design space of experimental methods for empirically investigating the perceptual processes involved in viewing data visualizations to inform visualization design guidelines [16].

# When To Use / Not Use
- Use when:
  - The work focuses on a few of the fundamental questions, e.g.: What is the best way to measure how a given visualization works?
  - In addition to general guidelines, several researchers have focused on developing robust frameworks for optimizing design.
- Avoid when:
  - Chang et al.’s work compared matrix diagrams, node-link diagrams, and weighted networks to ﬁnd effective matrix representations in side-by-side views for network exploration tasks on error, completion time, and user preference [139].
  - In an evaluation of multidimensional visualizations, where the task of ﬁnding range is evaluated on three user performance metrics of accuracy, completion time, and user satisfaction, parallel coordinates and tabular visualization were found to be effective in terms of accuracy and completion time, but parallel coordinates were least preferred by users [45].
- Failure modes:
  - Optimizing the use of typography in visualizations, e.g., the location of the labeling and parameters including typeface, font size, font weight, color, orientation, intensity (boldness), spacing, case, border, background, underline, and shadow, determines the legibility of text and, thus, inﬂuences the understandability of the visualization [49].

# Metrics Mentioned
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- A study focusing on the perceptual optimization of scatterplot design studied standard design parameters, including mark size, opacity, and aspect ratio, and it demonstrated that effective choices of the variables enhanced class separation [98].
- Optimizing the use of typography in visualizations, e.g., the location of the labeling and parameters including typeface, font size, font weight, color, orientation, intensity (boldness), spacing, case, border, background, underline, and shadow, determines the legibility of text and, thus, inﬂuences the understandability of the visualization [49].
- Based on the judged similarities using Likert ratings among visual variables, ﬁndings can be applied to improve visualization design through automatic palette optimization.
- Their guidelines considered optimizations based on typography (i.e., font weight, size, and color) and word placement (i.e., sorting, clustering, and spatial layout) [59].
- T ext.The optimal setting of typography parameters determines the legibility of text, thus, inﬂuences the understandability of visualizations.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-167-C1 | stance: support | summary: Comparing a visualization to a mental image is similar to statistical analysis, and thus repeated interpretation of visualization is sensitive to the multiple comparison problem—the probability of discovering false insights when visualization is examined more times or compared [132]. | evidence_ids: PENDING-REF-167-E1, PENDING-REF-167-E2
- CLAIM-PENDING-REF-167-C2 | stance: support | summary: As the research objectives and methodologies have evolved, insights have become more ﬁne-grained and nuanced, e.g., Chung et al. observed that color saturation with size could be used as an ordering variable [37]. | evidence_ids: PENDING-REF-167-E3, PENDING-REF-167-E4
- CLAIM-PENDING-REF-167-C3 | stance: support | summary: A study focusing on the perceptual optimization of scatterplot design studied standard design parameters, including mark size, opacity, and aspect ratio, and it demonstrated that effective choices of the variables enhanced class separation [98]. | evidence_ids: PENDING-REF-167-E5, PENDING-REF-167-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 4 | relevance: high | note: contains initialization sensitivity or control-policy evidence

# Evidence
- PENDING-REF-167-E1 | page: 15, section: extracted, quote: "Comparing a visualization to a mental image is similar to statistical analysis, and thus repeated interpretation of visualization is sensitive to the multiple comparison problem—the probability of discovering false insights when visualization is examined more times or compared [132]."
- PENDING-REF-167-E2 | page: 16, section: extracted, quote: "Recent suggestions for mitigating this problem revolve around tightly coupling original research with replication studies [12], [143], though this approach does not address the lack of incentives."
- PENDING-REF-167-E3 | page: 1, section: extracted, quote: "One of the key challenges with many graphical perception studies is their limited scope and reproducibility [12], caused in part by the difﬁculty of constructing human studies."
- PENDING-REF-167-E4 | page: 16, section: extracted, quote: "The problem is further exacerbated by the limited scope of visualization studies, speciﬁcity of experiments, and difﬁcult logistics required for reproducing a study."
- PENDING-REF-167-E5 | page: 16, section: extracted, quote: "As the research objectives and methodologies have evolved, insights have become more ﬁne-grained and nuanced, e.g., Chung et al. observed that color saturation with size could be used as an ordering variable [37]."
- PENDING-REF-167-E6 | page: 18, section: extracted, quote: "An optimizationbased method introduced and evaluated an approach to generate “spot-the-difference” alternatives [156]."
- PENDING-REF-167-E7 | page: 12, section: extracted, quote: "They used a method of color assignment to design scatterplots that optimized class separability perception taking into account densityrelated factors, such as spatial relationship, density, degree of overlaps between points and cluster, and background color [99], which could not be achieved by the default colormapping."
- PENDING-REF-167-E8 | page: 3, section: extracted, quote: "Seeing that the vast majority of perceptual studies in visualization had a speciﬁc low-level task as the main study objective or a low-level task was used in the evaluation, we centered on that as the main category of the taxonomy."
