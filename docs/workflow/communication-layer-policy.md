# Communication Layer Policy

Use two separate explanation layers in every final DR report.

Related:
- Workflow: [`docs/workflow/dr-analysis-workflow.md`](./dr-analysis-workflow.md)
- Final report contract: [`docs/workflow/reliability-report-contract.md`](./reliability-report-contract.md)

## Layer A: Internal Technical Record (Builder-facing)
Purpose:
- Preserve full technical detail for implementation, debugging, and audit.

Allowed content:
- technical keys such as task axis, metric bundle, warning gate, score table, and initialization stability.
- formulas, thresholds, and protocol details.

Audience:
- engineers and agents implementing DR code.

## Layer B: User Explanation (End-user-facing)
Purpose:
- Explain the decision so a DR novice with basic CS background can understand and act.

Required style:
- short sentences and concrete wording.
- explain what was done, why it matters, and what remains uncertain.
- always show final settings in copyable form.
- provide a concise runnable code snippet plus a short explanation of why this code was selected.
- describe hyperparameter tuning as Bayesian optimization in plain language.
- do not expose internal workflow nouns to end users.
- do not show internal key names (`snake_case`) in end-user explanation text.

Forbidden standalone jargon in user layer:
- `task axis`
- `task-axis`
- `task lock`
- `lock the task`
- `metric bundle`
- `metric-bundle`
- `bundle scoring`
- `score with bundles`
- `warning gate`
- `preprocessing signature`
- `preprocessing freeze`
- `preprocessing lock`
- `guardrail metric`
- `primary metric`
- `primary metric + guardrail metric`
- `candidate score table`
- `selection_status`
- `axis_confidence`
- `grid search`
- `random search`
- `parameter sweep`

Forbidden metric abbreviations/IDs in user layer:
- `tnc`, `nh`, `nd`, `mrre`, `lcmc`, `ca_tnc`, `l_tnc`
- `dsc`, `ivm`, `c_evm`, `snc`
- `stress`, `kl_div`, `dtm`, `topo`, `pr`, `srho`, `proc`, `qnx`, `spectral_overlap`

Rule:
- In user-facing explanation, write full metric names (for example `Trustworthiness and Continuity`) instead of metric IDs.
- Metric IDs are allowed only in internal technical layer.
- Do not expose token-like internal keys such as `primary_task_axis`, `warning_gate_result`, `candidate_score_table`, `selection_status`, `axis_confidence`, `frozen_preprocessing_signature`.

Forbidden platform/internal interface references in user layer:
- `DR KB`
- `knowledge base`
- `Context7`
- `this repo`
- `workflow step`
- `contract validator`

Rule:
- User-facing output must not mention where the guidance came from.
- Only deliver decision information, rationale, settings, and risks.

If a technical term is unavoidable:
- use `term (plain meaning: ...)` once, then continue with plain words.

## Plain-Language Rewrite Examples
- Bad: `First, we lock the task axis.`
- Good: `First, we confirm your main analysis goal.`
- Bad: `We score candidates with a metric bundle.`
- Good: `We compare methods using reliability checks.`
- Bad: `Primary plus guardrail metrics decided the winner.`
- Good: `We used one main quality check and one safety check to avoid misleading results.`

## Term Mapping Guide
- `task axis` -> `main analysis goal`
- `task lock` -> `confirm the main analysis goal`
- `metric bundle` -> `set of quality checks`
- `bundle scoring` -> `scored with reliability checks`
- `warning gate` -> `safety check`
- `preprocessing signature` -> `same data preparation rules`
- `preprocessing freeze` -> `use the same data preparation for all compared methods`
- `guardrail metric` -> `secondary safety-check score`
- `primary metric` -> `main quality check`
- `initialization stability` -> `whether repeated runs give similar conclusions`
- `tnc` -> `Trustworthiness and Continuity`
- `nh` -> `Neighborhood Hit`
- `nd` -> `Neighbor Dissimilarity`

## Hard Banned Phrases (User Layer)
- `preprocessing freeze`
- `preprocessing lock`
- `primary metric`
- `guardrail metric`
- `primary metric + guardrail metric`
- `task axis`
- `task-axis`
- `task lock`
- `lock the task`
- `metric bundle`
- `metric-bundle`
- `bundle scoring`
- `score with bundles`
- `warning gate`
- `전처리 동결`
- `메트릭 번들`
- `태스크 축`
- `업무 축`
- `잠근다`
- `지표 번들`
- `번들로 점수화`
- `그리드 서치`
- `랜덤 서치`

If any banned phrase appears in user layer, rewrite before finalizing.

## Minimum User Explanation Structure
1. `What you asked`
2. `What we compared`
3. `What we selected and why`
4. `Final settings you can reuse`
5. `What could still go wrong`

## User Deliverable Contract (Mandatory)
Every user-facing final answer must include both:
1. `Concise code`:
   - minimal runnable snippet focused on the chosen configuration
   - avoid exposing internal policy plumbing in user code
   - code should look like normal analysis code: load data, preprocess, fit DR, evaluate reliability scores
   - do not include internal report objects/keys (for example `task_lock`, `preprocessing_config`, `primary_task_axis`, `axis_confidence`)
   - prefer real library calls (for example `scikit-learn`, `umap-learn`, `openTSNE`, `PaCMAP`, `bayes_opt`, `zadu`) over policy-dictionary scaffolding
   - include the selected DR library, `bayes_opt` for tuning, and `zadu` for reliability checks
2. `Why this code`:
   - 3-5 short bullets explaining why the selected code matches the user's goal
   - include one line on residual risk

## Final Rewrite Pass (Mandatory)
Before sending a final user answer:
1. Draft technical answer internally.
2. Rewrite into novice-friendly user layer.
3. Remove all hard banned phrases and internal keys.
4. Replace abbreviations with full names.
5. Keep final wording concrete and short.
