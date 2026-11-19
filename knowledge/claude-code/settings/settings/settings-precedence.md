---
type: "Reference"
title: "Settings precedence and list merging"
description: "Order managed > command line > local > shared project > user, how lists merge, and special rules for model-list keys."
resource: "https://code.claude.com/docs/en/settings"
tags: [settings, precedence, merging, managed-settings]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.242"
surfaces: [cli, headless]
requires: ""
identifiers:
  - "--settings"
  - "fallbackModel"
  - "modelPicker"
  - "availableModels"
  - "deniedModels"
  - "modelSettings"
  - "effortLevel"
  - "permissions.allow"
  - "ANTHROPIC_MODEL"
  - "ANTHROPIC_DEFAULT_MODEL"
  - "spinnerTipsEnabled"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings"
    resource: "https://code.claude.com/docs/en/settings"
    title: "Settings files and precedence"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

When a key is set in several places the highest level wins; a lower-level key not set above it keeps its value.

# How to use it

1. Managed settings (file, MDM or server-managed): nothing in your files or `--settings` overrides a managed key; a flag such as `--model` can pick only from models the org allows. A managed `model` is a starting default, not a lock; the locks are `availableModels` and `deniedModels`. Multiple managed sources follow "precedence within the managed tier".
2. Command line: `--settings <file-or-json>`, one session. Other flags like `--model` set one thing and are not part of the stack.
3. Project local (`.claude/settings.local.json`).
4. Shared project (`.claude/settings.json`).
5. User (`~/.claude/settings.json`).

- Environment variables are not a level: pairing is decided per key. `ANTHROPIC_MODEL` in the shell beats the `model` key from any file; `ANTHROPIC_DEFAULT_MODEL` applies only when no file sets `model`. An `env` block inside a settings file is an ordinary key.
- Example: team's shared file sets `spinnerTipsEnabled: true`; put `false` in your `.claude/settings.local.json` to override for yourself; a managed `true` cannot be overridden; `claude --settings '{"spinnerTipsEnabled": true}'` wins over files for one session.

# Limits and defaults

Lists (e.g. `permissions.allow`) merge across files instead of overriding. Exceptions:

| Key | Rule |
| :- | :- |
| `fallbackModel` | ordered chain; whole value from the highest-precedence file that defines it |
| `modelPicker` | never merges; whole value from highest of managed, `--settings`, user; ignored in project and local (v2.1.242 or later) |
| `availableModels` | if applied managed settings define it, applied as-is, ignoring user/project/local entries (unless an embedding app supplies its own list); never merges across managed sources; merges normally across non-managed scopes |
| `modelSettings` | resolved one model at a time together with `effortLevel` |
