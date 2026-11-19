---
type: "Reference"
title: "Keys only a managed source can set"
description: "Managed-only settings for permission, plugin, MCP, sandbox and delivery controls, with version requirements."
resource: "https://code.claude.com/docs/en/managed-settings#keys-only-a-managed-source-can-set"
tags: [managed-settings, locks, plugins, sandbox]
kind: "setting"
maturity: "unlabelled"
since: "2.1.193"
surfaces: [cli]
requires: ""
identifiers:
  - "allowAllClaudeAiMcps"
  - "allowedChannelPlugins"
  - "channelsEnabled"
  - "allowManagedHooksOnly"
  - "allowManagedMcpServersOnly"
  - "allowManagedPermissionRulesOnly"
  - "blockedMarketplaces"
  - "disableCommandPluginSources"
  - "disableSideloadFlags"
  - "--plugin-dir"
  - "--plugin-url"
  - "--agents"
  - "--mcp-config"
  - "forceRemoteSettingsRefresh"
  - "managedMcpServers"
  - "managedSourcesBehavior"
  - "parentSettingsBehavior"
  - "pluginSuggestionMarketplaces"
  - "pluginTrustMessage"
  - "policyHelper"
  - "sandbox.filesystem.allowManagedReadPathsOnly"
  - "sandbox.network.allowManagedDomainsOnly"
  - "strictKnownMarketplaces"
  - "strictPluginOnlyCustomization"
  - "wslInheritsWindowsSettings"
  - "disableRemoteControl"
  - "claude doctor"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "managed-settings"
    resource: "https://code.claude.com/docs/en/managed-settings"
    title: "Deploy managed settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Keys read only from a managed source; in user or project files they have no effect. Most are locks telling Claude Code to honor only the managed value of an ordinary key.

# How to use it

| Setting | What it does |
| :- | :- |
| `allowAllClaudeAiMcps` | load claude.ai connectors alongside `managed-mcp.json` |
| `allowedChannelPlugins` | allowlist of channel plugins that may push messages; replaces default Anthropic list; needs `channelsEnabled: true` |
| `channelsEnabled` | allow channels for the organization |
| `allowManagedHooksOnly` | restrict which hooks run |
| `allowManagedMcpServersOnly` | only managed `allowedMcpServers` honored; denylist still merges |
| `allowManagedPermissionRulesOnly` | managed is the only permission-rule source |
| `blockedMarketplaces` | marketplace blocklist, checked before download |
| `disableCommandPluginSources` | block `command` plugin sources and marketplace `headersHelper` commands (v2.1.229+; headersHelper part v2.1.238+); follows `allowManagedHooksOnly` when unset |
| `disableSideloadFlags` | reject `--plugin-dir`, `--plugin-url`, `--agents`, `--mcp-config` at startup (v2.1.193+); in cloud sessions drops server-delivered `--mcp-config` servers instead |
| `forceRemoteSettingsRefresh` | block startup until remote settings fetched; exit on failure |
| `managedMcpServers` | provide remote MCP servers (v2.1.259+) |
| `managedSourcesBehavior`, `parentSettingsBehavior`, `policyHelper` | delivery controls |
| `pluginSuggestionMarketplaces`, `pluginTrustMessage` | plugin suggestion allowlist; custom trust-warning text |
| `sandbox.filesystem.allowManagedReadPathsOnly`, `sandbox.network.allowManagedDomainsOnly` | sandbox locks |
| `strictKnownMarketplaces` | which marketplace sources users may add |
| `strictPluginOnlyCustomization` | `true` locks skills, agents, hooks, MCP from user/project sources; an array names which |
| `wslInheritsWindowsSettings` | WSL reads the Windows policy chain |

# Limits and defaults

- Owners enable/disable Remote Control and cloud sessions organization-wide in claude.ai admin settings; disabling Remote Control disconnects connected sessions on v2.1.286+ at next hourly policy refresh. Per device: `disableRemoteControl`. Cloud sessions have no per-device managed key.
- `claude doctor` `Organization policy` line shows where org policy loaded from (v2.1.261+); `/status` shows it when policy did not load.
