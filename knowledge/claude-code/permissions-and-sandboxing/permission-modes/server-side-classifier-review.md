---
type: "Feature"
title: "Server-side classifier review"
description: "Auto mode can have the server review actions inside the session's model requests, with version gates, fallbacks and the CLAUDE_CODE_AUTO_MODE_SERVER switch."
resource: "https://code.claude.com/docs/en/permission-modes"
tags: [auto-mode, classifier, server-side, gateway, env-var]
kind: "env_var"
maturity: "unlabelled"
since: "2.1.271"
surfaces: [cli, headless, sdk, ide, desktop, cloud]
requires: ""
identifiers:
  - "CLAUDE_CODE_AUTO_MODE_SERVER"
  - "CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS"
  - "ANTHROPIC_BASE_URL"
  - "/status"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permission-modes"
    resource: "https://code.claude.com/docs/en/permission-modes"
    title: "Choose a permission mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Instead of sending its own classifier requests, Claude Code can ask the server to check, as part of the session's model requests, the actions that the decision order sends for review. When the server reviews, its verdicts decide, and there are no separate classifier calls to count.

# How to use it

`CLAUDE_CODE_AUTO_MODE_SERVER=0` skips the server and always uses Claude Code's own classifier requests. On a direct Anthropic API connection the variable needs v2.1.281+; setting it to `1` there turns server review on in a session lacking it, unless `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1` is also set. With `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1` and the other variable unset, Claude Code also stops asking the server (except as described in the LLM gateway protocol docs). `/status` shows `Auto mode server` as `Enabled` or `Disabled`.

# Limits and defaults

Sessions that ask (as Anthropic rolls it out):
- Direct Anthropic API: interactive terminal needs v2.1.271+ on Pro, Max, Ultra, Team; v2.1.278+ on Enterprise and Claude API accounts. `-p` and VS Code need v2.1.278+. Agent SDK and desktop need v2.1.281+. From v2.1.282 a session that does not fetch feature flags (for example telemetry off) asks by default in any kind of session.
- Cloud provider or LLM gateway/proxy (Claude Platform on AWS, Bedrock, Agent Platform, Foundry, or `ANTHROPIC_BASE_URL` pointed at a gateway): asking by default needs v2.1.278+.
- Signed-in Claude apps gateway: v2.1.280+.
- Anthropic-hosted cloud sessions started with Cloud selected; cloud scheduled-task sessions as rolled out.

Outcomes: if the server does not review (no results, or says it does not; common with a gateway that drops the request or results, or an unsupported platform/region/credential), Claude Code falls back to its own classifier and shows a classifier-billing notice on accounts where those requests are billed. If the server gives no verdict for an action, Claude Code denies it (response ended early, unreadable results, or a check failure such as a timeout), and can stop the turn after ten responses in a row with no verdict. If a hook or mod changes an action's input after review, the action can be denied; the denial text includes `a hook changed this call's input after auto mode reviewed it` (interactive terminal/VS Code on a direct connection).
