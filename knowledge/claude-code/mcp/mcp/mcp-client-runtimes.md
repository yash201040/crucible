---
type: "Feature"
title: "MCP client runtimes v1 and v2"
description: "Two MCP client runtimes (SDK 1.x vs SDK 2.0 with protocol revision 2026-07-28), how one is chosen and the variables to pick."
resource: "https://code.claude.com/docs/en/mcp"
tags: [mcp, runtime, protocol, env-var]
kind: "env_var"
maturity: "unlabelled"
since: "2.1.232"
surfaces: [cli, sdk, cloud]
requires: ""
identifiers:
  - "MCP_SDK_GENERATION"
  - "MCP_PROTOCOL_NEGOTIATION"
  - "CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST"
  - "DISABLE_TELEMETRY"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "mcp"
    resource: "https://code.claude.com/docs/en/mcp"
    title: "Connect Claude Code to tools via MCP"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The v1 runtime uses MCP TypeScript SDK 1.x; v2 is the same code on SDK 2.0 adding MCP protocol revision 2026-07-28. Claude Code picks one at start and keeps it until exit.

# How to use it

- Sessions that fetch feature flags use v2 on v2.1.232 or later.
- Sessions that do not fetch flags use v2 by default on v2.1.274 or later: Amazon Bedrock, Claude Platform on AWS, Google Cloud's Agent Platform, Microsoft Foundry (unless a host sets `CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST`), sessions through a Claude apps gateway, and sessions with telemetry or flag fetching off (for example `DISABLE_TELEMETRY`).
- Set `MCP_SDK_GENERATION` to `v1` or `v2` to pick.
- Set `MCP_PROTOCOL_NEGOTIATION` to `auto` or `legacy` to decide whether servers are asked about the newer revision. Unset, a stdio server may be skipped for 7 days (for example after it exits when asked); `auto` asks sooner.

# Limits and defaults

On v2: HTTP, stdio and claude.ai connector servers (including cloud and Remote Control connectors) are asked about the newer revision; `list_changed` arrives over a [held-open stream](./dynamic-tool-updates.md); a [channel](./mcp-channels.md) server on the newer revision is not registered; an OAuth sign-in whose response names an unexpected issuer fails; OAuth credentials go only to an HTTPS token endpoint or `localhost`/`127.0.0.1`/`::1`. Anthropic can keep a specific server on the earlier protocol with a fetched flag.
