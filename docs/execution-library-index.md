# Technique Execution Library Index

This page tracks implementation repositories used by technique execution cards.

For machine-readable mapping and maintenance snapshots, see:
- [`builder/evidence/technique-execution-map.csv`](../builder/evidence/technique-execution-map.csv)
- [`builder/evidence/library-maintenance.csv`](../builder/evidence/library-maintenance.csv)

## Primary Execution Repositories
| Technique | Primary Repository | Notes |
|---|---|---|
| UMAP | [lmcinnes/umap](https://github.com/lmcinnes/umap) | Core local-neighborhood baseline |
| t-SNE | [pavlin-policar/openTSNE](https://github.com/pavlin-policar/openTSNE) | Practical Python implementation |
| SNE | [TorchDR/TorchDR](https://github.com/TorchDR/TorchDR) | Python implementation path |
| TriMap | [eamid/trimap](https://github.com/eamid/trimap) | Triplet-based global-structure method |
| PaCMAP | [YingfanWang/PaCMAP](https://github.com/YingfanWang/PaCMAP) | Local/global balanced pairwise method |
| UMATO | [hyungkwonko/umato](https://github.com/hyungkwonko/umato) | Two-phase local/global method |
| PCA / MDS / Isomap / LLE / KPCA / CCA | [scikit-learn/scikit-learn](https://github.com/scikit-learn/scikit-learn) | General baseline family |
| LAMP | [gnavvy/Lamp](https://github.com/gnavvy/Lamp) | Reference implementation |
| LSP / PLMP fallback | [lvcarx/pyLSP](https://github.com/lvcarx/pyLSP) | Practical Python path |
| SOM | [JustGlowing/minisom](https://github.com/JustGlowing/minisom) | SOM implementation |
| Reliability metrics | [hj-n/zadu](https://github.com/hj-n/zadu) | Reliability-evaluation library |

## Additional Discovered Repositories
These are tracked as supporting references and can be promoted to primary mappings when needed.

| Related Method | Repository | Current Use |
|---|---|---|
| catSNE reference code | [via-cs/t-foresight](https://github.com/via-cs/t-foresight) | Linked from `docs/techniques/catsne.md` as reference implementation |
| SNE/NeRV experimental implementations | [jlmelville/sneer](https://github.com/jlmelville/sneer) | Linked from `docs/techniques/sne.md` as reference implementation |
