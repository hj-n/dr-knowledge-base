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
4. If tied, inspect source-note list and choose the better-justified option.

Support tier by distinct PDF count: `very_high` >= 6, `high` 4-5, `medium` 2-3, `low` 1, `none` 0.

## Metrics Ranking

| Rank | Metric | PDF Count | Support Tier |
|---:|---|---:|---|
| 1 | `stress` | 8 | `very_high` |
| 2 | `tnc` | 7 | `very_high` |
| 3 | `kl_div` | 6 | `very_high` |
| 4 | `mrre` | 6 | `very_high` |
| 5 | `snc` | 6 | `very_high` |
| 6 | `dsc` | 5 | `high` |
| 7 | `ivm` | 5 | `high` |
| 8 | `pr` | 5 | `high` |
| 9 | `proc` | 4 | `high` |
| 10 | `srho` | 4 | `high` |
| 11 | `c_evm` | 3 | `medium` |
| 12 | `dtm` | 3 | `medium` |
| 13 | `lcmc` | 3 | `medium` |
| 14 | `nd` | 3 | `medium` |
| 15 | `nm_stress` | 3 | `medium` |
| 16 | `sn_stress` | 3 | `medium` |
| 17 | `ca_tnc` | 2 | `medium` |
| 18 | `nh` | 2 | `medium` |
| 19 | `topo` | 2 | `medium` |
| 20 | `l_tnc` | 1 | `low` |

## Technique Ranking

| Rank | Technique | PDF Count | Support Tier |
|---:|---|---:|---|
| 1 | `mds` | 3 | `medium` |
| 2 | `t-sne` | 3 | `medium` |
| 3 | `isomap` | 2 | `medium` |
| 4 | `lle` | 2 | `medium` |
| 5 | `som` | 2 | `medium` |
| 6 | `catsne` | 1 | `low` |
| 7 | `cca` | 1 | `low` |
| 8 | `classimap` | 1 | `low` |
| 9 | `classnerv` | 1 | `low` |
| 10 | `kpca` | 1 | `low` |
| 11 | `lamp` | 1 | `low` |
| 12 | `lmds` | 1 | `low` |
| 13 | `lsp` | 1 | `low` |
| 14 | `nerv` | 1 | `low` |
| 15 | `pca` | 1 | `low` |
| 16 | `plmp` | 1 | `low` |
| 17 | `s-isomap` | 1 | `low` |
| 18 | `sne` | 1 | `low` |
| 19 | `umap` | 1 | `low` |

## Metric Source Map

Each item below shows where the metric is mentioned.

### `stress` (`8` PDFs)
- `papers/notes/zadu-ref-06-least-square-projection-a-fast-high-precision-multidimensional-projection-techni.md`
- `papers/notes/zadu-ref-03-2408-07724v2.md`
- `papers/notes/zadu-ref-13-ref03-geometric-inference-for-probability-measures.md`
- `papers/notes/zadu-ref-17-ref13-stochastic-neighbor-embedding.md`
- `papers/notes/zadu-ref-18-ref18-measuring-and-explaining-the-inter-cluster-reliability-of-multidimensional.md`
- `papers/notes/zadu-ref-07-local-multidimensional-scaling-for-nonlinear-dimension-reduction-graph-drawing-a.md`
- `papers/notes/2023-zadu-library.md`
- `papers/notes/zadu-ref-04-2510-08660v1.md`

### `tnc` (`7` PDFs)
- `papers/notes/zadu-ref-03-2408-07724v2.md`
- `papers/notes/zadu-ref-18-ref18-measuring-and-explaining-the-inter-cluster-reliability-of-multidimensional.md`
- `papers/notes/zadu-ref-07-local-multidimensional-scaling-for-nonlinear-dimension-reduction-graph-drawing-a.md`
- `papers/notes/zadu-ref-01-1-s2-0-s0893608006000724-main.md`
- `papers/notes/zadu-ref-02-1-s2-0-s0925231209000101-main.md`
- `papers/notes/zadu-ref-08-local-affine-multidimensional-projection-1.md`
- `papers/notes/2023-zadu-library.md`

### `kl_div` (`6` PDFs)
- `papers/notes/zadu-ref-03-2408-07724v2.md`
- `papers/notes/zadu-ref-17-ref13-stochastic-neighbor-embedding.md`
- `papers/notes/zadu-ref-11-jeon23tvcg-4.md`
- `papers/notes/zadu-ref-14-ref06-steering-distortions-to-preserve-classes-and-neighbors-in-supervised-dimen.md`
- `papers/notes/zadu-ref-04-2510-08660v1.md`
- `papers/notes/2023-zadu-library.md`

