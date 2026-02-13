# Preprocessing Profiles

Use this page to standardize preprocessing before method comparison.
The goal is to reduce protocol drift and improve reproducibility.

Related:
- Workflow anchor: [`docs/workflow/dr-analysis-workflow.md`](./dr-analysis-workflow.md)
- Reliability cautions: [`docs/reliability-cautions-and-tips.md`](../reliability-cautions-and-tips.md)

## Universal Rules
- remove exact duplicates unless duplicates represent true count semantics
- choose one distance definition and keep it fixed during comparison
- record missing-value handling explicitly
- keep one preprocessing setup fixed before tuning starts

## Profile A: Dense Numeric Features
Use for continuous numeric features.

Defaults:
- imputation: median or robust feature-wise strategy
- scaling: z-score or robust scaler
- distance default: Euclidean

Notes:
- without scaling, distance behavior can become unstable
- if clipping is used, record bounds because neighborhoods may change

## Profile B: Sparse or Count-Like Features
Use for bag-of-words, count vectors, or high sparsity.

Defaults:
- transform: log1p or TF-IDF style normalization
- scaling: avoid dense standardization that destroys sparsity
- distance default: cosine (or correlation when justified)
- optional: truncated SVD before nonlinear DR for efficiency

Notes:
- Euclidean distance on raw sparse counts is often misleading
- document whether zeros mean absence or missingness

## Profile C: Pretrained Embeddings
Use when input is already an embedding.

Defaults:
- normalization: L2 normalize unless model contract forbids it
- distance default: cosine
- deduplication: remove exact duplicates

Notes:
- mixing normalized and unnormalized vectors invalidates comparisons
- record embedding model/version to control representation drift

## Profile D: Labeled Data with Class-Aware Evaluation
Use when class-aware checks are part of evaluation.

Additional requirements:
- evaluate baseline label separation in original space
- if separability is weak or unknown, lower confidence for class-aware conclusions
- keep at least one label-agnostic check in final comparison

## Record Keeping
Keep a short reproducibility record for:
- selected preprocessing profile
- distance definition
- missing-value policy
- scaling policy
- duplicate policy
- compact preprocessing summary string

Example summary:
`profile=B;transform=log1p+tfidf;distance=cosine;dedup=exact;seed=42`
