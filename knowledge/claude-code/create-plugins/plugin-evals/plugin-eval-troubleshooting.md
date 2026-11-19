---
type: "Guide"
title: "Plugin eval troubleshooting"
description: "Errors and symptoms of claude plugin eval: trust, old git, missing baseline, zero scores, API errors, mock budget, timeouts."
resource: "https://code.claude.com/docs/en/plugin-evals"
tags: [evals, troubleshooting, errors, api-errors]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.299"
surfaces: [headless]
requires: ""
identifiers:
  - "plugin eval is currently in early access"
  - "plugin eval is currently unavailable"
  - "is not a trusted plugin directory, and this run cannot stop to ask you about it"
  - "is too old for claude plugin eval"
  - "cannot be evaluated where sessions load it"
  - "No eval cases found"
  - "ablation requested but no plugin resolved"
  - "--json output path must end in .json"
  - "ended on an API error and scored 0 without grading"
  - "mock call budget exceeded"
  - "claude plugin marketplace list"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugin-evals"
    resource: "https://code.claude.com/docs/en/plugin-evals"
    title: "Test plugins with evals"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Common problems keyed on what you see.

# How to use it

| Symptom | Cause and fix |
| :- | :- |
| `plugin eval is currently in early access` | Build predates general availability; `claude update`, fresh session |
| `plugin eval is currently unavailable` | Switched off server-side by Anthropic; `claude update` and retry later |
| `... is not a trusted plugin directory, and this run cannot stop to ask you about it` | Run once in a terminal and answer, or pass `--trust-plugin` |
| `is too old for claude plugin eval` | git older than 2.31 ignores the `GIT_CONFIG_COUNT` environment configuration (added in git 2.31) that disables repository git hooks and helper programs; the suite stops with exit 1. Install git 2.31+. Before v2.1.283 there was no check and those programs stayed on |
| `cannot be evaluated where sessions load it` | Named plugin from a marketplace added from a local path that no session can load now; check `claude plugin marketplace list`, restore the catalog, or pass a directory like `./plugins/formatter` |
| `No eval cases found` | No `prompt.md`/`case.yaml` under the eval directory, or `--case`/`--tag` matched none |
| No `W/OUT` column or `ablation requested but no plugin resolved` | No plugin found for the case; add `plugins: ["../.."]`. Expected if every case resumes a transcript via `context.history_file` |
| `Δ` near zero with `tool_used: Skill` failing | Usually real: skill `description` does not trigger on the phrasing |
| Everything scores zero though files exist | Graders target `files` (paths); use `{ source: file, path: <path> }` for contents. `file_exists` ignores scaffolded or merely edited files |
| Regex over trace does not match | Default `target` is `last_message`; trace is JSON per line (quotes as `\"`); use `flags: i`, not `(?i)` |
| Tools denied, MCP tools missing, Bash will not run | Needs `--allow-tools`; personal MCP servers never load; plugin servers need opt-in plus grant; read the full error in `NOTES` or `error` |
| Exit 1 but results fine | A stderr line names the cause (case failed to load, API-error runs); default threshold 1.0 |
| `--json output path must end in .json` | Target put after `--json`; put it first or give a `.json` path |
| Grader `passed: false` under a run scoring 1.0 | Excluded by design (`scored: false`) |
| `ended on an API error and scored 0 without grading` | A run's last request got an HTTP error (rate limit, plan usage limit); score 0, no grader results, non-zero exit regardless of scores and threshold, baseline runs included (`W/OUT` and `Δ` print `—`). Find the error at the end of the progress line after `error:` or in the JSON `error` field and rerun. Before v2.1.299 such a run was graded on what it had produced. The suite is not marked `partial`; rerun after the limit resets, with `--runs 1` or `--case` to stay under it |
| `mock call budget exceeded` | Agent mocks share 4 x `max_turns` calls per run (40 at default); raise `max_turns` |
| Timeouts or turn cap | Defaults 10 turns and 300 seconds; raise `max_turns` and `timeout_seconds`; use `--max-cost-usd` for cost rather than tight per-run limits |
