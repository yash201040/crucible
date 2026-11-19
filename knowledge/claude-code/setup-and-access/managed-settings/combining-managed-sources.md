---
type: "Reference"
title: "How managed sources are combined"
description: "Source ranking, managedSourcesBehavior first-wins vs merge, cross-source keys, login keys, policyHelper and parent settings."
resource: "https://code.claude.com/docs/en/managed-settings#how-claude-code-combines-managed-sources"
tags: [managed-settings, precedence, merge, policy-helper]
kind: "setting"
maturity: "unlabelled"
since: "2.1.242"
surfaces: [cli, ide, sdk, desktop]
requires: "managedSourcesBehavior merge needs v2.1.242 or later"
identifiers:
  - "managedSourcesBehavior"
  - "first-wins"
  - "merge"
  - "parentSettingsBehavior"
  - "policyHelper"
  - "wslInheritsWindowsSettings"
  - "managedSettings"
  - "sandbox.network.allowManagedDomainsOnly"
  - "sandbox.filesystem.allowManagedReadPathsOnly"
  - "allowAllClaudeAiMcps"
  - "allowManagedMcpServersOnly"
  - "deniedMcpServers"
  - "disableClaudeAiConnectors"
  - "sandbox.bwrapPath"
  - "sandbox.socatPath"
  - "sandbox.ripgrep"
  - "sandbox.filesystem.disabled"
  - "sandbox.network.strictAllowlist"
  - "useAutoModeDuringPlan"
  - "syncClaudeAiSkills"
  - "syncClaudeAiPlugins"
  - "enableArtifact"
  - "maxEffortLevel"
  - "forceRemoteSettingsRefresh"
  - "env"
  - "allowedProviders"
  - "forceLoginOrgUUID"
  - "forceLoginMethod"
  - "allowManagedPermissionRulesOnly"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "managed-settings"
    resource: "https://code.claude.com/docs/en/managed-settings"
    title: "Deploy managed settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

When several managed sources reach one machine, `managedSourcesBehavior` decides: `"first-wins"` (default) uses the highest-ranked source with at least one policy key and ignores the rest silently (`/status` names used and skipped); `"merge"` (v2.1.242+) applies every admin source. Ranking: (1) remote (server-managed or gateway), (2) MDM plist/HKLM, (3) managed files (`managed-settings.d/*.json` + `managed-settings.json`), (4) HKCU (never an admin source; used only when no admin document is present above it and no host-supplied restrictive parent settings). A policy key is any key other than the two control keys `wslInheritsWindowsSettings` and `managedSourcesBehavior`. An admin document is present when it sets any policy key to non-null (even unreadable) or exists but cannot be read.

# How to use it

Set `"managedSourcesBehavior": "merge"` in the highest-ranked source you deploy (read only from the highest-ranked source carrying it or a policy key; a machine without server-managed settings needs it in its MDM profile). Merge turns on lower-source list entries, so use only when every lower source is admin-controlled.

| Kind of key under merge | Combining |
| :- | :- |
| Lists (`permissions.allow`, `hooks`, `sandbox.network.allowedDomains`, `deniedMcpServers`, `deniedModels`) | union |
| Locks (`allowManagedHooksOnly`, `permissions.disableBypassPermissionsMode`, `crossSessionInbound`, `availableModelsMatch`) | strictest wins |
| Restriction allowlists (`availableModels`, `allowedMcpServers`, `strictKnownMarketplaces`, `allowedChannelPlugins`, `fallbackModel` chain) | highest-ranked list whole |
| Values taken whole (`sandbox.credentials.awsPairs`, `sandbox.ripgrep`) | highest-ranked |
| `managedMcpServers` | names combined; higher-ranked entry wins a clash |
| Highest-ranked only (`modelPicker`, `permissions.defaultMode`, `apiKeyHelper` etc.) | lower ignored |
| `env` | per variable across admin sources, either setting (v2.1.223+) |
| Login keys | from MDM/file ahead of remote |
| Others (`model`, `cleanupPeriodDays`) | highest-ranked |

# Limits and defaults

- Cross-source keys read from every admin source even under first-wins: sandbox locks (`sandbox.network.allowManagedDomainsOnly`, `sandbox.filesystem.allowManagedReadPathsOnly`, true anywhere turns on, allowlists union), `allowAllClaudeAiMcps`, `allowManagedMcpServersOnly` (v2.1.273+, highest-ranked admin list wins), `deniedMcpServers` and `disableClaudeAiConnectors` (v2.1.273+), `sandbox.bwrapPath`, `sandbox.socatPath`, `sandbox.ripgrep`, `sandbox.filesystem.disabled`, `sandbox.network.strictAllowlist`, deny-only `useAutoModeDuringPlan`/`syncClaudeAiSkills`/`syncClaudeAiPlugins` (false anywhere), `enableArtifact` (false from any admin turns Artifact tool off, v2.1.242+), `maxEffortLevel` (lowest cap, v2.1.267+), attribution opt-outs, `forceRemoteSettingsRefresh`, `env`.
- Login keys: `forceLoginOrgUUID` and `"claudeai"`/`"console"` `forceLoginMethod` come from the MDM policy or file (policy wins over file even under merge); gateway login keys never from remote settings. Set in server-managed settings too until all clients are v2.1.299+.
- `policyHelper`: an executable named by MDM/file policy, run at startup; its emitted `managedSettings` object is the only managed config (except `forceRemoteSettingsRefresh`). Schema violations after repair fail the helper run and Claude Code refuses to start.
- Parent settings (an embedding host such as Desktop, IDE or Agent SDK app passes `managedSettings`): ignored by default when an admin source exists; `parentSettingsBehavior: "merge"` (highest-priority source only) keeps only restrictive host values, but host allow rules and sandbox allowlists still apply unless `allowManaged*Only` locks are set. Admin `allowManagedPermissionRulesOnly` drops parent allow rules and `additionalDirectories`. `strictKnownMarketplaces` and `blockedMarketplaces` parent handling need v2.1.282+; `allowedProviders` v2.1.285+.
- Cowork folder access: with `allowManagedPermissionRulesOnly`, add allow rules like `Edit(~/CoworkProjects/**)` to the managed source in effect.
