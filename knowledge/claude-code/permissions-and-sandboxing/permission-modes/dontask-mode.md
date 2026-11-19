---
type: "Feature"
title: "dontAsk mode"
description: "Auto-denies every call that would prompt; only pre-approved tools and no-approval actions run, for CI and scripts."
resource: "https://code.claude.com/docs/en/permission-modes"
tags: [dontask, permissions, ci, headless, deny]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "dontAsk"
  - "--permission-mode dontAsk"
  - "AskUserQuestion"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permission-modes"
    resource: "https://code.claude.com/docs/en/permission-modes"
    title: "Choose a permission mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`dontAsk` auto-denies every tool call that would otherwise prompt (an installed mod can still approve some). Claude still runs what needs no approval in Manual mode: reads inside working directories, read-only Bash, calls matching `permissions.allow`, and calls approved by a `PreToolUse` hook. The session never waits for input. Status bar: `⏵⏵ don't ask on`.

# How to use it

`claude --permission-mode dontAsk` (never in the `Shift+Tab` cycle).

# Limits and defaults

- Calls matching explicit `ask` rules are denied, not prompted. `AskUserQuestion` is denied even with an allow rule; so are org-`ask` connector tools and MCP tools marked `_meta["anthropic/requiresUserInteraction"]`.
- An allow rule or `PreToolUse` hook cannot approve recognized `rm`/`rmdir` critical-path removals or network-path reads.
- Protected-path writes are denied.
- Cloud sessions ignore `defaultMode: "dontAsk"`.
