---
type: "Feature"
title: "Monitors in a plugin"
description: "Background shell commands started with the session whose output reaches Claude as notifications; interactive sessions only."
resource: "https://code.claude.com/docs/en/plugins/components"
tags: [plugins, monitors, notifications, background]
kind: "file"
maturity: "unlabelled"
since: "2.1.310"
surfaces: [cli]
requires: "Interactive session; on Bedrock, Claude Platform on AWS, Google Cloud Agent Platform, Foundry, or with telemetry disabled, Claude Code v2.1.310 or later"
identifiers:
  - "monitors/monitors.json"
  - "experimental.monitors"
  - "when"
  - "DISABLE_TELEMETRY"
  - "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC"
  - "-p"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-components"
    resource: "https://code.claude.com/docs/en/plugins/components"
    title: "Add components to a plugin"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A monitor is a shell command that Claude Code starts in the background when the session starts and keeps running until it ends. What it prints reaches Claude as notifications, so Claude can react to a log or status change unasked. A `when` field can instead start it the first time a named skill runs. Entries are a JSON array of `{ name, command, description }` in `monitors/monitors.json`.

# How to use it

The `experimental.monitors` manifest key takes the same array inline or a path to a JSON file and is read instead of `monitors/monitors.json`.

# Limits and defaults

- Runs in a shell in the session's current working directory, with the user's full permissions, outside the sandbox.
- Plugin monitors do not start in non-interactive mode (`-p`).
- On Amazon Bedrock, Claude Platform on AWS, Google Cloud's Agent Platform, Microsoft Foundry, or with `DISABLE_TELEMETRY` or `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` set, monitors need v2.1.310 or later (applies when feature-flag fetching is off).
- `command` gets path variables and `${ENV_VAR}` but never `${user_config.*}`; a monitor referencing one does not start, and monitor processes do not get `CLAUDE_PLUGIN_OPTION_<KEY>`.
- Disabling a plugin mid-session does not stop running monitors; they stop at session end.
