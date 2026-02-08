---
id: paper-2023-pending-ref-143
title: "V a embeddings star: A state-of-the-art report on the use of embeddings in visual analytics"
authors: "Z. Huang, D. Witschard, K. Kucher, and A. Kerren"
venue: "Journal of Physics: Condensed Matter"
year: 2023
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-143-2023-v-a-embeddings-star-a-state-of-the-art-report-on-the-use-of-embeddings-in-visual-anal.pdf
seed_note_id: "paper-2025-critical-analysis-dr-four-domains"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- Short description of Q UANTUM ESPRESSO QUANTUM ESPRESSO implements a variety of methods and algorithms aimed at a chemically realistic modeling of materials from the nanoscale upwards, based on the solution QUANTUM ESPRESSO 9 of the density-functional theory (DFT) [2, 3] problem, using a plane waves (PW) basis set and pseudopotentials (PP) [32] to represent electron-ion interactions.
- The distribution can even be redundant, with different applications addressing the same problem in different ways; at the end, the sole requirements that Q UANTUM ESPRESSO components must fulﬁll are that:i) they are distributed under the same GPL license agreement [20] as the other Q UANTUM ESPRESSO components; ii) they are fully interoperable with the other components.
- The eigenvalue problem is then solved in the QUANTUM ESPRESSO 26 2N-dimensional subspace spanned by the reduced basis set φ(0), formed by φ(0) i = ψ(0) i and φ(0) i+N = δψ (0) i : 2N∑ k=1 (Hjk− ϵiSjk)c(i) k = 0, (A.10) where Hjk =⟨φ(0) j |H|φ(0) k ⟩, S jk =⟨φ(0) j |S|φ(0) k ⟩. (A.11) Conventional algorithms for matrix diagonalization are used in this step.
- Their success has been made possible by a combination of competences, ranging from the ability to address meaningful and challenging problems, to a rigorous insight into theoretical methods, ending with a marked sensibility to matters of numerical accuracy and algorithmic efﬁciency.

# Method Summary
- Short description of Q UANTUM ESPRESSO QUANTUM ESPRESSO implements a variety of methods and algorithms aimed at a chemically realistic modeling of materials from the nanoscale upwards, based on the solution QUANTUM ESPRESSO 9 of the density-functional theory (DFT) [2, 3] problem, using a plane waves (PW) basis set and pseudopotentials (PP) [32] to represent electron-ion interactions.
- Their success has been made possible by a combination of competences, ranging from the ability to address meaningful and challenging problems, to a rigorous insight into theoretical methods, ending with a marked sensibility to matters of numerical accuracy and algorithmic efﬁciency.
- Q UANTUM ESPRESSO aims at promoting active cooperation between a vast and diverse community of scientists developing new methods and algorithms in electronic-structure theory and of end users interested in their application to the numerical simulation of materials and devices.
- Introduction The combination of methodological and algorithmic innovations and ever-increasing computer power is delivering a simulation revolution in materials modeling, starting from the nanoscale up to bulk materials and devices [1].
- Multiscale approaches, in particular, strive to combine methods with different accuracy and scope to describe different parts of a complex system, or phenomena occurring at different time and/or length scales.
- Emphasis is put onto the skills that are necessary to turn new ideas into new algorithms and onto the methods that are needed to validate the implementation and application of computer simulation methods.
- A solution can be found via an iterative procedure.PWscf uses an algorithm based on the modiﬁed Broyden method [88] in whichx contains the components of the charge density in reciprocal space.

# When To Use / Not Use
- Use when:
  - The two main goals of this project are to foster methodological innovation in the ﬁeld of electronic-structure simulations and to provide a wide and diverse community of end users with highly efﬁcient, robust, and user-friendly software implementing the most recent innovations in this ﬁeld.
  - The calculation of second-order derivatives of the energy works also for US PP [128, 129] and for all GGA ﬂavors [130, 131] used in PWscf and in CP.
- Avoid when:
  - Our general philosophy is rather that of an open distribution, i.e. an integrated suite of codes designed to be interoperable, much in the spirit of a Linux distribution, and thus built around a number ofcore componentsdesigned and maintained by a small group of core developers, plus a number of auxiliary/complementary codes designed, implemented, and maintained by members of a wider community of users.
  - The services so far available include source-code management software (CVS or SVN repository), mailing lists, public forums, bug tracking facilities, up/down-load space, and wiki pages for projects’ documentation. qe-forge is expected to be the main tool by which Q UANTUM ESPRESSO end users and external contributors can maintain Q UANTUM ESPRESSOrelated projects and make them available to the community.
- Failure modes:
  - High serial performance across different architectures is achieved by the systematic use of standardized mathematical libraries (BLAS, LAPACK [28], and FFTW [29]) for which highly optimized implementations exist on many platforms; when proprietary optimizations of these libraries are not available, the user can compile the library sources distributed with Q UANTUM ESPRESSO.

