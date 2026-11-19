---
type: "Feature"
title: "Voice dictation setup and requirements"
description: "The /voice command and voice settings enable hold or tap speech-to-text for the prompt; needs a claude.ai account and a local microphone."
resource: "https://code.claude.com/docs/en/voice-dictation"
tags: [voice, dictation, speech, requirements]
kind: "slash_command"
maturity: "unlabelled"
since: ""
surfaces: [cli, ide]
requires: "claude.ai account sign-in; local microphone; not available with API key, Bedrock, Google Cloud's Agent Platform or Foundry"
identifiers:
  - "/voice"
  - "/voice hold"
  - "/voice tap"
  - "/voice off"
  - "voice.enabled"
  - "voice.mode"
  - "voice.autoSubmit"
  - "language"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "voice-dictation"
    resource: "https://code.claude.com/docs/en/voice-dictation"
    title: "Voice dictation"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Speech is streamed to Anthropic servers for transcription (not processed locally) and appears live in the prompt input, mixing with typing. Transcription consumes no Claude messages or tokens and does not count toward `/usage` limits. It is tuned for coding vocabulary and adds the project name and git branch as hints.

# How to use it

| Command | Effect |
| :- | :- |
| `/voice` | Toggle on/off, keep current mode |
| `/voice hold` | Hold mode (default) |
| `/voice tap` | Tap mode |
| `/voice off` | Disable |

Persist in user settings: `{ "voice": { "enabled": true, "mode": "tap" } }`. Enabling runs a microphone check (triggers the macOS permission prompt). `"autoSubmit": true` in `voice` sends on key release in hold mode when the transcript has at least three words.

# Limits and defaults

- Requires a claude.ai account; not available with `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN`, an `apiKeyHelper` setting, Bedrock, Google Cloud's Agent Platform or Microsoft Foundry (those take precedence over a claude.ai sign-in).
- Needs a local microphone: does not work in cloud sessions or SSH sessions. VS Code extension supports it with the same account requirement but not in VS Code Remote (SSH, Dev Containers, Codespaces). WSL needs WSLg (WSL2).
- Audio uses a built-in native module on macOS, Linux and Windows; Linux falls back to `arecord` (ALSA) or `rec` (SoX).
- The `hold space to speak` hint shows for the first three sessions when the prompt is empty, and not with a custom status line.
- Dictation works in agent view in hold mode (dispatch input or peek-panel reply).

# Notes

- Language follows the `language` setting (code or name, e.g. `"japanese"`); empty means English (in VS Code, `accessibility.voice.speechLanguage` is used first). Supported codes: cs, da, nl, en, fr, de, el, hi, id, it, ja, ko, no, pl, pt, ru, es, sv, tr, uk. An unsupported language warns and falls back to English for dictation only.
