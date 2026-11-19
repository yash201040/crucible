---
type: "Feature"
title: "Permission mode and dispatch defaults"
description: "How a background session picks its permission mode and the claude agents flags that set defaults for every dispatch."
resource: "https://code.claude.com/docs/en/agent-view"
tags: [agent-view, permissions, defaults, restricted]
kind: "cli_flag"
maturity: "research-preview"
since: "2.1.142"
surfaces: [cli]
requires: ""
identifiers:
  - "--permission-mode"
  - "--dangerously-skip-permissions"
  - "--allow-dangerously-skip-permissions"
  - "--restricted"
  - "--agent"
  - "--effort"
  - "--model"
  - "permissions.defaultMode"
  - "effortLevel"
  - "modelSettings"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-view"
    resource: "https://code.claude.com/docs/en/agent-view"
    title: "Manage multiple agents with agent view"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Permission mode source depends on how the session started:
- Backgrounded with `/bg` or `←`: keeps its current mode.
- Dispatched from a shell-opened `claude agents` or `claude --bg`: starts as a new `claude` session in that directory would (unless the view has dispatch defaults).
- Dispatched from a view opened with `←`: first `permissions.defaultMode` of the target directory (`auto` and `bypassPermissions` take effect only from managed settings, a `--settings` file or `~/.claude/settings.json`; a project-file mode more permissive than the originating session's is refused), else the originating session's mode. If that was `bypassPermissions` and the acceptance is only in `.claude/settings.local.json` or a `--settings` file, the new session starts in Manual mode with notice `Bypass permissions was requested at launch and ignored`. A refused source falls through to the next. Permissiveness order: plan, then Manual and `dontAsk`, then `acceptEdits` and auto, then `bypassPermissions`.

# How to use it

```bash
claude agents --permission-mode plan --model opus --effort high
```

| Flag on `claude agents` | Effect |
| :- | :- |
| `--permission-mode`, `--model`, `--effort` | Defaults for every dispatch; `--effort` accepts `ultracode` |
| `--agent` | Subagent used when the prompt names none; defaults to the `agent` setting, else built-in catch-all `claude` agent |
| `--dangerously-skip-permissions` | Shorthand for `--permission-mode bypassPermissions` |
| `--allow-dangerously-skip-permissions` | Makes `bypassPermissions` available in each session's `Shift+Tab` cycle |
| `--restricted` | Start every dispatched session in restricted mode (v2.1.248+) |

Active defaults show in the footer. Bypass flags show the disclaimer if not yet accepted; `bypassPermissions` needs that acceptance on record.

# Limits and defaults

Persisted across supervisor restarts: permission mode, model, effort, carried flags, mid-session `/model` and `/effort` changes, names set with `/rename`/`Ctrl+R`, and a prompt stashed with `Ctrl+S` while attached (pasted content in the stash does not survive). If effort came from settings rather than a flag, settings are re-read at each process start (`effortLevel` key or `modelSettings` entry). After an auto-update, an away agent view (about an hour) can relaunch itself keeping dispatch defaults (v2.1.274).
