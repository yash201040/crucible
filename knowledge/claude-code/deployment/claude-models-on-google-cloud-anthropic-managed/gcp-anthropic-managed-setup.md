---
type: "Guide"
title: "Claude Models on Google Cloud (Anthropic managed) setup"
description: "Configure Claude Code for the Anthropic-run Claude API reached through a Google Cloud project, with env variables, ADC and model pinning."
resource: "https://code.claude.com/docs/en/claude-models-on-google-cloud-anthropic-managed"
tags: [google-cloud, anthropic-managed, setup, env-vars]
kind: "env_var"
maturity: "unlabelled"
since: "2.1.307"
surfaces: [cli, headless]
requires: "Claude Code v2.1.307 or later; Google Cloud project with account setup, roles/claude.user"
identifiers:
  - "CLAUDE_CODE_USE_ANTHROPIC_GOOGLE_CLOUD"
  - "ANTHROPIC_GOOGLE_CLOUD_PROJECT"
  - "ANTHROPIC_GOOGLE_CLOUD_WORKSPACE_ID"
  - "ANTHROPIC_GOOGLE_CLOUD_LOCATION"
  - "ANTHROPIC_GOOGLE_CLOUD_BASE_URL"
  - "CLAUDE_CODE_SKIP_ANTHROPIC_GOOGLE_CLOUD_AUTH"
  - "GOOGLE_APPLICATION_CREDENTIALS"
  - "GOOGLE_CLOUD_PROJECT"
  - "ANTHROPIC_DEFAULT_OPUS_MODEL"
  - "ANTHROPIC_DEFAULT_SONNET_MODEL"
  - "ANTHROPIC_DEFAULT_FABLE_MODEL"
  - "ANTHROPIC_DEFAULT_HAIKU_MODEL"
  - "claude auth status --text"
  - "roles/claude.user"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "claude-models-on-google-cloud-anthropic-managed"
    resource: "https://code.claude.com/docs/en/claude-models-on-google-cloud-anthropic-managed"
    title: "Claude Code with Claude Models on Google Cloud (Anthropic managed)"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Models on Google Cloud (Anthropic managed) is the Claude API run by Anthropic and reached through your Google Cloud project. It is distinct from Google Cloud's Agent Platform (formerly Vertex AI, Google managed). No Anthropic account login or logout is needed.

# How to use it

1. Create Application Default Credentials: `gcloud auth application-default login` (unset `GOOGLE_APPLICATION_CREDENTIALS` first, otherwise that file wins), or set `GOOGLE_APPLICATION_CREDENTIALS` to a service account key file in the shell or CI job.
2. Add to the `env` block of `~/.claude/settings.json`: `CLAUDE_CODE_USE_ANTHROPIC_GOOGLE_CLOUD=1`, `ANTHROPIC_GOOGLE_CLOUD_PROJECT`, `ANTHROPIC_GOOGLE_CLOUD_WORKSPACE_ID` (starts with `wrkspc_`). The same variables work per shell or CI job.
3. Verify: `/status` shows `API provider` containing `on Google Cloud`, plus `Workspace ID`, `GCP project`, `GCP location`; from a shell or CI use `claude auth status --text`; or `claude -p "hello"`.
- Team rollout: put the `env` block in managed settings on each machine, grant `roles/claude.user` on the project, each developer runs ADC login.
- Pin models in the same `env` block (example values `claude-opus-5-5`, `claude-sonnet-5-5`, `claude-fable-5-1`, `claude-haiku-4-5-20251001`) using the Claude API model IDs.

| Variable | Required | Meaning |
|---|---|---|
| `CLAUDE_CODE_USE_ANTHROPIC_GOOGLE_CLOUD` | yes | `1` routes requests here |
| `ANTHROPIC_GOOGLE_CLOUD_WORKSPACE_ID` | yes unless base URL set | workspace ID |
| `ANTHROPIC_GOOGLE_CLOUD_PROJECT` | recommended | project ID; falls back to `GOOGLE_CLOUD_PROJECT` |
| `ANTHROPIC_GOOGLE_CLOUD_LOCATION` | no | default `global` |
| `ANTHROPIC_GOOGLE_CLOUD_BASE_URL` | no | replaces built base URL (e.g. LLM gateway); API path such as `/v1/messages` appended |
| `CLAUDE_CODE_SKIP_ANTHROPIC_GOOGLE_CLOUD_AUTH` | no | `1` when a gateway attaches Google credentials; Claude Code sends no Google token |

# Limits and defaults

Not available: fast mode (`/fast`, `fastMode`), Remote Control and cloud sessions, claude.ai MCP connectors, Channels, `/design-sync` and `/import`, server-managed settings (use managed settings files instead).

# Notes

Troubleshooting: if login is requested or `/status` lacks `on Google Cloud`, check the variable, version 2.1.307+, and remove `CLAUDE_CODE_USE_BEDROCK`, `CLAUDE_CODE_USE_FOUNDRY`, `CLAUDE_CODE_USE_ANTHROPIC_AWS` (`CLAUDE_CODE_USE_VERTEX` may stay). Error messages: `No workspace ID found`, `No project was given`, `Could not load Google Cloud credentials`, `Google Cloud credentials expired or invalid`, `Google Cloud authentication failed` (check project, workspace, `roles/claude.user` or `roles/claude.admin`, and that `claude.googleapis.com` is enabled).
