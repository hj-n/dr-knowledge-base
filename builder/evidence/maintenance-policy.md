# Library Maintenance Policy

This policy defines how execution-library maintenance status is classified for DR technique guidance.

## Inputs
- Latest GitHub push timestamp for the mapped repository.
- Latest PyPI release upload timestamp for the mapped package.
- Open issue count and recent repository update timestamp (context only).

## Status Tiers
- `active`
  - At least one of these is true:
    - latest GitHub push is within 180 days, or
    - latest PyPI release is within 180 days.
- `watch`
  - No `active` signal, but at least one of these is true:
    - latest GitHub push is within 540 days, or
    - latest PyPI release is within 540 days.
- `risk`
  - Neither `active` nor `watch` thresholds are met, or no reliable maintenance signal is available.

## Tie and Missing-Data Rule
- If both GitHub and PyPI signals are available, the newer signal determines the tier.
- If one signal is missing, classify using the available signal.
- If both are missing, default to `risk`.

## Practical Use in Technique Docs
- `active`: safe default implementation option.
- `watch`: usable with caution; include a fallback implementation.
- `risk`: do not present as default unless there is no practical alternative; provide fallback and explicit caveat.

## Refresh Rule
- Regenerate `builder/evidence/library-maintenance.csv` whenever:
  - execution mappings change, or
  - significant documentation updates are made, or
  - before a release/publish step.

Command:
- `python scripts/update_library_maintenance.py`
