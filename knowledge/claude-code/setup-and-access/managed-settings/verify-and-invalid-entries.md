---
type: "Guide"
title: "Verifying policy and handling invalid managed entries"
description: "Reading /status and claude doctor, parse failures that stop startup, fail-closed keys and sandbox field handling."
resource: "https://code.claude.com/docs/en/managed-settings#check-that-a-policy-is-in-force"
tags: [managed-settings, validation, fail-closed, doctor]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.282"
surfaces: [cli, headless]
requires: "Fail-closed rule and per-field repair need v2.1.282 or later; per-field sandbox handling v2.1.283+; Skipped sources line v2.1.242+"
identifiers:
  - "/status"
  - "claude doctor"
  - "Setting sources"
  - "Skipped sources"
  - "allowManagedPermissionRulesOnly"
  - "disableAutoMode"
  - "skipDangerousModePermissionPrompt"
  - "permissions.defaultMode"
  - "allowedMcpServers"
  - "allowedProviders"
  - "allowedHttpHookUrls"
  - "httpHookAllowedEnvVars"
  - "allowedChannelPlugins"
  - "strictKnownMarketplaces"
  - "availableModels"
  - "availableModelsMatch"
  - "forceLoginOrgUUID"
  - "gatewayInternalNetworks"
  - "crossSessionInbound"
  - "deniedMcpServers"
  - "deniedModels"
  - "blockedMarketplaces"
  - "sandbox.credentials"
  - "strictPluginOnlyCustomization"
  - "enabledPlugins"
  - "requiredMinimumVersion"
  - "requiredMaximumVersion"
  - "disableAllHooks"
  - "sandbox.failIfUnavailable"
  - "sandbox.network.deniedDomains"
  - "sandbox.filesystem.denyRead"
  - "sandbox.filesystem.denyWrite"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "managed-settings"
    resource: "https://code.claude.com/docs/en/managed-settings"
    title: "Deploy managed settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

How to confirm a policy applied and what Claude Code does when managed values are invalid. `/status` `Setting sources` lists `Enterprise managed settings` with a label: `(remote)`, `(plist)`, `(HKLM)`, `(file)`, `(drop-ins)`, `(file + drop-ins)`, `(remote + file, merged)`, `(HKCU)`, `(parent process)`, `(helper)`. `Skipped sources` (v2.1.242+) names sources found but not selected. A missing line means no policy key was found; `claude doctor` reports the fetch outcome for server-managed settings.

# How to use it

- Individual invalid entries are repaired or skipped with warnings (startup dialog interactive; stderr summary with `-p`; `claude doctor` lists source and field).
- A managed file, drop-in, plist or HKLM value that exists but is not a JSON object makes Claude Code refuse to start even if another source is valid. Absent source is fine; empty file counts as `{}`; malformed HKCU only gives a notice. Unreadable-by-OS-permission: sessions start without that source (`-p` prints to stderr); other I/O errors: sessions exit asking to contact an administrator.
- Fail-closed keys (single restrictive value, e.g. `allowManagedPermissionRulesOnly`, `disableAutoMode`, `skipDangerousModePermissionPrompt`) read as that value when invalid; `null` removes a key; invalid `disableAllHooks` is dropped. Quoted `"true"`/`"false"` read as Boolean with a notice. `permissions`, `autoMode`, `worktree`, `attribution` repaired per field; invalid `permissions.defaultMode` reads as `default`; an unreadable `deny`/`ask` list withholds `allow` and `additionalDirectories`; unreadable `soft_deny`/`hard_deny` withholds `allow` and `environment`.

# Limits and defaults

| Key | When present but invalid |
| :- | :- |
| `allowedMcpServers` | empty allowlist (provided/managed-mcp servers still load) |
| `allowedProviders` | empty allowlist; Claude Code won't start |
| `allowedHttpHookUrls`, `httpHookAllowedEnvVars`, `allowedChannelPlugins` | empty allowlist (v2.1.267+) |
| `strictKnownMarketplaces` | empty allowlist (v2.1.277+) |
| `availableModels` | only Default model available |
| `availableModelsMatch` | treated `exact` |
| `forceLoginOrgUUID` | no organization may log in |
| `gatewayInternalNetworks` | `/login` refuses new gateway sign-ins |
| `crossSessionInbound` | `refuse` |
| `deniedMcpServers`, `deniedModels`, `blockedMarketplaces` | bad entries stripped; wholly invalid value dropped (blocks nothing) |
| `strictPluginOnlyCustomization` | `true` (locks all four surfaces) |
| `enabledPlugins` | bad entries dropped (v2.1.282+) |
| `requiredMinimumVersion`, `requiredMaximumVersion` | fail open: dropped |

Sandbox (v2.1.283+ per field): bad Booleans take the strictest value (enabling keys true, loosening keys false); invalid `failIfUnavailable` is dropped; bad list entries dropped; invalid `network.deniedDomains` withholds `network.allowedDomains`; invalid `filesystem.denyRead`/`denyWrite` withholds both `allowRead` and `allowWrite`. Before v2.1.283 all sandbox fields except `credentials` were dropped. User/project/local files stay strict: a file failing shape validation is rejected whole.
