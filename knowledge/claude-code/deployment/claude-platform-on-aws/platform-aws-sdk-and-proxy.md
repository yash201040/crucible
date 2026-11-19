---
type: "Feature"
title: "Claude Platform on AWS with Agent SDK and gateways"
description: "The Agent SDK reads the same provider variables as the CLI, and ANTHROPIC_AWS_BASE_URL routes through a proxy or gateway that may sign requests itself."
resource: "https://code.claude.com/docs/en/claude-platform-on-aws"
tags: [aws, agent-sdk, gateway, proxy]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [sdk, headless, cli]
requires: "Claude Platform on AWS"
identifiers:
  - "CLAUDE_CODE_SKIP_ANTHROPIC_AWS_AUTH"
  - "ANTHROPIC_AWS_BASE_URL"
  - "ANTHROPIC_AUTH_TOKEN"
  - "CLAUDE_CODE_USE_ANTHROPIC_AWS"
  - "ANTHROPIC_AWS_WORKSPACE_ID"
  - "ANTHROPIC_AWS_API_KEY"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "claude-platform-on-aws"
    resource: "https://code.claude.com/docs/en/claude-platform-on-aws"
    title: "Claude Code on Claude Platform on AWS"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Any program that spawns the Claude Code subprocess through the Agent SDK can target Claude Platform on AWS by exporting the same variables as the CLI before the call.

# How to use it

- SDK: set `process.env.CLAUDE_CODE_USE_ANTHROPIC_AWS = "1"`, `ANTHROPIC_AWS_WORKSPACE_ID`, `AWS_REGION`, then `query({ prompt })` from `@anthropic-ai/claude-agent-sdk`. Ambient AWS credential chain gives SigV4; set `ANTHROPIC_AWS_API_KEY` for a workspace key.
- Proxy or LLM gateway: set `ANTHROPIC_AWS_BASE_URL` to the proxy address; Claude Code sends the same workspace and auth headers, so any gateway that forwards them unchanged works.
- Gateway that signs requests itself: `CLAUDE_CODE_SKIP_ANTHROPIC_AWS_AUTH=1` sends unsigned requests so the gateway adds SigV4 before forwarding. If the gateway needs its own token, put it in `ANTHROPIC_AUTH_TOKEN`.
