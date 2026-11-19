---
type: "Feature"
title: "Auto mode and model fallback"
description: "auto mode uses a classifier model; switching to an unsupported model drops the session to default mode."
resource: "https://code.claude.com/docs/en/agent-sdk/permissions"
tags: [permission-modes, auto, classifier, set-model]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.299"
surfaces: [sdk]
requires: "A model and provider that support auto mode"
identifiers:
  - "auto"
  - "set_model()"
  - "setModel()"
  - "applyFlagSettings()"
  - "SDKStatusMessage"
  - "Cannot set permission mode to auto: auto mode unavailable for this model"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-permissions"
    resource: "https://code.claude.com/docs/en/agent-sdk/permissions"
    title: "Configure permissions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A classifier model reviews actions such as shell commands and network requests before they run and allows or blocks each one it reviews. Models, providers and decision order are on the main permission-modes page.

# How to use it

If you switch an auto-mode session to an unsupported model with `set_model()`, `setModel()` or `applyFlagSettings()`, the session changes to `default` mode (requires Claude Code v2.1.299 or later):
- You see a `system` message, subtype `status`, `permissionMode` `"default"` (TypeScript type `SDKStatusMessage`). Calls needing approval then reach `canUseTool`.
- To return: switch to a supported model, then call `set_permission_mode("auto")` / `setPermissionMode("auto")`. Switching the model back alone leaves it in `default`.

# Limits and defaults

While the unsupported model is active, the call fails with `Cannot set permission mode to auto: auto mode unavailable for this model`.
