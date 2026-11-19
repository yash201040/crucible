---
type: "Feature"
title: "Block the action when a hook fails (onFailure)"
description: "onFailure: block makes a failed or timed-out command or http hook block the action; includes Windows without Git Bash behavior."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, onfailure, policy, windows]
kind: "frontmatter"
maturity: "unlabelled"
since: "2.1.295"
surfaces: [cli]
requires: "Claude Code v2.1.295 or later"
identifiers:
  - "onFailure"
  - "\"onFailure\": \"block\""
  - "\"onFailure\": \"continue\""
  - "CLAUDE_CODE_GIT_BASH_PATH"
  - "shell"
  - "failed; blocking because onFailure is \"block\""
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

By default, a failing or timing-out hook lets the action continue, so a policy hook with a wrong path lets everything through. `"onFailure": "block"` on a `command` or `http` hook makes failure do what exit code 2 does on that event (v2.1.295+). On `PermissionRequest` a failure denies the request. For Agent SDK callbacks see the SDK hooks page.

# How to use it

```json
{"type":"command","command":"node","args":["${CLAUDE_PROJECT_DIR}/.claude/hooks/check-command.js"],"onFailure":"block"}
```
With a missing script the error reads `PreToolUse:Bash hook error: [...]: failed; blocking because onFailure is "block"` (after a timeout, `timed out` replaces `failed`).

What counts as failure: command cannot start; exit code other than 0 or 2 (even with allow JSON; return decisions with exit 0); HTTP connection failure or non-2xx; timeout; invalid output (unparseable or schema-invalid JSON; for HTTP a 2xx body that is neither empty nor a JSON object). Plain-text command stdout is not a failure.

# Limits and defaults

No effect on `Stop`, `SubagentStop`, `TaskCompleted`, `TeammateIdle` (exit 2 there sends Claude back to work), nor on background command hooks (`async`/`asyncRewake`).

# Notes

Windows without Git Bash: a shell-form `PreToolUse`/`PermissionRequest` command hook with `onFailure` unset can block the call, with error text `blocking because Git Bash wasn't found, so only exit code 0 or 2 counts as this hook's verdict.` (before v2.1.309 the text mentioned `shell` not being `"powershell"`). Any exit other than 0 or 2 counts as failure there. Fixes: `"onFailure": "continue"` to let calls go ahead; `"onFailure": "block"` with scripts that exit 0 for warnings (put the warning in `systemMessage`); install Git for Windows or set `CLAUDE_CODE_GIT_BASH_PATH`; for one `.exe` use exec form (`command` + `args`) with `onFailure: "block"`; for a PowerShell guard set `"onFailure": "block"` and `"shell": "powershell"`. Error `PowerShell started no program`: a `command` that is only quoted strings is printed, not run; set `"shell": "powershell"` and prefix `&` before the quoted path to run files, or remove inner quotes for a plain `.exe`.
