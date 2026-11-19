---
type: "Reference"
title: "Fast mode and ultracode settings"
description: "fastMode, fastModePerSessionOptIn and ultracode: speed-for-cost fast mode and automatic workflow planning."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [fast-mode, ultracode, workflows, settings]
kind: "setting"
maturity: "unlabelled"
since: "2.1.284"
surfaces: [cli, headless, ide, cloud]
requires: "ultracode needs dynamic workflows enabled and a model supporting xhigh effort; off/no-cap forms v2.1.284"
identifiers:
  - "fastMode"
  - "fastModePerSessionOptIn"
  - "ultracode"
  - "CLAUDE_CODE_DISABLE_FAST_MODE"
  - "/fast"
  - "/effort ultracode"
  - "/effort ultracode off"
  - "--effort ultracode"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`fastMode` turns on fast mode (faster, higher cost per token) where available. `ultracode` makes Claude plan a workflow for each substantive task unprompted.

# How to use it

| Key | Type | Default | What it does |
| :- | :- | :- | :- |
| `fastMode` | Boolean | unset (off) | `/fast` writes `true` to `~/.claude/settings.json`; turning it off removes the key. On Fable 5.2 you must also run `/fast` while using it |
| `fastModePerSessionOptIn` | Boolean | `false` | `true`: a saved `fastMode: true` no longer enables fast mode at start; each person runs `/fast` per session. `fastMode: true` passed via `--settings` still counts unless managed settings set this key |
| `ultracode` | Boolean | unset (off) | Sessions start with ultracode on. Claude Code reads but never writes it |

# Limits and defaults

- On the Anthropic API only Fable 5.2, Opus 5.5, Opus 5 and Opus 4.8 support fast mode; `/fast` from another model switches to Opus and switching to an unsupported model turns it off. On Google Cloud Agent Platform `/fast` switches to Fable 5.2, writes no key, and a saved `true` is ignored.
- `CLAUDE_CODE_DISABLE_FAST_MODE` turns fast mode off for a session; the key cannot re-enable it.
- With `fastModePerSessionOptIn` set by managed settings (Team or Enterprise owners can deploy via server-managed settings), `/fast on` is refused in non-interactive mode, the VS Code extension and cloud sessions.
- `ultracode` runs at whichever effort the session uses and does not change it; an effort cap lowers the level without turning ultracode off. Before v2.1.284 `ultracode: true` ran at `xhigh`, and a cap below `xhigh` kept it off.
- Per-session: `/effort ultracode` (one session), `/effort ultracode off` (turns off for one session when the key is `true`), `--effort ultracode` (on at `xhigh`). An Agent SDK `apply_flag_settings` control request also accepts the key.
