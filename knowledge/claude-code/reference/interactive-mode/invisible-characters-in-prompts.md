---
type: "Feature"
title: "Invisible character removal in prompts"
description: "Claude Code strips tag characters, bidi controls and zero-width characters from prompts on Enter."
resource: "https://code.claude.com/docs/en/interactive-mode#invisible-characters-in-prompts"
tags: [security, unicode, prompt, injection]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "Removed 3 invisible characters from your prompt"
  - "Removed 3 invisible characters · review and press Enter to send"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "interactive-mode"
    resource: "https://code.claude.com/docs/en/interactive-mode"
    title: "Interactive mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

On Enter, characters a terminal draws as nothing (tag characters, bidirectional controls, zero-width spaces) are removed from the prompt and from collapsed pasted-text references. Persian and Indic joiners and emoji-sequence selectors are kept.

# How to use it

A notice tells what happened: the first form (`Removed N invisible characters from your prompt`) means the prompt was sent cleaned if the input box is empty, or not sent if it is still there; the second (`... review and press Enter to send`) means nothing was sent and you confirm. A command-line prompt (`claude "fix the login bug"`) is cleaned and sent, but if the cleaned prompt would begin with `/` it is placed in the input box for review.
