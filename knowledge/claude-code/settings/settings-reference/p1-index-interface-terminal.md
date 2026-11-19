---
type: "Reference"
title: "Index: interface and terminal keys"
description: "Settings keys for display, input, notifications, status line, themes, voice, accessibility and tools in the desktop browser pane (index rows only)."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [interface, terminal, ui, settings]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop]
requires: ""
identifiers:
  - "askUserQuestionTimeout"
  - "autoContinueAtUsageLimit"
  - "autoScrollEnabled"
  - "axScreenReader"
  - "bashEditDiffEnabled"
  - "companyAnnouncements"
  - "defaultShell"
  - "dialogExpiry"
  - "editorMode"
  - "emojiCompletionEnabled"
  - "fileSuggestion"
  - "footerLinksRegexes"
  - "keybindingFlavor"
  - "maxProseWidth"
  - "prefersReducedMotion"
  - "promptSuggestionEnabled"
  - "respectGitignore"
  - "respondToBashCommands"
  - "showClearContextOnPlanAccept"
  - "showTurnDuration"
  - "spellcheck"
  - "spinnerTipsEnabled"
  - "spinnerTipsOverride"
  - "spinnerVerbs"
  - "statusLine"
  - "syntaxHighlightingDisabled"
  - "terminalProgressBarEnabled"
  - "terminalTitleFromRename"
  - "theme"
  - "timeFormat"
  - "timeZone"
  - "tui"
  - "verbose"
  - "viewMode"
  - "vimInsertModeRemaps"
  - "voice"
  - "voiceEnabled"
  - "wheelScrollAccelerationEnabled"
  - "browserExternalPageTools"
  - "disableBrowserExternalNavigation"
  - "disableMobileSimulatorTools"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Index entries from "Interface and terminal" plus three managed "Tools" keys for the desktop app. Detailed sections are in other parts of the page.

# How to use it

| Key | Scope | What it does |
| :- | :- | :- |
| `askUserQuestionTimeout` | User or managed | Let an unanswered question auto-continue after idle time |
| `autoContinueAtUsageLimit` | User or managed | Wait in the open session and continue automatically after a claude.ai usage limit resets |
| `dialogExpiry` | User or managed | How long Claude Code waits for Remote Control or an SDK host to answer a forwarded dialog before cancelling it |
| `bashEditDiffEnabled` | User or managed | Record files changed while a Bash command ran, in every permission mode |
| `axScreenReader` | User or managed | Screen-reader friendly output |
| `companyAnnouncements` | Any file | Show organization announcements at startup |
| `defaultShell` | Any file | Bash or PowerShell for commands typed with the `!` prefix |
| `respondToBashCommands` | Any file | Stop Claude responding after a `!` shell command runs |
| `editorMode` | Any file | Vim key bindings in the input prompt |
| `vimInsertModeRemaps` | User or managed | Map a two-key INSERT-mode sequence such as `jj` to Escape |
| `keybindingFlavor` | Any file | Deprecated, no effect; word-editing shortcuts follow readline |
| `emojiCompletionEnabled` | Any file | Turn off `:shortcode:` emoji suggestions |
| `fileSuggestion` | Any file | Supply `@` file autocomplete from your own command |
| `respectGitignore` | Any file | Keep gitignored files out of the `@` picker |
| `footerLinksRegexes` | User or managed | Turn issue or review IDs into clickable links below the input box |
| `maxProseWidth` | Any file | Cap prose width in wide terminals |
| `promptSuggestionEnabled` | Any file | Hide grayed-out prompt suggestions |
| `showClearContextOnPlanAccept` | Any file | Show a clear-context option on the plan accept screen |
| `showTurnDuration` | Any file | Hide the "Cooked for" duration |
| `spellcheck` | User or managed | Underline misspellings with an installed spell checker |
| `spinnerTipsEnabled` | Any file | Hide spinner tips |
| `spinnerTipsOverride` | Any file | Add or replace spinner tips |
| `spinnerVerbs` | Any file | Add or replace spinner verbs |
| `statusLine` | Any file | Run your own command to render a status line |
| `syntaxHighlightingDisabled` | Any file | Turn off syntax highlighting |
| `terminalProgressBarEnabled` | Any file | Hide the terminal progress bar |
| `terminalTitleFromRename` | Any file | Stop `/rename` and `--name` from changing the tab title |
| `theme` | Any file | Color theme, built-in or custom |
| `timeFormat` | Any file | 12-hour, 24-hour, UTC or strftime time display |
| `timeZone` | Any file | Time zone for displayed times |
| `tui` | Any file | Fullscreen or classic renderer |
| `autoScrollEnabled` | Any file | Follow new output to the bottom in fullscreen rendering |
| `wheelScrollAccelerationEnabled` | Any file | Turn off mouse-wheel acceleration in fullscreen |
| `prefersReducedMotion` | Any file | Reduce or turn off spinner, shimmer and flash animations |
| `verbose` | Any file | Show full tool output; `viewMode` takes precedence when both are set |
| `viewMode` | Any file | Start sessions in default, verbose or focus view |
| `voice` | Any file | Turn on voice dictation and pick hold or tap mode |
| `voiceEnabled` | Any file | Voice dictation, older single-key form |
| `browserExternalPageTools` | Managed | Keep Claude's tools off external pages in the desktop Browser pane |
| `disableBrowserExternalNavigation` | Managed | Limit the desktop Browser pane to localhost |
| `disableMobileSimulatorTools` | Managed | Block Claude's tools in the desktop iOS Simulator pane |
