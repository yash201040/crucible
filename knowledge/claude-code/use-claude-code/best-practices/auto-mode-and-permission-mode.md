---
type: "Feature"
title: "Choosing a permission mode and tuning auto mode"
description: "Manual, bypassPermissions and auto mode tradeoffs, classifier block thresholds, and the autoMode settings block with $defaults."
resource: "https://code.claude.com/docs/en/best-practices"
tags: [auto-mode, permissions, classifier, automode, settings]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli, ide, headless]
requires: ""
identifiers:
  - "autoMode"
  - "autoMode.environment"
  - "autoMode.allow"
  - "soft_deny"
  - "$defaults"
  - "/auto-mode-setup"
  - "/permissions"
  - "/fewer-permission-prompts"
  - "--permission-mode manual"
  - "bypassPermissions"
  - "Shift+Tab"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "best-practices"
    resource: "https://code.claude.com/docs/en/best-practices"
    title: "Best practices for Claude Code"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Manual mode: you approve every non-read-only edit and command. `bypassPermissions`: approves everything deny and ask rules do not cover; only sensible in a disposable container. Auto mode sits between: a separate classifier checks actions in a fixed order before they run and concentrates on `curl | bash`, production deploys and migrations, force pushes over others' work, sensitive data sent externally, and actions that look driven by content Claude read rather than by you. Interactive terminal and VS Code sessions start in auto mode.

# How to use it

- Blocked actions notify you and appear under **Recently blocked** in `/permissions`, where you can approve for retry.
- After three blocks in a row (or twenty in total), auto mode pauses and asks you again (interactive).
- Deny and ask rules and `PreToolUse` hooks run before the classifier, so a deny rule blocks in auto mode as everywhere. The sandbox still confines shell commands.
- Saying `don't push until I've reviewed` is treated as a block signal, but it can be lost at compaction; use a deny rule for anything that matters.
- Tune with the `autoMode` block in `~/.claude/settings.json`, using plain English entries; `/auto-mode-setup` can draft `environment`.

```json
{ "autoMode": { "environment": ["$defaults", "Trusted internal domains: *.internal.example.com"],
                "allow": ["$defaults", "Deploying to the staging namespace is fine"] } }
```

- `Shift+Tab` cycles modes; `claude --permission-mode manual` starts in Manual. `/fewer-permission-prompts` scans transcripts for common read-only Bash and MCP calls and adds an allowlist to `.claude/settings.json`.

# Limits and defaults

Keep `"$defaults"` in every list, otherwise your entries can replace built-in rules (losing built-in `environment` context, `allow` exceptions and the `soft_deny` blocks on force pushes and production deploys). The classifier ignores `autoMode` in project settings, so it must be in `~/.claude/settings.json`. Your org can turn auto mode off.
