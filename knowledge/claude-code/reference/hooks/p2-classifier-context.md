---
type: "Feature"
title: "classifierContext for auto mode"
description: "A PostToolUse note aimed at the auto mode classifier instead of Claude, with trust rules and a 2,000-character cap."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, auto-mode, classifier, posttooluse]
kind: "hook"
maturity: "unlabelled"
since: "2.1.236"
surfaces: [cli, sdk]
requires: "Claude Code v2.1.236 or later; auto mode"
identifiers:
  - "classifierContext"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`hookSpecificOutput.classifierContext` in a PostToolUse response sends a short note about the call's result to the auto mode classifier, not to Claude, for its review of later actions. Example: "This query ran against the staging database, not production."

# How to use it

Return `{"hookSpecificOutput": {"hookEventName": "PostToolUse", "classifierContext": "..."}}`. Keep it a short assertion about this one call (origin, or a user statement about it); do not copy untrusted tool output or third-party text, or use it for unrelated messages or event streams.

Trust: hooks from settings files, plugins, skills and agent frontmatter are treated as unverified application context and never establish user intent (a claim of user approval is checked against your own messages). An in-process Agent SDK TypeScript callback returning the note during the live session may have a relayed user statement weighed as intent, but never lifts a block your own message could not lift. After resume, restored notes are unverified. Combined notes from both groups are unverified.

# Limits and defaults

- Notes for one tool call are capped at 2,000 characters total across hooks; the rest is truncated.
- Synchronous responses only; ignored from a background (`async`) hook.
- Discarded for calls the classifier does not record (read-only lookups such as file reads and searches).
- When describing output you replace with `updatedToolOutput`, return both in the same response; the note is dropped if that rewrite is rejected or replaced by another hook's rewrite. A note returned without a rewrite is delivered even if another hook rewrites the output.
