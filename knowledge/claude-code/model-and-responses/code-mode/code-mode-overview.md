---
type: "Feature"
title: "Code Mode overview and limitations"
description: "Experimental mode where Claude writes JavaScript that makes several tool calls in one step, with a list of its limitations."
resource: "https://code.claude.com/docs/en/code-mode"
tags: [code-mode, experimental, tools, javascript]
kind: "behavior"
maturity: "experimental"
since: "2.1.323"
surfaces: [cli]
requires: "Claude Code v2.1.323+; Claude subscription or Console account"
identifiers:
  - "REPL"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "code-mode"
    resource: "https://code.claude.com/docs/en/code-mode"
    title: "Run tool calls from code with Code Mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Instead of asking for each tool call (Bash, Read, Edit) and reading each result, Claude writes JavaScript that makes the tool calls and Claude Code runs it in your session. One piece of code can run commands in parallel, feed one result into the next call and return only the output Claude needs. Docs label it experimental and off by default; it may change or be removed in any release; feedback via `/feedback`.

Example code shape: `await $\`rg -l "..." src\`.text()`, `await edit(target, old, new)`, and a last expression returning an object, with `$\`...\`.nothrow()` for commands allowed to fail. The tool that runs the code is named `REPL`.

# How to use it

Good for: a change repeated across many files; searches whose results need filtering; several independent commands at once. You see the tool calls (such as edit diffs) but not the code; press `Ctrl+O` for the transcript viewer, where each piece of code is a collapsed **Code** row.

# Limits and defaults

- **Resuming**: only in the terminal, with Code Mode on.
- **Auto mode**: its classifier reviews the code, not each tool call.
- **Long-running code**: you wait for it, and it stops after ten minutes, unless it can run in the background (see [long-running code](./long-running-code.md)).
- **Hooks**: tool calls can be refused when a `PreToolUse` hook cannot run or times out.
- **Unavailable**: Remote Control, Claude in Chrome, computer use.
- **Moving the session**: cannot move to the Desktop app or become a background session; `/fork` cannot start a background copy.
