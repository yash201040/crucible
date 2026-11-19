---
type: "Reference"
title: "Exceptions to managed settings precedence"
description: "Restrictive values honored from lower scopes even over managed settings (disableClaudeAiConnectors, isolatePeerMachines, block reads/writes outside and more)."
resource: "https://code.claude.com/docs/en/settings"
tags: [settings, managed-settings, security, precedence]
kind: "setting"
maturity: "unlabelled"
since: "2.1.242"
surfaces: [cli]
requires: ""
identifiers:
  - "disableClaudeAiConnectors"
  - "enableArtifact"
  - "disableArtifact"
  - "isolatePeerMachines"
  - "permissions.blockReadsOutsideWorkingDirectories"
  - "permissions.blockWritesOutsideWorkingDirectories"
  - "permissions.denyInsteadOfPrompting"
  - "autoMode.classifyAllShell"
  - "remoteControlAtStartup"
  - "crossSessionInbound"
  - "useAutoModeDuringPlan"
  - "syncClaudeAiSkills"
  - "syncClaudeAiPlugins"
  - "maxEffortLevel"
  - "CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings"
    resource: "https://code.claude.com/docs/en/settings"
    title: "Settings files and precedence"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

For keys whose values restrict a session, Claude Code honors the restrictive value from a scope that otherwise could not override managed settings.

# How to use it

| Key | Value honored | Notes |
| :- | :- | :- |
| `disableClaudeAiConnectors` | `true` from any scope | even if managed sets `false` |
| `enableArtifact` / `disableArtifact` | `enableArtifact: false` or `disableArtifact: true` from any scope | even if managed sets `true`; nothing turns the Artifact tool back on; v2.1.242 or later |
| `isolatePeerMachines` | `true` from any scope | even if managed sets `false` |
| `permissions.blockReadsOutsideWorkingDirectories` | `true` from any scope | v2.1.257 or later |
| `permissions.blockWritesOutsideWorkingDirectories` | `true` from any scope | v2.1.314 or later |
| `permissions.denyInsteadOfPrompting` | `true` from `~/.claude/settings.json` or `--settings` | v2.1.319 or later |
| `autoMode.classifyAllShell` | `true` from `~/.claude/settings.json` or `--settings` | even if managed sets `false` |
| `remoteControlAtStartup` | `false` from `.claude/settings.json` or `.claude/settings.local.json` | a project or local `true` is ignored |
| `crossSessionInbound` | a stricter value from project or local, on the ladder `accept` < `hold` < `refuse` | beats managed, `--settings`, user; non-stricter ignored |
| `useAutoModeDuringPlan` | `false` from any managed source, `--settings`, user, or local | `false` in `.claude/settings.json` ignored |
| `syncClaudeAiSkills` | `false` from any managed source, `--settings`, user, or local | `false` in `.claude/settings.json` ignored |
| `syncClaudeAiPlugins` | `false` from any managed source, `--settings`, user, or local | `false` in `.claude/settings.json` ignored |
| `maxEffortLevel` | a lower cap from any scope incl. `--settings` | lowest cap applies; v2.1.267 or later |

# Notes

An app embedding Claude Code that sets `CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST` takes its own model configuration over `model`, `fallbackModel`, `modelPicker` and `modelOverrides` from every managed source and over model-selection variables in a managed `env` block (`ANTHROPIC_MODEL`, the `ANTHROPIC_DEFAULT_*_MODEL` family). A managed `availableModels` allowlist stays in force unless the app supplies its own.
