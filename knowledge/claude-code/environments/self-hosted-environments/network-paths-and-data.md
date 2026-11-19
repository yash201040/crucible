---
type: "Concept"
title: "Network paths, proxies and data residency"
description: "All connections are outbound HTTPS to api.anthropic.com; proxy and mTLS variables are honored; conversation always leaves your network."
resource: "https://code.claude.com/docs/en/self-hosted-environments"
tags: [network, proxy, egress, data, security]
kind: "behavior"
maturity: "beta"
since: ""
surfaces: [cloud]
requires: "Self-hosted environments (Team or Enterprise)"
identifiers:
  - "HTTPS_PROXY"
  - "NO_PROXY"
  - "api.anthropic.com"
  - "Proxy-Authorization"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "self-hosted-environments"
    resource: "https://code.claude.com/docs/en/self-hosted-environments"
    title: "Self-hosted environments"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The connection model of a self-hosted environment. No inbound connectivity from Anthropic is required.

# How to use it

- Control plane: runner polls `api.anthropic.com` for work and posts setup-progress and failure events (polling is the heartbeat).
- Git: runner clones and pushes over HTTPS or SSH with credentials you provide; with the Anthropic git proxy, github.com git traffic goes through `api.anthropic.com`. With Anthropic-managed git the child opens a WebSocket to `api.anthropic.com` carrying `git` and `gh` traffic.
- Session child: holds the event stream and makes its own calls for model inference and git commands. Inference auth is an Anthropic-issued, session-scoped OAuth token; the API endpoint is delivered per session.
- Optional orchestrator SCM connector is not available (its tunnel does not open).
- Corporate egress proxies: runner and orchestrator honor the proxy and mTLS variables from the Network configuration page (`HTTPS_PROXY`, `NO_PROXY`) set in each process's environment; sessions inherit them. Session streaming uses server-sent events, so a proxy must not buffer responses. A proxy needing `Proxy-Authorization` can be handled by the runner.

# Limits and defaults

Stays on your infrastructure: repository checkouts, build artifacts, secrets, files sessions create. Goes to Anthropic: the conversation, even when inference goes to Bedrock or Agent Platform.
