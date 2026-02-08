---
id: paper-2003-pending-ref-117
title: "Random projection for high dimensional data clustering: A cluster ensemble approach"
authors: "X. Z. Fern and C. E. Brodley"
venue: "International Journal of Database Theory and Application"
year: 2003
tags: [dr, reliability, visual_analytics, reference, pending_references]
source_pdf: papers/raw/pending-references/pending-ref-117-2003-random-projection-for-high-dimensional-data-clustering-a-cluster-ensemble-approach.pdf
seed_note_id: "paper-2017-random-projection-survey"
evidence_level: medium
updated_at: 2026-02-08
---

# Problem
- It was demonstrated that the rep resentation depth is beneﬁcial for the classiﬁcation accuracy, and that state-of-the-art performance on the ImageNet challenge dataset can be achieved using a conventional ConvNet architecture (LeCun et al., 1989; Krizhevsky et al., 2012) with substantially increased depth.
- In this section, we present the image classiﬁcation results achieved by the described ConvNet architectures on the ILSVRC-2012 dataset (which was used for ILSVRC 2012–2014 challenges).

# Method Summary
- While more sophisticated methods of speeding up ConvNet tra ining have been recently proposed (Krizhevsky, 2014), which employ model and data parallelism for different layers of the net, we have found that our conceptually much simpler scheme already provides a speedup of3.75 times on an off-the-shelf 4-GPU system, as compared to using a sing le GPU.
- Even though in our case the 1 × 1 convolution is essentially a linear projection onto the space of the same dimensionality (the number of input and output channels is the same), an additional non-linearity is introduced by the rectiﬁcation function.
- The second approach to setting S is multi-scale training, where each training image is indiv idually rescaled by randomly sampling S from a certain range [Smin, Smax] (we used Smin = 256 and Smax = 512).
- In this section, we present the image classiﬁcation results achieved by the described ConvNet architectures on the ILSVRC-2012 dataset (which was used for ILSVRC 2012–2014 challenges).
- As can be seen, using multiple crops performs sl ightly better than dense evaluation, and the two approaches are indeed complementary, as their combination outperforms each of them.
- 3 C LASSIFICATION FRAMEWORK In the previous section we presented the details of our netwo rk conﬁgurations.
- We consider two approaches for setting the training scaleS.

# When To Use / Not Use
- Use when:
  - While we believe that in practice the increasedcomputation time of multiple crops does not justify the potential gains in accuracy, for reference we also evaluate our networks using50 crops per scale (5 × 5 regular grid with 2 ﬂips), for a total of 150 crops over 3 scales, which is comparable to 144 crops over 4 scales used by Szegedy et al. (2014).
  - We have made our two best-performing ConvNet models publicly a vailable to facilitate further research on the use of deep visual representations in computer vision.
- Avoid when:
  - This is remarkable, considering that our best result is achieved by combining just two models – signiﬁcantly less than used in most ILSVRC submissions.
  - As a result, we come up with signiﬁcantly more accurate ConvN et architectures, which not only achieve the state-of-the-art accuracy on ILSVRC classiﬁca tion and localisation tasks, but are also applicable to other image recognition datasets, where theyachieve excellent performance even when used as a part of a relatively simple pipelines (e.g. deep features classiﬁed by a linear SVM without ﬁne-tuning).
- Failure modes:
  - GoogLeNet (Szegedy et al., 2014), a top-performing entry of the ILSVRC-2014 classiﬁcation task, was developed independently of our work, but is similar in th at it is based on very deep ConvNets 3 Published as a conference paper at ICLR 2015 (22 weight layers) and small convolution ﬁlters (apart from 3 × 3, they also use 1 × 1 and 5 × 5 convolutions).

# Metrics Mentioned
- No explicit named metric was extracted from this source; combine this source with complementary DR quality checks in workflow Step 3.

# Implementation Notes
- We conjecture that in spite of the l arger number of parameters and the greater depth of our nets compared to (Krizhevsky et al., 2012), the nets required less epochs to converge due to (a) implicit regularisation imposed by greater depth and smaller conv. ﬁlter sizes; (b) pre-initialisation of certain layers.
- Second, we decrease the number of parameters: assuming that both the input and the output of a three-layer 3 × 3 convolution stack has C channels, the stack is parametrised by 3 ( 32C2) = 27C2 weights; at the same time, a single 7 × 7 conv. layer would require 72C2 = 49 C2 parameters, i.e.
- To this end, we ﬁx other parameters of the architecture, and steadily increase the depth of the network by adding more convolutional layers, wh ich is feasible due to the use of very small (3 × 3) convolution ﬁlters in all layers.
- To obtain the ﬁxed-size224× 224 ConvNet input images, they were randomly cropped from rescaled training images (one crop per image per SGD iteration).
- Network A,A-LRN B C D E Number of parameters 133 133 134 138 144 such layers have a 7 × 7 effective receptive ﬁeld.
- Keep preprocessing, initialization policy, and seed protocol fixed when comparing methods or parameter settings.

