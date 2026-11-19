---
type: "Limit"
title: "Exec wrappers and find actions"
description: "Prefix rules cannot auto-approve exec wrappers such as watch or find with -exec/-delete; use exact rules or a PreToolUse hook."
resource: "https://code.claude.com/docs/en/permissions"
tags: [permissions, bash, find, limits]
kind: "limit"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "watch"
  - "setsid"
  - "ionice"
  - "flock"
  - "-exec"
  - "-delete"
  - "-rm"
  - "-fprint"
  - "-files0-from"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permissions"
    resource: "https://code.claude.com/docs/en/permissions"
    title: "Configure permissions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A prefix rule like `Bash(watch *)` or `Bash(find *)` cannot auto-approve these, so Manual mode prompts:
- Exec wrappers such as `watch`, `setsid`, `ionice`, `flock`.
- `find` with an action that runs commands, deletes or writes files (`-exec`, `-delete`, `-rm`, `-fprint`) or with `-files0-from`.

# How to use it

For one specific invocation with no `*` write an exact-match rule, for example `Bash(find build -type f -delete)`. If the command contains a `*` (such as `find . -name '*.tmp' -delete`), it is read as a wildcard pattern, not exact, and still prompts. Approve each time or use a PreToolUse hook returning `"allow"`.
