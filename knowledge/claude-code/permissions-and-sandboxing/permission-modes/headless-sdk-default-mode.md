---
type: "Feature"
title: "Default mode in -p and SDK runs"
description: "Non-interactive and Agent SDK runs start Manual (default) from v2.1.302 and deny calls needing approval unless allowed."
resource: "https://code.claude.com/docs/en/permission-modes"
tags: [headless, sdk, permissions, unattended, auto]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.302"
surfaces: [headless, sdk]
requires: ""
identifiers:
  - "--allowedTools"
  - "--permission-prompt-tool"
  - "canUseTool"
  - "permissionMode"
  - "permission_mode"
  - "ClaudeAgentOptions"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permission-modes"
    resource: "https://code.claude.com/docs/en/permission-modes"
    title: "Choose a permission mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

From Claude Code v2.1.302, `claude -p` and Agent SDK runs with no permission mode set start in Manual (`default` in SDK options and settings). Calls that need approval are denied unless an allow rule, a hook, a `canUseTool` callback or `--permission-prompt-tool` approves them.

# How to use it

Two ways to get calls approved:

- Add allow rules: `claude -p ... --allowedTools "Bash(npm test)"`, or the SDK allowed-tools option.
- Start in auto mode so the classifier reviews calls:

```bash
claude -p "Run the test suite and fix any failures" --permission-mode auto
```
```typescript
const options = { permissionMode: "auto" };
```
```python
options = ClaudeAgentOptions(permission_mode="auto")
```

# Limits and defaults

- Before v2.1.302 these runs could start in auto mode if they did not fetch feature flags, for example on a third-party provider or with `DISABLE_TELEMETRY`.
- On Bedrock, Agent Platform, Foundry and Claude apps gateway, `-p`/SDK runs also start Manual unless `--permission-mode auto` or the SDK option is passed.
