---
type: "Feature"
title: "AskUserQuestion tool and question timeout"
description: "Multiple-choice questions to the user, with an optional auto-continue timeout."
resource: "https://code.claude.com/docs/en/tools-reference#askuserquestion-tool-behavior"
tags: [questions, timeout, unattended, interactive]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "AskUserQuestion"
  - "askUserQuestionTimeout"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "tools-reference"
    resource: "https://code.claude.com/docs/en/tools-reference"
    title: "Tools reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude asks multiple-choice questions; you pick an option or type text via the `Other` row or notes field. Questions stay open until answered by default.

# How to use it

Set `askUserQuestionTimeout` to `60s`, `5m` or `10m` in user `settings.json`, or via **Question auto-continue timeout** in `/config`. After that idle time the dialog submits any selected options and tells Claude you may be away, so Claude proceeds on its own judgment and may re-ask later. A countdown shows for the last 20 seconds; any key restarts it; the timer does not count while the terminal window is focused.

# Limits and defaults

The timer never starts in a background session, screen reader mode, or while connected to Remote Control; those questions wait. It applies only to `AskUserQuestion`; permission prompts, including plan approval, never auto-resolve on idle.
