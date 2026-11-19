---
type: "Concept"
title: "No-plugin baseline and ablation scoring"
description: "With-arm versus without-arm runs, when only one arm runs, and which graders are excluded from the score."
resource: "https://code.claude.com/docs/en/plugin-evals"
tags: [evals, baseline, ablation, delta]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [headless]
requires: ""
identifiers:
  - "--ablation none"
  - "--ablation with-without"
  - "arm: with-only"
  - "arm: both"
  - "scored: false"
  - "single-arm (no Δ)"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugin-evals"
    resource: "https://code.claude.com/docs/en/plugin-evals"
    title: "Test plugins with evals"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A case normally runs in two arms: the with-arm (plugin loaded) and the without-arm (same number of runs, no plugin). `Δ` is with-score minus without-score.

# How to use it

A case runs the with-arm only (no `W/OUT` or `Δ`) when:
- you pass `--ablation none` (halves cost);
- it resumes a transcript (`context.history_file`) and the target is a path: one arm by default, with a `single-arm (no Δ)` notice on stderr; pass `--ablation with-without` to compare;
- no plugin was found for the case and the target is a path.

In a two-arm run some graders are reported with `scored: false` and excluded from the score in both arms (shown as pass/fail indicators in the with-arm), because they could never pass without the plugin:
- every `tool_used` grader whose `tool` is `Skill`;
- every `regex` with `target: mock_calls` and every `llm` with `focus: mock_calls`, when each mocked server is one your plugin declares;
- any grader marked `arm: with-only`.

# Limits and defaults

- If every grader in a case is excluded, they are scored normally.
- `arm: both` scores a grader in both arms (e.g. a must-not-invoke-skill check with `min: 0`, `max: 0`).
- Under `--ablation none` nothing is excluded, so absolute scores can differ from the two-arm mode.
- A baseline run that dispatches the plugin's own agent fails with `Agent type '<plugin>:<agent-name>' not found`; expected. With the plugin, a case listing `Agent` in `allowed_tools` can dispatch it by namespaced name (e.g. `my-plugin:code-reviewer`).
