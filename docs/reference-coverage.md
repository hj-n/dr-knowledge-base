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
2. Apply warning gates (for example, label-separation-sensitive metrics).
3. Prefer higher `PDF Count` among remaining candidates.
4. Down-rank candidates with `contested` conflict status by one tier.
5. If tied, inspect source-note list and choose the better-justified option.

Support tier by distinct PDF count: `very_high` >= 6, `high` 4-5, `medium` 2-3, `low` 1, `none` 0.

## Metrics Ranking

| Rank | Metric | PDF Count | Support Tier | Conflict Status |
|---:|---|---:|---|---|
| 1 | `stress` | 8 | `very_high` | `accepted` |
| 2 | `tnc` | 7 | `very_high` | `accepted` |
| 3 | `kl_div` | 6 | `very_high` | `accepted` |
| 4 | `mrre` | 6 | `very_high` | `accepted` |
| 5 | `snc` | 6 | `very_high` | `accepted` |
| 6 | `dsc` | 5 | `high` | `accepted` |
| 7 | `ivm` | 5 | `high` | `accepted` |
| 8 | `pr` | 5 | `high` | `accepted` |
| 9 | `proc` | 4 | `high` | `accepted` |
| 10 | `srho` | 4 | `high` | `accepted` |
| 11 | `c_evm` | 3 | `medium` | `accepted` |
| 12 | `dtm` | 3 | `medium` | `accepted` |
| 13 | `lcmc` | 3 | `medium` | `accepted` |
| 14 | `nd` | 3 | `medium` | `accepted` |
| 15 | `nm_stress` | 3 | `medium` | `accepted` |
| 16 | `sn_stress` | 3 | `medium` | `accepted` |
| 17 | `ca_tnc` | 2 | `medium` | `accepted` |
| 18 | `nh` | 2 | `medium` | `accepted` |
| 19 | `qnx` | 2 | `medium` | `unknown` |
| 20 | `spectral_overlap` | 2 | `medium` | `unknown` |
| 21 | `topo` | 2 | `medium` | `accepted` |
| 22 | `l_tnc` | 1 | `low` | `accepted` |

## Technique Ranking

| Rank | Technique | PDF Count | Support Tier | Conflict Status |
|---:|---|---:|---|---|
| 1 | `mds` | 5 | `high` | `accepted` |
| 2 | `t-sne` | 5 | `high` | `accepted` |
| 3 | `laplacian_eigenmaps` | 3 | `medium` | `unknown` |
| 4 | `pca` | 3 | `medium` | `accepted` |
| 5 | `umap` | 3 | `medium` | `accepted` |
| 6 | `isomap` | 2 | `medium` | `unknown` |
| 7 | `lle` | 2 | `medium` | `unknown` |
| 8 | `random_projection` | 2 | `medium` | `unknown` |
| 9 | `som` | 2 | `medium` | `unknown` |
| 10 | `catsne` | 1 | `low` | `unknown` |
| 11 | `cca` | 1 | `low` | `unknown` |
| 12 | `classimap` | 1 | `low` | `unknown` |
| 13 | `classnerv` | 1 | `low` | `unknown` |
| 14 | `kpca` | 1 | `low` | `unknown` |
| 15 | `lamp` | 1 | `low` | `unknown` |
| 16 | `lmds` | 1 | `low` | `unknown` |
| 17 | `lsp` | 1 | `low` | `unknown` |
| 18 | `nerv` | 1 | `low` | `unknown` |
| 19 | `plmp` | 1 | `low` | `unknown` |
| 20 | `s-isomap` | 1 | `low` | `unknown` |
| 21 | `sne` | 1 | `low` | `unknown` |

## Metric Source Map

Each item below shows where the metric is mentioned.

### `stress` (`8` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-06-least-square-projection-a-fast-high-precision-multidimensional-projection-techni.md`
- `papers/notes/zadu-ref-03-2408-07724v2.md`
- `papers/notes/zadu-ref-13-ref03-geometric-inference-for-probability-measures.md`
- `papers/notes/zadu-ref-17-ref13-stochastic-neighbor-embedding.md`
- `papers/notes/zadu-ref-18-ref18-measuring-and-explaining-the-inter-cluster-reliability-of-multidimensional.md`
- `papers/notes/zadu-ref-07-local-multidimensional-scaling-for-nonlinear-dimension-reduction-graph-drawing-a.md`
- `papers/notes/2023-zadu-library.md`
- `papers/notes/zadu-ref-04-2510-08660v1.md`

