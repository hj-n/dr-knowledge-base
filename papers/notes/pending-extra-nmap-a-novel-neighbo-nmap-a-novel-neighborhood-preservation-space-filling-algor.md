---
id: paper-2026-pending-extra-nmap-a-novel-neighbo
title: "Nmap: A Novel Neighborhood Preservation Space-filling Algorithm"
authors: "Felipe S. L. G. Duarte, Fabio Sikansi, Francisco M. Fatore, Samuel G. Fadel, Fernando V. Paulovich"
venue: "IEEE Transactions on Visualization and Computer Graphics"
year: 2014
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/Nmap_A_Novel_Neighborhood_Preservation_Space-filling_Algorithm.pdf
seed_note_id: "paper-2019-mdp-visual-analytics-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- 3S LICE AND SCALE TREEMAP ALGORITHM Neighborhood Map (Nmap) tackles the problem of preserving distance-similarity relationships when constructing a Treemap using an approach that consecutively bisects the available area and scales the resulting bisections.
- Tak and Cockburn [18] tackle this problem by recursively splitting the visual space into quadrants, therefore rectangular areas, which are positioned following a Hilbert or Moore curve of level zero.
- Thereby, not only better representing the distance-similarity metaphor and reducing problems associated on violating that, but also being able to handle large datasets in real time.
- One of the few approaches that seek to overcome this problem is the Spatially-Ordered Treemap (SOT) [24].

# Method Summary
- In this paper, we propose a novel approach, called Neighborhood T reemap (Nmap), that seeks to solve this limitation by employing a slice and scale strategy where the visual space is successively bisected on the horizontal or vertical directions and the bisections are scaled until one rectangle is deﬁned per data element.
- 3S LICE AND SCALE TREEMAP ALGORITHM Neighborhood Map (Nmap) tackles the problem of preserving distance-similarity relationships when constructing a Treemap using an approach that consecutively bisects the available area and scales the resulting bisections.
- Although a simple approach, the Nmap surpass techniques that are adaptations of an algorithm (Squariﬁed Treemap) which is know to render rectangles with very good aspect-ratio.
- 6C ONCLUSIONS In this paper we proposed a novel rectangular Treemap algorithm called Neighborhood Treemap (Nmap).
- Although this process of creating clusters inside cluster deﬁnes a hierarchy of groups and subgroups based on a clustering algorithm, the Nmap strategies can also be used to represent any given hierarchy, being independent of this cluster-based organization.
- This is a parameter that the user can change, according to his/her expertise about the dataset under analysis, using some metadata information available, or employing an algorithm to automatically estimate the number of groups/clusters [8].
- E-mail: {felipelageduarte, fhenrique, fmfatore, samuel.fadel}@usp.br and paulovic@icmc.usp.br different algorithms have been proposed, however the core idea is the same, to split the visual space into rectangles following some criteria.

# When To Use / Not Use
- Use when:
  - In this paper, we propose a novel approach, called Neighborhood T reemap (Nmap), that seeks to solve this limitation by employing a slice and scale strategy where the visual space is successively bisected on the horizontal or vertical directions and the bisections are scaled until one rectangle is deﬁned per data element.
  - Although this process of creating clusters inside cluster deﬁnes a hierarchy of groups and subgroups based on a clustering algorithm, the Nmap strategies can also be used to represent any given hierarchy, being independent of this cluster-based organization.
- Avoid when:
  - This representation allows users to browse document collection into different levels of abstraction, starting with a high-level view and successively detailing the areas of interest until the documents are presented, speeding-up this exploratory process.
  - This is a parameter that the user can change, according to his/her expertise about the dataset under analysis, using some metadata information available, or employing an algorithm to automatically estimate the number of groups/clusters [8].
- Failure modes:
  - In general, the Nmap strategies produced layouts that best preserves the shape and neighborhoods of the initial conﬁgurations, achieving a more reliable representation of the distance-similarity metaphor.

