---
type: "Feature"
title: "Run a skill in a subagent (context: fork)"
description: "context: fork starts an isolated subagent of type agent with the skill as its prompt; runs in background by default."
resource: "https://code.claude.com/docs/en/skills"
tags: [skills, subagents, fork, background]
kind: "frontmatter"
maturity: "unlabelled"
since: "2.1.295"
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "context: fork"
  - "agent"
  - "background"
  - "CLAUDE_CODE_DISABLE_BACKGROUND_TASKS"
  - "Explore"
  - "Plan"
  - "general-purpose"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "skills"
    resource: "https://code.claude.com/docs/en/skills"
    title: "Extend Claude with skills"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`context: fork` starts a new subagent of the type in `agent` (built-in `Explore`, `Plan`, `general-purpose`, or a custom one in `.claude/agents/`; default `general-purpose`) and gives it the skill content as its prompt. The subagent does not see conversation history, so instructions must stand alone. It is not a fork of the current conversation; for that use conversation forking. Makes sense only for skills with an explicit task: guideline-only skills return nothing useful.

# How to use it

```
---
name: deep-research
context: fork
agent: Explore
---
Research $ARGUMENTS thoroughly...
```

- The `agent` field decides model, tools and permissions; the subagent returns a summary to the main conversation.
- Compare: skill with `context: fork` has system prompt from agent type, task = SKILL.md, loads CLAUDE.md per the agent's startup context. A subagent with a `skills` field has the subagent's markdown body as system prompt, task from Claude's delegation message, and preloaded skills plus CLAUDE.md. Explore and Plan agents start without CLAUDE.md and git status.

# Limits and defaults

- Runs in the background by default; result arrives in the conversation when done. `background: false` waits in the invoking turn.
- It waits anyway: in non-interactive mode (`-p` or the Agent SDK); when `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS` is `1`; when invoked while an earlier invocation of the same skill still runs; when a session-scoped scheduled task fires with the skill as prompt.
- An agent in a dynamic workflow that invokes a forked skill waits for and receives the result; before v2.1.295 a backgrounded fork's result went to the main conversation instead.
- A backgrounded fork gets the narrower tool set of background subagents; set `background: false` to keep the full set.
- A backgrounded fork's edits fall outside checkpoints: `/rewind` restores only files Claude already edited in the conversation; use git to revert the rest.
