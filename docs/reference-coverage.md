# Reference Coverage

This user-facing page summarizes how frequently metrics and techniques are supported by reference PDFs.
Use this for priority ranking when multiple candidates are already task-aligned.

Related:
- Overview: [`docs/overview.md`](./overview.md)
- Workflow: [`docs/workflow/dr-analysis-workflow.md`](./workflow/dr-analysis-workflow.md)
- Task axis/subtask policy: [`docs/task-taxonomy.md`](./task-taxonomy.md)
- Selection policy: [`docs/metrics-and-libraries.md`](./metrics-and-libraries.md)
- Grouped reliability cautions: [`docs/reliability-cautions-and-tips.md`](./reliability-cautions-and-tips.md)
- Metric catalog: [`docs/metrics/README.md`](./metrics/README.md)
- Technique catalog: [`docs/techniques/README.md`](./techniques/README.md)
- Paper catalog: [`docs/paper-catalog.md`](./paper-catalog.md)

Updated at: `2026-02-08`

Priority rule:
1. Filter by task alignment first.
2. Apply label-separation checks (for example, label-separation-sensitive metrics).
3. Prefer higher `PDF Count` among remaining candidates.
4. Down-rank candidates with `contested` conflict status by one tier.
5. If tied, inspect source-note list and choose the better-justified option.

Support tier by distinct PDF count: `very_high` >= 6, `high` 4-5, `medium` 2-3, `low` 1, `none` 0.

## Metrics Ranking

| Rank | Metric | PDF Count | Support Tier | Conflict Status |
|---:|---|---:|---|---|
| 1 | `stress` | 14 | `very_high` | `accepted` |
| 2 | `tnc` | 13 | `very_high` | `accepted` |
| 3 | `kl_div` | 12 | `very_high` | `accepted` |
| 4 | `pr` | 10 | `very_high` | `accepted` |
| 5 | `proc` | 10 | `very_high` | `accepted` |
| 6 | `nd` | 9 | `very_high` | `accepted` |
| 7 | `topo` | 8 | `very_high` | `accepted` |
| 8 | `mrre` | 7 | `very_high` | `accepted` |
| 9 | `dtm` | 6 | `very_high` | `accepted` |
| 10 | `snc` | 6 | `very_high` | `accepted` |
| 11 | `dsc` | 5 | `high` | `accepted` |
| 12 | `ivm` | 5 | `high` | `accepted` |
| 13 | `srho` | 4 | `high` | `accepted` |
| 14 | `c_evm` | 3 | `medium` | `accepted` |
| 15 | `lcmc` | 3 | `medium` | `accepted` |
| 16 | `nm_stress` | 3 | `medium` | `accepted` |
| 17 | `qnx` | 3 | `medium` | `unknown` |
| 18 | `sn_stress` | 3 | `medium` | `accepted` |
| 19 | `ca_tnc` | 2 | `medium` | `accepted` |
| 20 | `nh` | 2 | `medium` | `accepted` |
| 21 | `spectral_overlap` | 2 | `medium` | `unknown` |
| 22 | `l_tnc` | 1 | `low` | `accepted` |

## Technique Ranking

| Rank | Technique | PDF Count | Support Tier | Conflict Status |
|---:|---|---:|---|---|
| 1 | `mds` | 13 | `very_high` | `accepted` |
| 2 | `t-sne` | 13 | `very_high` | `accepted` |
| 3 | `laplacian_eigenmaps` | 11 | `very_high` | `unknown` |
| 4 | `pca` | 11 | `very_high` | `accepted` |
| 5 | `umap` | 11 | `very_high` | `accepted` |
| 6 | `isomap` | 10 | `very_high` | `unknown` |
| 7 | `lle` | 10 | `very_high` | `unknown` |
| 8 | `random_projection` | 10 | `very_high` | `unknown` |
| 9 | `sne` | 9 | `very_high` | `unknown` |
| 10 | `som` | 7 | `very_high` | `unknown` |
| 11 | `kpca` | 6 | `very_high` | `unknown` |
| 12 | `cca` | 4 | `high` | `unknown` |
| 13 | `plmp` | 4 | `high` | `unknown` |
| 14 | `classimap` | 3 | `medium` | `unknown` |
| 15 | `lmds` | 3 | `medium` | `unknown` |
| 16 | `nerv` | 3 | `medium` | `unknown` |
| 17 | `classnerv` | 2 | `medium` | `unknown` |
| 18 | `lamp` | 2 | `medium` | `unknown` |
| 19 | `catsne` | 1 | `low` | `unknown` |
| 20 | `lsp` | 1 | `low` | `unknown` |
| 21 | `s-isomap` | 1 | `low` | `unknown` |

## Metric Source Map

Each item below shows where the metric is mentioned.

