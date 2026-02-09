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
- `papers/notes/zadu-ref-06-least-square-projection-a-fast-high-precision-multidimensional-projection-techni.md`
- `papers/notes/zadu-ref-03-2408-07724v2.md`
- `papers/notes/zadu-ref-13-ref03-geometric-inference-for-probability-measures.md`
- `papers/notes/zadu-ref-17-ref13-stochastic-neighbor-embedding.md`
- `papers/notes/zadu-ref-18-ref18-measuring-and-explaining-the-inter-cluster-reliability-of-multidimensional.md`
- `papers/notes/zadu-ref-07-local-multidimensional-scaling-for-nonlinear-dimension-reduction-graph-drawing-a.md`
- `papers/notes/pending-ref-004-information-retrieval-perspective-to-nonlinear-dimensional.md`
- `papers/notes/pending-ref-013-a-survey-of-dimension-reduction-methods-for-high-dimension.md`
- `papers/notes/pending-ref-019-local-multidimensional-scaling.md`
- `papers/notes/pending-ref-024-viscoder-a-tool-for-visually-comparing-dimensionality-redu.md`
- `papers/notes/pending-ref-035-stress-maps-analysing-local-phenomena-in-dimensionality-re.md`
- `papers/notes/pending-ref-037-attribute-based-visual-explanation-of-multidimensional-pro.md`
- `papers/notes/2023-zadu-library.md`
- `papers/notes/zadu-ref-04-2510-08660v1.md`

### `tnc` (`13` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-03-2408-07724v2.md`
- `papers/notes/zadu-ref-18-ref18-measuring-and-explaining-the-inter-cluster-reliability-of-multidimensional.md`
- `papers/notes/zadu-ref-07-local-multidimensional-scaling-for-nonlinear-dimension-reduction-graph-drawing-a.md`
- `papers/notes/zadu-ref-01-1-s2-0-s0893608006000724-main.md`
- `papers/notes/zadu-ref-02-1-s2-0-s0925231209000101-main.md`
- `papers/notes/zadu-ref-08-local-affine-multidimensional-projection-1.md`
- `papers/notes/pending-ref-004-information-retrieval-perspective-to-nonlinear-dimensional.md`
- `papers/notes/pending-ref-009-uniform-manifold-approximation-with-two-phase-optimization.md`
- `papers/notes/pending-ref-016-visual-interaction-with-dimensionality-reduction-a-structu.md`
- `papers/notes/pending-ref-019-local-multidimensional-scaling.md`
- `papers/notes/pending-ref-028-visualizing-the-quality-of-dimensionality-reduction.md`
- `papers/notes/pending-ref-029-stability-comparison-of-dimensionality-reduction-technique.md`
- `papers/notes/2023-zadu-library.md`

### `kl_div` (`12` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-03-2408-07724v2.md`
- `papers/notes/zadu-ref-17-ref13-stochastic-neighbor-embedding.md`
- `papers/notes/zadu-ref-11-jeon23tvcg-4.md`
- `papers/notes/zadu-ref-14-ref06-steering-distortions-to-preserve-classes-and-neighbors-in-supervised-dimen.md`
- `papers/notes/zadu-ref-04-2510-08660v1.md`
- `papers/notes/pending-ref-009-uniform-manifold-approximation-with-two-phase-optimization.md`
- `papers/notes/pending-ref-040-tvisne-interactive-assessment-and-interpretation-of-t-sne.md`
- `papers/notes/pending-ref-041-quantitative-evaluation-of-time-dependent-multidimensional.md`
- `papers/notes/pending-ref-061-visne-enables-visualization-of-high-dimensional-single-cel.md`
- `papers/notes/pending-ref-073-trustworthiness-and-metrics-in-visualizing-similarity-of-g.md`
- `papers/notes/pending-ref-104-implicit-multidimensional-projection-of-local-subspaces.md`
- `papers/notes/2023-zadu-library.md`

