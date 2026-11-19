---
type: "Reference"
title: "Session, context and background-work commands"
description: "Slash commands for directories, conversation control, branching, forking, background sessions, goals, scheduling and exporting."
resource: "https://code.claude.com/docs/en/commands"
tags: [slash-commands, sessions, context, background, goal]
kind: "slash_command"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "/add-dir"
  - "/autocompact"
  - "/background"
  - "/bg"
  - "/branch"
  - "/btw"
  - "/cd"
  - "/clear"
  - "/reset"
  - "/new"
  - "/compact"
  - "/context"
  - "/copy"
  - "/diff"
  - "/exit"
  - "/quit"
  - "/export"
  - "/fork"
  - "/goal"
  - "/list-agents"
  - "/peers"
  - "/recap"
  - "/rename"
  - "/resume"
  - "/continue"
  - "/rewind"
  - "/checkpoint"
  - "/undo"
  - "/schedule"
  - "/routines"
  - "/status"
  - "/stop"
  - "/subtask"
  - "/tasks"
  - "/bashes"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "commands"
    resource: "https://code.claude.com/docs/en/commands"
    title: "Commands"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Commands that manage the working directory, context window, conversation history, background and forked sessions, goals and scheduled tasks.

# How to use it

| Command | What it does |
| :- | :- |
| `/add-dir <path>` | Add a working directory for file access; most `.claude/` config is not discovered from it; network paths mostly rejected; runs `DirectoryAdded` hooks after a successful add; mid-response, next tool call can use it once confirmed |
| `/autocompact [auto\|<tokens>]` | Set the auto-compact window (for example `500k`), saved to user settings and applied now; no argument opens a dialog. v2.1.221+ |
| `/background [prompt]` | Detach the session as a background agent, optionally sending one more instruction; monitor with `claude agents`. Alias `/bg` |
| `/branch [name]` | Branch the conversation at this point, switch into it, keep the original (return via `/resume`) |
| `/btw [question]` | Side question that does not enter the conversation; with no question shows the latest side question |
| `/cd <path>` | Move the session to a new working directory, keeping the conversation |
| `/clear [name]` | New conversation with empty context; name labels the previous one in `/resume`. Aliases `/reset`, `/new` |
| `/compact [instructions]` | Summarize the conversation to free context, optional focus instructions |
| `/context [all]` | Colored grid of context usage with suggestions and over-limit warning; `all` expands the per-item breakdown in fullscreen |
| `/copy [N]` | Copy the last (or Nth-latest) assistant response; picker for code blocks; `w` writes to a file |
| `/diff` | Review working-tree changes including Claude's edits |
| `/exit` | Exit; in an attached background session it detaches and the session keeps running. Alias `/quit` |
| `/export [filename]` | Export the conversation as plain text to a file or via dialog |
| `/fork [prompt]` | Copy the conversation into a new background session and keep working here; with a prompt the copy starts at once. The copy is told to create its own worktree before code changes (v2.1.221+) unless it edits in place. With agent view off it starts a forked subagent instead |
| `/goal [condition\|clear]` | Keep working across turns until the condition is met; no argument shows the current goal; `clear`, `stop`, `off`, `reset`, `none`, `cancel` remove it |
| `/list-agents` | List subagents, agent-team teammates and other sessions Claude can message, with names. Alias `/peers`. Only where cross-session messaging is enabled; teammate rows need v2.1.239+ |
| `/recap` | One-line session summary on demand |
| `/rename [name]` | Rename the session (works with `-p`); control and invisible characters become spaces and names are capped at 200 characters (v2.1.221+); empty names are rejected |
| `/resume [session]` | Resume by ID or name or open the picker; background sessions are marked `bg`; resuming a running one moves the current conversation to the background and attaches (before v2.1.285 it refused). Alias `/continue` |
| `/rewind` | Roll back conversation and/or code to a checkpoint, or summarize from a message. Aliases `/checkpoint`, `/undo` |
| `/schedule [description]` | Create, update, list or run cloud scheduled tasks (formerly routines). Alias `/routines` |
| `/status` | Settings interface on the Status tab; `Session kind` reads `background job · attached`, `background job · unattended`, or `interactive`. Works mid-response |
| `/stop` | Stop the background session you are attached to; transcript and worktree kept |
| `/subtask <task>` | Spawn a forked background subagent that inherits the conversation and returns its result here; unavailable with agent view off |
| `/tasks` | View and manage background work, including finished subagents. Alias `/bashes` |