### `stress` (`14` PDFs, conflict: `accepted`)
- Least Square Projection: A Fast High-Precision Multidimensional Projection Technique and Its Application to Document Mapping (F.V. Paulovich et al., 2008)
- “Normalized Stress” is Not Normalized: How to Interpret Stress Correctly (Kiran Smelser et al., 2025)
- Geometric Inference for Measures based on Distance Functions (Frédéric Chazal et al., 2010)
- Stochastic Neighbor Embedding (Geoffrey E. Hinton et al., 2002)
- Measuring and Explaining the Inter-Cluster Reliability of Multidimensional Projections (Hyeon Jeon et al., 2021)
- Local Multidimensional Scaling for Nonlinear Dimension Reduction, Graph Drawing, and Proximity Analysis (Lisha Chen et al., 2009)
- Information retrieval perspective to nonlinear dimensionality reduction for data visualization (J. V enna et al., 2010)
- High Performance Dimension Reduction and Visualization for Large High-Dimensional Data Analysis (D. Engel et al., 2012)
- Local multidimensional scaling (Jarkko Venna and Samuel Kaski, 2006)
- VisCoDeR: A tool for visually comparing dimensionality reduction algorithms (René Cutura et al., 2018)
- Stress Maps: Analysing Local Phenomena in Dimensionality Reduction Based Visualisations (Christin Seifert et al., 2010)
- Attribute-based Visual Explanation of Multidimensional Projections (Renato R. O. da Silva et al., 2015)
- ZADU: A Python Library for Evaluating the Reliability of Dimensionality Reduction Embeddings (Hyeon Jeon et al., 2023)
- How Scale Breaks “Normalized Stress” and KL Divergence: Rethinking Quality Metrics (Kiran Smelser et al., 2024)

### `tnc` (`13` PDFs, conflict: `accepted`)
- “Normalized Stress” is Not Normalized: How to Interpret Stress Correctly (Kiran Smelser et al., 2025)
- Measuring and Explaining the Inter-Cluster Reliability of Multidimensional Projections (Hyeon Jeon et al., 2021)
- Local Multidimensional Scaling for Nonlinear Dimension Reduction, Graph Drawing, and Proximity Analysis (Lisha Chen et al., 2009)
- Local multidimensional scaling (Jarkko Venna et al., 2006)
- Quality assessment of dimensionality reduction: Rank-based criteria (John A. Lee et al., 2009)
- Local Affine Multidimensional Projection (theory to build accurate local transformations that can be dynamically modiﬁed according to user knowledge. The accuracy et al., 2011)
- Information retrieval perspective to nonlinear dimensionality reduction for data visualization (J. V enna et al., 2010)
- Uniform manifold approximation with two-phase optimization (H. Jeon et al., 2022)
- Visual Interaction with Dimensionality Reduction: A Structured Literature Analysis (D. Sacha et al, 2017)
- Local multidimensional scaling (Jarkko Venna and Samuel Kaski, 2006)
- Visualizing the quality of dimensionality reduction (Bassam Mokbel et al., 2013)
- Stability Comparison of Dimensionality Reduction Techniques Attending to Data and Parameter Variations (Francisco J. García-Fernández et al., 2013)
- ZADU: A Python Library for Evaluating the Reliability of Dimensionality Reduction Embeddings (Hyeon Jeon et al., 2023)

### `kl_div` (`12` PDFs, conflict: `accepted`)
- “Normalized Stress” is Not Normalized: How to Interpret Stress Correctly (Kiran Smelser et al., 2025)
- Stochastic Neighbor Embedding (Geoffrey E. Hinton et al., 2002)
- Classes are Not Clusters: Improving Label-Based Evaluation of Dimensionality Reduction (Hyeon Jeon et al., 2024)
- Steering Distortions to Preserve Classes and Neighbors in Supervised Dimensionality Reduction (Benoit Colange et al., 2020)
- How Scale Breaks “Normalized Stress” and KL Divergence: Rethinking Quality Metrics (Kiran Smelser et al., 2024)
- Uniform manifold approximation with two-phase optimization (H. Jeon et al., 2022)
- t-viSNE: Interactive Assessment and Interpretation of t-SNE Projections (Angelos Chatzimparmpas et al., 2020)
- Quantitative evaluation of time-dependent multidimensional projection techniques (E. F. V ernier et al., 2020)
- viSNE enables visualization of high dimensional single-cell data and reveals phenotypic heterogeneity of leukemia (E.-A. D. Amir et al, 2013)
- Trustworthiness and metrics in visualizing similarity of gene expression (S. Kaski et al., 2003)
- Implicit Multidimensional Projection of Local Subspaces (Rongzheng Bian et al., 2021)
- ZADU: A Python Library for Evaluating the Reliability of Dimensionality Reduction Embeddings (Hyeon Jeon et al., 2023)

