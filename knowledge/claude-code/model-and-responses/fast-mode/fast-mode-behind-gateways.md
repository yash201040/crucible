---
type: "Guide"
title: "Fast mode behind proxies and LLM gateways"
description: "Claude Code checks fast mode availability directly at api.anthropic.com; skip variables fix gateway and proxy failures."
resource: "https://code.claude.com/docs/en/fast-mode"
tags: [fast-mode, gateway, proxy, troubleshooting]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless]
requires: ""
identifiers:
  - "CLAUDE_CODE_SKIP_FAST_MODE_NETWORK_ERRORS"
  - "CLAUDE_CODE_SKIP_FAST_MODE_ORG_CHECK"
  - "ANTHROPIC_BASE_URL"
  - "ANTHROPIC_API_KEY"
  - "ANTHROPIC_AUTH_TOKEN"
  - "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "fast-mode"
    resource: "https://code.claude.com/docs/en/fast-mode"
    title: "Speed up responses with fast mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Before offering fast mode on the Anthropic API, Claude Code checks the organization's availability with a request directly to `api.anthropic.com`. The check ignores `ANTHROPIC_BASE_URL` but uses a configured HTTP proxy.

# How to use it

| Message | Cause | Fix |
| - | - | - |
| Fast mode unavailable due to network connectivity issues | Check failed (for example direct egress blocked); requests run at standard speed. A past successful check stays cached, so mostly new installs are hit | Allowlist egress to `api.anthropic.com`, or `CLAUDE_CODE_SKIP_FAST_MODE_NETWORK_ERRORS=1` (failed check counts as available; a "disabled by your organization" response still honored) |
| Fast mode is currently unavailable | Gateway setups with no cached success: `ANTHROPIC_BASE_URL` plus a gateway-issued `ANTHROPIC_API_KEY` not in Anthropic key format, or `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` set (check skipped) | `CLAUDE_CODE_SKIP_FAST_MODE_NETWORK_ERRORS=1` |
| Fast mode has been disabled by your organization (despite being enabled) | Only `ANTHROPIC_AUTH_TOKEN` with no claude.ai login, API key or cached check; or a proxy (such as TLS inspection) answers with its own HTTP 200 page read as "disabled" | `CLAUDE_CODE_SKIP_FAST_MODE_ORG_CHECK=1` (skips the check entirely; the NETWORK_ERRORS variable does not apply) |

# Limits and defaults

The skip variables change only the client-side check. If the organization really has fast mode disabled, the API rejects fast requests regardless; Claude Code retries at standard speed, turns fast mode off and `/fast` reports it.
