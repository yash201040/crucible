---
type: "Reference"
title: "Eval results: HTML report and JSON"
description: "results/<timestamp>/ contents, the self-contained HTML report, optional artifact publishing, and the aggregate-result.json fields."
resource: "https://code.claude.com/docs/en/plugin-evals"
tags: [evals, report, json, artifacts]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless]
requires: "claude.ai subscription sign-in with artifacts available, to publish the report"
identifiers:
  - "aggregate-result.json"
  - "report.html"
  - "schemaVersion"
  - "partial"
  - "partialReason"
  - "aggregates.overallScore"
  - "aggregates.casesPassed"
  - "aggregates.casesTotal"
  - "aggregates.meanDelta"
  - "cases[].name"
  - "cases[].aggregates.score"
  - "cases[].aggregates.delta"
  - "cases[].arms.with[].error"
  - "cases[].arms.with[].aborted"
  - "cases[].arms.with[].skippedPaidGraders"
  - "cases[].arms.without[].error"
  - "costUsd"
  - "durationSeconds"
  - "claudeVersion"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugin-evals"
    resource: "https://code.claude.com/docs/en/plugin-evals"
    title: "Test plugins with evals"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Every run with at least one case writes `results/<timestamp>/` in the eval directory with `aggregate-result.json` and `report.html`. For a path target it is under the plugin; for a named plugin, under the current directory. `report.html` is a single self-contained file making no external requests. It shows a verdict line and tiles (suite score, Ablation Δ, baseline score, cases at threshold, perfect runs), case cards (case Δ, score bar, threshold tick, red left edge for negative Δ), runs with grader chips (failed ones expanded with explanation; `llm` shows judge votes and evidence; non-scoring graders carry a `plugin-fired indicator` badge), then the prompt and graders.

With a claude.ai subscription and artifacts available, Claude Code also publishes the report as a private artifact and prints `Published: <url>`; `--no-publish` keeps it local. API-key auth gives no `Published:` line. A run started by a Claude Code session also stays local (`Report:` says `kept local`); `--publish-report` overrides.

# How to use it

`aggregate-result.json` / `--json` output has `schemaVersion: 1`, camelCase fields, new fields added without renaming; scripts should ignore unknown fields.

| Field | Meaning |
| :- | :- |
| `partial`, `partialReason` | `true` with `cost_ceiling`, `interrupted` or `auth_failed`; leave out of trend charts |
| `aggregates.overallScore` | Mean case score |
| `aggregates.casesPassed`, `aggregates.casesTotal` | Cases at or above `--threshold`, and total |
| `aggregates.meanDelta` | Mean `Δ` in two-arm mode |
| `cases[].name` | Case name |
| `cases[].aggregates.score` | Mean with-arm run score |
| `cases[].aggregates.delta` | With minus without; omitted for one arm or incomparable arms |
| `cases[].arms.with[].error` | `null` or why a run ended abnormally (e.g. `timed out after 300s`); some are still graded; an API-error run scores 0 ungraded |
| `cases[].arms.with[].aborted` | Present when a mock stopped the run via `expect:`, `abort_when` or the agent-mock budget, with `server`, `tool`, `reason`; score 0, `error` stays `null` |
| `cases[].arms.with[].skippedPaidGraders` | `true` when the cost ceiling skipped judge graders; score not comparable |
| `costUsd`, `durationSeconds`, `claudeVersion` | List-price cost including judge calls, wall seconds, Claude Code version |

# Notes

The document also carries suite configuration, grader definitions and per-run grader results with explanations and evidence.
