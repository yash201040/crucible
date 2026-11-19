---
type: "Feature"
title: "Shell mode with the ! prefix"
description: "Run a shell command directly from the prompt, add its output to context and have Claude respond."
resource: "https://code.claude.com/docs/en/interactive-mode#shell-mode-with--prefix"
tags: [shell, bang, prompt, sandbox]
kind: "ui"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "!"
  - "respondToBashCommands"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "interactive-mode"
    resource: "https://code.claude.com/docs/en/interactive-mode"
    title: "Interactive mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Prefix input with `!` (for example `! npm test`) to run a command without Claude interpreting or approving it. The command and output enter the conversation context.

# How to use it

- Supports `Ctrl+B` backgrounding, `Tab` completion from earlier `!` commands in the project, and live file-path completion for tokens containing `/`.
- Exit with `Escape`, `Backspace` or `Ctrl+U` on an empty prompt. Pasting text that starts with `!` into an empty prompt enters shell mode.
- Claude responds to the output automatically, costing the same as a normal prompt. Set `respondToBashCommands` to `false` in `settings.json` to add output without a response.

# Limits and defaults

Shell-mode commands run outside the sandbox even with sandboxing enabled (except in sessions under strict sandbox mode), because the sandbox covers commands Claude runs.
