---
type: "Reference"
title: "Sideload flags and fail-closed settings refresh"
description: "Managed keys that reject sideloading CLI flags and block startup until server-managed settings are freshly fetched."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [settings, managed, sideload, startup]
kind: "setting"
maturity: "unlabelled"
since: "2.1.193"
surfaces: [cli, sdk, cloud, desktop]
requires: "Managed settings"
identifiers:
  - "disableSideloadFlags"
  - "forceRemoteSettingsRefresh"
  - "--plugin-dir"
  - "--plugin-url"
  - "--agents"
  - "--mcp-config"
  - "CLAUDE_CODE_PLUGIN_DIRS"
  - "addPlugins"
  - "reloadPlugins()"
  - "setMcpServers()"
  - "claude auth"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Two managed-scope Booleans (default `false`).

# How to use it

`disableSideloadFlags` (needs v2.1.193+): `true` makes Claude Code exit with an error naming rejected flags `--plugin-dir`, `--plugin-url`, `--agents`, `--mcp-config`, which users could otherwise use to bypass `strictKnownMarketplaces` for one run. Also rejected:
- `CLAUDE_CODE_PLUGIN_DIRS` naming a plugin folder: exit at startup naming the variable (needs v2.1.280+).
- Agent SDK `addPlugins` passed to `reloadPlugins()`: that call fails; session keeps its existing plugins (needs v2.1.301+).

`forceRemoteSettingsRefresh`: `true` blocks CLI startup until server-managed settings are freshly fetched, and exits if the fetch fails. A `true` from any admin-controlled managed source counts, even a lower-priority one. Unset: startup does not block, though at a sign-in startup it waits up to five seconds; Anthropic can still require the settings; a Cloud gateway session waits and exits if the gateway is unreachable. Applies only to sessions that fetch server-managed settings. `claude auth` subcommands are exempt.

# Limits and defaults

- `--mcp-config` whose servers are all in-process `type: "sdk"` entries is still accepted, so the Agent SDK and VS Code extension keep working. Users can still use `claude mcp add` or `.mcp.json`; add `allowedMcpServers` for per-server control.
- Cloud sessions: the session starts and every server-delivered `--mcp-config` entry is dropped except `type: "sdk"` entries and a Claude Tag session's Slack tools; server-delivered mid-session MCP updates (cloud session configuration, SDK `setMcpServers()`) are also ignored. Before v2.1.268 Slack tools were dropped too; before v2.1.239 a server-delivered `--mcp-config` blocked a cloud session from starting.
- Desktop app: when deployed through MDM, OS policy or a managed file, the app does not pass its own managed plugins (claude.ai-synced, org-deployed) to Code sessions on the machine (they also start without the account's claude.ai skills; marketplace plugins from managed settings still load; before Claude Desktop v1.37937.0 these sessions failed at startup) nor to Cowork sessions on the machine (skills stay available; before v1.44121.0 they failed at startup).
