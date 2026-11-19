---
type: "Reference"
title: "Hook locations, scope and managed restrictions"
description: "Where hooks can be defined, how they merge, and the managed settings that restrict hooks and HTTP hook URLs."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, settings, managed-policy, scope]
kind: "setting"
maturity: "unlabelled"
since: "2.1.229"
surfaces: [cli, ide, desktop, cloud]
requires: ""
identifiers:
  - "~/.claude/settings.json"
  - ".claude/settings.json"
  - ".claude/settings.local.json"
  - "hooks/hooks.json"
  - "allowManagedHooksOnly"
  - "disableCommandPluginSources"
  - "allowedHttpHookUrls"
  - "httpHookAllowedEnvVars"
  - "statusLine"
  - "fileSuggestion"
  - "enabledPlugins"
  - "disableAllHooks"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Where a hook is defined sets its scope. Hook entries merge across levels: user, project and local settings add hooks without removing managed ones.

# How to use it

| Location | Scope | Shareable |
| :- | :- | :- |
| `~/.claude/settings.json` | All your projects | No |
| `.claude/settings.json` | Single project | Yes, committable |
| `.claude/settings.local.json` | Single project | No (gitignored when Claude Code saves a setting to it) |
| Managed policy settings | Organization-wide | Yes, admin-controlled |
| Plugin `hooks/hooks.json` | While the plugin is enabled | Yes |
| Skill frontmatter | Rest of the session once the skill is invoked | Yes |
| Subagent frontmatter | While that subagent runs | Yes |

Hooks from settings files, managed policy and plugins also run inside subagents: `PreToolUse`/`PostToolUse` fire the same configured hooks, with `agent_id` and `agent_type` in the input.

`allowManagedHooksOnly` (managed settings): blocks user, project, local and plugin hooks (plugins force-enabled in managed `enabledPlugins` are exempt); narrows `statusLine` and `fileSuggestion` to managed settings; disables plugins with a `command` source (including force-enabled ones) unless `disableCommandPluginSources` is explicitly `false` (`command` sources need v2.1.229+); blocks marketplace `headersHelper` commands under the same condition except marketplaces declared by managed settings.

HTTP hook allowlists (managed or any settings file): `allowedHttpHookUrls` (HTTP handler runs only if its URL matches the merged list) and `httpHookAllowedEnvVars` (only listed env vars are interpolated into headers).

# Limits and defaults

- Cloud sessions do not read local `~/.claude/settings.json`. In a self-hosted environment, hooks seeded from the runner host's `~/.claude/` also run, plus hooks in the runner image's managed settings file when it is among the applied managed sources (by default only when neither server-managed settings nor MDM policy supplies the managed tier).
- The same handler defined in several settings files runs once; a plugin's or skill's copy stays separate.
- `disableAllHooks` cannot disable managed hooks from outside managed settings. See [disable or remove hooks](./p1-hooks-menu-and-disabling.md).
