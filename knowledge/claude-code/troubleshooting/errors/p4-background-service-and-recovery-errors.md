---
type: "Reference"
title: "Background service start and session recovery errors"
description: "Errors starting or reattaching background sessions: dead host process, unresponsive session, EUNKNOWN/EACCES, service exit, trust, gateway, wrapper, /loop wakeup."
resource: "https://code.claude.com/docs/en/errors"
tags: [errors, background-sessions, daemon, windows, recovery]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.246"
surfaces: [cli]
requires: ""
identifiers:
  - "claude daemon status"
  - "claude daemon run"
  - "claude daemon stop --any"
  - "claude respawn"
  - "claude attach"
  - "claude stop"
  - "claude --bg"
  - "/background"
  - "~/.claude/daemon.lock"
  - "CLAUDE_CODE_PROCESS_WRAPPER"
  - "ANTHROPIC_BASE_URL"
  - "--agent"
  - "agent"
  - "/loop"
  - "EUNKNOWN"
  - "EACCES"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Failures of the background service (the supervisor that hosts background sessions) and of reattaching or restarting a session. The conversation is saved in every case.

# How to use it

| Message | Cause | Fix |
|---|---|---|
| `terminal host process died - press Enter to restart` | A session's terminal host process died while the service held its connection. Linux and WSL check every few seconds. Shell-command rows are never rerun | Enter on the row, or `claude attach <id>` (restarts a failed row; else prints the cause). Before v2.1.247 the open hung on `opening...` |
| `Session isn't responding` | Open accepted but no output for about 10 seconds | Press Enter again on the row (stops and restarts), or `claude stop <id>` then `claude attach <id>`; shell-command rows: Ctrl+X or `claude stop <id>` |
| `Session <id> was stopped while the respawn was in flight` | Another process stopped it during restart (before v2.1.246 could hit a just-dispatched session) | Open the row again or `claude respawn <id>` |
| `This session was running agent '<name>', which is no longer available` | Resumed session used `--agent` or the `agent` setting; searched session's original directory (if trusted) then the resume directory; resumes with default tools and prompt, warning repeats each resume (also stderr in `-p`; not shown for `--input-format stream-json`; built-in `claude` agent does not warn). Before v2.1.216 silent and only the resume directory | Re-create `.claude/agents/<name>.md` or `~/.claude/agents/<name>.md`, or resume with `--agent <name>` |
| `This session restarted ... after its next /loop wakeup was due` | A self-paced `/loop` in a background session: process ended while waiting and the wakeup came due before restart; missed wakeup does not fire late (notice since v2.1.295) | Reply to the session to continue the loop |
| `No LLM gateway: a gateway set in your shell isn't passed to a session opened from another folder` | Session dispatched/woken/restarted from another folder while `ANTHROPIC_BASE_URL` was a shell export (before v2.1.302 showed a sign-in error) | `claude respawn <id>` from the named folder in a shell with the gateway set (supervisor must also have started from such a shell), or put `ANTHROPIC_BASE_URL` and key/token in a settings file `env` block (`~/.claude/settings.json` or `.claude/settings.local.json`) |
| `CLAUDE_CODE_PROCESS_WRAPPER: launcher ... is not an executable regular file` | Launcher value unusable; process refused rather than run unwrapped. A launcher that daemonizes fails the session: `must exec, not daemonize` | Absolute path to an executable ending in `exec "$@"`; check `/status` Self-exec or `claude daemon status`; `claude daemon stop --any` after fixing |
| `Couldn't reach the background service (spawn background service: EUNKNOWN ...)` | Windows policy (Group Policy, AppLocker) blocking a program. Service starts via PowerShell 7 if present, else 5.1, else directly (service then dies with the terminal). Before v2.1.212 only PowerShell 5.1 was used (`Couldn't start the session`) | Upgrade to v2.1.212+; workaround `claude daemon run` in a separate terminal; ask the admin |
| `Couldn't start the background service - spawn background service: EACCES` | Binary being replaced (npm install or auto-update). Waits up to ten seconds and up to two minutes while an npm install is visibly running (before v2.1.257 always ten; before v2.1.246 failed at once); then `Claude Code is being updated by npm on this machine` | Retry later; check binary permissions or reinstall |
| `Couldn't reach the background service (background service exited before it became reachable (exit code N): ...)` | Service exited early (before v2.1.246: after a 45-second wait, `did not become reachable within 45s`). `Error: claude native binary not installed.` = npm placeholder during install. On Windows exit code 1 on every start with `nothing on stderr`: stale `daemon.lock` | Retry; delete `~/.claude/daemon.lock` for the Windows case (before v2.1.257 it blocked every start) |
| `Couldn't start a background session (working directory no longer exists or is not accessible: <dir>)` | Directory removed during start (before v2.1.257 showed as failed row; before v2.1.281 also when already gone, now `could not be resolved on disk`) | Recreate or dispatch elsewhere |
| `This forked session could not be started. Fork the conversation again to retry.` | Forking a Remote Control session from claude.ai failed to start its background session | Fork again once idle |
| `Workspace not trusted. Run claude in <path> once and accept the trust prompt, then retry.` | Dispatch or restart where the trust dialog cannot appear (script, different directory). Variants: `The home directory is trusted one session at a time`; `<path> could not be resolved on disk`. Before v2.1.286 Windows could wrongly show it for path-case mismatches | Run `claude` in the directory and accept |

# Limits and defaults

- Unresponsive-session detection: about 10 seconds with no output.
- npm update retry wait: up to 10 seconds, or 2 minutes while an npm install is running.

# Notes

`claude daemon status` reports whether a service is running.
