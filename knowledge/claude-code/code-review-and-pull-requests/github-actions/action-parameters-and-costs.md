---
type: "Reference"
title: "Action inputs, CLI args, costs and troubleshooting"
description: "Common claude-code-action inputs, passing CLI args such as --max-turns, cost controls, beta-to-v1 migration, and fixes for non-responding or CI-less runs."
resource: "https://code.claude.com/docs/en/github-actions"
tags: [github-actions, parameters, cost, max-turns]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [headless, cloud]
requires: ""
identifiers:
  - "prompt"
  - "claude_args"
  - "anthropic_api_key"
  - "claude_code_oauth_token"
  - "github_token"
  - "plugin_marketplaces"
  - "plugins"
  - "settings"
  - "trigger_phrase"
  - "use_bedrock"
  - "use_vertex"
  - "use_foundry"
  - "--max-turns"
  - "--model"
  - "--mcp-config"
  - "--allowedTools"
  - "--allowed-tools"
  - "--debug"
  - "anthropics/claude-code-action@v1"
  - "mode"
  - "direct_prompt"
  - "custom_instructions"
  - "--append-system-prompt"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "github-actions"
    resource: "https://code.claude.com/docs/en/github-actions"
    title: "Claude Code GitHub Actions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Inputs map to `with:` keys of the `anthropics/claude-code-action@v1` step.

# How to use it

| Input | Description | Required |
| - | - | - |
| `prompt` | Instructions or skill invocation; omitted means respond to trigger phrase | No |
| `claude_args` | Any Claude Code CLI argument | No |
| `anthropic_api_key` | Claude API key (not used for Bedrock, Agent Platform, Foundry) | Unless OAuth token or federation |
| `claude_code_oauth_token` | Subscription token from `claude setup-token` | No |
| `github_token` | Token for GitHub operations; omitted means the Claude GitHub App | No |
| `plugin_marketplaces`, `plugins` | Newline-separated marketplace Git URLs and plugin names to install first | No |
| `settings` | Settings JSON string or path | No |
| `trigger_phrase` | Default `@claude` | No |
| `use_bedrock`, `use_vertex`, `use_foundry` | Route inference through a cloud provider | No |

Common `claude_args`: `--max-turns`, `--model` (default is Claude Code's default model), `--mcp-config`, `--allowedTools` (alias `--allowed-tools`), `--debug`. Example: `--max-turns 5 --model claude-sonnet-5 --mcp-config /path/to/config.json`.

# Limits and defaults

Cost drivers: GitHub Actions minutes on GitHub-hosted runners, and API tokens (OAuth token runs use the subscription instead of API billing). Controls: specific requests, issue templates, concise `CLAUDE.md`, `--max-turns`, workflow-level timeouts, GitHub concurrency controls.

# Notes

- Upgrade from beta: change `@beta` to `@v1`; remove `mode` (auto-detected); replace `direct_prompt` with `prompt`; move options like `max_turns` and `model` into `claude_args`; `custom_instructions` becomes `--append-system-prompt`.
- Not responding: confirm App installed, workflows enabled, secret set, `@claude` as a whole word (not `/claude` or `@claude-bot`), commenter write access.
- CI not running on Claude's commits: GitHub does not trigger workflows for commits made with the default `GITHUB_TOKEN`; remove `github_token: ${{ secrets.GITHUB_TOKEN }}` so it acts as the Claude GitHub App, or pass a custom app token; ensure CI triggers include `push` or `pull_request`.
- Org usage tracking: analytics dashboard and monitoring.
- Provider inputs and OIDC: see [cloud providers](../github-actions-cloud-providers/cloud-provider-oidc-setup.md).
