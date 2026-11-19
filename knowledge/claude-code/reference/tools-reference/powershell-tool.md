---
type: "Feature"
title: "PowerShell tool"
description: "Native PowerShell execution: availability by platform, enabling, Bash deny-rule interaction, shell selection and encoding notes."
resource: "https://code.claude.com/docs/en/tools-reference#powershell-tool"
tags: [powershell, windows, shell, preview]
kind: "tool"
maturity: "preview"
since: "2.1.296"
surfaces: [cli]
requires: "PowerShell 7+ (pwsh on PATH) on Linux, macOS, WSL"
identifiers:
  - "PowerShell"
  - "CLAUDE_CODE_USE_POWERSHELL_TOOL"
  - "CLAUDE_CODE_POWERSHELL_RESPECT_EXECUTION_POLICY"
  - "defaultShell"
  - "shell"
  - "PowerShell(git push *)"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "tools-reference"
    resource: "https://code.claude.com/docs/en/tools-reference"
    title: "Tools reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Runs PowerShell commands natively instead of routing through Git Bash. The docs list known preview limitations: PowerShell profiles are not loaded, and on Windows sandboxing is not supported.

# How to use it

- Availability: Windows without Git Bash, automatic. Windows with Git Bash: on by default for claude.ai and Console accounts; set `CLAUDE_CODE_USE_POWERSHELL_TOOL=1` to enable in Bedrock, Google Cloud Agent Platform and Foundry sessions, `0` to turn off. Linux, macOS, WSL: opt-in with `CLAUDE_CODE_USE_POWERSHELL_TOOL=1` (in the environment or `settings.json` `env`), requires PowerShell 7+.
- Windows detects `pwsh.exe` (7+) with fallback to `powershell.exe` (5.1). Spawned with `-ExecutionPolicy Bypass` at process scope (Group Policy still applies); `CLAUDE_CODE_POWERSHELL_RESPECT_EXECUTION_POLICY=1` respects the machine policy.
- Hooks: PreToolUse hooks receive `tool_input.command`; match `Bash|PowerShell` in shell-inspecting hooks.
- Shell selection: `"defaultShell": "powershell"` routes interactive `!` commands (needs the tool enabled); `"shell": "powershell"` on a command hook (works regardless of the tool variable); `shell: powershell` in skill frontmatter for `` !`command` `` blocks (needs the tool enabled).
- Same working-directory reset rules and `CLAUDE_BASH_MAINTAIN_PROJECT_WORKING_DIR` as Bash; persisted `CLAUDE_ENV_FILE` variables reach PowerShell commands (v2.1.296+).

# Limits and defaults

On Windows with Git Bash, any Bash deny rule (bare or scoped like `Bash(git push *)`, from settings or `--disallowedTools`) turns the PowerShell tool off silently, since Bash rules do not restrict it. Keep it on by setting `CLAUDE_CODE_USE_POWERSHELL_TOOL=1` or adding a scoped `PowerShell` rule such as `PowerShell(git push *)`. A rule removing all of Bash leaves no shell tool.

# Notes

Exit code 1 is treated as normal for `grep`, `rg`, `egrep`, `fgrep`, `findstr`, `git grep`, `git diff`; `Error: Exit code 1` may still show in longer pipelines (for example `rg foo | Out-Null`), and for `where.exe`, `fc.exe`, `diff.exe`, and `robocopy` codes 1 to 7 (8 or higher is failure). In a skill with `shell: powershell` such an error counts as failed. Encoding: `>` and `>>` write UTF-8 on 5.1, piped stdin to native commands is UTF-8, error output has no ANSI sequences, a child waiting on stdin gets end-of-file.
