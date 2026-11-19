---
type: "Reference"
title: "Permission, removal-prompt and auto mode variables"
description: "Variables that tune critical-path removal prompts, bypassPermissions safeguards, the auto mode classifier, restricted mode and ultrareview trust."
resource: "https://code.claude.com/docs/en/env-vars"
tags: [permissions, auto-mode, safety, bypass-permissions]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "CLAUDE_CODE_DISABLE_DANGEROUS_RM_TIMEOUT"
  - "CLAUDE_CODE_DISABLE_INLINE_SHELL_RM_PROMPT"
  - "CLAUDE_CODE_STRICT_INLINE_SHELL_RM_PROMPT"
  - "CLAUDE_CODE_DISABLE_SUBSTITUTION_RM_PROMPT"
  - "CLAUDE_CODE_DISABLE_MOUNTED_DRIVE_RM_PROMPT"
  - "CLAUDE_CODE_DISABLE_POWERSHELL_CMD_RM_DENY"
  - "CLAUDE_CODE_EVEN_MORE_DANGEROUSLY_SKIP_PERMISSIONS"
  - "CLAUDE_CODE_AUTO_MODE_MODEL"
  - "CLAUDE_CODE_AUTO_MODE_SERVER"
  - "CLAUDE_CODE_ENABLE_AUTO_MODE"
  - "CLAUDE_CODE_RESTRICTED"
  - "CLAUDE_CODE_DISABLE_ULTRAREVIEW_TRUST_CHECK"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "env-vars"
    resource: "https://code.claude.com/docs/en/env-vars"
    title: "Environment variables"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Permission-mode safety valves and the auto mode classifier. Most "disable" variables here must be set in the environment that launches Claude Code, because a settings `env` copy is ignored.

# How to use it

| Variable | What it does |
| :- | :- |
| `CLAUDE_CODE_DISABLE_DANGEROUS_RM_TIMEOUT` | `1` turns off the `auto` and `bypassPermissions` time limit and denials on critical-path removals (they go to the classifier in `auto`; untimed prompt in `bypassPermissions` where one can show). Launch environment only. Requires v2.1.281+. |
| `CLAUDE_CODE_DISABLE_INLINE_SHELL_RM_PROMPT` | `1` stops reading `-c` scripts (such as `bash -c 'rm -rf ~'`) for critical-path removals; variable and positional targets are still checked. Launch environment only. Requires v2.1.288+. |
| `CLAUDE_CODE_STRICT_INLINE_SHELL_RM_PROMPT` | `1` flags more `-c` scripts Claude Code cannot check, including ones naming neither `rm` nor `rmdir`. Launch environment only; no effect when the disable variable is `1`. Requires v2.1.299+. |
| `CLAUDE_CODE_DISABLE_SUBSTITUTION_RM_PROMPT` | `1` turns off the critical-path check for recursive `rm` whose target is entirely command-substitution output (such as `rm -rf "$(pwd)"`). Launch environment only. Requires v2.1.281+. |
| `CLAUDE_CODE_DISABLE_MOUNTED_DRIVE_RM_PROMPT` | `1` turns off the mounted drive prompt for paths such as `/Volumes/USB`. Launch environment only. Requires v2.1.304+. |
| `CLAUDE_CODE_DISABLE_POWERSHELL_CMD_RM_DENY` | `1` turns off the PowerShell tool check denying `cmd` built-ins `rd`, `rmdir`, `del`, `erase` on a system path (drive root, home). Ignored in a settings `env` block. Requires v2.1.283+. |
| `CLAUDE_CODE_EVEN_MORE_DANGEROUSLY_SKIP_PERMISSIONS` | `1` runs dangerous `rm` commands with no prompt in `bypassPermissions` mode, removing a safety prompt for destructive deletes. Launch environment only. Requires v2.1.311+. |
| `CLAUDE_CODE_AUTO_MODE_MODEL` | Model for auto mode classifier requests, a full ID such as `claude-sonnet-4-6`. Requires v2.1.302+. |
| `CLAUDE_CODE_AUTO_MODE_SERVER` | Whether the server reviews auto mode actions; `0` uses Claude Code's own classifier requests. On a direct Anthropic API connection needs v2.1.281+. Requires v2.1.271+. |
| `CLAUDE_CODE_ENABLE_AUTO_MODE` | Accepted for compatibility, no effect. Auto mode is available by default on every provider and signed-in Claude apps gateway sessions. In v2.1.158 through v2.1.206, `1` was required on those providers. |
| `CLAUDE_CODE_RESTRICTED` | `1` starts restricted mode, same as `--restricted`. Ignored in a settings `env` block. Requires v2.1.248+. |
| `CLAUDE_CODE_DISABLE_ULTRAREVIEW_TRUST_CHECK` | `1` stops `claude ultrareview` exiting with `Error: Workspace not trusted` without a terminal or with `CI=true`. From v2.1.314 also skips the trust check in `/ultrareview` and `/code-review ultra`. Set in the launch environment only, only where every review starts in a trusted folder. Requires v2.1.309+. |
