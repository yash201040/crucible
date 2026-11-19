---
type: "Feature"
title: "Security guidance plugin"
description: "A hook-based plugin that reviews Claude's own edits for vulnerabilities per edit, per turn and per commit, and has Claude fix findings in the same session."
resource: "https://code.claude.com/docs/en/security-guidance"
tags: [security, plugin, hooks, review]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop, ide]
requires: "Python 3.7+ on PATH (3.10+ for agentic commit review and for model-backed reviews on third-party providers); git repository for turn and commit reviews"
identifiers:
  - "/plugin install security-guidance@claude-plugins-official"
  - "enabledPlugins"
  - "security-guidance@claude-plugins-official"
  - "SessionStart"
  - "UserPromptSubmit"
  - "PostToolUse"
  - "Stop"
  - "~/.claude/security/log.txt"
  - "~/.claude/security/"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "security-guidance"
    resource: "https://code.claude.com/docs/en/security-guidance"
    title: "Catch security issues as Claude writes code"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Installed once, it runs automatically with no command. Three layers:

| Layer | When | How |
| :- | :- | :- |
| Per edit | After Edit, Write, NotebookEdit land | Deterministic pattern match, no model call and no cost; warning appended to Claude's context; fires once per pattern per file per session. Categories: dynamic code execution (`eval(`, `new Function`, `os.system`, `child_process.exec`), unsafe deserialization (`pickle`), DOM injection (`dangerouslySetInnerHTML`, `.innerHTML =`, `document.write`), edits under `.github/workflows/` |
| End of turn | `Stop` hook | Background model review of the turn's git diff (edit tools, Bash, subagents); findings re-prompt Claude; covers up to 30 changed files per turn and fires at most three times in a row before yielding |
| Commit or push | `git commit`/`git push` run through Claude's Bash tool | Background agentic review reading callers and sanitizers; capped at 20 per rolling hour; not triggered by commits from your own shell or `!`; no re-prompt if it duplicates the turn review |

# How to use it

Install: `/plugin install security-guidance@claude-plugins-official` (choose user scope to load everywhere); errors `Marketplace "claude-plugins-official" not found` and `Plugin "<name>" not found in marketplace "claude-plugins-official"` have the same fixes as other official plugins. If `/plugin` is unavailable use the desktop app tab, the VS Code **Manage plugins** dialog, or managed settings. Cloud sessions do not load plugins from user settings or the repo's `.claude/settings.json`. Team enablement: `{"enabledPlugins": {"security-guidance@claude-plugins-official": true}}` in `.claude/settings.json` plus each teammate running `claude plugin install security-guidance@claude-plugins-official --scope project` once per clone; admins set `enabledPlugins` in managed settings.

# Limits and defaults

- First run creates a virtualenv under `~/.claude/security/` and installs the Claude Agent SDK (needs pip and network). If that fails or Python is below 3.10 the first-party commit review falls back to single-shot; on a third-party provider model-backed reviews skip. Interpreter preference: `python3.13` to `python3.10`, then `python3`, `python`, `py -3`.
- Reviews use a separate Claude call with fresh context. Nothing blocks writes or commits; findings reach Claude as instructions and the reviewer can miss issues. Not a complete security solution.
- Available on all plans; reviews run on a Claude Opus model by default and cost usage like any request.

# Notes

Hooks registered: `SessionStart` (bootstrap Python environment), `UserPromptSubmit` (capture working-tree baseline for the turn diff), `PostToolUse` on `Edit`/`Write`/`NotebookEdit` (pattern match), `Stop` (turn review), `PostToolUse` on `Bash` filtered to `git commit` and `git push` (commit review). The plugin's source is a working example of a hook making a separate model call. Diagnostics go to `~/.claude/security/log.txt`; silent skips happen outside git, with no authentication or provider, or when a YAML patterns file exists but PyYAML is not importable.
