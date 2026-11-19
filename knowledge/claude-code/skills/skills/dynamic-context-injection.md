---
type: "Feature"
title: "Dynamic context injection (! commands)"
description: "!`cmd` and ```! blocks run shell commands before Claude sees the skill; failures abort the invocation; disableSkillShellExecution turns it off."
resource: "https://code.claude.com/docs/en/skills"
tags: [skills, shell, injection, permissions]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.228"
surfaces: [cli, ide]
requires: ""
identifiers:
  - "!`<command>`"
  - "```!"
  - "disableSkillShellExecution"
  - "shell"
  - "|| true"
  - "[shell command execution disabled by policy]"
  - "ultrathink"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "skills"
    resource: "https://code.claude.com/docs/en/skills"
    title: "Extend Claude with skills"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The syntax `` !`<command>` `` (or a fenced block opened with ` ```! ` for multi-line) runs shell commands before the skill content reaches Claude; output replaces the placeholder. Substitution runs once over the original file and output is not re-scanned for further placeholders. The inline form is recognized only when `!` starts a line or follows whitespace (`` KEY=!`cmd` `` stays literal).

# How to use it

- Disable for user, project, plugin and additional-directory skills with `"disableSkillShellExecution": true` in settings (best in managed settings); each command becomes `[shell command execution disabled by policy]`. Bundled and managed skills are unaffected.
- Synced claude.ai skills never run `!` commands in terminal or VS Code (v2.1.228 or later).
- Including `ultrathink` anywhere in skill content requests deeper reasoning.

# Limits and defaults

How commands run (from the `shell` key and environment):
- `shell: powershell` with the PowerShell tool enabled: runs via PowerShell.
- `shell: bash` with no bash (Windows without Git Bash): invocation fails with ``Skill <name> requires bash (`shell: bash` in frontmatter) but Git Bash was not found``.
- Otherwise Bash tool when available, else PowerShell tool.
- Runs in the session shell's current working directory (moves with `cd`); use `${CLAUDE_SKILL_DIR}` or `${CLAUDE_PROJECT_DIR}` for stable paths. With bash, stderr merges into stdout.
- Each command has the Bash tool's default 2-minute timeout. If auto-moved to background the skill still renders and reports the task and output file; a command never auto-backgrounded is killed at timeout, which aborts the invocation. Output past the inline ceiling arrives as a file path plus preview.

Failures: any failed command aborts the whole invocation (Claude never sees the skill) with `Shell command failed for pattern "..."`. With bash any non-zero exit fails, except exit code 1 from search and comparison commands (listed under tool Output limits), which is a normal result; exit 2 or higher fails. PowerShell has a different carveout set (includes `grep` and `git diff`, not `find` or `diff`). Append `|| true` for commands expected to exit non-zero. `No shell command in <name> was run` means a character the tool rejects.

# Notes

Permissions: injected commands never prompt while rendering. A command matched by a deny rule aborts with `Shell command permission check failed for pattern "..."`. Outside auto mode, any non-allow result aborts unless pre-approved by `allowed-tools`; deny and ask rules, managed-only rules, and bare-repository folders (HEAD beside `refs` or `commondir`, which makes `allowed-tools` ignored for git-containing or unparseable Bash commands) still abort. In auto mode a command needing approval does not abort; the skill loads with an instruction to run it first and Claude's own call goes through auto-mode checks. It still aborts in a forked skill that sets `agent`, and where the shell tool is unavailable.
