---
type: "Reference"
title: "VS Code prompt box features and commands"
description: "Permission modes, model and effort picker, Ultracode, slash commands, context and cache indicators, and keyboard commands in the extension."
resource: "https://code.claude.com/docs/en/vs-code"
tags: [vscode, prompt-box, slash-commands, permission-modes, shortcuts]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.257"
surfaces: [ide]
requires: ""
identifiers:
  - "/plan"
  - "/plan open"
  - "/model"
  - "/skills"
  - "/status"
  - "/sandbox"
  - "/chrome"
  - "/export"
  - "/logout"
  - "/bug"
  - "/feedback"
  - "/btw"
  - "/copy"
  - "/bookmarks"
  - "/usage"
  - "/tasks"
  - "/compact"
  - "/mcp"
  - "/plugins"
  - "@browser"
  - "@terminal:name"
  - "remoteControlAtStartup"
  - "showThinkingSummaries"
  - "promptSuggestionEnabled"
  - "CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION"
  - "DISABLE_FEEDBACK_COMMAND"
  - "SendUserFile"
  - "cleanupPeriodDays"
  - "modelSettings"
  - "Option+K"
  - "Alt+K"
  - "Cmd+Esc"
  - "Ctrl+Esc"
  - "Cmd+Shift+Esc"
  - "Ctrl+Option+F"
  - "claude-vscode.toggleDictation"
  - "Focus Input"
  - "Open in New Tab"
  - "Open in New Window"
  - "Toggle Focus view"
  - "Rename Session Tab"
  - "Add Session Tab to Group"
  - "Mark Session as Unread"
  - "Accept Change at Cursor"
  - "Reject Change at Cursor"
  - "Claude Code: Add to Chat"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "vs-code"
    resource: "https://code.claude.com/docs/en/vs-code"
    title: "Use Claude Code in VS Code"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Prompt-box features, each with the version it needs:

| Feature | Notes |
|---|---|
| Permission modes | Auto, Manual, Plan, Edit automatically. Auto is the built-in starting mode from v2.1.283 (earlier only Pro, Max, Ultra, Team). Plan opens as a Markdown doc with inline comments |
| `/plan` | v2.1.280+: switch to plan mode (shows plan if already in it); `/plan <task>` starts planning; `/plan open` opens plan file |
| Model picker | `/model` alone opens picker (v2.1.284+); Effort row and level on button (v2.1.257+). Non-`max` level saved per model under `modelSettings`; `max` is session-only |
| Ultracode switch | Under Effort when dynamic workflows are enabled and the model supports it; plans a workflow per substantive task (v2.1.284+) |
| Customize menu | Slash commands dialog (v2.1.257+), `/skills` visibility (v2.1.280+), Output styles (v2.1.257+, build custom v2.1.261+), Hooks view/edit (v2.1.269+), Permissions rules (v2.1.269+), Memory (v2.1.274+, edit v2.1.275+), Instructions (v2.1.274+), `/status` `/sandbox` `/chrome` (v2.1.280+), `/export` (v2.1.280+) |
| Remote Control toggle | "Enable Remote Control for all sessions" sets `remoteControlAtStartup` (v2.1.203+); applies to open sessions in the window, and other windows from v2.1.261 |
| Focus view | Hides tool calls/results/thinking; `Ctrl+Option+F`; subagent progress rows shown (v2.1.269+) |
| Feedback | `/bug`, `/feedback` (v2.1.229+); saved locally under `~/.claude/feedback-bundles/` (v2.1.284+); turned off by org policy, `DISABLE_FEEDBACK_COMMAND` or `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` |
| `/btw` | Side question without adding to the conversation (v2.1.227+); newest 20 exchanges kept, expire per `cleanupPeriodDays` |
| `/copy`, `/bookmarks` | `/copy 2` copies second-to-last response (v2.1.277+); bookmarks panel v2.1.286+ |
| `SendUserFile` | Files Claude sends over Remote Control shown as rows (v2.1.295+) |
| Prompt cache clock | Countdown of the 5-minute or 1-hour cache lifetime; turns red when expired or after compaction |
| Agent map | Agent count at bottom; tree of subagents with status, elapsed time, tokens; stop a subagent; background tasks below (v2.1.269+, tasks v2.1.277+) |
| Suggested prompts | Tab to accept; each uses a background request counting toward usage; off via `promptSuggestionEnabled: false` (and `CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION`) |
| Thinking | Switch in Model section; summaries need `showThinkingSummaries: true` plus reload |

Context helpers: `@file`, `@auth` fuzzy match, trailing slash for folders, `@terminal:name`, `@browser` (Claude in Chrome extension 1.0.36+), `Option+K`/`Alt+K` inserts `@file.ts#5-10`; Explorer "Claude Code: Add to Chat" (v2.1.327+). Selected text from files matching `files.exclude`/`search.exclude` or gitignored is withheld in the chat panel (not in terminal mode). LaTeX math renders in v2.1.301+ (not in terminal mode). PDF page reads need poppler-utils.

# How to use it

Command Palette commands and shortcuts: Focus Input `Cmd+Esc`/`Ctrl+Esc` (macOS Tahoe Game Overlay can intercept it); Open in New Tab `Cmd+Shift+Esc`; New Conversation `Cmd+N` (needs `enableNewConversationShortcut`); Reopen Closed Session `Cmd+Shift+T`; Insert @-Mention `Option+K`; Accept/Reject Change at Cursor (v2.1.275+; per-change buttons disabled for diffs over 100 changes); Toggle Focus view; Rename Session Tab, Add Session Tab to Group, Mark Session as Unread (v2.1.257+); Focus last message (v2.1.268+); `claude-vscode.toggleDictation` `Cmd+D`; Show Logs; Logout.

# Limits and defaults

Unlike the CLI, `Ctrl+J` adds a newline in the prompt box; unbind in `keybindings.json` (`"ctrl+j": null` in a `Chat` block; extension reads this file in 2.1.309+).
