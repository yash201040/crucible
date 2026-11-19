---
type: "Reference"
title: "FAQ responses and starter prompts"
description: "One-line answers to common rollout questions and eight starter prompt templates."
resource: "https://code.claude.com/docs/en/communications-kit#quick-reference"
tags: [adoption, faq, prompts, onboarding]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, ide]
requires: ""
identifiers:
  - "/init"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "communications-kit"
    resource: "https://code.claude.com/docs/en/communications-kit"
    title: "Communications kit"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Short replies for common questions and starter prompts to share.

# How to use it

FAQ: works in VS Code and JetBrains (same features); no configuration needed (install, run `claude`, run `/init` once); code goes to Anthropic's API for inference and on Team or Enterprise is not used for training; it reads what you give it access to and file reads inside the working directory do not prompt; differs from Copilot in being an agent that reads files, runs commands and makes multi-file edits.

Prompt templates: fix a bug; understand code; safe refactor (use plan mode); write tests for edge cases; review the working diff before commit; open a PR with a conventional commit; make a skill (e.g. `/ship` running tests and lint); debug a stack trace for root cause.

# Notes

The page advises verifying version-specific details against the docs home page before distributing internally.
