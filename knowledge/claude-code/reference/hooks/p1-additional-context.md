---
type: "Feature"
title: "Adding context for Claude from a hook"
description: "additionalContext injects a string into Claude's context as a system reminder; where it lands per event and how it persists across resume."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, context, additionalcontext, resume]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "additionalContext"
  - "hookSpecificOutput"
  - "--continue"
  - "--resume"
  - "--fork-session"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`hookSpecificOutput.additionalContext` passes a string into Claude's context, wrapped in a system reminder and inserted where the hook fired. Claude reads it on the next model request; it is not shown as a chat message.

# How to use it

`{"hookSpecificOutput":{"hookEventName":"PostToolUse","additionalContext":"This file is generated. Edit src/schema.ts and run `bun generate` instead."}}`

Where it appears:
- `SessionStart`, `SubagentStart`: at conversation start, before the first prompt
- `UserPromptSubmit`, `UserPromptExpansion`: alongside the submitted prompt
- `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PostToolBatch`: next to the tool result
- `Stop`, `SubagentStop`: end of turn; the conversation continues so Claude can act
- `PostModelSwitch`: with the next request after the switch

Several hooks returning values for one event: Claude receives all. Good uses: environment state, conditional project rules, external data. For unchanging instructions prefer CLAUDE.md. Write factual statements, not imperative system-style commands, which can trigger prompt-injection defenses so Claude surfaces the text to you instead.

# Limits and defaults

- Over 10,000 characters: saved to a file in the session directory, Claude gets the path and a preview of up to 2,000 characters.
- A `<system-reminder>` tag inside the string has its `<` replaced by `&lt;`.
- The injected text is saved in the transcript. On `--continue`/`--resume`, mid-session events (`PostToolUse`, `UserPromptSubmit`) replay the saved text instead of re-running, so timestamps or SHAs go stale. `SessionStart` runs again with `source` `"resume"` (or `"fork"` with `--fork-session`) and can refresh.
