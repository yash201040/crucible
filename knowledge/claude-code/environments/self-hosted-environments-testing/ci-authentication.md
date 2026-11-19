---
type: "Limit"
title: "Authenticating dispatch commands from CI"
description: "claude -p --environment and --cloud need a claude.ai OAuth token with a 30-day cap; API keys, setup-token and environment secrets do not work."
resource: "https://code.claude.com/docs/en/self-hosted-environments-testing"
tags: [self-hosted, ci, authentication, oauth, limits]
kind: "limit"
maturity: "beta"
since: ""
surfaces: [cli, headless]
requires: "claude.ai account"
identifiers:
  - "claude auth login"
  - "claude setup-token"
  - "user:sessions:claude_code"
  - "~/.claude/.credentials.json"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "self-hosted-environments-testing"
    resource: "https://code.claude.com/docs/en/self-hosted-environments-testing"
    title: "Test self-hosted environments end to end"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Both `claude -p ... --environment` and `claude -p ... --cloud` authenticate only with a claude.ai OAuth token. API keys such as `sk-ant-xxxxx` are not accepted.

# How to use it

Long-lived CI host: run `claude auth login` interactively once on the machine, using a dedicated automation account. Token is stored in the OS keychain on macOS, or `~/.claude/.credentials.json` on Linux and Windows (also on macOS when the Keychain cannot be written, e.g. an SSH session with a locked login Keychain). The CLI refreshes the access token on each invocation.

# Limits and defaults

- The refresh grant is capped at 30 days from initial login: re-run `claude auth login` every 30 days.
- Ephemeral CI runners: no long-lived token exists. The `user:sessions:claude_code` scope is capped server-side at 30 days; `claude setup-token` (one-year, inference-only) does not cover it; the environment secret only authorizes runner registration, not creating sessions. Run `claude -p` from a long-lived CI host; ask the Anthropic account team about a machine-identity path.
