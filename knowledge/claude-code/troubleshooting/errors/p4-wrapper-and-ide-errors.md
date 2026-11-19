---
type: "Reference"
title: "Wrapper, VS Code and Agent SDK launch errors"
description: "Errors from programs that launch Claude Code: 60000ms initialize timeout, process exit codes, PATH not found in PowerShell, missing bundled binary, dropped connection."
resource: "https://code.claude.com/docs/en/errors"
tags: [errors, sdk, vscode, initialization, hooks]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.304"
surfaces: [ide, sdk]
requires: ""
identifiers:
  - "initializeTimeoutMs"
  - "startup()"
  - "SessionStart"
  - "Setup"
  - "claudeCode.claudeProcessWrapper"
  - "claude doctor"
  - "where.exe claude"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Errors reported by the VS Code extension or an Agent SDK application rather than by Claude Code itself.

# How to use it

| Error | Cause | Fix |
|---|---|---|
| `Subprocess initialization did not complete within 60000ms` (VS Code chat shows `Claude Code did not finish starting`) | The launched process did not answer the initialize request in time; slow plugins, MCP servers, hooks, disks or network. The text says if SessionStart or Setup hooks were reported running | Retry; View output logs / Show Logs; shorten slow hooks or lower a non-async hook `timeout`. In the SDK `startup()` call, set `initializeTimeoutMs` long enough or leave it unset |
| `Error: Claude Code process exited with code N` | Non-zero exit; the real error is in the process output. On Windows the native build can exit `4294967295` after a turn; the extension closes quietly at a turn boundary (before v2.1.273 it showed the error) | Check logs; catch it around the SDK message loop (see SDK troubleshooting `cli-process-exit`); run `claude` in the same project; `claude doctor` |
| `Could not locate the Claude CLI on PATH` | VS Code on Windows, PowerShell terminal; extension refuses to launch by name to avoid running a `claude` from the open folder | Set PATH as user or system variable (not just the PowerShell profile), restart VS Code; check `where.exe claude` |
| `The Claude Code program for this computer ... could not be found` | Bundled binary for the platform missing (before v2.1.290: `Unsupported platform: <platform>-<arch>`) | Install the platform-matching package, reinstall, or set `claudeCode.claudeProcessWrapper` to a separate `claude` binary |
| `The connection to Claude Code ended before this message completed` | Connection ended with no error before acknowledgment; message may be unprocessed | Resend; next message starts a fresh process that resumes |

# Limits and defaults

- Initialize timeout default: 60000 ms. Up to 10 minutes of reported SessionStart/Setup hook time does not count toward it, from VS Code extension v2.1.304 and TypeScript Agent SDK v0.3.304 (before, all hook time counted and the message said to check authentication and network connectivity).

# Notes

Applies to extension and SDK launches; hook timing is an unattended-run concern.
