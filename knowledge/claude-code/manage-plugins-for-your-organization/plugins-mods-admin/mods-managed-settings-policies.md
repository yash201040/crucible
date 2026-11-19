---
type: "Feature"
title: "Mod policies via managed settings"
description: "Managed settings that decide whether user-installed mods run: allowManagedModsOnly, allowManagedHooksOnly, disableAllHooks, disableSideloadFlags."
resource: "https://code.claude.com/docs/en/plugins/mods/admin"
tags: [mods, managed-settings, policy, hooks, admin]
kind: "setting"
maturity: "unlabelled"
since: "2.1.286"
surfaces: [cli]
requires: "Claude Code v2.1.286 or later (mods on by default); managed settings"
identifiers:
  - "pluginConfigs"
  - "cc-plugin-sec-default@builtin"
  - "allowManagedModsOnly"
  - "allowModsToOverrideDenyRules"
  - "allowManagedHooksOnly"
  - "disableAllHooks"
  - "disableSideloadFlags"
  - "CLAUDE_CODE_ENABLE_FUNCTION_HOOKS"
  - "--plugin-dir"
  - "--plugin-url"
  - "--safe-mode"
  - "managed-settings.json"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-admin"
    resource: "https://code.claude.com/docs/en/plugins/mods/admin"
    title: "Manage mods for your organization"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A mod is a plugin that runs code inside Claude Code with the installing user's permissions and is not sandboxed. Through managed settings an admin decides whether mods run, which ones, and in what order. Mods are on by default from v2.1.286.

# How to use it

Policy table:

| Goal | Settings |
|---|---|
| No installed mod runs, settings hooks untouched | guard option `allowManagedModsOnly` and no own mods |
| No mods and no hooks at all (managed hooks too) | `disableAllHooks: true` |
| Only organization's mods | `allowManagedModsOnly` plus install your mods so they count as yours (plus `disableSideloadFlags`) |
| Any mod from approved marketplaces | marketplace restrictions plus `disableSideloadFlags: true` |
| Any mod, own mod checks others | install your mod, list it with `sec-default@builtin` in `prependPlugins` |

Example (managed-settings.json):

```json
{ "pluginConfigs": { "cc-plugin-sec-default@builtin": { "options": { "allowManagedModsOnly": true } } } }
```

Setting meanings: `allowManagedModsOnly` (guard option) refuses all user mods incl. `--plugin-dir` and mods Claude wrote in-session; users' settings hooks, status lines, `/goal` keep working. `allowManagedHooksOnly` is wider: only org mods and built-in mods load and it also blocks hooks in users' own settings files. `disableAllHooks` is widest: stops mods in every installed plugin (yours included) and all settings hooks, so managed `PreToolUse` hooks stop blocking; custom status lines and `/goal` stop. `disableSideloadFlags` rejects `--plugin-dir` and `--plugin-url` at startup, keeps session-written mods from loading, and also rejects `--agents` and `--mcp-config`.

# Limits and defaults

- Option is read only from managed settings; the same entry in user, project, local settings or `--settings` file does nothing. Option id has one form: `cc-plugin-sec-default@builtin`.
- v2.1.287 and later ignore `CLAUDE_CODE_ENABLE_FUNCTION_HOOKS` at any value; replace a `0` from early access with `allowManagedModsOnly`.
- `claude --safe-mode` turns installed mods off (org mods too). No mod is loaded in an untrusted directory until the trust prompt is answered.
- Built-in mods (such as `AGENTS.md` support) each have their own switch and are not affected.
- Verify: `claude --plugin-dir ./first-mod` shows the guard message naming `allowManagedModsOnly`; with `claude --debug`, a refused user mod logs `refused by cc-plugin-sec-default: mods are limited to your organization's by policy (allowManagedModsOnly)`; `--plugin-dir` with `disableSideloadFlags` exits with `--plugin-dir is disabled by your organization's managed settings (disableSideloadFlags)`.
