---
type: "Reference"
title: "Bash, PowerShell and shell tool variables"
description: "Variables for shell tool timeouts, output size, shell choice, command wrapping, working directory, PowerShell behavior and edit diffs."
resource: "https://code.claude.com/docs/en/env-vars"
tags: [bash, powershell, timeouts, shell]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "BASH_DEFAULT_TIMEOUT_MS"
  - "BASH_MAX_TIMEOUT_MS"
  - "BASH_MAX_OUTPUT_LENGTH"
  - "CLAUDE_BASH_MAINTAIN_PROJECT_WORKING_DIR"
  - "CLAUDE_CODE_BASH_EDIT_DIFF"
  - "CLAUDE_CODE_SHELL"
  - "CLAUDE_CODE_SHELL_PREFIX"
  - "CLAUDE_CODE_GIT_BASH_PATH"
  - "CLAUDE_CODE_USE_POWERSHELL_TOOL"
  - "CLAUDE_CODE_POWERSHELL_RESPECT_EXECUTION_POLICY"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "env-vars"
    resource: "https://code.claude.com/docs/en/env-vars"
    title: "Environment variables"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Controls for how commands run and how much output returns.

# How to use it

| Variable | What it does |
| :- | :- |
| `BASH_DEFAULT_TIMEOUT_MS` | Default timeout for a foreground Bash or PowerShell command (120000 = 2 min). A value above the default background time limit replaces that default in unattended sessions (needs v2.1.285+). |
| `BASH_MAX_TIMEOUT_MS` | Maximum timeout the model may set (default 600000 = 10 min); the effective ceiling is the larger of this and `BASH_DEFAULT_TIMEOUT_MS`. A ceiling over 2 hours also becomes the max background time limit in unattended sessions (v2.1.285+). |
| `BASH_MAX_OUTPUT_LENGTH` | Characters of bash output read back into a result (default 30000, max 150000). Ignored if the `bashOutputMaxChars` setting is set. |
| `CLAUDE_BASH_MAINTAIN_PROJECT_WORKING_DIR` | Return to the original working directory after each Bash or PowerShell command in the main session. |
| `CLAUDE_CODE_BASH_EDIT_DIFF` | `0` turns off the diff of files changed during a Bash command; `1` records it in every permission mode. Beats `bashEditDiffEnabled`. Requires v2.1.269+. |
| `CLAUDE_CODE_SHELL` | Path to a `bash` or `zsh` binary for the Bash tool (for example `/opt/homebrew/bin/bash`); other shells such as `fish` unsupported. Invalid values fall back to auto-detection (`$SHELL` if bash or zsh, else first working `zsh` then `bash`). |
| `CLAUDE_CODE_SHELL_PREFIX` | Prefix wrapping Bash calls, hook commands, status line commands and stdio MCP startup commands (not PowerShell or exec-form hooks). The wrapper gets the command as one quoted `$1` and must re-evaluate it, for example `exec bash -c "$1"`. For Bash calls `$1` is the full assembled invocation. |
| `CLAUDE_CODE_GIT_BASH_PATH` | Windows: path to `bash.exe`. Invalid paths or names other than `bash.exe`, `sh.exe`, `bash`, `sh` are ignored with a `--debug` warning. Before v2.1.219 a missing path exited at startup. |
| `CLAUDE_CODE_USE_POWERSHELL_TOOL` | Windows without Git Bash: tool on automatically, `0` disables. Windows with Git Bash: on by default for claude.ai and Console accounts; `1` enables on Bedrock, Google Cloud's Agent Platform, Foundry; `0` turns off. Linux, macOS, WSL: `1` enables, requires `pwsh` on `PATH`. |
| `CLAUDE_CODE_POWERSHELL_RESPECT_EXECUTION_POLICY` | `1` stops passing `-ExecutionPolicy Bypass` for PowerShell in tool calls, hooks and status line; process-scope bypass never overrides Group Policy `MachinePolicy` or `UserPolicy`. |
