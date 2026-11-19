---
type: "Reference"
title: "Print-mode and output flags"
description: "Flags for non-interactive -p runs: output and input formats, JSON schema, budgets, turn limits, hook events, bare mode, persistence."
resource: "https://code.claude.com/docs/en/cli-reference"
tags: [print-mode, headless, stream-json, budget, bare]
kind: "cli_flag"
maturity: "unlabelled"
since: "2.1.217"
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "--print"
  - "-p"
  - "--output-format"
  - "--input-format"
  - "--json-schema"
  - "--include-partial-messages"
  - "--include-hook-events"
  - "--replay-user-messages"
  - "--prompt-suggestions"
  - "--forward-subagent-text"
  - "CLAUDE_CODE_FORWARD_SUBAGENT_TEXT"
  - "--max-turns"
  - "--max-budget-usd"
  - "--no-session-persistence"
  - "CLAUDE_CODE_SKIP_PROMPT_HISTORY"
  - "--init"
  - "--init-only"
  - "--maintenance"
  - "--bare"
  - "CLAUDE_CODE_SIMPLE"
  - "--exclude-dynamic-system-prompt-sections"
  - "--append-subagent-system-prompt"
  - "--append-subagent-system-prompt-file"
  - "--verbose"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "cli-reference"
    resource: "https://code.claude.com/docs/en/cli-reference"
    title: "CLI reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Flags that shape unattended `claude -p` runs: what is emitted, what limits apply, and how fast and cacheable the start is.

# How to use it

| Flag | Needs | What it does |
| :- | :- | :- |
| `--print`, `-p` | | Print the response without interactive mode |
| `--output-format` | print | `text`, `json`, `stream-json` |
| `--input-format` | print | `text`, `stream-json` |
| `--json-schema` | print | Validated JSON output matching a schema after the workflow completes; invalid schema exits with an error; `format` keyword accepted as annotation only |
| `--include-partial-messages` | `--print`, `stream-json` | Include partial streaming events |
| `--include-hook-events` | `stream-json` | Include hook lifecycle events. `SessionStart` and `Setup` events are always included. `Notification`, `SessionEnd`, `PreCompact`, `PostCompact` never produce `hook_started`; `hook_progress` still appears for command hooks running over a second, `hook_response` only for background hooks |
| `--replay-user-messages` | stream-json both ways | Re-emit stdin user messages on stdout for acknowledgment |
| `--prompt-suggestions` | `--print`, `stream-json`, `--verbose` | Emit a `prompt_suggestion` message after turns that produce one |
| `--forward-subagent-text` | `--print`, `stream-json`; v2.1.211+ | Emit subagent text and thinking blocks as `assistant`/`user` messages with `parent_tool_use_id`; foreground subagents' text is omitted without it. Env var `CLAUDE_CODE_FORWARD_SUBAGENT_TEXT` does the same |
| `--max-turns` | print | Limit agentic turns; no limit by default. With `stream-json` input a queued message starts a new turn with its own limit |
| `--max-budget-usd` | print | Stop when estimated spend reaches the amount. Uses a client-side estimate that can differ from the bill; subagent spend counts; spend can pass the cap; totals restored by `--continue`/`--resume` do not count. At the cap, spawning a subagent fails with `Budget limit reached` and running background subagents are stopped (v2.1.217+) |
| `--no-session-persistence` | print | Do not save the session to disk; it cannot be resumed. `CLAUDE_CODE_SKIP_PROMPT_HISTORY` does the same in any mode |
| `--init` | print | Run Setup hooks with the `init` matcher before the session |
| `--init-only` | | Run Setup and `SessionStart` hooks, then exit |
| `--maintenance` | print | Run Setup hooks with the `maintenance` matcher |
| `--bare` | | Minimal mode: skip auto-discovery of hooks, skills, custom commands, subagents, plugins, MCP servers, auto memory and CLAUDE.md; keeps Bash, file read and edit tools; skills from `--add-dir` still load. Sets `CLAUDE_CODE_SIMPLE` |
| `--exclude-dynamic-system-prompt-sections` | default system prompt only | Move per-user context (such as auto memory location) into the first user message to improve prompt-cache reuse across users and machines; ignored with `--system-prompt` or `--system-prompt-file` |
| `--append-subagent-system-prompt` | `-p`; v2.1.205+ | Append text to every subagent's system prompt, nested ones included, except forked subagents |
| `--append-subagent-system-prompt-file` | `-p`; v2.1.261+ | File form for long text; cannot be combined with the inline flag |
| `--verbose` | | Verbose turn-by-turn logging; overrides the `viewMode` setting |
