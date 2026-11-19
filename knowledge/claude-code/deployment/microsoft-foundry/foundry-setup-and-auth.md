---
type: "Guide"
title: "Microsoft Foundry setup and authentication"
description: "Configure Claude Code on Microsoft Foundry with an API key, Entra ID or bearer token, resource name and RBAC roles; no setup wizard exists."
resource: "https://code.claude.com/docs/en/microsoft-foundry"
tags: [foundry, azure, auth, setup]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "Azure subscription with Microsoft Foundry access and Claude deployments"
identifiers:
  - "CLAUDE_CODE_USE_FOUNDRY"
  - "ANTHROPIC_FOUNDRY_RESOURCE"
  - "ANTHROPIC_FOUNDRY_BASE_URL"
  - "ANTHROPIC_FOUNDRY_API_KEY"
  - "ANTHROPIC_FOUNDRY_AUTH_TOKEN"
  - "az login"
  - "Foundry User"
  - "Cognitive Services User"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "microsoft-foundry"
    resource: "https://code.claude.com/docs/en/microsoft-foundry"
    title: "Claude Code on Microsoft Foundry"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Code connects to Claude deployments in a Microsoft Foundry resource. Unlike Bedrock and Google Cloud's Agent Platform, there is no interactive setup wizard; environment variables are the only path.

# How to use it

- Provision: in the Foundry portal create a resource and Claude Opus, Sonnet, Haiku deployments (note each deployment name; the hosting option decides Azure or Anthropic infrastructure). Select a specific model version, not "auto-update to latest".
- Auth (precedence: bearer token, then API key, then default chain): API key from **Endpoints and keys** in `ANTHROPIC_FOUNDRY_API_KEY`; Microsoft Entra ID via the Azure SDK default credential chain (leave key and token unset, e.g. `az login`); bearer token in `ANTHROPIC_FOUNDRY_AUTH_TOKEN` sent as `Authorization: Bearer` on every request.
- Enable: `CLAUDE_CODE_USE_FOUNDRY=1` plus `ANTHROPIC_FOUNDRY_RESOURCE` (resource name only; a URL or host name is refused when a message is sent) or `ANTHROPIC_FOUNDRY_BASE_URL=https://{resource}.services.ai.azure.com/anthropic`.
- Run `claude`; `/status` shows API provider `Microsoft Foundry` and resource or base URL.
- RBAC for Entra or bearer auth: `Foundry User` (formerly `Azure AI User`) or `Cognitive Services User` on the resource.

# Limits and defaults

`/logout` is unavailable. Troubleshooting: `Failed to get token from azureADTokenProvider: ChainedTokenCredential authentication failed` means configure Entra ID or set the API key; repeated connection errors on the first prompt mean `ANTHROPIC_FOUNDRY_RESOURCE` is a placeholder or wrong name.