### `tnc` (`7` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-03-2408-07724v2.md`
- `papers/notes/zadu-ref-18-ref18-measuring-and-explaining-the-inter-cluster-reliability-of-multidimensional.md`
- `papers/notes/zadu-ref-07-local-multidimensional-scaling-for-nonlinear-dimension-reduction-graph-drawing-a.md`
- `papers/notes/zadu-ref-01-1-s2-0-s0893608006000724-main.md`
- `papers/notes/zadu-ref-02-1-s2-0-s0925231209000101-main.md`
- `papers/notes/zadu-ref-08-local-affine-multidimensional-projection-1.md`
- `papers/notes/2023-zadu-library.md`

### `kl_div` (`6` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-03-2408-07724v2.md`
- `papers/notes/zadu-ref-17-ref13-stochastic-neighbor-embedding.md`
- `papers/notes/zadu-ref-11-jeon23tvcg-4.md`
- `papers/notes/zadu-ref-14-ref06-steering-distortions-to-preserve-classes-and-neighbors-in-supervised-dimen.md`
- `papers/notes/zadu-ref-04-2510-08660v1.md`
- `papers/notes/2023-zadu-library.md`

### `mrre` (`6` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-03-2408-07724v2.md`
- `papers/notes/zadu-ref-18-ref18-measuring-and-explaining-the-inter-cluster-reliability-of-multidimensional.md`
- `papers/notes/zadu-ref-02-1-s2-0-s0925231209000101-main.md`
- `papers/notes/zadu-ref-11-jeon23tvcg-4.md`
- `papers/notes/zadu-ref-04-2510-08660v1.md`
- `papers/notes/2023-zadu-library.md`

### `snc` (`6` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-03-2408-07724v2.md`
- `papers/notes/zadu-ref-15-ref10-feature-learning-for-nonlinear-dimensionality-reduction-toward-maximal-ext.md`
- `papers/notes/zadu-ref-18-ref18-measuring-and-explaining-the-inter-cluster-reliability-of-multidimensional.md`
- `papers/notes/zadu-ref-11-jeon23tvcg-4.md`
- `papers/notes/zadu-ref-04-2510-08660v1.md`
- `papers/notes/2023-zadu-library.md`

### `dsc` (`5` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-03-2408-07724v2.md`
- `papers/notes/zadu-ref-05-computer-graphics-forum-2009-sips-selecting-good-views-of-high-e2-80-90dimension.md`
- `papers/notes/zadu-ref-11-jeon23tvcg-4.md`
- `papers/notes/zadu-ref-04-2510-08660v1.md`
- `papers/notes/2023-zadu-library.md`

### `ivm` (`5` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-18-ref18-measuring-and-explaining-the-inter-cluster-reliability-of-multidimensional.md`
- `papers/notes/zadu-ref-19-ref42-a-comparison-for-dimensionality-reduction-methods-of-single-cell-rna-seq-d.md`
- `papers/notes/zadu-ref-08-local-affine-multidimensional-projection-1.md`
- `papers/notes/zadu-ref-11-jeon23tvcg-4.md`
- `papers/notes/2023-zadu-library.md`

### `pr` (`5` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-15-ref10-feature-learning-for-nonlinear-dimensionality-reduction-toward-maximal-ext.md`
- `papers/notes/zadu-ref-18-ref18-measuring-and-explaining-the-inter-cluster-reliability-of-multidimensional.md`
- `papers/notes/zadu-ref-14-ref06-steering-distortions-to-preserve-classes-and-neighbors-in-supervised-dimen.md`
- `papers/notes/zadu-ref-04-2510-08660v1.md`
- `papers/notes/2023-zadu-library.md`

