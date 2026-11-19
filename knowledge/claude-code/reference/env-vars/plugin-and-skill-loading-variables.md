---
type: "Reference"
title: "Plugin, marketplace and skill sync variables"
description: "Variables for plugin directories, caches, marketplace cloning and auto-install, synchronous plugin install in headless runs, and claude.ai skill sync."
resource: "https://code.claude.com/docs/en/env-vars"
tags: [plugins, skills, marketplace, headless]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "CLAUDE_CODE_PLUGIN_CACHE_DIR"
  - "CLAUDE_CODE_PLUGIN_DIRS"
  - "CLAUDE_CODE_PLUGIN_DIR_WATCH"
  - "CLAUDE_CODE_PLUGIN_GIT_TIMEOUT_MS"
  - "CLAUDE_CODE_PLUGIN_KEEP_MARKETPLACE_ON_FAILURE"
  - "CLAUDE_CODE_PLUGIN_PREFER_HTTPS"
  - "CLAUDE_CODE_PLUGIN_SEED_DIR"
  - "CLAUDE_CODE_DISABLE_OFFICIAL_MARKETPLACE_AUTOINSTALL"
  - "FORCE_AUTOUPDATE_PLUGINS"
  - "CLAUDE_CODE_ENABLE_BACKGROUND_PLUGIN_REFRESH"
  - "CLAUDE_CODE_SYNC_PLUGIN_INSTALL"
  - "CLAUDE_CODE_SYNC_PLUGIN_INSTALL_TIMEOUT_MS"
  - "CLAUDE_CODE_SYNC_SKILLS"
  - "CLAUDE_CODE_SYNC_SKILLS_INSTALL_TIMEOUT_MS"
  - "CLAUDE_CODE_SYNC_SKILLS_WAIT_TIMEOUT_MS"
  - "CLAUDE_CODE_DISABLE_BUNDLED_SKILLS"
  - "CLAUDE_CODE_DISABLE_POLICY_SKILLS"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "env-vars"
    resource: "https://code.claude.com/docs/en/env-vars"
    title: "Environment variables"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Packaging controls for plugins and skills, including what an unattended `-p` run has available on its first turn.

# How to use it

| Variable | What it does |
| :- | :- |
| `CLAUDE_CODE_PLUGIN_CACHE_DIR` | Plugins root directory (not the cache itself; marketplaces and cache live in subdirectories). Default `~/.claude/plugins`. |
| `CLAUDE_CODE_PLUGIN_DIRS` | Plugin directories loaded for the session as `--plugin-dir` does; separate with `:` (Unix) or `;` (Windows); absolute paths or leading `~`, relative paths skipped. Requires v2.1.280+. |
| `CLAUDE_CODE_PLUGIN_DIR_WATCH` | Mod reload on file change. Default: mods in skills directories reload in any session taking more than one prompt (non-interactive included); mods in `--plugin-dir` directories reload only in interactive terminal sessions. `1` reloads them like skills-directory mods, `0` turns reloading off everywhere. Requires v2.1.287+. |
| `CLAUDE_CODE_PLUGIN_GIT_TIMEOUT_MS` | Timeout for cloning or refreshing a marketplace (default 120000). |
| `CLAUDE_CODE_PLUGIN_KEEP_MARKETPLACE_ON_FAILURE` | `1` skips re-clone and keeps the existing marketplace checkout when a refresh cannot reach or authenticate to the remote (offline or airgapped). |
| `CLAUDE_CODE_PLUGIN_PREFER_HTTPS` | `1` clones GitHub `owner/repo` shorthand over HTTPS instead of SSH, for install, update and `/plugin marketplace add` and `update` (CI, containers without an SSH key). |
| `CLAUDE_CODE_PLUGIN_SEED_DIR` | Read-only seed directories (`:` or `;` separated) to bundle a pre-populated plugins directory into a container image; marketplaces registered at startup, pre-cached plugins used without re-cloning. |
| `CLAUDE_CODE_DISABLE_OFFICIAL_MARKETPLACE_AUTOINSTALL` | `1` disables automatic registration of the official plugin marketplace. Read when about to register (usually a first interactive launch); once skipped it stays skipped. Register later with `claude plugin marketplace add anthropics/claude-plugins-official`. |
| `FORCE_AUTOUPDATE_PLUGINS` | `1` forces plugin auto-updates even when `DISABLE_AUTOUPDATER` is set. |
| `CLAUDE_CODE_ENABLE_BACKGROUND_PLUGIN_REFRESH` | `1` refreshes plugin state at turn boundaries in non-interactive mode after a background install completes. Off by default because it changes the system prompt mid-session, invalidating prompt caching for that turn. |
| `CLAUDE_CODE_SYNC_PLUGIN_INSTALL` | `1` in `-p` mode waits for plugin installation before the first query; otherwise plugins install in the background and may be missing on turn one. |
| `CLAUDE_CODE_SYNC_PLUGIN_INSTALL_TIMEOUT_MS` | Bound for that wait; on timeout Claude Code proceeds without plugins and logs an error. No default (waits until complete). |
| `CLAUDE_CODE_SYNC_SKILLS` | `1` downloads skills enabled for your claude.ai account; in `-p` mode also waits up to `CLAUDE_CODE_SYNC_SKILLS_WAIT_TIMEOUT_MS` for the list before the first query. Needs claude.ai auth. Terminal sessions signed in with claude.ai sync without it; interactive use of the variable needs v2.1.323+. |
| `CLAUDE_CODE_SYNC_SKILLS_INSTALL_TIMEOUT_MS` | Timeout for the mid-session skills resync when an Agent SDK app reloads skills (default 30000); on expiry the reload continues with arrived skills and the rest finish in the background. |
| `CLAUDE_CODE_SYNC_SKILLS_WAIT_TIMEOUT_MS` | First-query wait for the initial skill list (default 5000); then the query runs with arrived skills, and Claude waits for a skill's download when invoking it. |
| `CLAUDE_CODE_DISABLE_BUNDLED_SKILLS` | `1` removes bundled skills and workflows entirely; built-in commands like `/init` stay typable but hidden from the model; `/doctor` stays typable (hide with `DISABLE_DOCTOR_COMMAND`). Skills from plugins, `.claude/skills/`, `.claude/commands/` unaffected. Same as `disableBundledSkills`. |
| `CLAUDE_CODE_DISABLE_POLICY_SKILLS` | `1` skips skills from the system-wide managed skills directory (container or CI sessions). |
