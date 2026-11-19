---
type: "Feature"
title: "UserPromptSubmit hook event"
description: "Runs before Claude processes a prompt; can add context, set the session title or block the prompt."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, userpromptsubmit, prompts, blocking]
kind: "hook"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "UserPromptSubmit"
  - "prompt"
  - "decision"
  - "reason"
  - "additionalContext"
  - "sessionTitle"
  - "suppressOriginalPrompt"
  - "onFailure"
  - "timeout"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Runs when a prompt is submitted, before Claude processes it. It also fires for: a session-scoped scheduled task firing (including a `/loop` iteration), a background subagent reporting back to the session that started it, a message another session sends to your main conversation, and (before v2.1.328) the output of code Claude runs in a Code Mode session for `command`, `http` and `mcp_tool` hooks.

# How to use it

Input adds `prompt` (pasted content arrives expanded; in sessions that mark pasted text it sits between `<pasted_content id="...">` lines) and `session_title` when a custom title exists. A typed skill/custom command such as `/deploy staging` arrives as typed, not expanded; if blocked, the command and its `` !`cmd` `` injections do not run. Use [UserPromptExpansion](./p2-userpromptexpansion-event.md) to match command names.

Context: plain stdout on exit 0, or JSON `additionalContext`; each is injected as a system reminder starting with the hook's name, with no visible transcript entry.

| Output field | Description |
| :- | :- |
| `decision` | `"block"` stops the prompt; omit to allow |
| `reason` | Shown to the user on block; not added to context |
| `additionalContext` | Added to Claude's context with the prompt |
| `sessionTitle` | Names the session from prompt content |
| `suppressOriginalPrompt` | `true` leaves the prompt text out of the block message |

Exit 2 treats stderr like `reason`.

# Limits and defaults

- Default `timeout` is 30 seconds for `command`, `http`, `mcp_tool` (others default to 600 s).
- On timeout (except an `async: true` command hook) the hook is cancelled, its output including `additionalContext` is discarded and the prompt still reaches Claude. Set `onFailure: "block"` on a command or HTTP hook to block instead. The transcript shows a notice.
- An Agent SDK callback hook that times out blocks the prompt (fail closed) and the session continues.
- `Esc` or interrupt during the check stops it and the prompt does not reach Claude; text returns to input. If a hook blocks at the same moment, the block stands.
- A blocked prompt's block message ends with `Original prompt:` plus the text and is written to the transcript file; `suppressOriginalPrompt: true` (works with `decision: "block"` or exit 2) omits it. The text can still appear in transcript and prompt history, so blocking is not a way to keep a secret off disk.
