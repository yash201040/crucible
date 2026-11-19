---
type: "Feature"
title: "Call a model from a mod"
description: "$.model.complete sends a standalone prompt and $.model.fork sends the conversation plus a prompt; both bill to the session's credentials."
resource: "https://code.claude.com/docs/en/plugins/mods/api"
tags: [mods, model, cost, subagent-calls]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "$.model.complete"
  - "$.model.fork"
  - "model"
  - "prompt"
  - "system"
  - "maxTokens"
  - "timeoutMs"
  - "effort"
  - "r.isAnswered"
  - "r.reason"
  - "r.text"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-api"
    resource: "https://code.claude.com/docs/en/plugins/mods/api"
    title: "Use the mods API"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A mod can make its own model requests for small jobs such as classifying or summarizing. Both calls use the session's credentials and bill to the user's plan, API key or cloud provider.

# How to use it

| In the request | `$.model.complete` | `$.model.fork` |
| :- | :- | :- |
| Model | the `model` you pass (e.g. `'haiku'`) | the session's model |
| System prompt | short attribution block, then your `system` | the session's system prompt |
| Messages | one user message, your `prompt` | conversation so far, then your `prompt` |
| CLAUDE.md and project context | not included | included |
| Tools | none | Claude's tools, which the model cannot call |

A fork repeats the conversation's last request, so most of it is served from the prompt cache while the conversation is cached.

Example: `await $.model.complete({ model: 'haiku', system: '...', prompt: e.args, maxTokens: 20, timeoutMs: 15000 })`; use `r.text` only if `r.isAnswered`.

# Limits and defaults

A Claude API failure does not reject the call: check `r.isAnswered` and read `r.reason` when false. The call rejects for a request Claude Code will not send, such as a model the organization blocks. The `maxTokens` default is in the reference limits; other options such as `effort` are in the build's types.
