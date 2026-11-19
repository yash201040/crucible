---
type: "Reference"
title: "MCP allowlist, denylist and managed server keys"
description: "Settings that restrict which MCP servers load, provide managed servers and control claude.ai connectors alongside managed-mcp.json."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [settings, mcp, allowlist, managed]
kind: "setting"
maturity: "unlabelled"
since: "2.1.259"
surfaces: [cli, sdk, cloud]
requires: ""
identifiers:
  - "allowedMcpServers"
  - "deniedMcpServers"
  - "allowManagedMcpServersOnly"
  - "managedMcpServers"
  - "allowAllClaudeAiMcps"
  - "allowClaudeInChromeWithManagedMcp"
  - "disableClaudeAiConnectors"
  - "ENABLE_CLAUDEAI_MCP_SERVERS"
  - "serverName"
  - "serverCommand"
  - "serverUrl"
  - "managed-mcp.json"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Keys that decide which MCP servers can load.

# How to use it

| Name | Scope | Type / default | What it does |
| :- | :- | :- | :- |
| `allowedMcpServers` | any file; entries merge unless `allowManagedMcpServersOnly` | array of objects with exactly one key: `serverName` (letters, numbers, hyphens, underscores), `serverCommand` (array matched exactly), `serverUrl` (pattern with `*`). Unset allows all; empty array blocks every user-added server | Blocks non-matching servers wherever defined (plugins, `--mcp-config`, claude.ai). Once any `serverCommand` entry exists, stdio servers must match one; once any `serverUrl` exists, remote servers must match one |
| `deniedMcpServers` | any file; always merges | same shape; `serverName` may be a connector display name such as `"claude.ai Slack"`; unset or empty blocks nothing | Blocks servers everywhere, including `managed-mcp.json`, `managedMcpServers` and claude.ai connectors; beats the allowlist |
| `allowManagedMcpServersOnly` | managed | Boolean, default `false` | Read `allowedMcpServers` from managed settings only; the denylist still merges from all scopes |
| `managedMcpServers` | managed (dropped with warning in user/project/local; not read in Desktop Code tab on third-party deployment or Cowork) | object by server name, `.mcp.json` shape for `http` or `sse`, required `https://` `url`, optional `headers`, `oauth`; invalid entries dropped. Needs v2.1.259+ | Remote MCP servers provided to every user; users cannot edit or remove them |
| `allowAllClaudeAiMcps` | managed | Boolean, default `false` | Load claude.ai connectors alongside a deployed `managed-mcp.json`, which otherwise has exclusive control and suppresses them. Allow/deny lists still apply. Connectors in cloud sessions on a host with `managed-mcp.json` stay suppressed |
| `allowClaudeInChromeWithManagedMcp` | managed, device-local only (MDM plist, HKLM, system `managed-settings.json`); ignored in server-managed, HKCU, user, project | Boolean, default `false`. Needs v2.1.282+ | Let Claude in Chrome run alongside `managed-mcp.json`; a `deniedMcpServers` entry for `claude-in-chrome` still blocks it |
| `disableClaudeAiConnectors` | any file | Boolean, default `false` | `true` anywhere applies (project `false` cannot override user or managed `true`); stops fetching and connecting claude.ai connectors. `ENABLE_CLAUDEAI_MCP_SERVERS=false` does it per session; neither can undo the other. `--mcp-config` servers unaffected |

# Limits and defaults

Exemptions from the allowlist (denylist still applies): built-in servers (Claude in Chrome, the `ide` server for VS Code and JetBrains, CLI-configured servers), a Claude Tag session's Slack tools (v2.1.268+), every `managedMcpServers` entry, and `managed-mcp.json` entries with no `${VAR}` expansion outside `env` (before v2.1.259 these had to match). In-process `type: "sdk"` servers are exempt from both lists.
