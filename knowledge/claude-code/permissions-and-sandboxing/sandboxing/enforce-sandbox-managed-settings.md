---
type: "Guide"
title: "Enforce the sandbox with managed settings"
description: "Managed-settings configuration that requires the sandbox, refuses to start without it and blocks unsandboxed retries, plus Windows fleet handling."
resource: "https://code.claude.com/docs/en/sandboxing"
tags: [sandbox, managed-settings, enterprise, enforcement]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "managed settings (MDM file or server-managed settings on claude.ai)"
identifiers:
  - "sandbox.enabled"
  - "sandbox.failIfUnavailable"
  - "sandbox.allowUnsandboxedCommands"
  - "sandbox.excludedCommands"
  - "sandbox.credentials"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sandboxing"
    resource: "https://code.claude.com/docs/en/sandboxing"
    title: "Configure the sandboxed Bash tool"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Deliver `sandbox` keys through managed settings (an MDM-managed file, or server-managed settings) to require sandboxing for every developer.

# How to use it

```
{ "sandbox": { "enabled": true, "failIfUnavailable": true, "allowUnsandboxedCommands": false } }
```

- `failIfUnavailable`: Claude Code refuses to start when the platform is unsupported or a dependency is missing, instead of falling back to unsandboxed execution.
- `allowUnsandboxedCommands: false`: the `dangerouslyDisableSandbox` escape hatch is ignored.

Add alongside: `excludedCommands` for approved tools that need no isolation (a repository cannot supply them under this configuration), and `sandbox.credentials` entries for `~/.aws`, `~/.ssh` and secret env vars, since the default read policy allows them.

# Limits and defaults

- Developers can still type a command at the `!` prompt and run it outside the sandbox (see [strict mode](./unsandboxed-retry-and-strict-mode.md)).
- Native Windows has no sandbox, so `failIfUnavailable` makes Claude Code exit there. Options: deliver the config only to macOS and Linux machines via MDM or a managed file (server-managed settings follow the member, not the device), or move Windows users into WSL2 or a container.
