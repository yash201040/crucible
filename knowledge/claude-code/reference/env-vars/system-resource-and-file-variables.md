---
type: "Reference"
title: "Tool memory cap, temp directory and file system variables"
description: "Variables for the Linux tool memory cap, low disk and memory warnings, temp directory, checkpointing, Perforce mode, automount roots and config lock wait."
resource: "https://code.claude.com/docs/en/env-vars"
tags: [memory, disk, tmpdir, checkpointing]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless]
requires: ""
identifiers:
  - "CLAUDE_CODE_TOOL_MEMORY_LIMIT"
  - "CLAUDE_CODE_TOOL_MEMORY_CGROUP_EXCLUDE"
  - "CLAUDE_CODE_WARN_DISK_FREE_GIB"
  - "CLAUDE_CODE_WARN_MEMORY_FREE_GIB"
  - "CLAUDE_CODE_TMPDIR"
  - "CLAUDE_CODE_DISABLE_FILE_CHECKPOINTING"
  - "CLAUDE_CODE_PERFORCE_MODE"
  - "CLAUDE_CODE_AUTOMOUNT_ROOTS"
  - "CLAUDE_CODE_CONFIG_LOCK_WAIT_MS"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "env-vars"
    resource: "https://code.claude.com/docs/en/env-vars"
    title: "Environment variables"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Host resource guards and file handling, useful when many agents share a machine.

# How to use it

| Variable | What it does |
| :- | :- |
| `CLAUDE_CODE_TOOL_MEMORY_LIMIT` | Linux and WSL: size such as `4G` capping memory of Bash and PowerShell tool commands (and Monitor tool commands on v2.1.246+). Plain digits alone (bytes) or with `K`, `M`, `G`, `T`; `0` or `off` disables. After the first process sets it on or off, a changed value applies at next launch. Requires v2.1.233+. |
| `CLAUDE_CODE_TOOL_MEMORY_CGROUP_EXCLUDE` | Linux/WSL: comma-separated process kinds excluded from the cap, such as `mcp` or `lsp`; `none` caps every kind; `all-new` caps only Bash, PowerShell and Monitor commands. Those three always stay capped. Requires v2.1.246+. |
| `CLAUDE_CODE_WARN_DISK_FREE_GIB` | Whole GiB (for example `10`): warn Claude via system reminder when free space on the working directory's filesystem falls below it. Off when unset, `0` or not plain digits. Set in the launching environment; a settings `env` copy is ignored. Requires v2.1.304+. |
| `CLAUDE_CODE_WARN_MEMORY_FREE_GIB` | Linux/WSL: same for available memory (for example `4`). Same off conditions and launching-environment rule. Requires v2.1.304+. |
| `CLAUDE_CODE_TMPDIR` | Temp directory for internal files; Claude Code appends `/claude-{uid}/` on Unix or `/claude/` on Windows. Default `/tmp` on macOS, `os.tmpdir()` on Linux and Windows. Sandboxed Bash gets a short fallback `$TMPDIR` when the override is long; unsandboxed commands inherit the shell's. Ignored in project and local settings. |
| `CLAUDE_CODE_DISABLE_FILE_CHECKPOINTING` | `1` disables file checkpointing, so `/rewind` cannot restore code changes. Overrides `fileCheckpointingEnabled`. |
| `CLAUDE_CODE_PERFORCE_MODE` | `1` makes Edit, Write and NotebookEdit fail with a `p4 edit <file>` hint when the target lacks the owner-write bit. |
| `CLAUDE_CODE_AUTOMOUNT_ROOTS` | Automount roots to skip when looking in folders above the working directory for `CLAUDE.md`, skills, `.mcp.json`. Separate with `:` (Unix) or `;` (Windows); absolute paths without symlinks. Requires v2.1.323+. |
| `CLAUDE_CODE_CONFIG_LOCK_WAIT_MS` | Ms that `claude mcp add` or remove for `user` or `local` scope keeps trying for the `~/.claude.json` lock (unset: about 10 to 20 seconds; a shorter value changes nothing). Requires v2.1.318+. |
