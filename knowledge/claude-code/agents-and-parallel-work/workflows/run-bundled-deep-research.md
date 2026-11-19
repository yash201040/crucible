---
type: "Feature"
title: "Bundled /deep-research workflow and progress view"
description: "The built-in /deep-research workflow and the /workflows progress view with its keys."
resource: "https://code.claude.com/docs/en/workflows"
tags: [workflows, deep-research, progress, keybindings]
kind: "slash_command"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop]
requires: "WebSearch tool available"
identifiers:
  - "/deep-research"
  - "/workflows"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "workflows"
    resource: "https://code.claude.com/docs/en/workflows"
    title: "Orchestrate subagents at scale with dynamic workflows"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`/deep-research <question>` is the only bundled workflow: it fans out web searches across angles, fetches and cross-checks sources, votes on each claim and returns a cited report with claims that failed cross-checking filtered out. If verifier agents cannot check a claim (rate limit, API error) the report lists it as unverified, not refuted. Saved workflows become commands the same way and appear in `/` autocomplete.

# How to use it

`/deep-research What changed in the Node.js permission model between v20 and v22?` then approve; the run goes to the background. `/workflows` lists running and completed runs (with one run it opens that run directly); a one-line progress summary also shows in the task panel under the input (down arrow, Enter to expand). In the list, `x` stops a run without opening it.

| Key | Action |
| :- | :- |
| Up / Down | Select a phase or agent |
| Enter or Right | Drill into phase, then agent detail (Enter expands/collapses detail) |
| Esc or Left | Back one level |
| `j` / `k` | Scroll agent detail |
| `f` | Filter agents in the phase by status (press again to cycle) |
| `p` | Pause or resume the run |
| `x` | Stop selected agent, or whole workflow when focus is on the run |
| `r` | Restart the selected running agent |
| `s` | Save the run's script as a command |

The agent detail shows prompt, recent tool calls with state, result and any task list; Enter expands prompt, result and call input/result start.

# Limits and defaults

In the Desktop app the progress view is in the Background tasks side pane.
