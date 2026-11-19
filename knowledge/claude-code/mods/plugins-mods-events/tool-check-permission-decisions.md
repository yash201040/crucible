---
type: "Feature"
title: "tool.check: approve or refuse before the user is asked"
description: "A tool.check hook decides allow, ask or deny for a tool call before prompts, auto mode and PermissionRequest hooks, with an isReadOnly field."
resource: "https://code.claude.com/docs/en/plugins/mods/events"
tags: [mods, permissions, tool-check, read-only]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.304"
surfaces: [cli, desktop, ide]
requires: ""
identifiers:
  - "tool.check"
  - "e.input"
  - "e.isReadOnly"
  - "{ decision: 'allow' }"
  - "{ decision: 'deny', reason }"
  - "isReadOnly: true"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-events"
    resource: "https://code.claude.com/docs/en/plugins/mods/events"
    title: "React to events with a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`tool.check` is where Claude Code decides whether a tool call may run. `await next(e)` returns Claude Code's own decision, an object whose `decision` is `allow`, `ask` or `deny` (no permission prompt appears while it runs). `e.input` holds the tool's arguments. It fires after `PreToolUse` hooks and before the permission prompt, auto mode's classifier, or a `PermissionRequest` hook.

For fixed commands or paths a permission rule such as `Bash(npm test)` needs no code; use `tool.check` when the decision depends on live state (e.g. current Git branch).

# How to use it

Return your own object (`{ decision: 'allow' }` or `{ decision: 'deny', reason }`) or return what `await next(e)` gave. Example: deny `git push` while the branch is `main`, using `$.process.run(['git','branch','--show-current'])`.

`e.isReadOnly` is `true` when the tool reports the call read-only; otherwise absent (not `false`). Read, Grep, Glob, WebSearch always report read-only; Bash reports it if the command passes the built-in read-only check; MCP tools if the server sets `readOnlyHint: true`. WebFetch and Agent also report read-only, so do not approve on this field alone. Filter with a matcher `{ tool: 'Bash', isReadOnly: true }`; `isReadOnly: false` in a matcher means the hook never runs, so test it in the body.

# Limits and defaults

- If the hook throws or times out, the call gets the decision it would get without the mod; to fail closed use `.catch` returning `{ decision: 'deny', reason }`.
- In plan mode, for a call that is not read-only, a hook can tighten the decision but not loosen it.
- `e.isReadOnly` requires v2.1.304 or later.
- The hook matches command text, so treat it as a reminder for Claude, not a hard block.
