---
type: "Reference"
title: "Gateway product requirements and rollout checkpoints"
description: "What a gateway must do (format, streaming, routing, header pass-through, unmodified errors, WAF exemption) and the five rollout steps with checkpoints."
resource: "https://code.claude.com/docs/en/llm-gateway-rollout"
tags: [gateway, rollout, requirements, verification]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless]
requires: ""
identifiers:
  - "POST /v1/messages"
  - "GET /v1/models"
  - "claude -p"
  - "x-claude-code-session-id"
  - "ANTHROPIC_AUTH_TOKEN"
  - "ANTHROPIC_API_KEY"
  - "/status"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "llm-gateway-rollout"
    resource: "https://code.claude.com/docs/en/llm-gateway-rollout"
    title: "Roll out an LLM gateway for your organization"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Admin walkthrough assuming a deployed gateway that serves HTTPS at the exact address distributed (not an address that redirects) and routes Claude model names to the provider. Prerequisites: a provider credential (Console API key, or cloud credentials with model access) and a way to deliver settings files (MDM, configuration management).

# How to use it

Gateway requirements: accept a supported API format; stream SSE incrementally including pings; route each Claude model name developers use (a name not routed returns `404`); forward `anthropic-beta`, `anthropic-version` and the body unchanged both ways; return upstream errors unmodified (unless using `capability_rejected:` tokens); exempt the path from request-body WAF inspection (a WAF returns `403` on real sessions while short tests pass). Optionally serve `GET /v1/models` for model discovery.

Five steps, each with a checkpoint:

1. Confirm routing: a one-token `POST /v1/messages` per model name returns `200` with `content` (`404` = name not routed; provider `401` = wrong provider credential).
2. Issue each developer a key (one per developer for attribution and individual offboarding). Bearer gateway: `ANTHROPIC_AUTH_TOKEN`; `x-api-key` gateway: `ANTHROPIC_API_KEY`.
3. Test Claude Code: export base URL and key in a terminal, run `claude -p "Reply with one word: connected"`; gateway log should show `POST` on `/v1/messages` with `200` (match on path since Claude Code appends `?beta=true`). `Not logged in` with empty gateway log means no credential reached the session.
4. Distribute configuration.
5. Verify from a developer machine with a streaming curl (`"stream": true`); data lines must arrive incrementally. Gateway logs identify the developer by credential and group requests by `x-claude-code-session-id`.

# Limits and defaults

A wrong or unreachable base URL makes Claude Code retry with backoff and can show no output for several minutes; check the gateway log instead of waiting.
