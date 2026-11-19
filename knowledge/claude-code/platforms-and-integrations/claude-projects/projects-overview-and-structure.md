---
type: "Feature"
title: "Projects: a coordinator conversation with parallel threads"
description: "A project is one long-running conversation where Claude starts and tracks parallel cloud-session threads sharing instructions, repositories and memory."
resource: "https://code.claude.com/docs/en/claude-projects"
tags: [projects, threads, coordination, cloud, beta]
kind: "behavior"
maturity: "beta"
since: ""
surfaces: [web, desktop, mobile, cloud]
requires: "Pro, Max or Ultra plan (not Team or Enterprise); rolling out gradually"
identifiers:
  - "Overview pane"
  - "Library"
  - "Work locally"
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

Projects are in public beta. A project is one coordinating conversation plus the threads it starts. The conversation (coordinator) takes tasks, decides what becomes a thread, tracks threads, and sees what threads report, not every step. Each thread is a separate session with its own context window, usually a cloud session on its own branch (opening a PR when warranted); a thread can instead run on the user's own computer via Remote Control. Threads run in parallel and can be steered from a phone.

Every cloud thread starts with: the project's repositories and files, instructions and memory; each repo's `CLAUDE.md`; the connectors on the claude.ai account; and the project's cloud environment.

# How to use it

- Send work in the conversation: quick questions answered in place; new work goes to a new thread or an existing thread in that area; unrelated tasks in one message become separate threads. Sometimes Claude lists **Suggested threads**.
- Overview pane groups threads: Ready for review, Waiting on you, Working, Landing, Idle, Resolved (marked done by the user, by Claude, or automatically after a week of inactivity). Library holds uploaded files and thread outputs; Scheduled tasks lists cloud scheduled tasks Claude set up.
- Open a thread to read it, steer in its own message box (follow-ups in the project conversation reach it only if Claude matches them), answer its permission prompts, or interrupt with Stop or Esc.
- Default thread behavior with code: new branch from default branch; PR when asked (or on its own for a concrete fix); then watches the PR with auto-fix on, whether or not auto-fix is on for other cloud sessions.
- Notifications (desktop): by default on Claude posts, thread errors or thread needs input; optional per turn finished.

# Limits and defaults

- Not in the terminal CLI, VS Code extension, JetBrains plugin, or via Bedrock, Google Cloud Agent Platform or Foundry.
- One project belongs to one user; no sharing, no org-level controls in beta. A thread belongs to one project; cannot be moved or merged; projects cannot be merged. You cannot add a session you started on your machine, only bring its work in.
- A cloud thread's sandbox pauses between turns; if it cannot resume, the thread continues from a fresh clone and uncommitted changes can be lost, so ask Claude to commit and push progress.
- Compared with related features: subagents live inside one session; agent teams end with one task; Claude Tag is a shared Slack identity on Team and Enterprise; agent view tracks local sessions you start yourself.
