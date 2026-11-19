---
type: "Guide"
title: "Code tab sessions, prompt box and workspace"
description: "How a Desktop session starts, the prompt box, panes, terminal, file editing, view modes, keyboard shortcuts and usage display."
resource: "https://code.claude.com/docs/en/desktop"
tags: [desktop, code-tab, panes, shortcuts, ui]
kind: "ui"
maturity: "unlabelled"
since: ""
surfaces: [desktop]
requires: "Claude Desktop v1.2581.0 or later for the pane layout, terminal, file editor and view modes"
identifiers:
  - "/context"
  - "/compact"
  - "/btw"
  - "/code-review"
  - "Ctrl+`"
  - "Cmd+Shift+B"
  - "Cmd+Shift+D"
  - "Cmd+;"
  - "Ctrl+O"
  - "Cmd+Shift+M"
  - "Cmd+Shift+I"
  - "Cmd+Shift+E"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "desktop"
    resource: "https://code.claude.com/docs/en/desktop"
    title: "Desktop application"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

In the Claude Desktop app, Claude Code is the **Code** tab (the app also has chat and Cowork). Each conversation is a session with its own chat history, project folder and changes; the sidebar lists sessions and runs several in parallel.

# How to use it

- **Start a session**: in the row under the prompt box choose environment (Local, Cloud, SSH, WSL), project folder (cloud: repositories), permission mode and model; all but the environment can change mid-session. Press Enter to send.
- **Steer**: stop button interrupts at once; typing a correction and pressing Enter sends it without stopping the current action (read after the current action completes).
- **Context**: `@filename` mentions, attach images/PDFs via **+** or drag and drop. In a cloud session `@` lists files only after the first message. In a WSL session the **+** menu may allow only images.
- **Suggested prompts**: grey next-prompt text, accepted with Tab or Right arrow; each suggestion is a background request that counts toward plan usage or API cost; turn off with **Prompt suggestions** in Settings.
- **Panes**: chat, diff, browser, terminal, file, plan, tasks, subagent, plus iOS Simulator on macOS; drag to rearrange, pop out into own window, minimize (Terminal, Browser, iOS Simulator, side chat; needs v4.0.0 or later). Terminal opens in the session working directory with Claude's environment; available in local and SSH sessions.
- **File pane**: local sessions can edit files in the working directory (except view-only ones such as `.mcp.json` and `.claude/settings.json`); cloud, SSH and WSL panes are view-only. **Auto save** is on by default.
- **View modes** (session menu > Transcript view, or Ctrl+O): Normal, Thinking, Verbose.
- **Usage**: Context card (percentage) or the usage ring; `/context` prints a per-category breakdown; plan usage is shared across all Claude Code surfaces. Context auto-summarizes when full; `/compact` does it earlier.

| Shortcut (macOS) | Action |
| - | - |
| Cmd+N / Cmd+W | New / close session |
| Ctrl+Tab, Ctrl+Shift+Tab | Switch sessions |
| Cmd+Shift+D / Cmd+Shift+B | Toggle diff / Browser pane |
| Ctrl+` | Toggle terminal |
| Cmd+; | Open side chat |
| Cmd+Shift+M / I / E | Permission mode / model / effort menu |
| Cmd+/ | Show all shortcuts |

# Limits and defaults

Windows and Linux swap Cmd for Ctrl (Cmd+Option becomes Alt). `Shift+Tab` does not cycle permission modes in Desktop. Terminal-dialog commands with no argument form (for example `/permissions`) reply `isn't available in this environment`; `/config` opens Settings > Code. Versions before 1.46388.1 also had a Summary view mode.
