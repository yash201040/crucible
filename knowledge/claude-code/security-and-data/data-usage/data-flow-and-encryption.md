---
type: "Concept"
title: "Local and cloud data flow and encryption at rest"
description: "How data moves for local, cloud and Remote Control sessions, and encryption at rest per model provider."
resource: "https://code.claude.com/docs/en/data-usage"
tags: [data-flow, encryption, cloud-sessions, remote-control]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, cloud]
requires: ""
identifiers: []
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "data-usage"
    resource: "https://code.claude.com/docs/en/data-usage"
    title: "Data usage"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

- Local Claude Code runs locally and sends all prompts and model outputs over TLS 1.2+. Compatible with most VPNs and LLM proxies.
- Remote Control follows the local flow (execution on your machine), but the transcript is also stored on Anthropic servers while connected, to sync across devices.
- Anthropic-hosted cloud sessions: repo cloned into an isolated VM; Anthropic stores the transcript; GitHub credentials stay encrypted on Anthropic servers and never enter the VM (an Anthropic proxy attaches them); all outbound traffic goes through a security proxy for audit and abuse prevention. Self-hosted environments run on your infrastructure. Claude accesses only the repository where the session is started.

# Limits and defaults

| Provider | Encryption at rest |
| - | - |
| Anthropic API | Infrastructure-level AES-256; ZDR for no server-side persistence |
| Amazon Bedrock | AES-256 with AWS-managed keys; customer-managed keys via AWS KMS |
| Google Cloud's Agent Platform | Google-managed keys; CMEK available |
| Microsoft Foundry | Depends on hosting option; Hosted on Anthropic uses AES-256 disk encryption |