### `pr` (`10` PDFs, conflict: `accepted`)
- Feature Learning for Nonlinear Dimensionality Reduction toward Maximal Extraction of Hidden Patterns (Takanori Fujiwara et al., 2023)
- Measuring and Explaining the Inter-Cluster Reliability of Multidimensional Projections (Hyeon Jeon et al., 2021)
- Steering Distortions to Preserve Classes and Neighbors in Supervised Dimensionality Reduction (Benoit Colange et al., 2020)
- How Scale Breaks “Normalized Stress” and KL Divergence: Rethinking Quality Metrics (Kiran Smelser et al., 2024)
- Quality Metrics for Information Visualization (M. Behrisch et al., 2018)
- Nonlinear dimensionality reduction and data visualization: a review (Hujun Yin, 2007)
- Assessing single-cell transcriptomic variability through density-preserving data visualization (A. Narayan et al., 2020)
- TriMap: Large-scale Dimensionality Reduction Using Triplets (Ehsan Amid and Manfred K. Warmuth, 2022)
- With Respect to What? Simultaneous Interaction with Dimension Reduction and Clustering Projections (John Wenskovitch et al., 2020)
- ZADU: A Python Library for Evaluating the Reliability of Dimensionality Reduction Embeddings (Hyeon Jeon et al., 2023)

### `proc` (`10` PDFs, conflict: `accepted`)
- Feature Learning for Nonlinear Dimensionality Reduction toward Maximal Extraction of Hidden Patterns (Takanori Fujiwara et al., 2023)
- Local Affine Multidimensional Projection (theory to build accurate local transformations that can be dynamically modiﬁed according to user knowledge. The accuracy et al., 2011)
- Mach Learn (2009) 77: 1–25 (Yair Goldberg et al., 2009)
- Feature Learning for Nonlinear Dimensionality Reduction toward Maximal Extraction of Hidden Patterns (Takanori Fujiwara et al., 2023)
- Stability Comparison of Dimensionality Reduction Techniques Attending to Data and Parameter Variations (Francisco J. García-Fernández et al., 2013)
- Interactive Dimensionality Reduction for Comparative Analysis (Takanori Fujiwara et al., 2022)
- t-viSNE: Interactive Assessment and Interpretation of t-SNE Projections (Angelos Chatzimparmpas et al., 2020)
- Local procrustes for manifold embedding: A measure of embedding quality and embedding algorithms (Y. Goldberg and Y. Ritov, 2009)
- ClassiMap: A new dimension reduction technique for exploratory data analysis of labeled data (S. Lespinats et al., 2015)
- ZADU: A Python Library for Evaluating the Reliability of Dimensionality Reduction Embeddings (Hyeon Jeon et al., 2023)

### `nd` (`9` PDFs, conflict: `accepted`)
- Feature Learning for Nonlinear Dimensionality Reduction toward Maximal Extraction of Hidden Patterns (Takanori Fujiwara et al., 2023)
- Measuring and Explaining the Inter-Cluster Reliability of Multidimensional Projections (Hyeon Jeon et al., 2021)
- High Performance Dimension Reduction and Visualization for Large High-Dimensional Data Analysis (D. Engel et al., 2012)
- Visualizing the quality of dimensionality reduction (Bassam Mokbel et al., 2013)
- Neighborhood preserving embedding (X. He et al., 2005)
- Explaining three-dimensional dimensionality reduction plots (Danilo B. Coimbra et al., 2016)
- The art of seeing the elephant in the room: 2D embeddings of single-cell data do make sense (Jan Lause et al., 2024)
- Hierarchical stochastic neighbor embedding (N. Pezzotti et al., 2016)
- ZADU: A Python Library for Evaluating the Reliability of Dimensionality Reduction Embeddings (Hyeon Jeon et al., 2023)

### `topo` (`8` PDFs, conflict: `accepted`)
- Quantifying the Neighborhood Preservation of Self-Organizing Feature Maps (of Self/-Organizing F eature Maps, 1992)
- Charting a manifold (M. Brand, 2002)
- UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction (Leland McInnes et al., 2020)
- High-dimensional labeled data analysis with topology representing graphs (Michaël Aupetit and Thibaud Catz, 2005)
- Nonlinear dimensionality reduction and data visualization: a review (Hujun Yin, 2007)
- Evaluating multi-dimensional visualizations for understanding fuzzy clusters (Y . Zhao et al., 2018)
- A methodology to compare Dimensionality Reduction algorithms in terms of loss of quality (A. Gracia et al., 2014)
- ZADU: A Python Library for Evaluating the Reliability of Dimensionality Reduction Embeddings (Hyeon Jeon et al., 2023)

### `mrre` (`7` PDFs, conflict: `accepted`)
- “Normalized Stress” is Not Normalized: How to Interpret Stress Correctly (Kiran Smelser et al., 2025)
- Measuring and Explaining the Inter-Cluster Reliability of Multidimensional Projections (Hyeon Jeon et al., 2021)
- Quality assessment of dimensionality reduction: Rank-based criteria (John A. Lee et al., 2009)
- Classes are Not Clusters: Improving Label-Based Evaluation of Dimensionality Reduction (Hyeon Jeon et al., 2024)
- How Scale Breaks “Normalized Stress” and KL Divergence: Rethinking Quality Metrics (Kiran Smelser et al., 2024)
- Uniform manifold approximation with two-phase optimization (H. Jeon et al., 2022)
- ZADU: A Python Library for Evaluating the Reliability of Dimensionality Reduction Embeddings (Hyeon Jeon et al., 2023)

