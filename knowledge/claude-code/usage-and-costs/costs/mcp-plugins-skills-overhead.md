---
type: "Guide"
title: "Reduce tokens: MCP, plugins, hooks, skills"
description: "Cut context use by deferring MCP tools, preferring CLI tools, using code intelligence plugins, hooks that filter output, and skills."
resource: "https://code.claude.com/docs/en/costs"
tags: [mcp, hooks, skills, plugins, context]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "/context"
  - "/mcp"
  - "/hooks"
  - "PreToolUse"
  - "updatedInput"
  - "hookSpecificOutput"
  - "--debug-file"
  - "~/.claude/hooks/filter-test-output.sh"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "costs"
    resource: "https://code.claude.com/docs/en/costs"
    title: "Manage costs effectively"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Ways to keep fixed and bulky context out of the conversation.

# How to use it

- MCP tool definitions are deferred by default (only names and server instructions enter context until a tool is used). Run `/context` to see space use. Prefer CLI tools (`gh`, `aws`, `gcloud`, `sentry-cli`): no per-tool listing. Disable unused servers via `/mcp`.
- Code intelligence plugins give symbol navigation instead of text search, cutting file reads, and report type errors after edits.
- Hooks can preprocess data: a PreToolUse hook matching `Bash` returns `hookSpecificOutput` with `hookEventName: "PreToolUse"` and `updatedInput` to rewrite the command. The docs' example script `~/.claude/hooks/filter-test-output.sh` appends `2>&1 | tail -n 100` to `npm test`, `pytest` or `go test` commands. Register it under `hooks.PreToolUse` with `matcher: "Bash"` and a `command` hook in settings.json.
- Verify with `/hooks`, or run `claude --debug-file ./claude-debug.txt`; a rewrite logs a `modified tool input keys` line.
- Skills load on demand; a skill such as "codebase-overview" saves exploration tokens. Move workflow-specific instructions from CLAUDE.md into skills and keep CLAUDE.md under 200 lines.