# Claim Atoms (For Conflict Resolution)
- CLAIM-PENDING-REF-117-C1 | stance: support | summary: It was demonstrated that the rep resentation depth is beneﬁcial for the classiﬁcation accuracy, and that state-of-the-art performance on the ImageNet challenge dataset can be achieved using a conventional ConvNet architecture (LeCun et al., 1989; Krizhevsky et al., 2012) with substantially increased depth. | evidence_ids: PENDING-REF-117-E1, PENDING-REF-117-E2
- CLAIM-PENDING-REF-117-C2 | stance: support | summary: While more sophisticated methods of speeding up ConvNet tra ining have been recently proposed (Krizhevsky, 2014), which employ model and data parallelism for different layers of the net, we have found that our conceptually much simpler scheme already provides a speedup of3.75 times on an off-the-shelf 4-GPU system, as compared to using a sing le GPU. | evidence_ids: PENDING-REF-117-E3, PENDING-REF-117-E4
- CLAIM-PENDING-REF-117-C3 | stance: support | summary: We conjecture that in spite of the l arger number of parameters and the greater depth of our nets compared to (Krizhevsky et al., 2012), the nets required less epochs to converge due to (a) implicit regularisation imposed by greater depth and smaller conv. ﬁlter sizes; (b) pre-initialisation of certain layers. | evidence_ids: PENDING-REF-117-E5, PENDING-REF-117-E6

# Workflow Relevance Map
- step: 1 | relevance: medium | note: supports explicit task clarification before DR recommendation
- step: 2 | relevance: medium | note: adds preprocessing/data-condition constraints for reliable comparison
- step: 3 | relevance: high | note: directly informs task-aligned method and metric selection
- step: 4 | relevance: high | note: contains initialization sensitivity or control-policy evidence

# Evidence
- PENDING-REF-117-E1 | page: 8, section: extracted, quote: "It was demonstrated that the rep resentation depth is beneﬁcial for the classiﬁcation accuracy, and that state-of-the-art performance on the ImageNet challenge dataset can be achieved using a conventional ConvNet architecture (LeCun et al., 1989; Krizhevsky et al., 2012) with substantially increased depth."
- PENDING-REF-117-E2 | page: 5, section: extracted, quote: "In this section, we present the image classiﬁcation results achieved by the described ConvNet architectures on the ILSVRC-2012 dataset (which was used for ILSVRC 2012–2014 challenges)."
- PENDING-REF-117-E3 | page: 5, section: extracted, quote: "While more sophisticated methods of speeding up ConvNet tra ining have been recently proposed (Krizhevsky, 2014), which employ model and data parallelism for different layers of the net, we have found that our conceptually much simpler scheme already provides a speedup of3.75 times on an off-the-shelf 4-GPU system, as compared to using a sing le GPU."
- PENDING-REF-117-E4 | page: 3, section: extracted, quote: "Even though in our case the 1 × 1 convolution is essentially a linear projection onto the space of the same dimensionality (the number of input and output channels is the same), an additional non-linearity is introduced by the rectiﬁcation function."
- PENDING-REF-117-E5 | page: 4, section: extracted, quote: "The second approach to setting S is multi-scale training, where each training image is indiv idually rescaled by randomly sampling S from a certain range [Smin, Smax] (we used Smin = 256 and Smax = 512)."
- PENDING-REF-117-E6 | page: 7, section: extracted, quote: "As can be seen, using multiple crops performs sl ightly better than dense evaluation, and the two approaches are indeed complementary, as their combination outperforms each of them."
- PENDING-REF-117-E7 | page: 4, section: extracted, quote: "3 C LASSIFICATION FRAMEWORK In the previous section we presented the details of our netwo rk conﬁgurations."
- PENDING-REF-117-E8 | page: 4, section: extracted, quote: "We consider two approaches for setting the training scaleS."
