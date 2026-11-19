---
type: "Guide"
title: "MCP servers in self-hosted sessions"
description: "How MCP servers reach runner sessions, startup waits, and denying the built-in Claude Code Remote server."
resource: "https://code.claude.com/docs/en/self-hosted-environments-configuration"
tags: [self-hosted, mcp, startup, permissions, connectors]
kind: "mixed"
maturity: "beta"
since: "2.1.299"
surfaces: [cloud]
requires: "Self-hosted environments (Team or Enterprise)"
identifiers:
  - "claude mcp add --scope user"
  - "claude mcp add-json"
  - "SELF_HOSTED_RUNNER_HOST_CONFIG_DIR"
  - "/etc/claude-code/managed-mcp.json"
  - "managedMcpServers"
  - ".mcp.json"
  - "--mcp-config"
  - "--trust-workspace"
  - "ENABLE_TOOL_SEARCH"
  - "alwaysLoad"
  - "MCP_CONNECTION_NONBLOCKING"
  - "MCP_CONNECT_TIMEOUT_MS"
  - "CLAUDE_CODE_MCP_STARTUP_WAIT_MS"
  - "mcp__Claude_Code_Remote"
  - "mcp__claude-code-remote"
  - "deniedMcpServers"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "self-hosted-environments-configuration"
    resource: "https://code.claude.com/docs/en/self-hosted-environments-configuration"
    title: "Customize sessions in self-hosted environments"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Ways MCP servers get into every session a runner starts, plus control of the control plane's own MCP server.

# How to use it

- Image build: `claude mcp add --scope user sidecar -- /usr/local/bin/mcp-sidecar`; `--scope user` is required (local scope is not seeded). Runner snapshots `mcpServers` from the host's `.claude.json` once at startup; restart to pick up changes. Unknown `type` entries are dropped with a startup warning. `SELF_HOSTED_RUNNER_HOST_CONFIG_DIR` changes the source; an empty dir disables seeding.
- Other sources: managed MCP file (`/etc/claude-code/managed-mcp.json` on Linux, `/Library/Application Support/ClaudeCode/managed-mcp.json` on macOS; when present, control-plane-delivered servers including claude.ai connectors are skipped; before v2.1.229 such sessions exited at startup); `managedMcpServers` in managed settings (v2.1.259+); `<repo>/.mcp.json` (auto-approved in cloud sessions, at most one repo's file loads in multi-repo sessions, skipped with `--trust-workspace false` unless approved elsewhere, v2.1.319+); `--mcp-config` appended after `"$@"` in a wrapper (before v2.1.299 its servers shut down at the first delivered-server update).
- Connector delivery: control plane delivers claude.ai connectors to interactively created sessions through `api.anthropic.com`; programmatic sessions such as CLI dispatches do not get them. A same-named host or repo server is not connected when a connector exists.
- `settings.json` has no top-level `mcpServers`. Set `ENABLE_TOOL_SEARCH` in the runner environment for MCP tool search.
- Startup waits: session startup waits up to 5 seconds for HTTP/SSE servers with `alwaysLoad: true` (all servers with `MCP_CONNECTION_NONBLOCKING=0`); change with `MCP_CONNECT_TIMEOUT_MS`. First turn waits up to 2 seconds for connecting stdio servers; change with `CLAUDE_CODE_MCP_STARTUP_WAIT_MS` (v2.1.274+). `claude mcp add` lacks `alwaysLoad`; use `claude mcp add-json`.
- Turn off the built-in Claude Code Remote server (creates scheduled tasks, steers other cloud sessions, adds repositories, follows PR activity) with deny rules `mcp__Claude_Code_Remote`, `mcp__claude-code-remote`, `mcp__bf7c680d-5fdc-5ef4-b4a0-abadb619bf0a` (one per registration name, exact case); per tool append `__<tool>`; to block connection use `deniedMcpServers`. Place in server-managed settings or the runner's `~/.claude/settings.json` (the latter on Bedrock/Agent Platform runners).

# Limits and defaults

Startup wait 5 seconds and first-turn wait 2 seconds by default; missing tools appear later without action.
