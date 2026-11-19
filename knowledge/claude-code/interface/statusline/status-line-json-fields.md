---
type: "Reference"
title: "Status line JSON input fields"
description: "Session data fields Claude Code sends on stdin to a status line script: model, workspace, cost, context window, effort, rate limits, PR, worktree."
resource: "https://code.claude.com/docs/en/statusline"
tags: [statusline, json, cost, context-window, worktree]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "model.id"
  - "model.display_name"
  - "cwd"
  - "workspace.current_dir"
  - "workspace.project_dir"
  - "workspace.added_dirs"
  - "workspace.git_worktree"
  - "workspace.repo.host"
  - "workspace.repo.owner"
  - "workspace.repo.name"
  - "cost.total_cost_usd"
  - "cost.total_duration_ms"
  - "cost.total_api_duration_ms"
  - "cost.total_lines_added"
  - "cost.total_lines_removed"
  - "context_window.total_input_tokens"
  - "context_window.total_output_tokens"
  - "context_window.context_window_size"
  - "context_window.used_percentage"
  - "context_window.remaining_percentage"
  - "context_window.current_usage"
  - "exceeds_200k_tokens"
  - "fast_mode"
  - "effort.level"
  - "thinking.enabled"
  - "rate_limits.five_hour.used_percentage"
  - "rate_limits.seven_day.used_percentage"
  - "rate_limits.five_hour.resets_at"
  - "rate_limits.seven_day.resets_at"
  - "session_id"
  - "session_name"
  - "prompt_id"
  - "transcript_path"
  - "version"
  - "output_style.name"
  - "vim.mode"
  - "agent.name"
  - "pr.number"
  - "pr.url"
  - "pr.review_state"
  - "pr.kind"
  - "worktree.name"
  - "worktree.path"
  - "worktree.branch"
  - "worktree.original_cwd"
  - "worktree.original_branch"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "statusline"
    resource: "https://code.claude.com/docs/en/statusline"
    title: "Customize your status line"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The JSON object piped to a status line command. It is a live feed of per-session cost, context, identity and git/worktree state that a script can also log or forward elsewhere.

# How to use it

| Field | Meaning |
| - | - |
| `model.id`, `model.display_name` | Current model |
| `cwd`, `workspace.current_dir` | Same value; `workspace.current_dir` preferred |
| `workspace.project_dir` | Where Claude Code was launched; may differ from `cwd` |
| `workspace.added_dirs` | Dirs from `/add-dir` or `--add-dir`; empty array if none |
| `workspace.git_worktree` | Name of any linked `git worktree add` tree; absent in main tree (unlike `worktree.*`) |
| `workspace.repo.host/owner/name` | Parsed from `origin` remote; absent without a git repo or origin. For gitlab.com subgroups `owner` is the full namespace path. Before v2.1.260 absent for these projects |
| `cost.total_cost_usd` | Estimated session cost, computed client-side at list price unless a `modelPricing` table is in effect; resets to 0 on `/clear` |
| `cost.total_duration_ms` | Wall-clock session time, accumulates across resumes |
| `cost.total_api_duration_ms` | Time waiting on API responses |
| `cost.total_lines_added`, `cost.total_lines_removed` | Lines changed |
| `context_window.total_input_tokens`, `total_output_tokens` | Tokens in the window from the latest response; input includes cache reads and writes |
| `context_window.context_window_size` | Max window in tokens |
| `context_window.used_percentage`, `remaining_percentage` | Pre-calculated; used = input + cache creation + cache read tokens only (no output); may be null early |
| `context_window.current_usage` | `input_tokens`, `output_tokens`, `cache_creation_input_tokens`, `cache_read_input_tokens`; null before first call and after `/compact` until next call |
| `exceeds_200k_tokens` | Fixed 200k threshold regardless of window size |
| `fast_mode` | Whether fast mode is on |
| `effort.level` | `low`, `medium`, `high`, `xhigh`, `max` as set for the session (not set by skill, subagent or `ultrathink`); shows `CLAUDE_CODE_EFFORT_LEVEL` value if set; absent if model lacks effort support |
| `thinking.enabled` | Extended thinking on |
| `rate_limits.*` | See [prompt cache and spend fields](./prompt-cache-and-spend-fields.md); `five_hour` / `seven_day` `used_percentage` (0-100) and `resets_at` (epoch seconds) |
| `session_id` | Unique id |
| `session_name` | From `--name` or `/rename`, else AI title; default display name does not populate it |
| `prompt_id` | UUID of the prompt being processed; matches `prompt.id` on OpenTelemetry events; absent until first input |
| `transcript_path`, `version`, `output_style.name` | Transcript file, Claude Code version, output style |
| `vim.mode` | `NORMAL`, `INSERT`, `VISUAL`, `VISUAL LINE` when vim mode on |
| `agent.name` | When run with `--agent` or agent settings |
| `pr.number`, `pr.url` | Open PR for the branch; for GitLab remotes the MR (needs v2.1.234+) |
| `pr.review_state` | `approved`, `pending`, `changes_requested`, `draft` |
| `pr.kind` | `mr` for a GitLab merge request; absent for GitHub (v2.1.234+) |
| `worktree.name/path/branch/original_cwd/original_branch` | Only in a worktree session; `branch` and `original_branch` absent for hook-based worktrees |

# Notes

- `rate_limits` appears only for claude.ai Pro, Max and Ultra subscribers, or behind a Claude apps gateway with a spend limit, and only after the first API response; each window may be absent and is dropped after its `resets_at`.
- Handle absence with jq fallbacks such as `// 0` and `// empty`. `/context` can read higher than `used_percentage` because it adds an estimate for messages since the last response.
- Test a script with mock input: `echo '{...}' | ./statusline.sh`.
