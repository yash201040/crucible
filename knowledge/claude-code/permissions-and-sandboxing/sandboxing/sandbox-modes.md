---
type: "Feature"
title: "Sandbox modes: auto-allow and regular"
description: "Two sandbox modes that differ only in whether sandboxed Bash commands are auto-approved, with the exceptions that still prompt."
resource: "https://code.claude.com/docs/en/sandboxing"
tags: [sandbox, auto-allow, permissions, modes]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "sandbox.autoAllowBashIfSandboxed"
  - "/sandbox"
  - "Bash(make *)"
  - "Bash(eval \"ls\")"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sandboxing"
    resource: "https://code.claude.com/docs/en/sandboxing"
    title: "Configure the sandboxed Bash tool"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Both modes enforce the same filesystem and network limits. They differ in approval.

- **Auto-allow**: a command that runs inside the sandbox is approved with no prompt. Commands outside the sandbox (matching `excludedCommands`, or an unsandboxed retry) use the regular permission flow. Works independently of the permission mode, so sandboxed Bash commands that modify files run without prompting even in Manual mode. Exceptions: plan mode (auto-allow does not widen approvals), an auto mode command carrying per-command allowed domains, and server-side classifier review of sandboxed commands in auto mode.
- **Regular permissions**: every Bash command goes through the regular permission flow even when sandboxed.

# How to use it

Pick on the Mode tab of `/sandbox`, or set `sandbox.autoAllowBashIfSandboxed` to `true` in settings (with `sandbox.enabled`).

Still applies in auto-allow:
- A command matching a `Bash` deny rule is blocked.
- `rm`/`rmdir` on a critical path goes through the regular flow.
- Content-scoped ask rules such as `Bash(git push *)` still prompt.
- A bare `Bash` or `Bash(*)` ask rule is skipped for sandboxed commands, but in plan mode it prompts even for sandboxed read-only commands.
- Monitor tool commands are not auto-approved (they still run sandboxed); add an allow rule such as `Bash(npm run *)`.
- Commands like `FOO=bar npm test`, `make CC=clang` and `eval "ls"` go through the regular flow (still sandboxed). Allow rules that stop the prompt: `Bash(make *)`, `Bash(FOO=bar npm *)` (include the assignment), `Bash(eval "ls")` (a wildcard `Bash(eval *)` does not work).

An allow rule that matches a command also approves its unsandboxed retry.

# Notes

The sandbox auto-allow mode is separate from permission-mode auto mode (classifier-based); they can be combined. See [permissions relationship](./sandbox-and-permissions.md).
