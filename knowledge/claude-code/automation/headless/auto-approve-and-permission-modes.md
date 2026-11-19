---
type: "Feature"
title: "Permissions in -p runs"
description: "--allowedTools, --permission-mode, default Manual mode from v2.1.302, and how Bash allow entries behave in auto mode."
resource: "https://code.claude.com/docs/en/headless"
tags: [headless, permissions, allowedtools, permission-mode]
kind: "cli_flag"
maturity: "unlabelled"
since: "2.1.302"
surfaces: [headless, sdk]
requires: ""
identifiers:
  - "--allowedTools"
  - "--permission-mode"
  - "auto"
  - "dontAsk"
  - "acceptEdits"
  - "--permission-prompt-tool"
  - "PermissionRequest"
  - "permissions.allow"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "headless"
    resource: "https://code.claude.com/docs/en/headless"
    title: "Run Claude Code programmatically"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`--allowedTools` lets Claude use tools without prompting. `Read` and `Edit` allow reads and edits except reads from network paths. `Bash` does the same for shell commands, except in a run that starts in auto mode, where a bare `Bash` entry is dropped as a broad allow rule and auto mode evaluates each command. Example: `claude -p "Run the test suite and fix any failures" --allowedTools "Bash,Read,Edit"`.

# How to use it

- Unlisted tools run if they need no approval. In a Manual mode `-p` run, a call needing approval is denied unless a `PermissionRequest` hook or `--permission-prompt-tool` approves it. From v2.1.302, `claude -p` runs start in Manual mode when nothing sets a permission mode.
- `--permission-mode` sets a baseline:

| Mode | Effect |
| --- | --- |
| `auto` | A classifier reviews most actions |
| `dontAsk` | Denies every call that would prompt; good for locked-down CI. A mod you installed can still approve some calls. Calls needing no approval in Manual mode (reads in working directories, read-only command set) and those covered by `--allowedTools` or `permissions.allow` still run. Denied even with an allow rule: `AskUserQuestion`, connector tools your org set to `ask`, MCP tools marked `requiresUserInteraction`, network-path reads |
| `acceptEdits` | Writes files without prompting and auto-approves filesystem commands like `mkdir`, `touch`, `mv`, `cp`; other shell commands and network requests still need `--allowedTools` or `permissions.allow` |

- Rule syntax: `--allowedTools "Bash(git diff *),Bash(git log *),Bash(git status *),Bash(git commit *)"`. The space before `*` matters: `Bash(git diff*)` would also match `git diff-index`.

# Notes

See [unattended runs](./unattended-permission-prompts.md) for `--permission-prompts none`.