### `mrre` (`6` PDFs)
- `papers/notes/zadu-ref-03-2408-07724v2.md`
- `papers/notes/zadu-ref-18-ref18-measuring-and-explaining-the-inter-cluster-reliability-of-multidimensional.md`
- `papers/notes/zadu-ref-02-1-s2-0-s0925231209000101-main.md`
- `papers/notes/zadu-ref-11-jeon23tvcg-4.md`
- `papers/notes/zadu-ref-04-2510-08660v1.md`
- `papers/notes/2023-zadu-library.md`

### `snc` (`6` PDFs)
- `papers/notes/zadu-ref-03-2408-07724v2.md`
- `papers/notes/zadu-ref-15-ref10-feature-learning-for-nonlinear-dimensionality-reduction-toward-maximal-ext.md`
- `papers/notes/zadu-ref-18-ref18-measuring-and-explaining-the-inter-cluster-reliability-of-multidimensional.md`
- `papers/notes/zadu-ref-11-jeon23tvcg-4.md`
- `papers/notes/zadu-ref-04-2510-08660v1.md`
- `papers/notes/2023-zadu-library.md`

### `dsc` (`5` PDFs)
- `papers/notes/zadu-ref-03-2408-07724v2.md`
- `papers/notes/zadu-ref-05-computer-graphics-forum-2009-sips-selecting-good-views-of-high-e2-80-90dimension.md`
- `papers/notes/zadu-ref-11-jeon23tvcg-4.md`
- `papers/notes/zadu-ref-04-2510-08660v1.md`
- `papers/notes/2023-zadu-library.md`

### `ivm` (`5` PDFs)
- `papers/notes/zadu-ref-18-ref18-measuring-and-explaining-the-inter-cluster-reliability-of-multidimensional.md`
- `papers/notes/zadu-ref-19-ref42-a-comparison-for-dimensionality-reduction-methods-of-single-cell-rna-seq-d.md`
- `papers/notes/zadu-ref-08-local-affine-multidimensional-projection-1.md`
- `papers/notes/zadu-ref-11-jeon23tvcg-4.md`
- `papers/notes/2023-zadu-library.md`

### `pr` (`5` PDFs)
- `papers/notes/zadu-ref-15-ref10-feature-learning-for-nonlinear-dimensionality-reduction-toward-maximal-ext.md`
- `papers/notes/zadu-ref-18-ref18-measuring-and-explaining-the-inter-cluster-reliability-of-multidimensional.md`
- `papers/notes/zadu-ref-14-ref06-steering-distortions-to-preserve-classes-and-neighbors-in-supervised-dimen.md`
- `papers/notes/zadu-ref-04-2510-08660v1.md`
- `papers/notes/2023-zadu-library.md`

### `proc` (`4` PDFs)
- `papers/notes/zadu-ref-15-ref10-feature-learning-for-nonlinear-dimensionality-reduction-toward-maximal-ext.md`
- `papers/notes/zadu-ref-08-local-affine-multidimensional-projection-1.md`
- `papers/notes/zadu-ref-16-ref12-local-procrustes-for-manifold-embedding-a-measure-of-embedding-quality-and.md`
- `papers/notes/2023-zadu-library.md`

### `srho` (`4` PDFs)
- `papers/notes/zadu-ref-03-2408-07724v2.md`
- `papers/notes/zadu-ref-15-ref10-feature-learning-for-nonlinear-dimensionality-reduction-toward-maximal-ext.md`
- `papers/notes/zadu-ref-04-2510-08660v1.md`
- `papers/notes/2023-zadu-library.md`

### `c_evm` (`3` PDFs)
- `papers/notes/zadu-ref-19-ref42-a-comparison-for-dimensionality-reduction-methods-of-single-cell-rna-seq-d.md`
- `papers/notes/zadu-ref-11-jeon23tvcg-4.md`
- `papers/notes/2023-zadu-library.md`

### `dtm` (`3` PDFs)
- `papers/notes/zadu-ref-13-ref03-geometric-inference-for-probability-measures.md`
- `papers/notes/zadu-ref-11-jeon23tvcg-4.md`
- `papers/notes/2023-zadu-library.md`

### `lcmc` (`3` PDFs)
- `papers/notes/zadu-ref-18-ref18-measuring-and-explaining-the-inter-cluster-reliability-of-multidimensional.md`
- `papers/notes/zadu-ref-02-1-s2-0-s0925231209000101-main.md`
- `papers/notes/2023-zadu-library.md`

### `nd` (`3` PDFs)
- `papers/notes/zadu-ref-15-ref10-feature-learning-for-nonlinear-dimensionality-reduction-toward-maximal-ext.md`
- `papers/notes/zadu-ref-18-ref18-measuring-and-explaining-the-inter-cluster-reliability-of-multidimensional.md`
- `papers/notes/2023-zadu-library.md`

