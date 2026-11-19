---
type: "Guide"
title: "Changing a setting: /config, files, --settings"
description: "Three ways to change settings (the /config menu, editing JSON, per-session --settings, flags or env vars) and when edits take effect."
resource: "https://code.claude.com/docs/en/settings"
tags: [settings, config, cli-flags, hot-reload]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless]
requires: ""
identifiers:
  - "/config"
  - "/config verbose=true"
  - "--settings"
  - "--model"
  - "--effort"
  - "--append-system-prompt"
  - "ANTHROPIC_MODEL"
  - "ANTHROPIC_DEFAULT_MODEL"
  - "$schema"
  - "ConfigChange"
  - "apiKeyHelper"
  - "/model"
  - "/effort"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings"
    resource: "https://code.claude.com/docs/en/settings"
    title: "Settings files and precedence"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Settings can be changed from the `/config` menu, by editing a file, or for one session from the command line.

# How to use it

- `/config` (Config tab): a short list of personal options. Saved to `~/.claude/settings.json` (most), `.claude/settings.local.json` (a few, e.g. Show tips), or `~/.claude.json` (global config options). Set one directly with `/config verbose=true`. `/config` is terminal only; the VS Code chat panel and the desktop app do not open it.
- Edit files: strict JSON, so `//` comments or trailing commas are a Settings Error. Add `"$schema": "https://json.schemastore.org/claude-code-settings.json"` for editor validation (the schema can lag the newest CLI keys). Confirm with `/status`.
- One session, nothing saved: `--settings '<json-or-path>'` (applies above user, project and local, below managed; can set any key a user file can, not `Managed` or `Global config` keys), e.g. `claude --settings '{"model": "claude-opus-5-5"}'`; a per-key flag such as `--model`, or `--effort` for `effortLevel` and `modelSettings`; or the paired env var such as `ANTHROPIC_MODEL`. Each key's settings-reference entry lists overrides.
- `/model` saves the value as the new-session default; pressing `s` in the picker switches without saving. `/effort` saves some picks and not others (see the model-config docs).
- Claude Code's system prompt is not published; use `CLAUDE.md` or `--append-system-prompt` for standing instructions.

# Limits and defaults

- Files are watched and reloaded; most edits (including `permissions`, `hooks`, `apiKeyHelper`) apply mid-session without restart. A file created mid-session loads if its folder existed at start; for the project `.claude/` folder it loads even if created that session.
- Reload covers user, project, local and managed. The `ConfigChange` hook runs for direct file edits, not managed settings from MDM or the console, which reach running sessions on a per-source schedule.
- Some keys are read only at session start (e.g. admin `requiredMinimumVersion`). Use `/model` for `model` mid-session (each model has its own prompt cache, so the first request after a switch re-reads the conversation uncached); use `/effort` for `effortLevel` and `modelSettings`.
- Removing `permissions.blockReadsOutsideWorkingDirectories` mid-session does not lift the block; remove it from every file and restart each running session.
