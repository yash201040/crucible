---
type: "Reference"
title: "Proxy, TLS certificate and network variables"
description: "Variables for HTTP proxies, CA certificate sources, mTLS client certificates, proxy DNS resolution and request body compression."
resource: "https://code.claude.com/docs/en/env-vars"
tags: [proxy, tls, mtls, network]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "HTTP_PROXY"
  - "HTTPS_PROXY"
  - "NO_PROXY"
  - "CLAUDE_CODE_CERT_STORE"
  - "CLAUDE_CODE_CLIENT_CERT"
  - "CLAUDE_CODE_CLIENT_KEY"
  - "CLAUDE_CODE_CLIENT_KEY_PASSPHRASE"
  - "CLAUDE_CODE_DISABLE_MTLS_RELOAD_ON_STALE_CONNECTION"
  - "CLAUDE_CODE_PROXY_RESOLVES_HOSTS"
  - "CLAUDE_CODE_DISABLE_PROXY_SCHEME_REPAIR"
  - "CLAUDE_CODE_GZIP_REQUEST_BODIES"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "env-vars"
    resource: "https://code.claude.com/docs/en/env-vars"
    title: "Environment variables"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Network plumbing variables.

# How to use it

| Variable | What it does |
| :- | :- |
| `HTTP_PROXY` | HTTP proxy server for network connections. |
| `HTTPS_PROXY` | HTTPS proxy server. |
| `NO_PROXY` | Domains and IPs reached directly, bypassing the proxy. |
| `CLAUDE_CODE_CERT_STORE` | Comma-separated CA sources: `bundled` (Mozilla set) and `system` (OS trust store, only on runtimes with `tls.getCACertificates`: native binary, or Node 22.15+ for npm installs). Default `bundled,system`. |
| `CLAUDE_CODE_CLIENT_CERT` | Client certificate file path for mTLS. |
| `CLAUDE_CODE_CLIENT_KEY` | Client private key path for mTLS. |
| `CLAUDE_CODE_CLIENT_KEY_PASSPHRASE` | Optional passphrase for an encrypted client key. |
| `CLAUDE_CODE_DISABLE_MTLS_RELOAD_ON_STALE_CONNECTION` | `1` stops re-reading the mTLS cert and key after a connection-level failure; rotated files load only at next settings apply or startup. Requires v2.1.232+. |
| `CLAUDE_CODE_PROXY_RESOLVES_HOSTS` | `1` lets the proxy do DNS resolution. With `CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST`, set it in the environment of the process that starts Claude Code. |
| `CLAUDE_CODE_DISABLE_PROXY_SCHEME_REPAIR` | `1` makes Claude Code stop at startup on a plain `host:port` in `HTTPS_PROXY`/`https_proxy` even with no terminal. Ignored in project and local settings. Requires v2.1.327+. |
| `CLAUDE_CODE_GZIP_REQUEST_BODIES` | `0` turns off gzip of API, telemetry and artifact-publish bodies to `api.anthropic.com`. By default large bodies on direct connections are compressed, skipped with a proxy, client certificate or `NODE_EXTRA_CA_CERTS`. |
