---
type: "Limit"
title: "Thinking, effort and output token errors"
description: "Errors for thinking config mismatches by model version, effort above high with thinking off, thinking budget, and output token cutoffs."
resource: "https://code.claude.com/docs/en/errors"
tags: [errors, thinking, effort, output-tokens, versions]
kind: "limit"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk, desktop]
requires: ""
identifiers:
  - "MAX_THINKING_TOKENS"
  - "alwaysThinkingEnabled"
  - "CLAUDE_CODE_MAX_OUTPUT_TOKENS"
  - "/effort"
  - "--effort"
  - "effortLevel"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Errors tied to thinking, effort and the output token ceiling.

# How to use it

| Error | Detail |
|---|---|
| `thinking.type.enabled is not supported for this model` | Claude Code too old for the model. Minimum CLI versions: Opus 4.7 v2.1.111; Opus 4.8 v2.1.154; Sonnet 5 v2.1.197; Opus 5 v2.1.219; Opus 5.5 v2.1.280; Sonnet 5.5 v2.1.284. SDK minimums: TypeScript Opus 4.8 v0.3.154, Sonnet 5 v0.3.197, Opus 5 v0.3.219, Opus 5.5 v0.3.280, Sonnet 5.5 v0.3.284; Python Opus 4.8 v0.2.88. Fallback: Opus 4.6 or Sonnet 4.6. The stable channel may lag. |
| `Effort 'xhigh' isn't available with thinking turned off` | Effort above `high` with thinking off (`MAX_THINKING_TOKENS=0` or `alwaysThinkingEnabled: false`). Lower to `high` (`/effort high`, `--effort high`, `effortLevel`) or turn thinking on. Claude Code sends `high` itself to models known to reject it, like Opus 5 (v2.1.251+); custom message since v2.1.242. |
| `max_tokens must be greater than thinking.budget_tokens` | Raise `CLAUDE_CODE_MAX_OUTPUT_TOKENS` above the thinking budget. |
| `Claude's response exceeded the ... output token maximum` | Reply cut off. A request re-sent without streaming is capped at 64,000 output tokens, which `CLAUDE_CODE_MAX_OUTPUT_TOKENS` cannot raise; before v2.1.299 such cutoffs ended silently as complete. In an interactive session reply `continue`. |

# Notes

Ask for output in smaller pieces (one file or section per reply) to stay under the cap.
