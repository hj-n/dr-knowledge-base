# DR Reliability Cautions and Tips

Use this page to avoid common reliability failures when applying DR and to improve recommendation quality.
Similar claims from multiple papers are grouped into shared themes.

Related:
- Workflow anchor: [`docs/workflow/dr-analysis-workflow.md`](./workflow/dr-analysis-workflow.md)
- Task confirmation protocol: [`docs/workflow/task-confirmation-protocol.md`](./workflow/task-confirmation-protocol.md)
- Preprocessing profiles: [`docs/workflow/preprocessing-profiles.md`](./workflow/preprocessing-profiles.md)
- Deterministic selection policy: [`docs/workflow/configuration-selection-policy.md`](./workflow/configuration-selection-policy.md)
- Task-aligned initialization rules: [`docs/workflow/task-aligned-initialization.md`](./workflow/task-aligned-initialization.md)
- Selection policy: [`docs/metrics-and-libraries.md`](./metrics-and-libraries.md)
- Frequency ranking: [`docs/reference-coverage.md`](./reference-coverage.md)

## Grouped Cautions

### 1) Task-Method Mismatch
Do not select methods before clarifying the primary analytical task. Local methods are often misused for global-distance or density questions, which can produce convincing but invalid interpretations.

Reliability action:
- Confirm one main task first, then map method family and reliability checks to that task.

Source notes:
- Stop Misusing t-SNE and UMAP for Visual Analytics (Hyeon Jeon, 2025)
- Visualizing Dimensionally-Reduced Data: Interviews with Analysts and a Characterization of Task Sequences (Matthew Brehmer; Michael Sedlmair; Stephen Ingram; Tamara Munzner, 2014)
- Dimensionality Reduction in the Wild: Gaps and Guidance (Michael Sedlmair; Matthew Brehmer; Stephen Ingram; Tamara Munzner, 2012)

### 1.1) Popularity-Driven Recommendation Drift
Methods are often recommended because they are familiar or commonly used, not because they fit the confirmed analytical goal. This can preserve misuse patterns even when better-aligned alternatives exist.

Reliability action:
- Reject popularity-only justification in final recommendations.
- Require explicit task-fit evidence and reliability-check evidence for the selected method.
- If rationale is weak, downgrade recommendation confidence and keep alternatives visible.

Source notes:
- Stop Misusing t-SNE and UMAP for Visual Analytics (Hyeon Jeon, 2025)
- Unveiling High-dimensional Backstage: A Survey for Reliable Visual Analytics with Dimensionality Reduction (Hyeon Jeon et al., 2025)

### 2) Hidden Task-Sequence Drift
Even when a high-level task is stated, analysts often switch to a different subtask sequence during exploration (for example, cluster verification to class matching). If the workflow does not detect this drift, metric/technique choices become misaligned.

Reliability action:
- Re-confirm the active task whenever users switch from one interpretive action to another.
- Keep one main goal fixed, and track sequence transitions as optional subtask updates.

Source notes:
- Visualizing Dimensionally-Reduced Data: Interviews with Analysts and a Characterization of Task Sequences (Matthew Brehmer; Michael Sedlmair; Stephen Ingram; Tamara Munzner, 2014)
- Dimensionality Reduction in the Wild: Gaps and Guidance (Michael Sedlmair; Matthew Brehmer; Stephen Ingram; Tamara Munzner, 2012)

### 3) Label-Separation Assumption Violations
Some class-aware metrics assume class labels are already well separated in the original high-dimensional space. If that assumption is weak, these metrics can become unreliable and overstate embedding quality.

Affected metrics:
- Distance Consistency
- Internal Validation Measure
- Clustering-plus-External Validation Measure
- Neighborhood Hit
- Class-Aware Trustworthiness and Continuity

Reliability action:
- Explicitly check label separability before using these metrics as decision-driving evidence.
- If separability is weak or unknown, down-weight these metrics and use additional label-agnostic measures.

Source notes:
- ZADU README Operational Warning for Label-Separation-Sensitive Metrics (hj-n/zadu maintainers, 2026)
- Classes are Not Clusters: Improving Label-Based Evaluation of Dimensionality Reduction (Hyeon Jeon et al., 2024)
- Selecting good views of high‐dimensional data using class consistency (Mike Sips et al., 2009)
- Measuring and Explaining the Inter-Cluster Reliability of Multidimensional Projections (Hyeon Jeon et al., 2021)
- A Comparison for Dimensionality Reduction Methods of Single-Cell RNA-seq Data (Ruizhi Xiang et al., 2021)

