---
type: "Concept"
title: "Tool call denied after a hook changed input"
description: "In auto mode a call is denied when a mod or PreToolUse hook changed its input after the classifier reviewed it."
resource: "https://code.claude.com/docs/en/plugins/mods/troubleshoot"
tags: [auto-mode, permissions, hooks, classifier]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, ide]
requires: "auto mode"
identifiers:
  - "a hook changed this call's input after the model wrote it"
  - "a hook changed this call's input after auto mode reviewed it"
  - "tool.call"
  - "turn.step"
  - "PreToolUse"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-troubleshoot"
    resource: "https://code.claude.com/docs/en/plugins/mods/troubleshoot"
    title: "Troubleshoot a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

In auto mode a denied tool call may carry the reason `a hook changed this call's input after the model wrote it`. A hook changed the input after the server-side classifier reviewed it, so the review does not cover what would run. The hook can be a mod's `tool.call` or `turn.step` hook, or a `PreToolUse` settings hook; the message does not say which.

# How to use it

The message tells Claude to issue the call again as recorded. If that is denied too, the hook changes the input every time: turn off the mod or hook, or leave auto mode and approve the call yourself.

# Notes

In some interactive terminal sessions and VS Code sessions, the same denial reads `a hook changed this call's input after auto mode reviewed it`. The repeated call there carries the mod's first change, a `tool.call` hook still runs on it, but a further change is dropped. No change is needed unless Claude's reply says auto mode could not check the call.
