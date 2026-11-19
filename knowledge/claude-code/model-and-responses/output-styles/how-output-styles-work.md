---
type: "Concept"
title: "How output styles work"
description: "Style instructions are sent with every request, affect the main conversation and forks only, and change token usage."
resource: "https://code.claude.com/docs/en/output-styles#how-output-styles-work"
tags: [output-styles, system-prompt, subagents, tokens]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "keep-coding-instructions"
  - "CLAUDE_CODE_SIMPLE_SYSTEM_PROMPT"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "output-styles"
    resource: "https://code.claude.com/docs/en/output-styles"
    title: "Output styles"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

An output style changes the instructions Claude Code gives Claude, sent with every request.

# How to use it

On the full system prompt, custom styles leave out Claude Code's section of built-in software engineering instructions (how to scope changes, write comments, verify work) unless `keep-coding-instructions: true`. The shorter system prompt has no such section, so the field has no effect there. To rely on the field, set `CLAUDE_CODE_SIMPLE_SYSTEM_PROMPT` to `0`, which selects the full prompt on any model.

# Limits and defaults

- Styles apply to the main conversation and to a fork (which inherits the parent's conversation and system prompt). Other subagents run their own system prompt, so styles do not change how they respond.
- Token usage: a style's instructions add input tokens, reduced by prompt caching after the first request. Explanatory and Learning raise output tokens; Concise lowers them; custom styles depend on the instructions.
