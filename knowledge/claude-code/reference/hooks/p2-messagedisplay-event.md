---
type: "Feature"
title: "MessageDisplay hook event"
description: "Rewrites assistant text as it streams to the screen; display-only, transcript and Claude keep the original."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, messagedisplay, redaction, display]
kind: "hook"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "MessageDisplay"
  - "displayContent"
  - "turn_id"
  - "message_id"
  - "index"
  - "final"
  - "delta"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Runs while an assistant message streams to the screen. Each batch of newly completed lines calls the hook once and the hook's replacement text is rendered in their place. Use to strip markdown, transform text an Agent SDK app shows, or redact keys and hostnames.

# How to use it

Input adds `turn_id` (turn UUID), `message_id` (message UUID, stable across batches, not the API `msg_` id), `index` (zero-based batch index), `final` (true on last batch; exactly one per message), `delta` (new lines, always whole lines except possibly the final batch; in interactive runs the final delta is empty if the message ended on a newline, so rely on `final`).

Return `hookSpecificOutput.displayContent` to replace the delta; omit to show the original. Example: `jq '{hookSpecificOutput: {hookEventName: "MessageDisplay", displayContent: (.delta | gsub("\\*\\*"; ""))}}'`.

# Limits and defaults

- Display-only: transcript and what Claude sees keep the original; verbose mode shows the original. Only assistant text is passed, not tool results or typed text.
- No matcher; fires for every streaming assistant message with text (not tool-call-only ones). No decision control; `systemMessage` and `continue` are discarded.
- Default timeout 10 seconds. On failure or timeout, the original text is shown; failures note only in debug output.
- Non-interactive runs (Agent SDK queries, `claude -p`): one call per assistant message after completion, `index` 0, `final` true, `delta` holds the entire message.
