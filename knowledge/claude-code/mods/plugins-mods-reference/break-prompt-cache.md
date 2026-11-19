---
type: "Feature"
title: "breakPromptCache: send a changed prompt section or tool description"
description: "Return breakPromptCache: true after invalidating prompt.section or tool.describe so a running conversation reads changed text, at the cost of a prompt-cache restart."
resource: "https://code.claude.com/docs/en/plugins/mods/reference"
tags: [mods, prompt-cache, system-prompt, cost]
kind: "api"
maturity: "unlabelled"
since: "2.1.321"
surfaces: [cli, desktop, ide]
requires: ""
identifiers:
  - "breakPromptCache: true"
  - "$.ui.invalidate('prompt.section')"
  - "$.ui.invalidate('tool.describe')"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-reference"
    resource: "https://code.claude.com/docs/en/plugins/mods/reference"
    title: "Mods reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

To change a system prompt section or a tool description mid-conversation, call `$.ui.invalidate('prompt.section')` or `$.ui.invalidate('tool.describe')` so the hook reruns, and return `{ text, breakPromptCache: true }` or `{ description, breakPromptCache: true }`. Without the field, Claude keeps reading the text saved with the conversation for a section or an upfront-loaded tool until a new conversation or a compaction.

# Limits and defaults

- The changed text reaches Claude on the next turn and the prompt cache starts over, so that turn is slower and more expensive.
- Field requires v2.1.321+. From v2.1.299 until v2.1.321 a running conversation got the changed text on the next turn.
