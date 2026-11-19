---
type: "Reference"
title: "MCP restriction patterns and managed-mcp.json"
description: "Patterns for controlling MCP in an organization and exclusive control via the managed-mcp.json file."
resource: "https://code.claude.com/docs/en/managed-mcp"
tags: [mcp, managed-mcp, admin, exclusive-control]
kind: "file"
maturity: "unlabelled"
since: "2.1.282"
surfaces: [cli, ide, cloud]
requires: ""
identifiers:
  - "managed-mcp.json"
  - "/Library/Application Support/ClaudeCode/managed-mcp.json"
  - "/etc/claude-code/managed-mcp.json"
  - "allowAllClaudeAiMcps"
  - "allowClaudeInChromeWithManagedMcp"
  - "--mcp-config"
  - "--strict-mcp-config"
  - "claude mcp list"
  - "claude mcp add"
  - "claude --chrome"
  - "strictPluginOnlyCustomization"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "managed-mcp"
    resource: "https://code.claude.com/docs/en/managed-mcp"
    title: "Control MCP server access for your organization"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

By default any user can connect any MCP server. Patterns: Disable MCP (`managed-mcp.json` with an empty `mcpServers` map); Fixed deployment (`managed-mcp.json`); Provided servers (`managedMcpServers`); Approved catalog (`allowedMcpServers` + `allowManagedMcpServersOnly: true`); Plugin servers only (`strictPluginOnlyCustomization` with `mcp`); Soft allowlist; Denylist only; No restrictions. There is no built-in server registry.

# How to use it

`managed-mcp.json` (same format as project `.mcp.json`) paths: macOS `/Library/Application Support/ClaudeCode/`, Linux/WSL `/etc/claude-code/`, Windows `C:\Program Files\ClaudeCode\`. It cannot be delivered through server-managed settings. Don't put credentials in `env` (any user can read it); use `${VAR}` expansion, OAuth/per-user headers or `headersHelper`.

With the file deployed, only these load: its servers, `managedMcpServers`, in-process servers an app registers (VS Code, desktop connectors), the server a mod adds, and Claude in Chrome if allowed. Plugin servers, `--mcp-config` servers and claude.ai connectors are suppressed.

- `"allowAllClaudeAiMcps": true` loads claude.ai connectors alongside; read only from admin tiers (server-managed, plist/HKLM, system file). A file on a cloud-session host still suppresses its connectors.
- `"allowClaudeInChromeWithManagedMcp": true` (v2.1.282+) lets Claude in Chrome run; read only from device sources (plist, HKLM, system file), not server-managed.

# Limits and defaults

- `--mcp-config` with the file on a workstation: exits with `You cannot dynamically configure MCP servers when an enterprise MCP config is present`. In cloud sessions the managed servers only load and skipped servers are named in a stderr warning (debug level on self-hosted runners). `--strict-mcp-config` makes Claude Code exit in both.
- `claude mcp add` fails with `Cannot add MCP server: enterprise MCP configuration is active and has exclusive control over MCP servers`; `claude mcp list` should show only managed servers (otherwise check the path).
- `deniedMcpServers` applies to managed servers; managed servers need no allowlist entry unless they use `${VAR}` outside `env` (before v2.1.305 also `env`; before v2.1.259 every managed server when an allowlist was set).
