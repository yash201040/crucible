---
type: "Reference"
title: "Multiline, quick commands, transcript viewer, voice keys"
description: "Ways to enter multiline input, the prefix characters at prompt start, transcript viewer keys and the dictation key."
resource: "https://code.claude.com/docs/en/interactive-mode"
tags: [keyboard, multiline, transcript, voice, prefixes]
kind: "ui"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "Shift+Enter"
  - "Option+Enter"
  - "Ctrl+J"
  - "/"
  - "!"
  - "@"
  - ":"
  - "?"
  - "transcript:toggleShowAll"
  - "transcript:exit"
  - "/voice tap"
  - "/tui"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "interactive-mode"
    resource: "https://code.claude.com/docs/en/interactive-mode"
    title: "Interactive mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Smaller shortcut tables: multiline entry, quick-command prefixes, transcript viewer keys, voice dictation, and command completion.

# How to use it

| Input | Meaning |
| :- | :- |
| `\` + `Enter` | Newline, works in all terminals |
| `Option+Enter` | Newline after enabling Option as Meta on macOS |
| `Shift+Enter` | Native in iTerm2, WezTerm, Ghostty, Kitty, Warp, Windows Terminal 1.25+ |
| `Ctrl+J` | Newline in any terminal |
| `/` at start | Command or skill |
| `!` at start | Shell mode |
| `@` | File path mention; with cross-session messaging, one letter after `@` also suggests other live sessions (v2.1.232+) |
| `:` | Emoji shortcode |
| `?` on empty input | Toggle shortcut help panel |

Transcript viewer (toggled by `Ctrl+O`): `?` help, `{` / `}` previous/next user prompt, `[` write full conversation to terminal scrollback, `v` open in `$VISUAL`/`$EDITOR` (all need fullscreen rendering); `Ctrl+E` toggle show all (classic renderer only; rebindable via `transcript:toggleShowAll`); `q`, `Ctrl+C`, `Esc` exit (rebindable via `transcript:exit`). `/tui` with no argument shows the active renderer. Inside the `/theme` picker, `Ctrl+T` toggles syntax highlighting.

Voice: hold or tap `Space` for dictation when voice dictation is enabled; `/voice tap` switches to tap-to-toggle.

Mid-prompt completion: type `/` after a space plus first letters; a command runs only when it starts the message. Fullscreen shows a list (`Tab` inserts top match, no row highlighted so `Enter` sends as typed); classic shows ghost text with a count like `+2`. A plugin skill matches on its bare name and inserts the full `/plugin:skill`.
