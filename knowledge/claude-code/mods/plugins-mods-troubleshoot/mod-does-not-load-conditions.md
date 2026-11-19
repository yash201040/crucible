---
type: "Reference"
title: "Conditions that stop mods loading"
description: "Trust prompt not answered, --safe-mode, and hot reloading that stops being offered after three unanswered questions."
resource: "https://code.claude.com/docs/en/plugins/mods/troubleshoot"
tags: [mods, troubleshooting, trust, hot-reload]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "--safe-mode"
  - "askUserQuestionTimeout"
  - "AskUserQuestion"
  - "--plugin-dir"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-troubleshoot"
    resource: "https://code.claude.com/docs/en/plugins/mods/troubleshoot"
    title: "Troubleshoot a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Cases where no mod, or no installed plugin, loads at all.

# How to use it

- **No mod loads in a directory opened for the first time**: the trust prompt was not answered. Start an interactive session with `claude` there and accept it.
- **No installed plugin loads at all**: Claude Code was started with `--safe-mode`; start without the flag.
- **Claude Code stops asking to enable hot reloading**: after Claude writes a mod and nothing loads, if the question ends three times without an answer, hot reloading stays off. It ends that way when `askUserQuestionTimeout` is set and expires (the question uses the same dialog as `AskUserQuestion`). A question you dismiss yourself does not count. Workaround: copy the mod directory out of the mods folder and start `claude --plugin-dir ~/mods/git-branch`.

# Notes

The `--plugin-dir` form reloads on save and shows load lines in the transcript.
