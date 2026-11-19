---
type: "Feature"
title: "PreModelSwitch hook event"
description: "Runs before a requested model switch; can block or confirm it using cache-cost fields in the input."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, model, cost, prompt-cache]
kind: "hook"
maturity: "unlabelled"
since: "2.1.251"
surfaces: [cli, sdk]
requires: "Claude Code v2.1.251 or later"
identifiers:
  - "PreModelSwitch"
  - "from_model"
  - "to_model"
  - "requested_model"
  - "source"
  - "context_tokens"
  - "prompt_cache_warm"
  - "cache_ttl"
  - "estimated_cache_write_usd"
  - "pricing"
  - "set_model"
  - "apply_flag_settings"
  - "permissionDecision"
  - "permissionDecisionReason"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Runs before Claude Code applies a model switch that you or a client requested, to block it, require confirmation, or show the cost. Runs for: `/model <name>` and the `/model` picker; the `Option+P`/`Alt+P` picker; the Model setting in `/config`; turning on fast mode when that changes the model; a `set_model` request or a model change in an `apply_flag_settings` request from an Agent SDK host or Remote Control. Not run for switches Claude Code makes itself (automatic model fallback, restoring the model on resume): those reach PostModelSwitch only.

# How to use it

The matcher compares against the canonical model name of the target, ignoring a `[1m]` suffix; an alias (`opus`), dated ID and provider ID (Bedrock) all match the one canonical name (`claude-opus-5` covers every spelling). Write an exact name, a `|` list such as `claude-opus-4-6|claude-opus-5`, or a regex such as `.*opus.*`. If no canonical name can be determined (e.g. a custom model ID known only to an LLM gateway), every PreModelSwitch hook runs, so check `to_model` in the hook rather than rely on the matcher.

| Input field | Type | Description |
| :- | :- | :- |
| `from_model` | string | Model switched from |
| `to_model` | string | Model switched to |
| `requested_model` | string or null | Alias or ID named; null for the default model |
| `source` | string | `"command"` (`/model <name>`, `/config` Model setting, fast mode), `"picker"`, or `"sdk"` |
| `context_tokens` | number | Tokens the next request re-sends (input, cache read, cache creation, output of last main-conversation response); 0 before first response |
| `prompt_cache_warm` | boolean | Whether the current model's cache is likely warm (switch forfeits it) |
| `cache_ttl` | string | `"5m"` or `"1h"` |
| `estimated_cache_write_usd` | number | Estimated cost of writing `context_tokens` on `to_model` at the `cache_ttl` rate, excluding the response; an estimate |
| `pricing` | string | `"configured"` (org's own rates), `"catalog"` (list price) or `"default"` (no known price, default rate assumed) |

Decision: exit 2 or top-level `decision: "block"` cancels. Finer: `hookSpecificOutput.permissionDecision` of `"allow"` (proceeds and skips the confirmation shown while the cache is warm), `"deny"`, or `"ask"`, with `permissionDecisionReason`. No `"defer"`, `updatedInput` or `additionalContext`. Precedence `deny` > `ask` > `allow`. Any `systemMessage` is shown to the user whatever the decision.

# Limits and defaults

- Only `/model` in an interactive session can show the `"ask"` prompt; elsewhere (including `-p`, `/config`, `set_model`) `"ask"` is a refusal. For `deny` the reason is returned as the error for a `set_model` request.
- A hook that does not respond before its timeout blocks the switch; default timeout 30 seconds. An exit code other than 0 or 2 without valid JSON is a non-blocking error (the switch goes ahead) unless the hook's failure is set to block.
