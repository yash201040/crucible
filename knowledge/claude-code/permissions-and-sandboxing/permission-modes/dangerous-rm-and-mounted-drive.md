---
type: "Reference"
title: "Dangerous rm and mounted drive prompts"
description: "The Dangerous rm operation not ruled out reason, the mounted-drive prompt, path shapes, and the env var that disables it."
resource: "https://code.claude.com/docs/en/permission-modes"
tags: [rm, mounted-drive, prompts, safety, env-var]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "macOS, Linux or WSL for the mounted drive prompt"
identifiers:
  - "CLAUDE_CODE_DISABLE_MOUNTED_DRIVE_RM_PROMPT"
  - "Dangerous rm operation not ruled out"
  - "Dangerous rm operation on mounted drive path"
  - "Dangerous rm operation on critical path"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permission-modes"
    resource: "https://code.claude.com/docs/en/permission-modes"
    title: "Choose a permission mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`Dangerous rm operation not ruled out — the shell may read this command differently than it was parsed`: the shell may read a command differently than Claude Code did, so a removal may hide in an unchecked part, even with no `rm`. In `auto` or `bypassPermissions` a denial reads `This command could not be checked for dangerous rm operations: the shell may read it differently than it was parsed.` It is handled like a critical-path removal in each mode (see [outcomes per mode](./critical-path-outcomes.md)); a `Bash`/`Bash(*)` allow rule, sandbox auto-allow or a `PreToolUse` `"allow"` cannot approve it.

The mounted drive prompt (reason `Dangerous rm operation on mounted drive path: <path>`) fires when a recursive `rm` (or any `rm` ending `/*`) targets a listed mount path. It is treated as a critical-path removal even with an `rm` allow rule.

# How to use it

Path shapes (each placeholder is one segment):

| Under | Shapes |
| :- | :- |
| `/Volumes` | `/Volumes/<drive>`, `/Volumes/<drive>/<name>` |
| `/System/Volumes` | `/System/Volumes`, `/<volume>`, `/<volume>/<name>` |
| `/media` | `/media/<user>`, `/<user>/<drive>`, `/<user>/<drive>/<name>` |
| `/run/media` | `/run/media`, plus `<user>`, `<user>/<drive>`, `<user>/<drive>/<name>` |
| `/mnt` | `/mnt/<name>`, and `/mnt/<letter>/<name>` for one-letter mounts such as WSL `/mnt/c` |

`/Volumes`, `/media`, `/mnt` themselves give the critical-path reason `Dangerous rm operation on critical path: <path>`. Relative targets count from the working directory.

Turn off: set `CLAUDE_CODE_DISABLE_MOUNTED_DRIVE_RM_PROMPT=1` in the launching environment (`export ...` then `claude`). A settings-file `env` block is ignored, and a running session does not pick it up.

# Limits and defaults

With the prompt off in Manual mode with `Bash(rm *)` allowed, `rm -rf build` in `/Volumes/USB` runs unprompted, but these still prompt: targets outside working directories (add the directory), targets with `*`, and critical paths (`/mnt` itself, the working directory itself).
