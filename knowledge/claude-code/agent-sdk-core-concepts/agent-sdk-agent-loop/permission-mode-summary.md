---
type: "Reference"
title: "Permission modes in the loop"
description: "One-line behavior and use case for each permission mode, plus bypassPermissions TypeScript requirement."
resource: "https://code.claude.com/docs/en/agent-sdk/agent-loop"
tags: [permissions, modes, bypasspermissions, headless]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "permission_mode"
  - "permissionMode"
  - "default"
  - "acceptEdits"
  - "plan"
  - "dontAsk"
  - "auto"
  - "bypassPermissions"
  - "allowDangerouslySkipPermissions"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-agent-loop"
    resource: "https://code.claude.com/docs/en/agent-sdk/agent-loop"
    title: "How the agent loop works"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

| Mode | Behavior | Use case |
| :- | :- | :- |
| `"default"` | Calls needing approval and not covered by allow rules trigger `canUseTool`; no callback means deny | Interactive apps |
| `"acceptEdits"` | Auto-approves edits and `mkdir`, `touch`, `mv`, `cp` etc. in working directories | Prototyping |
| `"plan"` | Plan only; file-tool edits go to `canUseTool` | Review, large changes |
| `"dontAsk"` | Never prompts; anything that would prompt is denied | Headless agents with nobody to approve |
| `"auto"` | Model classifier reviews actions | Autonomous agents with guardrails |
| `"bypassPermissions"` | Runs calls without asking, including unlisted tools | CI, containers, isolated environments |

# Limits and defaults

`bypassPermissions` in the TypeScript SDK also requires `allowDangerouslySkipPermissions: true` in `options`, and cannot be used when running as root on Unix. Full details: the SDK permissions page.
