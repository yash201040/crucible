---
type: "Feature"
title: "Send no effort level"
description: "Set CLAUDE_CODE_EFFORT_LEVEL to auto or unset so the API default applies; how to confirm with /effort status."
resource: "https://code.claude.com/docs/en/model-config#send-no-effort-level"
tags: [effort, env-var, api-default]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "CLAUDE_CODE_EFFORT_LEVEL"
  - "/effort status"
  - "maxEffortLevel"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "model-config"
    resource: "https://code.claude.com/docs/en/model-config"
    title: "Model configuration"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

When Claude Code sends no effort level to a supported model, the API's default applies instead of Claude Code's.

# How to use it

Start `claude` from a shell with `export CLAUDE_CODE_EFFORT_LEVEL=auto` (or `unset`; identical). The header and footer show no effort level. Confirm with `/effort status`:
- `Effort level: auto` means none is sent.
- `Effort level: auto (currently <level>)` means a level is still sent: a `maxEffortLevel` below `max` applies, so Claude Code sends its default lowered to that cap. Remove the setting or set it to `max`.

# Notes

Before v2.1.304, `/effort status` printed `Effort level: auto (currently high)` even when none was sent.
