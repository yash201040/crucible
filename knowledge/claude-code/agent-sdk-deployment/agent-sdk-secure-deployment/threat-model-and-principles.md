---
type: "Concept"
title: "Agent deployment threat model and security principles"
description: "Prompt injection and model error as the threat, built-in features, and the boundary, least-privilege and defense-in-depth principles."
resource: "https://code.claude.com/docs/en/agent-sdk/secure-deployment"
tags: [security, threat-model, least-privilege, prompt-injection, agent-sdk]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, sdk]
requires: ""
identifiers: []
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-secure-deployment"
    resource: "https://code.claude.com/docs/en/agent-sdk/secure-deployment"
    title: "Securely deploying AI agents"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Agents can take unintended actions through prompt injection (instructions inside files, webpages or user input) or model error; defense in depth is good practice even though Claude models are designed to resist it.

Built-in features: permission rules (run, block or ask), critical-path removal gate (in `default` mode an `rm` or `rmdir` recognized as removing the working directory or another critical path needs approval, and an allow rule does not skip it; this is a gate, not a sandbox), web search summarization, and sandbox mode for Bash.

# How to use it

- Security boundary: keep sensitive resources (credentials) outside the boundary containing the agent.
- Least privilege table: filesystem (mount only needed directories, prefer read-only), network (restrict via proxy), credentials (inject via proxy), system capabilities (drop Linux capabilities).
- Defense in depth options: container isolation, network restrictions, filesystem controls, request validation at a proxy.
- In every configuration Claude Code or the SDK app runs inside the isolation boundary.
