---
type: "Reference"
title: "Index: MCP, plugin and skill keys"
description: "Settings keys for MCP server allow and deny lists, managed MCP, claude.ai connectors, plugins, marketplaces, mods and skills (index rows only)."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [mcp, plugins, skills, managed-settings]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "allowAllClaudeAiMcps"
  - "allowClaudeInChromeWithManagedMcp"
  - "allowedMcpServers"
  - "allowManagedMcpServersOnly"
  - "deniedMcpServers"
  - "disableClaudeAiConnectors"
  - "disabledMcpjsonServers"
  - "enableAllProjectMcpServers"
  - "enabledMcpjsonServers"
  - "managedMcpServers"
  - "allowedChannelPlugins"
  - "appendPlugins"
  - "prependPlugins"
  - "blockedMarketplaces"
  - "channelsEnabled"
  - "disableBundledSkills"
  - "disableCommandPluginSources"
  - "disableSkillShellExecution"
  - "enabledPlugins"
  - "extraKnownMarketplaces"
  - "pluginConfigs"
  - "pluginSuggestionMarketplaces"
  - "pluginTrustMessage"
  - "skillOverrides"
  - "strictKnownMarketplaces"
  - "strictPluginOnlyCustomization"
  - "strictPluginOnlyCustomization.agents"
  - "strictPluginOnlyCustomization.hooks"
  - "strictPluginOnlyCustomization.mcp"
  - "strictPluginOnlyCustomization.skills"
  - "syncClaudeAiPlugins"
  - "syncClaudeAiSkills"
  - "disableSideloadFlags"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Index entries from the "MCP" and "Plugins and skills" topics (plus `disableSideloadFlags`, indexed under Enterprise and managed settings). Detailed sections are in other parts of the page.

# How to use it

| Key | Scope | What it does |
| :- | :- | :- |
| `allowedMcpServers` | Any file | Allowlist which MCP servers users can add |
| `deniedMcpServers` | Any file | Block MCP servers by URL, command or name |
| `allowManagedMcpServersOnly` | Managed | Make the managed MCP allowlist the only one |
| `managedMcpServers` | Managed | Provide remote MCP servers to every user alongside their own |
| `allowAllClaudeAiMcps` | Managed | Load claude.ai connectors alongside a deployed `managed-mcp.json` |
| `allowClaudeInChromeWithManagedMcp` | Managed | Let the built-in Claude in Chrome server run alongside `managed-mcp.json` |
| `disableClaudeAiConnectors` | Any file | Stop fetching claude.ai connectors |
| `enableAllProjectMcpServers` | Any file | Approve every server in project `.mcp.json` without a prompt |
| `enabledMcpjsonServers` | Any file | Approve specific servers from a project's `.mcp.json` |
| `disabledMcpjsonServers` | Any file | Reject specific servers from a project's `.mcp.json` |
| `enabledPlugins` | Any file | Turn individual plugins on or off per scope |
| `extraKnownMarketplaces` | Any file | Register marketplaces for a repository or organization |
| `strictKnownMarketplaces` | Managed | Allowlist marketplace sources users can add and install from |
| `blockedMarketplaces` | Managed | Block plugin marketplace sources |
| `pluginSuggestionMarketplaces` | Managed | Marketplaces allowed to surface install suggestions in `/plugin` |
| `pluginTrustMessage` | Managed | Add text to the plugin trust warning |
| `pluginConfigs` | User or managed | Stored answers to a plugin's configuration dialog |
| `disableCommandPluginSources` | Managed | Block plugins that install by running a marketplace-declared command |
| `allowedChannelPlugins` | Managed | Replace the default allowlist of channel plugins that can push messages |
| `channelsEnabled` | Managed | Allow channels for the organization |
| `prependPlugins` | User or managed | Run the organization's mods before every user-installed mod |
| `appendPlugins` | User or managed | Run the organization's mods after every user-installed mod |
| `strictPluginOnlyCustomization` | Managed | Block skills, agents, hooks and MCP servers from user and project sources; sub-keys `.agents`, `.hooks`, `.mcp`, `.skills` do each one |
| `syncClaudeAiPlugins` | User, local or managed | Stop loading and downloading plugins enabled on the claude.ai account |
| `syncClaudeAiSkills` | User, local or managed | Stop loading and downloading skills enabled on the claude.ai account |
| `disableBundledSkills` | Any file | Turn off the skills and workflows included with Claude Code |
| `disableSkillShellExecution` | Any file | Stop skills and custom commands from running inline shell |
| `skillOverrides` | Any file | Hide or collapse a skill without editing its SKILL.md |
| `disableSideloadFlags` | Managed | Reject CLI flags that sideload plugins, subagents and MCP servers |
