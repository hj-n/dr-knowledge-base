---
id: paper-2015-pending-ref-173
title: "Random projection-based dimensionality reduction method for hyperspectral target detection"
authors: "W. Feng, Q. Chen, W. He, G. R. Arce, G. Gu, and J. Zhuang"
venue: "Journal of Big Data"
year: 2015
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-173-2015-random-projection-based-dimensionality-reduction-method-for-hyperspectral-target-dete.pdf
seed_note_id: "paper-2017-random-projection-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- The selected papers were analyzed and reviewed to (1) list and define the DL approaches and network types, (2) list and explain CNN architectures, (3) present the challenges of DL and sug - gest the alternate solutions, (4) assess the applications of DL, (5) assess computational approaches.
- In comparison with tradi - tional supervised techniques, performing this learning is much more difficult, as no straightforward loss function is available in the reinforcement learning technique.
- In this paper, an overview of DL is presented that adopts various perspectives such as the main concepts, architectures, challenges, applications, computational tools and evolution matrix.
- The motivation behinds our review was to cover the most important aspect of DL including open challenges, applications, and computational tools perspective.

# Method Summary
- We additionally discuss the proposed solutions tackling these issues. • We provide an exhaustive list of medical imaging applications with deep learning by categorizing them based on the tasks by starting with classification and ending with registration. • We discuss the computational approaches (CPU, GPU, FPGA) by comparing the influence of each tool on deep learning algorithms.
- Therefore, in this contribution, we propose using a more holistic approach in order to provide a more suitable starting point from which to develop a full understanding of DL.
- The selected papers were analyzed and reviewed to (1) list and define the DL approaches and network types, (2) list and explain CNN architectures, (3) present the challenges of DL and sug - gest the alternate solutions, (4) assess the applications of DL, (5) assess computational approaches.
- Moreover, it has gradually become the most widely used computational approach in the field of ML, thus achiev‑ ing outstanding results on several complex cognitive tasks, matching or even beating those provided by human performance.
- Generalization: Different data types or different applications can use the same DL technique, an approach frequently referred to as transfer learning (TL) which explained in the latter section.
- Law - rence Livermore National Laboratory (LLNL), a large enterprise working on evolving frameworks for networks, adopted a similar approach, where thousands of nodes can be implemented [53].
- DL is designed using numerous layers of algorithms (artificial neural networks, or ANNs), each of which provides a different interpretation of the data that has been fed to them [18, 25].

# When To Use / Not Use
- Use when:
  - Frameworks and datasets Several DL frameworks and datasets have been developed in the last few years. vari - ous frameworks and libraries have also been used in order to expedite the work with good results.
  - Unlike conventional fully connected (FC) networks, shared weights and local connections in the CNN are employed to make full use of 2D input-data structures like image signals.
- Avoid when:
  - Convolutional neural network (CNN) is one of the most popular and used of DL networks [19, 20].
  - Furthermore, it is the most used in several applications among other networks.
- Failure modes:
  - Unlike conventional networks, RNN uses sequential data in the network.

# Metrics Mentioned
- `rank-based quality criteria`: referenced as part of projection-quality or reliability assessment.

# Implementation Notes
- Therefore, careful parameter selection is an extremely significant issue that should be considered during optimization scheme development. • Impressive and robust hardware resources like GPUs are required for effective CNN training.
- To alleviate this issue, TL and data augmentation have been researched over the last few years. • Although ML slowly transitions to semi-supervised and unsupervised learning to manage practical data without the need for manual human labeling, many of the current deep-learning models utilize supervised learning. • The CNN performance is greatly influenced by hyper-parameter selection.
- In addition, there are two essential differences between supervised learning and rein - forcement learning: first, there is no complete access to the function, which requires optimization, meaning that it should be queried via interaction; second, the state being interacted with is founded on an environment, where the input xt is based on the preceding actions [9 , 56].
- In addi - tion, the kernels are the basis of the local connections, which share similar parameters (bias bk and weight W k ) for generating k feature maps hk with a size of ( m − n − 1 ) each and are convolved with input, as mentioned above.
- The main reason to consider CNN is the weight sharing feature, which reduces the number of trainable network parameters and in turn helps the network to enhance generalization and to avoid overfitting.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-173-C1 | stance: support | summary: The selected papers were analyzed and reviewed to (1) list and define the DL approaches and network types, (2) list and explain CNN architectures, (3) present the challenges of DL and sug - gest the alternate solutions, (4) assess the applications of DL, (5) assess computational approaches. | evidence_ids: PENDING-REF-173-E1, PENDING-REF-173-E2
- CLAIM-PENDING-REF-173-C2 | stance: support | summary: We additionally discuss the proposed solutions tackling these issues. • We provide an exhaustive list of medical imaging applications with deep learning by categorizing them based on the tasks by starting with classification and ending with registration. • We discuss the computational approaches (CPU, GPU, FPGA) by comparing the influence of each tool on deep learning algorithms. | evidence_ids: PENDING-REF-173-E3, PENDING-REF-173-E4
- CLAIM-PENDING-REF-173-C3 | stance: support | summary: Therefore, careful parameter selection is an extremely significant issue that should be considered during optimization scheme development. • Impressive and robust hardware resources like GPUs are required for effective CNN training. | evidence_ids: PENDING-REF-173-E5, PENDING-REF-173-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 5 | relevance: high | note: provides hyperparameter sensitivity/optimization guidance

# Evidence
- PENDING-REF-173-E1 | page: 4, section: extracted, quote: "The selected papers were analyzed and reviewed to (1) list and define the DL approaches and network types, (2) list and explain CNN architectures, (3) present the challenges of DL and sug - gest the alternate solutions, (4) assess the applications of DL, (5) assess computational approaches."
- PENDING-REF-173-E2 | page: 10, section: extracted, quote: "In comparison with tradi - tional supervised techniques, performing this learning is much more difficult, as no straightforward loss function is available in the reinforcement learning technique."
- PENDING-REF-173-E3 | page: 2, section: extracted, quote: "In this paper, an overview of DL is presented that adopts various perspectives such as the main concepts, architectures, challenges, applications, computational tools and evolution matrix."
- PENDING-REF-173-E4 | page: 3, section: extracted, quote: "The motivation behinds our review was to cover the most important aspect of DL including open challenges, applications, and computational tools perspective."
- PENDING-REF-173-E5 | page: 3, section: extracted, quote: "We additionally discuss the proposed solutions tackling these issues. • We provide an exhaustive list of medical imaging applications with deep learning by categorizing them based on the tasks by starting with classification and ending with registration. • We discuss the computational approaches (CPU, GPU, FPGA) by comparing the influence of each tool on deep learning algorithms."
- PENDING-REF-173-E6 | page: 1, section: extracted, quote: "Therefore, in this contribution, we propose using a more holistic approach in order to provide a more suitable starting point from which to develop a full understanding of DL."
- PENDING-REF-173-E7 | page: 1, section: extracted, quote: "Moreover, it has gradually become the most widely used computational approach in the field of ML, thus achiev‑ ing outstanding results on several complex cognitive tasks, matching or even beating those provided by human performance."
- PENDING-REF-173-E8 | page: 9, section: extracted, quote: "Generalization: Different data types or different applications can use the same DL technique, an approach frequently referred to as transfer learning (TL) which explained in the latter section."
