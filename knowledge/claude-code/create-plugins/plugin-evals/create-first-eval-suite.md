---
type: "Guide"
title: "Create and run your first eval suite"
description: "Walkthrough: eval init, run claude plugin eval ., read the summary table and report, iterate with one arm."
resource: "https://code.claude.com/docs/en/plugin-evals"
tags: [evals, init, quickstart, plugins]
kind: "cli_flag"
maturity: "unlabelled"
since: "2.1.269"
surfaces: [cli]
requires: "Claude Code v2.1.269 or later"
identifiers:
  - "claude plugin eval init"
  - "claude plugin eval init --bare <name>"
  - "claude plugin eval ."
  - "--case"
  - "--runs 1"
  - "--ablation none"
  - "Trust this plugin directory?"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugin-evals"
    resource: "https://code.claude.com/docs/en/plugin-evals"
    title: "Test plugins with evals"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A four-step flow from a plugin root directory containing one skill.

# How to use it

1. `claude plugin eval init` (answer `y` to `Trust this plugin directory?`). An interactive session asks what a good result looks like, proposes triggering and non-triggering prompts, designs graders, trials them once and writes one case directory per prompt under `evals/`. Exit with `/exit` or Ctrl+D.
2. `claude plugin eval .` runs every case. Each case runs 3 times with and 3 times without the plugin, so one case is six runs; a progress line prints per run.
3. Summary columns: `CASE WITH W/OUT Δ RUNS COST NOTES`, then a line like `1 case(s) · mean Δ +0.67 · 74s · $0.41`, then `Report: <path>/report.html` and optionally `Published: <url>`. `COST` is a list-price estimate; `NOTES` shows the highest-weight failing grader's explanation or the run's error from the with-arm.
4. Open the report. The common first finding is `Δ` near zero with `tool_used: Skill` failing: Claude is not choosing the skill on natural phrasing, so adjust the skill `description` and rerun.

Single-arm iteration: `claude plugin eval . --case <case-name> --runs 1 --ablation none` (the table then shows `SCORE` and `PASS%` instead of `WITH`, `W/OUT`, `Δ`). One run is noisy; confirm changes at the default three runs.

# Notes

In CI, `init` needs a terminal; use `claude plugin eval init --bare <name>` for a blank template.
