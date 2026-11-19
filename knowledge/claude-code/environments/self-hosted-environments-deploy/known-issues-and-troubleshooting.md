---
type: "Guide"
title: "Known issues and troubleshooting"
description: "Connector traffic leaving the network, common runner and session failures with their log lines, and proxy problems with the SSE stream."
resource: "https://code.claude.com/docs/en/self-hosted-environments-deploy"
tags: [self-hosted, troubleshooting, proxy, errors, connectors]
kind: "behavior"
maturity: "beta"
since: ""
surfaces: [cloud]
requires: ""
identifiers:
  - "allowedMcpServers"
  - "deniedMcpServers"
  - "NODE_EXTRA_CA_CERTS"
  - "CLAUDE_CODE_OAUTH_TOKEN"
  - "[runner:fatal]"
  - "poll auth failed"
  - "RegisterRunner auth failed"
  - "cannot create or write to base directory"
  - "SSE connect failed"
  - "disableAllHooks"
  - "allowManagedHooksOnly"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "self-hosted-environments-deploy"
    resource: "https://code.claude.com/docs/en/self-hosted-environments-deploy"
    title: "Deploy self-hosted environments to production"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Diagnostic table for self-hosted runners. Issues are reported to your Anthropic account team.

# How to use it

| Symptom | Cause and action |
| :- | :- |
| Connector (GitHub, Slack, Linear) tools used in session | Anthropic calls them from its infrastructure via `api.anthropic.com`, not from your network. Filter with `allowedMcpServers`/`deniedMcpServers`; with a URL allowlist add `https://api.anthropic.com/v2/ccr-sessions/*`, `https://api.anthropic.com/v1/code/sessions/*`, `https://api.anthropic.com/v1/code/mcp/*`. Run local MCP servers to keep traffic inside. |
| `RegisterRunner failed:` or `poll failed:` with TLS error | Set `NODE_EXTRA_CA_CERTS` on runner/orchestrator (and spawn-runner runners); git needs `GIT_SSL_CAINFO` too. |
| Sessions stay queued | Runners locked to other owners; check `claude_code_self_hosted_runner_locked_account` or `locked_account` in `[runner:health]`; add replicas. |
| Start script write error `Resource temporarily unavailable` | Runner switches shared stdout/stderr pipe non-blocking; redirect output to a file. |
| Picked up but Claude never answers first message | Proxy buffers `GET https://api.anthropic.com/v1/code/sessions/<session-id>/worker/events/stream` (`text/event-stream`, open up to an hour, keep-alive at least every 15 s). Look for `SSE connect failed (no response in 30s)`, `SSE liveness timeout`, `SSE stream ended by server` after `no child output for ... — releasing` (default 15 min startup timeout; v2.1.287+). |
| Turn 401 | Runner fetches fresh `CLAUDE_CODE_OAUTH_TOKEN` and rotates it over session stdin; a wrapper severing stdin breaks it about 30 min in. |
| `The server has refused to renew this session's access to the model` | Token expired and renewal got HTTP 400; start a new session. |
| `This model needs a newer version of Claude Code` | Upgrade runners. |
| `couldn't find remote ref` | Branch missing; message reworded in v2.1.314, specific handling in v2.1.301. |
| Repository skipped (`could not access context source`, `could not read context source`) | Read-only repos can be skipped without a `checkout` hook (v2.1.274 and v2.1.311 changes). |
| Claude Tag not replying in Slack | Needs runner v2.1.229+, python3, and hooks not disabled (`disableAllHooks`, `allowManagedHooksOnly`, `strictPluginOnlyCustomization`). |
| Runner log `was paused or too slow` | Only newest 256 KiB per stream kept; see `--log-file`. |

# Notes

Malformed poll responses (`rejecting the malformed poll response`) are rejected from v2.1.246; earlier they read as an empty queue and could end sessions. Runner logs are plain text; lifecycle log to stdout, debug to stderr.
