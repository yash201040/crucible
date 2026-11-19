---
type: "Guide"
title: "Credential management with the proxy pattern"
description: "Run a proxy outside the agent boundary to inject credentials, via ANTHROPIC_BASE_URL or HTTP_PROXY/HTTPS_PROXY, custom tools, or TLS-terminating traffic forwarding."
resource: "https://code.claude.com/docs/en/agent-sdk/secure-deployment"
tags: [credentials, proxy, anthropic-base-url, tls, secrets]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [sdk, cli]
requires: ""
identifiers:
  - "ANTHROPIC_BASE_URL"
  - "HTTP_PROXY"
  - "HTTPS_PROXY"
  - "NODE_USE_ENV_PROXY"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-secure-deployment"
    resource: "https://code.claude.com/docs/en/agent-sdk/secure-deployment"
    title: "Securely deploying AI agents"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The recommended approach: a proxy outside the agent's security boundary injects credentials into outgoing requests. The agent never sees them; the proxy can enforce an endpoint allowlist, log requests, and keep credentials in one place.

# How to use it

| Method | Behavior |
| - | - |
| `ANTHROPIC_BASE_URL="http://localhost:8080"` | Sampling API requests only; proxy receives plaintext HTTP and can inspect, modify and add credentials |
| `HTTP_PROXY` / `HTTPS_PROXY` | System-wide for Claude Code and the SDK; HTTPS becomes an opaque CONNECT tunnel unless TLS is intercepted |
| Custom tool or MCP server | Tool calls a service or proxy outside the boundary that holds credentials (e.g. a git MCP server forwarding to a host git proxy); no TLS interception needed |
| Traffic forwarding | A TLS-terminating proxy outside the container, its CA certificate in the agent trust store, and proxy variables set; handles any HTTP service |

Proxy options named: Envoy (`credential_injector` filter), mitmproxy (TLS-terminating), Squid, LiteLLM (credential injection and rate limiting).

# Limits and defaults

Not every program respects proxy variables: curl, pip, npm and git do; Node.js `fetch()` ignores them by default (Node 24+ supports `NODE_USE_ENV_PROXY=1`). For stubborn tools use proxychains or iptables redirection to a transparent proxy (still needs the TLS-terminating proxy and trusted CA).
