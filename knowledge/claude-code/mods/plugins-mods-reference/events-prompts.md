---
type: "Reference"
title: "Events: prompts and what Claude reads"
description: "Prompt events for typed text and Claude Code's own system prompt, context, attachments, @-mentions and attribution."
resource: "https://code.claude.com/docs/en/plugins/mods/reference"
tags: [mods, events, prompts, system-prompt]
kind: "hook"
maturity: "unlabelled"
since: "2.1.290"
surfaces: [cli, desktop, ide]
requires: ""
identifiers:
  - "prompt.submit"
  - "prompt.fill"
  - "prompt.suggest"
  - "prompt.edit"
  - "prompt.autocomplete"
  - "prompt.compose"
  - "prompt.section"
  - "prompt.context"
  - "prompt.attachment"
  - "prompt.mention"
  - "skill.prompt"
  - "attribution.text"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-reference"
    resource: "https://code.claude.com/docs/en/plugins/mods/reference"
    title: "Mods reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

| Event | Fires when | A hook can return |
| :- | :- | :- |
| `prompt.submit` | a prompt is submitted | `next({ ...e, text })`, `next({ ...e, context })`, `{ drop: reason }` |
| `prompt.fill`, `prompt.suggest` | text goes into the prompt box as draft or dim suggestion | `next(e)` with changed text |
| `prompt.edit` | user edits the prompt box | `next(e)` |
| `prompt.autocomplete` | user types and a word ends at the cursor (`e.token`); Claude Code does not wait, its rows show first | `{ suggestions }`: list of `{ text, label, description }` shown below; choosing writes `text` over the word |
| `prompt.compose` | a system prompt is rendered | `{ sections }`: list of `{ id, text, scope }` in send order |
| `prompt.section` | once per named system prompt section (`e.name` is the `id`) | `{ text }`, or `{ text: null }` to omit; add `breakPromptCache: true` to send a change next turn |
| `prompt.context` | once per conversation, context sent with first message | `{ blocks }` |
| `prompt.attachment` | Claude Code adds its own message, such as a reminder (`e.type` kind, `e.detail` facts) | `{ text }` or `{ text: null }` |
| `prompt.mention` | Claude Code is about to read an @-mentioned file; needs v2.1.290+ | `next({ ...e, path })` or `{ deny: reason }` |
| `skill.prompt` | a skill's text is expanded for Claude | `{ text }` |
| `attribution.text` | commit or PR attribution text is composed | `{ text }` |
