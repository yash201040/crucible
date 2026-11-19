---
type: "Reference"
title: "Admin enforcement controls and keys"
description: "Table of managed-settings keys for permissions, sandbox, MCP, plugins, hooks, login, providers, models, versions and telemetry."
resource: "https://code.claude.com/docs/en/admin-setup#decide-what-to-enforce"
tags: [managed-settings, enforcement, permissions, sandbox, hooks]
kind: "setting"
maturity: "unlabelled"
since: "2.1.285"
surfaces: [cli, ide, sdk]
requires: ""
identifiers:
  - "permissions.allow"
  - "permissions.deny"
  - "allowManagedPermissionRulesOnly"
  - "permissions.disableBypassPermissionsMode"
  - "--dangerously-skip-permissions"
  - "permissions.defaultMode"
  - "permissions.disableAutoMode"
  - "sandbox.enabled"
  - "sandbox.network.allowedDomains"
  - "allowedMcpServers"
  - "deniedMcpServers"
  - "allowManagedMcpServersOnly"
  - "managedMcpServers"
  - "managed-mcp.json"
  - "strictKnownMarketplaces"
  - "blockedMarketplaces"
  - "disableSideloadFlags"
  - "disableCommandPluginSources"
  - "pluginSuggestionMarketplaces"
  - "strictPluginOnlyCustomization"
  - "syncClaudeAiSkills"
  - "syncClaudeAiPlugins"
  - "allowManagedHooksOnly"
  - "allowedHttpHookUrls"
  - "forceLoginMethod"
  - "forceLoginOrgUUID"
  - "allowedProviders"
  - "disableAgentView"
  - "processWrapper"
  - "availableModels"
  - "enforceAvailableModels"
  - "maxEffortLevel"
  - "minimumVersion"
  - "requiredMinimumVersion"
  - "requiredMaximumVersion"
  - "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC"
  - "claude agents"
  - "--bg"
  - "/background"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "admin-setup"
    resource: "https://code.claude.com/docs/en/admin-setup"
    title: "Set up Claude Code for your organization"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Control surfaces an administrator can lock down through managed settings, with the keys that drive each.

# How to use it

| Control | Keys | Notes |
| :- | :- | :- |
| Permission rules | `permissions.allow`, `permissions.deny` | allow/ask/deny of tools and commands |
| Permission lockdown | `allowManagedPermissionRulesOnly`, `permissions.disableBypassPermissionsMode` | managed becomes the only rule source; disables `--dangerously-skip-permissions` |
| Starting permission mode | `permissions.defaultMode`, `permissions.disableAutoMode` | set terminal start mode or remove auto mode |
| Sandboxing | `sandbox.enabled`, `sandbox.network.allowedDomains` | OS-level filesystem/network isolation |
| MCP control | `allowedMcpServers`, `deniedMcpServers`, `allowManagedMcpServersOnly`, `managedMcpServers`, `managed-mcp.json` | see [managed MCP](../managed-mcp/mcp-patterns-and-files.md) |
| Plugin marketplaces | `strictKnownMarketplaces`, `blockedMarketplaces`, `disableSideloadFlags`, `disableCommandPluginSources`, `pluginSuggestionMarketplaces` | sideload flags reject CLI flags that load plugins, agents, MCP for one run |
| Customization lockdown | `strictPluginOnlyCustomization` | blocks skills, agents, hooks, MCP from user and project sources |
| claude.ai sync | `syncClaudeAiSkills`, `syncClaudeAiPlugins` | set `false` to stop syncing; on v2.1.273+ turning Skills off in claude.ai also removes already-synced ones |
| Hook restrictions | `allowManagedHooksOnly`, `allowedHttpHookUrls` | restrict which hooks run and HTTP hook URLs |
| Login enforcement | `forceLoginMethod`, `forceLoginOrgUUID` | sessions using `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN` or `apiKeyHelper` are blocked at startup when set; before v2.1.212 only terminal logins applied them |
| Provider restrictions | `allowedProviders` | v2.1.285+; unlisted provider refused at startup, login and next API contact |
| Agent view | `disableAgentView` | turns off `claude agents`, `--bg`, `/background` and the on-demand supervisor |
| Corporate launcher | `processWrapper` | prefixes the background-agent supervisor and workers with a required launcher |
| Model restrictions | `availableModels`, `enforceAvailableModels` | the second also constrains the auto-selected default |
| Effort cap | `maxEffortLevel` | cap per model or all, any provider |
| Version floor / range | `minimumVersion`, `requiredMinimumVersion`, `requiredMaximumVersion` | the required pair refuses to start outside the range |
| Telemetry opt-out | `env` with `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1` | |

# Limits and defaults

- Permission rules and sandboxing cover different layers: denying WebFetch does not stop `curl` through an allowed Bash; the sandbox network allowlist does.
- On Enterprise with claude.ai/API sign-in, org-level model restrictions, default model and effort limits are set in admin settings (server-side). None reach Bedrock, Vertex, Foundry or Claude Platform on AWS; use `availableModels`, `model` and `maxEffortLevel` there.
- Cloud sessions have admin surfaces on claude.ai: organization-shared environments (network access level, env vars, setup script) and a default environment at claude.ai/admin-settings/claude-code.
