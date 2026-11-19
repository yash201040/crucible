---
type: "Reference"
title: "Permission mode on resume"
description: "Which permission mode a resumed session starts in, by resume route, including plan-mode restoration under -p."
resource: "https://code.claude.com/docs/en/sessions"
tags: [sessions, permissions, resume, plan-mode, headless]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.246"
surfaces: [cli, headless, ide]
requires: "Claude Code v2.1.246 or later for plan-mode restore on non-interactive and VS Code paths"
identifiers:
  - "--permission-mode"
  - "--dangerously-skip-permissions"
  - "--permission-prompt-tool"
  - "--permission-prompts none"
  - "--fork-session"
  - "permissions.defaultMode"
  - "permissions.denyInsteadOfPrompting"
  - "ExitPlanMode"
  - "bypassPermissions"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sessions"
    resource: "https://code.claude.com/docs/en/sessions"
    title: "Manage sessions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The resumed mode depends on how you resume. This applies when Claude Code loads the conversation from its transcript; a still-running background session keeps its own mode.

# How to use it

- Terminal (`claude --continue`, `claude --resume <session-id>`, or `--resume <name>` matching one session, without `-p`): restores the session's mode except per the table. `--permission-mode` or `--dangerously-skip-permissions` override.
- Non-interactive (`claude -p --resume` / `--continue`): starts in the mode a new `claude -p` run would, except a session that ended in plan mode resumes in plan mode under the conditions below.
- Picker at launch (`claude --resume` alone, `--from-pr`, ambiguous name): starts in the mode a new session would from the same command line, except plan mode is restored; not restored if `--permission-mode`, `--dangerously-skip-permissions` or `--fork-session` is passed. No other stored mode is restored.
- `/resume` inside a session: the conversation continues in the current permission mode, except one that ended in plan mode resumes in plan mode (even if launched with `--permission-mode` or `--dangerously-skip-permissions`). A conversation already open earlier in this run continues in the current mode.
- VS Code: only plan mode is covered here.

| Ended in | Route | Resumed mode |
| :- | :- | :- |
| `bypassPermissions` | Terminal | The mode a new session would start in; re-enable with a launch flag or `permissions.defaultMode: "bypassPermissions"` in user, `--settings` or managed settings |
| `plan` | Terminal | Plan mode; with `--fork-session`, the new-session mode |
| `plan` | Terminal, deny rule removes `ExitPlanMode` or `permissions.denyInsteadOfPrompting` on | New-session mode |
| `auto` | Terminal | `auto`, only if the account still meets auto mode requirements |
| Manual | Terminal | Manual when a new session would start in auto mode from the built-in default; a settings-file `defaultMode` that takes effect wins |
| `plan` | Non-interactive, under conditions | Plan mode |
| Any | Non-interactive, other | New `claude -p` mode |
| `plan` | VS Code | Plan mode, with exceptions on the VS Code page |

# Limits and defaults

`claude -p --resume`/`--continue` resumes in plan mode only when all hold: `--permission-prompt-tool` is passed and `--permission-prompts none` is not; `permissions.denyInsteadOfPrompting` is off; no `--permission-mode` or `--dangerously-skip-permissions`; no `--fork-session`; the run is not started through channels; no deny rule removes `ExitPlanMode`. If `ExitPlanMode` is removed or `denyInsteadOfPrompting` is on, Claude cannot present a plan, so plan mode is not restored.
