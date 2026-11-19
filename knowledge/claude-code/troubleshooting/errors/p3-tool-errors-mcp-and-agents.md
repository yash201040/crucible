---
type: "Reference"
title: "Tool errors: MCP calls, subagent tools, Agent tool, teams"
description: "Tool-result errors for unknown tools, lost MCP connections, disabled servers, elicitation timeouts, zero-tool subagents, subagent_type, and agent team inbox failures."
resource: "https://code.claude.com/docs/en/errors"
tags: [errors, subagents, mcp, agent-teams, tools]
kind: "tool"
maturity: "unlabelled"
since: "2.1.208"
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "tools"
  - "disallowedTools"
  - "background: true"
  - "subagent_type"
  - "Agent"
  - "Agent(...)"
  - "general-purpose"
  - "CLAUDE_AGENT_SDK_DISABLE_BUILTIN_AGENTS"
  - "CronCreate"
  - "Elicitation"
  - "onElicitation"
  - "shutdown_request"
  - "teammateMode"
  - "~/.claude/teams/{team-name}/inboxes/"
  - "hasTrustDialogAccepted"
  - "/config"
  - "in-process"
  - "tmux"
  - "iterm2"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Errors returned to Claude as tool results (the turn continues) when it calls tools, MCP servers, subagents or agent-team teammates.

# How to use it

| Error | Cause | Fix |
|---|---|---|
| `Error: No such tool available: <name>` | Tool absent from the session list (names are case-sensitive; tool names over 200 characters are cut). After resume an MCP server may still be connecting; Claude Code now waits (before v2.1.284 it failed at once) | Usually none; `/mcp` or `claude mcp list` to check server status |
| `MCP server "<name>" connection closed before the tool call was answered` | HTTP MCP server or claude.ai connector dropped the connection; the tool may have run. Claude Code retries once on its own only when the server marks the tool safe to repeat | Check the target service before re-running; server authors can mark tools safe to repeat |
| `MCP server "<name>" is disabled` | Tool called on a turned-off server | `/mcp` re-enable; SDK `toggleMcpServer()` with `enabled` true / `toggle_mcp_server()` |
| `MCP server "<name>" tool "<tool>" timed out after <N>s. The server asked the user a question ...` | Non-interactive elicitation unanswered before the call time limit (before v2.1.310 no mention of the question) | `Elicitation` hook that answers; TS SDK `onElicitation` callback; longer per-server `timeout` in ms (e.g. `600000`) |
| `Agent '<name>' would be spawned with zero tools - refusing` (since v2.1.208) | Every entry in the subagent `tools` list failed: unrecognized, not available to subagents (background subagents keep a smaller built-in tool set, and background is the default), or matched nothing in this session (e.g. `Agent` at depth limit, MCP server not connected). Omitting `tools`, or an empty list, never triggers it | Correct entries; use `mcp__<full server name>__*`; remove `background: true` or let Claude wait so `CronCreate` is kept; list `Agent` alongside another tool |
| `subagent_type is required: the general-purpose agent is not available in this session` | `CLAUDE_AGENT_SDK_DISABLE_BUILTIN_AGENTS=1` in non-interactive mode removes all built-ins, or main agent's `tools: Agent(...)` allowlist omits `general-purpose` (before v2.1.235: `Agent type 'general-purpose' not found`) | Retry with a listed subagent; add `general-purpose` or unset the variable |
| `Failed to write to <name>'s inbox - nothing was sent` | Agent team mailbox under `~/.claude/teams/{team-name}/inboxes/` could not be written (disk, permissions, lock held); reported as sent before v2.1.224. Variants: plan approval request not submitted, permission request not delivered to lead, shutdown confirmation not written | Resend; check disk and permissions |
| `Its agent definition was not restored: the folder ... is not trusted` | Resumed stopped teammate whose subagent definition (project or `--add-dir` `.claude/agents/`) came from an untrusted folder; runs with team-essential tools, no custom instructions | Run `claude` in that folder and accept trust, or set `hasTrustDialogAccepted` in `~/.claude.json` |
| `Only a teammate can approve a shutdown request` | Lead sent an approval; nothing shut down | Send the teammate `shutdown_request` |
| `The deny rule "<rule>" cannot be handed to a teammate intact` | Split-pane teammate not started because command-line deny rules would be read differently | Set Teammate mode to `in-process` in `/config`, or move rule to `permissions.deny` in settings |

# Notes

Related cross-session messaging errors: [cross-session errors](./p3-cross-session-messaging-errors.md).