### `proc` (`4` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-15-ref10-feature-learning-for-nonlinear-dimensionality-reduction-toward-maximal-ext.md`
- `papers/notes/zadu-ref-08-local-affine-multidimensional-projection-1.md`
- `papers/notes/zadu-ref-16-ref12-local-procrustes-for-manifold-embedding-a-measure-of-embedding-quality-and.md`
- `papers/notes/2023-zadu-library.md`

### `srho` (`4` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-03-2408-07724v2.md`
- `papers/notes/zadu-ref-15-ref10-feature-learning-for-nonlinear-dimensionality-reduction-toward-maximal-ext.md`
- `papers/notes/zadu-ref-04-2510-08660v1.md`
- `papers/notes/2023-zadu-library.md`

### `c_evm` (`3` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-19-ref42-a-comparison-for-dimensionality-reduction-methods-of-single-cell-rna-seq-d.md`
- `papers/notes/zadu-ref-11-jeon23tvcg-4.md`
- `papers/notes/2023-zadu-library.md`

### `dtm` (`3` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-13-ref03-geometric-inference-for-probability-measures.md`
- `papers/notes/zadu-ref-11-jeon23tvcg-4.md`
- `papers/notes/2023-zadu-library.md`

### `lcmc` (`3` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-18-ref18-measuring-and-explaining-the-inter-cluster-reliability-of-multidimensional.md`
- `papers/notes/zadu-ref-02-1-s2-0-s0925231209000101-main.md`
- `papers/notes/2023-zadu-library.md`

### `nd` (`3` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-15-ref10-feature-learning-for-nonlinear-dimensionality-reduction-toward-maximal-ext.md`
- `papers/notes/zadu-ref-18-ref18-measuring-and-explaining-the-inter-cluster-reliability-of-multidimensional.md`
- `papers/notes/2023-zadu-library.md`

### `nm_stress` (`3` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-04-2510-08660v1.md`
- `papers/notes/2023-zadu-library.md`
- `papers/notes/zadu-ref-03-2408-07724v2.md`

### `sn_stress` (`3` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-03-2408-07724v2.md`
- `papers/notes/zadu-ref-04-2510-08660v1.md`
- `papers/notes/2023-zadu-library.md`

### `ca_tnc` (`2` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-11-jeon23tvcg-4.md`
- `papers/notes/2023-zadu-library.md`

### `nh` (`2` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-04-2510-08660v1.md`
- `papers/notes/2023-zadu-library.md`

### `qnx` (`2` PDFs, conflict: `unknown`)
- `papers/notes/2019-spectral-overlap-quality-metrics.md`
- `papers/notes/2021-quantitative-survey-dr-techniques.md`

### `spectral_overlap` (`2` PDFs, conflict: `unknown`)
- `papers/notes/2019-spectral-overlap-quality-metrics.md`
- `papers/notes/2021-quantitative-survey-dr-techniques.md`

### `topo` (`2` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-10-download-2.md`
- `papers/notes/2023-zadu-library.md`

### `l_tnc` (`1` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-11-jeon23tvcg-4.md`

## Technique Source Map

Each item below shows where the technique is mentioned.

### `mds` (`5` PDFs, conflict: `accepted`)
- `papers/notes/2506.08725v2-stop-misusing-tsne-umap.md`
- `papers/notes/zadu-ref-07-local-multidimensional-scaling-for-nonlinear-dimension-reduction-graph-drawing-a.md`
- `papers/notes/zadu-ref-03-2408-07724v2.md`
- `papers/notes/2019-mdp-visual-analytics-survey.md`
- `papers/notes/2015-gisbrecht-nonlinear-dr-visualization.md`

### `t-sne` (`5` PDFs, conflict: `accepted`)
- `papers/notes/2506.08725v2-stop-misusing-tsne-umap.md`
- `papers/notes/zadu-ref-04-2510-08660v1.md`
- `papers/notes/zadu-ref-17-ref13-stochastic-neighbor-embedding.md`
- `papers/notes/2020-kobak-initialization-tsne-umap.md`
- `papers/notes/2022-revisiting-dr-visual-cluster-analysis.md`

