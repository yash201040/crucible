---
type: "Feature"
title: "Custom prompts and dynamic boundary caching"
description: "Replace the prompt with a string, a Python file form, or a TypeScript array split by SYSTEM_PROMPT_DYNAMIC_BOUNDARY for caching."
resource: "https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts"
tags: [custom-prompt, caching, boundary, system-prompt-file]
kind: "api"
maturity: "unlabelled"
since: "2.1.275"
surfaces: [sdk, cli]
requires: "Claude Code v2.1.275 or later for the CLI boundary line; direct Claude API or Claude Platform on AWS for the split"
identifiers:
  - "systemPrompt"
  - "system_prompt={\"type\": \"file\", \"path\": \"...\"}"
  - "SYSTEM_PROMPT_DYNAMIC_BOUNDARY"
  - "__SYSTEM_PROMPT_DYNAMIC_BOUNDARY__"
  - "--system-prompt"
  - "--system-prompt-file"
  - "CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS"
  - "cache_creation_input_tokens"
  - "cache_read_input_tokens"
  - "Argument list too long"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-modifying-system-prompts"
    resource: "https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts"
    title: "Modifying system prompts"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A string `systemPrompt` replaces the default entirely. In Python a large prompt can load from a file with `system_prompt={"type": "file", "path": "..."}`, because a string prompt is passed as one command-line argument and one over the OS limit fails at spawn (Linux: `Argument list too long`).

# How to use it

TypeScript only: pass an array with `SYSTEM_PROMPT_DYNAMIC_BOUNDARY` (imported from `@anthropic-ai/claude-agent-sdk`) between the static and per-request parts: `systemPrompt: [instructions, SYSTEM_PROMPT_DYNAMIC_BOUNDARY, ticketContext]`. Strings before the marker become one text block, after it a second, each with its own cache breakpoint. Strings on each side are joined with a blank line; the marker is removed; a repeated marker splits at the first and removes the rest; without the marker all strings join into one block. Not available in Python.

CLI: with `--system-prompt` or `--system-prompt-file`, include a line containing only `__SYSTEM_PROMPT_DYNAMIC_BOUNDARY__`; the first such line splits the prompt and is removed. Requires Claude Code v2.1.275 or later.

# Limits and defaults

The split happens only when calling the Claude API directly or on Claude Platform on AWS. On Amazon Bedrock, Google Cloud's Agent Platform, Microsoft Foundry or an LLM gateway, the whole prompt is one block; the same when `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1`. Track results with `cache_creation_input_tokens` and `cache_read_input_tokens` on result messages.
