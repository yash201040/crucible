---
type: "Reference"
title: "Proxy, CA certificate and mTLS configuration"
description: "Proxy variables, CA store sources, custom CA files and mTLS client certificates with rotation behavior, plus where each is honored."
resource: "https://code.claude.com/docs/en/network-config"
tags: [proxy, ca-certificates, mtls, network]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop, web]
requires: ""
identifiers:
  - "HTTPS_PROXY"
  - "HTTP_PROXY"
  - "NO_PROXY"
  - "https_proxy"
  - "http_proxy"
  - "CLAUDE_CODE_CERT_STORE"
  - "NODE_EXTRA_CA_CERTS"
  - "CLAUDE_CODE_GZIP_REQUEST_BODIES"
  - "CLAUDE_CODE_CLIENT_CERT"
  - "CLAUDE_CODE_CLIENT_KEY"
  - "CLAUDE_CODE_CLIENT_KEY_PASSPHRASE"
  - "CLAUDE_CODE_DISABLE_MTLS_RELOAD_ON_STALE_CONNECTION"
  - "NODE_TLS_REJECT_UNAUTHORIZED"
  - "CLAUDE_CODE_OAUTH_SCOPES"
  - "--debug"
  - "--debug-file"
  - "/status"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "network-config"
    resource: "https://code.claude.com/docs/en/network-config"
    title: "Enterprise network configuration"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Enterprise network settings, all via environment variables (also settable in `settings.json`). Shell variables are read once at startup.

# How to use it

- Proxy: `HTTPS_PROXY` (recommended) or `HTTP_PROXY`; lowercase variants work, first set wins in order `https_proxy`, `HTTPS_PROXY`, `http_proxy`, `HTTP_PROXY`. `NO_PROXY` takes space or comma lists, or `*` for all. Basic auth via `http://user:pass@host:port`. WebSocket traffic to `localhost`, `::1`, `127.0.0.0/8` never uses the proxy. SOCKS proxies are not supported; for NTLM or Kerberos use an LLM gateway. Remote MCP sign-in requests also use these variables; for `claude mcp login` set them in shell, user settings or managed settings, not project/local.
- Startup check: an unparseable proxy URL (e.g. missing `http://`) stops launch naming the variable; from v2.1.327 non-terminal starts (Claude Desktop, SDK, cron) proceed on a scheme-less `HTTPS_PROXY`, but write full URLs.
- CA store: default trusts bundled Mozilla CAs plus the OS store (native installer always; npm installs need Node 22.15+). `CLAUDE_CODE_CERT_STORE` = comma list of `bundled`, `system` (default `bundled,system`); no settings schema key, use the `env` block. `NODE_EXTRA_CA_CERTS=/path/ca.pem` adds a CA (two documented warnings appear if the file is partly or wholly unreadable). `CLAUDE_CODE_GZIP_REQUEST_BODIES=0` turns off gzip for Claude API, telemetry and artifact publish requests if a TLS-inspecting proxy mishandles it.
- mTLS: `CLAUDE_CODE_CLIENT_CERT`, `CLAUDE_CODE_CLIENT_KEY`, optional `CLAUDE_CODE_CLIENT_KEY_PASSPHRASE`. Files are read at startup and re-read whenever settings apply; replace files at the same paths to rotate. After a connection-level failure (reset, TLS handshake error) it re-reads and retries (before v2.1.232 it did not). No re-read when the gateway completes TLS and returns an HTTP error. Half-written rotations keep the old pair. OTLP exporters keep the first-loaded certificate, so restart for them. `CLAUDE_CODE_DISABLE_MTLS_RELOAD_ON_STALE_CONNECTION=1` disables the re-read. Debug log line: `Stale connection — reloaded rotated mTLS client material`.
- Verify: `claude --debug` (log in `~/.claude/debug/<session-id>.txt` or `--debug-file <path>`) shows `CA certs: Appended extra certificates ...`, `mTLS: Loaded client certificate ...`; `/status` rows Proxy, mTLS client cert, mTLS client key, Additional CA cert(s).

# Limits and defaults

- Cloud sessions ignore `CLAUDE_CODE_CLIENT_CERT`, `CLAUDE_CODE_CLIENT_KEY`, `CLAUDE_CODE_CLIENT_KEY_PASSPHRASE`, `NODE_EXTRA_CA_CERTS`, `NODE_TLS_REJECT_UNAUTHORIZED`, `CLAUDE_CODE_OAUTH_SCOPES` from settings `env` blocks.
- Claude Desktop sessions where the app manages the provider connection read these (except `CLAUDE_CODE_OAUTH_SCOPES`) and the proxy variables only from managed settings and `~/.claude/settings.json` (before v2.1.217 they were ignored in every settings file). A variable already set in the launch environment wins over the settings file value.
