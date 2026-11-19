---
type: "Feature"
title: "ultrathink keyword"
description: "Including ultrathink in a prompt requests deeper reasoning for one turn, raising it to xhigh where supported."
resource: "https://code.claude.com/docs/en/model-config#use-ultrathink-for-one-off-deep-reasoning"
tags: [ultrathink, effort, reasoning, keyword]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.311"
surfaces: [cli, ide, desktop]
requires: "Terminal v2.1.311+, VS Code v2.1.316+, desktop local Code tab v2.1.316+"
identifiers:
  - "ultrathink"
  - "CLAUDE_CODE_DISABLE_ULTRATHINK"
  - "maxEffortLevel"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "model-config"
    resource: "https://code.claude.com/docs/en/model-config"
    title: "Model configuration"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Put `ultrathink` anywhere in a prompt to request deeper reasoning on that turn without changing the session effort. Claude Code adds an in-context instruction. Other phrases ("think", "think hard", "think more") are ordinary text, not keywords.

# How to use it

To also raise the turn to `xhigh`, type it in the terminal prompt (word shows rainbow; v2.1.311+), VS Code chat box (v2.1.316+), or a local session in the desktop app Code tab (v2.1.316+).

If it is not rainbow: retype it outside quotes, brackets, paths or commands in a prompt not starting with `/`; unset `CLAUDE_CODE_EFFORT_LEVEL` if below `xhigh`, raise `maxEffortLevel` to `xhigh` or above, or ask an admin to raise the org limit; switch to an Opus 5.5, Sonnet 5.5, Haiku 5.5, Fable 5.2 or Fable 5.1 model. Where it cannot raise a turn (Bedrock, Agent Platform, Claude apps gateway) set effort instead.

# Limits and defaults

Disable the keyword and its in-context instruction with `CLAUDE_CODE_DISABLE_ULTRATHINK=1` in the shell or a settings file (v2.1.316+).
