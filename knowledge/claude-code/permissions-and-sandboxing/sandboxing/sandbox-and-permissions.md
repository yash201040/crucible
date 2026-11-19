---
type: "Concept"
title: "How sandboxing relates to permissions"
description: "Sandboxing (OS-enforced) versus permission rules and modes (checked before a tool runs), which settings and rules feed the merged sandbox config."
resource: "https://code.claude.com/docs/en/sandboxing"
tags: [sandbox, permissions, auto-mode, rules]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "--dangerously-skip-permissions"
  - "sandbox.filesystem.allowWrite"
  - "sandbox.filesystem.denyRead"
  - "sandbox.filesystem.allowRead"
  - "sandbox.filesystem.disabled"
  - "WebFetch(domain:...)"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sandboxing"
    resource: "https://code.claude.com/docs/en/sandboxing"
    title: "Configure the sandboxed Bash tool"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Permission rules control which tools Claude can use and are evaluated before any tool runs, for every tool (a deny or ask rule cannot block `EndConversation` while any other tool remains). Sandboxing is OS-level enforcement on Bash, PowerShell and Monitor commands and children; it holds regardless of what the model chose. Permission decisions are based on the command string and, in auto mode, a classifier.

# How to use it

| Setting or rule | Effect |
| - | - |
| `sandbox.filesystem.allowWrite` | Extra write paths |
| `sandbox.filesystem.denyWrite` / `denyRead` | Block access to paths |
| `sandbox.filesystem.allowRead` | Re-allow reads inside a `denyRead` region |
| `sandbox.filesystem.disabled` | Turn the filesystem layer off |
| `Edit` allow rules | Grant write access like `allowWrite` |
| `Read` and `Edit` deny rules | Block files or directories |
| `WebFetch(domain:...)` allow/deny | Control domain access |
| Sandbox `allowedDomains` / `deniedDomains` | Bash domain access; `deniedDomains` beats a broader wildcard allow |

Paths and domains from both are merged into the final sandbox config.

`/sandbox` is not a permission mode. Compare: `/sandbox` controls what a Bash command can access once running (the boundary replaces the prompt in auto-allow); auto mode controls whether each tool call runs (a classifier replaces the prompt); `--dangerously-skip-permissions` controls whether each call runs (nothing replaces the prompt; protected-path checks are skipped, but actions no mode auto-approves still apply). Auto-allow and auto mode work independently and can be combined.

# Notes

The claude-code repository's examples/settings directory has starter sandbox settings.
