---
type: "Feature"
title: "Passing arguments and stacking skills"
description: "Skills take arguments from the user or Claude; at the terminal up to six skills can be stacked in one message, but -p and the SDK load only the first."
resource: "https://code.claude.com/docs/en/skills"
tags: [skills, arguments, stacking, headless]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "$ARGUMENTS"
  - "/write-tests /fix-issue 123"
  - "claude -p"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "skills"
    resource: "https://code.claude.com/docs/en/skills"
    title: "Extend Claude with skills"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Both you and Claude can pass arguments when invoking a skill; they surface through [substitutions](./skill-string-substitutions.md). `/fix-issue 123` with `Fix GitHub issue $ARGUMENTS` yields "Fix GitHub issue 123".

# How to use it

- At the terminal prompt, stack skills at the start of a message: `/write-tests /fix-issue 123` loads both and passes `123` as `$ARGUMENTS` to each.
- Claude Code expands the first skill plus up to five more. Expansion stops at the first token that is not an inline user-invocable skill.

# Limits and defaults

- Through the Agent SDK or `claude -p`, only the first skill loads, with the rest of the line as its arguments.
- A forked skill (such as `/code-review`) or one whose arguments may start with another command (such as `/loop`) ends expansion; that token and everything after it become argument text for every expanded skill.
