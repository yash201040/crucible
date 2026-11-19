---
type: "Reference"
title: "mTLS for the OTLP exporter"
description: "Which client certificate variables apply per OTLP protocol, and which variable trusts the collector's CA."
resource: "https://code.claude.com/docs/en/monitoring-usage"
tags: [telemetry, mtls, otlp, tls]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "CLAUDE_CODE_CLIENT_CERT"
  - "CLAUDE_CODE_CLIENT_KEY"
  - "CLAUDE_CODE_CLIENT_KEY_PASSPHRASE"
  - "NODE_EXTRA_CA_CERTS"
  - "OTEL_EXPORTER_OTLP_CLIENT_KEY"
  - "OTEL_EXPORTER_OTLP_CLIENT_CERTIFICATE"
  - "OTEL_EXPORTER_OTLP_METRICS_CLIENT_KEY"
  - "OTEL_EXPORTER_OTLP_CERTIFICATE"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "monitoring-usage"
    resource: "https://code.claude.com/docs/en/monitoring-usage"
    title: "Monitoring"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Client-certificate setup depends on the OTLP protocol used for each signal (`OTEL_EXPORTER_OTLP_PROTOCOL` or the per-signal override). The same configuration applies to metrics, logs and traces.

# How to use it

| Protocol | Client certificate variables | Trust collector CA with |
| - | - | - |
| `http/protobuf`, `http/json` | `CLAUDE_CODE_CLIENT_CERT`, `CLAUDE_CODE_CLIENT_KEY`, optionally `CLAUDE_CODE_CLIENT_KEY_PASSPHRASE` (see the network configuration page) | `NODE_EXTRA_CA_CERTS` |
| `grpc` | `OTEL_EXPORTER_OTLP_CLIENT_KEY` and `OTEL_EXPORTER_OTLP_CLIENT_CERTIFICATE`, or per-signal variants such as `OTEL_EXPORTER_OTLP_METRICS_CLIENT_KEY` | `OTEL_EXPORTER_OTLP_CERTIFICATE` |

# Notes

For `grpc` the OpenTelemetry SDK reads the standard OTLP variables directly. On machines with managed settings, per-signal credentials may be removed (see [locking](./otlp-destination-locking.md)).
