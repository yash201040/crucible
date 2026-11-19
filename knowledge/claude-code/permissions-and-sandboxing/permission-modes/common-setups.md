---
type: "Guide"
title: "Common permission setups"
description: "Goal-to-command table pairing review, plan, auto, CI allowlist and unattended container runs with flags and isolation."
resource: "https://code.claude.com/docs/en/permission-modes"
tags: [permissions, ci, unattended, headless, sandbox]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, cloud]
requires: ""
identifiers:
  - "--permission-mode"
  - "--dangerously-skip-permissions"
  - "--allowedTools"
  - "-p"
  - "sandbox.enabled"
  - "sandbox.autoAllowBashIfSandboxed"
  - "/sandbox"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permission-modes"
    resource: "https://code.claude.com/docs/en/permission-modes"
    title: "Choose a permission mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Modes decide whether Claude asks; the Bash sandbox and outer isolation decide what an action can reach once it runs. The page gives starting commands per goal.

# How to use it

| Goal | Start with | Isolation |
| :- | :- | :- |
| Review every action | `claude --permission-mode default` | None |
| Fewer prompts, no classifier | Manual plus Bash sandbox auto-allow: `claude --permission-mode default`, run `/sandbox`, pick auto-allow; or set `sandbox.enabled` and `sandbox.autoAllowBashIfSandboxed` to `true` | Built-in Bash sandbox (macOS, Linux, WSL2). Deny rules and command-naming ask rules like `Bash(git push *)` still apply |
| Explore first | `claude --permission-mode plan` | None; edits blocked until a plan is approved |
| Hands-off auto | `claude --permission-mode auto` | None required; sandbox or container adds defense in depth. Needs a supported model; an organization can turn it off |
| CI with exact allowlist | `claude -p "run the test suite" --permission-mode dontAsk --allowedTools "Bash(npm test)" "Read"` | Whatever the CI runner gives |
| Fully unattended in container | `claude -p "<prompt>" --dangerously-skip-permissions` | Required: container, VM, or sandbox runtime; on Linux and macOS run as non-root |

# Limits and defaults

- Cloud sessions ignore `dontAsk` and the bypass mode from settings files.
- In a `-p` bypass run, the few calls that would still prompt are denied instead.
- The sandbox and auto mode work independently and combine, with exceptions listed in the sandboxing docs.
