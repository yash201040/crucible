---
type: "Feature"
title: "Toggle fast mode and switch models"
description: "Turn fast mode on with /fast or the fastMode setting, how it persists, behaves in -p mode and follows model switches."
resource: "https://code.claude.com/docs/en/fast-mode"
tags: [fast-mode, slash-command, settings, headless]
kind: "mixed"
maturity: "research-preview"
since: "2.1.205"
surfaces: [cli, headless, ide, cloud]
requires: ""
identifiers:
  - "/fast"
  - "/fast on"
  - "/fast off"
  - "fastMode"
  - "--settings"
  - "claude -p --settings '{\"fastMode\": true}'"
  - "/config model=<model>"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "fast-mode"
    resource: "https://code.claude.com/docs/en/fast-mode"
    title: "Speed up responses with fast mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

How to switch fast mode on and off and how it interacts with model changes.

# How to use it

- CLI: run `/fast`, press Space to toggle, Enter to confirm; or set `"fastMode": true` in the user settings file on a supported model (on another model you stay on it with fast mode off; on Fable 5.2 the setting alone does nothing until you run `/fast` on Fable 5.2). The VS Code extension has a **Toggle fast mode** command when the model supports it; on the Anthropic API it saves to `fastMode`.
- Persistence (Anthropic API): fast mode turned on in an interactive session persists across sessions on a supported model; on Fable 5.2 only if turned on while using Fable 5.2. Reset each session with [per-session opt-in](./fast-mode-organization-controls.md).
- Non-interactive `-p`: `/fast` works only when the session was launched with fast mode in `--settings`, for example `claude -p --settings '{"fastMode": true}'`; applies to that session only and is not saved. Requires v2.1.205+. Elsewhere in non-interactive mode `/fast` reports it is not available.
- `/fast` can run while Claude works; the running turn finishes at its original speed and the change applies from the next turn. If the current model does not support fast mode, enabling it also switches the model (to Opus on the Anthropic API; used from the next request).
- Enabling shows "Fast mode ON", and a `↯` icon appears next to the prompt. `/fast` again shows the status. Disabling keeps your current model.
- Defaults: Opus 5.5 is the fast mode default from v2.1.280; before that, Opus 5 (from v2.1.219). Fable 5.2 fast mode needs v2.1.321+.
- Enable at session start for best cost efficiency.

# Limits and defaults

Model switches: switching to an unsupported model turns fast mode off (including Opus 4.7; before v2.1.221 it stayed on and the API rejected requests). Switching back restores it on a supported Opus model when the saved preference is on (with per-session opt-in, run `/fast`). Switching to Fable 5.2 turns it off unless it was turned on while using Fable 5.2. Every on/off shows `Fast mode ON` or `Fast mode OFF`, whether you use `/model`, `/config model=<model>` or Remote Control.
