---
type: "Reference"
title: "Startup and config file errors"
description: "Errors for a corrupt or empty ~/.claude.json, deleted working directory, refused temp directory, and /add-dir resolution failures."
resource: "https://code.claude.com/docs/en/errors"
tags: [errors, startup, config, tmpdir]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless]
requires: ""
identifiers:
  - "~/.claude.json"
  - "~/.claude/backups/"
  - "CLAUDE_CODE_TMPDIR"
  - "/add-dir"
  - "claude mcp add"
  - "CLAUDE_CODE_CONFIG_LOCK_WAIT_MS"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Fatal or near-fatal conditions found while `claude` starts, before a session runs. Non-interactive starts exit with code 1.

# How to use it

| Condition | Message / behaviour | Fix |
|---|---|---|
| Unparseable `~/.claude.json` | `Claude configuration file at ... is corrupted`; output names a backup in `~/.claude/backups/` (`.claude.json.corrupted.<ts>`, `.claude.json.backup.<ts>`) and a `cp -f` restore line; `claude -p` exits 1 | Run the `cp` line; else fix the JSON or copy another backup; with no file Claude starts with defaults |
| Blank config file, no backup holds anything | `Claude configuration file at ... was empty and no backup holds anything: starting with defaults.` (before v2.1.318 reported as corrupted) | Re-add `user`/`local` MCP servers via `claude mcp add`; sign in again |
| Working directory deleted or moved | `The current directory no longer exists ...`, exit 1 in interactive and non-interactive mode (before v2.1.239: raw `ENOENT uv_cwd` crash). Other causes name the code, e.g. `Can't read the current directory (EACCES)`. macOS `EPERM` in Desktop/Documents/Downloads/iCloud Drive means the terminal app is blocked | `cd` to an existing dir (`cd "$PWD"` if recreated); for EPERM quit terminal with Cmd+Q, enable it under System Settings > Privacy & Security > Files and Folders |
| Temp directory refused | macOS/Linux create `claude-<uid>` under the system temp dir or `CLAUDE_CODE_TMPDIR`; failures (ENOSPC, EDQUOT, not a directory/symlink, wrong owner uid, not readable) go to stderr, exit 1 | Free space, remove the entry itself, `chmod 0700`, or set `CLAUDE_CODE_TMPDIR` to a directory you control. Before v2.1.309 only raw OS error text was shown |
| `/add-dir` subdirectory not resolvable | `<dir> couldn't be resolved to a real location, so its skills, commands, and agents weren't loaded.` File access is unchanged; before v2.1.261 also shown wrongly under `/net/<host>` automounts | Check the path is a real directory inside the working directory |
| Config write lock / unreadable after MCP edit | `MCP server "x" was not saved to ~/.claude.json` or `may not have been saved`; add/remove commands waited 10 to 20 seconds on the file lock | Re-run with `CLAUDE_CODE_CONFIG_LOCK_WAIT_MS=60000`; make file writable; run `claude mcp get <name>` to verify. Before v2.1.283 these commands reported success even when nothing was written; before v2.1.318 the lock was not mentioned |

# Limits and defaults

- Config lock wait: about 10 to 20 seconds by default; `CLAUDE_CODE_CONFIG_LOCK_WAIT_MS` extends it (in ms).

# Notes

`claude import` read of an unparseable `~/.claude.json` is covered in [claude import and MCP management errors](./p3-mcp-management-cli-errors.md).
