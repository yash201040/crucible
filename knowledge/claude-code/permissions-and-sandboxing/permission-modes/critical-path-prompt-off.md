---
type: "Feature"
title: "Turn off the rm prompt in bypass mode"
description: "CLAUDE_CODE_EVEN_MORE_DANGEROUSLY_SKIP_PERMISSIONS lets critical-path rm run unprompted in bypassPermissions, with startup notices and causes it fails."
resource: "https://code.claude.com/docs/en/permission-modes"
tags: [bypass, rm, env-var, unattended, safety]
kind: "env_var"
maturity: "unlabelled"
since: "2.1.311"
surfaces: [cli, headless, sdk]
requires: "bypassPermissions mode; launch environment only"
identifiers:
  - "CLAUDE_CODE_EVEN_MORE_DANGEROUSLY_SKIP_PERMISSIONS"
  - "is set, so dangerous rm commands can run without a prompt"
  - "has no effect in this session"
  - "has no effect while the Windows registry cannot be read for managed settings"
  - "--tools"
  - "stderr"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permission-modes"
    resource: "https://code.claude.com/docs/en/permission-modes"
    title: "Choose a permission mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Setting `CLAUDE_CODE_EVEN_MORE_DANGEROUSLY_SKIP_PERMISSIONS=1` (v2.1.311+) lets Bash `rm`/`rmdir` targeting critical paths run with no prompt in `bypassPermissions`. Read from the launch environment only; ignored in a settings `env` block. It applies only in `bypassPermissions` itself (not plan mode) and only to what the critical-path check flags in the Bash and Monitor tools, including commands Claude Code cannot fully parse. The docs warn `rm -rf ~` can then run without asking; use only in isolated environments.

# How to use it

```bash
export CLAUDE_CODE_EVEN_MORE_DANGEROUSLY_SKIP_PERMISSIONS=1
claude --permission-mode bypassPermissions
```
PowerShell: `$env:CLAUDE_CODE_EVEN_MORE_DANGEROUSLY_SKIP_PERMISSIONS = "1"`; CMD: `set CLAUDE_CODE_EVEN_MORE_DANGEROUSLY_SKIP_PERMISSIONS=1`.

Startup line (stderr in `-p`; Agent SDK needs the `stderr` option): `is set, so dangerous rm commands can run without a prompt`; `has no effect in this session`; or `has no effect while the Windows registry cannot be read for managed settings` (takes effect with no restart if a later registry read succeeds). A missing line does not mean the prompt is on (an SDK app with no `stderr` option sees none).

# Limits and defaults

It has no effect when:
- Something else handles prompts: `--permission-prompt-tool`, an SDK `canUseTool` callback without `--permission-prompts none`, a `PermissionRequest` hook (any matcher), or a mod handling that event.
- The VS Code chat panel or Desktop app runs the session (use a terminal).
- A deny or ask rule targets Bash, Edit or Read, at launch or once read in session, even if later removed (use `--tools` instead of a deny rule).
- `permissions.blockReadsOutsideWorkingDirectories` is on.
- `claude` runs inside another session (from the Bash tool or a hook); not a security boundary.
- A `PreToolUse` hook answers `ask` for a removal.
- Claude Code starts the session: background sessions, agent-team teammates in split panes, Remote Control server-created sessions start without the variable.
- Managed settings cannot be read, or on Windows/WSL the registry query fails (non-English Windows, WSL with interop off, container on a WSL2 kernel).
