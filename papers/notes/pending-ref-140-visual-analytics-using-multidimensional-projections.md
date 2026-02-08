---
id: paper-2013-pending-ref-140
title: "Visual analytics using multidimensional projections"
authors: "M. Aupetit and L. van der Maaten"
venue: "PLoS ONE"
year: 2013
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-140-2013-visual-analytics-using-multidimensional-projections.pdf
seed_note_id: "paper-2019-mdp-visual-analytics-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- McMurdie, Susan Holmes * Department of Statistics, Stanford University, Stanford, California, United States of America Abstract Background: The analysis of microbial communities through DNA sequencing brings many challenges: the integration of different types of data with methods from ecology, genetics, phylogenetics, multivariate statistics, visualization and testing.
- For instance the bootstrap uses many thousands of analyses of resampled data to address problems such as statistical stability or bias estimation [69], and can even provide confidence regions [69] for nonstandard parameters, such as phylogenetic trees [70].
- Abstract Background: The analysis of microbial communities through DNA sequencing brings many challenges: the integration of different types of data with methods from ecology, genetics, phylogenetics, multivariate statistics, visualization and testing.
- With the increased breadth of experimental designs now being pursued, project-specific statistical analyses are often needed, and these analyses are often difficult (or impossible) for peer researchers to independently reproduce.

# Method Summary
- Comparisons of the type and quantity of OTUs observed between microbiome samples (‘‘beta diversity’’) is often approached through the calculation of pairwise ecological distances [42,43], and through dimensional reduction (ordination) methods.
- McMurdie, Susan Holmes * Department of Statistics, Stanford University, Stanford, California, United States of America Abstract Background: The analysis of microbial communities through DNA sequencing brings many challenges: the integration of different types of data with methods from ecology, genetics, phylogenetics, multivariate statistics, visualization and testing.
- The abbreviations CA, DCA, RDA, and DPCoA stand for the ordination methods correspondence analysis, detrended correspondence analysis, redundancy analysis, and double principal An R Package for Microbiome Census Data PLOS ONE | www.plosone.org 9 April 2013 | Volume 8 | Issue 4 | e61217 coordinates analysis, respectively.
- Both the ‘‘biplot’’ and ‘‘split’ ’ options allow dual projections of both OTU- and sample-space. doi:10.1371/journal.pone.0061217.g005 An R Package for Microbiome Census Data PLOS ONE | www.plosone.org 6 April 2013 | Volume 8 | Issue 4 | e61217 characteristics of the data and research questions.
- An alternative experimental method is random ‘‘shotgun’’ sequencing [20,21] of un-amplified metagenomic DNA [22], in which case OTU clustering and counting is based upon one or more detectable phylogenetic markers in the metagenomic sequence fragments, using tools such as phylOTU [23].
- In phyloseq the interface for ecological distance calculations is a single function, distance, that takes a phyloseq object as its data argument as well as a character string indicating the distance method, with explicit support for more than 40 ecological distance methods.
- With this integrated representation of the data it is easy to use supervised methods — such as canonical correspondence analysis, discriminant correspondence analysis, sparse linear discriminant analysis, etc. — to explain clinical or environmental response variables.

# When To Use / Not Use
- Use when:
  - We hope that this will provide a gateway for users to take their analyses towards more robust nonparametric alternatives to classical least squares methods, and allow them to interact graphically with their data more easily and efficiently.
  - The intended role for phyloseq is indicated. doi:10.1371/journal.pone.0061217.g001 An R Package for Microbiome Census Data PLOS ONE | www.plosone.org 2 April 2013 | Volume 8 | Issue 4 | e61217 Repository [34], and uses a literate-programming framework based on structured in-source comments, called roxygen2 [41], for (re)building the R documentation (.Rd) files and the namespace specifications.
- Avoid when:
  - While it is often useful and convenient to have common analyses coupled within the application that decodes the sequences and clusters OTUs, we posit that a separate set of flexible open-source analytical tools is also needed that can be reproduced consistently by peers, and easily applied to new datasets and data sources.
  - This multi-component ‘‘experiment-level’’ class — named ‘‘phyloseq’’, and referred to here as ‘‘the phyloseq-class’’ — is a key design feature of the phyloseq project, with subsequent user-accessible functions expecting to operate on an instance of this class as their sole or primary input data.
- Failure modes:
  - In this particular example, the bioenv function from the vegan package [92] is demonstrated. (ZIP) Acknowledgments We would like to thank Martin Morgan and Valerie Obenchain at Bioconductor for their useful suggestions regarding the architecture and organization of phyloseq.

