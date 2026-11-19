---
type: "Reference"
title: "VS Code extension settings"
description: "Settings under Extensions > Claude Code (claudeCode.*) with their defaults and version requirements."
resource: "https://code.claude.com/docs/en/vs-code"
tags: [vscode, settings, extension, reference]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [ide]
requires: ""
identifiers:
  - "useTerminal"
  - "initialPermissionMode"
  - "preferredLocation"
  - "lockEditorGroups"
  - "autosave"
  - "attachOpenFile"
  - "attachSelection"
  - "useCtrlEnterToSend"
  - "scrollToBottomOnSend"
  - "showMessageTimestamps"
  - "spinnerVerbs"
  - "enableNewConversationShortcut"
  - "enableReopenClosedSessionShortcut"
  - "archiveInactiveSessions"
  - "continueAfterReload"
  - "hideOnboarding"
  - "focusView"
  - "respectGitIgnore"
  - "usePythonEnvironment"
  - "environmentVariables"
  - "disableLoginPrompt"
  - "allowDangerouslySkipPermissions"
  - "claudeProcessWrapper"
  - "claudeCode.useTerminal"
  - "chat.fontSize"
  - "chat.fontFamily"
  - "chat.editor.fontSize"
  - "chat.editor.fontFamily"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "vs-code"
    resource: "https://code.claude.com/docs/en/vs-code"
    title: "Use Claude Code in VS Code"
stale_after: "2027-01-19T00:00:00Z"
---

# How to use it

Extension settings live in VS Code settings (Extensions > Claude Code); shared Claude Code settings live in `~/.claude/settings.json` (allowed commands, env vars, hooks, MCP servers). `initialPermissionMode` is read from user settings only; workspace values are ignored (before v2.1.225 the default was `default` and workspace values applied).

| Setting | Default | What it does |
|---|---|---|
| `useTerminal` | `false` | Terminal mode instead of the graphical panel |
| `initialPermissionMode` | unset | New-conversation mode: `default`, `plan`, `acceptEdits`, `bypassPermissions`; `manual` aliases `default` |
| `preferredLocation` | `panel` | `sidebar` (right) or `panel` (new tab) |
| `lockEditorGroups` | `true` | Lock editor groups Claude starts (v2.1.274+) |
| `autosave` | `true` | Auto-save before Read/Edit/Write tools run (does not save before NotebookEdit) |
| `attachOpenFile` | `true` | Add open file to messages (v2.1.271+) |
| `attachSelection` | `true` | Add selected text to messages (v2.1.300+) |
| `useCtrlEnterToSend` | `false` | Ctrl/Cmd+Enter sends |
| `scrollToBottomOnSend` | `true` | Scroll on send (v2.1.275+) |
| `showMessageTimestamps` | `true` | Timestamps (v2.1.284+; default `false` before v2.1.290) |
| `spinnerVerbs` | `{"mode":"append","verbs":[]}` | Spinner verbs, same fields as CLI |
| `enableNewConversationShortcut` | `false` | Cmd/Ctrl+N new conversation |
| `enableReopenClosedSessionShortcut` | `true` | Cmd/Ctrl+Shift+T reopens closed Claude tab |
| `archiveInactiveSessions` | `14` | Days before auto-archive: 1, 2, 7, 14; `0` off (v2.1.265+) |
| `continueAfterReload` | `true` | Continue interrupted step after reload (v2.1.274+) |
| `hideOnboarding` | `false` | Hide onboarding checklist |
| `focusView` | `false` | Hide tool calls/results/thinking (v2.1.221+) |
| `respectGitIgnore` | `true` | Exclude gitignored files from searches and selection context |
| `usePythonEnvironment` | `true` | Activate workspace Python env (needs Python extension) |
| `environmentVariables` | `[]` | Env vars for the Claude process; `CLAUDE_CONFIG_DIR` only if absolute path |
| `disableLoginPrompt` | `false` | Skip auth prompts (third-party providers) |
| `allowDangerouslySkipPermissions` | `false` | Adds Bypass permissions to mode selector; sandboxes without internet only |
| `claudeProcessWrapper` | unset | Executable that launches the Claude process; skips the "still open somewhere else" check; set when no bundled binary exists for the platform |

Font settings: `chat.fontSize`, `chat.fontFamily` (VS Code 1.104+), `chat.editor.fontSize` (v2.1.300+), `chat.editor.fontFamily`.

# Notes

`CLAUDE_CODE_RESUME_*` variables set in VS Code's environment or `environmentVariables` have no effect in the panel (the extension strips them). Add `"$schema": "https://json.schemastore.org/claude-code-settings.json"` to `settings.json` for validation.
