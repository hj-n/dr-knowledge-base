# Preprocessing Profiles

Use this page to standardize preprocessing before technique and metric comparison.
The objective is to reduce protocol drift and make DR recommendations reproducible.

Related:
- Workflow step: [`docs/workflow/dr-analysis-workflow.md`](./dr-analysis-workflow.md)
- Reliability cautions: [`docs/reliability-cautions-and-tips.md`](../reliability-cautions-and-tips.md)

## Universal Controls (All Data Types)
- Remove exact duplicate rows unless duplicates encode count semantics.
- Define one distance metric and keep it fixed during method comparison.
- Record missing-value policy explicitly.
- Freeze preprocessing policy before hyperparameter optimization.

## Profile A: Dense Numeric Features
Use when features are continuous numeric values.

Required defaults:
- imputation: median (or feature-wise robust strategy)
- scaling: z-score or robust scaler
- outlier handling: clip to robust percentile bounds only if required
- distance default: Euclidean

Reliability notes:
- If feature scales differ and no scaling is applied, distance-based DR behavior becomes unstable.
- If clipping is used, record bounds because neighborhood structure can change materially.

## Profile B: Sparse / Count-like Features
Use for bag-of-words, count matrices, or highly sparse vectors.

Required defaults:
- transform: log1p or TF-IDF style normalization (task dependent)
- scaling: avoid dense standardization that destroys sparsity
- distance default: cosine (or correlation) unless domain-specific requirement exists
- optional reduction: truncated SVD before nonlinear DR for efficiency

Reliability notes:
- Euclidean distance on raw sparse counts can produce misleading neighborhoods.
- Document whether zero entries represent missingness or true absence.

## Profile C: Pretrained Embeddings
Use when input is already an embedding from another model.

Required defaults:
- normalization: L2-normalize vectors unless model contract forbids it
- distance default: cosine
- deduplication: remove exact duplicates to avoid artificial density spikes

Reliability notes:
- Mixing normalized and unnormalized embeddings in one run invalidates comparisons.
- Record embedding model/version because representation drift can dominate DR effects.

## Profile D: Labeled Data with Class-Aware Metrics
Use when class-aware metrics may be evaluated.

Additional required checks:
- evaluate baseline label separability in original space
- if separability is weak/unknown, mark label-separation check as `fail` or `unknown`
- keep at least one label-agnostic metric in final bundle

## Output Contract
Step 2 must output:
- `preprocessing_profile_id` (`A|B|C|D` with combinations if needed)
- `distance_metric`
- `missing_value_policy`
- `scaling_policy`
- `duplicate_policy`
- `frozen_preprocessing_signature` (short reproducibility string)

## Minimal Signature Example
```text
frozen_preprocessing_signature: profile=B;transform=log1p+tfidf;distance=cosine;dedup=exact;seed=42
```
