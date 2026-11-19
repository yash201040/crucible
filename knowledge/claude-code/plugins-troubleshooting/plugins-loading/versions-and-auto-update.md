---
type: "Feature"
title: "Plugin versions, refresh and auto-update rules"
description: "How the plugin version is computed, when a marketplace refreshes before install, and which marketplaces auto-update and when."
resource: "https://code.claude.com/docs/en/plugins/loading"
tags: [plugins, versions, auto-update, refresh, command-source]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless]
requires: ""
identifiers:
  - "version"
  - "DISABLE_UPDATES"
  - "DISABLE_AUTOUPDATER"
  - "FORCE_AUTOUPDATE_PLUGINS"
  - "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC"
  - "claude plugin update"
  - "claude plugin install"
  - "/plugin install"
  - "/reload-plugins"
  - "/reload-plugins --force"
  - "headersHelper"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-loading"
    resource: "https://code.claude.com/docs/en/plugins/loading"
    title: "Plugin loading reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Code computes a version per installed plugin and uses it to detect updates and name the cache dir. `claude plugin update` and background auto-update recompute it and skip replacing the cache when it matches `installed_plugins.json` (`<name> is already at the latest version (<version>).`).

# How to use it

Version order for every source except `command`: manifest `version`, then marketplace entry `version`, then by source type:

| Source | Version if none set |
|---|---|
| `github`, `url`, `git-subdir` | source commit SHA, 12 chars (`git-subdir` also carries a hash of the path) |
| `archive` | SHA-256 digest, 12 chars (`sha256` pin or the downloaded file) |
| relative path in a Git marketplace | commit SHA of the installed directory |
| local dir, no git | `unknown` |
| `npm` | `unknown` |

A repository enclosing the install path is not used. `command` sources always derive the version from output (12-char hash, or `<manifest version>-<hash>`); entry `version` ignored. A marketplace hosted on claude.ai uses the version claude.ai records. In-place local plugins load current files regardless of version.

Pre-install refresh: `name@marketplace` (either `/plugin install` or `claude plugin install`) refreshes the named marketplace first, independent of auto-update or `DISABLE_AUTOUPDATER`; `name` alone with `/plugin install` refreshes only auto-update marketplaces and only after a miss; `claude plugin install name` refreshes nothing. On failure it uses the cached catalog (`marketplace not refreshed`). Refresh is skipped for local `file`/`directory` or inline `settings` marketplaces, seed-supplied ones, one refreshed within 30 seconds, `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`, or policy-blocked ones.

# Limits and defaults

- Auto-update runs in an interactive session after the first message plus a random delay up to ten minutes, refreshing every auto-update marketplace and updating installed plugins on disk. Notice: `Plugin updated: <name> · Run /reload-plugins to apply`; new versions load next launch regardless.
- Marketplace auto-update precedence: `autoUpdate` on its `extraKnownMarketplaces` entry, then `autoUpdate` in `known_marketplaces.json` (the `/plugin` toggle), then default: on for Anthropic official marketplaces such as `claude-plugins-official` and for marketplaces added from claude.ai; off for `knowledge-work-plugins`, `first-party-plugins` and all others.
- `DISABLE_UPDATES=1`, `DISABLE_AUTOUPDATER=1` or `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1` turn the whole pass off and hide the toggle unless `FORCE_AUTOUPDATE_PLUGINS=1`. Auto-update skips plugins whose entry declares `headersHelper`.
- Mid-session updates: hook commands, monitors, MCP and LSP servers keep the old path until `/reload-plugins` (monitors need a restart).
- `command` source re-run: on every install/update, once per session in the background for each enabled command plugin (independent of auto-update), and at startup or `/reload-plugins` when the installed version is missing from cache; skipped by `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` except explicit installs/updates. Changed output installs a new version and reloads in place; if that would invalidate the prompt cache, it prompts for `/reload-plugins`, which warns about cost and applies with `--force`.