### 4) Scale-Sensitive Metric Misinterpretation
Raw stress-like and KL-like scores can be distorted by embedding scale choices. Comparing methods without consistent scale handling can flip rankings and hide true quality differences.

Reliability action:
- Fix or optimize scale consistently before cross-method comparison.
- Prefer scale-aware or normalized variants when comparing multiple embeddings.

Source notes:
- “Normalized Stress” is Not Normalized: How to Interpret Stress Correctly (Kiran Smelser et al., 2025)
- How Scale Breaks “Normalized Stress” and KL Divergence: Rethinking Quality Metrics (Kiran Smelser et al., 2024)
- Multidimensional scaling by optimizing goodness of fit to a nonmetric hypothesis (J. B. Kruskal, 1964)

### 5) Single-Metric Overconfidence
A single metric rarely captures all reliability dimensions. Over-relying on one score can optimize one structural property while silently degrading others.

Reliability action:
- Use a compact reliability check set across local, cluster-level, and global perspectives.
- Require consistency across multiple reliability checks before final recommendation.

Source notes:
- ZADU: A Python Library for Evaluating the Reliability of Dimensionality Reduction Embeddings (Hyeon Jeon et al., 2023)
- Local multidimensional scaling (Jarkko Venna et al., 2006)
- Least Square Projection: A Fast High-Precision Multidimensional Projection Technique and Its Application to Document Mapping (F.V. Paulovich et al., 2008)
- Local Multidimensional Scaling for Nonlinear Dimension Reduction, Graph Drawing, and Proximity Analysis (Lisha Chen et al., 2009)
- Quantifying the Neighborhood Preservation of Self-Organizing Feature Maps (of Self/-Organizing F eature Maps, 1992)
- Geometric Inference for Measures based on Distance Functions (Frédéric Chazal et al., 2010)
- Feature Learning for Nonlinear Dimensionality Reduction toward Maximal Extraction of Hidden Patterns (Takanori Fujiwara et al., 2023)
- Mach Learn (2009) 77: 1–25 (Yair Goldberg et al., 2009)
- Stochastic Neighbor Embedding (Geoffrey E. Hinton et al., 2002)

### 6) Initialization Confounding in Method Comparisons
Method-comparison claims can be invalid when initialization policies differ across algorithms. This is especially critical for t-SNE/UMAP global-structure interpretations.

Reliability action:
- Hold all settings constant except the factor being tested.
- Log initialization policy as mandatory experiment metadata.
- Prefer informative initialization when global structure is part of the decision.

Source notes:
- Initialization Is Critical for Preserving Global Data Structure in Both t-SNE and UMAP (Dmitry Kobak; George C. Linderman, 2020)
- Unveiling High-dimensional Backstage: A Survey for Reliable Visual Analytics with Dimensionality Reduction (Hyeon Jeon; Hyunwook Lee; Yun-Hsin Kuo; Taehyun Yang; Daniel Archambault; Sungahn Ko; Takanori Fujiwara; Kwan-Liu Ma; Jinwook Seo, 2025)

### 7) Reproducibility Drift (Preprocessing/Seed/Protocol)
Score comparisons are unreliable when preprocessing, random seeds, or evaluation settings change across runs. Apparent improvements may be protocol artifacts.

Reliability action:
- Fix preprocessing policy and seed policy before comparing methods.
- Keep identical evaluation protocol across candidate methods.

Source notes:
- Local multidimensional scaling (Jarkko Venna et al., 2006)
- Local Multidimensional Scaling for Nonlinear Dimension Reduction, Graph Drawing, and Proximity Analysis (Lisha Chen et al., 2009)
- Supervised Nonlinear Dimensionality Reduction for Visualization and Classification (X. Geng et al., 2005)
- Geometric Inference for Measures based on Distance Functions (Frédéric Chazal et al., 2010)
- Mach Learn (2009) 77: 1–25 (Yair Goldberg et al., 2009)

### 8) Hyperparameter and Optimization Pitfalls
Method behavior can change materially with hyperparameters and optimization path. Local optima, unstable settings, and undocumented search ranges reduce trustworthiness of final recommendations.

Reliability action:
- Use explicit hyperparameter optimization with recorded search space, seed schedule, and objective metrics.
- Treat convergence quality and stability as part of the recommendation evidence.

