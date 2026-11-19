---
type: "Feature"
title: "Change model and settings mid-session"
description: "setModel, setPermissionMode, applyFlagSettings and updateSettings let a streaming-input session change configuration while running."
resource: "https://code.claude.com/docs/en/agent-sdk/configuration"
tags: [streaming-input, model-switch, permission-mode, caching]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: "Streaming input mode"
identifiers:
  - "setModel()"
  - "set_model()"
  - "setPermissionMode()"
  - "set_permission_mode()"
  - "applyFlagSettings()"
  - "updateSettings()"
  - "localSettings"
  - "userSettings"
  - "effortLevel"
  - "outputStyle"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-configuration"
    resource: "https://code.claude.com/docs/en/agent-sdk/configuration"
    title: "Configure your agent"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

With streaming input you can switch a running session's model and permission mode. TypeScript: methods on the object `query()` returns. Python: methods on `ClaudeSDKClient` (since `query()` returns a plain iterator).

# How to use it

| Method | What it does |
| - | - |
| `setModel()` / `set_model()` | Switches model; with no model it goes to Claude Code's default, not the `model` option. In auto mode, switching to an unsupported model changes the session to `default` mode |
| `setPermissionMode()` / `set_permission_mode()` | Switches permission mode |
| `applyFlagSettings()` (TypeScript) | Applies settings-file keys at runtime, e.g. `{ effortLevel: "high" }`; see the reference for which keys take effect mid-session |
| `updateSettings()` (TypeScript) | Writes one allowlisted key to a settings file: `"localSettings"` (e.g. `{ outputStyle: "Explanatory" }`, effective on the next request and persists); `"userSettings"` accepts only `effortLevel` (saved as default for the current model; the running session's effort does not change) |

# Notes

Each model has its own prompt cache, so after a mid-session switch the next request recomputes the full conversation uncached at the new model's rates.
