---
type: "Feature"
title: "Defer a tool call for later (-p)"
description: "A PreToolUse hook returns defer so a claude -p run pauses at a tool call and resumes later with the answer."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, headless, resume, defer]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.246"
surfaces: [headless, sdk]
requires: "non-interactive mode (-p)"
identifiers:
  - "defer"
  - "tool_deferred"
  - "tool_deferred_unavailable"
  - "deferred_tool_use"
  - "--resume"
  - "--permission-prompt-tool"
  - "--permission-mode"
  - "--dangerously-skip-permissions"
  - "CLAUDE_CODE_DROP_UNAVAILABLE_DEFERRED_TOOL"
  - "cleanupPeriodDays"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`permissionDecision: "defer"` is for integrations that run `claude -p` as a subprocess and read its JSON output (an Agent SDK app or a custom UI). It lets the caller pause Claude at a tool call, collect input through its own interface, and resume. Honored only in `-p` mode and only when Claude makes a single tool call in the turn; in interactive sessions it logs a warning and ignores the result, and with several tool calls at once it is ignored with a warning and the normal permission flow applies.

# How to use it

1. Claude calls the tool (typically `AskUserQuestion`, which needs a permission host such as `--permission-prompt-tool`); PreToolUse fires.
2. Hook returns `"defer"`. The tool does not run; the result has `stop_reason: "tool_deferred"` and the pending call stays in the transcript.
3. The caller reads `deferred_tool_use` (`id`, `name`, `input`) from the SDK result and gets an answer.
4. The caller runs `claude -p --resume <session-id>` with the same permission host; PreToolUse fires again.
5. Hook returns `"allow"` with the answer in `updatedInput`; the tool runs and Claude continues.

If the answer is not ready the hook can return `"defer"` again. A prompt sent with that resume is answered without the tool's result and the call does not run, so resume without a prompt until the hook returns `allow` or `deny`.

To resume a deferred session in plan mode pass `--permission-prompt-tool` with `--resume` (v2.1.246 or later). Resuming with `-p` does not restore a stored permission mode: pass `--permission-mode` or `--dangerously-skip-permissions` again.

Unavailable tool: a result with `stop_reason: "tool_deferred_unavailable"` (tool not available in the resumed session, e.g. MCP server not connected; PreToolUse does not fire; `deferred_tool_use` names the tool). Any prompt then does not reach Claude and the run exits with code 1; `result` starts with `<tool> isn't available, so its deferred call didn't run.` Make the tool available and resume, or drop the call by resuming with a prompt and `CLAUDE_CODE_DROP_UNAVAILABLE_DEFERRED_TOOL=1` (Claude gets an error as the call's result; a second result carries its answer; exit 0 unless the answer is an error; with no prompt it drops the call and exits 1).

# Limits and defaults

- No timeout or retry limit. The session stays on disk until the `cleanupPeriodDays` retention sweep deletes it, after 30 days by default.
- Before v2.1.319, Claude Code answered a prompt without the tool's result and dropped the call; send a new prompt once the tool is available.
