---
type: "Limit"
title: "Background command time limits"
description: "Time limits on background Bash/PowerShell commands in unattended sessions, how to raise them and how long -p runs wait."
resource: "https://code.claude.com/docs/en/tools-reference#time-limit-for-background-commands"
tags: [background, timeout, headless, unattended, limits]
kind: "limit"
maturity: "unlabelled"
since: "2.1.285"
surfaces: [headless, sdk, cloud]
requires: ""
identifiers:
  - "run_in_background"
  - "BASH_DEFAULT_TIMEOUT_MS"
  - "BASH_MAX_TIMEOUT_MS"
  - "CLAUDE_CODE_DISABLE_BACKGROUND_TASKS"
  - "/tasks"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "tools-reference"
    resource: "https://code.claude.com/docs/en/tools-reference"
    title: "Tools reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude sets `run_in_background: true` to start a long-running command as a background task. In sessions that run unattended (a `-p` run, an Agent SDK application, a CI job, a cloud session) background Bash and PowerShell commands have a time limit; local terminal, desktop app and VS Code sessions have none. The limit needs v2.1.285+; before v2.1.288 it applied in every session.

# How to use it

- Default limit counts from the moment the command enters the background: 30 minutes, or the `timeout` Claude passes with `run_in_background`, up to a 2-hour maximum. A foreground command moved to the background at its timeout gets 30 minutes from the move.
- In a `-p` run whose prompt is passed as text (not `--input-format stream-json`), both defaults are 10 minutes.
- Raise: `BASH_DEFAULT_TIMEOUT_MS` above `1800000` replaces the 30-minute default (in text `-p` runs, any value above `600000` replaces the 10-minute default); `BASH_MAX_TIMEOUT_MS` above `7200000`, or `BASH_DEFAULT_TIMEOUT_MS` above `7200000`, raises the 2-hour maximum. Neither can shorten a limit.
- At the limit Claude Code stops the command and tells Claude: `Background command "<description>" was stopped after reaching its background time limit`. Claude can restart with a longer `timeout`.

# Limits and defaults

- A command started by a foreground subagent stops when that subagent's run ends. One started by the main conversation or a background subagent keeps running past a final response until exit, stop or time limit.
- A `-p` run stays open after its result while a main-conversation background command runs, until it exits or hits its limit. A command a background subagent started is stopped when the run exits.
- When a foreground command times out it is moved to background (unless it starts with `sleep`); with `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1` or bare mode it stops instead. The result reads `Command did not complete within its 120s timeout and was moved to the background` with task ID and output path; a `cd`, `pushd`, `popd` or `chdir` in it never carries over (`Session cwd remains <dir>; ...`).
