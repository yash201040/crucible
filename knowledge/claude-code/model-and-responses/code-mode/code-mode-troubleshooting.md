---
type: "Reference"
title: "Code Mode troubleshooting"
description: "Reasons Code Mode does not start with fixes, and the hook-failure errors that refuse tool calls."
resource: "https://code.claude.com/docs/en/code-mode"
tags: [code-mode, troubleshooting, hooks, errors]
kind: "mixed"
maturity: "experimental"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "apiKeyHelper"
  - "ANTHROPIC_AUTH_TOKEN"
  - "ANTHROPIC_CUSTOM_HEADERS"
  - "ANTHROPIC_API_KEY"
  - "CLAUDE_CODE_ENABLE_TELEMETRY"
  - "ENABLE_BETA_TRACING_DETAILED"
  - "--remote-control"
  - "/plugin"
  - "onFailure"
  - "the hook failed"
  - "the hook did not finish"
  - "~/.claude.json"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "code-mode"
    resource: "https://code.claude.com/docs/en/code-mode"
    title: "Run tool calls from code with Code Mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

When Claude Code starts without Code Mode it prints `Code Mode (experimental) isn't available` plus a reason (also in `/status`). Fix, then start a new session.

# How to use it

| Reason includes | Fix |
| - | - |
| `it isn't open to your account in this version` / `yet` | Update if older than v2.1.323; else check network and retry later |
| `it only works directly with the Anthropic API` | Remove settings routing via a cloud provider, gateway or custom `ANTHROPIC_BASE_URL` |
| `it doesn't work with an API key helper` | Remove `apiKeyHelper`, `ANTHROPIC_AUTH_TOKEN`, any `Authorization` or `X-Api-Key` header in `ANTHROPIC_CUSTOM_HEADERS`; sign in or set `ANTHROPIC_API_KEY` |
| `it only works with Opus 5.5, Sonnet 5.5 and later models` | Use a supported model (for example `--model opus`); Haiku 5.5 and Fable 5.2 also work |
| `it doesn't work in background jobs` | Start in the foreground, without `--remote-control`; for a teammate split pane use in-process display mode |
| `it needs settings that Claude Code downloads from Anthropic` | Unset the variable that turns off feature-flag fetching, such as `DISABLE_TELEMETRY` |
| `OpenTelemetry is on` | Unset `CLAUDE_CODE_ENABLE_TELEMETRY` and `ENABLE_BETA_TRACING_DETAILED` |
| `it doesn't yet work with the plugin` | `/plugin`, disable each named plugin (ask admin if org-enabled) |
| `it doesn't yet work with an installed mod` | Turn off the mod that checks tool calls |
| `it can't be used together with agent teams yet` | Update to v2.1.326+, or unset `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` |
| `this launch's tool options` | Start without `--restricted`, add `REPL` to `--tools`, remove `REPL` from `--disallowedTools` and `deny` rules |
| `couldn't save your answer` | Make `~/.claude.json` writable |
| `your organization's settings don't allow it` | Ask the admin about the managed setting |

With no Code Mode line at all: check `claude --version` (update if older than v2.1.323), that the variable is `1` in shell or user settings, and remove any `0` from those and any `--settings` file.

Tool call refused by a hook (a `PreToolUse` hook gave no decision, refusing even when `onFailure` is unset):
- `the hook failed`: on a call from code the hook could not start, was killed, exited 126, 127 or above 128, or returned an HTTP error or invalid output.
- `the hook did not finish`: it timed out on a call from code, or on any tool call once Claude has run code in the session; raise the hook `timeout`.
- To let calls proceed when a `command` or `http` hook fails or times out, set `"onFailure": "continue"`. A `command` hook exiting with an ordinary code such as 1 lets the call go ahead unless `"onFailure": "block"`.