### `pr` (`10` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-15-ref10-feature-learning-for-nonlinear-dimensionality-reduction-toward-maximal-ext.md`
- `papers/notes/zadu-ref-18-ref18-measuring-and-explaining-the-inter-cluster-reliability-of-multidimensional.md`
- `papers/notes/zadu-ref-14-ref06-steering-distortions-to-preserve-classes-and-neighbors-in-supervised-dimen.md`
- `papers/notes/zadu-ref-04-2510-08660v1.md`
- `papers/notes/pending-ref-057-quality-metrics-for-information-visualization.md`
- `papers/notes/pending-ref-068-nonlinear-dimensionality-reduction-and-data-visualization.md`
- `papers/notes/pending-ref-077-assessing-single-cell-transcriptomic-variability-through-d.md`
- `papers/notes/pending-ref-101-trimap-large-scale-dimensionality-reduction-using-triplets.md`
- `papers/notes/pending-ref-148-with-respect-to-what-simultaneous-interaction-with-dimensi.md`
- `papers/notes/2023-zadu-library.md`

### `proc` (`10` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-15-ref10-feature-learning-for-nonlinear-dimensionality-reduction-toward-maximal-ext.md`
- `papers/notes/zadu-ref-08-local-affine-multidimensional-projection-1.md`
- `papers/notes/zadu-ref-16-ref12-local-procrustes-for-manifold-embedding-a-measure-of-embedding-quality-and.md`
- `papers/notes/pending-ref-015-feature-learning-for-nonlinear-dimensionality-reduction-to.md`
- `papers/notes/pending-ref-029-stability-comparison-of-dimensionality-reduction-technique.md`
- `papers/notes/pending-ref-030-interactive-dimensionality-reduction-for-comparative-analy.md`
- `papers/notes/pending-ref-040-tvisne-interactive-assessment-and-interpretation-of-t-sne.md`
- `papers/notes/pending-ref-043-local-procrustes-for-manifold-embedding-a-measure-of-embed.md`
- `papers/notes/pending-ref-044-classimap-a-new-dimension-reduction-technique-for-explorat.md`
- `papers/notes/2023-zadu-library.md`

### `nd` (`9` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-15-ref10-feature-learning-for-nonlinear-dimensionality-reduction-toward-maximal-ext.md`
- `papers/notes/zadu-ref-18-ref18-measuring-and-explaining-the-inter-cluster-reliability-of-multidimensional.md`
- `papers/notes/pending-ref-013-a-survey-of-dimension-reduction-methods-for-high-dimension.md`
- `papers/notes/pending-ref-028-visualizing-the-quality-of-dimensionality-reduction.md`
- `papers/notes/pending-ref-046-neighborhood-preserving-embedding.md`
- `papers/notes/pending-ref-087-explaining-three-dimensional-dimensionality-reduction-plot.md`
- `papers/notes/pending-ref-111-the-art-of-seeing-the-elephant-in-the-room-2d-embeddings-o.md`
- `papers/notes/pending-ref-123-hierarchical-stochastic-neighbor-embedding.md`
- `papers/notes/2023-zadu-library.md`

### `topo` (`8` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-10-download-2.md`
- `papers/notes/pending-ref-014-charting-a-manifold.md`
- `papers/notes/pending-ref-026-umap-uniform-manifold-approximation-and-projection-for-dim.md`
- `papers/notes/pending-ref-063-high-dimensional-labeled-data-analysis-with-topology-repre.md`
- `papers/notes/pending-ref-068-nonlinear-dimensionality-reduction-and-data-visualization.md`
- `papers/notes/pending-ref-109-evaluating-multi-dimensional-visualizations-for-understand.md`
- `papers/notes/pending-ref-125-a-methodology-to-compare-dimensionality-reduction-algorith.md`
- `papers/notes/2023-zadu-library.md`

### `mrre` (`7` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-03-2408-07724v2.md`
- `papers/notes/zadu-ref-18-ref18-measuring-and-explaining-the-inter-cluster-reliability-of-multidimensional.md`
- `papers/notes/zadu-ref-02-1-s2-0-s0925231209000101-main.md`
- `papers/notes/zadu-ref-11-jeon23tvcg-4.md`
- `papers/notes/zadu-ref-04-2510-08660v1.md`
- `papers/notes/pending-ref-009-uniform-manifold-approximation-with-two-phase-optimization.md`
- `papers/notes/2023-zadu-library.md`

### `dtm` (`6` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-13-ref03-geometric-inference-for-probability-measures.md`
- `papers/notes/zadu-ref-11-jeon23tvcg-4.md`
- `papers/notes/pending-ref-009-uniform-manifold-approximation-with-two-phase-optimization.md`
- `papers/notes/pending-ref-024-viscoder-a-tool-for-visually-comparing-dimensionality-redu.md`
- `papers/notes/pending-ref-054-a-large-scale-sensitivity-analysis-on-latent-embeddings-an.md`
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

