---
type: "Reference"
title: "Managed settings delivery mechanisms and priority"
description: "The four ways managed policy reaches a machine, their priority order, file paths and the WSL rule."
resource: "https://code.claude.com/docs/en/admin-setup"
tags: [managed-settings, mdm, precedence, server-managed]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop]
requires: "Teams or Enterprise plan for admin-console delivery"
identifiers:
  - "managed-settings.json"
  - "com.anthropic.claudecode"
  - "HKLM\\SOFTWARE\\Policies\\ClaudeCode"
  - "HKCU\\SOFTWARE\\Policies\\ClaudeCode"
  - "/etc/claude-code/managed-settings.json"
  - "/Library/Application Support/ClaudeCode/managed-settings.json"
  - "wslInheritsWindowsSettings"
  - "fallbackModel"
  - "availableModels"
  - "modelPicker"
  - "permissions.allow"
  - "permissions.deny"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "admin-setup"
    resource: "https://code.claude.com/docs/en/admin-setup"
    title: "Set up Claude Code for your organization"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Managed settings take precedence over user and project settings (apart from a few security-sensitive exceptions). Claude Code checks four sources in priority order.

# How to use it

| Mechanism | Delivery | Priority | Platforms |
| :- | :- | :- | :- |
| Server-managed | claude.ai admin console, or self-hosted Claude apps gateway | Highest | All |
| plist / registry policy | macOS `com.anthropic.claudecode` plist; Windows `HKLM\SOFTWARE\Policies\ClaudeCode` | High | macOS, Windows |
| File-based | macOS `/Library/Application Support/ClaudeCode/managed-settings.json`; Linux/WSL `/etc/claude-code/managed-settings.json`; Windows `C:\Program Files\ClaudeCode\managed-settings.json` | Medium | All |
| Windows user registry | `HKCU\SOFTWARE\Policies\ClaudeCode` | Lowest | Windows only |

Server-managed settings are fetched at startup and refreshed hourly; the admin console route needs Teams or Enterprise. Bedrock, Vertex and Foundry deployments can get remote delivery through a Claude apps gateway, or use file/OS mechanisms. Mixed-provider orgs should combine server-managed settings with a file or plist/registry fallback.

# Limits and defaults

- HKLM and plist resist tampering (admin to write); HKCU is writable without elevation, so it is a convenience, not enforcement.
- WSL reads only `/etc/claude-code` by default; `wslInheritsWindowsSettings: true` in an admin-only Windows source extends Windows policy to WSL.
- Array settings such as `permissions.allow` and `permissions.deny` merge lower-precedence entries in, so developers can extend but not remove managed entries. `fallbackModel`, `availableModels` and `modelPicker` managed values replace lower layers.
