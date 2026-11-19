---
type: "Reference"
title: "gateway.yaml structure, secrets and listener"
description: "Layout of gateway.yaml: five required sections, optional sections, secret expansion forms and the listen block."
resource: "https://code.claude.com/docs/en/claude-apps-gateway-config"
tags: [gateway, gateway-yaml, listen, secrets, tls]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "gateway.yaml"
  - "claude gateway --config"
  - "listen.host"
  - "listen.port"
  - "listen.public_url"
  - "listen.tls.cert"
  - "listen.tls.key"
  - "listen.trusted_proxies"
  - "${VAR}"
  - "${file:/path}"
  - "CLAUDE_GATEWAY_LOG_LEVEL"
  - "CLAUDE_GATEWAY_LOG_FORMAT"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "claude-apps-gateway-config"
    resource: "https://code.claude.com/docs/en/claude-apps-gateway-config"
    title: "Claude apps gateway configuration"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A Claude apps gateway is configured by one YAML file, conventionally `gateway.yaml`, read once at startup and validated against a schema at boot (a malformed config fails at start with a field-level error). Five sections are required: `listen`, `oidc`, `session`, `store`, `upstreams`.

# How to use it

Start with `claude gateway --config /path/to/gateway.yaml`.

Optional sections (defaults apply when omitted): `login_notice`, `admin`, `enforcement`, `pricing`, `models` plus `auto_include_builtin_models`, `managed`, `telemetry`, the HTTP tuning blocks (`access_control`, `limits`, `timeouts`, `rate_limits`), and `load_test_mode`.

Secret expansion (do not write `client_secret`, `jwt_secret`, `postgres_url` inline):

| Form | Resolves to |
| - | - |
| `${VAR}` | environment variable; boot fails if undefined |
| `${file:/path}` | trimmed contents of the absolute-path file; must be the field's whole value, not embedded in a longer string |

`listen` fields:

| Field | Default | Notes |
| - | - | - |
| `host` | `0.0.0.0` | bind address |
| `port` | `8080` | bind port |
| `public_url` | none | externally visible `https://` origin; required unless host is loopback; also required to enable telemetry; never derived from `X-Forwarded-*` |
| `tls.cert` / `tls.key` | none | PEM paths if the gateway terminates TLS itself |
| `trusted_proxies` | none | CIDRs/IPs whose `X-Forwarded-For` is trusted, for per-IP rate limits and audit |

Log verbosity: `CLAUDE_GATEWAY_LOG_LEVEL` (debug, info, warn, error; default info; debug also logs claim names of each id_token). `CLAUDE_GATEWAY_LOG_FORMAT=json` writes operational log lines as JSON (v2.1.319 or later); audit events are always emitted.

# Limits and defaults

List a frontend in `trusted_proxies` only if the last `X-Forwarded-For` entry it passes on was not written by a developer. Entries written as `ipv4:port` or `[ipv6]:port` are read with the port dropped.
