---
type: "Reference"
title: "Settings, environment variables and commands for mods"
description: "Settings keys and env vars that affect mods, the sec-default guard, and the claude plugin validate and test commands."
resource: "https://code.claude.com/docs/en/plugins/mods/reference"
tags: [mods, settings, managed-settings, cli]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.326"
surfaces: [cli, desktop, ide]
requires: ""
identifiers:
  - "CLAUDE_CODE_PLUGIN_DIRS"
  - "CLAUDE_CODE_PLUGIN_DIR_WATCH"
  - "prependPlugins"
  - "appendPlugins"
  - "allowManagedModsOnly"
  - "allowModsToOverrideDenyRules"
  - "allowManagedHooksOnly"
  - "disableAllHooks"
  - "disableSideloadFlags"
  - "pluginConfigs"
  - "--plugin-url"
  - "claude plugin validate <directory>"
  - "--strict"
  - "--json"
  - "claude plugin test [directory]"
  - "claude --plugin-dir <directory>"
  - "/reload-plugins"
  - "/plugin"
  - "sec-default@builtin"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-reference"
    resource: "https://code.claude.com/docs/en/plugins/mods/reference"
    title: "Mods reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

| Name | Where | What it does |
| :- | :- | :- |
| `CLAUDE_CODE_PLUGIN_DIRS` | environment, or `env` in `~/.claude/settings.json` | plugin directories loaded as `--plugin-dir` does, for apps you cannot pass a flag to; absolute paths separated by `:` (`;` on Windows) |
| `CLAUDE_CODE_PLUGIN_DIR_WATCH` | environment | whether mods reload on save (defaults in the env vars reference) |
| `prependPlugins`, `appendPlugins` | managed settings (user settings only on a machine with no managed settings or `managed-mcp.json`, in a session whose credential is not a Team or Enterprise `/login`) | lists of plugin ids such as `acme-guard@acme-tools`; prepend mods run before every user-installed mod, append mods after, in listed order |
| `allowManagedModsOnly` | managed settings, option on the built-in guard | only mods that count as the organization's, and built-in mods, run hooks; users' settings hooks keep running |
| `allowModsToOverrideDenyRules` | managed settings, option on the guard | lets a user-installed mod approve a tool call past most default-standing outcomes, including a `deny` rule |
| `allowManagedHooksOnly` | managed settings | blocks hooks and installed mods that are not the organization's |
| `disableAllHooks` | any settings file | in managed settings no mod or hook from an installed plugin runs; in your own settings what the organization manages keeps running |
| `disableSideloadFlags` | managed settings | rejects `--plugin-dir` and `--plugin-url` at startup |
| `pluginConfigs` | user or managed settings | `userConfig` values for a mod, keyed by plugin id (`acme-guard@acme-tools`) or name plus `@inline` (`first-mod@inline`) for `--plugin-dir` |

`sec-default@builtin` (shown as `cc-plugin-sec-default`) runs ahead of every user-installed mod where it loads; if managed `prependPlugins` is set the guard loads only when that list names it, at the listed position. Source: `mods/sec-default` in the Claude Code repository.

# How to use it

| Command | What it does |
| :- | :- |
| `/plugin` | shows a line such as `1 mod active · first-mod` under its tabs |
| `claude plugin validate <directory>` | reads manifest and hooks module; reports errors, events handled, mods API calls; `--strict` treats warnings as errors, `--json` prints a machine-readable report |
| `claude plugin test [directory]` | runs every file ending `.test.ts` or `.test.tsx` under the directory (or current); exits 1 when a test fails |
| `claude --plugin-dir <directory>` | loads a plugin directory for one session, reloads hooks module on save; repeat to load several |
| `/reload-plugins` | reloads plugins |
