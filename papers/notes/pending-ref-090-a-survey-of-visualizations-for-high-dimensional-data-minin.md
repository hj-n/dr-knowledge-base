---
id: paper-2002-pending-ref-090
title: "A survey of visualizations for high-dimensional data mining"
authors: "P. Hoffman and G. Grinstein"
venue: "Nature Methods"
year: 2002
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-090-2002-a-survey-of-visualizations-for-high-dimensional-data-mining.pdf
seed_note_id: "paper-2021-quantitative-survey-dr-techniques"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- A presolve routine80 solves trivial problems and otherwise per - forms problem simplifications, such as bound tightening and removal of fixed variables, and one of several routines for elimi - nating redundant equality constraints is automatically chosen to reduce the chance of numerical difficulties caused by singular matrices.
- Although the main solver implementation is pure Python, end-to-end sparse matrix support and heavy use of SciPy’s compiled linear system solvers—often for the same system with multiple right hand sides owing to the predictor-corrector approach—provide speed sufficient for problems with tens of thousands of variables and constraints.
- SciPy includes algorithms for optimization, integration, interpolation, eigenvalue problems, algebraic equations, differential equations and many other classes of problems; it also provides specialized data struc - tures, such as sparse matrices and k-dimensional trees.
- 39A list of members and affiliations appears at the end of the paper. *e-mail: scipy.articles@gmail.com S ciPy is a library of numerical routines for the Python programming language that provides fundamental building blocks for modeling and solving scientific problems.

