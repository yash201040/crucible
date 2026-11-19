---
type: "Guide"
title: "Prompt patterns that work"
description: "Six prompting patterns from the prompt library: outcome, self-check, reference, measurable target, artifact, answer format."
resource: "https://code.claude.com/docs/en/prompt-library"
tags: [prompts, best-practices, verification]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "/verify"
  - "@"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "prompt-library"
    resource: "https://code.claude.com/docs/en/prompt-library"
    title: "Prompt library"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A library of copy-paste prompts tagged by task and role, gathered from Common workflows, Best practices, and how Anthropic teams use Claude Code. They are starting points; each has a "Why this works" note.

# How to use it

| Pattern | Idea |
| :- | :- |
| Describe the outcome, not the steps | Say what you want and let Claude find the files |
| Give it a way to check its own work | Ask to run, test, compare or verify in the same prompt; `/verify` checks the finished change against the running app |
| Point at a reference | Name an existing file or pattern to match |
| State the measurable target | Give the metric and threshold |
| Give it the artifact | Paste errors, logs, screenshots, or type `@` to reference a file |
| Say how you want the answer | Name format, length or audience; an output style sets a default format |

# Notes

Next step after a prompt works: save it as a skill, record conventions in CLAUDE.md, use plan mode for larger or riskier changes. Team rollout pointers: administration (managed settings) and costs and usage pages.
