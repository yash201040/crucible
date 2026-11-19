---
type: "Reference"
title: "Prompt and agent hook fields"
description: "Fields for prompt hooks (single-turn model evaluation) and agent hooks (subagent verification, experimental)."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, prompt, agent, experimental]
kind: "frontmatter"
maturity: "experimental"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "prompt"
  - "model"
  - "$ARGUMENTS"
  - "type: \"prompt\""
  - "type: \"agent\""
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Prompt hooks (`type: "prompt"`) send a prompt to a Claude model for single-turn evaluation, which returns its decision as JSON. Agent hooks (`type: "agent"`) spawn a subagent that can use tools such as Read, Grep and Glob before returning a decision. The docs label agent hooks experimental and subject to change.

# How to use it

| Field | Required | Description |
| :- | :- | :- |
| `prompt` | yes | Prompt text; `$ARGUMENTS` is a placeholder for the hook input JSON; escape with a backslash for literal text (`\$1.00` renders `$1.00`) |
| `model` | no | Evaluation model; defaults to the model Claude Code uses for background functionality |

# Limits and defaults

Default `timeout` is 30 seconds for prompt hooks and 60 for agent hooks. When more than 12 prompt/agent hooks match one event, 12 run at once. See [common fields](./p1-handler-types-and-common-fields.md).
