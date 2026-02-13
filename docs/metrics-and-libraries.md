# Metrics and Libraries

Related:
- Workflow anchor: [`docs/workflow/dr-analysis-workflow.md`](./workflow/dr-analysis-workflow.md)
- Task confirmation: [`docs/workflow/task-confirmation-protocol.md`](./workflow/task-confirmation-protocol.md)
- Selection policy: [`docs/workflow/configuration-selection-policy.md`](./workflow/configuration-selection-policy.md)
- Metric catalog: [`docs/metrics/README.md`](./metrics/README.md)
- Metric similarity map: [`docs/metrics/metric-relationships.md`](./metrics/metric-relationships.md)
- Technique catalog: [`docs/techniques/README.md`](./techniques/README.md)
- Coverage ranking: [`docs/reference-coverage.md`](./reference-coverage.md)

## Purpose
Use this page to choose reliability checks and DR techniques that match the user's analysis goal.
Write recommendations in plain language. Do not expose internal mapping tables or key/value syntax in user answers.

## Default Evaluation Library
Use `zadu` as the default reliability-check library.
If a needed behavior is not covered, add an extra metric only when paper evidence is explicit.

## User-Layer Wording Rule
In end-user answers:
- use plain terms such as `main goal`, `reliability checks`, and `safety check`
- do not use internal mapping-table syntax in user prose
- when references are requested, cite papers (title, authors, venue, year, URL)

## Mandatory Label-Separation Check
Before using class-aware checks, verify that labels are reasonably separated in the original high-dimensional space.
If this assumption is weak or unknown, do not base the final recommendation on class-aware checks alone.

Class-aware checks include:
- Distance Consistency
- Internal Validation Measure
- Clustering-plus-External Validation Measure
- Neighborhood Hit
- Class-Aware Trustworthiness and Continuity

## Best/Optimal Selection Mode
When the user asks for the best or optimal DR configuration:
- compare all techniques aligned to the confirmed goal before pruning
- compare all aligned reliability checks before pruning
- allow exclusions only for hard failures, and record clear reasons

## Goal-Aligned Reliability Checks (Plain-Language Guide)
1. Neighborhood identification:
- prioritize local-neighborhood faithfulness checks
- cross-check with a global distortion check

2. Outlier identification:
- prioritize local-neighborhood checks that are sensitive to isolated points
- cross-check with a global distortion check

3. Cluster identification:
- combine local and cluster-level checks
- add one global check to avoid overfitting to local structure

4. Point-distance investigation:
- prioritize global distance-preservation checks
- add one local check to detect local collapse

5. Class-separability investigation:
- prioritize class-aware checks only after label-separation validation
- add label-agnostic local/global checks as safeguards

6. Cluster-distance investigation:
- prioritize checks that capture inter-cluster spacing and global ordering
- add one topology-oriented check

7. Cluster-density investigation:
- prioritize checks that reflect density and distance distortion
- add one local check so density conclusions do not hide neighborhood artifacts

## Goal-Aligned Technique Families (Plain-Language Guide)
1. Neighborhood identification:
- methods that preserve local neighborhoods (for example UMAP, t-SNE, PaCMAP, LLE, Laplacian Eigenmaps)

2. Outlier identification:
- local-structure methods that keep neighborhood detail visible (for example UMAP, t-SNE, LLE)

3. Cluster identification:
- methods that make local grouping behavior visible (for example UMAP, t-SNE, PaCMAP, SOM)

4. Point-distance investigation:
- methods that better preserve global distance relationships (for example PCA, MDS, Isomap, TriMap, UMATO)

5. Class-separability investigation:
- supervised or label-aware methods (for example ClassNeRV, Classimap, catSNE), with label-quality checks

6. Cluster-distance investigation:
- methods with stronger global spacing behavior (for example PCA, MDS, Isomap, TriMap, UMATO)

7. Cluster-density investigation:
- methods that are usually more stable for density comparison under global geometry constraints (for example PCA, MDS, Isomap, TriMap, UMATO)

Rule:
- Do not switch to supervised or label-aware techniques unless the confirmed main goal is class-separability investigation and label quality is validated.

## Ranking Policy
Final ranking must follow [`docs/workflow/configuration-selection-policy.md`](./workflow/configuration-selection-policy.md).
Do not use ad-hoc preference rules.

## Paper References (User-Facing)
- Hyeon Jeon et al. (2025). *Stop Misusing t-SNE and UMAP: Analyzing, Visualizing, and Reconciling Distortion in DR*. arXiv:2506.08725.
- Hyeon Jeon et al. (2023). *ZADU: A Python Library for Evaluating the Reliability of Dimensionality Reduction Embeddings*. IEEE VIS 2023.
