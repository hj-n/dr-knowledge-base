---
id: note-2026-zadu-readme-warning
title: "ZADU README Operational Warning for Label-Separation-Sensitive Metrics"
year: 2026
tags: [dr, zadu, warning, labels]
source_pdf: https://github.com/hj-n/zadu/blob/master/README.md
evidence_level: high
updated_at: 2026-02-07
---

# Problem
- Some ZADU measures rely on assumptions about class-label structure in the original high-dimensional space.
- If this assumption is violated, reliability scores can be misleading.

# Method Summary
- The official ZADU README includes an explicit warning for a subset of label-sensitive measures.
- The warning states that these measures should be used only when class labels are well-separated.

# When To Use / Not Use
- Use these measures when you are confident labels are well-separated in original space.
- Avoid using them as hard evidence when class separation is weak or unknown.

# Metrics Mentioned
- `dsc`
- `ivm`
- `c_evm`
- `nh`
- `ca_tnc`

# Implementation Notes
- Surface this warning wherever these metrics are recommended.
- Ask users to confirm label separability before relying on these metrics.

# Claim Atoms (For Conflict Resolution)
- CLAIM-ZADU-LABEL-SEPARABILITY-WARNING | stance: support | summary: dsc, ivm, c_evm, nh, and ca_tnc can be unreliable when labels are not well-separated in original space | evidence_ids: ZADU-RM-E1, ZADU-RM-E2

# Evidence
- ZADU-RM-E1 | source: README warning block, quote: "if class labels are not well-separated, measures may be unreliable"
- ZADU-RM-E2 | source: README warning block, quote: "measures: dsc, ivm, c_evm, nh, ca_tnc"
