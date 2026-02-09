---
id: paper-2026-zadu-ref-10
title: "Quantifying the Neighborhood Preservation of Self-Organizing Feature Maps"
authors: "of Self/-Organizing F eature Maps"
venue: "IEEE Transactions on Neural Networks"
year: 1992
tags: [dr, zadu-table1-reference, topo]
source_pdf: papers/raw/zadu-table1-references/download (2).pdf
evidence_level: medium
updated_at: 2026-02-08
---
# Problem
- This is a coincidence of t w o indep enden t in v estigations in to the e/ ects of v arying output space dimensionalit y in SFMs/, whic h underlines the imp ortance of top ograph y in suc h maps/. /1/8 /7 Summary and discussion In this con tribution/, w e solv ed the problem of the quan titativ e c haracterization of neigh/- b orho o d preserv ation in self/-organizing feature maps/.
- Ev en though for this example the in tuitiv e approac h seems adequate/, w e note that the top ographic pro duct metho d is an in terpretation/-free/, quan ti/- tativ e approac h/, whic h will pro v e its v alue for more complicated mapping problems/, when the /"in tuitiv e approac h/" fails for whatev er reasons/.
- If the recognition problem is just a feature v ector classi/ cation as in phoneme recognition/, neigh b orho o d relations b et w een the output no des are of no imp ortance for the p erformance of the net/.
- It is sensitiv e to large scale violations of the neigh b orho o d ordering/, but do es not accoun t for neigh b orho o d ordering distortions due to v arying areal magni/ cation factors/.
- In Fig/. /3/, this is the case for no de /3 and its fourth/-nearest neigh b or n V /4 /(/3/) /= /1/0/2/, whic h ha v e closeb y p oin ters due to a distortion of the map/.

# Method Summary
- In this w a y the optimization of net w ork p erformance b y optimizing the net w ork top ology /, a strategy whic h pro v ed v ery sucessful for MLPs/, will b e easier to implemen t also for SFMs/. /8 Ac kno wledgemen ts This w ork has b een supp orted b y the Deutsc he F orsc h ungsgemeinsc haft /(Sonder/- forsc h ungsb ereic h /1/8/5 /"Nic h tlineare Dynamik/"/, TP A/1/0/)/.
- The recognition w as p erformed b y classifying the resulting tra jectories in the output space with a dynamics time w arping algorithm/. /2 Kohonen Algorithm for Self/-Organizing F eature Maps The Kohonen algorithm is a w ell a established learning rule for self/-organizing feature maps/, whic h can easily b e implemen ted/.
- The classi/ cation w as p erformed with a dynamic time w arping algorithm/, whic h eliminated / uctuations of the sp eak er v elo cit y /. /(Apart from the time w arping asp ect/, w e built the demonstration sc heme of the last c hapter follo wing their approac h/)/.
- It is this asp ect of maps whic h serv es as an organizing principle for map formation algorithms/, one of whic h/, the Kohonen/-algorithm/, w e will discuss in the second c hapter/.
- W e should note here/, that other map formation algorithms ha v e b een prop osed/, whic h induce non trivial output space top ologies /[/1/7 /, /1/8/]/.
- Here it should su/ce to giv e only a short accoun t of the algorithm whic h will pro vide the notation used in the subsequen t c hapters/.
- F or the classi/ cation of the output space tra jecto/- ries for example a dynamic time w arping /(DTW/) algorithm can b e used/.

# When To Use / Not Use
- Use when:
  - Ev en though for this example the in tuitiv e approac h seems adequate/, w e note that the top ographic pro duct metho d is an in terpretation/-free/, quan ti/- tativ e approac h/, whic h will pro v e its v alue for more complicated mapping problems/, when the /"in tuitiv e approac h/" fails for whatev er reasons/.
  - One p ossible reason is an input space of dimensionalit y D V /> /3/, b ecause then the map cannot b e visualized/, ev en if the stim uli lie in a lo w er dimensional subspace/. /5 Recognition of Sequences This c hapter is mean t as a demonstration/, that a p erfect preserv ation of neigh b orho o d relations can ha v e a v alue in applications/, whic h go es w a y b ey ond some esthetic consid/- erations of theorists/.
  - There it w as used to a similar purp ose lik e in this pap er/: it serv ed as a to ol to select optimal em b edding parameters /(dimension and dela y time/) for the reconstruction of c haotic attractors from one/-v ariable time series via dela y co ordinates/.
