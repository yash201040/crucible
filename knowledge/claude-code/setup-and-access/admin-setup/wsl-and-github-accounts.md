---
type: "Guide"
title: "Desktop WSL sessions and connected GitHub accounts"
description: "How managed policy reaches WSL 2 sessions in Claude Code Desktop and how Owners manage GitHub accounts linked to the organization."
resource: "https://code.claude.com/docs/en/admin-setup"
tags: [wsl, desktop, github, admin]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [desktop]
requires: "Claude Desktop v1.19367.0 or later for the WSL registry policy; Team or Enterprise plan for GitHub accounts"
identifiers:
  - "disableWslSessions"
  - "HKLM\\SOFTWARE\\Policies\\Claude"
  - "wslInheritsWindowsSettings"
  - "allowedWorkspaceFolders"
  - "github_app_installation_linked"
  - "github_app_installation_unlinked"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "admin-setup"
    resource: "https://code.claude.com/docs/en/admin-setup"
    title: "Set up Claude Code for your organization"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Code Desktop can run Code sessions inside a WSL 2 distribution; those sessions resolve managed settings via the WSL path. Separately, Owners can manage GitHub accounts linked to the Claude organization.

# How to use it

- Desktop turns WSL sessions off by default on devices detected as organization-managed (for example when `C:\Program Files\ClaudeCode\managed-settings.json` exists).
- To enable: create `disableWslSessions` under `HKLM\SOFTWARE\Policies\Claude` as `REG_SZ` `false` or `REG_DWORD` `0`. HKCU does not work. Read at each WSL session start, no restart.
- Then deploy `wslInheritsWindowsSettings: true` so WSL sessions inherit policy; check with `/status` `Setting sources`.
- Denials appear in `main.log` as `[wslPolicyGate] denying WSL session` with a reason such as `(cli-file-present)`.
- Processes in the WSL 2 VM are invisible to Windows-side endpoint sensors; OpenTelemetry tool-execution telemetry is identical for WSL and native.
- GitHub: Organization settings > Git providers lists accounts linked via the Claude GitHub App. Requires the Owner role (Admin cannot open it). Unlink via "Unlink from this workspace"; to prevent relinking, uninstall the app on GitHub. Enterprise Compliance API activity types: `github_app_installation_linked`, `github_app_installation_unlinked`.
