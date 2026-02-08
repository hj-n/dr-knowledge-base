---
id: paper-2023-pending-ref-166
title: "Projection Ensemble: Visualizing the Robust Structures of Multidimensional Projections"
authors: "Myeongwon Jung, Jiwon Choi, and Jaemin Jo"
venue: "2023 IEEE Visualization and Visual Analytics (VIS)"
year: 2023
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-166-2023-projection-ensemble-visualizing-the-robust-structures-of-multidimensional-projections.pdf
seed_note_id: "paper-2025-jeon-reliable-va-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- In common with most MR algorithms, it divides the six-dimensional search problem for each copy into a three-dimensional rotation search followed by a three-dimensional translation search.
- This task is challenging, because the molecules are typically very large, chain tracing is difficult at low resolution and effective resolution can be even lower in some regions.
- Cryo-EM: Mtriage The sample for a cryo-EM experiment is not crystalline, so many of the problems discussed in the previous section (3.1.1) are not relevant.
- By providing the model and optional data in mmCIF format, the validation report can help users identify problems before starting the deposition process.

# Method Summary
- This approach is very efficient because high-level algorithms (such as refinement protocols) can be rapidly developed in the scripting language while computationally intensive algorithms can be implemented in the compiled language.
- Each method has a different approach to derive structural information, with Phenix offering specific tools to address the unique properties of the experimental data.
- The protocol is particularly useful for low resolution diffraction data (Brunger et al., 2012). –“Rosetta refinement” (phenix.rosetta_refine) integrates the Rosetta methods for conformational sampling (DiMaio et al., 2013) with the X-ray targets, ADP refinement and map generation in phenix.refine.
- For example, free electron lasers (FELs) and serial synchrotron crystallography (Chapman et al., 2011; Rossmann, 2014; Diederichs & Wang, 2017; Standfuss & Spence, 2017; Schlichting, 2015) have opened up new approaches to studying the dynamics of macromolecules.
- Abstract Diffraction (X-ray, neutron, electron) and electron cryo-microscopy are powerful methods to determine three-dimensional macromolecular structures that are required to understand biological processes and to develop new therapeutics against diseases.
- Since the first protein structures were determined in the 1950’s (Kendrew et al., 1958; Perutz et al., 1960), the method has experienced many methodological and technological developments and is now considered quite mature (Wlodawer et al., 2013).
- Technological advances, such as the development of direct electron detectors (Li et al., 2013) and improvements in image processing (Bai et al., 2015) have transformed the method, leading to greatly improved resolution of cryo-EM maps.

# When To Use / Not Use
- Use when:
  - Furthermore, the use of focused refinement of cryo-EM data (von Loeffelholz et al., 2017; Natchiar et al., 2017) can generate much improved local reconstructions, but it remains to be seen how these can be best combined for model generation and subsequent model refinement.
  - Emphasis is put on the automation of all procedures to avoid burdening the user with repetitive, time-consuming and often error-prone tasks.
- Avoid when:
  - The real-space refinement procedure is robust and works at resolutions from 1 to 6 Å.
  - In addition, likelihood provides a framework for the use of ensemble models created with Ensembler (phenix.ensembler) and 3 MAD = multiple-wavelength anomalous diffraction, MIR = multiple isomorphous replacement, SIR = single isomorphous replacement Acta Crystallographica Section D feature articles 9 for exploiting the placement of one copy to increase the signal of the search for another copy (McCoy et al., 2007).
- Failure modes:
  - Parallelity restraints keep the atom groups parallel (Sobolev et al., 2015; Richardson, 2015). – Rotamer-specific restraints: These restraints lock a particular χ-angle configuration of an amino-acid residue side chain to preserve its valid rotameric state. – NCS restraints: If the asymmetric unit contains two or more similar copies of the same molecule, torsion- or Cartesian-based NCS restraints can be used.

