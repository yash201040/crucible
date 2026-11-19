---
type: "Reference"
title: "Global config keys: copy, agent view, footer"
description: "Keys in ~/.claude.json for /copy, mouse selection, opening agent view, the external editor and the PR status footer."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [global-config, agent-view, copy, claude-json]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "copyFullResponse"
  - "copyOnSelect"
  - "defaultToAgentsView"
  - "externalEditorContext"
  - "leftArrowOpensAgents"
  - "prStatusFooterEnabled"
  - "disableAgentView"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Interface keys saved in `~/.claude.json` (scope `Global config`). Claude Code ignores each of them in `settings.json`. All are booleans.

# How to use it

| Name | Default | What it does |
| - | - | - |
| `copyFullResponse` | `false` | `true`: `/copy` copies the full response without the picker. `false`: when the response has code blocks or blockquotes, `/copy` shows a picker. Choosing "Always copy full response" in the picker sets it to `true`. `/config`: Skip the /copy picker. |
| `copyOnSelect` | `true` | Copies text to the clipboard when a mouse selection finishes in fullscreen rendering or agent view. `false` leaves the clipboard alone; copy with a keyboard shortcut. `/config`: Copy on select (while fullscreen rendering is on). |
| `defaultToAgentsView` | `false` | `true`: running `claude` with no arguments opens agent view instead of a new conversation, unless agent view is turned off (`disableAgentView`). `/config`: Open agents view by default. |
| `externalEditorContext` | `false` | `true`: pressing `Ctrl+G` opens the external editor with Claude's previous response as `#` comment lines (stripped on save; only text below the marker line is sent). Keeps the last 50 lines and marks the cut with `# … (earlier output truncated)`. `/config`: Show last response in external editor. |
| `leftArrowOpensAgents` | `true` | `←` on an empty prompt backgrounds the session and opens agent view. `false` turns the shortcut off; in a session attached to from agent view, `←` on an empty prompt still detaches. `/config`: ← opens agents (when agent view is available). |
| `prStatusFooterEnabled` | `true` | Shows a prompt-footer badge for the current branch's open pull or merge request with a colored status underline. `false` skips the PR/MR check; a session attached from agent view can still show a plain link to a linked pull request. `/config`: Show PR status footer. |

# Notes

Agent view and background sessions are described on the agent-view page; these keys only change how it is reached.
