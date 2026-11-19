---
type: "Feature"
title: "SessionStart hook event"
description: "Fires when a session starts, resumes, clears, compacts or forks; input carries source, model and resume-cost fields."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, sessionstart, resume, session]
kind: "hook"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless]
requires: ""
identifiers:
  - "SessionStart"
  - "startup"
  - "resume"
  - "clear"
  - "compact"
  - "fork"
  - "source"
  - "model"
  - "agent_type"
  - "session_title"
  - "seconds_since_last_response"
  - "context_tokens"
  - "prompt_cache_likely_expired"
  - "estimated_cache_write_usd"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Runs when Claude Code starts a new session or resumes one. Meant for loading context (issues, recent changes) or setting environment variables. Static context belongs in CLAUDE.md instead. It runs on every session, so keep hooks fast. Only `type: "command"` and `type: "mcp_tool"` hooks are supported.

# How to use it

Matcher values (how the session began):

| Matcher | Fires on |
| :- | :- |
| `startup` | New session |
| `resume` | `--resume`, `--continue`, `/resume` |
| `clear` | `/clear` |
| `compact` | Auto or manual compaction |
| `fork` | `--fork-session` with `--resume`/`--continue`, the `/fork` background copy, `/branch`, or a conversation moved to the background |

Input fields beyond the common ones: `source` (same five values), `model` (may be omitted, e.g. after `/clear` or conversation recovery), `agent_type` (present with `claude --agent <name>`), `session_title` (present when a custom title exists via `--name`, `/rename`, a hook's `sessionTitle`, or the SDK's `renameSession()`; a generated title is not included).

When `source` is `resume` or `fork` and the transcript has at least one Claude response, four extra fields arrive (Claude Code v2.1.251 or later):

| Field | Meaning |
| :- | :- |
| `seconds_since_last_response` | Wall-clock seconds since last response |
| `context_tokens` | Tokens the first request re-sends as its prompt |
| `prompt_cache_likely_expired` | `true` if the last response is older than the prompt cache lifetime or a later compaction replaced the cached conversation |
| `estimated_cache_write_usd` | Estimated dollar cost of writing `context_tokens` to the cache on the session's model, excluding the response |

# Limits and defaults

- In interactive start, `--continue`/`--resume` and `/clear`, hooks run in the background; you can type, but Claude's first response still waits for them. A prompt sent while they run does not reach Claude until they finish. `Esc` takes the prompt back; hooks keep running.
- With `/resume` inside a session, the switch waits for the hooks.
- If you `/clear` or switch conversation while background hooks run, nothing they return applies.

See [SessionStart output](./p2-sessionstart-output.md) for what a hook can return.
