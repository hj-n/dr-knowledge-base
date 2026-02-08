---
id: paper-1999-pending-ref-089
title: "A new method of generalizing Sammon mapping with application to algorithm speed-up"
authors: "E. Pekalska, D. de Ridder, R. P. W. Duin, and M. A. Kraaijveld"
venue: "IEEE Transactions on Pattern Analysis and Machine Intelligence"
year: 1999
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-089-1999-a-new-method-of-generalizing-sammon-mapping-with-application-to-algorithm-speed-up.pdf
seed_note_id: "paper-2019-mdp-visual-analytics-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- For kernel-based methods, due to the implicit high-dimensional nonlinear mapping determined by kernel, many typical “large sample size” problems in observation space, such as handwritten digit recognition, are turned into SSS problems infeature space.
- However, it is difficult to do so directly because it is computationally very intensive to compute the dot products in a high-dimensional feature space .
- To avoid this difficulty, the present KFD algorithms [4], [6], [7] all formulate the problem in the space spanned by the mapped training samples.
- Several ways suggested by Mika et al. [10] and Burges and Scho¨ lkopf [45] can be used to deal with this problem, but the optimal implementation scheme (e.g., developing a more efficient numerical algorithm for large scale eigenproblems) is still open.

# Method Summary
- Thus, in Hilbert space H, the Fisher criterion function can be defined by J/C8 ð’ Þ¼ ’ TS/C8 b ’ ’ TS/C8 w’ ;’ 6¼ 0: ð11Þ If the within-class scatter operator S/C8 w is invertible, ’ TS/C8 w’> 0 always holds for every nonzero vector ’ .I n such a case, the Fisher criterion can be directly employed to extract a set of optimal discriminant vectors (projection axes) using the standard LDA algorithm [35].
- In the phase of model selection, our goal is to determine proper kernel parameters (i.e., the order r of the polynomial kernel and the width /C14 of the Gaussian RBF kernel), the dimension of the projection subspace for each method, and the fusion coefficient /C18 for CKFD.
- One is the polynomial kernel kðx; yÞ¼ð x /C1y þ 1Þ r and the other is the Gaussian RBF kernel kðx; yÞ¼ expð/C0jj x /C0 yjj2=/C14 Þ .T h r e e methods, namely, Kernel Eigenface [11], Kernel Fisherface [11], and the proposed CKFD algorithm, are tested and compared.
- Like Liu et al.’s [21] method, our previous LDA algorithm [ 2 4 ]c a no b t a i nm o r et h a n c /C0 1 features, that is, all c /C0 1 irregular discriminant features plus some regular ones.
- In Section 5, the experiments are performed on the FERET face database and CENPARMI handwritten numeral database whereby the proposed algorithm is evaluated and compared to other methods.
- 4.4 Relationship to Other KFD (or LDA) Algorithms In this section, we will review some other KFD (LDA) methods and explicitly distinguish them from the proposed CKFD.
- This algorithm turned out to be more effective than Chen and Yu’s methods, which can extract at most c /C0 1 features.

# When To Use / Not Use
- Use when:
  - In such a case, the Fisher criterion degenerates into the following between-class scatter criterion: J /C8 b ð’ Þ¼ ’ TS/C8 b ’; ðjj’ jj ¼ 1Þ: ð12Þ As a special case of the Fisher criterion, the criterion given in (12) is very intuitive since it is reasonable to use the betweenclass scatter to measure the discriminatory ability of a projection axis when the within-class scatter is zero [22], [24].
  - In this paper, we will use the between-class scatter criterion defined in (12) to derive the irregular discriminant vectors from nullðS /C8 wÞ (i.e., the null space of S/C8 w), while using the standard Fisher criterion defined in (11) to derive the regular discriminant vectors from the complementary set H/C0 nullðS/C8 wÞ.
- Avoid when:
  - Taking kernel Fisherface as an example, we can first use KPCA to reduce the dimension to l (note that here only l components are used; l is subject to c /C20 l /C20 M /C0 c, where M is the number of training samples and c is the number of classes) and then perform standard LDA in the KPCAtransformed space.
  - Several ways suggested by Mika et al. [10] and Burges and Scho¨ lkopf [45] can be used to deal with this problem, but the optimal implementation scheme (e.g., developing a more efficient numerical algorithm for large scale eigenproblems) is still open.
- Failure modes:
  - In order to gain more insights into our algorithm, two additional versions, 1) CKFD: regular, where only the regular discriminant features are used, and 2) CKFD:irregular, where only the irregular discriminant features are used, are also evaluated.

