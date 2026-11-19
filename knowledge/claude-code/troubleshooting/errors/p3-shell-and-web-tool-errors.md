---
type: "Reference"
title: "Shell, temp-file and WebFetch tool errors"
description: "Tool-result errors for Bash/PowerShell: output swap refused, disk full, pkill self-match, approved command not run; and WebFetch localhost and domain safety check."
resource: "https://code.claude.com/docs/en/errors"
tags: [errors, bash, webfetch, disk, tmpdir]
kind: "tool"
maturity: "unlabelled"
since: "2.1.309"
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "CLAUDE_CODE_TMPDIR"
  - "pkill"
  - "skipWebFetchPreflight"
  - "WebFetch"
  - "xcode-select --install"
  - "MEMORY.md"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Errors from the shell tools, auto-memory writes, and WebFetch that matter when agents run unattended.

# How to use it

| Message | Cause | Fix |
|---|---|---|
| `task output swap refused (tasks dir moved or linked)` | Each Bash command's output goes to a file under the temp directory; its path was found redirected (symlink, extra hard link, moved dir). A running command is killed: `Command killed: its output file was replaced or could no longer be verified`. Versions before v2.1.260 sometimes showed it falsely | Upgrade to v2.1.260+; restart with `CLAUDE_CODE_TMPDIR` set to a fresh directory; remove a stray link or directory itself |
| `The command was not started: this computer's disk is full (ENOSPC) ...` / `Disk full:` / `Disk quota used up:` / `Nearly out of inodes:` | Cannot create the output file in Claude Code's temp dir, or a command ran with the volume nearly full | Free space, inodes or quota, or set `CLAUDE_CODE_TMPDIR` to another volume. Older wording (before v2.1.309 and v2.1.305) was raw `ENOSPC`/`EDQUOT` text |
| `pkill: refusing to run - this pattern matches the Claude CLI process` | Linux only: Claude Code tests the `pkill` pattern with `pgrep` and refuses when its own PID matches (before v2.1.214 it killed the session) | Narrow the pattern or use `pkill -P $$` |
| `This call was not run. Claude Code could not confirm that the shell is back in the directory where it was approved.` | Approved shell command after a restart; directory gone, outside the start directory, or untracked in a worktree session | Let Claude continue; approve again if asked |
| `git is not installed on this Mac` | `/usr/bin/git` is Apple's stand-in | `xcode-select --install` |
| `this write left the memory index at MEMORY.md at 214 lines, over its 200-line read limit` | Auto memory index over 200 lines or 25KB; only the first of either loads (before v2.1.210 silent). Frontmatter and block HTML comments are not counted (before v2.1.211 the raw file was measured). A milder reminder appears near the limit | Have Claude rewrite under 140 lines: one line per entry, details in topic files |
| `Command contains an invisible character` | PowerShell tool refuses U+FEFF or U+180E | Claude rewrites it; skill files per injected-command errors |
| `WebFetch cannot fetch localhost or other hostnames without a dot` | Hostnames with no dot refused before any request (before v2.1.268 `Invalid URL`) | Use Bash with `curl` |
| `Claude Code is unable to fetch from <host>` | Domain safety blocklist check at `api.anthropic.com` said no | None |
| `The safety check for domain <host> is rate-limited` / `Unable to verify if domain <host> is safe to fetch` | Check endpoint returned HTTP 429 (rate-limit wording changed in v2.1.286; before v2.1.285 shown as Unable to verify), or failed/timed out. Not cached | Skip the check with `skipWebFetchPreflight: true`, or allowlist `api.anthropic.com` |

# Limits and defaults

- MEMORY.md load limit: 200 lines or 25KB; rewrite target under 140 lines.

# Notes

None of these block the turn; they return as the tool's result.
