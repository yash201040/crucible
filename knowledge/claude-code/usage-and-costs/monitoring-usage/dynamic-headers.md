---
type: "Feature"
title: "Dynamic OTLP headers via helper script"
description: "otelHeadersHelper runs a script that prints JSON headers, refreshed periodically, for http protocols only."
resource: "https://code.claude.com/docs/en/monitoring-usage"
tags: [telemetry, headers, authentication, helper]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless]
requires: ""
identifiers:
  - "otelHeadersHelper"
  - "CLAUDE_CODE_OTEL_HEADERS_HELPER_DEBOUNCE_MS"
  - "otelHeadersHelper failed; telemetry is not being exported"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "monitoring-usage"
    resource: "https://code.claude.com/docs/en/monitoring-usage"
    title: "Monitoring"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

For environments needing rotating credentials, a script generates OTLP headers. Applies only to `http/protobuf` and `http/json`; with `grpc` only the static `OTEL_EXPORTER_OTLP_HEADERS` variables (and per-signal variants) are used.

# How to use it

```json
{ "otelHeadersHelper": "/path/to/generate-otel-headers.sh" }
```

The value may be an executable path (spaces allowed) or a shell command line with arguments; on Windows it always runs through the shell, so quote paths with spaces. The script must print valid JSON of string key-value header pairs, e.g. `{"Authorization": "Bearer ...", "X-API-Key": "..."}`. It runs at startup and then every 29 minutes by default (`CLAUDE_CODE_OTEL_HEADERS_HELPER_DEBOUNCE_MS`).

# Limits and defaults

If the helper fails or prints bad output, exports fail and the backend receives nothing from the session until it works. Failure is reported as: a once-per-session warning `otelHeadersHelper failed; telemetry is not being exported` in interactive sessions, in `/status`, in the debug log (`--debug` or `/debug`), and on stderr in `-p` sessions.
