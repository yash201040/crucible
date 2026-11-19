---
type: "Feature"
title: "System prompt flags and snapshot behavior"
description: "Five flags to replace or append to the system prompt, how combining works, caching boundary marker and recording in resumed sessions."
resource: "https://code.claude.com/docs/en/cli-reference#system-prompt-flags"
tags: [system-prompt, caching, resume, snapshot]
kind: "cli_flag"
maturity: "unlabelled"
since: "2.1.283"
surfaces: [cli, headless]
requires: ""
identifiers:
  - "--system-prompt"
  - "--system-prompt-file"
  - "--append-system-prompt"
  - "--append-system-prompt-file"
  - "--system-prompt-snapshot"
  - "__SYSTEM_PROMPT_DYNAMIC_BOUNDARY__"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "cli-reference"
    resource: "https://code.claude.com/docs/en/cli-reference"
    title: "CLI reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Four flags set the system prompt text and a fifth controls whether a conversation keeps the prompt it started with. All work in interactive and non-interactive modes.

# How to use it

| Flag | Behavior |
| :- | :- |
| `--system-prompt` | Replace the entire default prompt with text |
| `--system-prompt-file` | Replace with file contents |
| `--append-system-prompt` | Append text to the default prompt |
| `--append-system-prompt-file` | Append file contents |
| `--system-prompt-snapshot` | `off` rebuilds the prompt on every request; `on` (default) reuses a recorded prompt where recording applies |

To replace and still append, combine a replace flag with an append flag. From v2.1.283 a flag can also be combined with its own file form; file contents come first, then a blank line, then the inline text.

Cache split: put a line containing only `__SYSTEM_PROMPT_DYNAMIC_BOUNDARY__` between static instructions and per-run context in replacement text; Claude Code splits at the first such line and removes it, so the upper part stays cached. Requires v2.1.275+.

Choosing: append keeps default tool guidance, safety instructions and coding conventions; replace drops all of it, suited to non-coding agents in unattended pipelines.

# Limits and defaults

The prompt is built once on the first request and recorded in the session; later requests, including after `--resume` or `--continue`, reuse it until the conversation is compacted. Different flag text on a later launch takes effect after compaction or in a new conversation. In bare mode (`--bare` or `CLAUDE_CODE_SIMPLE=1`) outside cloud sessions, recording stays off unless `--system-prompt-snapshot on`. Before v2.1.268, sessions without feature-flag fetching (including Bedrock, Google Cloud's Agent Platform, Microsoft Foundry) rebuilt every request and the flag had no effect. `--system-prompt-snapshot` requires v2.1.257+. Before v2.1.265, any system prompt flag turned recording off unless `on` was passed.