### `dtm` (`6` PDFs, conflict: `accepted`)
- Geometric Inference for Measures based on Distance Functions (Frédéric Chazal et al., 2010)
- Classes are Not Clusters: Improving Label-Based Evaluation of Dimensionality Reduction (Hyeon Jeon et al., 2024)
- Uniform manifold approximation with two-phase optimization (H. Jeon et al., 2022)
- VisCoDeR: A tool for visually comparing dimensionality reduction algorithms (René Cutura et al., 2018)
- A Large-Scale Sensitivity Analysis on Latent Embeddings and Dimensionality Reductions for Text Spatializations (D. Atzberger et al., 2025)
- ZADU: A Python Library for Evaluating the Reliability of Dimensionality Reduction Embeddings (Hyeon Jeon et al., 2023)

### `snc` (`6` PDFs, conflict: `accepted`)
- “Normalized Stress” is Not Normalized: How to Interpret Stress Correctly (Kiran Smelser et al., 2025)
- Feature Learning for Nonlinear Dimensionality Reduction toward Maximal Extraction of Hidden Patterns (Takanori Fujiwara et al., 2023)
- Measuring and Explaining the Inter-Cluster Reliability of Multidimensional Projections (Hyeon Jeon et al., 2021)
- Classes are Not Clusters: Improving Label-Based Evaluation of Dimensionality Reduction (Hyeon Jeon et al., 2024)
- How Scale Breaks “Normalized Stress” and KL Divergence: Rethinking Quality Metrics (Kiran Smelser et al., 2024)
- ZADU: A Python Library for Evaluating the Reliability of Dimensionality Reduction Embeddings (Hyeon Jeon et al., 2023)

### `dsc` (`5` PDFs, conflict: `accepted`)
- “Normalized Stress” is Not Normalized: How to Interpret Stress Correctly (Kiran Smelser et al., 2025)
- Selecting good views of high‐dimensional data using class consistency (Mike Sips et al., 2009)
- Classes are Not Clusters: Improving Label-Based Evaluation of Dimensionality Reduction (Hyeon Jeon et al., 2024)
- How Scale Breaks “Normalized Stress” and KL Divergence: Rethinking Quality Metrics (Kiran Smelser et al., 2024)
- ZADU: A Python Library for Evaluating the Reliability of Dimensionality Reduction Embeddings (Hyeon Jeon et al., 2023)

### `ivm` (`5` PDFs, conflict: `accepted`)
- Measuring and Explaining the Inter-Cluster Reliability of Multidimensional Projections (Hyeon Jeon et al., 2021)
- A Comparison for Dimensionality Reduction Methods of Single-Cell RNA-seq Data (Ruizhi Xiang et al., 2021)
- Local Affine Multidimensional Projection (theory to build accurate local transformations that can be dynamically modiﬁed according to user knowledge. The accuracy et al., 2011)
- Classes are Not Clusters: Improving Label-Based Evaluation of Dimensionality Reduction (Hyeon Jeon et al., 2024)
- ZADU: A Python Library for Evaluating the Reliability of Dimensionality Reduction Embeddings (Hyeon Jeon et al., 2023)

### `srho` (`4` PDFs, conflict: `accepted`)
- “Normalized Stress” is Not Normalized: How to Interpret Stress Correctly (Kiran Smelser et al., 2025)
- Feature Learning for Nonlinear Dimensionality Reduction toward Maximal Extraction of Hidden Patterns (Takanori Fujiwara et al., 2023)
- How Scale Breaks “Normalized Stress” and KL Divergence: Rethinking Quality Metrics (Kiran Smelser et al., 2024)
- ZADU: A Python Library for Evaluating the Reliability of Dimensionality Reduction Embeddings (Hyeon Jeon et al., 2023)

### `c_evm` (`3` PDFs, conflict: `accepted`)
- A Comparison for Dimensionality Reduction Methods of Single-Cell RNA-seq Data (Ruizhi Xiang et al., 2021)
- Classes are Not Clusters: Improving Label-Based Evaluation of Dimensionality Reduction (Hyeon Jeon et al., 2024)
- ZADU: A Python Library for Evaluating the Reliability of Dimensionality Reduction Embeddings (Hyeon Jeon et al., 2023)

### `lcmc` (`3` PDFs, conflict: `accepted`)
- Measuring and Explaining the Inter-Cluster Reliability of Multidimensional Projections (Hyeon Jeon et al., 2021)
- Quality assessment of dimensionality reduction: Rank-based criteria (John A. Lee et al., 2009)
- ZADU: A Python Library for Evaluating the Reliability of Dimensionality Reduction Embeddings (Hyeon Jeon et al., 2023)

