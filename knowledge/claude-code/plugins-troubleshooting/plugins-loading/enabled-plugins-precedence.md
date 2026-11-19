---
type: "Reference"
title: "enabledPlugins sources and precedence"
description: "The six settings sources for enabledPlugins in order of precedence, and why a disabled or project-enabled plugin still loads or not."
resource: "https://code.claude.com/docs/en/plugins/loading"
tags: [plugins, settings, precedence, scopes, add-dir]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless]
requires: ""
identifiers:
  - "enabledPlugins"
  - "--add-dir"
  - "--settings"
  - "--setting-sources"
  - ".claude/settings.json"
  - ".claude/settings.local.json"
  - "~/.claude/settings.json"
  - "claude plugin install <name>@<marketplace> --scope project"
  - "--scope user"
  - "CLAUDE_CODE_SYNC_PLUGIN_INSTALL"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-loading"
    resource: "https://code.claude.com/docs/en/plugins/loading"
    title: "Plugin loading reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

An `enabledPlugins` entry can be set in six sources, merged key by key; for each plugin id the highest-precedence source that mentions it wins.

# How to use it

| Source (lowest to highest) | Where | Reaches |
|---|---|---|
| `--add-dir` | `.claude/settings.json` or `.claude/settings.local.json` in the added directory | this session only; only `true` has effect and every other source overrides it |
| `user` | `~/.claude/settings.json` | you, all projects |
| `project` | `.claude/settings.json` | everyone who clones |
| `local` | `.claude/settings.local.json` | you, this repo |
| `flag` | `--settings` value | this session |
| `managed` | managed settings | all covered users; `true` force-enables, `false` blocks, nothing overrides |

A plugin `false` in user settings but `true` in a higher source shows `Disabled in ~/.claude/settings.json but still loads — ...` naming `project`, `project, gitignored`, `cli flag` or `managed`. To opt out of a project-enabled plugin, set `false` in `.claude/settings.local.json`.

An `--add-dir` directory's `true` is read only if its setting source is on: `settings.json` needs `project`; `settings.local.json` needs `project` and `local` (`--setting-sources user,project` / `user,project,local`). In the CLI `user`, `project`, `local` are on by default.

Project-enabled but not installed: the plugin does not load until installed: `claude plugin install <name>@<marketplace> --scope project` (repeat per clone, or `--scope user`), then `/reload-plugins`. No install is needed for seed-directory plugins, relative-path plugins from a locally added marketplace, or relative-path plugins of a git marketplace (`/reload-plugins` for the current session; for one `-p` run set `CLAUDE_CODE_SYNC_PLUGIN_INSTALL=1`).

# Limits and defaults

Claude Code fetches an external-source plugin only when set `true` by user settings, an untracked `.claude/settings.local.json`, the `--settings` flag, or managed settings.
