---
type: "Feature"
title: "Handle AskUserQuestion clarifying questions"
description: "Detect AskUserQuestion in canUseTool, parse the questions array and return an answers map keyed by question text."
resource: "https://code.claude.com/docs/en/agent-sdk/user-input"
tags: [agent-sdk, askuserquestion, plan-mode, clarifying-questions]
kind: "tool"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "AskUserQuestion"
  - "questions"
  - "answers"
  - "response"
  - "multiSelect"
  - "header"
  - "options"
  - "label"
  - "description"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-user-input"
    resource: "https://code.claude.com/docs/en/agent-sdk/user-input"
    title: "Handle approvals and user input"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

When a task has multiple valid approaches, Claude calls `AskUserQuestion`, which triggers `canUseTool` with `toolName` `AskUserQuestion`. Claude generates the questions and options; you present them and return selections. You cannot add your own questions to this flow. Questions are especially common in `plan` mode.

# How to use it

1. Pass a `canUseTool` callback. `AskUserQuestion` is available by default; if you restrict with a `tools` array (for example `["Read","Glob","Grep"]`), add `AskUserQuestion` or Claude cannot ask.
2. In the callback, branch on `toolName == "AskUserQuestion"`.
3. Read `input.questions`.
4. Show them in your UI.
5. Return allow with `updatedInput` containing the original `questions` (required for tool processing) and an `answers` object: each key is the `question` text, each value the selected option's `label`. Multi-select: an array of labels or labels joined with `", "`. Free text typed by the user is used as the value, not the word "Other".

Question fields:

| Field | Description |
| - | - |
| `question` | full question text |
| `header` | short label, max 12 characters |
| `options` | 2-4 choices, each with `label` and `description`; TypeScript may add `preview` |
| `multiSelect` | true if several can be chosen |

Response fields: `questions`, `answers`, and optional `response`, a freeform reply when the user dismisses the card and types a general reply; when set, Claude receives "The user responded: ..." instead of the per-question answers.

# Limits and defaults

- Each call supports 1-4 questions with 2-4 options each.
- `AskUserQuestion` is not currently available in subagents spawned via the Agent tool.
