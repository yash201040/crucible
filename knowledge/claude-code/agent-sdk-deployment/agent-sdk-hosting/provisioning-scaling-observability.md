---
type: "Guide"
title: "Provisioning, scaling, auth and observability for hosted agents"
description: "Runtime dependencies, resource baseline, scaling formula, cost, OpenTelemetry environment variables and auth/secrets guidance."
resource: "https://code.claude.com/docs/en/agent-sdk/hosting"
tags: [agent-sdk, scaling, observability, otel, resources]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: "Python 3.10+ or Node.js 18.14+"
identifiers:
  - "CLAUDE_CODE_ENABLE_TELEMETRY"
  - "CLAUDE_CODE_ENHANCED_TELEMETRY_BETA"
  - "OTEL_TRACES_EXPORTER"
  - "OTEL_METRICS_EXPORTER"
  - "OTEL_LOGS_EXPORTER"
  - "OTEL_EXPORTER_OTLP_PROTOCOL"
  - "OTEL_EXPORTER_OTLP_ENDPOINT"
  - "ANTHROPIC_API_KEY"
  - "ANTHROPIC_BASE_URL"
  - "pathToClaudeCodeExecutable"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-hosting"
    resource: "https://code.claude.com/docs/en/agent-sdk/hosting"
    title: "Hosting the Agent SDK"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Production decisions for self-hosted SDK agents.

# How to use it

- Runtime: Python 3.10+ or Node.js 18.14+. Both SDKs bundle a native Claude Code binary for most installs (no separate Node.js for the CLI); the binary is pinned to the SDK package version, so updating the SDK updates the CLI. SDK follows semver: take patches continuously, read the changelog before a minor.
- Resources: starting point of 1 GiB RAM, 5 GiB disk, 1 CPU per agent, a floor not a ceiling; memory grows with session length and tool activity.
- Network: outbound HTTPS to `api.anthropic.com` (or Bedrock or Agent Platform regional endpoints) and any MCP or tool endpoints; use an egress proxy for allowlists, credential injection and logging. Inbound: expose HTTP or WebSocket on the container; put user authentication at a gateway in front.
- Observability: the SDK inherits OpenTelemetry config from the environment, so set at container level: `CLAUDE_CODE_ENABLE_TELEMETRY=1`, `OTEL_TRACES_EXPORTER=otlp`, `OTEL_METRICS_EXPORTER=otlp`, `OTEL_LOGS_EXPORTER=otlp`, `OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf`, `OTEL_EXPORTER_OTLP_ENDPOINT=http://collector.example.com:4318`. `CLAUDE_CODE_ENHANCED_TELEMETRY_BETA=1` is required only for traces. Prompt text and tool inputs are excluded by default.
- Auth: subprocess reads `ANTHROPIC_API_KEY` from its environment, or set `ANTHROPIC_BASE_URL` to a proxy that injects the key outside the container; keep tool credentials out of the agent environment.
- Scaling: `agents per host = (host RAM - overhead) / (per-session RAM ceiling)`, measure peak RSS for a representative session. For long-running sessions use a container pool behind a load balancer pinning each session by consistent hashing on `sessionId`.
- Cost: token cost typically dominates container cost by an order of magnitude or more; a minimal container is about $0.05 per hour while one long session can cost dollars.