### `srho` (`4` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-03-2408-07724v2.md`
- `papers/notes/zadu-ref-15-ref10-feature-learning-for-nonlinear-dimensionality-reduction-toward-maximal-ext.md`
- `papers/notes/zadu-ref-04-2510-08660v1.md`
- `papers/notes/2023-zadu-library.md`

### `c_evm` (`3` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-19-ref42-a-comparison-for-dimensionality-reduction-methods-of-single-cell-rna-seq-d.md`
- `papers/notes/zadu-ref-11-jeon23tvcg-4.md`
- `papers/notes/2023-zadu-library.md`

### `lcmc` (`3` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-18-ref18-measuring-and-explaining-the-inter-cluster-reliability-of-multidimensional.md`
- `papers/notes/zadu-ref-02-1-s2-0-s0925231209000101-main.md`
- `papers/notes/2023-zadu-library.md`

### `nm_stress` (`3` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-04-2510-08660v1.md`
- `papers/notes/2023-zadu-library.md`
- `papers/notes/zadu-ref-03-2408-07724v2.md`

### `qnx` (`3` PDFs, conflict: `unknown`)
- `papers/notes/2019-spectral-overlap-quality-metrics.md`
- `papers/notes/2021-quantitative-survey-dr-techniques.md`
- `papers/notes/pending-ref-028-visualizing-the-quality-of-dimensionality-reduction.md`

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

### `spectral_overlap` (`2` PDFs, conflict: `unknown`)
- `papers/notes/2019-spectral-overlap-quality-metrics.md`
- `papers/notes/2021-quantitative-survey-dr-techniques.md`

### `l_tnc` (`1` PDFs, conflict: `accepted`)
- `papers/notes/zadu-ref-11-jeon23tvcg-4.md`

## Technique Source Map

Each item below shows where the technique is mentioned.

### `mds` (`13` PDFs, conflict: `accepted`)
- `papers/notes/2506.08725v2-stop-misusing-tsne-umap.md`
- `papers/notes/zadu-ref-07-local-multidimensional-scaling-for-nonlinear-dimension-reduction-graph-drawing-a.md`
- `papers/notes/zadu-ref-03-2408-07724v2.md`
- `papers/notes/2019-mdp-visual-analytics-survey.md`
- `papers/notes/2015-gisbrecht-nonlinear-dr-visualization.md`
- `papers/notes/pending-ref-002-empirical-guidance-on-scatterplot-and-dimension-reduction.md`
- `papers/notes/pending-ref-004-information-retrieval-perspective-to-nonlinear-dimensional.md`
- `papers/notes/pending-ref-013-a-survey-of-dimension-reduction-methods-for-high-dimension.md`
- `papers/notes/pending-ref-014-charting-a-manifold.md`
- `papers/notes/pending-ref-016-visual-interaction-with-dimensionality-reduction-a-structu.md`
- `papers/notes/pending-ref-019-local-multidimensional-scaling.md`
- `papers/notes/pending-ref-024-viscoder-a-tool-for-visually-comparing-dimensionality-redu.md`
- `papers/notes/pending-ref-026-umap-uniform-manifold-approximation-and-projection-for-dim.md`

### `t-sne` (`13` PDFs, conflict: `accepted`)
- `papers/notes/2506.08725v2-stop-misusing-tsne-umap.md`
- `papers/notes/zadu-ref-04-2510-08660v1.md`
- `papers/notes/zadu-ref-17-ref13-stochastic-neighbor-embedding.md`
- `papers/notes/2020-kobak-initialization-tsne-umap.md`
- `papers/notes/2022-revisiting-dr-visual-cluster-analysis.md`
- `papers/notes/pending-ref-002-empirical-guidance-on-scatterplot-and-dimension-reduction.md`
- `papers/notes/pending-ref-004-information-retrieval-perspective-to-nonlinear-dimensional.md`
- `papers/notes/pending-ref-009-uniform-manifold-approximation-with-two-phase-optimization.md`
- `papers/notes/pending-ref-015-feature-learning-for-nonlinear-dimensionality-reduction-to.md`
- `papers/notes/pending-ref-024-viscoder-a-tool-for-visually-comparing-dimensionality-redu.md`
- `papers/notes/pending-ref-026-umap-uniform-manifold-approximation-and-projection-for-dim.md`
- `papers/notes/pending-ref-029-stability-comparison-of-dimensionality-reduction-technique.md`
- `papers/notes/pending-ref-039-assessing-singlecell-transcriptomic-variability-through-de.md`

