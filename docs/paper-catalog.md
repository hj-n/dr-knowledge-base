# Paper Catalog

Use this catalog to see which papers have been processed and how each source note is linked.

- CSV file: [`docs/paper-catalog.csv`](./paper-catalog.csv)

## Column Definitions
- `source_note`: note file path in `papers/notes/`.
- `paper_title`: paper title used by this repository.
- `authors`: author list from note frontmatter.
- `venue`: publication venue from note frontmatter.
- `year`: publication year.
- `source_pdf`: original source path.
- `is_seed_paper`: `true` if source path is directly under `papers/raw/`; `false` if source path is under a subdirectory.
- `reference_group`: subdirectory name under `papers/raw/` for reference papers (for example `zadu-table1-references`).
- `parent_seed_note_id`: seed note ID connected to the reference group.
- `parent_seed_source_note`: resolved seed source note path.
- `evidence_level`: note evidence level.
- `updated_at`: note update date.

## Seed vs Reference Rule
- Seed papers: source files directly under `papers/raw/`.
- Reference papers: source files under `papers/raw/<subdirectory>/`.
- A reference paper should map to a seed paper through:
  - `seed_note_id` in note frontmatter, or
  - `builder/evidence/reference-group-map.json`.
