---
type: "Concept"
title: "Boolean and numeric value formats"
description: "How Claude Code parses on/off and numeric environment variables, including the variables where any non-empty value counts as on."
resource: "https://code.claude.com/docs/en/env-vars"
tags: [env, parsing, boolean, numbers]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.211"
surfaces: [cli]
requires: ""
identifiers: []
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "env-vars"
    resource: "https://code.claude.com/docs/en/env-vars"
    title: "Environment variables"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Conventions for variable values.

# How to use it

- On/off variables: `1`, `true`, `yes`, `on` turn a behavior on; `0`, `false`, `no`, `off` turn it off, any casing.
- Numeric variables (timeouts, token budgets, retry counts) accept scientific notation and digit separators: `2e3` reads as 2000, `64_000` as 64000. Exception: variables whose row says "plain digits only".
- Before v2.1.211 those spellings could silently set a much smaller value (for example `1e6` set a timeout to 1).
- Presence-only variables: any non-empty value, including `0`, turns the behavior on; unset or empty turns it off. These are `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`, `DISABLE_TELEMETRY`, `DISABLE_ERROR_REPORTING`, `CLAUDE_CODE_TMUX_TRUECOLOR` and `IS_DEMO`.

# Notes

Each variable's row states its own rule; some boolean-looking variables read plain digits only.
