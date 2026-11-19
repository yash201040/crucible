---
type: "Guide"
title: "Seeing what Claude received"
description: "The SDK stream omits system reminders; log raw API bodies or use a gateway to inspect them."
resource: "https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts"
tags: [debugging, observability, otel, gateway]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "OTEL_LOG_RAW_API_BODIES"
  - "ANTHROPIC_BASE_URL"
  - "<system-reminder>"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-modifying-system-prompts"
    resource: "https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts"
    title: "Modifying system prompts"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The SDK message stream does not include system reminders, so messages your code receives do not show what Claude saw.

# How to use it

- Set `OTEL_LOG_RAW_API_BODIES` to `file:<dir>`; Claude Code writes each request body there.
- Or point `ANTHROPIC_BASE_URL` at a proxy that logs request bodies.

In a logged request, look in the `messages` array: a reminder is inside a user message wrapped in `<system-reminder>` tags or, on some models, a separate message with the `system` role.
