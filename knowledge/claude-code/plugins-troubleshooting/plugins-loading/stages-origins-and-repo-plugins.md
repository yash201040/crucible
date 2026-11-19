---
type: "Concept"
title: "Plugin load stages, origins and repository plugins"
description: "The declared, fetched and loaded stages, plugin id origin suffixes, and trust and component limits for repository plugins."
resource: "https://code.claude.com/docs/en/plugins/loading"
tags: [plugins, loading, origins, trust, skills-dir]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.246"
surfaces: [cli, headless, sdk, desktop, cloud]
requires: ""
identifiers:
  - "enabledPlugins"
  - "extraKnownMarketplaces"
  - "known_marketplaces.json"
  - "installed_plugins.json"
  - "@inline"
  - "@skills-dir"
  - "@synced"
  - "--plugin-dir"
  - "--plugin-url"
  - "CLAUDE_CODE_PLUGIN_DIRS"
  - "defaultEnabled"
  - "/reload-plugins"
  - "strictPluginOnlyCustomization"
  - "strictKnownMarketplaces"
  - "blockedMarketplaces"
  - "/cd"
  - ".claude/skills/"
  - "claude plugin list --json"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-loading"
    resource: "https://code.claude.com/docs/en/plugins/loading"
    title: "Plugin loading reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

An `enabledPlugins` entry becomes usable in three stages: declared in settings (`enabledPlugins`, `extraKnownMarketplaces`; `claude plugin marketplace add` writes to user `extraKnownMarketplaces`), fetched to disk under `~/.claude/plugins/` (`known_marketplaces.json` per user, `installed_plugins.json` with `scope`/`installPath`/`version`, `cache/`), and loaded in the running session. After changes outside the `/plugin` panel run `/reload-plugins` or start a new session.

Plugins load at start from `installed_plugins.json` and the cache without the network; then declared marketplaces are checked in the background: an unknown marketplace is cloned and enabled plugins downloaded; a changed source is re-fetched with `Plugins changed. Run /reload-plugins to activate.`. A plugin with no usable cache shows `Plugin "<name>" not cached at <path>`.

# How to use it

Plugin id is `<name>@<origin>`:

| Suffix | Origin | Turn on/off |
|---|---|---|
| `@<marketplace>` | installed from an added marketplace | `enabledPlugins` true/false |
| `@inline` | `--plugin-dir`, `--plugin-url`, `CLAUDE_CODE_PLUGIN_DIRS`, or SDK `plugins` option; session only | on unless manifest `defaultEnabled: false` or `"<name>@inline": false` |
| `@skills-dir` | plugin dir with `.claude-plugin/plugin.json` under `~/.claude/skills/` or project `.claude/skills/` | manifest `defaultEnabled`, or `"<name>@skills-dir"` true/false |
| `@synced` | synced from claude.ai | on unless `defaultEnabled: false` or `"<name>@synced": false`; org-required loads regardless |

`inline`, `skills-dir` and `synced` are reserved and cannot be marketplace names. Entry name (install and enable key, cache dir name) can differ from manifest `name` (component namespace, name-conflict comparison).

# Limits and defaults

- Share through a repo via `enabledPlugins` in `.claude/settings.json` or `.claude/skills/`; a project `.claude/plugins/` is not scanned. Cloud sessions do not add repo `extraKnownMarketplaces` (no trust dialog).
- Project-scope plugins load only after the workspace trust check (parent-folder trust or `-p` is not enough). MCP servers go through per-server approval like `.mcp.json`; MCP bundles (`.mcpb`/`.dxt`) or files outside the plugin dir are skipped; background monitors do not load. These limits do not apply to `~/.claude/skills/`.
- A repo `.claude/skills/` plugin is read only from the session's primary working directory (no parent search); use `/cd` (v2.1.246+) or launch from root. Desktop app worktrees load from the main checkout.
- Managed settings skip skills-directory plugins silently when `strictPluginOnlyCustomization` locks any kind, or an allowlist lacks `{ "source": "skills-dir" }`, or a blocklist has it. Plain `SKILL.md` at the folder root still loads unless skills are locked. Check `/status` for `Enterprise managed settings`.
