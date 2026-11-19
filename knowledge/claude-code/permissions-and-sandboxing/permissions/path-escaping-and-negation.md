---
type: "Concept"
title: "Path escaping and ! negation"
description: "Approved paths are escaped; a deny or ask pattern starting with ! carves exceptions out of earlier rules from the same source."
resource: "https://code.claude.com/docs/en/permissions"
tags: [permissions, gitignore, negation, deny-rules]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "Read(!sample.env)"
  - "Edit(./Finance (2024)/**)"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permissions"
    resource: "https://code.claude.com/docs/en/permissions"
    title: "Configure permissions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

When you approve a path with "Yes, and don't ask again" Claude Code escapes `[`, `]`, `*` so the rule matches only that literal path. Rules you write are not escaped. Parentheses work (`Edit(./Finance (2024)/**)`). An allow rule whose path is not a usable gitignore pattern approves nothing.

# How to use it

A deny or ask pattern starting with `!` is a gitignore negation that carves paths out of earlier `path` or `./path` rules. In one settings file's deny list, `Read(*.env)` then `Read(!sample.env)` blocks every `*.env` except `sample.env`. A `!` rule listed first carves nothing.

# Limits and defaults

- Carve-outs reach only rules from the same source: `Read(!.env)` in project settings or `--disallowedTools` does not cancel a managed `Read(./.env)` deny.
- `!` patterns are read relative to the cwd even when `/`, `~/` or `//` follows, so `Read(!~/notes/public/**)` carves nothing out of `Read(~/notes/**)`.
- A carve-out cannot reopen a file inside a directory blocked as a whole: with `Read(secrets/**)` and `Read(!secrets/public/**)`, `secrets/public` stays blocked.
