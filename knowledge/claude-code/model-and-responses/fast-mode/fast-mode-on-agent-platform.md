---
type: "Feature"
title: "Fast mode on Google Cloud Agent Platform"
description: "Fable 5.2 fast mode on Agent Platform needs v2.1.322, a global/us/eu region, and launch flags in non-interactive mode."
resource: "https://code.claude.com/docs/en/fast-mode"
tags: [fast-mode, vertex, agent-platform, headless]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.322"
surfaces: [cli, headless]
requires: "Claude Code v2.1.322+; Fable 5.2; region global, us or eu"
identifiers:
  - "VERTEX_REGION_CLAUDE_FABLE_5_2"
  - "claude-fable-5-2"
  - "--model"
  - "--settings"
  - "/fast on"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "fast-mode"
    resource: "https://code.claude.com/docs/en/fast-mode"
    title: "Speed up responses with fast mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

On Google Cloud's Agent Platform, fast mode works for Fable 5.2. Here `/fast` and the `fastMode` setting behave differently from the Anthropic API.

# How to use it

- Set the region before starting Claude Code: `export VERTEX_REGION_CLAUDE_FABLE_5_2=global` (must be `global`, `us` or `eu`; in another region `/fast` reports `Fast mode needs Vertex region global, us or eu` and `claude -p` runs at standard speed).
- Interactive: run `/fast`; it switches you to Fable 5.2 from an Opus or other model without fast mode there. Not saved as default.
- Non-interactive: `claude -p "Summarize this project" --model claude-fable-5-2 --settings '{"fastMode": true}'`.
- `"fastMode": true` in user, project, local or managed settings has no effect on Agent Platform.

# Limits and defaults

If Agent Platform refuses fast mode, Claude Code falls back to standard speed. Interactive messages: `Using standard speed on Fable 5.2 · fast mode wasn't available` (run `/fast on` to retry); `Fast mode paused: your cloud provider refused a fast request · trying again in 30m` (provider answered 403 or 404; run `/fast on` to retry sooner; requires v2.1.323+).
