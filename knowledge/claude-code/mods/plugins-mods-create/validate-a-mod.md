---
type: "Feature"
title: "Validate a mod with claude plugin validate"
description: "Static analysis lists a mod's hooks, API calls, env and state access, and enforces rules on how hooks and calls are written."
resource: "https://code.claude.com/docs/en/plugins/mods/create"
tags: [mods, validate, static-analysis, rules]
kind: "cli_flag"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "claude plugin validate"
  - "hooks:"
  - "calls:"
  - "env reads:"
  - "env writes:"
  - "state reads:"
  - "state writes:"
  - "gating hook without .catch"
  - "$.state"
  - "claude-code"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-create"
    resource: "https://code.claude.com/docs/en/plugins/mods/create"
    title: "Create a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`claude plugin validate ./first-mod` checks the manifest and runs the same static analysis on the hooks module source that Claude Code runs on load, without running code or starting a session. Output lines: `hooks:` (events with filters in braces, e.g. `command.run{command=tally}`), `calls:` (every mods API method), `env reads:`/`env writes:`, `state reads:`/`state writes:` (if `$.state` is used), and one line per refusing hook such as `gating hook without .catch: tool.call`. A misspelled event shows as an error like `"tool.calls" is not an event`; an event missing from `hooks:` will not be called.

# Limits and defaults

Rules so static analysis finds every hook and call:
- Write API calls in full (`$.store.get('notes')`). `$` may be passed to a function declared at top level of the same file (`calls:` shows `$.store.get (via loadNotes)`); passing to a method, an inner function, or an imported function fails, except the `read` and `update` functions `$.state` uses. Do not assign `$` or a namespace to a variable, destructure, or index by computed name (`const ui = $.ui` fails with `$.ui is used as a value`).
- The event name in each `on` call must be a string literal (else `the event name passed to on() is not a string literal`).
- Inside `register`, do not redeclare `on` (`"on" is declared again (shadowed)`).
- Import only files inside the plugin directory by relative path; the one bare import allowed is `claude-code`.
- Use top-of-file `import` declarations; dynamic `import()` fails; use ES modules, not `require`.