# Metrics Mentioned
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- This is particularly true when the preprocessing transformations are the result of ‘‘manual’’ adjustments in a spreadsheet, custom code/script that is not included in the publication, or random subsampling (‘‘rarefying’’ to even sequencing effort) with no reported seed.
- For instance the bootstrap uses many thousands of analyses of resampled data to address problems such as statistical stability or bias estimation [69], and can even provide confidence regions [69] for nonstandard parameters, such as phylogenetic trees [70].
- An organizing principle in many nonparametric testing protocols is that the repetition of an analysis multiple times enables the user to control for multiple testing, or to evaluate the quality of estimators or the optimal values of tuning parameters.
- A related example is the (often not-so) reproducible choice of tuning parameters and perturbation-based statistical validation procedures, allowing for the easy testing of alternatives and robustness of results.
- Additional parameters easily map the respective sample variable or taxonomic rank to color, size, or shape aesthetics.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-140-C1 | stance: support | summary: McMurdie, Susan Holmes * Department of Statistics, Stanford University, Stanford, California, United States of America Abstract Background: The analysis of microbial communities through DNA sequencing brings many challenges: the integration of different types of data with methods from ecology, genetics, phylogenetics, multivariate statistics, visualization and testing. | evidence_ids: PENDING-REF-140-E1, PENDING-REF-140-E2
- CLAIM-PENDING-REF-140-C2 | stance: support | summary: Comparisons of the type and quantity of OTUs observed between microbiome samples (‘‘beta diversity’’) is often approached through the calculation of pairwise ecological distances [42,43], and through dimensional reduction (ordination) methods. | evidence_ids: PENDING-REF-140-E3, PENDING-REF-140-E4
- CLAIM-PENDING-REF-140-C3 | stance: support | summary: This is particularly true when the preprocessing transformations are the result of ‘‘manual’’ adjustments in a spreadsheet, custom code/script that is not included in the publication, or random subsampling (‘‘rarefying’’ to even sequencing effort) with no reported seed. | evidence_ids: PENDING-REF-140-E5, PENDING-REF-140-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 4 | relevance: high | note: contains initialization sensitivity or control-policy evidence

# Evidence
- PENDING-REF-140-E1 | page: 1, section: extracted, quote: "McMurdie, Susan Holmes * Department of Statistics, Stanford University, Stanford, California, United States of America Abstract Background: The analysis of microbial communities through DNA sequencing brings many challenges: the integration of different types of data with methods from ecology, genetics, phylogenetics, multivariate statistics, visualization and testing."
- PENDING-REF-140-E2 | page: 8, section: extracted, quote: "For instance the bootstrap uses many thousands of analyses of resampled data to address problems such as statistical stability or bias estimation [69], and can even provide confidence regions [69] for nonstandard parameters, such as phylogenetic trees [70]."
- PENDING-REF-140-E3 | page: 1, section: extracted, quote: "Abstract Background: The analysis of microbial communities through DNA sequencing brings many challenges: the integration of different types of data with methods from ecology, genetics, phylogenetics, multivariate statistics, visualization and testing."
- PENDING-REF-140-E4 | page: 1, section: extracted, quote: "With the increased breadth of experimental designs now being pursued, project-specific statistical analyses are often needed, and these analyses are often difficult (or impossible) for peer researchers to independently reproduce."
- PENDING-REF-140-E5 | page: 3, section: extracted, quote: "Comparisons of the type and quantity of OTUs observed between microbiome samples (‘‘beta diversity’’) is often approached through the calculation of pairwise ecological distances [42,43], and through dimensional reduction (ordination) methods."
- PENDING-REF-140-E6 | page: 9, section: extracted, quote: "The abbreviations CA, DCA, RDA, and DPCoA stand for the ordination methods correspondence analysis, detrended correspondence analysis, redundancy analysis, and double principal An R Package for Microbiome Census Data PLOS ONE / www.plosone.org 9 April 2013 / Volume 8 / Issue 4 / e61217 coordinates analysis, respectively."
- PENDING-REF-140-E7 | page: 6, section: extracted, quote: "Both the ‘‘biplot’’ and ‘‘split’ ’ options allow dual projections of both OTU- and sample-space. doi:10.1371/journal.pone.0061217.g005 An R Package for Microbiome Census Data PLOS ONE / www.plosone.org 6 April 2013 / Volume 8 / Issue 4 / e61217 characteristics of the data and research questions."
- PENDING-REF-140-E8 | page: 1, section: extracted, quote: "An alternative experimental method is random ‘‘shotgun’’ sequencing [20,21] of un-amplified metagenomic DNA [22], in which case OTU clustering and counting is based upon one or more detectable phylogenetic markers in the metagenomic sequence fragments, using tools such as phylOTU [23]."
