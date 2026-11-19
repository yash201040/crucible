---
type: "Guide"
title: "Answering AskUserQuestion and ExitPlanMode from a hook"
description: "In -p runs these interactive tools need a permission host or a PreToolUse hook that returns allow with updatedInput."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, headless, askuserquestion, permissions]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [headless, sdk]
requires: ""
identifiers:
  - "AskUserQuestion"
  - "ExitPlanMode"
  - "updatedInput"
  - "--permission-prompt-tool"
  - "canUseTool"
  - "anthropic/requiresUserInteraction"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`AskUserQuestion` and `ExitPlanMode` need user interaction. In non-interactive `-p` mode they are offered only when the run has a permission host (for example an Agent SDK `canUseTool` callback or an MCP tool given with `--permission-prompt-tool`). A PreToolUse hook can fill that role.

# How to use it

The hook must: read the tool input from stdin, collect the answer through its own UI, and return `permissionDecision: "allow"` together with `updatedInput` holding the answer. `"allow"` alone is not enough. For `AskUserQuestion`, echo the original `questions` array and add an `answers` object mapping each question's text to the chosen label.

# Limits and defaults

- An MCP tool whose server marks it with `_meta["anthropic/requiresUserInteraction"]` is stricter: a hook cannot skip its approval prompt with `"allow"`, with or without `updatedInput`.
