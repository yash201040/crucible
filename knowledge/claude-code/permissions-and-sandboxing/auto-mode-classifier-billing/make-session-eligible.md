---
type: "Feature"
title: "Make the session eligible (CLAUDE_CODE_AUTO_MODE_SERVER)"
description: "Gateway pass-through requirements for server-side classifier checks and the temporary CLAUDE_CODE_AUTO_MODE_SERVER=0 opt-out."
resource: "https://code.claude.com/docs/en/auto-mode-classifier-billing#make-the-session-eligible"
tags: [auto-mode, gateway, env-var, classifier, billing]
kind: "env_var"
maturity: "unlabelled"
since: "2.1.281"
surfaces: [cli, headless]
requires: "CLAUDE_CODE_AUTO_MODE_SERVER on a direct Anthropic API connection needs v2.1.281+"
identifiers:
  - "CLAUDE_CODE_AUTO_MODE_SERVER"
  - "CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS"
  - "anthropic-beta"
  - "anthropic_beta"
  - "safeguards"
  - "safeguard_results"
  - "env"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "auto-mode-classifier-billing"
    resource: "https://code.claude.com/docs/en/auto-mode-classifier-billing"
    title: "Auto mode classifier request charges"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

What an LLM gateway must pass through for the server's classifier checks to work, and a switch to tell Claude Code not to request them.

# How to use it

Gateway requirements (where the upstream accepts the format the gateway receives, the gateway passes requests and responses through unchanged):
- Requests: forward both the `anthropic-beta` header and the `safeguards` body field unchanged (they travel as a pair). On the Amazon Bedrock InvokeModel format, forward the `anthropic_beta` body field instead of the header.
- Responses: return responses and streaming events without dropping fields or rewriting tool-use IDs; keep the `safeguard_results` field.

Once the gateway does this, new sessions use the server's checks again.

If the gateway cannot provide them, set `CLAUDE_CODE_AUTO_MODE_SERVER=0` before starting the session (shell export or the `env` settings key). Classifier requests are then always Claude Code's own, billed the same way, and the notice does not appear.

```bash
export CLAUDE_CODE_AUTO_MODE_SERVER=0
```

# Limits and defaults

- On a direct Anthropic API connection the variable needs Claude Code v2.1.281 or later.
- `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1` while `CLAUDE_CODE_AUTO_MODE_SERVER` is unset also turns the server's checks off, except as described in the gateway protocol doc's "Disable pre-release capabilities".
- `CLAUDE_CODE_AUTO_MODE_SERVER` is a temporary setting and may be removed in a later release.
