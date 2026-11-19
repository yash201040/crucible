---
type: "Feature"
title: "Turning workflows off"
description: "Disable workflows per user or organization via /config, disableWorkflows or CLAUDE_CODE_DISABLE_WORKFLOWS."
resource: "https://code.claude.com/docs/en/workflows"
tags: [workflows, disable, managed-settings, ultracode]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop, ide, headless, sdk]
requires: ""
identifiers:
  - "disableWorkflows"
  - "CLAUDE_CODE_DISABLE_WORKFLOWS"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "workflows"
    resource: "https://code.claude.com/docs/en/workflows"
    title: "Orchestrate subagents at scale with dynamic workflows"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Workflows are available in the CLI, Desktop app, IDE extensions, `claude -p` and the Agent SDK; the same disable settings apply everywhere.

# How to use it

Yourself: toggle Dynamic workflows off in `/config`; `"disableWorkflows": true` in `~/.claude/settings.json`; or `CLAUDE_CODE_DISABLE_WORKFLOWS=1` (read at startup).
Organization: `"disableWorkflows": true` in managed settings, or the toggle on the Claude Code admin settings page.

# Limits and defaults

- When disabled: `/workflows`, workflow commands and the `/workflow-authoring` skill are unavailable; the `ultracode` keyword stops triggering and the Ultracode toggle leaves `/effort`. A run already in progress continues.
- Disabling workflows also makes ultracode unavailable. No managed setting disables ultracode alone; an effort cap lowers the effort a session with ultracode runs at but does not turn it off.
