---
type: "Feature"
title: "Control who invokes a skill"
description: "disable-model-invocation and user-invocable decide whether you, Claude, or both can run a skill and when its description is in context."
resource: "https://code.claude.com/docs/en/skills"
tags: [skills, invocation, context, permissions]
kind: "frontmatter"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "disable-model-invocation"
  - "user-invocable"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "skills"
    resource: "https://code.claude.com/docs/en/skills"
    title: "Extend Claude with skills"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

By default both you and Claude can invoke any skill. Two fields restrict that.

# How to use it

| Frontmatter | You can invoke | Claude can invoke | Context |
| :- | :- | :- | :- |
| (default) | yes | yes | description in context; full skill loads on invoke |
| `disable-model-invocation: true` | yes | not on its own | description not in context; loads on invoke |
| `user-invocable: false` | no | yes | description in context; loads on invoke |

- Use `disable-model-invocation: true` for side-effect workflows (`/commit`, `/deploy`, `/send-slack-message`). If Claude tries without your message containing `/deploy` as a separate word with no punctuation, Claude Code blocks the call.
- `user-invocable: false` suits background knowledge; Claude can still invoke it via the Skill tool. To stop that, set `disable-model-invocation: true`.
- Where you write the name: at the start of a message (`/deploy staging`) runs the skill directly; after plain text as a separate word (`go ahead and /deploy to staging`) runs nothing directly but counts as permission for that message. Omit the slash to write about a skill without permitting a run.

# Notes

In a regular session only descriptions are in context; [subagents with preloaded skills](https://code.claude.com/docs/en/sub-agents#preload-skills-into-subagents) get full content injected at startup.