- Avoid when:
  - First w e do not w an t to confuse the results of dimensionalit y mismatc h with other in/ uence factors/, secondly w e w an t to c hec k the /1/1 quan titativ e results of the top ographic pro duct metho d for plausibilit y /.
  - T o this purp ose w e need not in tro duce a new example/, but w e can /1/4 use the results from the last c hapter/, whic h dealt with the mapping from a square input space on to output spaces of di/ eren t dimension/.
- Failure modes:
  - This turns out to b e in agreemen t with a comparable sp eec h recognition exp erimen t /[/1/5/]/, where Kohonen maps of /3 di/ eren t output space dimension ha v e b een used for prepro cessing/.
  - This is b ecause only one output no de is activ ated during a classi/ cation pro cess/, and the application do es not in v olv e an y measure of distance b et w een the output no des/.

# Metrics Mentioned
- `nd`: neighbor-shape dissimilarity or neighbor distortion.
- `pr`: pairwise-distance correlation behavior.

# Implementation Notes
- There it w as used to a similar purp ose lik e in this pap er/: it serv ed as a to ol to select optimal em b edding parameters /(dimension and dela y time/) for the reconstruction of c haotic attractors from one/-v ariable time series via dela y co ordinates/.
- A t ypical c hoice for h /0 j/;i is h /0 j/;i /( d /) /= e /? d /2 /2 / /2 /: /(/2/./3/) The complete learning phase consists in a /(random/) initialization of the w j /, follo w ed b y a n um b er of the ab o v e describ ed learning steps/.
- In fact/, large scale neigh b orho o d violations in maps are usually detected b y visually insp ecting the map/; a metho d/, whic h is restricted to su/cien tly lo w/-dimensional input spaces /(not to men tion its arbitrariness/)/.
- Nev ertheless/, the shap e of the curv es in Fig/. /5b is ab out the same as in Fig/. /4b/, with a horizon tal axis rescaled linearly with the n um b er of no des /(The maxim um neigh b orho o d order has a v alue of N /? /1/)/.
- It is sensitiv e to large scale violations of the neigh b orho o d ordering/, but do es not accoun t for neigh b orho o d ordering distortions due to v arying areal magni/ cation factors/.
- The v alues seem to con v erge ev en on a logarithmic scale/, in this w a y justifying the heuristic a v eraging in Eq/. /(/3/./1/2/)/.
- Keep preprocessing, initialization policy, and random-seed protocol fixed when comparing methods.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PAPER2026ZADUREF10-C1 | stance: support | summary: This is a coincidence of t w o indep enden t in v estigations in to the e/ ects of v arying output space dimensionalit y in SFMs/, whic h underlines the imp ortance of top ograph y in suc h maps/. /1/8 /7 Summary and discussion In this con tribution/, w e solv ed the problem of the quan titativ e c haracterization of neigh/- b orho o d preserv ation in self/-organizing feature maps/. | evidence_ids: PAPER2026ZADUREF10-E1, PAPER2026ZADUREF10-E2
- CLAIM-PAPER2026ZADUREF10-C2 | stance: support | summary: In this w a y the optimization of net w ork p erformance b y optimizing the net w ork top ology /, a strategy whic h pro v ed v ery sucessful for MLPs/, will b e easier to implemen t also for SFMs/. /8 Ac kno wledgemen ts This w ork has b een supp orted b y the Deutsc he F orsc h ungsgemeinsc haft /(Sonder/- forsc h ungsb ereic h /1/8/5 /"Nic h tlineare Dynamik/"/, TP A/1/0/)/. | evidence_ids: PAPER2026ZADUREF10-E3, PAPER2026ZADUREF10-E4
- CLAIM-PAPER2026ZADUREF10-C3 | stance: support | summary: There it w as used to a similar purp ose lik e in this pap er/: it serv ed as a to ol to select optimal em b edding parameters /(dimension and dela y time/) for the reconstruction of c haotic attractors from one/-v ariable time series via dela y co ordinates/. | evidence_ids: PAPER2026ZADUREF10-E5, PAPER2026ZADUREF10-E6
- CLAIM-METRIC-TOPO-SOURCE-10 | stance: support | summary: This source includes evidence relevant to `topo` in dimensionality-reduction reliability evaluation. | evidence_ids: PAPER2026ZADUREF10-E1, PAPER2026ZADUREF10-E2

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports task clarification before model selection
- step: 2 | relevance: medium | note: adds constraints for preprocessing and data-audit checks
- step: 3 | relevance: high | note: directly informs task-aligned technique/metric selection
- step: 5 | relevance: medium | note: adds initialization sensitivity guidance
- step: 6 | relevance: high | note: adds hyperparameter sensitivity or optimization guidance

