---
type: "Reference"
title: "Skill injected-command errors and Unknown command"
description: "Errors for skills with injected shell commands (/security-review without origin/HEAD, control characters, 4,000,000-character limit) and unknown slash commands."
resource: "https://code.claude.com/docs/en/errors"
tags: [errors, skills, slash-commands, hooks, git]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.274"
surfaces: [cli, headless, sdk, desktop, ide, cloud]
requires: ""
identifiers:
  - "/security-review"
  - "origin/HEAD"
  - "git remote set-head origin"
  - "allowed-tools"
  - "shell: bash"
  - "shell: powershell"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Errors tied to skills and commands that run shell commands before their prompt, plus how unmatched `/` names are handled across surfaces.

# How to use it

- `/security-review` diffs against `origin/HEAD`. When the ref is missing (single-branch/CI checkout, remote HEAD points at an unpushed branch, no `origin`), it fails with `Error: Shell command failed for pattern "!`git diff --name-only origin/HEAD...`"`. Any skill with injected dynamic context shows the same error and a failed injected command aborts that invocation. Fix: `git remote set-head origin <default-branch>` (if the tracking ref is missing: `git remote set-branches --add origin <branch>`, `git fetch origin`, then set-head) or `git fetch origin` then `git remote set-head origin --auto`. Errors: `Cannot determine remote HEAD`, `Not a valid ref`.
- Sibling strings: `Shell command permission check failed for pattern "..."` (permission check did not allow it; `allowed-tools` can pre-approve) and `Skill <name> requires bash (shell: bash in frontmatter) but Git Bash was not found` (install Git for Windows or use `shell: powershell`).
- `No shell command in <name> was run`: the `` !`...` `` command has a raw control character other than tab/newline (PowerShell tool also refuses U+FEFF, U+180E). Unprintable characters are shown as the replacement character; remove them from the skill file or substituted arguments.
- A message with `more than 4,000,000 characters` means a skill, command, or prompt/agent hook did not run. Save long arguments to a file and pass its path (run `/clear` since text stays in the conversation). Outside Code Mode a `PreToolUse` prompt or agent hook over the limit does not block the call; command hooks have no such limit.
- `Unknown command: /hepl. Did you mean /help?` appears only in an interactive terminal session. In every other session (`-p`, Agent SDK, Desktop Code tab, VS Code chat panel, cloud sessions, cloud scheduled tasks) an unmatched name is sent to Claude as a normal message with a note and list of runnable commands; a built-in command that cannot run there still answers that it is unavailable.

# Limits and defaults

- Skill, command or prompt/agent hook text limit: 4,000,000 characters.
- Prompts starting with `/` followed by punctuation (such as `/--`) or a path (`/var/log/syslog`) are sent as normal messages.

# Notes

Before v2.1.274 only cloud sessions and cloud scheduled tasks sent unmatched names to Claude; before v2.1.273 they answered `Unknown command` too. Before v2.1.236, Enter ran a near-match from the menu.
