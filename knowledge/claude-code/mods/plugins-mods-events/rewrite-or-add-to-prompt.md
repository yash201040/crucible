---
type: "Feature"
title: "Rewrite or add to a prompt (prompt.submit)"
description: "A prompt.submit hook can rewrite the prompt text, add Claude-only context, or drop the prompt."
resource: "https://code.claude.com/docs/en/plugins/mods/events"
tags: [mods, prompt, context, drop]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop, ide]
requires: ""
identifiers:
  - "prompt.submit"
  - "{ drop: 'the reason' }"
  - "prompt.section"
  - "prompt.context"
  - "skill.prompt"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-events"
    resource: "https://code.claude.com/docs/en/plugins/mods/events"
    title: "React to events with a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`prompt.submit` sees each prompt before the turn starts; `e.text` is what was typed.

# How to use it

| To do this | Return |
| :- | :- |
| Rewrite the prompt (transcript and history show new text) | `next({ ...e, text: newText })` |
| Add text only Claude reads, after the prompt | `next({ ...e, context: [...(e.context ?? []), extraText] })` |
| Stop the prompt | `{ drop: 'the reason' }` (text returns to prompt input; user sees `Prompt dropped by a hook:` plus reason) |

Other events cover the rest of what Claude reads: `prompt.section` (system prompt sections), `prompt.context` (context sent with the first message), `skill.prompt` (a skill's text).

# Limits and defaults

The prompt still goes through when a hook returns `drop` after its `next(e)` let it through (the hook fails with a message including `a drop after its next() was answered`), or when the hook throws or times out (add `.catch` to avoid sending).
