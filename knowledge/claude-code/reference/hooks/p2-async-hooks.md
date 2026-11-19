---
type: "Feature"
title: "Async (background) command hooks"
description: "async: true runs a command hook in the background without blocking; output is delivered on a later turn."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, async, background, headless]
kind: "hook"
maturity: "unlabelled"
since: "2.1.295"
surfaces: [cli, headless]
requires: ""
identifiers:
  - "async"
  - "asyncRewake"
  - "additionalContext"
  - "systemMessage"
  - "--verbose"
  - "cancelled"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

By default hooks block Claude until they finish. Setting `"async": true` on a `type: "command"` hook (only available on command hooks) runs it in the background while Claude continues. Async hooks cannot block or control behavior: `decision`, `permissionDecision` and `continue` have no effect because the action already completed.

# How to use it

Add `"async": true` to the hook entry, for example on a `PostToolUse` `Write|Edit` matcher running a test script. The hook gets the same stdin JSON as a synchronous hook. After the process exits, Claude Code delivers `additionalContext` and `systemMessage` from its JSON response to Claude on the next conversation turn (unlike a synchronous hook's `systemMessage`, neither is shown to you). Print the JSON response alone on stdout (may span several lines, requires v2.1.295 or later) or on one line of its own (other stdout text allowed, e.g. `jq -c`). The response is validated against the same output schema as synchronous hooks; fields with the wrong type are dropped, and `--debug` warns for each. Completion notifications are suppressed by default; show them with `Ctrl+O` verbose mode or `--verbose`.

# Limits and defaults

- Once running in the background `timeout` is not enforced, except for a hook run with `asyncRewake`, where it still is.
- Results are delivered only while the session runs. In `-p` mode, any async hook still running at teardown is killed and finalized with outcome `cancelled`; for work that must outlive a `claude -p` session start a fully detached process.
- Output waits for the next conversation turn when idle, except an `asyncRewake` hook exiting with code 2, which wakes Claude immediately even when idle.
- Each execution is a separate background process.
- An async `SessionStart` hook runs every time the event fires. Its output is skipped when the `additionalContext` and `systemMessage` text matches what Claude last received from that hook (unless a synchronous SessionStart hook added other text since); delivered again when changed, and after a compaction or `/clear`. Before v2.1.295 the same text was re-added on every resume.