### `nm_stress` (`3` PDFs)
- `papers/notes/zadu-ref-04-2510-08660v1.md`
- `papers/notes/2023-zadu-library.md`
- `papers/notes/zadu-ref-03-2408-07724v2.md`

### `sn_stress` (`3` PDFs)
- `papers/notes/zadu-ref-03-2408-07724v2.md`
- `papers/notes/zadu-ref-04-2510-08660v1.md`
- `papers/notes/2023-zadu-library.md`

### `ca_tnc` (`2` PDFs)
- `papers/notes/zadu-ref-11-jeon23tvcg-4.md`
- `papers/notes/2023-zadu-library.md`

### `nh` (`2` PDFs)
- `papers/notes/zadu-ref-04-2510-08660v1.md`
- `papers/notes/2023-zadu-library.md`

### `topo` (`2` PDFs)
- `papers/notes/zadu-ref-10-download-2.md`
- `papers/notes/2023-zadu-library.md`

### `l_tnc` (`1` PDFs)
- `papers/notes/zadu-ref-11-jeon23tvcg-4.md`

## Technique Source Map

Each item below shows where the technique is mentioned.

### `mds` (`3` PDFs)
- `papers/notes/2506.08725v2-stop-misusing-tsne-umap.md`
- `papers/notes/zadu-ref-07-local-multidimensional-scaling-for-nonlinear-dimension-reduction-graph-drawing-a.md`
- `papers/notes/zadu-ref-03-2408-07724v2.md`

### `t-sne` (`3` PDFs)
- `papers/notes/2506.08725v2-stop-misusing-tsne-umap.md`
- `papers/notes/zadu-ref-04-2510-08660v1.md`
- `papers/notes/zadu-ref-17-ref13-stochastic-neighbor-embedding.md`

### `isomap` (`2` PDFs)
- `papers/notes/zadu-ref-01-1-s2-0-s0893608006000724-main.md`
- `papers/notes/zadu-ref-09-supervised-nonlinear-dimensionality-reduction-for-visualization-and-classificati.md`

### `lle` (`2` PDFs)
- `papers/notes/zadu-ref-07-local-multidimensional-scaling-for-nonlinear-dimension-reduction-graph-drawing-a.md`
- `papers/notes/zadu-ref-16-ref12-local-procrustes-for-manifold-embedding-a-measure-of-embedding-quality-and.md`

### `som` (`2` PDFs)
- `papers/notes/zadu-ref-10-download-2.md`
- `papers/notes/zadu-ref-02-1-s2-0-s0925231209000101-main.md`

### `catsne` (`1` PDFs)
- `papers/notes/zadu-ref-14-ref06-steering-distortions-to-preserve-classes-and-neighbors-in-supervised-dimen.md`

### `cca` (`1` PDFs)
- `papers/notes/zadu-ref-01-1-s2-0-s0893608006000724-main.md`

### `classimap` (`1` PDFs)
- `papers/notes/zadu-ref-14-ref06-steering-distortions-to-preserve-classes-and-neighbors-in-supervised-dimen.md`

### `classnerv` (`1` PDFs)
- `papers/notes/zadu-ref-14-ref06-steering-distortions-to-preserve-classes-and-neighbors-in-supervised-dimen.md`

### `kpca` (`1` PDFs)
- `papers/notes/zadu-ref-07-local-multidimensional-scaling-for-nonlinear-dimension-reduction-graph-drawing-a.md`

### `lamp` (`1` PDFs)
- `papers/notes/zadu-ref-08-local-affine-multidimensional-projection-1.md`

### `lmds` (`1` PDFs)
- `papers/notes/zadu-ref-07-local-multidimensional-scaling-for-nonlinear-dimension-reduction-graph-drawing-a.md`

### `lsp` (`1` PDFs)
- `papers/notes/zadu-ref-06-least-square-projection-a-fast-high-precision-multidimensional-projection-techni.md`

### `nerv` (`1` PDFs)
- `papers/notes/zadu-ref-14-ref06-steering-distortions-to-preserve-classes-and-neighbors-in-supervised-dimen.md`

### `pca` (`1` PDFs)
- `papers/notes/2506.08725v2-stop-misusing-tsne-umap.md`

### `plmp` (`1` PDFs)
- `papers/notes/zadu-ref-08-local-affine-multidimensional-projection-1.md`

### `s-isomap` (`1` PDFs)
- `papers/notes/zadu-ref-09-supervised-nonlinear-dimensionality-reduction-for-visualization-and-classificati.md`

### `sne` (`1` PDFs)
- `papers/notes/zadu-ref-17-ref13-stochastic-neighbor-embedding.md`

### `umap` (`1` PDFs)
- `papers/notes/2506.08725v2-stop-misusing-tsne-umap.md`
