---
type: "Reference"
title: "Microsoft Foundry, Google Cloud and Vertex variables"
description: "Endpoint, project, workspace and credential variables for Microsoft Foundry, Claude Models on Google Cloud and Google Cloud's Agent Platform."
resource: "https://code.claude.com/docs/en/env-vars"
tags: [foundry, google-cloud, vertex, providers]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: "Microsoft Foundry or Google Cloud provider"
identifiers:
  - "ANTHROPIC_FOUNDRY_API_KEY"
  - "ANTHROPIC_FOUNDRY_AUTH_TOKEN"
  - "ANTHROPIC_FOUNDRY_BASE_URL"
  - "ANTHROPIC_FOUNDRY_RESOURCE"
  - "ANTHROPIC_GOOGLE_CLOUD_BASE_URL"
  - "ANTHROPIC_GOOGLE_CLOUD_LOCATION"
  - "ANTHROPIC_GOOGLE_CLOUD_PROJECT"
  - "ANTHROPIC_GOOGLE_CLOUD_WORKSPACE_ID"
  - "ANTHROPIC_VERTEX_BASE_URL"
  - "ANTHROPIC_VERTEX_PROJECT_ID"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "env-vars"
    resource: "https://code.claude.com/docs/en/env-vars"
    title: "Environment variables"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Provider-specific endpoint and credential variables. Per-model Vertex regions are in [Vertex region overrides](./vertex-region-overrides.md).

# How to use it

| Variable | What it does |
| :- | :- |
| `ANTHROPIC_FOUNDRY_API_KEY` | Foundry API key. |
| `ANTHROPIC_FOUNDRY_AUTH_TOKEN` | Bearer token (for example Entra access token) sent as `Authorization: Bearer`; beats the API key and the Azure default credential chain. Requires v2.1.203+. |
| `ANTHROPIC_FOUNDRY_BASE_URL` | Full Foundry resource URL, for example `https://my-resource.services.ai.azure.com/anthropic`; alternative to the resource name. |
| `ANTHROPIC_FOUNDRY_RESOURCE` | Foundry resource name (for example `my-resource`); a URL or host name is refused. Required if the base URL is unset. |
| `ANTHROPIC_GOOGLE_CLOUD_BASE_URL` | Override the Claude Models on Google Cloud endpoint (for example via an LLM gateway). |
| `ANTHROPIC_GOOGLE_CLOUD_LOCATION` | Location put in the request URL; default `global`. |
| `ANTHROPIC_GOOGLE_CLOUD_PROJECT` | Google Cloud project ID. |
| `ANTHROPIC_GOOGLE_CLOUD_WORKSPACE_ID` | Workspace ID; required unless v2.1.307+ and `ANTHROPIC_GOOGLE_CLOUD_BASE_URL` is set. |
| `ANTHROPIC_VERTEX_BASE_URL` | Override the Google Cloud Agent Platform endpoint. |
| `ANTHROPIC_VERTEX_PROJECT_ID` | GCP project ID that requests are addressed to. |
