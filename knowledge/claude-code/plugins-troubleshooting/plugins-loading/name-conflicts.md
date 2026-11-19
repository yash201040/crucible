---
type: "Concept"
title: "Plugin name conflict precedence"
description: "Which plugin wins when enabled plugins share a manifest name, and how same-name hooks and session-only plugins behave."
resource: "https://code.claude.com/docs/en/plugins/loading"
tags: [plugins, name-conflicts, precedence, hooks]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.296"
surfaces: [cli]
requires: "Same-name hooks note needs Claude Code v2.1.296 or later"
identifiers:
  - "--plugin-dir"
  - "--plugin-url"
  - "CLAUDE_CODE_PLUGIN_DIRS"
  - "<name>@inline"
  - "hooks/hooks.json"
  - "enabledPlugins"
  - "--debug"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-loading"
    resource: "https://code.claude.com/docs/en/plugins/loading"
    title: "Plugin loading reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

When enabled plugins from different origins share a manifest name, this order decides which loads (highest first):
1. A plugin whose id is in managed `enabledPlugins` (true or false); a `--plugin-dir` copy is ignored with `--plugin-dir copy of "<name>" ignored: plugin is locked by managed settings`.
2. Enabled `--plugin-dir`, `--plugin-url` or `CLAUDE_CODE_PLUGIN_DIRS` plugin. It silently replaces an installed marketplace plugin (only `--debug` log under `~/.claude/debug/` records `overrides installed version`) and replaces a skills-directory plugin with a `Not loaded` Errors-tab row.
3. Installed marketplace plugin.
4. Skills-directory plugin (`~/.claude/skills/` beats project `.claude/skills/`).
5. Synced plugin (reported as not loaded if any other enabled plugin has the name).

Comparison is by manifest name, so `--plugin-dir` `hello-plugin` replaces `hello@example-marketplace` if its manifest says `hello-plugin`.

# Limits and defaults

Two enabled plugins with the same manifest name from different marketplaces: only one registers `hooks/hooks.json` hooks and one loads a hooks module; a managed-enabled copy holds the name, else the first loaded. The Errors tab note begins `Its hooks.json hooks do not run` or `Its hooks module does not load`. To switch, disable or uninstall the holder and run `/reload-plugins`; a managed-enabled holder cannot be disabled.

# Notes

To stop a session-only plugin shadowing anything (or when a parent process passes the flag), set `"hello-plugin@inline": false` in any settings file; a disabled session-only plugin does not shadow.
