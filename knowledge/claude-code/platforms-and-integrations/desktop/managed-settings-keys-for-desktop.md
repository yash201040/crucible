---
type: "Reference"
title: "Managed settings keys for Desktop"
description: "Managed keys that govern Desktop behavior and the Claude Code settings that act differently in the Code tab."
resource: "https://code.claude.com/docs/en/desktop"
tags: [desktop, managed-settings, enterprise, reference]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [desktop]
requires: "Team or Enterprise for admin-console delivery"
identifiers:
  - "permissions.disableBypassPermissionsMode"
  - "disableAutoMode"
  - "autoMode"
  - "browserExternalPageTools"
  - "disableMobileSimulatorTools"
  - "disableBrowserExternalNavigation"
  - "disableRemotePreviewScripts"
  - "managedMcpServers"
  - "parentSettingsBehavior"
  - "requiredMaximumVersion"
  - "askUserQuestionTimeout"
  - "awaySummaryEnabled"
  - "bashEditDiffEnabled"
  - "companyAnnouncements"
  - "defaultShell"
  - "fileSuggestion"
  - "modelPicker"
  - "availableModels"
  - "pluginTrustMessage"
  - "prUrlTemplate"
  - "respectGitignore"
  - "respondToBashCommands"
  - "showClearContextOnPlanAccept"
  - "skipDangerousModePermissionPrompt"
  - "verbose"
  - "viewMode"
  - "worktree.baseRef"
  - "worktree.sparsePaths"
  - "worktree.symlinkDirectories"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "desktop"
    resource: "https://code.claude.com/docs/en/desktop"
    title: "Desktop application"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Managed settings override project and user settings in Desktop sessions. Delivery depends on where the session runs: local sessions use a managed settings file on disk and, with an eligible login, admin-console settings; cloud sessions get server-managed settings only (self-hosted runners also read the file in the runner image); SSH sessions read the file on the remote host, while Desktop itself reads `sshConfigs`, `sshHostAllowlist`, `disableSshSavedPasswords`, `disableDesktopLocalSessions` locally; Cowork sessions never fetch admin-console settings.

# How to use it

| Key | Effect |
| - | - |
| `permissions.disableBypassPermissionsMode` | `"disable"` blocks Bypass permissions |
| `disableAutoMode` | `"disable"` removes Auto mode |
| `autoMode` | customize auto classifier trust and blocks |
| `browserExternalPageTools` | `"disabled"` stops Claude using tools on external pages |
| `disableMobileSimulatorTools` | `true` blocks Claude's iOS simulator tools (JSON boolean; string ignored) |
| `disableBrowserExternalNavigation` | `true` blocks all external navigation |
| `disableRemotePreviewScripts` | `true` stops scripts in SSH/WSL HTML previews (v5.1231.0+) |
| `managedMcpServers` | 3P Desktop only; transport `http`, `sse` or `stdio`, optional `toolPolicy`; gateway delivery needs Claude Code v2.1.232+ on the gateway |
| `parentSettingsBehavior` | set `"merge"` when creating managed settings on a machine that had none, or Claude Code ignores Desktop's embedded policy |

The first three browser/simulator/scripts keys stay off when set in the highest-ranked local MDM policy or file even if server settings leave them unset (v4.4212.0+; scripts key v5.1231.0+).

Code tab differences (keys that still apply in the terminal): `askUserQuestionTimeout` (no timeout), `awaySummaryEnabled` (no effect), `bashEditDiffEnabled`, `companyAnnouncements` (not shown), `defaultShell` (`!` commands use login shell or PowerShell), `fileSuggestion` and `respectGitignore` (picker builds its own list), `modelPicker` (use `availableModels`), `pluginTrustMessage`, `prUrlTemplate`, `respondToBashCommands` (always responds), `showClearContextOnPlanAccept`, `skipDangerousModePermissionPrompt`, `verbose` and `viewMode` (user picks Transcript view), `worktree.baseRef`, `worktree.sparsePaths`, `worktree.symlinkDirectories`.

# Limits and defaults

`requiredMaximumVersion` below the app's own Claude Code version makes local sessions fail with "newer than the maximum version allowed by your organization".
