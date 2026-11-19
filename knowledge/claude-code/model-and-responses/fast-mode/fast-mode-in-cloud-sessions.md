---
type: "Feature"
title: "Fast mode in cloud sessions"
description: "Fast mode works in cloud sessions with /fast on for that session only, on Anthropic-managed or self-hosted runners."
resource: "https://code.claude.com/docs/en/fast-mode"
tags: [fast-mode, cloud-sessions, self-hosted]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.271"
surfaces: [cloud, web]
requires: "Claude Code v2.1.271+ in the session environment; fast mode available to the account"
identifiers:
  - "/fast on"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "fast-mode"
    resource: "https://code.claude.com/docs/en/fast-mode"
    title: "Speed up responses with fast mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Fast mode works in cloud sessions, whether on Anthropic-managed infrastructure or a self-hosted runner on the Anthropic API.

# How to use it

Type `/fast on` in the session. It stays on for that session only and is not saved as your default. At claude.ai/code you can also toggle it from the model menu on the message box (shown when the plan includes fast mode and the model supports it). All [requirements](./fast-mode-requirements.md) apply. Managed `fastModePerSessionOptIn: true` refuses `/fast on` in cloud sessions.
