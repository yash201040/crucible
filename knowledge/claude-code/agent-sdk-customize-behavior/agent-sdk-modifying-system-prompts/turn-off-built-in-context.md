---
type: "Reference"
title: "Turning off built-in context"
description: "Settings and env vars that remove git instructions, attribution, CLAUDE.md, attachments and file-mention expansion."
resource: "https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts"
tags: [git-instructions, attribution, attachments, env-vars]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.299"
surfaces: [sdk]
requires: ""
identifiers:
  - "includeGitInstructions"
  - "CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS"
  - "attribution.commit"
  - "attribution.pr"
  - "CLAUDE_CODE_DISABLE_CLAUDE_MDS"
  - "CLAUDE_CODE_DISABLE_ATTACHMENTS"
  - "CLAUDE_CODE_DISABLE_FILE_MENTIONS"
  - "settings"
  - "env"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-modifying-system-prompts"
    resource: "https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts"
    title: "Modifying system prompts"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Turn off built-in context when your agent supplies its own guidance, to avoid conflicting instructions (for example Claude Code still asks for a `Co-Authored-By` trailer when your prompt says no trailers). Pass settings keys via the `settings` option and env vars via `env` (TypeScript: `env` replaces the inherited environment, so spread `process.env`).

# How to use it

| Built-in context | How to turn it off |
| :- | :- |
| Commit and PR instructions and the git status snapshot | `includeGitInstructions: false` or `CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS=1` |
| `Co-Authored-By` trailer and PR footer | `attribution.commit` and `attribution.pr` set to your text or empty strings |
| User or project settings source incl. its CLAUDE.md | Leave `'user'`/`'project'` out of `settingSources` |
| Every CLAUDE.md file | `CLAUDE_CODE_DISABLE_CLAUDE_MDS=1` |
| Task list nudges, file-changed notes, skill list | `CLAUDE_CODE_DISABLE_ATTACHMENTS=1` |
| Only `@` file-mention expansion | `CLAUDE_CODE_DISABLE_FILE_MENTIONS=1` (Claude Code v2.1.299 or later) |

# Limits and defaults

- The git instructions are part of the Bash tool description and reach Claude even with a custom `systemPrompt`. With the minimal default, a custom `systemPrompt` or a custom main-thread agent with its own prompt, the session also starts without the git status snapshot.
- `CLAUDE_CODE_DISABLE_ATTACHMENTS` also sends `@` file mentions as plain text; the available-subagents list and background task notifications still arrive.
- With `CLAUDE_CODE_DISABLE_FILE_MENTIONS`, Claude gets the paths plus a note to read them, and `PreToolUse` hooks see each read as a tool call.