### `nm_stress` (`3` PDFs, conflict: `accepted`)
- How Scale Breaks “Normalized Stress” and KL Divergence: Rethinking Quality Metrics (Kiran Smelser et al., 2024)
- ZADU: A Python Library for Evaluating the Reliability of Dimensionality Reduction Embeddings (Hyeon Jeon et al., 2023)
- “Normalized Stress” is Not Normalized: How to Interpret Stress Correctly (Kiran Smelser et al., 2025)

### `qnx` (`3` PDFs, conflict: `unknown`)
- Spectral Overlap and a Comparison of Parameter-Free, Dimensionality Reduction Quality Metrics (Jonathan Johannemann; Robert Tibshirani, 2019)
- Toward a Quantitative Survey of Dimension Reduction Techniques (Mateus Espadoto; Rafael M. Martins; Auri S. Hirata; Alexandru C. Telea, 2021)
- Visualizing the quality of dimensionality reduction (Bassam Mokbel et al., 2013)

### `sn_stress` (`3` PDFs, conflict: `accepted`)
- “Normalized Stress” is Not Normalized: How to Interpret Stress Correctly (Kiran Smelser et al., 2025)
- How Scale Breaks “Normalized Stress” and KL Divergence: Rethinking Quality Metrics (Kiran Smelser et al., 2024)
- ZADU: A Python Library for Evaluating the Reliability of Dimensionality Reduction Embeddings (Hyeon Jeon et al., 2023)

### `ca_tnc` (`2` PDFs, conflict: `accepted`)
- Classes are Not Clusters: Improving Label-Based Evaluation of Dimensionality Reduction (Hyeon Jeon et al., 2024)
- ZADU: A Python Library for Evaluating the Reliability of Dimensionality Reduction Embeddings (Hyeon Jeon et al., 2023)

### `nh` (`2` PDFs, conflict: `accepted`)
- How Scale Breaks “Normalized Stress” and KL Divergence: Rethinking Quality Metrics (Kiran Smelser et al., 2024)
- ZADU: A Python Library for Evaluating the Reliability of Dimensionality Reduction Embeddings (Hyeon Jeon et al., 2023)

### `spectral_overlap` (`2` PDFs, conflict: `unknown`)
- Spectral Overlap and a Comparison of Parameter-Free, Dimensionality Reduction Quality Metrics (Jonathan Johannemann; Robert Tibshirani, 2019)
- Toward a Quantitative Survey of Dimension Reduction Techniques (Mateus Espadoto; Rafael M. Martins; Auri S. Hirata; Alexandru C. Telea, 2021)

### `l_tnc` (`1` PDFs, conflict: `accepted`)
- Classes are Not Clusters: Improving Label-Based Evaluation of Dimensionality Reduction (Hyeon Jeon et al., 2024)

## Technique Source Map

Each item below shows where the technique is mentioned.

### `mds` (`13` PDFs, conflict: `accepted`)
- Stop Misusing t-SNE and UMAP for Visual Analytics (Hyeon Jeon, 2025)
- Local Multidimensional Scaling for Nonlinear Dimension Reduction, Graph Drawing, and Proximity Analysis (Lisha Chen et al., 2009)
- “Normalized Stress” is Not Normalized: How to Interpret Stress Correctly (Kiran Smelser et al., 2025)
- Multidimensional Projection for Visual Analytics: Linking Techniques with Distortions, Tasks, and Layout Enrichment (Luis Gustavo Nonato; Michael Aupetit, 2019)
- Data Visualization by Nonlinear Dimensionality Reduction (Andrej Gisbrecht; Barbara Hammer, 2015)
- Empirical Guidance on Scatterplot and Dimension Reduction Technique Choices (M. Sedlmair et al., 2013)
- Information retrieval perspective to nonlinear dimensionality reduction for data visualization (J. V enna et al., 2010)
- High Performance Dimension Reduction and Visualization for Large High-Dimensional Data Analysis (D. Engel et al., 2012)
- Charting a manifold (M. Brand, 2002)
- Visual Interaction with Dimensionality Reduction: A Structured Literature Analysis (D. Sacha et al, 2017)
- Local multidimensional scaling (Jarkko Venna and Samuel Kaski, 2006)
- VisCoDeR: A tool for visually comparing dimensionality reduction algorithms (René Cutura et al., 2018)
- UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction (Leland McInnes et al., 2020)

### `t-sne` (`13` PDFs, conflict: `accepted`)
- Stop Misusing t-SNE and UMAP for Visual Analytics (Hyeon Jeon, 2025)
- How Scale Breaks “Normalized Stress” and KL Divergence: Rethinking Quality Metrics (Kiran Smelser et al., 2024)
- Stochastic Neighbor Embedding (Geoffrey E. Hinton et al., 2002)
- Initialization Is Critical for Preserving Global Data Structure in Both t-SNE and UMAP (Dmitry Kobak; George C. Linderman, 2020)
- Revisiting Dimensionality Reduction Techniques for Visual Cluster Analysis: An Empirical Study (Jiazhi Xia; Yuchen Zhang; Jie Song; Yang Chen; Yunhai Wang; Shixia Liu, 2022)
- Empirical Guidance on Scatterplot and Dimension Reduction Technique Choices (M. Sedlmair et al., 2013)
- Information retrieval perspective to nonlinear dimensionality reduction for data visualization (J. V enna et al., 2010)
- Uniform manifold approximation with two-phase optimization (H. Jeon et al., 2022)
- Feature Learning for Nonlinear Dimensionality Reduction toward Maximal Extraction of Hidden Patterns (Takanori Fujiwara et al., 2023)
- VisCoDeR: A tool for visually comparing dimensionality reduction algorithms (René Cutura et al., 2018)
- UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction (Leland McInnes et al., 2020)
- Stability Comparison of Dimensionality Reduction Techniques Attending to Data and Parameter Variations (Francisco J. García-Fernández et al., 2013)
- Assessing singlecell transcriptomic variability through density-preserving data visualization (Ashwin Narayan et al., 2021)

