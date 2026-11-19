---
type: "Reference"
title: "Module load errors"
description: "Messages when a mod's hooks module fails to load: missing modules key, load failure, userConfig mismatch, 2000-scope nesting, stack and parser errors."
resource: "https://code.claude.com/docs/en/plugins/mods/troubleshoot"
tags: [mods, troubleshooting, load-errors, limits]
kind: "limit"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "hooks/hooks.json"
  - "\"modules\": [\"./register.js\"]"
  - "hooks module did not load"
  - "; the version loaded before is unloaded"
  - "/reload-plugins"
  - "options do not fit plugin.json userConfig"
  - "pluginConfigs"
  - "code nested too deep to scan: more than 2000 scopes"
  - "the engine ran out of stack linking the file and its imports"
  - "the parser stopped"
  - "the engine ran out of stack loading the file"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-troubleshoot"
    resource: "https://code.claude.com/docs/en/plugins/mods/troubleshoot"
    title: "Troubleshoot a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Errors where the mod's hooks module cannot be loaded. Each line starts with the mod's name.

# How to use it

| Symptom or message | Cause and fix |
| :- | :- |
| `validate` passes and lists no `hooks` line | `hooks/hooks.json` has no `modules` key or it is misspelled. Add `"modules": ["./register.js"]` |
| `hooks module did not load: <reason>` | Module could not load, e.g. top-level code threw; a syntax error gives file and line. If the reason ends `; the version loaded before is unloaded`, no version runs; fix, then run `/reload-plugins` |
| `hooks module did not load: options do not fit plugin.json userConfig: <reason>` | An option fails its `userConfig` field (e.g. number above `max`, missing required value). Set or change it; the line ends with its `pluginConfigs` entry in `settings.json` |
| `code nested too deep to scan: more than 2000 scopes` | A hooks-module file nests scopes (functions, blocks, loops) more than 2,000 deep; `claude plugin validate` reports it too. Rewrite shallower |
| `the engine ran out of stack linking the file and its imports` | Code too deeply nested or import chain too long; shorten |
| `code nested too deep to scan (the parser stopped: <message>)` or `the engine ran out of stack loading the file (code nested too deep): <message>` | One file nested so deeply the stack ran out; no line number is given, find the deepest code and flatten it |

If you installed the mod and did not write it, ask its author to fix it.

# Notes

Related: [refusal messages](./refusal-messages.md).
