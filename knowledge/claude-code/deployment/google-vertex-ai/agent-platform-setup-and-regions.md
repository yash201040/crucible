---
type: "Guide"
title: "Google Cloud Agent Platform setup and regions"
description: "Configure Claude Code on Google Cloud's Agent Platform (formerly Vertex AI): wizard, credentials, gcpAuthRefresh, region variables and verification."
resource: "https://code.claude.com/docs/en/google-vertex-ai"
tags: [vertex-ai, google-cloud, setup, region]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "GCP project with Agent Platform API enabled and Claude model access in Model Garden"
identifiers:
  - "CLAUDE_CODE_USE_VERTEX"
  - "CLOUD_ML_REGION"
  - "ANTHROPIC_VERTEX_PROJECT_ID"
  - "ANTHROPIC_VERTEX_BASE_URL"
  - "VERTEX_REGION_CLAUDE_HAIKU_4_5"
  - "VERTEX_REGION_CLAUDE_4_6_SONNET"
  - "VERTEX_REGION_CLAUDE_*"
  - "GOOGLE_APPLICATION_CREDENTIALS"
  - "gcpAuthRefresh"
  - "ENABLE_TOOL_SEARCH"
  - "DISABLE_PROMPT_CACHING"
  - "ENABLE_PROMPT_CACHING_1H"
  - "/setup-vertex"
  - "aiplatform.googleapis.com"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "google-vertex-ai"
    resource: "https://code.claude.com/docs/en/google-vertex-ai"
    title: "Claude Code on Google Cloud's Agent Platform"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

This page covers the Google-managed route (distinct from Claude Models on Google Cloud, Anthropic managed).

# How to use it

- Wizard: `claude` > **3rd-party platform** > **Google Vertex AI** (the label still used), or `/login`; `/setup-vertex` reopens it later. Choices: Application Default Credentials, service account key file, or ambient credentials; asks project and region, verifies models, lets you pin; writes the `env` block of `~/.claude/settings.json` (or `$CLAUDE_CONFIG_DIR/settings.json`).
- Manual: `gcloud services enable aiplatform.googleapis.com`; request Claude model access in Model Garden (may take 24-48 hours); then `CLAUDE_CODE_USE_VERTEX=1`, `CLOUD_ML_REGION` (`global`, multi-region `eu`/`us`, or a region like `us-east5`), `ANTHROPIC_VERTEX_PROJECT_ID`, optional `ANTHROPIC_VERTEX_BASE_URL`. With `global`, models lacking global endpoints need a per-model `VERTEX_REGION_CLAUDE_*` variable (e.g. `VERTEX_REGION_CLAUDE_HAIKU_4_5=us-east5`).
- Requests go to the project in `ANTHROPIC_VERTEX_PROJECT_ID` even if `GCLOUD_PROJECT`, `GOOGLE_CLOUD_PROJECT` or the credential file name another. X.509 Workload Identity Federation works via `GOOGLE_APPLICATION_CREDENTIALS`.
- `gcpAuthRefresh` setting (e.g. `gcloud auth application-default login`): runs when credentials are expired or can't load, after a token check; if the check exceeds 5 seconds it is skipped until a request fails with a credential error (before v2.1.261 a timeout counted as expired). Shows output but no interactive input; times out after 3 minutes. In project settings it falls under the same workspace-trust rule as hooks, including `-p` sessions in untrusted folders.
- Verify with `/status`: `API provider` shows `Google Vertex AI`; also `GCP project`, `Default region`, `Model`.

# Limits and defaults

- Invalid region values (slash, dot, space) count as unset: `VERTEX_REGION_CLAUDE_*` falls back to `CLOUD_ML_REGION`; `CLOUD_ML_REGION` falls back to `us-east5`.
- `/logout` unavailable. Rate limits via Google Cloud support.
- MCP tool search on by default for Opus 4.5, Sonnet 4.5, Haiku 4.5 and later; earlier models load tool definitions upfront (they reject the beta header) and `ENABLE_TOOL_SEARCH=true` does not override that. `ENABLE_TOOL_SEARCH=false` disables it everywhere.
- Prompt caching automatic; `DISABLE_PROMPT_CACHING=1` disables; `ENABLE_PROMPT_CACHING_1H=1` requests 1-hour TTL (billed higher).