# Evidence
- PAPER2026ZADUREF10-E1 | page: 18, section: extracted, quote: "This is a coincidence of t w o indep enden t in v estigations in to the e/ ects of v arying output space dimensionalit y in SFMs/, whic h underlines the imp ortance of top ograph y in suc h maps/. /1/8 /7 Summary and discussion In this con tribution/, w e solv ed the problem of the quan titativ e c haracterization of neigh/- b orho o d preserv ation in self/-organizing feature maps/."
- PAPER2026ZADUREF10-E2 | page: 14, section: extracted, quote: "Ev en though for this example the in tuitiv e approac h seems adequate/, w e note that the top ographic pro duct metho d is an in terpretation/-free/, quan ti/- tativ e approac h/, whic h will pro v e its v alue for more complicated mapping problems/, when the /'in tuitiv e approac h/' fails for whatev er reasons/."
- PAPER2026ZADUREF10-E3 | page: 15, section: extracted, quote: "If the recognition problem is just a feature v ector classi/ cation as in phoneme recognition/, neigh b orho o d relations b et w een the output no des are of no imp ortance for the p erformance of the net/."
- PAPER2026ZADUREF10-E4 | page: 1, section: extracted, quote: "It is sensitiv e to large scale violations of the neigh b orho o d ordering/, but do es not accoun t for neigh b orho o d ordering distortions due to v arying areal magni/ cation factors/."
- PAPER2026ZADUREF10-E5 | page: 9, section: extracted, quote: "In Fig/. /3/, this is the case for no de /3 and its fourth/-nearest neigh b or n V /4 /(/3/) /= /1/0/2/, whic h ha v e closeb y p oin ters due to a distortion of the map/."
- PAPER2026ZADUREF10-E6 | page: 3, section: extracted, quote: "Using the top ographic pro duct as a measure/, w e sho w/, ho w the matc hing output space dimensionalit y for this problem can b e found in an unam biguous w a y /."
- PAPER2026ZADUREF10-E7 | page: 20, section: extracted, quote: "In this w a y the optimization of net w ork p erformance b y optimizing the net w ork top ology /, a strategy whic h pro v ed v ery sucessful for MLPs/, will b e easier to implemen t also for SFMs/. /8 Ac kno wledgemen ts This w ork has b een supp orted b y the Deutsc he F orsc h ungsgemeinsc haft /(Sonder/- forsc h ungsb ereic h /1/8/5 /'Nic h tlineare Dynamik/'/, TP A/1/0/)/."
- PAPER2026ZADUREF10-E8 | page: 4, section: extracted, quote: "The recognition w as p erformed b y classifying the resulting tra jectories in the output space with a dynamics time w arping algorithm/. /2 Kohonen Algorithm for Self/-Organizing F eature Maps The Kohonen algorithm is a w ell a established learning rule for self/-organizing feature maps/, whic h can easily b e implemen ted/."
- PAPER2026ZADUREF10-E9 | page: 18, section: extracted, quote: "The classi/ cation w as p erformed with a dynamic time w arping algorithm/, whic h eliminated / uctuations of the sp eak er v elo cit y /. /(Apart from the time w arping asp ect/, w e built the demonstration sc heme of the last c hapter follo wing their approac h/)/."
- PAPER2026ZADUREF10-E10 | page: 2, section: extracted, quote: "It is this asp ect of maps whic h serv es as an organizing principle for map formation algorithms/, one of whic h/, the Kohonen/-algorithm/, w e will discuss in the second c hapter/."
- PAPER2026ZADUREF10-E11 | page: 6, section: extracted, quote: "W e should note here/, that other map formation algorithms ha v e b een prop osed/, whic h induce non trivial output space top ologies /[/1/7 /, /1/8/]/."
- PAPER2026ZADUREF10-E12 | page: 4, section: extracted, quote: "Here it should su/ce to giv e only a short accoun t of the algorithm whic h will pro vide the notation used in the subsequen t c hapters/."