### `laplacian_eigenmaps` (`11` PDFs, conflict: `unknown`)
- Dimensionality Reduction: A Comparative Review (Laurens van der Maaten; Eric O. Postma; Jaap van den Herik, 2009)
- Initialization Is Critical for Preserving Global Data Structure in Both t-SNE and UMAP (Dmitry Kobak; George C. Linderman, 2020)
- On the Exploration of Dimension Reduction Techniques for Visual Data Mining (Bernd Hamann (survey context), 2011)
- Information retrieval perspective to nonlinear dimensionality reduction for data visualization (J. V enna et al., 2010)
- Nonlinear Dimensionality Reduction by Locally Linear Embedding (Sam T. Roweis and Lawrence K. Saul, 2000)
- Human cluster evaluation and formal quality measures: A comparative study (Joshua Lewis et al., 2012)
- Local procrustes for manifold embedding: A measure of embedding quality and embedding algorithms (Y. Goldberg and Y. Ritov, 2009)
- Nonlinear dimensionality reduction and data visualization: a review (Hujun Yin, 2007)
- Uncorrelated Locality Preserving Projections (X. He and P. Niyogi, 2004)
- Global Versus Local Methods in Nonlinear Dimensionality Reduction (Vin Silva and Joshua Tenenbaum, 2002)
- DD-HDS: A Method for Visualization and Exploration of High-Dimensional Data (Sylvain Lespinats et al., 2007)

### `pca` (`11` PDFs, conflict: `accepted`)
- Stop Misusing t-SNE and UMAP for Visual Analytics (Hyeon Jeon, 2025)
- Dimensionality Reduction: A Comparative Review (Laurens van der Maaten; Eric O. Postma; Jaap van den Herik, 2009)
- A Survey of Dimensionality Reduction Techniques (C.O.S. Sorzano; J. Vargas; A. Pascual-Montano, 2014)
- Nonlinear Dimensionality Reduction by Locally Linear Embedding (Sam T. Roweis and Lawrence K. Saul, 2000)
- Feature Learning for Nonlinear Dimensionality Reduction toward Maximal Extraction of Hidden Patterns (Takanori Fujiwara et al., 2023)
- Local multidimensional scaling (Jarkko Venna and Samuel Kaski, 2006)
- VisCoDeR: A tool for visually comparing dimensionality reduction algorithms (René Cutura et al., 2018)
- Stability Comparison of Dimensionality Reduction Techniques Attending to Data and Parameter Variations (Francisco J. García-Fernández et al., 2013)
- Interactive Dimensionality Reduction for Comparative Analysis (Takanori Fujiwara et al., 2022)
- Interactive Visual Cluster Analysis by Contrastive Dimensionality Reduction (Jiazhi Xia et al., 2022)
- Dimensionality reduction for visualizing single-cell data using UMAP (E. Becht et al, 2019)

### `umap` (`11` PDFs, conflict: `accepted`)
- Stop Misusing t-SNE and UMAP for Visual Analytics (Hyeon Jeon, 2025)
- Initialization Is Critical for Preserving Global Data Structure in Both t-SNE and UMAP (Dmitry Kobak; George C. Linderman, 2020)
- Revisiting Dimensionality Reduction Techniques for Visual Cluster Analysis: An Empirical Study (Jiazhi Xia; Yuchen Zhang; Jie Song; Yang Chen; Yunhai Wang; Shixia Liu, 2022)
- Uniform manifold approximation with two-phase optimization (H. Jeon et al., 2022)
- Feature Learning for Nonlinear Dimensionality Reduction toward Maximal Extraction of Hidden Patterns (Takanori Fujiwara et al., 2023)
- UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction (Leland McInnes et al., 2020)
- Dimensionality reduction for visualizing single-cell data using UMAP (E. Becht et al, 2019)
- Assessing singlecell transcriptomic variability through density-preserving data visualization (Ashwin Narayan et al., 2021)
- Quantitative evaluation of time-dependent multidimensional projection techniques (E. F. V ernier et al., 2020)
- HyperNP: Interactive Visual Exploration of Multidimensional Projection Hyperparameters (G. Appleby et al., 2022)
- Assessing single-cell transcriptomic variability through density-preserving data visualization (A. Narayan et al., 2020)