# Method Summary
- The scope of the SciPy library narrowed, while the breadth of the eco - system grew through a new type of auxiliary package: the scikit (https://www.scipy.org/scikits.html), a complementary library developed outside SciPy, allowing for more rapid exploration of experimental ideas while maintaining familiar style and develop - ment methodology.
- Although the main solver implementation is pure Python, end-to-end sparse matrix support and heavy use of SciPy’s compiled linear system solvers—often for the same system with multiple right hand sides owing to the predictor-corrector approach—provide speed sufficient for problems with tens of thousands of variables and constraints.
- There are amendments to this paper NATuRE METHODS | VOL 17 | MARCH 2020 | 261–272 | www.nature.com/ naturemethods 261 PersPective NaTure MeThodS implementation, documentation and testing, and a culture eager to learn and adopt better practices—both for community management and software development.
- Travis Oliphant, a PhD student at the Mayo Clinic, released a number of packages 17,18 that built on top of the Numeric array package, and provided algorithms for signal processing, special functions, sparse matrices, quadrature, optimization, fast Fourier transforms and more.
- SciPy includes algorithms for optimization, integration, interpolation, eigenvalue problems, algebraic equations, differential equations and many other classes of problems; it also provides specialized data struc - tures, such as sparse matrices and k-dimensional trees.
- We often use Cython as a glue between well-established, low-level scientific NATuRE METHODS | VOL 17 | MARCH 2020 | 261–272 | www.nature.com/ naturemethods264 PersPectiveNaTure MeThodS computing libraries written in C/C++ and the Python inter - face offered by SciPy.
- Since its initial release in 2001, SciPy has become a de facto standard for leveraging scientific algorithms in Python, with over 600 unique code contributors, thousands of dependent packages, over 100,000 dependent repositories and millions of downloads per year.

# When To Use / Not Use
- Use when:
  - In the early SciPy workshops, recurrent topics reflected the state of development, with emphasis being placed on the underlying array package, plotting, parallel processing, acceleration/wrapping and user interfaces.
  - These low-level interfaces for Cython can also be used outside of the SciPy codebase to gain access to the functions in the wrapped libraries while avoiding the overhead of Python function calls.
- Avoid when:
  - Although the main solver implementation is pure Python, end-to-end sparse matrix support and heavy use of SciPy’s compiled linear system solvers—often for the same system with multiple right hand sides owing to the predictor-corrector approach—provide speed sufficient for problems with tens of thousands of variables and constraints.
  - A presolve routine80 solves trivial problems and otherwise per - forms problem simplifications, such as bound tightening and removal of fixed variables, and one of several routines for elimi - nating redundant equality constraints is automatically chosen to reduce the chance of numerical difficulties caused by singular matrices.
- Failure modes:
  - In 1995, Jim Hugunin, a graduate student at the Massachusetts Institute of Technology, wrote the first message in a new Python Matrix Special Interest Group (Matrix-SIG) mailing list 14: “There seems to be a fair amount of interest in the Python community concerning the addition of numeric operations to Python.

# Metrics Mentioned
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- Travis Oliphant, a PhD student at the Mayo Clinic, released a number of packages 17,18 that built on top of the Numeric array package, and provided algorithms for signal processing, special functions, sparse matrices, quadrature, optimization, fast Fourier transforms and more.
- SciPy includes algorithms for optimization, integration, interpolation, eigenvalue problems, algebraic equations, differential equations and many other classes of problems; it also provides specialized data struc - tures, such as sparse matrices and k-dimensional trees.
- The C libraries that we wrap in SciPy include trlib62 for optimization, SuperLU63,64 for solving sparse linear systems, Qhull65 for computational geometry and Cephes (http://www.netlib.org/ cephes/) for special functions.
- Four new methods for unconstrained optimization were added to minimize in recent versions of SciPy: dogleg, trust-ncg, trust-exact and trust-krylov.
- The scipy.optimize subpackage provides functions for the numerical solution of several classes of root finding and optimization problems.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-090-C1 | stance: support | summary: A presolve routine80 solves trivial problems and otherwise per - forms problem simplifications, such as bound tightening and removal of fixed variables, and one of several routines for elimi - nating redundant equality constraints is automatically chosen to reduce the chance of numerical difficulties caused by singular matrices. | evidence_ids: PENDING-REF-090-E1, PENDING-REF-090-E2
- CLAIM-PENDING-REF-090-C2 | stance: support | summary: The scope of the SciPy library narrowed, while the breadth of the eco - system grew through a new type of auxiliary package: the scikit (https://www.scipy.org/scikits.html), a complementary library developed outside SciPy, allowing for more rapid exploration of experimental ideas while maintaining familiar style and develop - ment methodology. | evidence_ids: PENDING-REF-090-E3, PENDING-REF-090-E4
- CLAIM-PENDING-REF-090-C3 | stance: support | summary: Travis Oliphant, a PhD student at the Mayo Clinic, released a number of packages 17,18 that built on top of the Numeric array package, and provided algorithms for signal processing, special functions, sparse matrices, quadrature, optimization, fast Fourier transforms and more. | evidence_ids: PENDING-REF-090-E5, PENDING-REF-090-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance
- step: 6 | relevance: high | note: guides reliable interpretation of projected views

# Evidence
- PENDING-REF-090-E1 | page: 6, section: extracted, quote: "A presolve routine80 solves trivial problems and otherwise per - forms problem simplifications, such as bound tightening and removal of fixed variables, and one of several routines for elimi - nating redundant equality constraints is automatically chosen to reduce the chance of numerical difficulties caused by singular matrices."
- PENDING-REF-090-E2 | page: 6, section: extracted, quote: "Although the main solver implementation is pure Python, end-to-end sparse matrix support and heavy use of SciPy’s compiled linear system solvers—often for the same system with multiple right hand sides owing to the predictor-corrector approach—provide speed sufficient for problems with tens of thousands of variables and constraints."
- PENDING-REF-090-E3 | page: 1, section: extracted, quote: "SciPy includes algorithms for optimization, integration, interpolation, eigenvalue problems, algebraic equations, differential equations and many other classes of problems; it also provides specialized data struc - tures, such as sparse matrices and k-dimensional trees."
- PENDING-REF-090-E4 | page: 1, section: extracted, quote: "39A list of members and affiliations appears at the end of the paper. *e-mail: scipy.articles@gmail.com S ciPy is a library of numerical routines for the Python programming language that provides fundamental building blocks for modeling and solving scientific problems."
- PENDING-REF-090-E5 | page: 4, section: extracted, quote: "The scope of the SciPy library narrowed, while the breadth of the eco - system grew through a new type of auxiliary package: the scikit (https://www.scipy.org/scikits.html), a complementary library developed outside SciPy, allowing for more rapid exploration of experimental ideas while maintaining familiar style and develop - ment methodology."
- PENDING-REF-090-E6 | page: 1, section: extracted, quote: "There are amendments to this paper NATuRE METHODS / VOL 17 / MARCH 2020 / 261–272 / www.nature.com/ naturemethods 261 PersPective NaTure MeThodS implementation, documentation and testing, and a culture eager to learn and adopt better practices—both for community management and software development."
- PENDING-REF-090-E7 | page: 2, section: extracted, quote: "Travis Oliphant, a PhD student at the Mayo Clinic, released a number of packages 17,18 that built on top of the Numeric array package, and provided algorithms for signal processing, special functions, sparse matrices, quadrature, optimization, fast Fourier transforms and more."
- PENDING-REF-090-E8 | page: 4, section: extracted, quote: "We often use Cython as a glue between well-established, low-level scientific NATuRE METHODS / VOL 17 / MARCH 2020 / 261–272 / www.nature.com/ naturemethods264 PersPectiveNaTure MeThodS computing libraries written in C/C++ and the Python inter - face offered by SciPy."
