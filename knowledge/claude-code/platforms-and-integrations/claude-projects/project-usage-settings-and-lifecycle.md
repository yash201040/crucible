---
type: "Limit"
title: "Project usage, limits, settings and lifecycle"
description: "Plan usage draw, 500 new threads per day cap, auto-continue after limits, project settings table and Pause, Archive, Delete."
resource: "https://code.claude.com/docs/en/claude-projects"
tags: [projects, usage, limits, lifecycle, settings]
kind: "limit"
maturity: "beta"
since: ""
surfaces: [web, desktop, mobile]
requires: "usage credits turned on to exceed plan limits"
identifiers:
  - "Auto-continue when usage limits reset"
  - "Restart Claude"
  - "Pause"
  - "Archive"
  - "Delete"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "claude-projects"
    resource: "https://code.claude.com/docs/en/claude-projects"
    title: "Let Claude coordinate ongoing work with Projects"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Usage accounting and controls for projects. Settings are in the app, not `settings.json`; changes to instructions, repos, plugins and environment reach new threads only.

# How to use it

| Setting | Section |
| - | - |
| Name, icon, goal | General |
| Coordinator model and effort | General |
| Thread model and effort | General |
| Project instructions | Memory |
| Project repositories, Cloud environment | Environment |
| Plugins | Plugins |
| Usage (token use by thread and by model) | Usage |
| Memory files | Memory |
| Auto-continue when usage limits reset (on by default) | General |
| Restart Claude | General |
| Pause, Archive, Delete | General |

- Pause: interrupts all threads and the conversation, no new threads, scheduled tasks stop until Resume.
- Archive: hides project, archives threads (stopping running or PR-watching ones), scheduled tasks do not run; Unarchive from Projects page (threads stay archived until unarchived individually).
- Delete: permanent; removes threads, memory, files, turns off scheduled tasks; GitHub branches and PRs unaffected.
- Reduce usage: on Pro, Max and Ultra within plan limits the cache lifetime is an hour, so an idle thread re-reads its whole conversation on a follow-up; prefer a fresh thread for new work; use smaller model or lower effort; run fewer threads.

# Limits and defaults

- Usage counts against the same plan limits as other Claude Code sessions; a project cannot spend past them unless usage credits are turned on (a thread cannot turn them on).
- Enforced cap: 500 new threads per day across your projects. No fixed concurrent thread count.
- A thread or conversation stopped at the five-hour or weekly limit waits and continues automatically on reset unless auto-continue is off (project-wide).
- Idle PR-watching threads wake and use the plan when CI fails or a review comment arrives. An idle project with no running threads, watched PRs or messages uses none.
- "Additional usage credits are required" when a request needs credits (model or context size not in plan).
- "Claude hasn't responded" banner: click **Restart Claude**; a reply in progress is lost, threads unaffected.
