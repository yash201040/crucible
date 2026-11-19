---
type: "Reference"
title: "Project instructions, memory and what threads load"
description: "Project instructions (16,000 chars), project memory, and which repository files cloud threads load or ignore."
resource: "https://code.claude.com/docs/en/claude-projects"
tags: [projects, memory, instructions, claude-md]
kind: "mixed"
maturity: "beta"
since: ""
surfaces: [web, desktop, cloud]
requires: ""
identifiers:
  - "MEMORY.md"
  - "CLAUDE.md"
  - ".claude/rules/"
  - ".claude/skills/"
  - ".mcp.json"
  - ".claude/settings.json"
  - "/mnt/project-files"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "claude-projects"
    resource: "https://code.claude.com/docs/en/claude-projects"
    title: "Let Claude coordinate ongoing work with Projects"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Standing context shared by all threads.

| Context | What it carries | Set via |
| - | - | - |
| Project memory | notes as files; every cloud thread reads index `MEMORY.md` at start and opens others on need | ask Claude to remember or forget; edit in Project settings > Memory (listed under Auto memory) |
| Project instructions | text sent to each new thread and the conversation, up to 16,000 characters | Project settings > Memory > Project instructions, or ask Claude |
| Repos, files, environment | repos cloned, files under `/mnt/project-files`, cloud environment | Project settings > Environment; Library Add |

Project memory is separate from local auto memory and from repo `CLAUDE.md`. Claude saves coordination preferences (such as thread limits) to memory itself; they are instructions Claude follows, not enforced settings.

# How to use it

What a cloud thread loads from each repository:

| In the repo | In a cloud thread |
| - | - |
| `CLAUDE.md`, `.claude/CLAUDE.md`, `.claude/rules/` at repo root | loaded from every repo; subdirectory `CLAUDE.md` and path-specific rules not loaded |
| `.claude/skills/` | not loaded; enable the skill for the claude.ai account |
| agents and commands under `.claude/` | not loaded; run the thread on your computer |
| `.mcp.json` servers | not loaded; use claude.ai connectors |
| plugins in `.claude/settings.json` | not loaded; add in Project settings > Plugins |
| permission rules in `.claude/settings.json` | not applied |
| hooks in `.claude/settings.json` | not run |
| `env` in `.claude/settings.json` | not applied; set in the cloud environment |

Connectors: all account connectors are available to every cloud thread with no per-project setup; the project conversation itself has no connectors. Turning one off in a thread's Connectors (+ menu) saves as the account default; a thread sees a new connector after its next message. Command-line tools go in the environment setup script.

# Notes

Instruction brief should cover purpose, where work happens (repos, branch, PR naming), how a thread checks its work, what to do when something is missing, and what needs go-ahead.
