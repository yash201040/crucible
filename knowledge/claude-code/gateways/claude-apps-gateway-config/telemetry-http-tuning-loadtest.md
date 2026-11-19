---
type: "Reference"
title: "Gateway telemetry relay, HTTP tuning, load test mode"
description: "OTLP forwarding with per-signal opt-in, access control and rate limits, request limits, and load_test_mode for unmetered load tests."
resource: "https://code.claude.com/docs/en/claude-apps-gateway-config"
tags: [gateway, telemetry, otlp, rate-limits, load-test]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop]
requires: ""
identifiers:
  - "telemetry.forward_to"
  - "telemetry.resource_attributes"
  - "CLAUDE_CODE_ENABLE_TELEMETRY"
  - "OTEL_METRICS_EXPORTER"
  - "OTEL_LOGS_EXPORTER"
  - "OTEL_TRACES_EXPORTER"
  - "OTEL_EXPORTER_OTLP_ENDPOINT"
  - "OTEL_EXPORTER_OTLP_PROTOCOL"
  - "OTEL_EXPORTER_OTLP_HEADERS"
  - "OTEL_RESOURCE_ATTRIBUTES"
  - "OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE"
  - "CLAUDE_CODE_ENHANCED_TELEMETRY_BETA"
  - "otelHeadersHelper"
  - "access_control.allow_cidrs"
  - "access_control.deny_cidrs"
  - "limits.max_request_bytes"
  - "limits.max_request_header_bytes"
  - "limits.max_url_length"
  - "timeouts.upstream_ttfb_ms"
  - "rate_limits.device_authorization"
  - "rate_limits.device_verify"
  - "load_test_mode.enabled"
  - "load_test_mode.reply_tokens"
  - "load_test_mode.reply_seconds"
  - "x-load-test-user"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "claude-apps-gateway-config"
    resource: "https://code.claude.com/docs/en/claude-apps-gateway-config"
    title: "Claude apps gateway configuration"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The gateway is an OTLP relay: clients send metrics, logs and (optionally) traces to it, and it forwards them verbatim over HTTP to each `telemetry.forward_to` destination. Sessions from `/login` are stamped with `user.id`, `user.email`, `user.groups` (v2.1.265 or later for Desktop/Cowork; `enduser.sub` v2.1.274 or later). Data goes only to destinations you configure, never to Anthropic. Four HTTP tuning blocks and `load_test_mode` round out the operational surface.

# How to use it

`forward_to` entries take `url` (https, with a loopback exception needing `CLAUDE_GATEWAY_ALLOW_LOOPBACK=1`), `headers`, and per-signal `metrics` (default true), `logs`, `traces` (default false). Setting `forward_to` plus `listen.public_url` makes the gateway push `CLAUDE_CODE_ENABLE_TELEMETRY=1`, the three `OTEL_*_EXPORTER` selectors, `OTEL_EXPORTER_OTLP_ENDPOINT=<public_url>` and `OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf` to clients. Traces also need `CLAUDE_CODE_ENHANCED_TELEMETRY_BETA=1` in a policy `env`. `telemetry.resource_attributes` adds fixed labels (v2.1.281 or later; reserved prefixes `user.`, `enduser.`, `identity.`). To export straight to your own collector set `OTEL_EXPORTER_OTLP_ENDPOINT` in a policy `env` (v2.1.265 or later on clients; not honored when `otelHeadersHelper` is set). Use `OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE=cumulative` for cumulative-only collectors.

HTTP tuning defaults:

| Key | Default | Notes |
| - | - | - |
| `access_control.allow_cidrs` / `deny_cidrs` | empty | deny checked first; non-empty allow list is default-deny; `/healthz` and `/readyz` exempt |
| `limits.max_request_bytes` | 32 MiB | oversize gets `413` |
| `limits.max_request_header_bytes` | unset | lowers 256 KiB cap; over gets `431` |
| `limits.max_url_length` | unset | over gets `414` |
| `timeouts.upstream_ttfb_ms` | 120000 | upstream header wait |
| `rate_limits.device_authorization` | 30 per 600 s | per-IP, sign-in only |
| `rate_limits.device_verify` | 10 per 600 s | per-IP code guess limit |

`load_test_mode` (v2.1.282 or later): `enabled` (required), `reply_tokens` (default 750, 1-100000), `reply_seconds` (default 9.5, 0-600). Requests build and sign as usual but are discarded and answered with a canned reply; `x-load-test-user` (up to seven digits) counts as separate developers. Needs an empty database; audit `inference` events carry `load_test: true`. Never enable on a gateway developers use.

# Limits and defaults

The gateway does not buffer or retry telemetry. After five consecutive failed deliveries it pauses a destination in 30-second stretches. `400`, `413`, `415`, `422`, `431` do not count as failures. Logs and traces can carry full Bash commands and file paths; metrics are aggregate counters. Telemetry is off in the CLI by default.