Source notes:
- Classes are Not Clusters: Improving Label-Based Evaluation of Dimensionality Reduction (Hyeon Jeon et al., 2024)
- Stochastic Neighbor Embedding (Geoffrey E. Hinton et al., 2002)
- How Scale Breaks “Normalized Stress” and KL Divergence: Rethinking Quality Metrics (Kiran Smelser et al., 2024)
- Spectral Overlap and a Comparison of Parameter-Free, Dimensionality Reduction Quality Metrics (Jonathan Johannemann; Robert Tibshirani, 2019)
- Large-Scale Evaluation of Topic Models and Dimensionality Reduction Methods for 2D Text Spatialization (Daniel Atzberger; Tim Cech; Matthias Trapp; Rico Richter; Willy Scheibel; Jürgen Döllner; Tobias Schreck, 2024)
- Stability Comparison of Dimensionality Reduction Techniques Attending to Data and Parameter Variations (Francisco J. García-Fernández et al., 2013)
- A Large-Scale Sensitivity Analysis on Latent Embeddings and Dimensionality Reductions for Text Spatializations (D. Atzberger et al., 2025)
- HyperNP: Interactive Visual Exploration of Multidimensional Projection Hyperparameters (G. Appleby et al., 2022)
- Understanding How Dimension Reduction Tools Work: An Empirical Approach to Deciphering t-SNE, UMAP, TriMap, and PaCMAP for Data Visualization (Yingfan Wang et al., 2021)
- Mountaineer: Topology-Driven Visual Analytics for Comparing Local Explanations (Parikshit Solunke et al., 2024)

### 9) Initialization/Seed Instability Hidden by Single Runs
Single-run screenshots can hide large initialization/seed variance in stochastic DR methods. A method may look reliable in one run while producing conflicting structure in another run under the same data and nominal settings.

Reliability action:
- Always report multi-seed stability when using initialization-sensitive methods.
- Keep initialization mode fixed during hyperparameter search, then separately evaluate initialization effect.
- If multi-seed rankings disagree, mark recommendation confidence as reduced and keep alternatives.

Source notes:
- Initialization Is Critical for Preserving Global Data Structure in Both t-SNE and UMAP (Dmitry Kobak; George C. Linderman, 2020)
- Stability Comparison of Dimensionality Reduction Techniques Attending to Data and Parameter Variations (Francisco J. García-Fernández et al., 2013)
- A Large-Scale Sensitivity Analysis on Latent Embeddings and Dimensionality Reductions for Text Spatializations (D. Atzberger et al., 2025)
- TriMap: Large-scale Dimensionality Reduction Using Triplets (Ehsan Amid and Manfred K. Warmuth, 2022)
- ENS-t-SNE: Embedding Neighborhoods Simultaneously t-SNE (Jacob Miller et al., 2024)
- UMATO: Bridging Local and Global Structures for Reliable Visual Analytics With Dimensionality Reduction (Hyeon Jeon et al., 2025)

### 10) Runtime-Quality Tradeoff Blind Spots
Some methods or evaluation procedures incur high runtime/complexity cost, and naive runtime assumptions can bias method choice.

Reliability action:
- Report runtime/complexity context together with reliability scores.
- Avoid ranking methods by quality without practical runtime feasibility checks.

Source notes:
- Quality assessment of dimensionality reduction: Rank-based criteria (John A. Lee et al., 2009)
- Local Affine Multidimensional Projection (Paulo Joia, Fernando V. Paulovich, Danilo Coimbra, Jose Alberto Cuminato, Luis Gustavo Nonato, 2011)
- Feature Learning for Nonlinear Dimensionality Reduction toward Maximal Extraction of Hidden Patterns (Takanori Fujiwara et al., 2023)
- Stochastic Neighbor Embedding (Geoffrey E. Hinton et al., 2002)
- A Comparison for Dimensionality Reduction Methods of Single-Cell RNA-seq Data (Ruizhi Xiang et al., 2021)
- A Survey of Dimensionality Reduction Techniques Based on Random Projection (Haozhe Xie; Jie Li; Hanqing Xue, 2017)

## Reliability Improvement Checklist

1. Confirm one primary analytical task before method selection.
2. Re-check task sequence when the analysis intent shifts.
3. Validate label separability before using class-aware metrics.
4. Use a multi-level reliability check set instead of a single metric.
5. Control scale when comparing stress/KL-related scores.
6. Keep preprocessing, seeds, and initialization policy consistent for fair comparison.
7. Log hyperparameter search space and optimization trace.
8. Include runtime feasibility with quality evidence.
9. Explain residual uncertainty and limits in the final recommendation.
10. Add an initialization/seed stability statement for stochastic methods.
11. Reject popularity-only rationale and require explicit task-fit evidence.
