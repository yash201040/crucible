---
type: "Feature"
title: "Start a turn from a mod with $.prompt.submit"
description: "A background job submits a prompt that Claude reads as from the mod, or as the user with asUser: true."
resource: "https://code.claude.com/docs/en/plugins/mods/api"
tags: [mods, prompt, turns, automation]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "$.prompt.submit"
  - "asUser"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-api"
    resource: "https://code.claude.com/docs/en/plugins/mods/api"
    title: "Use the mods API"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`$.prompt.submit({ text })` starts a turn when a background job finds something needing Claude's attention. Claude reads the text after a sentence naming the mod as sender; `asUser: true` sends it as the user's own words without that sentence.

# Limits and defaults

The call waits until the session is idle, then starts a new turn, and resolves when that turn starts. Do not `await` it in a handler that runs while Claude is working. It resolves with `{ drop: '<reason>' }` when refused (see [refused calls](./refused-calls-after-interruption.md)).
