---
type: "Guide"
title: "Desktop troubleshooting and SSH error codes"
description: "Fixes for 403 errors, blank screens, layout and version checks, host key failures and SSH connection error codes."
resource: "https://code.claude.com/docs/en/desktop"
tags: [desktop, troubleshooting, ssh, errors, version]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [desktop]
requires: ""
identifiers:
  - "SFTP_UNAVAILABLE"
  - "SFTP_NOT_STARTED"
  - "SESSION_LIMIT"
  - "ENOSPC"
  - "EDQUOT"
  - "CLI_UNRESPONSIVE"
  - "SERVER_NOT_RUNNABLE"
  - "SETUP_DIR_NOEXEC"
  - "DOWNLOAD_BUSY"
  - "ssh.log"
  - "git lfs install"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "desktop"
    resource: "https://code.claude.com/docs/en/desktop"
    title: "Desktop application"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Common Desktop problems and fixes. Earlier layout (environment above the prompt box) means Desktop older than v2.37337.0 (third-party: v3.1623.0 for local, v4.29.0 for organization infrastructure); update to get the session details panel and saved environments.

# How to use it

- **403 / auth errors**: sign out and in; confirm paid plan; if the CLI works, fully quit Desktop; check proxy.
- **Blank screen**: restart, update (apt on Linux), allow CDN hosts, check Windows Event Viewer.
- **Failed to load session**: missing folder, Git LFS not installed, or permissions.
- **Tools not found**: verify PATH in shell profile and restart.
- **Git**: worktree sessions need Git; Git LFS needs `git lfs install`.
- **Version**: macOS Claude > About Claude; Windows Help > About Claude; logs at Help > Troubleshooting. Report version, OS, exact error, logs.
- **Host key failures** (`SSH host key verification failed`, `Host key changed or not trusted`): compare fingerprints with the machine's own (`ssh-keygen -lf /etc/ssh/ssh_host_<type>_key.pub`) before **Trust new key**; Windows needs Microsoft's OpenSSH client.

| Code | Meaning / fix |
| - | - |
| `[SFTP_UNAVAILABLE]` | enable SFTP in `sshd_config` |
| `[SFTP_NOT_STARTED]` | test with `sftp` from your computer |
| `[SESSION_LIMIT]` | Desktop v3.1623.0+ or raise `MaxSessions` |
| `[ENOSPC]` / `[EDQUOT]` | free disk space or quota (remote, or locally for deploy prep) |
| `[CLI_UNRESPONSIVE]` | wait and retry; run the named command on the remote |
| `[SERVER_NOT_RUNNABLE]` / `[SETUP_DIR_NOEXEC]` | allow execution from `~/.claude/remote/` |
| `[DOWNLOAD_BUSY]` | retry; proxy may limit downloads |

# Notes

Runtime API errors (`API Error: 500`, `529 Overloaded`, `429`, `Prompt is too long`) are covered on the Error reference page. Branch missing locally for a cloud session: copy branch name then `git fetch origin <branch>`.
