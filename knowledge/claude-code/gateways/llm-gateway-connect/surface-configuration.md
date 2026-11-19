---
type: "Reference"
title: "Gateway configuration per surface"
description: "How gateway variables reach VS Code, Desktop, GitHub Actions, the Agent SDK, Slack and cloud sessions, Remote Control and voice dictation."
resource: "https://code.claude.com/docs/en/llm-gateway-connect"
tags: [gateway, sdk, github-actions, vscode, desktop]
kind: "mixed"
maturity: "beta"
since: ""
surfaces: [cli, ide, desktop, sdk, cloud]
requires: ""
identifiers:
  - "claudeCode.environmentVariables"
  - "ANTHROPIC_CUSTOM_HEADERS"
  - "anthropic_api_key"
  - "CLAUDE_CODE_OAUTH_TOKEN"
  - "options.env"
  - "ClaudeAgentOptions(env=...)"
  - "sshHostAllowlist"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "llm-gateway-connect"
    resource: "https://code.claude.com/docs/en/llm-gateway-connect"
    title: "Connect Claude Code to an LLM gateway"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The CLI reads environment variables and settings files. Other surfaces differ. The beta label applies only to SSH sessions in the desktop app with a gateway configuration.

# How to use it

| Surface | How the gateway is configured |
| - | - |
| VS Code extension | `claudeCode.environmentVariables` in VS Code user settings (array of `{name, value}`). The extension checks credentials from this setting before launch; values in `~/.claude/settings.json` reach the spawned process but not the extension's login check. |
| Desktop app | Reads its third-party inference configuration, not `ANTHROPIC_BASE_URL` or `settings.json`. Admin-distributed config makes the local form (Help, Troubleshooting, Enable Developer Mode, Developer, Configure Third-Party Inference) read-only. With a gateway active, Anthropic-hosted cloud environments are not offered and Remote Control is unavailable. |
| Desktop SSH sessions | Beta with a gateway configuration; requires Claude Desktop v1.40609.0 or later; off by default until hosts are listed in `sshHostAllowlist`; a gateway at `localhost` on the user's computer does not work because the remote machine connects to it. |
| GitHub Actions | Reads `ANTHROPIC_BASE_URL` and `ANTHROPIC_CUSTOM_HEADERS` from workflow `env`. Credential goes in the action's `anthropic_api_key` input (becomes `ANTHROPIC_API_KEY`, sent as `x-api-key`). For a bearer-token gateway also set `ANTHROPIC_AUTH_TOKEN` in `env`; the action does not read it and needs `anthropic_api_key`, `CLAUDE_CODE_OAUTH_TOKEN` or workload identity federation to launch. Action: `anthropics/claude-code-action@v1`. |
| Agent SDK | No gateway-specific options; passes env to the spawned Claude Code process. TypeScript: `options.env` replaces the whole environment, so spread `process.env`. Python: `ClaudeAgentOptions(env=...)` merges on top of the inherited environment. |
| Slack, cloud sessions | Not part of a gateway deployment; gateway variables in a cloud session's environment configuration are not applied. Do not enable them if traffic must stay on the gateway. |
| Remote Control, voice dictation | Both need a claude.ai identity. Unavailable while `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN` or an `apiKeyHelper` is active; Remote Control also disabled while `ANTHROPIC_BASE_URL` points at a non-Anthropic host. `claude doctor` names what blocks Remote Control. |

# Notes

Desktop shows `Gateway was unreachable` when the base URL cannot be reached at startup.
