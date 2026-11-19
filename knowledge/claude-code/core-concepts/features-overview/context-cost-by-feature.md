---
type: "Reference"
title: "Context cost and loading by feature"
description: "When each extension loads, what enters context, and its cost; includes subagent startup context and how to hide skill descriptions."
resource: "https://code.claude.com/docs/en/features-overview"
tags: [context, cost, skills, mcp, subagents]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "disable-model-invocation: true"
  - "skillOverrides"
  - "/mcp"
  - "/context all"
  - "/doctor"
  - "skills"
  - "omitClaudeMd"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "features-overview"
    resource: "https://code.claude.com/docs/en/features-overview"
    title: "Extend Claude Code"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Every feature consumes some context. Too much can fill the window and add noise, so skills may not trigger correctly or conventions get lost.

# How to use it

| Feature | When it loads | What loads | Cost |
| - | - | - | - |
| CLAUDE.md | Session start | Full content of each file that loads at start (managed, user, project) | Every request |
| Output styles | Session start and on switch | Active style's full instructions; nothing for Default | Every request |
| Skills | Session start + when used | Descriptions at start, full content when used | Low (descriptions every request) |
| MCP servers | Session start | Tool names and server instructions; full schemas on demand | Low until a tool is used |
| Code intelligence | After file edits and on demand | Diagnostics after edits; symbol info on lookup | Low; can reduce file reads |
| Subagents | When spawned | Fresh context, or parent conversation for a fork | Isolated from main session |
| Hooks | On trigger | Nothing | Zero unless the hook returns context |

# Limits and defaults

- Set `disable-model-invocation: true` in a skill's frontmatter to keep its description out of context (nothing loads until you invoke it). For a skill you did not write, set `skillOverrides` in settings.
- Subagent startup context: its own system prompt (not Claude Code's), full content of skills in its `skills:` field, CLAUDE.md and git status (built-in Explore and Plan agents start with neither; `omitClaudeMd` drops the CLAUDE.md files), plus whatever the lead passes in the prompt. A fork instead loads the parent's conversation, system prompt and tools. Subagents can still discover unlisted project, user and plugin skills through the Skill tool.
- Tool search is on by default, so idle MCP tools use minimal context. Run `/mcp` for connection status and `/context all` for per-tool token use. Remote MCP servers reconnect automatically.
- A nested CLAUDE.md over its per-file size limit is truncated to its start. `/doctor` gives trim proposals for a checked-in CLAUDE.md.

# Notes

The LSP tool is inactive until a code intelligence plugin is installed. Bundled skills such as `/code-review`, `/batch` and `/debug` work without setup. Hooks run at events including tool execution, session boundaries, prompt submission, permission requests and compaction.
