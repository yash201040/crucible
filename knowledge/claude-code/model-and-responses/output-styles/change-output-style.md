---
type: "Feature"
title: "Change your output style"
description: "Select a style with /output-style, /config, the VS Code menu or the outputStyle setting; case rules, persistence and timing."
resource: "https://code.claude.com/docs/en/output-styles#change-your-output-style"
tags: [output-styles, settings, headless, remote-control]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.251"
surfaces: [cli, headless, sdk, ide, desktop, web, mobile]
requires: "/output-style in -p, SDK and Remote Control needs v2.1.269+; VS Code menu needs v2.1.257+"
identifiers:
  - "/output-style"
  - "/output-style <style>"
  - "/config"
  - "outputStyle"
  - ".claude/settings.local.json"
  - "~/.claude/settings.json"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "output-styles"
    resource: "https://code.claude.com/docs/en/output-styles"
    title: "Output styles"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Ways to pick the active output style. The command and both menus save the choice to `.claude/settings.local.json` (local project level).

# How to use it

- `/output-style <style>`, e.g. `/output-style concise`; with no argument it lists styles and marks the current one. Ignores case. Also works in non-interactive mode and Agent SDK sessions, and from mobile app or web via Remote Control where only built-in styles can be listed and selected (v2.1.269+).
- Terminal: `/config` then **Output style**.
- VS Code: `/` command menu, **Output styles** (includes custom styles; v2.1.257+).
- Desktop app: set `outputStyle` in a settings file (e.g. `.claude/settings.local.json`); `/config` there opens Settings > Code or Settings > Claude Code instead of a menu.
- Settings file: `{ "outputStyle": "Explanatory" }`.

# Limits and defaults

- The `outputStyle` value is case-sensitive (`Proactive`, `Concise`, `Explanatory`, `Learning`); a non-matching value such as `explanatory` gives the Default style.
- Cross-project default: set `outputStyle` in `~/.claude/settings.json`; a project's settings take precedence.
- Switching mid-session applies from the next message (before v2.1.251 only after `/clear` or a new session); see prompt-caching docs for the first-message cost.