# Metrics Mentioned
- `stress`: referenced as part of projection-quality or reliability assessment.
- `neighborhood-preservation criteria`: referenced as part of projection-quality or reliability assessment.
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- In the phase of model selection, our goal is to determine proper kernel parameters (i.e., the order r of the polynomial kernel and the width /C14 of the Gaussian RBF kernel), the dimension of the projection subspace for each method, and the fusion coefficient /C18 for CKFD.
- Images of one person in the FERET database. (a) Original images. (b) Cropped images (after histogram equalization) corresponding to images in (a). interval where the optimal parameters might exist.
- 3a and 3c show the recognition accuracy versus the variation of kernel parameters corresponding to four methods with a fixed dimension of 20 and /C18 ¼ 1 for CKFD.
- Specifically, we fix the dimension and the fusion coefficient (only for CKFD) in advance and try to find the optimal kernel parameter for a given kernel function.
- After globally searching over a wide range of the parameter space, we find a candidate 236 IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE, VOL.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-089-C1 | stance: support | summary: For kernel-based methods, due to the implicit high-dimensional nonlinear mapping determined by kernel, many typical “large sample size” problems in observation space, such as handwritten digit recognition, are turned into SSS problems infeature space. | evidence_ids: PENDING-REF-089-E1, PENDING-REF-089-E2
- CLAIM-PENDING-REF-089-C2 | stance: support | summary: Thus, in Hilbert space H, the Fisher criterion function can be defined by J/C8 ð’ Þ¼ ’ TS/C8 b ’ ’ TS/C8 w’ ;’ 6¼ 0: ð11Þ If the within-class scatter operator S/C8 w is invertible, ’ TS/C8 w’> 0 always holds for every nonzero vector ’ .I n such a case, the Fisher criterion can be directly employed to extract a set of optimal discriminant vectors (projection axes) using the standard LDA algorithm [35]. | evidence_ids: PENDING-REF-089-E3, PENDING-REF-089-E4
- CLAIM-PENDING-REF-089-C3 | stance: support | summary: In the phase of model selection, our goal is to determine proper kernel parameters (i.e., the order r of the polynomial kernel and the width /C14 of the Gaussian RBF kernel), the dimension of the projection subspace for each method, and the fusion coefficient /C18 for CKFD. | evidence_ids: PENDING-REF-089-E5, PENDING-REF-089-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-REF-089-E1 | page: 1, section: extracted, quote: "For kernel-based methods, due to the implicit high-dimensional nonlinear mapping determined by kernel, many typical “large sample size” problems in observation space, such as handwritten digit recognition, are turned into SSS problems infeature space."
- PENDING-REF-089-E2 | page: 2, section: extracted, quote: "However, it is difficult to do so directly because it is computationally very intensive to compute the dot products in a high-dimensional feature space ."
- PENDING-REF-089-E3 | page: 3, section: extracted, quote: "To avoid this difficulty, the present KFD algorithms [4], [6], [7] all formulate the problem in the space spanned by the mapped training samples."
- PENDING-REF-089-E4 | page: 13, section: extracted, quote: "Several ways suggested by Mika et al. [10] and Burges and Scho¨ lkopf [45] can be used to deal with this problem, but the optimal implementation scheme (e.g., developing a more efficient numerical algorithm for large scale eigenproblems) is still open."
- PENDING-REF-089-E5 | page: 3, section: extracted, quote: "Thus, in Hilbert space H, the Fisher criterion function can be defined by J/C8 ð’ Þ¼ ’ TS/C8 b ’ ’ TS/C8 w’ ;’ 6¼ 0: ð11Þ If the within-class scatter operator S/C8 w is invertible, ’ TS/C8 w’> 0 always holds for every nonzero vector ’ .I n such a case, the Fisher criterion can be directly employed to extract a set of optimal discriminant vectors (projection axes) using the standard LDA algorithm [35]."
- PENDING-REF-089-E6 | page: 7, section: extracted, quote: "In the phase of model selection, our goal is to determine proper kernel parameters (i.e., the order r of the polynomial kernel and the width /C14 of the Gaussian RBF kernel), the dimension of the projection subspace for each method, and the fusion coefficient /C18 for CKFD."
- PENDING-REF-089-E7 | page: 7, section: extracted, quote: "One is the polynomial kernel kðx; yÞ¼ð x /C1y þ 1Þ r and the other is the Gaussian RBF kernel kðx; yÞ¼ expð/C0jj x /C0 yjj2=/C14 Þ .T h r e e methods, namely, Kernel Eigenface [11], Kernel Fisherface [11], and the proposed CKFD algorithm, are tested and compared."
- PENDING-REF-089-E8 | page: 6, section: extracted, quote: "Like Liu et al.’s [21] method, our previous LDA algorithm [ 2 4 ]c a no b t a i nm o r et h a n c /C0 1 features, that is, all c /C0 1 irregular discriminant features plus some regular ones."
