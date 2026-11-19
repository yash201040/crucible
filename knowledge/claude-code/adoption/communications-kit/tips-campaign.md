---
type: "Reference"
title: "Tips and tricks drip campaign"
description: "Ready-to-paste tips on models, memory, permission modes, rewind, MCP, skills, hooks, images, git, plugins and security."
resource: "https://code.claude.com/docs/en/communications-kit#tips-and-tricks-campaign"
tags: [adoption, tips, models, permission-modes, rewind]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "/model"
  - "/model fable"
  - "/init"
  - "/rewind"
  - "Shift+Tab"
  - "Esc"
  - ".mcp.json"
  - ".claude/skills/<name>/SKILL.md"
  - "/plugin"
  - "Ctrl+V"
  - "Alt+V"
  - "acceptEdits"
  - "plan"
  - "default"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "communications-kit"
    resource: "https://code.claude.com/docs/en/communications-kit"
    title: "Communications kit"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A set of stand-alone Slack/Teams tips, one or two per week, each with a hook, payoff, try-it-now prompt and docs link.

# How to use it

| Topic | Fact stated |
| :- | :- |
| Models | Sonnet: recommended everyday default; Opus: large refactors, hard debugging, high-stakes; Haiku: quick questions and mechanical edits; Fable: most capable for hardest long tasks, opt-in with `/model fable` |
| Automatic fallback | Cybersecurity or biology content on Fable falls back to Opus; on Opus 5.5, Sonnet 5.5 and Opus 5, flagged content switches to an earlier model in the same family, except flagged biology content on Opus 5 or Sonnet 5.5, which is refused |
| Memory | `/init` writes a CLAUDE.md (keep under two screens); `@` file and directory references |
| Permission modes | Shift+Tab cycles: Manual (`default`) asks before edits and most shell commands, `acceptEdits` lets edits and common filesystem commands through, `plan` researches and proposes without editing |
| Rewind | `/rewind` or `Esc` twice rolls back conversation and file changes; checkpointing is automatic |
| MCP | `.mcp.json` at project root wires GitHub, Jira, Linear |
| Skills / Hooks | `SKILL.md` in `.claude/skills/<name>/` becomes `/name`; a Stop hook sends a desktop notification |
| Images | drag in, `Ctrl+V` paste, or `Alt+V` on Windows and WSL |
| Plugins | `/plugin` browses and installs |
| Security | CLI talks directly to Anthropic's API; optional OS-level sandboxing for shell commands |

# Limits and defaults

Habits recommended: start in plan mode for multi-file changes, run `/init` early, review diffs before committing, verify critical-path changes.
