---
type: "Reference"
title: "Plugin files on disk and Node dependency install"
description: "Layout under the plugins root, in-place versus cached loading, escape rules, 14-day cleanup and the lockfile-based npm/Bun dependency install."
resource: "https://code.claude.com/docs/en/plugins/loading"
tags: [plugins, cache, filesystem, npm, dependencies]
kind: "file"
maturity: "unlabelled"
since: "2.1.324"
surfaces: [cli, headless]
requires: "mcpb/ directory needs v2.1.324 or later; the lockfile's package manager must be on PATH"
identifiers:
  - "CLAUDE_CODE_PLUGIN_CACHE_DIR"
  - "${CLAUDE_PLUGIN_ROOT}"
  - "${CLAUDE_PLUGIN_DATA}"
  - "cache/<marketplace>/<plugin>/<version>/"
  - "data/<plugin-id>/"
  - "marketplaces/<name>/"
  - "mcpb/"
  - "synced/"
  - ".trash/"
  - "known_marketplaces_claudeai.json"
  - "flagged-plugins.json"
  - "installed_plugins.set-aside.<date>.<hash>.json"
  - "installed_plugins.unreadable.<date>.<hash>.kept"
  - ".orphaned_at"
  - "cleanupPeriodDays"
  - "bun.lock"
  - "bun.lockb"
  - "npm-shrinkwrap.json"
  - "package-lock.json"
  - "yarn.lock"
  - "pnpm-lock.yaml"
  - "--keep-data"
  - "--ignore-scripts"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-loading"
    resource: "https://code.claude.com/docs/en/plugins/loading"
    title: "Plugin loading reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Plugin state lives under `~/.claude/plugins` unless `CLAUDE_CODE_PLUGIN_CACHE_DIR` is set.

# How to use it

| Path | Holds |
|---|---|
| `cache/<marketplace>/<plugin>/<version>/` | one dir per installed version; `${CLAUDE_PLUGIN_ROOT}` points here |
| `data/<plugin-id>/` | persistent `${CLAUDE_PLUGIN_DATA}`; created on first use, kept across updates, deleted on last-scope uninstall unless `--keep-data` |
| `marketplaces/<name>/` | clone/download of GitHub, git or URL marketplaces (local file/directory marketplaces have no copy) |
| `mcpb/` | extracted MCP bundles (v2.1.324+) |
| `synced/`, `.trash/` | claude.ai synced plugins; plugins sync removed |
| `installed_plugins.json`, `known_marketplaces.json` | records; claude.ai marketplaces in `known_marketplaces_claudeai.json` |
| `flagged-plugins.json` | plugins flagged removed because their marketplace delisted them |
| `installed_plugins.set-aside.<date>.<hash>.json`, `installed_plugins.unreadable.<date>.<hash>.kept` | dated copies kept before dropping/rebuilding records; aged out per `cleanupPeriodDays` |

Because the root path changes per version, keep durable files in `${CLAUDE_PLUGIN_DATA}`.

In place (never copied): `--plugin-dir` and skills-directory plugins (a `--plugin-url` archive or `--plugin-dir` `.zip` is extracted to a session temp dir); relative-path plugins of a locally added marketplace (edits apply next start or `/reload-plugins`; hooks/MCP/LSP get `CLAUDE_PLUGIN_ROOT` pointing at the source); `command` plugins in link mode. All others are copied to the cache; files outside the plugin dir are not copied.

Paths escaping the plugin dir are rejected (`path escapes plugin directory`; plugin loads without that component): `..` paths, symlinks leading outside (except between plugins in one marketplace), and on macOS/Linux any path containing a backslash.

# Limits and defaults

- Cleanup: update or uninstall writes `.orphaned_at` in the old version dir; removed by background cleanup 14 days later; sweep runs only while `installed_plugins.json` has at least one install.
- Dependency install (cannot be turned off): runs on install, update, and when an enabled plugin is not cached; needs `package.json` plus a supported lockfile. Lockfile order: `bun.lock` (Bun, `lockfileVersion` at most 2), `npm-shrinkwrap.json`, `package-lock.json` (npm, `lockfileVersion` 2 or 3). Skipped for `bun.lockb`, `yarn.lock`, `pnpm-lock.yaml`. Missing manager is not substituted. Use `npm-shrinkwrap.json` for npm-source plugins.
- Constraints: registry packages pinned to exact versions only (git/GitHub/folder/workspace/linked deps get no install); lockfile links must be `https` unless the user's own npm registry; runs in a separate folder (plugin `.npmrc`, `.env`, `bunfig.toml` not read); frozen resolution, skipped if `package.json` and lockfile differ; `--ignore-scripts`; skipped for npm `overrides` or Bun `patchedDependencies`; 60-second timeout.
- Not done for relative-path local-marketplace plugins loaded in place. On failure the plugin still loads; `/plugin` and `claude plugin list` note missing `node_modules`. Fallback: install from a hook into `${CLAUDE_PLUGIN_DATA}`.
