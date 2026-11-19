---
type: "Feature"
title: "Dispatching sessions from agent view"
description: "Dispatch input prefixes, in-view commands, and how to target a different directory."
resource: "https://code.claude.com/docs/en/agent-view"
tags: [agent-view, dispatch, subagents, directories]
kind: "ui"
maturity: "research-preview"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "@<agent-name>"
  - "@<repo>"
  - "! <command>"
  - "/exit"
  - "/quit"
  - "/logout"
  - "/login"
  - "/fast"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-view"
    resource: "https://code.claude.com/docs/en/agent-view"
    title: "Manage multiple agents with agent view"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Typing a prompt in the bottom input and pressing `Enter` starts a new background session, auto-named by a Haiku-class model from the prompt (rename with `Ctrl+R`). Images can be pasted. Pasted text over 800 characters or more than three lines collapses to `[Pasted text #N]` (paste again to expand). Prompts shorter than four characters are rejected with `Too short`.

# How to use it

| Input | Effect |
| :- | :- |
| `<agent-name> <prompt>` | First word matching a custom subagent runs it as the main agent with its frontmatter config |
| `@<agent-name>` | Same, anywhere in the prompt |
| `@<repo>` | Run the session in that repository |
| `/<command>` | Suggest skills and commands as the prompt |
| `! <command>` | Run a shell command as a background job instead of a Claude session |
| `#<number>` or PR/MR URL | Select the existing session on that request |

Commands run in agent view itself: `/exit`, `/quit`, `/logout`, `/login`, `/model`, `/effort`, `/fast` (the last two need v2.1.299+), and bare `/resume`/`/continue`. Skills, custom commands and prompt-expanding built-ins such as `/init` are sent to a new session as first prompt. Other built-ins show `isn't available in agent view` and the text stays in the input. When `@name` matches both a subagent and a repo, the subagent wins; a prompt starting with a subagent name also matches (use `@` to be explicit).

Target another directory: open `claude agents` there; or from a parent use `@<repo>` (typing `@` lists git repos one level below, registered worktrees inside the repo tree such as `.claude/worktrees/` ones labelled with branch, and directories that already have a session; names with spaces are not listed; worktrees outside the repo, e.g. `../feature`, are not listed); or `cd` and `claude --bg "<prompt>"`. Grouped by directory, dispatch goes to the selected row's directory. Packaging a recurring task as a skill lets you dispatch it repeatedly.
