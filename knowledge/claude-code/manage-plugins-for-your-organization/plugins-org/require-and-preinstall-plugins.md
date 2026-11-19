---
type: "Feature"
title: "Require and pre-install plugins by managed settings"
description: "Managed settings register marketplaces and force-enable plugins on every machine, or per repository, with delivery by server, MDM or file."
resource: "https://code.claude.com/docs/en/plugins/org"
tags: [plugins, managed-settings, marketplace, enterprise, ci]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, cloud]
requires: "Server-managed delivery needs a Claude for Teams or Enterprise organization and an Owner role"
identifiers:
  - "extraKnownMarketplaces"
  - "additionalMarketplaces"
  - "enabledPlugins"
  - "managedSourcesBehavior"
  - "managed-settings.json"
  - "managed-settings.d/"
  - "autoUpdate"
  - "claude plugin install <name>@<marketplace> --scope project"
  - "CLAUDE_CODE_SYNC_PLUGIN_INSTALL"
  - "hasTrustDialogAccepted"
  - "claude-plugins-official"
  - "/plugin"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-org"
    resource: "https://code.claude.com/docs/en/plugins/org"
    title: "Manage Claude Code plugins for your organization"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Two managed-settings keys install plugins for a fleet: `extraKnownMarketplaces` registers a marketplace (keyed by the marketplace's own `name`), and `enabledPlugins` names plugins as `plugin-name@marketplace-name`. Users cannot override managed settings; a user disabling a force-enabled plugin does not stop it loading. Setting a plugin to `false` in managed `enabledPlugins` blocks it at every scope and hides it.

# How to use it

Delivery mechanisms (three):
- Server-managed settings: JSON at Organization settings > Claude Code > Managed settings (Owner role). Cloud sessions wait for these before installing plugins.
- MDM: macOS plist with settings keys at top level; Windows registry value holding the JSON as a string.
- Managed file: `managed-settings.json` at the platform system path, plus optional `managed-settings.d/` drop-ins.

By default only the first source that delivers a policy key applies (server, then MDM, then file). Server-delivered settings with even one unrelated key make the MDM and file plugin keys be ignored on that machine. Set `managedSourcesBehavior` to `"merge"` to apply all sources.

Example entry: `"extraKnownMarketplaces": {"your-marketplace": {"source": {"source": "github", "repo": "your-org/your-marketplace"}, "autoUpdate": true}}` plus `"enabledPlugins": {"code-formatter@your-marketplace": true}`. Registration and install happen at the start of the user's next session. A managed marketplace entry replaces a same-name lower-precedence entry; fields do not merge. `claude-plugins-official` needs no `extraKnownMarketplaces` entry when one of its plugins is enabled.

Per repository: put the same keys in `.claude/settings.json`. `extraKnownMarketplaces` applies only in a trusted folder (silently ignored otherwise); for `-p` runs, only where trust was accepted interactively or `hasTrustDialogAccepted` is set in `~/.claude.json`. `enabledPlugins` in a repo does not install; each contributor runs `claude plugin install <name>@<marketplace> --scope project`. Relative-path `directory`/`file` marketplaces resolve against the main checkout, so all worktrees share it.

| Surface | Managed keys | Repo `.claude/settings.json` |
|---|---|---|
| Terminal, interactive | applied at session start | marketplaces after trust; plugins at start |
| `-p` and CI | applied at start, installs in background | marketplaces in trusted folders only; plugins applied |
| Cloud sessions | only server-managed settings reach an Anthropic-hosted session | see Install docs |

In `-p`/CI, plugins install in the background so one can be missing on the first turn: set `CLAUDE_CODE_SYNC_PLUGIN_INSTALL=1` to wait before the first query.

Confirm: run `/plugin`, or `claude -p --output-format stream-json --verbose` and read the `plugins` list in the `init` event.

# Notes

Aliases `additionalMarketplaces` (for `extraKnownMarketplaces`) need v2.1.232 or later; older clients ignore them. When both spellings are set the canonical key wins. Bundles with dependencies are rolled out by putting the bundle plugin in `enabledPlugins`. Private git marketplaces need each user to have git read access with stored credentials (no prompts).
