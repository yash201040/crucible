---
type: "Feature"
title: "Side questions with /btw"
description: "Ask a tool-less question answered from current context without adding to conversation history."
resource: "https://code.claude.com/docs/en/interactive-mode#side-questions-with-btw"
tags: [btw, side-question, context, subagents, forks]
kind: "slash_command"
maturity: "unlabelled"
since: "2.1.227"
surfaces: [cli, ide]
requires: ""
identifiers:
  - "/btw"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "interactive-mode"
    resource: "https://code.claude.com/docs/en/interactive-mode"
    title: "Interactive mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`/btw <question>` answers from what is already in the conversation (messages, replies, tool results). Question and answer never enter history. It runs even while Claude is working, without interrupting the turn, and sees the conversation except the reply still being written.

# How to use it

- No tool access: it cannot read files, run commands or search. Single response; ask again to continue.
- Cheap while the prompt cache is warm. Each ask replays the newest 20 earlier side-question exchanges; the five newest show dimmed above the answer.
- Overlay keys: `Space`/`Enter`/`Escape` dismiss; `Up`/`Down` scroll; `Shift+Left`/`Shift+Right` (or `[` `]`, `Tab`/`Shift+Tab`) step between answers (v2.1.257+; v2.1.187 to v2.1.256 used plain `Left`/`Right`); `c` copy raw Markdown; `f` fork into a background subagent that inherits the conversation plus this Q&A with full tools (local sessions only); `x` clear earlier exchanges. `/btw` with no question reopens the overlay.
- In VS Code `/btw` opens a panel that survives reloads (extension v2.1.227+).
- In an attached background session `Left` detaches (v2.1.257+); the side question keeps running.
- With a subagent transcript open, `/btw` answers from that transcript (v2.1.314+); from an agent team teammate's transcript it answers from the main conversation.

# Notes

Use `/btw` for what Claude already knows; use a subagent to find out something new; a fork starts from a copy of the conversation.