### `laplacian_eigenmaps` (`11` PDFs, conflict: `unknown`)
- `papers/notes/2009-comparative-review-dr-techniques.md`
- `papers/notes/2020-kobak-initialization-tsne-umap.md`
- `papers/notes/2011-hamann-survey-dimension-reduction.md`
- `papers/notes/pending-ref-004-information-retrieval-perspective-to-nonlinear-dimensional.md`
- `papers/notes/pending-ref-008-nonlinear-dimensionality-reduction-by-locally-linear-embed.md`
- `papers/notes/pending-ref-022-human-cluster-evaluation-and-formal-quality-measures-a-com.md`
- `papers/notes/pending-ref-043-local-procrustes-for-manifold-embedding-a-measure-of-embed.md`
- `papers/notes/pending-ref-068-nonlinear-dimensionality-reduction-and-data-visualization.md`
- `papers/notes/pending-ref-083-locality-preserving-projections.md`
- `papers/notes/pending-ref-088-global-versus-local-methods-in-nonlinear-dimensionality-re.md`
- `papers/notes/pending-ref-092-dd-hds-a-method-for-visualization-and-exploration-of-high.md`

### `pca` (`11` PDFs, conflict: `accepted`)
- `papers/notes/2506.08725v2-stop-misusing-tsne-umap.md`
- `papers/notes/2009-comparative-review-dr-techniques.md`
- `papers/notes/2014-sorzano-survey-dr-techniques.md`
- `papers/notes/pending-ref-008-nonlinear-dimensionality-reduction-by-locally-linear-embed.md`
- `papers/notes/pending-ref-015-feature-learning-for-nonlinear-dimensionality-reduction-to.md`
- `papers/notes/pending-ref-019-local-multidimensional-scaling.md`
- `papers/notes/pending-ref-024-viscoder-a-tool-for-visually-comparing-dimensionality-redu.md`
- `papers/notes/pending-ref-029-stability-comparison-of-dimensionality-reduction-technique.md`
- `papers/notes/pending-ref-030-interactive-dimensionality-reduction-for-comparative-analy.md`
- `papers/notes/pending-ref-031-interactive-visual-cluster-analysis-by-contrastive-dimensi.md`
- `papers/notes/pending-ref-032-dimensionality-reduction-for-visualizing-single-cell-data.md`

### `umap` (`11` PDFs, conflict: `accepted`)
- `papers/notes/2506.08725v2-stop-misusing-tsne-umap.md`
- `papers/notes/2020-kobak-initialization-tsne-umap.md`
- `papers/notes/2022-revisiting-dr-visual-cluster-analysis.md`
- `papers/notes/pending-ref-009-uniform-manifold-approximation-with-two-phase-optimization.md`
- `papers/notes/pending-ref-015-feature-learning-for-nonlinear-dimensionality-reduction-to.md`
- `papers/notes/pending-ref-026-umap-uniform-manifold-approximation-and-projection-for-dim.md`
- `papers/notes/pending-ref-032-dimensionality-reduction-for-visualizing-single-cell-data.md`
- `papers/notes/pending-ref-039-assessing-singlecell-transcriptomic-variability-through-de.md`
- `papers/notes/pending-ref-041-quantitative-evaluation-of-time-dependent-multidimensional.md`
- `papers/notes/pending-ref-055-hypernp-interactive-visual-exploration-of-multidimensional.md`
- `papers/notes/pending-ref-077-assessing-single-cell-transcriptomic-variability-through-d.md`

