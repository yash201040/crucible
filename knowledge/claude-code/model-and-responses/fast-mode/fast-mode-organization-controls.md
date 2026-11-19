---
type: "Feature"
title: "Fast mode per-session opt-in and rate-limit fallback"
description: "fastModePerSessionOptIn makes every session start with fast mode off; rate limits and exhausted credits fall back to standard speed."
resource: "https://code.claude.com/docs/en/fast-mode"
tags: [fast-mode, settings, rate-limits, managed-settings]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, ide, cloud, sdk]
requires: ""
identifiers:
  - "fastModePerSessionOptIn"
  - "--output-format stream-json"
  - "system"
  - "notification"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "fast-mode"
    resource: "https://code.claude.com/docs/en/fast-mode"
    title: "Speed up responses with fast mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Controls for keeping fast mode spend bounded, and the fallback when fast mode cannot be served.

# How to use it

- **Per-session opt-in**: set `"fastModePerSessionOptIn": true` in any settings file so every session starts with fast mode off and users run `/fast` each session. Useful where users run several concurrent sessions. The user's saved preference is kept, so removing the setting restores persistence. Team and Enterprise Owners can deploy it via server-managed settings. When set in managed settings, `/fast on` works only in an interactive terminal session; elsewhere (non-interactive mode, VS Code extension, cloud sessions) it is refused with a message that the organization disabled fast mode.
- **Rate limits**: fast mode has separate rate limits from standard speed. On hitting them, it falls back to standard speed, the `↯` icon turns gray (cooldown), you continue at standard speed and pricing, and fast mode re-enables when the cooldown expires. Run `/fast` to disable manually.
- **Out of usage credits**: each rejected fast request is retried at standard speed and pricing, with no cooldown. Interactive: shows "Fast mode disabled · Out of usage credits" and turns fast mode off (saved preference unchanged; run `/fast` to re-enable). With `--output-format stream-json` and through the Agent SDK: the same text is emitted as a `system` message with subtype `notification`, once per turn while out of credits, and fast mode stays on.
