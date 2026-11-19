---
type: "Concept"
title: "Capabilities: automation, agents, scheduling, CLI"
description: "Overview of what Claude Code does: scripted -p runs, git work, MCP, CLAUDE.md, skills, hooks, parallel agents, scheduled tasks and cross-surface handoff."
resource: "https://code.claude.com/docs/en/overview"
tags: [overview, agents, scheduling, headless, mcp]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk, desktop, web, mobile]
requires: ""
identifiers:
  - "claude -p"
  - "CLAUDE.md"
  - "AGENTS.md"
  - "/schedule"
  - "/loop"
  - "/desktop"
  - "claude --teleport"
  - "claude --cloud"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "overview"
    resource: "https://code.claude.com/docs/en/overview"
    title: "Overview"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The overview lists what Claude Code can do, with pointers to detailed pages.

# How to use it

- **Scripting and CI**: Claude Code follows the Unix philosophy. Examples: `tail -200 app.log | claude -p "Slack me if you see any anomalies"`, `claude -p "translate new strings into French and raise a PR for review"`, `git diff main --name-only | claude -p "review these changed files for security issues"`. In CI, GitHub Actions or GitLab CI/CD can automate code review and issue triage.
- **Instructions and extension**: `CLAUDE.md` in the project root is read at the start of every session; a repository's `AGENTS.md` can be read in its place. Auto memory saves learnings across sessions. Skills package repeatable workflows (e.g. `/review-pr`, `/deploy-staging`); hooks run shell commands before or after Claude Code actions.
- **Parallel agents**: spawn multiple agents (subagents) working on parts of a task, with a lead agent coordinating, assigning subtasks and merging results. To run several full sessions and watch them on one screen, use background agents (agent view). The Agent SDK builds custom agents with full control over orchestration, tool access and permissions. Dynamic workflows orchestrate many subagents at once.
- **Scheduling**: cloud scheduled tasks (formerly routines) run in the cloud even when your computer is off, can trigger on API calls or GitHub events, and are created from the web, the Desktop app or `/schedule` in the CLI. Desktop scheduled tasks run on your machine with local access. `/loop` repeats a prompt within a CLI session for polling.
- **Moving between surfaces**: Remote Control (continue a local session from phone or browser); Dispatch (message a task from phone and open the Desktop session); `claude --teleport` pulls a web or mobile session into the terminal (requires a claude.ai subscription); `/desktop` continues a terminal session in the Desktop app (requires a claude.ai subscription; macOS and x64 Windows); `@Claude` in Slack returns a pull request.
- **MCP**: Model Context Protocol connects external data sources and tools (e.g. Google Drive, Jira, Slack).

# Notes

Surface map from the page: Remote Control (continue a local session elsewhere), Channels (push Telegram, Discord, iMessage or webhook events into a session), `claude --cloud` (start locally, continue on mobile), cloud or Desktop scheduled tasks, GitHub Actions or GitLab CI/CD, GitHub Code Review, Slack, Chrome (debug live web apps), Agent SDK.
