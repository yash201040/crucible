---
type: "Feature"
title: "Emoji shortcodes"
description: "Typing :name: inserts an emoji; a suggestion popup appears after two characters."
resource: "https://code.claude.com/docs/en/interactive-mode#emoji-shortcodes"
tags: [emoji, prompt, settings]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "emojiCompletionEnabled"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "interactive-mode"
    resource: "https://code.claude.com/docs/en/interactive-mode"
    title: "Interactive mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A complete shortcode such as `:heart:` is replaced when the closing `:` is typed; `:` plus at least two characters opens a popup (`Tab` or `Enter` to insert). The shortcode must start the input or follow a space.

# How to use it

Turn off both popup and inline replacement with `"emojiCompletionEnabled": false` in `settings.json`.
