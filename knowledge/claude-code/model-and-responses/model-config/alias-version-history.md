---
type: "Reference"
title: "Alias version history"
description: "The Claude Code version at which each model alias changed the model it resolves to."
resource: "https://code.claude.com/docs/en/model-config#version-history"
tags: [model, aliases, versions, history]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers: []
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "model-config"
    resource: "https://code.claude.com/docs/en/model-config"
    title: "Model configuration"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A table of Claude Code versions at which an alias moved to a new model, newest first. Earlier versions resolve aliases to older models.

# How to use it

| Version | Change |
| :- | :- |
| v2.1.321 | `fable` resolves to Fable 5.2, except in Claude apps gateway sessions |
| v2.1.321 | `best` resolves to the same model as `opus` (earlier: the model `fable` resolves to, where Fable is available) |
| v2.1.293 | `haiku` resolves to Haiku 5.5 on the Anthropic API |
| v2.1.284 | `sonnet` resolves to Sonnet 5.5 on the Anthropic API |
| v2.1.280 | `opus` resolves to Opus 5.5 on the Anthropic API, Claude Platform on AWS, Bedrock, Agent Platform |
| v2.1.257 | `fable` resolves to Fable 5.1, except in Claude apps gateway sessions |
| v2.1.219 | `opus` resolves to Opus 5 on the Anthropic API, Claude Platform on AWS, Bedrock, Agent Platform |
| v2.1.207 | `opus` resolves to Opus 4.8 on Claude Platform on AWS, Bedrock, Agent Platform |
| v2.1.197 | `sonnet` resolves to Sonnet 5 on the Anthropic API |
| v2.1.154 | `opus` resolves to Opus 4.8 on the Anthropic API |
| Earlier | `opus` was Opus 4.7 on Claude Platform on AWS and Opus 4.6 on Bedrock and Agent Platform; `fable` was Fable 5 and `haiku` was Haiku 4.5 on every provider |
