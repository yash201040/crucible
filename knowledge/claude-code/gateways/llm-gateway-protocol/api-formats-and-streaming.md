---
type: "Reference"
title: "Gateway API formats, endpoints and streaming rules"
description: "The three API formats a gateway can expose, their endpoints and forward-unchanged fields, optional endpoints, and streaming requirements."
resource: "https://code.claude.com/docs/en/llm-gateway-protocol"
tags: [gateway, api-format, streaming, endpoints]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "/v1/messages"
  - "/v1/messages/count_tokens"
  - "/model/{model}/invoke"
  - "/model/{model}/invoke-with-response-stream"
  - "/model/{model}/count-tokens"
  - ":rawPredict"
  - ":streamRawPredict"
  - "count-tokens:rawPredict"
  - "ANTHROPIC_BASE_URL"
  - "ANTHROPIC_BEDROCK_BASE_URL"
  - "ANTHROPIC_VERTEX_BASE_URL"
  - "ANTHROPIC_FOUNDRY_BASE_URL"
  - "ANTHROPIC_AWS_BASE_URL"
  - "anthropic-workspace-id"
  - "HEAD /api/hello"
  - "application/vnd.amazon.eventstream"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "llm-gateway-protocol"
    resource: "https://code.claude.com/docs/en/llm-gateway-protocol"
    title: "Claude Code gateway compatibility guide"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A gateway must expose at least one format. Terms: "forward unchanged" means pass byte-for-byte; "consume" means the gateway may read it and need not forward.

# How to use it

| Format | Selected by | Endpoints | Forward unchanged |
| - | - | - | - |
| Anthropic Messages | `ANTHROPIC_BASE_URL` | `/v1/messages`, optional `/v1/messages/count_tokens` | `anthropic-beta`, `anthropic-version` headers, plus `Authorization` when a claude.ai login authenticates to Anthropic |
| Amazon Bedrock InvokeModel | `ANTHROPIC_BEDROCK_BASE_URL` with `CLAUDE_CODE_USE_BEDROCK=1` | `/model/{model}/invoke`, `/model/{model}/invoke-with-response-stream`, optional `/model/{model}/count-tokens` | `anthropic_beta`, `anthropic_version` body fields |
| Google Cloud's Agent Platform rawPredict | `ANTHROPIC_VERTEX_BASE_URL` with `CLAUDE_CODE_USE_VERTEX=1` | `:rawPredict`, `:streamRawPredict`, optional `count-tokens:rawPredict` | `anthropic-beta`, `anthropic-version` headers, `anthropic_version` body field |

- Foundry (`ANTHROPIC_FOUNDRY_BASE_URL`) and Claude Platform on AWS (`ANTHROPIC_AWS_BASE_URL`) implement the Anthropic Messages format; a gateway in front of the latter must also forward `anthropic-workspace-id`.
- Token counting is the only optional endpoint; without it Claude Code estimates context by characters.
- Match on path: inference posts to `/v1/messages?beta=true`.
- Best-effort startup traffic a gateway may reject: `HEAD /api/hello` (skipped when an HTTP proxy or client certificate is configured), and on Bedrock-format `GET /inference-profiles?type=SYSTEM_DEFINED` and `GET /inference-profiles/{profile}`.
- The fast mode availability check and WebFetch domain safety check call `api.anthropic.com` directly and never appear in gateway logs.
- Sessions through a gateway are not eligible for the HIPAA configuration.

# Limits and defaults

Streaming: a buffering gateway stalls Claude Code. The full event sequence through `message_delta` and `message_stop` is expected; a body ending cleanly after a content block starts but before the final `message_delta` is treated as a dropped connection. A stream with no bytes longer than the streaming idle timeout is aborted, so a gateway must not strip or buffer SSE `ping` events (a gateway translating from Bedrock's binary stream should emit its own). Bedrock-format streaming must stay binary `application/vnd.amazon.eventstream` with its `Content-Type` unmodified.

# Notes

Format mismatch: with Bedrock or Agent Platform formats Claude Code sends only the subset those providers accept; with Anthropic Messages format it sends the full set even if the gateway forwards to Bedrock or Agent Platform, and bridging is the gateway's job. Claude apps gateway serves its own endpoint reference at `GET /protocol`.