# Metrics Mentioned
- `continuity`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- This is a parameter that the user can change, according to his/her expertise about the dataset under analysis, using some metadata information available, or employing an algorithm to automatically estimate the number of groups/clusters [8].
- 3S LICE AND SCALE TREEMAP ALGORITHM Neighborhood Map (Nmap) tackles the problem of preserving distance-similarity relationships when constructing a Treemap using an approach that consecutively bisects the available area and scales the resulting bisections.
- Although a simple approach, the Nmap surpass techniques that are adaptations of an algorithm (Squariﬁed Treemap) which is know to render rectangles with very good aspect-ratio.
- 6C ONCLUSIONS In this paper we proposed a novel rectangular Treemap algorithm called Neighborhood Treemap (Nmap).
- Although this process of creating clusters inside cluster deﬁnes a hierarchy of groups and subgroups based on a clustering algorithm, the Nmap strategies can also be used to represent any given hierarchy, being independent of this cluster-based organization.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-EXTRA-C1 | stance: support | summary: 3S LICE AND SCALE TREEMAP ALGORITHM Neighborhood Map (Nmap) tackles the problem of preserving distance-similarity relationships when constructing a Treemap using an approach that consecutively bisects the available area and scales the resulting bisections. | evidence_ids: PENDING-EXTRA-E1, PENDING-EXTRA-E2
- CLAIM-PENDING-EXTRA-C2 | stance: support | summary: In this paper, we propose a novel approach, called Neighborhood T reemap (Nmap), that seeks to solve this limitation by employing a slice and scale strategy where the visual space is successively bisected on the horizontal or vertical directions and the bisections are scaled until one rectangle is deﬁned per data element. | evidence_ids: PENDING-EXTRA-E3, PENDING-EXTRA-E4
- CLAIM-PENDING-EXTRA-C3 | stance: support | summary: This is a parameter that the user can change, according to his/her expertise about the dataset under analysis, using some metadata information available, or employing an algorithm to automatically estimate the number of groups/clusters [8]. | evidence_ids: PENDING-EXTRA-E5, PENDING-EXTRA-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance
- step: 6 | relevance: high | note: guides reliable interpretation of projected views

# Evidence
- PENDING-EXTRA-E1 | page: 2, section: extracted, quote: "3S LICE AND SCALE TREEMAP ALGORITHM Neighborhood Map (Nmap) tackles the problem of preserving distance-similarity relationships when constructing a Treemap using an approach that consecutively bisects the available area and scales the resulting bisections."
- PENDING-EXTRA-E2 | page: 2, section: extracted, quote: "Tak and Cockburn [18] tackle this problem by recursively splitting the visual space into quadrants, therefore rectangular areas, which are positioned following a Hilbert or Moore curve of level zero."
- PENDING-EXTRA-E3 | page: 8, section: extracted, quote: "Thereby, not only better representing the distance-similarity metaphor and reducing problems associated on violating that, but also being able to handle large datasets in real time."
- PENDING-EXTRA-E4 | page: 2, section: extracted, quote: "One of the few approaches that seek to overcome this problem is the Spatially-Ordered Treemap (SOT) [24]."
- PENDING-EXTRA-E5 | page: 1, section: extracted, quote: "In this paper, we propose a novel approach, called Neighborhood T reemap (Nmap), that seeks to solve this limitation by employing a slice and scale strategy where the visual space is successively bisected on the horizontal or vertical directions and the bisections are scaled until one rectangle is deﬁned per data element."
- PENDING-EXTRA-E6 | page: 6, section: extracted, quote: "Although a simple approach, the Nmap surpass techniques that are adaptations of an algorithm (Squariﬁed Treemap) which is know to render rectangles with very good aspect-ratio."
- PENDING-EXTRA-E7 | page: 8, section: extracted, quote: "6C ONCLUSIONS In this paper we proposed a novel rectangular Treemap algorithm called Neighborhood Treemap (Nmap)."
- PENDING-EXTRA-E8 | page: 8, section: extracted, quote: "Although this process of creating clusters inside cluster deﬁnes a hierarchy of groups and subgroups based on a clustering algorithm, the Nmap strategies can also be used to represent any given hierarchy, being independent of this cluster-based organization."
