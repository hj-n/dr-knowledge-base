---
id: paper-2026-pending-extra-bbs017
title: "Integrative Genomics Viewer (IGV): high-performance genomics data visualization and exploration"
authors: "H. Thorvaldsdottir, J. T. Robinson, J. P. Mesirov"
venue: "Briefings in Bioinformatics"
year: 2013
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/bbs017.pdf
seed_note_id: "paper-2025-jeon-reliable-va-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- This poses a difficult challenge as NGS and recent array-based technologies can generate data sets from gigabytes to terabytes in size.
- Tools such as Google Maps solve this problem by precomputing images representing sections of maps at multiple resolution scales, and providing fast access to the images as needed to construct a view.
- However, millions of images would be required to support all resolution scales for a large genome, thus making image management difficult without introducing the requirement of a database.
- The problem is analogous to that faced by interactive geographical mapping tools, which provide views of very large geographical databases over many resolution scales.

# Method Summary
- Keywords:visualization; next-generation sequencing; NGS; genome viewer; IGV INTRODUCTION Next-generation sequencing (NGS) and array-based profiling methods now generate large quantities of diverse types of genomic data and are enabling researchers to study the genome at unprecedented resolution.
- Below, we describe in more detail some components of the IGV implementation, including our data-tiling approach for supporting large data sets and IGVs support for different categories of file formats.
- This is necessary for both application performance, as described in the ‘Methods and Technologies’ section above, and to help investigators make sense of the massive amount of data.
- Consequently, we adopted a different approach that is based on precomputing summarizations of data at multiple resolution scales, with rendering of the data deferred to runtime.
- Visualization of these data will require new approaches for aggregating data intelligently to reveal trends, while continuing to provide access to lower-level details on demand.
- However , the size and diversity of the data sets produced by today’s sequencing and array-based profiling methods present major challenges to visualization tools.
- METHODS AND TECHNOLOGIES IGV is a desktop application written in the Java programming language and runs on all major platforms (Windows, Mac and Linux).

# When To Use / Not Use
- Use when:
  - Key Points /C15 The IGV is a high-performance desktop viewer that efficiently handles large heterogeneous data sets, while providing a smooth and intuitive user experience at all levels of genome resolution. /C15 IGV allows researchers to visualize many different types of genomic data together , including NGS data, variant calls, microarray data and genome annotations.
  - This is an Open Access article distributed under the terms of the Creative Commons Attribution Non-Commercial License (http://creativecommons.org/licenses/ by-nc/3.0), which permits unrestricted non-commercial use, distribution, and reproduction in any medium, provided the original work is properly cited.
- Avoid when:
  - To select the genomic region to view and the zoom level, an investigator can enter genomic coordinates, search for genomic features by name, zoom in or out by clicking on the railroad track control in the upper right of the window or by using mouse shortcuts, and pan by click-dragging in the data panel.
  - For example, MATLAB users have used this capability to tie IGV to interactive analyses, loading files and jumping to loci in response to commands from MATLAB functions. (iii) The HTTP interface supports creating links to launch IGV on a specific data set or send data to an already running IGV.
- Failure modes:
  - For each resolution scale (‘zoom level’), the genome Integrative Genomics Viewer 17 9 Downloaded from https://academic.oup.com/bib/article/14/2/178/208453 by guest on 08 February 2026 is divided into tiles that correspond to the region viewable on the screen of a typical user display.

# Metrics Mentioned
- No explicit named metric was extracted from this source; combine this source with complementary DR quality checks in workflow Step 3.

# Implementation Notes
- Renderers are designed to be pluggable, and can be swapped at runtime, for example to switch graph types in response to a menu action. (ii) The data layer reads and parses the different genomic file formats and supplies the application layer with data tiles on demand.
- Consequently, we adopted a different approach that is based on precomputing summarizations of data at multiple resolution scales, with rendering of the data deferred to runtime.
- IGV selects default display parameters, such as graph type and colors, for each track, based on the data type and any preferences the user may have set.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-EXTRA-C1 | stance: support | summary: This poses a difficult challenge as NGS and recent array-based technologies can generate data sets from gigabytes to terabytes in size. | evidence_ids: PENDING-EXTRA-E1, PENDING-EXTRA-E2
- CLAIM-PENDING-EXTRA-C2 | stance: support | summary: Keywords:visualization; next-generation sequencing; NGS; genome viewer; IGV INTRODUCTION Next-generation sequencing (NGS) and array-based profiling methods now generate large quantities of diverse types of genomic data and are enabling researchers to study the genome at unprecedented resolution. | evidence_ids: PENDING-EXTRA-E3, PENDING-EXTRA-E4
- CLAIM-PENDING-EXTRA-C3 | stance: support | summary: Renderers are designed to be pluggable, and can be swapped at runtime, for example to switch graph types in response to a menu action. (ii) The data layer reads and parses the different genomic file formats and supplies the application layer with data tiles on demand. | evidence_ids: PENDING-EXTRA-E5, PENDING-EXTRA-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-EXTRA-E1 | page: 2, section: extracted, quote: "This poses a difficult challenge as NGS and recent array-based technologies can generate data sets from gigabytes to terabytes in size."
- PENDING-EXTRA-E2 | page: 2, section: extracted, quote: "Tools such as Google Maps solve this problem by precomputing images representing sections of maps at multiple resolution scales, and providing fast access to the images as needed to construct a view."
- PENDING-EXTRA-E3 | page: 2, section: extracted, quote: "However, millions of images would be required to support all resolution scales for a large genome, thus making image management difficult without introducing the requirement of a database."
- PENDING-EXTRA-E4 | page: 2, section: extracted, quote: "The problem is analogous to that faced by interactive geographical mapping tools, which provide views of very large geographical databases over many resolution scales."
- PENDING-EXTRA-E5 | page: 1, section: extracted, quote: "Keywords:visualization; next-generation sequencing; NGS; genome viewer; IGV INTRODUCTION Next-generation sequencing (NGS) and array-based profiling methods now generate large quantities of diverse types of genomic data and are enabling researchers to study the genome at unprecedented resolution."
- PENDING-EXTRA-E6 | page: 2, section: extracted, quote: "Below, we describe in more detail some components of the IGV implementation, including our data-tiling approach for supporting large data sets and IGVs support for different categories of file formats."
- PENDING-EXTRA-E7 | page: 7, section: extracted, quote: "This is necessary for both application performance, as described in the ‘Methods and Technologies’ section above, and to help investigators make sense of the massive amount of data."
- PENDING-EXTRA-E8 | page: 2, section: extracted, quote: "Consequently, we adopted a different approach that is based on precomputing summarizations of data at multiple resolution scales, with rendering of the data deferred to runtime."
