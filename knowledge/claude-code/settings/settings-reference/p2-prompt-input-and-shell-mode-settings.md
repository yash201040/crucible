---
type: "Reference"
title: "Prompt input, shell mode and voice settings"
description: "Settings for the input box: editor mode, emoji, spellcheck, voice, suggestions, file picker, shell mode and plan-approval menu."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [settings, prompt-input, voice, shell-mode]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "bashEditDiffEnabled"
  - "companyAnnouncements"
  - "defaultShell"
  - "editorMode"
  - "emojiCompletionEnabled"
  - "keybindingFlavor"
  - "promptSuggestionEnabled"
  - "respectGitignore"
  - "respondToBashCommands"
  - "showClearContextOnPlanAccept"
  - "spellcheck"
  - "vimInsertModeRemaps"
  - "voice"
  - "voiceEnabled"
  - "CLAUDE_CODE_BASH_EDIT_DIFF"
  - "CLAUDE_CODE_USE_POWERSHELL_TOOL"
  - "CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Keys that shape typing, shell commands run with the `!` prefix, and a few prompts. Scope is any file unless noted.

# How to use it

| Name | Type / values | Default | What it does |
| :- | :- | :- | :- |
| `bashEditDiffEnabled` | Boolean | unset | Record which files a Bash command changed in a Git repo, show the diff, and give PostToolUse Bash hooks the changed-file list. Unset means recorded only in auto and `bypassPermissions` mode. `true` records in every mode (needs v2.1.269+). A `true` counts only from user settings, `--settings` or managed settings; a repo-level `false` still turns it off. `CLAUDE_CODE_BASH_EDIT_DIFF` overrides per session. A listed file may have been changed by another program |
| `companyAnnouncements` | array of strings | unset | Startup announcements; one random per session, the first on a person's very first launch |
| `defaultShell` | `"bash"` or `"powershell"` | `"bash"` (`"powershell"` on Windows without Bash) | Shell for `!` commands. `"powershell"` needs the PowerShell tool on; on macOS/Linux/WSL/Bedrock/Vertex/Foundry set `CLAUDE_CODE_USE_POWERSHELL_TOOL=1` (`0` turns it off). Falls back to the other shell if unavailable |
| `editorMode` | `"normal"` or `"vim"` | `"normal"` | Prompt key bindings; vim has NORMAL, INSERT, VISUAL |
| `emojiCompletionEnabled` | Boolean | `true` | `:shortcode:` suggestions and replacement |
| `keybindingFlavor` | `"classic"` or `"readline"` | unset | Deprecated since v2.1.261, no effect (readline word editing is always on). Was effective in v2.1.238 to v2.1.260. Still accepted |
| `promptSuggestionEnabled` | Boolean | `true` | Grayed-out prompt predictions. Need claude.ai or Console account with telemetry on; on Bedrock, Google Cloud's Agent Platform, Foundry or with telemetry off, only `CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION=1` turns them on |
| `respectGitignore` | Boolean | `true` | `@` picker hides gitignored files; falls back to `~/.claude.json` value |
| `respondToBashCommands` | Boolean | `true` | `false` adds `!` command output to context without a reply |
| `showClearContextOnPlanAccept` | Boolean | `false` | Adds first plan-approval option "Yes, clear context and ..." |
| `spellcheck` | object: `enabled`, `checker` (`"aspell"`, `"hunspell"`, `"ispell"`, `"auto"`), `language`, `color` | unset (off); checker `"auto"` | Underline misspellings in the input box using an installed checker. User or managed scope; the highest tier's block applies whole. Needs v2.1.235+ |
| `vimInsertModeRemaps` | object: two-character sequence to `"<Esc>"` | unset | INSERT-mode remaps in vim mode; only `"<Esc>"` target supported. User or managed scope |
| `voice` | object: `enabled`, `autoSubmit` (hold mode only), `mode` (`"hold"` or `"tap"`) | unset (off); mode `"hold"` when enabled | Voice dictation; written by `/voice`. Requires a claude.ai account |
| `voiceEnabled` | Boolean | unset | Deprecated since v2.1.92 (replaced by `voice`); `voice.enabled` wins when both set |

# Notes

Prompt suggestions, voice and the file picker are interactive-only conveniences.
