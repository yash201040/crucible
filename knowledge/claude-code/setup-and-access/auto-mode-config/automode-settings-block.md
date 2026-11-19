---
type: "Reference"
title: "autoMode settings block and scopes"
description: "The autoMode keys, which settings scopes the classifier reads, merging, the $defaults token and precedence tiers."
resource: "https://code.claude.com/docs/en/auto-mode-config"
tags: [auto-mode, classifier, settings, permissions]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli, sdk]
requires: ""
identifiers:
  - "autoMode"
  - "autoMode.environment"
  - "autoMode.allow"
  - "autoMode.soft_deny"
  - "autoMode.hard_deny"
  - "autoMode.classifyAllShell"
  - "$defaults"
  - "permissions.ask"
  - "permissions.deny"
  - "--settings"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "auto-mode-config"
    resource: "https://code.claude.com/docs/en/auto-mode-config"
    title: "Configure auto mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Auto mode routes tool calls through a classifier that blocks irreversible, destructive or out-of-environment actions. By default it trusts only the working directory and the repo's configured remotes. `autoMode` tells it what else is trusted. Deny and explicit ask rules run before the classifier.

# How to use it

| Key | Purpose |
| :- | :- |
| `autoMode.environment` | prose entries: trusted repos, buckets, domains, services (the main field) |
| `autoMode.hard_deny` | block even when the user asks |
| `autoMode.soft_deny` | destructive actions user intent can clear |
| `autoMode.allow` | exceptions to soft_deny |
| `autoMode.classifyAllShell` | `true` suspends Bash/PowerShell allow rules while auto mode (and plan-mode classifier review) is active |

Include the literal `"$defaults"` in a list to keep built-in entries; include it in every list you set. Each list is evaluated independently.

Scopes read: `~/.claude/settings.json`, managed settings, and `--settings` / Agent SDK inline JSON (per-invocation automation overrides). Project `.claude/settings.json` and `.claude/settings.local.json` are NOT read (a repo could inject allow rules). Entries combine across scopes; developers can extend but not remove managed entries, and a developer `allow` can override an organization `soft_deny`.

# Limits and defaults

- Precedence: `hard_deny` > `soft_deny` > `allow` exceptions > explicit user intent (message specifically names the exact action).
- Human checkpoint: `permissions.ask` such as `Bash(git push *)` and `Bash(gh pr create *)` prompts; it does not match `git -C <dir> push`. Use a PreToolUse hook for full-command inspection. `permissions.deny` blocks before the classifier.
- A boundary stated only in conversation can be lost to context compaction.
- Code Mode: classifier applies hard_deny/soft_deny to each code piece as a whole before it runs; use `permissions.deny` for specific calls.
- Broad allow rules such as `Bash(*)` are dropped in auto mode; narrow ones stay unless `classifyAllShell` is set.
- Available on every provider including Bedrock, Vertex, Foundry, Claude Platform on AWS and gateway sessions.
