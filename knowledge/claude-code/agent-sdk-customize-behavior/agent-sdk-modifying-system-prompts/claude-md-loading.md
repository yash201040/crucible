---
type: "Feature"
title: "CLAUDE.md loading in the SDK"
description: "CLAUDE.md is injected into the conversation via setting sources, independent of the system prompt."
resource: "https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts"
tags: [claude-md, setting-sources, project-context]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "CLAUDE.md"
  - ".claude/CLAUDE.md"
  - "~/.claude/CLAUDE.md"
  - "settingSources"
  - "setting_sources"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-modifying-system-prompts"
    resource: "https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts"
    title: "Modifying system prompts"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The SDK injects CLAUDE.md content into the conversation and leaves the system prompt untouched, so it works with any system prompt. `'project'` loads `CLAUDE.md` or `.claude/CLAUDE.md` from the working directory; `'user'` loads `~/.claude/CLAUDE.md`. Default `query()` options enable both.

# How to use it

Set `settingSources: ["project"]` (Python `setting_sources=["project"]`) alongside the `claude_code` preset. If you set it explicitly, include the sources you need. Loading is controlled by setting sources, not by the preset.

# Limits and defaults

Not loaded when `settingSources` is an empty array.
