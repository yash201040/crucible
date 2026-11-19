---
type: "Reference"
title: "Allowlist surface coverage"
description: "Which delivery mechanism (server-managed vs MDM/file) reaches which surface for availableModels enforcement."
resource: "https://code.claude.com/docs/en/model-config#surface-coverage"
tags: [managed-settings, allowlist, surfaces, cloud]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, ide, desktop, web, mobile, cloud, sdk]
requires: ""
identifiers:
  - "availableModels"
  - "apiKeyHelper"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "model-config"
    resource: "https://code.claude.com/docs/en/model-config"
    title: "Model configuration"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Every surface enforces the allowlist it receives; what differs is which delivery path reaches it.

# How to use it

| Delivery | CLI and IDE | Desktop local | Web, mobile, cloud | Agent SDK and non-interactive | Cowork |
| :- | :- | :- | :- | :- | :- |
| Server-managed settings (admin console) | Enforced | Enforced | Enforced, but not delivered to Claude Tag sessions or sessions on a self-hosted runner using Bedrock or Agent Platform | Enforced | Remote Cowork: server checks the model; on user's machine: not delivered |
| MDM or managed settings files | Enforced | Enforced | Not delivered in Anthropic-hosted environments; in self-hosted environments enforced from the runner image | Enforced | Enforced where deployed |

# Notes

- Cloud sessions (including those started from Desktop) run on Anthropic-managed VMs by default; device-deployed settings do not reach them, so use server-managed settings. Mid-session model switch in a cloud session is rejected if excluded; a non-empty server-managed `availableModels` makes the server reject starting a cloud session on an excluded model.
- Claude Tag sessions get no server-managed settings; in self-hosted environments they read the managed file in the runner image.
- Cowork does not receive server-managed settings; when the list is non-empty the server rejects an outside model for a remote Cowork session.
- Third-party providers (Bedrock, Agent Platform, Foundry, Claude Platform on AWS): deliver via MDM or managed files.
- Admin console delivery needs an eligible login or OAuth token for the organization; API-key fleets (including `apiKeyHelper`) must use MDM or managed files.
- Desktop SSH sessions read the managed file on the remote host.
- claude.ai and Desktop model pickers hide or grey excluded models, but that is convenience, not enforcement.
