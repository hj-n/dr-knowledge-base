---
id: paper-2020-pending-ref-147
title: "t-Distributed Stochastic Neighbor Embedding (t-SNE): A tool for eco-physiological transcriptomic analysis"
authors: "M. C. Cieslak, A. M. Castelfranco, V . Roncalli, P . H. Lenz, and D. K. Hartline"
venue: "Marine Genomics"
year: 2020
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-147-2020-t-distributed-stochastic-neighbor-embedding-t-sne-a-tool-for-eco-physiological-transc.pdf
seed_note_id: "paper-2025-critical-analysis-dr-four-domains"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- In addressing the problem at the geneexpression level, much of ecology, including biological oceanography, currently depends on identifying the condition of pre-selected biological processes using single-gene (or small gene-set) biomarkers for expression profiling of transcriptional physiological state.
- However, the technology generates complex data consisting of millions of short-read sequences that can be difficult to analyze and interpret.

# Method Summary
- Contents lists available atScienceDirect Marine Genomics journal homepage: www.elsevier.com/locate/margen Method paper t-Distributed Stochastic Neighbor Embedding (t-SNE): A tool for eco-physiological transcriptomic analysis Matthew C.
- More recently a broader approach has been taken: twode novoreference transcriptomes have been assembled for this species using high-throughput Illumina sequencing (RNA-Seq) of short RNA fragments (Lenz et al., 2014;Tarrant et al., 2014).
- One complexity-reducing tool that has been used successfully in other fields is “t-distributed Stochastic Neighbor Embedding” (t-SNE).
- Contents lists available atScienceDirect Marine Genomics journal homepage: www.elsevier.com/locate/margen Method paper t-Distributed Stochastic Neighbor Embedding (t-SNE): A tool for eco-physiological transcriptomic analysis Matthew C.
- Hartlinea aPacific Biosciences Research Center, University of Hawaiʻi at Mānoa, 1993 East-West Rd., Honolulu, HI 96822, USA b Department of Genetics, Microbiology and Statistics, Facultat de Biologia, IRBio, Universitat de Barcelona, Av.
- Diagonal 643, 08028 Barcelona, Spain ARTICLE INFO Keywords: Omics RNA-Seq Bioinformatics Zooplankton Copepod ABSTRACT High-throughput RNA sequencing (RNA-Seq) has transformed the ecophysiological assessment of individual plankton species and communities.
- However, the technology generates complex data consisting of millions of short-read sequences that can be difficult to analyze and interpret.

# When To Use / Not Use
- Use when:
  - But the “physiological state” of an organism is not easily determined because it comprises a multitude of interacting chemical and physical processes governed by gene expression and gene regulatory networks operating simultaneously in multiple organs and tissues of the body.
  - For example, gene expression studies on key zooplankton species such asCalanus finmarchicus, have typically focused on relative expression of target genes as biomarkers of physiological responsiveness (e.g. stress markers: Voznesensky et al., 2004;Tarrant et al., 2008;Hansen et al., 2008, 2010; Aruda et al., 2011;Roncalli et al., 2016c).
- Avoid when:
  - Caveats As we have shown, the t-SNE algorithm has proven to be quite effective in quickly identifying clusters of similar transcriptomic profiles in samplesbothfromlabexperimentsand fieldcollections.However,as noted above, there are limitations to the proper application of the tool.
  - The analysis byRoncalli et al. (2019), which categorized each station intoaseparate“group”,usedaGeneralizedLinearModel(GLM)toidentify patterns of increased nutritional stress between Prince William Sound and out along the Seward Line (GAK1 to GAK14).
- Failure modes:
  - Transcriptional profiling ofN. flemingeripre-adults (copepodid stage CV)demonstratedhowregionalheterogeneityinresourceavailabilityis affecting the physiology of a copepod during preparation for diapause (dormancy) (Roncalli et al., 2019).

