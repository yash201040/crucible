---
type: "Concept"
title: "The agentic loop"
description: "Claude works in three blended phases (gather context, take action, verify) using models and tools, and the user can interrupt at any point."
resource: "https://code.claude.com/docs/en/how-claude-code-works"
tags: [agentic-loop, harness, models, tools]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "/model"
  - "--model"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "how-claude-code-works"
    resource: "https://code.claude.com/docs/en/how-claude-code-works"
    title: "How Claude Code works"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A task goes through gather context, take action and verify results. The phases blend and repeat until the task is complete; Claude decides each step from what it learned in the previous one. The loop is powered by models that reason and tools that act. Claude Code is the layer around the model that provides tools and manages context, called the agentic harness.

# How to use it

Switch models with `/model` during a session or start with `claude --model <name>`. Sonnet is described as handling most coding tasks; Opus gives stronger reasoning for complex architectural decisions. Interrupting at any point steers the loop.

# Notes

The same loop runs on every interface; only where code executes and how you interact changes.
