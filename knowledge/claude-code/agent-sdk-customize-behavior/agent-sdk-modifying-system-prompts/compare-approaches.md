---
type: "Reference"
title: "Comparing four prompt customization approaches"
description: "CLAUDE.md, output styles, append and custom systemPrompt compared on persistence, tool guidance and safety, plus combining them."
resource: "https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts"
tags: [system-prompt, comparison, output-styles, append]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "CLAUDE.md"
  - "systemPrompt"
  - "append"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-modifying-system-prompts"
    resource: "https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts"
    title: "Modifying system prompts"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

| Feature | CLAUDE.md | Output Styles | `systemPrompt` with append | Custom `systemPrompt` |
| - | - | - | - | - |
| Persistence | Per-project file | Saved as files | Session only | Session only |
| Reusability | Per-project | Across projects | Code duplication | Code duplication |
| Management | Filesystem | CLI + files | In code | In code |
| Tool guidance | Preserved | Preserved | Preserved | Lost unless included |
| Built-in safety | Maintained | Maintained | Maintained | Must be added |
| Customization | Additions only | Additions; can omit coding instructions | Additions only | Complete control |
| Version control | With project | Yes | With code | With code |
| Scope | Project | User or project | Code session | Code session |

# How to use it

The approaches compose: a persistent output style or CLAUDE.md sets long-lived behavior, and `append` layers session-specific instructions on top without touching saved configuration (for example an active Code Reviewer style plus an `append` listing OAuth 2.0 compliance, token storage and session management as focus).

# Notes

CLAUDE.md does not change the system prompt itself; its content is injected as project context.
