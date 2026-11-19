---
type: "Feature"
title: "CwdChanged hook event"
description: "Fires when a shell command in the main conversation changes directory; can return watchPaths and use CLAUDE_ENV_FILE."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, cwdchanged, direnv, environment]
kind: "hook"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "CwdChanged"
  - "old_cwd"
  - "new_cwd"
  - "watchPaths"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Runs when a shell command in the main conversation changes the working directory (for example Claude runs `cd`). Use to reload environment, activate toolchains or run setup. Pairs with FileChanged for tools like direnv. No matchers. Has access to `CLAUDE_ENV_FILE`; variables persist until the next CwdChanged event, when Claude Code clears them.

# How to use it

Input adds `old_cwd` and `new_cwd`. Output: `watchPaths` (array of absolute paths) replaces the current dynamic FileChanged watch list; paths from `matcher` configuration are always watched; an empty array clears the dynamic list (typical when entering a new directory). Also reads `systemMessage`.

# Limits and defaults

- No decision control; cannot block the directory change. `continue` is discarded.
- In interactive sessions `systemMessage` shows as a brief terminal notification; it does not reach the SDK message stream.