# Metrics Mentioned
- `stress`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- The starting set is typically obtained from the previous scf iteration, if available, and if not, from the previous time step, or optimization step, or from a superposition of atomic orbitals.
- At a given iteration we have ( − ¯h2 2m∇2 + Vext(r) + V (in)(r) ) ψi(r) = ϵiψi(r), (A.2) where ϵi and ψi are KS energies and orbitals respectively, i labels the occupied states, Vext is the sum of the PPs of atomic cores (written for simplicity as a local potential), the input Hartree and exchange-correlation potential V (in)(r) = VHxc[ρ(in)(r)] is a functional of the input charge density ρ(in).
- High serial performance across different architectures is achieved by the systematic use of standardized mathematical libraries (BLAS, LAPACK [28], and FFTW [29]) for which highly optimized implementations exist on many platforms; when proprietary optimizations of these libraries are not available, the user can compile the library sources distributed with Q UANTUM ESPRESSO.
- GIPAW The GIPAW code allows for the calculation of physical parameters measured by i) nuclear magnetic resonance (NMR) in insulators (the electric ﬁeld gradient (EFG) tensors and the chemical shift tensors), and by ii) electronic paramagnetic resonance (EPR) spectroscopy for paramagnetic defects in solids or in radicals (the hyperﬁne tensors and the g-tensor).
- Once the optimal linear combination of ρ(in) from previous iterations (typically 4 to 8) is determined, one adds a step in the new search direction that is, in the simplest case, a fraction of the optimal ∆ρ or, taking advantage of some approximate electronic screening[188], a preconditioned ∆ρ.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-143-C1 | stance: support | summary: Short description of Q UANTUM ESPRESSO QUANTUM ESPRESSO implements a variety of methods and algorithms aimed at a chemically realistic modeling of materials from the nanoscale upwards, based on the solution QUANTUM ESPRESSO 9 of the density-functional theory (DFT) [2, 3] problem, using a plane waves (PW) basis set and pseudopotentials (PP) [32] to represent electron-ion interactions. | evidence_ids: PENDING-REF-143-E1, PENDING-REF-143-E2
- CLAIM-PENDING-REF-143-C2 | stance: support | summary: Short description of Q UANTUM ESPRESSO QUANTUM ESPRESSO implements a variety of methods and algorithms aimed at a chemically realistic modeling of materials from the nanoscale upwards, based on the solution QUANTUM ESPRESSO 9 of the density-functional theory (DFT) [2, 3] problem, using a plane waves (PW) basis set and pseudopotentials (PP) [32] to represent electron-ion interactions. | evidence_ids: PENDING-REF-143-E3, PENDING-REF-143-E4
- CLAIM-PENDING-REF-143-C3 | stance: support | summary: The starting set is typically obtained from the previous scf iteration, if available, and if not, from the previous time step, or optimization step, or from a superposition of atomic orbitals. | evidence_ids: PENDING-REF-143-E5, PENDING-REF-143-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-REF-143-E1 | page: 8, section: extracted, quote: "Short description of Q UANTUM ESPRESSO QUANTUM ESPRESSO implements a variety of methods and algorithms aimed at a chemically realistic modeling of materials from the nanoscale upwards, based on the solution QUANTUM ESPRESSO 9 of the density-functional theory (DFT) [2, 3] problem, using a plane waves (PW) basis set and pseudopotentials (PP) [32] to represent electron-ion interactions."
- PENDING-REF-143-E2 | page: 5, section: extracted, quote: "The distribution can even be redundant, with different applications addressing the same problem in different ways; at the end, the sole requirements that Q UANTUM ESPRESSO components must fulﬁll are that:i) they are distributed under the same GPL license agreement [20] as the other Q UANTUM ESPRESSO components; ii) they are fully interoperable with the other components."
- PENDING-REF-143-E3 | page: 1, section: extracted, quote: "The eigenvalue problem is then solved in the QUANTUM ESPRESSO 26 2N-dimensional subspace spanned by the reduced basis set φ(0), formed by φ(0) i = ψ(0) i and φ(0) i+N = δψ (0) i : 2N∑ k=1 (Hjk− ϵiSjk)c(i) k = 0, (A.10) where Hjk =⟨φ(0) j /H/φ(0) k ⟩, S jk =⟨φ(0) j /S/φ(0) k ⟩. (A.11) Conventional algorithms for matrix diagonalization are used in this step."
- PENDING-REF-143-E4 | page: 3, section: extracted, quote: "Their success has been made possible by a combination of competences, ranging from the ability to address meaningful and challenging problems, to a rigorous insight into theoretical methods, ending with a marked sensibility to matters of numerical accuracy and algorithmic efﬁciency."
- PENDING-REF-143-E5 | page: 6, section: extracted, quote: "Q UANTUM ESPRESSO aims at promoting active cooperation between a vast and diverse community of scientists developing new methods and algorithms in electronic-structure theory and of end users interested in their application to the numerical simulation of materials and devices."
- PENDING-REF-143-E6 | page: 3, section: extracted, quote: "Introduction The combination of methodological and algorithmic innovations and ever-increasing computer power is delivering a simulation revolution in materials modeling, starting from the nanoscale up to bulk materials and devices [1]."
- PENDING-REF-143-E7 | page: 3, section: extracted, quote: "Multiscale approaches, in particular, strive to combine methods with different accuracy and scope to describe different parts of a complex system, or phenomena occurring at different time and/or length scales."
- PENDING-REF-143-E8 | page: 7, section: extracted, quote: "Emphasis is put onto the skills that are necessary to turn new ideas into new algorithms and onto the methods that are needed to validate the implementation and application of computer simulation methods."