### `isomap` (`10` PDFs, conflict: `unknown`)
- `papers/notes/zadu-ref-01-1-s2-0-s0893608006000724-main.md`
- `papers/notes/zadu-ref-09-supervised-nonlinear-dimensionality-reduction-for-visualization-and-classificati.md`
- `papers/notes/pending-ref-004-information-retrieval-perspective-to-nonlinear-dimensional.md`
- `papers/notes/pending-ref-016-visual-interaction-with-dimensionality-reduction-a-structu.md`
- `papers/notes/pending-ref-019-local-multidimensional-scaling.md`
- `papers/notes/pending-ref-024-viscoder-a-tool-for-visually-comparing-dimensionality-redu.md`
- `papers/notes/pending-ref-029-stability-comparison-of-dimensionality-reduction-technique.md`
- `papers/notes/pending-ref-043-local-procrustes-for-manifold-embedding-a-measure-of-embed.md`
- `papers/notes/pending-ref-045-a-behavioral-investigation-of-dimensionality-reduction.md`
- `papers/notes/pending-ref-048-linear-dimensionality-reduction-survey-insights-and-genera.md`

### `lle` (`10` PDFs, conflict: `unknown`)
- `papers/notes/zadu-ref-07-local-multidimensional-scaling-for-nonlinear-dimension-reduction-graph-drawing-a.md`
- `papers/notes/zadu-ref-16-ref12-local-procrustes-for-manifold-embedding-a-measure-of-embedding-quality-and.md`
- `papers/notes/pending-ref-004-information-retrieval-perspective-to-nonlinear-dimensional.md`
- `papers/notes/pending-ref-008-nonlinear-dimensionality-reduction-by-locally-linear-embed.md`
- `papers/notes/pending-ref-013-a-survey-of-dimension-reduction-methods-for-high-dimension.md`
- `papers/notes/pending-ref-014-charting-a-manifold.md`
- `papers/notes/pending-ref-019-local-multidimensional-scaling.md`
- `papers/notes/pending-ref-029-stability-comparison-of-dimensionality-reduction-technique.md`
- `papers/notes/pending-ref-043-local-procrustes-for-manifold-embedding-a-measure-of-embed.md`
- `papers/notes/pending-ref-049-dimreader-axis-lines-that-explain-non-linear-projections.md`

### `random_projection` (`10` PDFs, conflict: `unknown`)
- `papers/notes/2017-random-projection-survey.md`
- `papers/notes/2021-quantitative-survey-dr-techniques.md`
- `papers/notes/pending-ref-045-a-behavioral-investigation-of-dimensionality-reduction.md`
- `papers/notes/pending-ref-064-experiments-with-random-projection.md`
- `papers/notes/pending-ref-117-random-projection-for-high-dimensional-data-clustering-a-c.md`
- `papers/notes/pending-ref-133-semi-random-projection-for-dimensionality-reduction-and-ex.md`
- `papers/notes/pending-ref-158-loch-a-neighborhood-based-multidimensional-projection-tech.md`
- `papers/notes/pending-ref-173-random-projection-based-dimensionality-reduction-method-fo.md`
- `papers/notes/pending-extra-10-5923-j-ajsp-20130-10-5923-j-ajsp-20130303-01.md`
- `papers/notes/pending-extra-1403-0700v1-1403-0700v1.md`

### `sne` (`9` PDFs, conflict: `unknown`)
- `papers/notes/zadu-ref-17-ref13-stochastic-neighbor-embedding.md`
- `papers/notes/pending-ref-002-empirical-guidance-on-scatterplot-and-dimension-reduction.md`
- `papers/notes/pending-ref-004-information-retrieval-perspective-to-nonlinear-dimensional.md`
- `papers/notes/pending-ref-009-uniform-manifold-approximation-with-two-phase-optimization.md`
- `papers/notes/pending-ref-015-feature-learning-for-nonlinear-dimensionality-reduction-to.md`
- `papers/notes/pending-ref-024-viscoder-a-tool-for-visually-comparing-dimensionality-redu.md`
- `papers/notes/pending-ref-026-umap-uniform-manifold-approximation-and-projection-for-dim.md`
- `papers/notes/pending-ref-029-stability-comparison-of-dimensionality-reduction-technique.md`
- `papers/notes/pending-ref-032-dimensionality-reduction-for-visualizing-single-cell-data.md`

### `som` (`7` PDFs, conflict: `unknown`)
- `papers/notes/zadu-ref-10-download-2.md`
- `papers/notes/zadu-ref-02-1-s2-0-s0925231209000101-main.md`
- `papers/notes/pending-ref-044-classimap-a-new-dimension-reduction-technique-for-explorat.md`
- `papers/notes/pending-ref-073-trustworthiness-and-metrics-in-visualizing-similarity-of-g.md`
- `papers/notes/pending-ref-125-a-methodology-to-compare-dimensionality-reduction-algorith.md`
- `papers/notes/pending-ref-136-survey-and-comparison-of-quality-measures-for-selforganizi.md`
- `papers/notes/pending-ref-154-recent-advances-in-nonlinear-dimensionality-reduction-mani.md`

