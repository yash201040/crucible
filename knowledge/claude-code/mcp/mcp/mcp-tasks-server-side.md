---
type: "Feature"
title: "MCP tasks that run on the server"
description: "Public-beta MCP tasks extension: long server-run jobs, footer count, resume behavior, requirements and status messages."
resource: "https://code.claude.com/docs/en/mcp"
tags: [mcp, tasks, beta, resume, headless]
kind: "behavior"
maturity: "beta"
since: "2.1.304"
surfaces: [cli, sdk]
requires: "Claude Code v2.1.304 or later; server on protocol revision 2026-07-28"
identifiers:
  - "CLAUDE_CODE_DISABLE_MCP_TASK_BACKGROUND"
  - "CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS"
  - "CLAUDE_AUTO_BACKGROUND_TASKS"
  - "--input-format stream-json"
  - "--resume"
  - "--continue"
  - "--fork-session"
  - "/tasks"
  - "Elicitation"
  - "onElicitation"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "mcp"
    resource: "https://code.claude.com/docs/en/mcp"
    title: "Connect Claude Code to tools via MCP"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

An MCP task is a long job (report export, build) that the server runs itself via the MCP tasks extension. Claude's tool call returns once the server accepts the job; the footer shows a count such as `1 MCP task`; when it ends the transcript says `MCP task <server task id> (<server>/<tool>) completed.` and the result goes to Claude (not the transcript). If Claude is idle it starts on the result unprompted. A task on a remote server keeps running after you exit; a stdio server's process stops when Claude Code exits.

Labelled public beta in the CLI; requires v2.1.304 or later.

# How to use it

- Stop: select it in `/tasks` and press `x`, or ask Claude. Claude Code asks the server to cancel (it may still finish) and cannot follow the task again. `Esc` does not stop a background task. Reconnect a disconnected server from `/mcp` first so the cancel can go out.
- Questions: a task can open an elicitation dialog; close `/tasks` to answer; `Esc` defers it unless Claude is set to wait; reopen via `/tasks` details and Enter (answering later needs v2.1.324 or later). In non-interactive sessions the server is asked to cancel a task requesting input, without running `Elicitation` hooks or the SDK `onElicitation` callback.
- Make Claude wait (interactive): set `CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS=0` (waits for every MCP call) or `CLAUDE_CODE_DISABLE_MCP_TASK_BACKGROUND=1` (waits for a task's result; with automatic backgrounding on, the call moves after two minutes as a plain background call that does not survive exit). While waiting, `Esc` or the wall-clock/idle limit ends the call and asks the server to cancel. `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1` or bare mode alone does not make Claude wait.

| Situation | Result |
|---|---|
| `/clear`, `/branch`, `/resume` another session while open | result arrives in the current conversation |
| exit | no option cancels a remote task; stop in `/tasks` first or resume later |
| `claude --resume`, `--continue`, `/resume` interactively | task followed again once the server connects, if server name and connection settings unchanged |
| `--resume`/`--continue` in one-shot `claude -p "<prompt>"` | not followed; resume interactively or with `--input-format stream-json` |
| new session or `--fork-session` | not followed |

# Limits and defaults

A call becomes an MCP task only when all hold: server supports tasks; HTTP, stdio or claude.ai connector server on protocol revision 2026-07-28 (not with `MCP_SDK_GENERATION=v1` or `MCP_PROTOCOL_NEGOTIATION=legacy`); the session fetches feature flags (not Bedrock-style third-party providers, not telemetry or flags off); Anthropic enabled it for the session kind (v2.1.304+: terminal CLI, Agent SDK, GitHub Actions; not VS Code extension or desktop app); the call is from the main conversation, not a subagent; and the session is interactive, or an Agent SDK / `claude -p --input-format stream-json` run with `CLAUDE_AUTO_BACKGROUND_TASKS=1`, `CLAUDE_CODE_DISABLE_MCP_TASK_BACKGROUND` not `1` and `CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS` not `0`. A one-shot `claude -p "<prompt>"` run gets no MCP tasks; keep SDK/stream-json input open because the run does not wait for MCP tasks after input closes. A background task has no Claude Code time limit by default; call limits apply until the server answers with the task, and for the whole task if Claude waits. Answered status checks count as idle activity.

Status messages in `/tasks`:

| Message | Meaning / action |
|---|---|
| `reconnecting…` | no answer since resume; reconnect from `/mcp` if it stays |
| `needs a sign-in to <server>` | status check refused; sign in from `/mcp` |
| `status requests come back with errors; retrying…` | wait |
| `server '<name>' did not reconnect within 300s` | reconnect from `/mcp` |
| `server '<name>' asked for a sign-in, and none was accepted within 300s` | sign in from `/mcp` |
| `status requests to server '<name>' came back with errors, and none succeeded in 300s` | check the server's health |
| `server '<name>' is not configured in this session; the task may still be running on it` | restore the server under the same name, then resume |
| `server '<name>' was reconfigured to a different transport since this task was created` | restore earlier URL/command/args/env/headers/timeout, resume |
| `the server rejected this task's id; asking again…` | retried up to five minutes |
| transcript line ending `outcome unknown.` (for example `expired on the server: outcome unknown.`) | a second call may repeat work; check what the server did first |
