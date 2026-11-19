---
type: "Feature"
title: "Command history and reverse search"
description: "Per-directory prompt history, recovery of cleared drafts, and Ctrl+R search."
resource: "https://code.claude.com/docs/en/interactive-mode"
tags: [history, search, drafts, prompt]
kind: "ui"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "Ctrl+R"
  - "Ctrl+S"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "interactive-mode"
    resource: "https://code.claude.com/docs/en/interactive-mode"
    title: "Interactive mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Up-arrow recall of past prompts, stored per working directory and reaching prompts from past sessions of the same project.

# How to use it

- `/clear` starts a new session; recall lists the new session first, then earlier ones.
- Submitting the same prompt twice in a row records one entry. `!` history expansion is disabled by default.
- Recalled pasted text is resent in full unless cleaned up already.
- Cleared draft: press `Up` once on the still-empty prompt (v2.1.288+), or after sending press `Up` to step back; the ten most recent cleared drafts are kept for the session with pasted text and images (v2.1.292+), discarded on exit.
- `Ctrl+R`: in fullscreen rendering it opens a dialog (`Up`/`Down`, preview pane, `Ctrl+S` cycles scope this session / this project / all projects, `Enter` or `Tab` to place, `Esc` cancel). Classic renderer does inline search over all projects: `Ctrl+R` again for older matches, `Tab`/`Esc` accept, `Enter` accept and run, `Ctrl+C` cancel and restore.
- Searching a word inside a long pasted block works from v2.1.314.