### `isomap` (`10` PDFs, conflict: `unknown`)
- Local multidimensional scaling (Jarkko Venna et al., 2006)
- Supervised Nonlinear Dimensionality Reduction for Visualization and Classification (X. Geng et al., 2005)
- Information retrieval perspective to nonlinear dimensionality reduction for data visualization (J. V enna et al., 2010)
- Visual Interaction with Dimensionality Reduction: A Structured Literature Analysis (D. Sacha et al, 2017)
- Local multidimensional scaling (Jarkko Venna and Samuel Kaski, 2006)
- VisCoDeR: A tool for visually comparing dimensionality reduction algorithms (René Cutura et al., 2018)
- Stability Comparison of Dimensionality Reduction Techniques Attending to Data and Parameter Variations (Francisco J. García-Fernández et al., 2013)
- Local procrustes for manifold embedding: A measure of embedding quality and embedding algorithms (Y. Goldberg and Y. Ritov, 2009)
- A behavioral investigation of dimensionality reduction (J. Lewis et al., 2012)
- Linear dimensionality reduction: Survey, insights, and generalizations (John P Cunningham and Zoubin Ghahramani, 2015)

### `lle` (`10` PDFs, conflict: `unknown`)
- Local Multidimensional Scaling for Nonlinear Dimension Reduction, Graph Drawing, and Proximity Analysis (Lisha Chen et al., 2009)
- Mach Learn (2009) 77: 1–25 (Yair Goldberg et al., 2009)
- Information retrieval perspective to nonlinear dimensionality reduction for data visualization (J. V enna et al., 2010)
- Nonlinear Dimensionality Reduction by Locally Linear Embedding (Sam T. Roweis and Lawrence K. Saul, 2000)
- High Performance Dimension Reduction and Visualization for Large High-Dimensional Data Analysis (D. Engel et al., 2012)
- Charting a manifold (M. Brand, 2002)
- Local multidimensional scaling (Jarkko Venna and Samuel Kaski, 2006)
- Stability Comparison of Dimensionality Reduction Techniques Attending to Data and Parameter Variations (Francisco J. García-Fernández et al., 2013)
- Local procrustes for manifold embedding: A measure of embedding quality and embedding algorithms (Y. Goldberg and Y. Ritov, 2009)
- DimReader: Axis lines that explain non-linear projections (R. Faust et al., 2019)

### `random_projection` (`10` PDFs, conflict: `unknown`)
- A Survey of Dimensionality Reduction Techniques Based on Random Projection (Haozhe Xie; Jie Li; Hanqing Xue, 2017)
- Toward a Quantitative Survey of Dimension Reduction Techniques (Mateus Espadoto; Rafael M. Martins; Auri S. Hirata; Alexandru C. Telea, 2021)
- A behavioral investigation of dimensionality reduction (J. Lewis et al., 2012)
- Experiments with random projection (S. Dasgupta, 2000)
- Random projection for high dimensional data clustering: A cluster ensemble approach (X. Z. Fern and C. E. Brodley, 2003)
- Semi-random projection for dimensionality reduction and extreme learning machine in high-dimensional space (R. Zhao and K. Mao, 2015)
- LoCH: A neighborhood-based multidimensional projection technique for highdimensional sparse spaces (S. Fadel et al., 2015)
- Random projection-based dimensionality reduction method for hyperspectral target detection (W. Feng et al., 2015)
- Evaluation of Random-Projection-Based Feature Combination on Dysarthric Speech Recognition (Tetsuya Takiguchi et al., 2013)
- Random projections on manifolds of Symmetric Positive Definite matrices for image classification (Azadeh Alavi et al., 2014)

### `sne` (`9` PDFs, conflict: `unknown`)
- Stochastic Neighbor Embedding (Geoffrey E. Hinton et al., 2002)
- Empirical Guidance on Scatterplot and Dimension Reduction Technique Choices (M. Sedlmair et al., 2013)
- Information retrieval perspective to nonlinear dimensionality reduction for data visualization (J. V enna et al., 2010)
- Uniform manifold approximation with two-phase optimization (H. Jeon et al., 2022)
- Feature Learning for Nonlinear Dimensionality Reduction toward Maximal Extraction of Hidden Patterns (Takanori Fujiwara et al., 2023)
- VisCoDeR: A tool for visually comparing dimensionality reduction algorithms (René Cutura et al., 2018)
- UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction (Leland McInnes et al., 2020)
- Stability Comparison of Dimensionality Reduction Techniques Attending to Data and Parameter Variations (Francisco J. García-Fernández et al., 2013)
- Dimensionality reduction for visualizing single-cell data using UMAP (E. Becht et al, 2019)

