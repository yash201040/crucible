---
type: "Guide"
title: "Deploying managed settings and delivery mechanisms"
description: "Quick file deployment, the four delivery mechanisms, storage locations, managed-settings.d drop-ins and which surfaces read policy."
resource: "https://code.claude.com/docs/en/managed-settings"
tags: [managed-settings, mdm, drop-in, surfaces]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: [cli, ide, desktop, sdk, cloud]
requires: ""
identifiers:
  - "managed-settings.json"
  - "managed-settings.d/"
  - "managed-mcp.json"
  - "com.anthropic.claudecode"
  - "HKLM\\SOFTWARE\\Policies\\ClaudeCode"
  - "HKCU\\SOFTWARE\\Policies\\ClaudeCode"
  - "forceRemoteSettingsRefresh"
  - "requiredMinimumVersion"
  - "policyHelper"
  - "settingSources"
  - "/status"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "managed-settings"
    resource: "https://code.claude.com/docs/en/managed-settings"
    title: "Deploy managed settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Managed settings are applied above every other level (user, project, local, `--settings`), with a few security-sensitive exceptions where a stricter lower value counts. Quickest route: write `managed-settings.json` (same shape as `settings.json`) and place it at macOS `/Library/Application Support/ClaudeCode/`, Linux/WSL `/etc/claude-code/`, or Windows `C:\Program Files\ClaudeCode\`. Verify with `/status`: `Setting sources` shows `Enterprise managed settings (file)`. The legacy `C:\ProgramData\ClaudeCode\managed-settings.json` is not read. Symlinks are followed (warning in `/status` and `claude doctor` if the target is outside the directory).

# How to use it

| Mechanism | When read | Use when |
| :- | :- | :- |
| Server-managed (admin console or gateway) | startup, polled hourly | one place for a claude.ai org |
| MDM / OS policy (macOS profile `com.anthropic.claudecode`; Windows HKLM value `Settings` under `HKLM\SOFTWARE\Policies\ClaudeCode`, REG_SZ or REG_EXPAND_SZ) | startup, rechecked every 30 minutes | existing MDM / Group Policy |
| File-based (`managed-settings.json`, optional `managed-settings.d/`, `managed-mcp.json`) | startup, reloaded when a file changes | no MDM, Linux, images |
| HKCU registry (Windows/WSL) | startup, rechecked every 30 minutes | cannot write HKLM |

Split policy across teams with `managed-settings.d/*.json`: merged after `managed-settings.json`, alphabetical (use `10-telemetry.json`, `20-security.json`); hidden and non-.json files ignored. Merge rules: single values - later wins; lists - combined and deduplicated; nested blocks - key by key; `fallbackModel` and `modelPicker` - later replaces whole; `extraKnownMarketplaces` and `managedMcpServers` - later same-name entry replaces whole. Starter MDM templates are in the anthropics/claude-code `examples/mdm` repo.

# Limits and defaults

- Surfaces that read policy: terminal, VS Code and JetBrains extensions, desktop Code tab, Agent SDK (managed settings load even when `settingSources` excludes user/project/local).
- Cloud sessions in Anthropic-hosted environments do not read device MDM or files, so use server-managed settings. Self-hosted environments also read the runner image's file, by default only when server-managed delivers no policy key. Claude Tag sessions receive no server-managed settings. Cowork sessions never fetch server-managed settings; on the user's machine they read MDM/file policy; with `requireCoworkFullVmSandbox` or remote Cowork there is no device policy.
- Running sessions: most changes apply without restart. `forceRemoteSettingsRefresh`, `requiredMinimumVersion` and some user-editable keys apply at next session start; a new `policyHelper` at next launch. Server-managed changes needing approval (hooks, `env`) wait for the dialog in interactive sessions and apply for the current run in IDE/SDK hosts. `requiredMinimumVersion` does not end an already-running session.
- Managed `model` and `autoCompactWindow` are defaults, not locks: `--model`, `ANTHROPIC_MODEL`, `--autocompact` and `CLAUDE_CODE_AUTO_COMPACT_WINDOW` still override for a session; use `availableModels` to restrict. A local admin can edit managed sources; server cache edits last only until the next fetch; managed settings bind Claude Code only.
