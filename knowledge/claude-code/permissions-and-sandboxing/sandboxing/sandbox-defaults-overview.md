---
type: "Concept"
title: "Sandbox defaults and boundary"
description: "What the OS-enforced Bash sandbox lets shell commands read, write and reach by default, and which settings change each default."
resource: "https://code.claude.com/docs/en/sandboxing"
tags: [sandbox, bash, defaults, isolation]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "macOS, Linux or WSL2 (native Windows runs commands unsandboxed)"
identifiers:
  - "/sandbox"
  - "sandbox.enabled"
  - "sandbox.filesystem.allowWrite"
  - "sandbox.filesystem.denyWrite"
  - "sandbox.filesystem.denyRead"
  - "sandbox.network.allowedDomains"
  - "sandbox.network.deniedDomains"
  - "CLAUDE_CODE_SUBPROCESS_ENV_SCRUB"
  - "@anthropic-ai/sandbox-runtime"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sandboxing"
    resource: "https://code.claude.com/docs/en/sandboxing"
    title: "Configure the sandboxed Bash tool"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The Bash sandbox is an operating-system-enforced boundary around the shell commands Claude runs on your machine (Bash, PowerShell and Monitor commands and the processes they start). It is built on the open source `@anthropic-ai/sandbox-runtime` package. It is off by default. Sandboxed commands still pass through the regular permission flow unless auto-allow mode is chosen (see [sandbox modes](./sandbox-modes.md)).

It runs on macOS (Seatbelt), Linux and WSL2 (bubblewrap). On native Windows, Claude Code runs commands unsandboxed; run it inside WSL2 to get the sandbox.

# How to use it

Turn it on with `/sandbox` in a session, or set `sandbox.enabled` to `true` in a settings file such as `~/.claude/settings.json`.

| Access | Default | Change it with |
| - | - | - |
| Writes | Working directory, a per-user temp directory, directories added with `--add-dir`, `/add-dir` or `permissions.additionalDirectories`. Protected paths stay write-denied | `sandbox.filesystem.allowWrite`, `sandbox.filesystem.denyWrite` |
| Reads | Most of the machine, including `~/.ssh` and `~/.aws/credentials` | `sandbox.filesystem.denyRead`, `sandbox.credentials` |
| Network | No direct route out. Connections go through a local proxy that checks each host against allowed domains, which start empty | `sandbox.network.allowedDomains`, `sandbox.network.deniedDomains` |
| Environment variables | Inherited from Claude Code, secrets included | `sandbox.credentials`, `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB` |

# Limits and defaults

- The sandbox covers shell commands only; see [what runs outside it](./what-runs-outside-sandbox.md).
- If the platform is unsupported or the startup dependency check fails, Claude Code by default runs commands without sandboxing; `sandbox.failIfUnavailable: true` makes it exit instead.