# Metrics Mentioned
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- This strategy, called joint X-ray and neutron refinement (joint XN refinement), ameliorates the data-to-parameters ratio by increasing the amount of experimental data used in refinement, leading to more complete and accurate models (Coppens, 1967; Orpen et al., 1978; Wlodawer, 1980; Wlodawer & Hendrickson, 1982).
- The shape search applies the following key elements: An initial search, focusing on the overall shape of the molecule, is performed at lower resolution, This initial search is done without rotation to optimize runtime;, it can supplemented optionally by matching the moments of inertia of the model and map.
- ADP parameterizations include the Translation/Libration/Screw (TLS) model for movement of groups treated as rigid (Schomaker & Trueblood, 1968; Urzhumtsev et al., 2016; Afonine, Adams et al., 2018) as well as individual isotropic, anisotropic and grouped isotropic ADP.
- The default mode performs gradient-driven minimization of the entire model, but optimization can also be performed using simulated annealing, morphing (Terwilliger et al., 2013), rigid-body refinement and systematic side-chain improvement (Oldfield, 2001).
- X-ray: phenix.refine For crystallographic data, refinement is usually performed in reciprocal space, i.e. the parameters of the model are changed so that model-derived structure factors match experimental structure factor amplitudes or intensities.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-166-C1 | stance: support | summary: In common with most MR algorithms, it divides the six-dimensional search problem for each copy into a three-dimensional rotation search followed by a three-dimensional translation search. | evidence_ids: PENDING-REF-166-E1, PENDING-REF-166-E2
- CLAIM-PENDING-REF-166-C2 | stance: support | summary: This approach is very efficient because high-level algorithms (such as refinement protocols) can be rapidly developed in the scripting language while computationally intensive algorithms can be implemented in the compiled language. | evidence_ids: PENDING-REF-166-E3, PENDING-REF-166-E4
- CLAIM-PENDING-REF-166-C3 | stance: support | summary: This strategy, called joint X-ray and neutron refinement (joint XN refinement), ameliorates the data-to-parameters ratio by increasing the amount of experimental data used in refinement, leading to more complete and accurate models (Coppens, 1967; Orpen et al., 1978; Wlodawer, 1980; Wlodawer & Hendrickson, 1982). | evidence_ids: PENDING-REF-166-E5, PENDING-REF-166-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-REF-166-E1 | page: 8, section: extracted, quote: "In common with most MR algorithms, it divides the six-dimensional search problem for each copy into a three-dimensional rotation search followed by a three-dimensional translation search."
- PENDING-REF-166-E2 | page: 10, section: extracted, quote: "This task is challenging, because the molecules are typically very large, chain tracing is difficult at low resolution and effective resolution can be even lower in some regions."
- PENDING-REF-166-E3 | page: 6, section: extracted, quote: "Cryo-EM: Mtriage The sample for a cryo-EM experiment is not crystalline, so many of the problems discussed in the previous section (3.1.1) are not relevant."
- PENDING-REF-166-E4 | page: 16, section: extracted, quote: "By providing the model and optional data in mmCIF format, the validation report can help users identify problems before starting the deposition process."
- PENDING-REF-166-E5 | page: 16, section: extracted, quote: "This approach is very efficient because high-level algorithms (such as refinement protocols) can be rapidly developed in the scripting language while computationally intensive algorithms can be implemented in the compiled language."
- PENDING-REF-166-E6 | page: 4, section: extracted, quote: "Each method has a different approach to derive structural information, with Phenix offering specific tools to address the unique properties of the experimental data."
- PENDING-REF-166-E7 | page: 14, section: extracted, quote: "The protocol is particularly useful for low resolution diffraction data (Brunger et al., 2012). –“Rosetta refinement” (phenix.rosetta_refine) integrates the Rosetta methods for conformational sampling (DiMaio et al., 2013) with the X-ray targets, ADP refinement and map generation in phenix.refine."
- PENDING-REF-166-E8 | page: 17, section: extracted, quote: "For example, free electron lasers (FELs) and serial synchrotron crystallography (Chapman et al., 2011; Rossmann, 2014; Diederichs & Wang, 2017; Standfuss & Spence, 2017; Schlichting, 2015) have opened up new approaches to studying the dynamics of macromolecules."