### `som` (`7` PDFs, conflict: `unknown`)
- Quantifying the Neighborhood Preservation of Self-Organizing Feature Maps (of Self/-Organizing F eature Maps, 1992)
- Quality assessment of dimensionality reduction: Rank-based criteria (John A. Lee et al., 2009)
- ClassiMap: A new dimension reduction technique for exploratory data analysis of labeled data (S. Lespinats et al., 2015)
- Trustworthiness and metrics in visualizing similarity of gene expression (S. Kaski et al., 2003)
- A methodology to compare Dimensionality Reduction algorithms in terms of loss of quality (A. Gracia et al., 2014)
- Survey and comparison of quality measures for selforganizing maps (G. P €olzlbauer, 2004)
- Nonlinear Dimensionality Reduction and Manifold Learning (A. Wism €uller et al., 2010)

### `kpca` (`6` PDFs, conflict: `unknown`)
- Local Multidimensional Scaling for Nonlinear Dimension Reduction, Graph Drawing, and Proximity Analysis (Lisha Chen et al., 2009)
- Interactive Visual Cluster Analysis by Contrastive Dimensionality Reduction (Jiazhi Xia et al., 2022)
- Linear dimensionality reduction: Survey, insights, and generalizations (John P Cunningham and Zoubin Ghahramani, 2015)
- A new method of generalizing Sammon mapping with application to algorithm speed-up (E. Pekalska et al., 1999)
- dimRed and coRanking—Unifying Dimensionality Reduction in R (G. Kraemer et al., 2018)
- Nonlinear Dimensionality Reduction by Semideﬁnite Programming and Kernel Matrix Factorization (Programming and Kernel Matrix Factorization, 2000)

### `cca` (`4` PDFs, conflict: `unknown`)
- Local multidimensional scaling (Jarkko Venna et al., 2006)
- Linear dimensionality reduction: Survey, insights, and generalizations (John P Cunningham and Zoubin Ghahramani, 2015)
- A methodology to compare Dimensionality Reduction algorithms in terms of loss of quality (A. Gracia et al., 2014)
- Sanity check for class-coloring-based evaluation of dimension reduction techniques (Michaël Aupetit, 2014)

### `plmp` (`4` PDFs, conflict: `unknown`)
- Local Affine Multidimensional Projection (theory to build accurate local transformations that can be dynamically modiﬁed according to user knowledge. The accuracy et al., 2011)
- High Performance Dimension Reduction and Visualization for Large High-Dimensional Data Analysis (D. Engel et al., 2012)
- Piecewise laplacian-based projection for interactive data exploration and organization (F. V. Paulovich et al., 2011)
- Explaining three-dimensional dimensionality reduction plots (Danilo B. Coimbra et al., 2016)

### `classimap` (`3` PDFs, conflict: `unknown`)
- Steering Distortions to Preserve Classes and Neighbors in Supervised Dimensionality Reduction (Benoit Colange et al., 2020)
- ClassiMap: A new dimension reduction technique for exploratory data analysis of labeled data (S. Lespinats et al., 2015)
- Steering Distortions to Preserve Classes and Neighbors in Supervised Dimensionality Reduction (Benoît Colange et al., 2020)

### `lmds` (`3` PDFs, conflict: `unknown`)
- Local Multidimensional Scaling for Nonlinear Dimension Reduction, Graph Drawing, and Proximity Analysis (Lisha Chen et al., 2009)
- Local multidimensional scaling (Jarkko Venna and Samuel Kaski, 2006)
- Steering Distortions to Preserve Classes and Neighbors in Supervised Dimensionality Reduction (Benoît Colange et al., 2020)

### `nerv` (`3` PDFs, conflict: `unknown`)
- Steering Distortions to Preserve Classes and Neighbors in Supervised Dimensionality Reduction (Benoit Colange et al., 2020)
- Information retrieval perspective to nonlinear dimensionality reduction for data visualization (J. V enna et al., 2010)
- Steering Distortions to Preserve Classes and Neighbors in Supervised Dimensionality Reduction (Benoît Colange et al., 2020)

### `classnerv` (`2` PDFs, conflict: `unknown`)
- Steering Distortions to Preserve Classes and Neighbors in Supervised Dimensionality Reduction (Benoit Colange et al., 2020)
- Steering Distortions to Preserve Classes and Neighbors in Supervised Dimensionality Reduction (Benoît Colange et al., 2020)

### `lamp` (`2` PDFs, conflict: `unknown`)
- Local Affine Multidimensional Projection (theory to build accurate local transformations that can be dynamically modiﬁed according to user knowledge. The accuracy et al., 2011)
- Deep learning multidimensional projections (M. Espadoto et al., 2020)

### `catsne` (`1` PDFs, conflict: `unknown`)
- Steering Distortions to Preserve Classes and Neighbors in Supervised Dimensionality Reduction (Benoit Colange et al., 2020)

### `lsp` (`1` PDFs, conflict: `unknown`)
- Least Square Projection: A Fast High-Precision Multidimensional Projection Technique and Its Application to Document Mapping (F.V. Paulovich et al., 2008)

### `s-isomap` (`1` PDFs, conflict: `unknown`)
- Supervised Nonlinear Dimensionality Reduction for Visualization and Classification (X. Geng et al., 2005)
