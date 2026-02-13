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

Updated at: `2026-02-13`

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
| 3 | `kl_div` | 4 | `high` | `accepted` |
| 4 | `ivm` | 3 | `medium` | `accepted` |
| 5 | `mrre` | 3 | `medium` | `accepted` |
| 6 | `nm_stress` | 3 | `medium` | `accepted` |
| 7 | `snc` | 3 | `medium` | `accepted` |
| 8 | `c_evm` | 2 | `medium` | `accepted` |
| 9 | `ca_tnc` | 2 | `medium` | `accepted` |
| 10 | `dsc` | 2 | `medium` | `accepted` |
| 11 | `dtm` | 2 | `medium` | `accepted` |
| 12 | `lcmc` | 2 | `medium` | `accepted` |
| 13 | `sn_stress` | 2 | `medium` | `accepted` |
| 14 | `srho` | 2 | `medium` | `accepted` |
| 15 | `l_tnc` | 1 | `low` | `accepted` |
| 16 | `nd` | 1 | `low` | `accepted` |
| 17 | `proc` | 1 | `low` | `accepted` |
| 18 | `qnx` | 1 | `low` | `unknown` |
| 19 | `spectral_overlap` | 1 | `low` | `unknown` |
| 20 | `topo` | 1 | `low` | `accepted` |
| 21 | `nh` | 0 | `none` | `accepted` |
| 22 | `pr` | 0 | `none` | `accepted` |

## Technique Ranking

| Rank | Technique | PDF Count | Support Tier | Conflict Status |
|---:|---|---:|---|---|
| 1 | `catsne` | 0 | `none` | `unknown` |
| 2 | `cca` | 0 | `none` | `unknown` |
| 3 | `classimap` | 0 | `none` | `unknown` |
| 4 | `classnerv` | 0 | `none` | `unknown` |
| 5 | `isomap` | 0 | `none` | `unknown` |
| 6 | `kpca` | 0 | `none` | `unknown` |
| 7 | `lamp` | 0 | `none` | `unknown` |
| 8 | `laplacian_eigenmaps` | 0 | `none` | `unknown` |
| 9 | `lle` | 0 | `none` | `unknown` |
| 10 | `lmds` | 0 | `none` | `unknown` |
| 11 | `lsp` | 0 | `none` | `unknown` |
| 12 | `mds` | 0 | `none` | `accepted` |
| 13 | `nerv` | 0 | `none` | `unknown` |
| 14 | `pacmap` | 0 | `none` | `unknown` |
| 15 | `pca` | 0 | `none` | `accepted` |
| 16 | `plmp` | 0 | `none` | `unknown` |
| 17 | `random_projection` | 0 | `none` | `unknown` |
| 18 | `s-isomap` | 0 | `none` | `unknown` |
| 19 | `sne` | 0 | `none` | `unknown` |
| 20 | `som` | 0 | `none` | `unknown` |
| 21 | `t-sne` | 0 | `none` | `accepted` |
| 22 | `trimap` | 0 | `none` | `unknown` |
| 23 | `umap` | 0 | `none` | `accepted` |
| 24 | `umato` | 0 | `none` | `unknown` |

## Metric Source Map

Each item below shows where the metric is mentioned.

### `stress` (`8` PDFs, conflict: `accepted`)
- `papers/notes/2011-hamann-survey-dimension-reduction.md`
- `papers/notes/zadu-ref-02-1-s2-0-s0925231209000101-main.md`
- `papers/notes/zadu-ref-03-2408-07724v2.md`
- `papers/notes/zadu-ref-04-2510-08660v1.md`
- `papers/notes/zadu-ref-06-least-square-projection-a-fast-high-precision-multidimensional-projection-techni.md`
- `papers/notes/zadu-ref-07-local-multidimensional-scaling-for-nonlinear-dimension-reduction-graph-drawing-a.md`
- `papers/notes/zadu-ref-08-local-affine-multidimensional-projection-1.md`
- `papers/notes/zadu-ref-12-kruskal-1964a.md`

### `tnc` (`7` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-01-1-s2-0-s0893608006000724-main.md`
- `papers/notes/zadu-ref-02-1-s2-0-s0925231209000101-main.md`
- `papers/notes/zadu-ref-07-local-multidimensional-scaling-for-nonlinear-dimension-reduction-graph-drawing-a.md`
- `papers/notes/zadu-ref-11-jeon23tvcg-4.md`
- `papers/notes/zadu-ref-14-ref06-steering-distortions-to-preserve-classes-and-neighbors-in-supervised-dimen.md`
- `papers/notes/zadu-ref-16-ref12-local-procrustes-for-manifold-embedding-a-measure-of-embedding-quality-and.md`
- `papers/notes/zadu-ref-18-ref18-measuring-and-explaining-the-inter-cluster-reliability-of-multidimensional.md`

### `kl_div` (`4` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-04-2510-08660v1.md`
- `papers/notes/zadu-ref-11-jeon23tvcg-4.md`
- `papers/notes/zadu-ref-14-ref06-steering-distortions-to-preserve-classes-and-neighbors-in-supervised-dimen.md`
- `papers/notes/zadu-ref-17-ref13-stochastic-neighbor-embedding.md`

### `ivm` (`3` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-08-local-affine-multidimensional-projection-1.md`
- `papers/notes/zadu-ref-11-jeon23tvcg-4.md`
- `papers/notes/zadu-ref-19-ref42-a-comparison-for-dimensionality-reduction-methods-of-single-cell-rna-seq-d.md`