### `kpca` (`6` PDFs, conflict: `unknown`)
- `papers/notes/zadu-ref-07-local-multidimensional-scaling-for-nonlinear-dimension-reduction-graph-drawing-a.md`
- `papers/notes/pending-ref-031-interactive-visual-cluster-analysis-by-contrastive-dimensi.md`
- `papers/notes/pending-ref-048-linear-dimensionality-reduction-survey-insights-and-genera.md`
- `papers/notes/pending-ref-089-a-new-method-of-generalizing-sammon-mapping-with-applicati.md`
- `papers/notes/pending-ref-108-dimred-and-coranking-unifying-dimensionality-reduction-in.md`
- `papers/notes/pending-extra-weinberger05a-weinberger05a.md`

### `cca` (`4` PDFs, conflict: `unknown`)
- `papers/notes/zadu-ref-01-1-s2-0-s0893608006000724-main.md`
- `papers/notes/pending-ref-048-linear-dimensionality-reduction-survey-insights-and-genera.md`
- `papers/notes/pending-ref-125-a-methodology-to-compare-dimensionality-reduction-algorith.md`
- `papers/notes/pending-extra-2669557-2669578-2669557-2669578.md`

### `plmp` (`4` PDFs, conflict: `unknown`)
- `papers/notes/zadu-ref-08-local-affine-multidimensional-projection-1.md`
- `papers/notes/pending-ref-013-a-survey-of-dimension-reduction-methods-for-high-dimension.md`
- `papers/notes/pending-ref-072-piecewise-laplacian-based-projection-for-interactive-data.md`
- `papers/notes/pending-ref-087-explaining-three-dimensional-dimensionality-reduction-plot.md`

### `classimap` (`3` PDFs, conflict: `unknown`)
- `papers/notes/zadu-ref-14-ref06-steering-distortions-to-preserve-classes-and-neighbors-in-supervised-dimen.md`
- `papers/notes/pending-ref-044-classimap-a-new-dimension-reduction-technique-for-explorat.md`
- `papers/notes/pending-ref-161-steering-distortions-to-preserve-classes-and-neighbors-in.md`

### `lmds` (`3` PDFs, conflict: `unknown`)
- `papers/notes/zadu-ref-07-local-multidimensional-scaling-for-nonlinear-dimension-reduction-graph-drawing-a.md`
- `papers/notes/pending-ref-019-local-multidimensional-scaling.md`
- `papers/notes/pending-ref-161-steering-distortions-to-preserve-classes-and-neighbors-in.md`

### `nerv` (`3` PDFs, conflict: `unknown`)
- `papers/notes/zadu-ref-14-ref06-steering-distortions-to-preserve-classes-and-neighbors-in-supervised-dimen.md`
- `papers/notes/pending-ref-004-information-retrieval-perspective-to-nonlinear-dimensional.md`
- `papers/notes/pending-ref-161-steering-distortions-to-preserve-classes-and-neighbors-in.md`

### `classnerv` (`2` PDFs, conflict: `unknown`)
- `papers/notes/zadu-ref-14-ref06-steering-distortions-to-preserve-classes-and-neighbors-in-supervised-dimen.md`
- `papers/notes/pending-ref-161-steering-distortions-to-preserve-classes-and-neighbors-in.md`

### `lamp` (`2` PDFs, conflict: `unknown`)
- `papers/notes/zadu-ref-08-local-affine-multidimensional-projection-1.md`
- `papers/notes/pending-ref-145-deep-learning-multidimensional-projections.md`

### `catsne` (`1` PDFs, conflict: `unknown`)
- `papers/notes/zadu-ref-14-ref06-steering-distortions-to-preserve-classes-and-neighbors-in-supervised-dimen.md`

### `lsp` (`1` PDFs, conflict: `unknown`)
- `papers/notes/zadu-ref-06-least-square-projection-a-fast-high-precision-multidimensional-projection-techni.md`

### `s-isomap` (`1` PDFs, conflict: `unknown`)
- `papers/notes/zadu-ref-09-supervised-nonlinear-dimensionality-reduction-for-visualization-and-classificati.md`
