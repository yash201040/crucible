---
type: "Reference"
title: "Voice dictation error messages"
description: "Common /voice error messages and their fixes: account, policy, microphone, SoX, WSL, repeated failures, connection and speech detection."
resource: "https://code.claude.com/docs/en/voice-dictation"
tags: [voice, troubleshooting, errors, microphone]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, ide]
requires: ""
identifiers:
  - "Unknown command: /voice"
  - "Voice mode requires a Claude.ai account"
  - "Voice mode is disabled by your organization's policy"
  - "Microphone access is denied"
  - "Voice mode requires SoX for audio recording"
  - "Voice input is failing repeatedly and has been paused"
  - "No audio detected from microphone"
  - "Voice connection failed"
  - "No speech detected"
  - "tccutil reset Microphone"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "voice-dictation"
    resource: "https://code.claude.com/docs/en/voice-dictation"
    title: "Voice dictation"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Fixes for voice dictation not activating or recording.

# How to use it

| Message | Cause and fix |
| :- | :- |
| `Unknown command: /voice` | No active claude.ai sign-in; run `/login`; remove API key / auth token / `apiKeyHelper` / third-party provider |
| `Voice mode requires a Claude.ai account` | Run `/login` |
| `Voice mode is disabled by your organization's policy` | Admin policy; contact administrator |
| `Microphone access is denied` | Grant terminal microphone permission in OS settings, rerun `/voice` |
| `Voice mode requires SoX for audio recording` (Linux) | Install SoX, e.g. `sudo apt-get install sox` |
| `Voice mode requires a microphone, but SoX could not open an audio capture device` | No capture device (headless/container); reported as of v2.1.195 |
| `Voice mode could not find a working audio recorder in WSL` | `sudo apt install sox libsox-fmt-pulse` |
| `Voice input is failing repeatedly and has been paused` | Three failures within 10 seconds pause dictation until 10 seconds after the first; before v2.1.202 only start-up failures counted |
| `No audio detected from microphone` | Silent capture; check default input device and level; before v2.1.200 could show as connection failure |
| `Voice connection failed` | Recording never reached the service; check network |
| `Voice stream error: WebSocket upgrade rejected with HTTP <status>` | 400-range usually stale sign-in or proxy; run `/login`; non-400 statuses retried once |
| `No speech detected` | Speak closer, reduce noise, match dictation language |

# Notes

- Nothing happens when holding Space: if spaces accumulate, voice is off (`/voice hold`); if only one or two appear, key-repeat is disabled at OS level; switch to `/voice tap`.
- Terminal missing from macOS Microphone settings: `tccutil reset Microphone <bundle-id>` (`com.apple.Terminal`, `com.googlecode.iterm2`; others via `osascript -e 'id of app "AppName"'`), quit with Cmd+Q, relaunch, run `/voice`. Without a bundle ID the reset revokes microphone access for every app.
- TLS-inspecting proxy certificate errors are covered on the VS Code page.
