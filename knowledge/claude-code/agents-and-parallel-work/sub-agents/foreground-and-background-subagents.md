---
type: "Feature"
title: "Foreground and background subagents"
description: "Subagents Claude spawns start in the background by default; how waiting, permissions, notifications and panel rows behave."
resource: "https://code.claude.com/docs/en/sub-agents"
tags: [subagents, background, foreground, fork-mode, permissions]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.302"
surfaces: [cli, headless, sdk, ide, desktop]
requires: ""
identifiers:
  - "CLAUDE_CODE_FORK_SUBAGENT"
  - "CLAUDE_CODE_DISABLE_BACKGROUND_TASKS"
  - "background"
  - "/tasks"
  - "Ctrl+B"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sub-agents"
    resource: "https://code.claude.com/docs/en/sub-agents"
    title: "Create custom subagents"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Foreground subagents block the main conversation and pass permission prompts through. Background subagents run concurrently; a permission prompt they hit surfaces in the main session naming the subagent (approve, or Esc to deny that one call). With nothing configured, a subagent Claude spawns from the main conversation starts in the background.

# How to use it

- `claude -p` and the Agent SDK: Claude can wait, on its own judgment or when asked.
- Interactive terminal, VS Code and desktop sessions on your machine: to let Claude wait, set `CLAUDE_CODE_FORK_SUBAGENT` to `0` (e.g. in the `env` block of settings.json), restart, then ask Claude to wait ("run the reviewer subagent and wait for its report"). Ctrl+B in the terminal (or Run in background in VS Code) moves the wait to the background.
- `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1` instead makes Claude wait for subagents; background commands are off and Ctrl+B does nothing.
- Frontmatter `background: true` forces background even if Claude asks to wait.
- A skill with `context: fork` follows the skills page rules regardless of fork mode.

# Limits and defaults

- Background subagents get a smaller built-in tool set (see available tools), except forks and resumed foreground subagents.
- A durable permission answer (e.g. a grant for the rest of the session) given to a background subagent applies to the whole session including the main conversation.
- A background subagent can leave a background Bash/PowerShell command running past its turn; Claude Code notifies the subagent when it ends.
- Results arrive as a completion notification in a later turn; Claude waits for it before reporting.
- Panel rows: a successful subagent's row is removed immediately and `/tasks to see subagents` shows in the footer for 30 seconds (open it in `/tasks` with Enter); failed or stopped rows stay 30 seconds (press `x` to clear). A completed subagent stays in `/tasks` marked done for 30 seconds. Before v2.1.232 and v2.1.208 these behaved differently.
