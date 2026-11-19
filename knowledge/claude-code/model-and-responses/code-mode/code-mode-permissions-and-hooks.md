---
type: "Feature"
title: "Code Mode permission checks and hooks"
description: "How permission rules, PreToolUse and PostToolUse hooks and the auto mode classifier apply to code that Code Mode runs."
resource: "https://code.claude.com/docs/en/code-mode"
tags: [code-mode, permissions, hooks, auto-mode]
kind: "hook"
maturity: "experimental"
since: "2.1.328"
surfaces: [cli]
requires: "Code Mode on"
identifiers:
  - "PreToolUse"
  - "PostToolUse"
  - "UserPromptSubmit"
  - "REPL"
  - "tool_input.code"
  - "tool_response"
  - "updatedToolOutput"
  - "refusedCalls"
  - "images"
  - "documents"
  - "poll_event"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "code-mode"
    resource: "https://code.claude.com/docs/en/code-mode"
    title: "Run tool calls from code with Code Mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Each tool call made by Code Mode code goes through your `deny` and `ask` permission rules and `PreToolUse` hooks under the tool's usual name (such as `Bash`). Beyond that, the mode decides review.

# How to use it

- **Auto mode**: the classifier reviews each piece of code before it runs, not each tool call, and does not see run-time values (such as a path from search output); keep rules or hooks for calls you must control.
- **Other modes**: code starts without review; you are prompted for each tool call that would prompt in that mode.
- Compound commands: a `git push` in folder `app` can reach a hook as `cd 'app' && git push`; make shell-command hooks check each part. Bash rules still match command text only (use sandboxing for limits that do not).
- Check the code: a `PreToolUse` hook matching `REPL`, reading JavaScript from `tool_input.code`.
- Check or redact the output: a `PostToolUse` hook matching `REPL`; `tool_response` has `code`, `result`, `stdout`, `stderr`, `toolsUsed` (and `error` only when the code failed or was stopped; `images` / `documents` may appear). Return a changed copy as `hookSpecificOutput.updatedToolOutput`: redact `result`, `stdout`, `stderr`, `error`; handle a missing or `null` `result`; keep `code`, `stdout`, `stderr` strings and `error` a string or absent (a broken shape makes Claude get the original output); set `images` or `documents` to `[]` to hide them.

# Limits and defaults

- The same `PostToolUse` hook runs for background code on finish and for code that throws.
- Return `updatedToolOutput` even when the hook blocks, or Claude still reads the output.
- If the hook crashes, times out or prints invalid JSON, Claude gets the original output; on your own errors return placeholder text in redacted fields.
- Do not rely on it to hide values in a refused call's input (`refusedCalls` can repeat it).
- On v2.1.328 or later, `UserPromptSubmit` hooks do not receive code output, even from managed settings; move such checks to `PostToolUse`. Before that, a hook that blocks produces `UserPromptSubmit operation blocked by hook` in place of output; stay on an old version by not blocking when `source` in the hook input is `poll_event`.