# Metrics Mentioned
- `stress`: referenced as part of projection-quality or reliability assessment.
- `kl divergence`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- While the clusters are robust, the arrangement of clusters on the 2D plane is not necessarily informative and can switch around dramatically in different runs and with different parameters (as for example with the filters inFigs.
- The distances between clusters gives a sense of global geometry, but it requires optimizing the setting of the “perplexity” parameterto develop.
- Running the algorithm under multiple conditions of the controlling parameters can reduce ambiguity.
- Also, many iterations are required before the algorithm
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-147-C1 | stance: support | summary: In addressing the problem at the geneexpression level, much of ecology, including biological oceanography, currently depends on identifying the condition of pre-selected biological processes using single-gene (or small gene-set) biomarkers for expression profiling of transcriptional physiological state. | evidence_ids: PENDING-REF-147-E1, PENDING-REF-147-E2
- CLAIM-PENDING-REF-147-C2 | stance: support | summary: Contents lists available atScienceDirect Marine Genomics journal homepage: www.elsevier.com/locate/margen Method paper t-Distributed Stochastic Neighbor Embedding (t-SNE): A tool for eco-physiological transcriptomic analysis Matthew C. | evidence_ids: PENDING-REF-147-E3, PENDING-REF-147-E4
- CLAIM-PENDING-REF-147-C3 | stance: support | summary: While the clusters are robust, the arrangement of clusters on the 2D plane is not necessarily informative and can switch around dramatically in different runs and with different parameters (as for example with the filters inFigs. | evidence_ids: PENDING-REF-147-E5, PENDING-REF-147-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 4 | relevance: high | note: contains initialization sensitivity or control-policy evidence

# Evidence
- PENDING-REF-147-E1 | page: 1, section: extracted, quote: "In addressing the problem at the geneexpression level, much of ecology, including biological oceanography, currently depends on identifying the condition of pre-selected biological processes using single-gene (or small gene-set) biomarkers for expression profiling of transcriptional physiological state."
- PENDING-REF-147-E2 | page: 1, section: extracted, quote: "However, the technology generates complex data consisting of millions of short-read sequences that can be difficult to analyze and interpret."
- PENDING-REF-147-E3 | page: 1, section: extracted, quote: "Contents lists available atScienceDirect Marine Genomics journal homepage: www.elsevier.com/locate/margen Method paper t-Distributed Stochastic Neighbor Embedding (t-SNE): A tool for eco-physiological transcriptomic analysis Matthew C."
- PENDING-REF-147-E4 | page: 1, section: extracted, quote: "More recently a broader approach has been taken: twode novoreference transcriptomes have been assembled for this species using high-throughput Illumina sequencing (RNA-Seq) of short RNA fragments (Lenz et al., 2014;Tarrant et al., 2014)."
- PENDING-REF-147-E5 | page: 1, section: extracted, quote: "One complexity-reducing tool that has been used successfully in other fields is “t-distributed Stochastic Neighbor Embedding” (t-SNE)."
- PENDING-REF-147-E6 | page: 1, section: extracted, quote: "Hartlinea aPacific Biosciences Research Center, University of Hawaiʻi at Mānoa, 1993 East-West Rd., Honolulu, HI 96822, USA b Department of Genetics, Microbiology and Statistics, Facultat de Biologia, IRBio, Universitat de Barcelona, Av."
- PENDING-REF-147-E7 | page: 1, section: extracted, quote: "Diagonal 643, 08028 Barcelona, Spain ARTICLE INFO Keywords: Omics RNA-Seq Bioinformatics Zooplankton Copepod ABSTRACT High-throughput RNA sequencing (RNA-Seq) has transformed the ecophysiological assessment of individual plankton species and communities."
- PENDING-REF-147-E8 | page: 1, section: extracted, quote: "But the “physiological state” of an organism is not easily determined because it comprises a multitude of interacting chemical and physical processes governed by gene expression and gene regulatory networks operating simultaneously in multiple organs and tissues of the body."
- PENDING-REF-147-E9 | page: 2, section: extracted, quote: "Here we show the application and robustness of a technique termed “t-distributed Stochastic Neighbor Embedding,” or “t-SNE” (van der Maaten and Hinton, 2008).This stateof-the-art technique is being used increasingly for dimensionality-reduction of large datasets."
- PENDING-REF-147-E10 | page: 3, section: extracted, quote: "expression profiles (read-counts) were normalized across samples by the length of each transcript, being computed as the number of reads per kilobase of transcript length per million mapped reads (RPKM; Mortazavi et al., 2008; see also Supplementary Methods S1)."