### `mrre` (`3` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-02-1-s2-0-s0925231209000101-main.md`
- `papers/notes/zadu-ref-11-jeon23tvcg-4.md`
- `papers/notes/zadu-ref-18-ref18-measuring-and-explaining-the-inter-cluster-reliability-of-multidimensional.md`

### `nm_stress` (`3` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-03-2408-07724v2.md`
- `papers/notes/zadu-ref-04-2510-08660v1.md`
- `papers/notes/zadu-ref-12-kruskal-1964a.md`

### `snc` (`3` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-11-jeon23tvcg-4.md`
- `papers/notes/zadu-ref-15-ref10-feature-learning-for-nonlinear-dimensionality-reduction-toward-maximal-ext.md`
- `papers/notes/zadu-ref-18-ref18-measuring-and-explaining-the-inter-cluster-reliability-of-multidimensional.md`

### `c_evm` (`2` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-11-jeon23tvcg-4.md`
- `papers/notes/zadu-ref-19-ref42-a-comparison-for-dimensionality-reduction-methods-of-single-cell-rna-seq-d.md`

### `ca_tnc` (`2` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-11-jeon23tvcg-4.md`
- `papers/notes/zadu-ref-14-ref06-steering-distortions-to-preserve-classes-and-neighbors-in-supervised-dimen.md`

### `dsc` (`2` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-05-computer-graphics-forum-2009-sips-selecting-good-views-of-high-e2-80-90dimension.md`
- `papers/notes/zadu-ref-11-jeon23tvcg-4.md`

### `dtm` (`2` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-11-jeon23tvcg-4.md`
- `papers/notes/zadu-ref-13-ref03-geometric-inference-for-probability-measures.md`

### `lcmc` (`2` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-02-1-s2-0-s0925231209000101-main.md`
- `papers/notes/zadu-ref-18-ref18-measuring-and-explaining-the-inter-cluster-reliability-of-multidimensional.md`

### `sn_stress` (`2` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-03-2408-07724v2.md`
- `papers/notes/zadu-ref-04-2510-08660v1.md`

### `srho` (`2` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-03-2408-07724v2.md`
- `papers/notes/zadu-ref-04-2510-08660v1.md`

### `l_tnc` (`1` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-11-jeon23tvcg-4.md`

### `nd` (`1` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-15-ref10-feature-learning-for-nonlinear-dimensionality-reduction-toward-maximal-ext.md`

### `proc` (`1` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-16-ref12-local-procrustes-for-manifold-embedding-a-measure-of-embedding-quality-and.md`

### `qnx` (`1` PDFs, conflict: `unknown`)
- `papers/notes/2019-spectral-overlap-quality-metrics.md`

### `spectral_overlap` (`1` PDFs, conflict: `unknown`)
- `papers/notes/2019-spectral-overlap-quality-metrics.md`

### `topo` (`1` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-10-download-2.md`

### `nh` (`0` PDFs, conflict: `accepted`)
- No PDF-backed source note linked.

### `pr` (`0` PDFs, conflict: `accepted`)
- No PDF-backed source note linked.

## Technique Source Map

Each item below shows where the technique is mentioned.

### `catsne` (`0` PDFs, conflict: `unknown`)
- No PDF-backed source note linked.

### `cca` (`0` PDFs, conflict: `unknown`)
- No PDF-backed source note linked.

### `classimap` (`0` PDFs, conflict: `unknown`)
- No PDF-backed source note linked.

### `classnerv` (`0` PDFs, conflict: `unknown`)
- No PDF-backed source note linked.

### `isomap` (`0` PDFs, conflict: `unknown`)
- No PDF-backed source note linked.

### `kpca` (`0` PDFs, conflict: `unknown`)
- No PDF-backed source note linked.

### `lamp` (`0` PDFs, conflict: `unknown`)
- No PDF-backed source note linked.

### `laplacian_eigenmaps` (`0` PDFs, conflict: `unknown`)
- No PDF-backed source note linked.

### `lle` (`0` PDFs, conflict: `unknown`)
- No PDF-backed source note linked.

### `lmds` (`0` PDFs, conflict: `unknown`)
- No PDF-backed source note linked.

### `lsp` (`0` PDFs, conflict: `unknown`)
- No PDF-backed source note linked.

### `mds` (`0` PDFs, conflict: `accepted`)
- No PDF-backed source note linked.

### `nerv` (`0` PDFs, conflict: `unknown`)
- No PDF-backed source note linked.

### `pacmap` (`0` PDFs, conflict: `unknown`)
- No PDF-backed source note linked.

### `pca` (`0` PDFs, conflict: `accepted`)
- No PDF-backed source note linked.

### `plmp` (`0` PDFs, conflict: `unknown`)
- No PDF-backed source note linked.

### `random_projection` (`0` PDFs, conflict: `unknown`)
- No PDF-backed source note linked.

### `s-isomap` (`0` PDFs, conflict: `unknown`)
- No PDF-backed source note linked.

### `sne` (`0` PDFs, conflict: `unknown`)
- No PDF-backed source note linked.

### `som` (`0` PDFs, conflict: `unknown`)
- No PDF-backed source note linked.

### `t-sne` (`0` PDFs, conflict: `accepted`)
- No PDF-backed source note linked.

### `trimap` (`0` PDFs, conflict: `unknown`)
- No PDF-backed source note linked.

### `umap` (`0` PDFs, conflict: `accepted`)
- No PDF-backed source note linked.

### `umato` (`0` PDFs, conflict: `unknown`)
- No PDF-backed source note linked.
