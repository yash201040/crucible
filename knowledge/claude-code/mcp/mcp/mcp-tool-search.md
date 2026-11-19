---
type: "Feature"
title: "MCP tool search and deferral"
description: "MCP tool definitions are deferred and found on demand; ENABLE_TOOL_SEARCH modes, alwaysLoad, description length limits, gateways."
resource: "https://code.claude.com/docs/en/mcp"
tags: [mcp, tool-search, context, deferral]
kind: "env_var"
maturity: "unlabelled"
since: "2.1.285"
surfaces: [cli, headless, sdk]
requires: "Claude Opus 4, Sonnet 4, Haiku 4.5 or later (Opus 4.5, Sonnet 4.5, Haiku 4.5 or later on Google Cloud's Agent Platform)"
identifiers:
  - "ENABLE_TOOL_SEARCH"
  - "alwaysLoad"
  - "CLAUDE_CODE_MAX_MCP_DESCRIPTION_LENGTH"
  - "CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS"
  - "ToolSearch"
  - "permissions.deny"
  - "--tools"
  - "defer_loading"
  - "tool_reference"
  - "/context"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "mcp"
    resource: "https://code.claude.com/docs/en/mcp"
    title: "Connect Claude Code to tools via MCP"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Tool search keeps context low by deferring MCP tool definitions until Claude needs them: only tool names and server instructions load at session start. There is no fixed per-server tool cap; the limit is your context budget. On by default.

# How to use it

`ENABLE_TOOL_SEARCH` values:

| Value | Behavior |
|---|---|
| unset | all MCP tools deferred and loaded on demand; upfront on models earlier than Opus 4 / Sonnet 4, earlier Agent Platform models, and Foundry deployments hosted on Azure |
| `true` | deferred, same fallbacks |
| `auto` | threshold mode: tools load upfront while their definitions total under 10% of the context window; at 10% or more tool search turns on (and tools can stay deferred even if the total later drops below) |
| `auto:N` | custom percentage N (0-100), for example `auto:5` |
| `false` | all upfront, no deferral |

Also: deny the tool with `{"permissions": {"deny": ["ToolSearch"]}}`, or omit it from `--tools`, to load upfront (a request can still carry a placeholder `defer_loading` entry). Set the value in `settings.json` `env`.

- Exempt a server: `"alwaysLoad": true` in its config (any server type); its tools load regardless of `ENABLE_TOOL_SEARCH`. Startup waits for its tools up to the 5-second connect timeout (a valid `cached` entry avoids the wait); other servers connect in the background unless `MCP_CONNECTION_NONBLOCKING=0`.
- Defer a server: `"alwaysLoad": false` keeps all its tools deferred, even tools the author marked upfront (v2.1.287 or later).
- Per tool (author): `_meta["anthropic/alwaysLoad"]` true loads upfront without making startup wait; false keeps the tool deferred when the user's config sets `alwaysLoad: true`, for servers passed with `--mcp-config`, from an Agent SDK app, or from a plugin (v2.1.285 or later); other servers load it upfront.

# Limits and defaults

- Description limits: server instructions and descriptions of tools loaded upfront are cut at 4,096 characters; descriptions of tools loaded through tool search at 16,384. Before v2.1.296 the shorter limit was 2,048; before v2.1.295 it applied to every description. `CLAUDE_CODE_MAX_MCP_DESCRIPTION_LENGTH` (v2.1.280 or later) sets both; some Anthropic-hosted servers at `api.anthropic.com` are never cut. Tool search matches only the text within the shorter limit, so put key words first. Server instructions help Claude decide when to search for the server's tools.
- `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS` keeps tool search off; `ENABLE_TOOL_SEARCH` cannot override it (v2.1.227 or later: managed settings can keep it on). In a HIPAA-configured session tool search is off and nothing turns it on.
- Not supported on Microsoft Foundry deployments hosted on Azure (rejected server-side; detected and loaded upfront; `ENABLE_TOOL_SEARCH` cannot override).
- Gateway (`ANTHROPIC_BASE_URL`): the gateway must forward `defer_loading` fields and `tool_reference` blocks with the `anthropic-beta` header. Tool search is on by default behind a gateway; before v2.1.304 it was off unless `ENABLE_TOOL_SEARCH` was `true`, `auto` or `auto:N`. From v2.1.305 Claude Code can retry without tool search after a `400` or `422` (silently loading upfront, retrying tool search later).
- `/context` may label tools `(deferred)` or `(loaded on-demand)` below the `auto` threshold when tool search was already on in the conversation; no action needed.
