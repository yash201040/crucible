---
type: "Reference"
title: "prompt.md frontmatter fields"
description: "Every frontmatter field of an eval case's prompt.md with defaults; an unknown key is an error."
resource: "https://code.claude.com/docs/en/plugin-evals"
tags: [evals, frontmatter, reference, limits]
kind: "frontmatter"
maturity: "unlabelled"
since: ""
surfaces: [headless]
requires: ""
identifiers:
  - "schema_version"
  - "name"
  - "description"
  - "tags"
  - "plugins"
  - "runs"
  - "expected_outcome"
  - "model"
  - "max_turns"
  - "timeout_seconds"
  - "allowed_tools"
  - "append_system_prompt"
  - "env"
  - "EVAL_*"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugin-evals"
    resource: "https://code.claude.com/docs/en/plugin-evals"
    title: "Test plugins with evals"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The body of `prompt.md` is the exact prompt Claude receives. Frontmatter fields:

# How to use it

| Field | Default | Purpose |
| :- | :- | :- |
| `schema_version` | `"1.1"` set for you | Case format version |
| `name` | directory name | Case name; `--case` globs match it |
| `description` | | Humans only |
| `tags` | `[]` | `--tag` filtering; a case runs if any tag matches |
| `plugins` | nearest enclosing plugin | Plugin directories under test relative to the case dir, e.g. `plugins: ["../.."]` |
| `runs` | `3` | Runs per arm, 1 to 50; `--runs` overrides |
| `expected_outcome` | | Humans only |
| `model` | child session default | Model for agent under test; `--model` overrides |
| `max_turns` | `10` | Turn cap, up to 200; hitting it is a run error that usually lowers the score |
| `timeout_seconds` | `300` | Wall-clock cap per run, up to 3600 |
| `allowed_tools` | `[]` | Tools the case wants; read-only ones granted when listed here |
| `append_system_prompt` | | Appended to the child session system prompt |
| `env` | `{}` | Extra env vars; keys must match `EVAL_[A-Z0-9_]*` or the run fails |

# Limits and defaults

The run inherits only an allowlist from your shell: basics like `PATH` and locale, proxy and certificate settings, variables selecting and authenticating the model provider, most `ANTHROPIC_*` and `CLAUDE_CODE_*` configuration, and `EVAL_*`. Pass anything else (e.g. a toolchain setting) as an `EVAL_*` variable.
