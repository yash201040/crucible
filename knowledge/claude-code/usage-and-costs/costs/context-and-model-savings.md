---
type: "Guide"
title: "Reduce tokens: context, model and prompts"
description: "Habits that cut token use: clear between tasks, custom compaction, Sonnet over Opus, specific prompts, plan mode, checkpoints."
resource: "https://code.claude.com/docs/en/costs"
tags: [context, compaction, model-choice, plan-mode, tokens]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "/clear"
  - "/rename"
  - "/resume"
  - "/compact"
  - "/model"
  - "/config"
  - "/context"
  - "/rewind"
  - "model: haiku"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "costs"
    resource: "https://code.claude.com/docs/en/costs"
    title: "Manage costs effectively"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Token cost scales with context size. Claude Code already uses prompt caching and auto-compaction. These practices keep context small.

# How to use it

- Check usage with `/usage` or the status line context display.
- `/clear` between unrelated tasks; use `/rename` first and `/resume` to return.
- Custom compaction: `/compact Focus on code samples and API usage`, or a `# Compact instructions` section in the project CLAUDE.md.
- Model: Sonnet for most tasks, Opus for complex architecture or multi-step reasoning. Switch with `/model` or set a default in `/config`. A switch to Opus also applies to subagents that inherit the session model; for simple subagent tasks set `model: haiku` in the subagent config.
- Specific prompts avoid broad scanning ("add input validation to the login function in auth.ts" vs "improve this codebase").
- Plan mode (Shift+Tab) before implementation; press Escape to stop early; `/rewind` or double-tap Escape restores a checkpoint.
- Give verification targets (tests, screenshots, expected output); test incrementally.
