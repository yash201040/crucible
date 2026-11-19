---
type: "Feature"
title: "Hold, tap, cancel and rebind dictation"
description: "Hold mode records while a key is held; tap mode toggles recording and auto-sends; Esc or Ctrl+C cancels; voice:pushToTalk rebinds the key."
resource: "https://code.claude.com/docs/en/voice-dictation"
tags: [voice, keybindings, hold-mode, tap-mode]
kind: "ui"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "voice dictation enabled"
identifiers:
  - "voice:pushToTalk"
  - "~/.claude/keybindings.json"
  - "prefersReducedMotion"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "voice-dictation"
    resource: "https://code.claude.com/docs/en/voice-dictation"
    title: "Voice dictation"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Two recording modes sharing one key binding. Hold mode (default) is push-to-talk using key-repeat detection, so there is a brief warmup (footer `keep holding...` then `listening...`); the first key-repeat characters are removed automatically. Tap mode has no warmup: tap Space on an empty prompt to start (footer `REC · tap to send`), tap again to stop and send.

# How to use it

Rebind in `~/.claude/keybindings.json`, context `Chat`:

```json
{ "bindings": [ { "context": "Chat", "bindings": { "meta+k": "voice:pushToTalk", "space": null } } ] }
```

A custom key replaces the default Space binding. A modifier combo such as `meta+k` starts recording on the first keypress with no warmup and also works in the transcript viewer and vim mode outside INSERT. Avoid bare letters in hold mode. Keys like Caps Lock cannot be bound.

`Esc` or `Ctrl+C` cancels recording (and a transcript still processing), discards the transcript and restores the prompt; neither does anything else in that press.

# Limits and defaults

- Auto-submit (tap mode, or hold with `autoSubmit`) only when the transcript is at least three words; Japanese, Chinese and Thai count individual words.
- Tap mode stops automatically after 15 seconds of silence or two minutes total.
- The transcript is inserted at the cursor. In the VS Code extension a recording ends after 15 seconds without recognized words or at two minutes.
