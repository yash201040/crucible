---
type: "Feature"
title: "PostModelSwitch hook event"
description: "Runs after the session model changes, including automatic fallback and resume; adds guidance for the next request."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, model, fallback, context]
kind: "hook"
maturity: "unlabelled"
since: "2.1.251"
surfaces: [cli, sdk]
requires: "Claude Code v2.1.251 or later"
identifiers:
  - "PostModelSwitch"
  - "auto"
  - "resume"
  - "opusplan"
  - "requested_model"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Runs after the session's model changes, to give Claude model-specific guidance without editing every CLAUDE.md. It cannot block. Fires after: a switch you or a client requested; an automatic model fallback; a setting such as `opusplan` entering or leaving plan mode; Claude Code restoring the model on resume. It does not fire when a model from a fallback model chain serves a single turn (the session's model is unchanged).

# How to use it

Matcher follows the PreModelSwitch rules (canonical name of the target model). Input is the same as [PreModelSwitch](./p2-premodelswitch-event.md) with `hook_event_name` `"PostModelSwitch"` and two extra `source` values: `"auto"` (automatic fallback or other self-made change; `requested_model` is `null`) and `"resume"` (model restored on resume; `requested_model` is the saved setting restored).

Plain stdout on exit 0, or `hookSpecificOutput.additionalContext`, is delivered to Claude with the next request after the switch. Example: matcher `.*opus.*` echoing "On Opus, delegate implementation work to subagents and keep this conversation for planning and review."

# Limits and defaults

- If the hook has not finished within five seconds after you send the next prompt, that request is sent without the output and it attaches to the following request instead.
- If the model changes several times before the next request, only the output for the last switch's target model is delivered.