### `laplacian_eigenmaps` (`3` PDFs, conflict: `unknown`)
- `papers/notes/2009-comparative-review-dr-techniques.md`
- `papers/notes/2020-kobak-initialization-tsne-umap.md`
- `papers/notes/2011-hamann-survey-dimension-reduction.md`

### `pca` (`3` PDFs, conflict: `accepted`)
- `papers/notes/2506.08725v2-stop-misusing-tsne-umap.md`
- `papers/notes/2009-comparative-review-dr-techniques.md`
- `papers/notes/2014-sorzano-survey-dr-techniques.md`

### `umap` (`3` PDFs, conflict: `accepted`)
- `papers/notes/2506.08725v2-stop-misusing-tsne-umap.md`
- `papers/notes/2020-kobak-initialization-tsne-umap.md`
- `papers/notes/2022-revisiting-dr-visual-cluster-analysis.md`

### `isomap` (`2` PDFs, conflict: `unknown`)
- `papers/notes/zadu-ref-01-1-s2-0-s0893608006000724-main.md`
- `papers/notes/zadu-ref-09-supervised-nonlinear-dimensionality-reduction-for-visualization-and-classificati.md`

### `lle` (`2` PDFs, conflict: `unknown`)
- `papers/notes/zadu-ref-07-local-multidimensional-scaling-for-nonlinear-dimension-reduction-graph-drawing-a.md`
- `papers/notes/zadu-ref-16-ref12-local-procrustes-for-manifold-embedding-a-measure-of-embedding-quality-and.md`

### `random_projection` (`2` PDFs, conflict: `unknown`)
- `papers/notes/2017-random-projection-survey.md`
- `papers/notes/2021-quantitative-survey-dr-techniques.md`

### `som` (`2` PDFs, conflict: `unknown`)
- `papers/notes/zadu-ref-10-download-2.md`
- `papers/notes/zadu-ref-02-1-s2-0-s0925231209000101-main.md`

### `catsne` (`1` PDFs, conflict: `unknown`)
- `papers/notes/zadu-ref-14-ref06-steering-distortions-to-preserve-classes-and-neighbors-in-supervised-dimen.md`

### `cca` (`1` PDFs, conflict: `unknown`)
- `papers/notes/zadu-ref-01-1-s2-0-s0893608006000724-main.md`

### `classimap` (`1` PDFs, conflict: `unknown`)
- `papers/notes/zadu-ref-14-ref06-steering-distortions-to-preserve-classes-and-neighbors-in-supervised-dimen.md`

### `classnerv` (`1` PDFs, conflict: `unknown`)
- `papers/notes/zadu-ref-14-ref06-steering-distortions-to-preserve-classes-and-neighbors-in-supervised-dimen.md`

### `kpca` (`1` PDFs, conflict: `unknown`)
- `papers/notes/zadu-ref-07-local-multidimensional-scaling-for-nonlinear-dimension-reduction-graph-drawing-a.md`

### `lamp` (`1` PDFs, conflict: `unknown`)
- `papers/notes/zadu-ref-08-local-affine-multidimensional-projection-1.md`

### `lmds` (`1` PDFs, conflict: `unknown`)
- `papers/notes/zadu-ref-07-local-multidimensional-scaling-for-nonlinear-dimension-reduction-graph-drawing-a.md`

### `lsp` (`1` PDFs, conflict: `unknown`)
- `papers/notes/zadu-ref-06-least-square-projection-a-fast-high-precision-multidimensional-projection-techni.md`

### `nerv` (`1` PDFs, conflict: `unknown`)
- `papers/notes/zadu-ref-14-ref06-steering-distortions-to-preserve-classes-and-neighbors-in-supervised-dimen.md`

### `plmp` (`1` PDFs, conflict: `unknown`)
- `papers/notes/zadu-ref-08-local-affine-multidimensional-projection-1.md`

### `s-isomap` (`1` PDFs, conflict: `unknown`)
- `papers/notes/zadu-ref-09-supervised-nonlinear-dimensionality-reduction-for-visualization-and-classificati.md`

### `sne` (`1` PDFs, conflict: `unknown`)
- `papers/notes/zadu-ref-17-ref13-stochastic-neighbor-embedding.md`
