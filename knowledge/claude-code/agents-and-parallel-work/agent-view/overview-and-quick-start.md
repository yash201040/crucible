---
type: "Feature"
title: "Agent view overview and quick start"
description: "claude agents opens one screen listing all background sessions; dispatch, peek, attach and bring in existing sessions."
resource: "https://code.claude.com/docs/en/agent-view"
tags: [agent-view, background-sessions, dispatch, quick-start]
kind: "mixed"
maturity: "research-preview"
since: "2.1.139"
surfaces: [cli]
requires: ""
identifiers:
  - "claude agents"
  - "/bg"
  - "/background"
  - "defaultToAgentsView"
  - "claude \"<prompt>\""
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-view"
    resource: "https://code.claude.com/docs/en/agent-view"
    title: "Manage multiple agents with agent view"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Agent view, opened with `claude agents`, is one screen for all background sessions: what is running, what needs input, what is done. Each background session is a full Claude Code conversation that keeps running with no terminal attached. Introduced as a research preview in v2.1.139; the interface and shortcuts may change. Sessions run on your machine and you dispatch each one (for cloud-run parallel sessions the page points to Projects).

# How to use it

1. `claude agents` opens the view (an untrusted directory first shows the workspace trust dialog; declining exits). `Esc` returns to the shell, or to the conversation if the view was opened by backgrounding with `←`.
2. Type a prompt and press `Enter`: each prompt starts its own new session (a second prompt never follows up on the first). New sessions use the model shown in the header.
3. Select a row, press `Space` to peek, type a reply, `Enter` to send.
4. `Enter` or `→` attaches to the full conversation; `←` on an empty prompt detaches.
5. In an open regular session, `/bg` (alias `/background`) or `←` on an empty prompt moves it to agent view. In a fresh session with no messages `/bg` asks for a message first, while `←` works at once.

Footer hint in a regular session: `← for agents` for ten seconds after start; then `← N agents` counting sessions waiting on you (`← 99+ agents` above 99, refreshed about every ten seconds while focused); `← N done` briefly when sessions finish and none wait. `prefersReducedMotion` removes the colour change and the `done` count; screen reader mode hides the hint.

Open agent view by default: `/config` toggle "Open agents view by default" or `/config defaultToAgentsView=true`. Then bare `claude` opens agent view; `claude "fix the login test"` still starts a regular session. Turn off with `/config defaultToAgentsView=false`.

# Limits and defaults

Each session uses subscription quota independently. The default list shows every background session across all projects. Interactive sessions in other terminals do not appear until backgrounded; subagents and teammates are not listed as separate rows.
