---
type: "Concept"
title: "Precedence between env variables, settings and flags"
description: "Which source wins when a behavior can be set by an environment variable, a settings key, a CLI flag or an in-session command."
resource: "https://code.claude.com/docs/en/env-vars"
tags: [precedence, env, settings, override]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers: []
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "env-vars"
    resource: "https://code.claude.com/docs/en/env-vars"
    title: "Environment variables"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Rules for resolving conflicts between an environment variable and the settings key, flag or command that sets the same behavior. The winner differs per key, so each variable's row states it.

# How to use it

- `ANTHROPIC_MODEL` and `CLAUDE_CODE_AUTO_CONNECT_IDE`: the variable is read first; the `model` or `autoConnectIde` setting is used only when the variable is unset.
- `--model` and `/model` override `ANTHROPIC_MODEL`.
- `CLAUDE_CODE_EFFORT_LEVEL` overrides `--effort` and `/effort`.
- Same variable in shell and in a settings `env` block: the settings value usually wins, because Claude Code writes each `env` entry into the process environment, replacing the inherited value. Some sessions keep the inherited value; see settings-reference sections "How env values interact with your shell" and "When Claude Code applies env values".
- Between settings files, `env` follows settings precedence: managed settings override user or project settings.
- Project and local settings cannot set some variables (for example `CLAUDE_CONFIG_DIR` and the OpenTelemetry exporter variables); see "Variables Claude Code ignores in env" in the settings reference.
- A settings file can set a variable but not remove one. To override one you cannot unset (such as a stale `CLAUDE_CODE_USE_VERTEX` from a shell profile), set it to an empty string in `env`: `"CLAUDE_CODE_USE_VERTEX": ""`. Provider selection treats empty as unset, but subprocesses still inherit the empty value.

# Notes

Shell changes need a relaunch; `env` entries in settings files are reapplied to a running session when the file changes (startup-only features excepted).
