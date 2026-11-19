---
type: "Reference"
title: "Error reference: message index by section"
description: "Index mapping runtime error messages to sections: server, usage, authentication, network, request, command-line, plugin, tool, background session, wrapper and config errors."
resource: "https://code.claude.com/docs/en/errors"
tags: [errors, index, troubleshooting, messages]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop, cloud]
requires: ""
identifiers:
  - "API Error: 500 Internal server error"
  - "API Error: Repeated 529 Overloaded errors"
  - "Request timed out"
  - "API Error: No response from API"
  - "API Error: Stream idle timeout - no chunks received"
  - "Connection lost before a response was produced"
  - "The model's tool call could not be parsed (retry also failed)."
  - "Auto mode could not evaluate this action and is blocking it for safety"
  - "Agent terminated early due to an API error"
  - "You've hit your session limit"
  - "Usage credits required for 1M context"
  - "Request rejected (429)"
  - "Credit balance is too low"
  - "Not logged in · Please run /login"
  - "Prompt is too long"
  - "Request too large"
  - "--bg and --print conflict"
  - "Error: Invalid --agents configuration:"
  - "Error: --json-schema is not a valid JSON Schema"
  - "Error: bypassPermissions not supported in restricted mode"
  - "Error: Settings file exceeds the 2MiB limit"
  - "Error: No such tool available: <tool name>"
  - "would be spawned with zero tools — refusing"
  - "subagent_type is required: the general-purpose agent is not available in this session"
  - "Sandbox is required but failed to initialize: <reason>"
  - "Message too large for cross-session delivery"
  - "Too many messages to this session just now"
  - "Failed to write to <name>'s inbox — nothing was sent"
  - "Failed to resume the conversation"
  - "No conversation found with session ID: <session-id>"
  - "Transcript saving is off — CLAUDE_CODE_SKIP_PROMPT_HISTORY is set"
  - "Transcript saving is off — inherited CLAUDE_CODE_CHILD_SESSION marker"
  - "Subprocess initialization did not complete within 60000ms"
  - "Claude Code process exited with code N"
  - "Error: Input contained only whitespace"
  - "Input must be provided either through stdin or as a prompt argument when using --print"
  - "Error: stream-json input carried over 256M characters with no newline"
  - "Error: MCP tool <name> (passed via --permission-prompt-tool) not found"
  - "Permission prompt tool returned an invalid result"
  - "Remote managed settings failed to load (<cause>)"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The top of the Error reference is a "Find your error" table that maps each exact message to a section of the page. Part 1 of the page (this staging unit) details Automatic retries, Server errors and Usage limits; other parts detail the sections below. Errors apply to the CLI, the Desktop app and cloud sessions alike, since all wrap the same CLI, except Wrapper and IDE errors, which the launching program prints. Most runtime errors map to an underlying Claude API error code.

# How to use it

Sections and the kinds of messages in each:

| Section | Message families (examples) |
| :- | :- |
| Server errors | 500, repeated 529, `Request timed out`, `No response from API`, mid-response cut-offs, auto mode classifier failures, `Agent terminated early due to an API error` |
| Usage limits | session, weekly, Opus and Sonnet limits; `Usage credits required for 1M context`; `Server is temporarily limiting requests`; `Request rejected (429)`; `Credit balance is too low`; monthly, individual, org, channel and team spend limits |
| Authentication | `Not logged in`, `Invalid API key`, `apiKeyHelper` failures, organization policy denials, OAuth and Remote Control login errors, MCP re-authorization, AWS, Google Cloud, Foundry credential errors, `Scheduled tasks are off for your organization`, `Routines are off for your organization` |
| Network | `Unable to connect to API`, SSL certificate errors, `host_not_allowed` 403 in cloud sessions, cloud session history and sleep-related MCP timeouts |
| Request errors | `Prompt is too long`, `Request too large` (32MB API limit), image and PDF errors, tool schema and tool-name length limits (128 characters for MCP tool names, 200 for `tool_use.name`), model errors, thinking and effort mismatches, `tool_use` or `tool_result` mismatches, usage policy refusals |
| Command-line errors | `--bg` and `--print` conflicts, `--agents`, `--json-schema`, `--append-subagent-system-prompt` flag conflicts, restricted mode, cloud session policy, ultrareview, resume failures, skill command injection, `--print` input errors, MCP add and import errors |
| Plugin errors | marketplace name and source refusals, path escapes, `${user_config.*}` in commands, archive integrity |
| Tool errors | `No such tool available`, MCP server disabled or closed, zero-tool agents, symlink refusals, disk-full, teammate inbox and cross-session message errors, WebFetch limits |
| Background session errors | worktree isolation checks, sessions open in another terminal, `kept <id>` worktree messages, respawn and `/loop` wakeup notices, gateway and `CLAUDE_CODE_PROCESS_WRAPPER` errors |
| Wrapper and IDE errors | `Claude Code process exited with code N`, `Subprocess initialization did not complete within 60000ms` |
| Rewind, Session saving, Configuration warnings | partial restores, `Transcript writes are failing`, managed settings load failures, permission-rule warnings, `CLAUDE_CODE_AUTO_COMPACT_WINDOW` warnings, sandbox warnings |
| Response quality | responses lower quality than usual (no error shown) |

# Limits and defaults

Error text and cross-links are version dependent; the table includes version markers such as `the prompt to confirm went unanswered` from v2.1.324 and `could not confirm that the shell is back in the directory` from v2.1.323.

# Notes

Installation errors (`command not found`, TLS during setup) live on the separate install troubleshooting page.
