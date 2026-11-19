---
type: "Reference"
title: "Plugin policy keys and marketplace allowlist/blocklist"
description: "Control matrix of managed plugin policy keys plus the strictKnownMarketplaces allowlist and blockedMarketplaces blocklist source objects and matching rules."
resource: "https://code.claude.com/docs/en/plugins/org"
tags: [plugins, managed-settings, allowlist, blocklist, security, policy]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk, cloud]
requires: "Managed settings; some keys need v2.1.223, v2.1.232 or v2.1.273"
identifiers:
  - "strictKnownMarketplaces"
  - "allowedMarketplaces"
  - "blockedMarketplaces"
  - "syncClaudeAiPlugins"
  - "disableSideloadFlags"
  - "disableCommandPluginSources"
  - "allowManagedHooksOnly"
  - "strictPluginOnlyCustomization"
  - "pluginSuggestionMarketplaces"
  - "pluginTrustMessage"
  - "allowedChannelPlugins"
  - "channelsEnabled"
  - "CLAUDE_CODE_DISABLE_OFFICIAL_MARKETPLACE_AUTOINSTALL"
  - "allowManagedModsOnly"
  - "pluginConfigs"
  - "skills-dir"
  - "hostPattern"
  - "pathPattern"
  - "--plugin-dir"
  - "--plugin-url"
  - "--agents"
  - "--mcp-config"
  - "CLAUDE_CODE_PLUGIN_DIRS"
  - "addPlugins"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-org"
    resource: "https://code.claude.com/docs/en/plugins/org"
    title: "Manage Claude Code plugins for your organization"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Managed plugin policy keys decide which marketplace sources plugins may come from and which loading routes stay open. The lists match the marketplace's source (repo, URL or path), not the plugin entry inside it. They apply before any download (add, install, update, refresh, auto-update) and again at session start, so an installed plugin whose marketplace no longer matches does not load (`/plugin` shows `Marketplace "<name>" is not in the allowed marketplace list` or `... is blocked by enterprise policy`). While any allowlist is set, or a blocklist names a source other than `skills-dir`, a plugin whose marketplace cannot be found shows the policy error rather than not-found.

# How to use it

| Key | What it enforces | Cannot do |
|---|---|---|
| `strictKnownMarketplaces` (alias `allowedMarketplaces`) | allowlist of sources; `[]` blocks all including official | register a marketplace, restrict entries inside one, block `--plugin-dir` |
| `blockedMarketplaces` | blocklist, checked first | block an already registered marketplace from a non-matching source |
| `syncClaudeAiPlugins` | `false` stops downloading plugins synced from claude.ai (v2.1.273+) | turn off one synced plugin; use `"<name>@synced": false` in `enabledPlugins` |
| `enabledPlugins` | `true` force-enables, `false` blocks everywhere | install a plugin whose marketplace is not registered/allowed |
| `disableSideloadFlags` | rejects `--plugin-dir`, `--plugin-url`, `--agents`, SDK `plugins` option, `CLAUDE_CODE_PLUGIN_DIRS` folders, `--mcp-config` (unless all servers are in-process `type: "sdk"`), and SDK `addPlugins` mid-session | restrict `.mcp.json`, `claude mcp add`, SDK servers (pair with `allowedMcpServers`) |
| `disableCommandPluginSources` | blocks `command`-source plugins; defaults to the value of `allowManagedHooksOnly` when unset | other source types |
| `allowManagedHooksOnly` | restricts which hooks run | trust hooks of user-enabled plugins |
| `strictPluginOnlyCustomization` | `true` or array of `skills`,`agents`,`hooks`,`mcp` blocks those from user/project sources; also stops skills-directory plugins | restrict installs or CLI sideload flags |
| `pluginSuggestionMarketplaces` | marketplaces allowed to give install suggestions | built-in tips |
| `pluginTrustMessage` | appends text to the `/plugin` trust warning | change warning text |
| `allowedChannelPlugins` | replaces default list of plugins allowed to push channel messages; needs `channelsEnabled: true` | n/a |
| `CLAUDE_CODE_DISABLE_OFFICIAL_MARKETPLACE_AUTOINSTALL=1` | stops interactive sessions auto-registering the official marketplace (env var, deliver via managed `env`) | remove an existing registration |
| `allowManagedModsOnly` | option on a built-in plugin under `pluginConfigs`; stops non-org mods running hooks | stop a plugin containing a mod from installing |

All are managed-only except `enabledPlugins` (any scope, managed locks it), `syncClaudeAiPlugins` (users may also set it), the env var, and `allowManagedModsOnly`.

Allowlist source objects: `github` (`repo`, optional `ref`, `path`; `your-org/*` owner wildcard needs v2.1.223+, `*` must be the whole repo name), `git` (`url`), `url` (optional `headers`, not compared), `file`/`directory` (absolute `path`), `hostPattern` (regex on host of github/git/url sources; anchor with `^`/`$`), `pathPattern` (regex on file/directory path), `{ "source": "skills-dir" }` (matches no marketplace; keeps skills-directory plugins loading, which stop if any allowlist lacks it). Entries must match `repo`/`url`, `ref` and `path` exactly or be absent on both sides. A marketplace hosted on claude.ai is matched by a `hostPattern` for `claude.ai` (v2.1.273+).

Blocklist matching is wider: git URLs canonicalized, `github` and equivalent `git` entries cross-match, owner compare case-insensitive, no `ref`/`path` blocks all. Blocklist `url` entries also apply to cloned `https://` repo URLs (v2.1.232+). A blocklist with only `skills-dir` is not an active restriction.

Example combined policy: allow `anthropics/claude-plugins-official`, `your-org/*` and `skills-dir`, register both marketplaces explicitly in `extraKnownMarketplaces`, force-enable plugins, set `"disableSideloadFlags": true`.

# Limits and defaults

The allowlist does not register anything and the official marketplace self-registers only in interactive terminal sessions (never `-p` or cloud-attached terminals) and only if allowed. A blocked attempt is remembered; re-register via `extraKnownMarketplaces`, an `enabledPlugins` entry, or `/plugin marketplace add`. `[]` does not cover synced plugins. Aliases need v2.1.232+.

# Notes

Not enforceable by a key: per-user/per-group targeting (deliver separate settings per group), restricting entries inside an allowed marketplace (set plugin `false`), hiding `/plugin`, gating `--plugin-dir` via allowlist (use `disableSideloadFlags`), enforcing the claude.ai Plugins & skills toggles (those reach the CLI as synced plugins). Blocked adds fail with `is blocked by enterprise policy`; `claude --plugin-dir ./x` exits naming `disableSideloadFlags`.
