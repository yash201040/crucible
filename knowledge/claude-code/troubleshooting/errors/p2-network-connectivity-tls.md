---
type: "Reference"
title: "Connection, streaming, proxy and TLS errors"
description: "Errors from failed connections, dropped sockets, malformed gateway responses, Bedrock content-type checks and TLS interception."
resource: "https://code.claude.com/docs/en/errors"
tags: [errors, network, proxy, tls, gateway]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "HTTPS_PROXY"
  - "NO_PROXY"
  - "ANTHROPIC_BASE_URL"
  - "NODE_EXTRA_CA_CERTS"
  - "NODE_TLS_REJECT_UNAUTHORIZED"
  - "CLAUDE_CODE_DISABLE_NONSTREAMING_FALLBACK"
  - "CLAUDE_CODE_DISABLE_BEDROCK_CONTENT_TYPE_GUARD"
  - "ENABLE_TOOL_SEARCH"
  - "claude update"
  - "claude doctor"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Network-layer failures between Claude Code and the API, a proxy or an LLM gateway.

# How to use it

| Message | Cause and fix |
|---|---|
| `Unable to connect to API` family (`ConnectionRefused`/`ECONNREFUSED`, `ENOTFOUND`/`FailedToOpenSocket`, `EHOSTUNREACH`, `ERR_PROXY_TUNNEL`, `ECONNRESET`, `Request timed out`) | TCP failure. Test with `curl -I https://api.anthropic.com`; set `HTTPS_PROXY`; a leftover `ANTHROPIC_BASE_URL` pointing at a dead gateway gives Connection refused. Intermittent failures are retried automatically. Before v2.1.227 the code was appended to a generic message. Behind a gateway, endless `Connection dropped` can mean the gateway rejects tool search fields (`defer_loading`, `tool_reference`); default since v2.1.304, before that `ENABLE_TOOL_SEARCH`. |
| `Unable to connect to Anthropic services` | First-run check of `api.anthropic.com` and `platform.claude.com`, 10 second probe each. Skipped when managed settings set `forceLoginMethod` `"gateway"` or `forceLoginGatewayUrl` (v2.1.247+), or when user settings name a gateway (v2.1.295+). |
| `Socket is closed` | Streaming connection closed mid-response, often a Windows corporate proxy. Retried since v2.1.214. |
| `API returned an empty or malformed response (HTTP 200)` | The non-streaming retry got a non-API body (HTML, empty). Not retried. `CLAUDE_CODE_DISABLE_NONSTREAMING_FALLBACK=1` turns off the fallback except when streaming returns 404. |
| `Streaming response ended before any complete data was received` | Warned once per session, interactive only (silent before v2.1.239). Each affected request is sent twice. |
| `Bedrock streaming response has content-type ...; expected "application/vnd.amazon.eventstream"` | Gateway rewrote the stream. Not retried. `CLAUDE_CODE_DISABLE_BEDROCK_CONTENT_TYPE_GUARD=1` hides it but forces slower non-streaming. |
| SSL certificate errors (`UNABLE_TO_GET_ISSUER_CERT_LOCALLY`, `SELF_SIGNED_CERT_IN_CHAIN`) | TLS-inspecting proxy. Set `NODE_EXTRA_CA_CERTS=/path/to/ca-bundle.pem`; never `NODE_TLS_REJECT_UNAUTHORIZED=0`. Not retried since v2.1.199. |
| `The proxy refused the connection` (artifact fetch, HTTP 407/403/502) | CONNECT to `*.frame.claudeusercontent.com` refused; add `.frame.claudeusercontent.com` to `NO_PROXY` (not the broader `.claudeusercontent.com`). |

# Notes

The Bedrock-specific guard and gateway notes are in the Amazon Bedrock docs.
