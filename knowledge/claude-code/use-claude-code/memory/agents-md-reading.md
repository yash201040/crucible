---
type: "Feature"
title: "Reading AGENTS.md as project instructions"
description: "Claude Code reads AGENTS.md directly when no CLAUDE.md is present; rules for which files count, what is read and when it is unavailable."
resource: "https://code.claude.com/docs/en/memory"
tags: [agents-md, instructions, compatibility, hooks]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.277"
surfaces: []
requires: "Claude Code v2.1.277 or later"
identifiers:
  - "AGENTS.md"
  - ".claude/AGENTS.md"
  - "AGENTS.local.md"
  - "AGENTS.override.md"
  - "InstructionsLoaded"
  - "/import"
  - "/memory"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "memory"
    resource: "https://code.claude.com/docs/en/memory"
    title: "How Claude remembers your project"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A repository set up for other agents works without a CLAUDE.md. Default behavior:

| Repository has | Claude reads |
| :- | :- |
| `AGENTS.md`, no `CLAUDE.md`/`CLAUDE.local.md` in working dir or above | `AGENTS.md` |
| `AGENTS.md` plus a `CLAUDE.md` or `CLAUDE.local.md` | `CLAUDE.md` files only |
| `CLAUDE.md` that imports `AGENTS.md` | `CLAUDE.md`, with `AGENTS.md` via the import |

# How to use it

- Files that count as CLAUDE.md for the check: `CLAUDE.md`, `.claude/CLAUDE.md`, `CLAUDE.local.md` in the working directory or above. Do not count: `~/.claude/CLAUDE.md`, the managed CLAUDE.md, `.claude/rules/` files.
- When none count: at start Claude reads every `AGENTS.md` and `.claude/AGENTS.md` in the working directory and above (an interactive line like `no CLAUDE.md found; AGENTS.md loaded: <path>` is shown); a subdirectory `AGENTS.md` loads when Claude opens a file there via Read and the subdirectory has none of the three CLAUDE.md files. `@path` imports and `claudeMdExcludes` apply; subagents that start without project instructions also skip these files.
- Not read: `AGENTS.local.md`, `AGENTS.override.md`, anything under `.agents/`.
- Adding a `CLAUDE.local.md` stops Claude reading `AGENTS.md` unless [Project instructions](./project-instructions-setting.md) is `claude-md-and-agents-md`.
- Check with `/memory`. Before v2.1.280, `/memory` and `/context` did not list an AGENTS.md read directly.

# Limits and defaults

Unavailable (CLAUDE.md only; setting hidden in `/config`): version before v2.1.277; built-in plugin disabled with `/plugin`; sometimes the first session after upgrading from v2.1.276 or earlier. Before v2.1.281, some sessions (Amazon Bedrock, telemetry disabled) read CLAUDE.md only.

Differences from CLAUDE.md: `InstructionsLoaded` hooks do not fire for an AGENTS.md read via the setting (they fire for one imported or symlinked by a CLAUDE.md); with `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD` set, `--add-dir` directories' AGENTS.md do not load; an `@path` import outside the working directory loads only if external imports were already approved, with no prompt.

# Notes

Earlier workarounds: a `CLAUDE.md` with `@AGENTS.md` can stay (never read twice); a CLAUDE.md that only tells Claude in words to read AGENTS.md should be replaced; a symlink is harmless; a `SessionStart` hook that prints AGENTS.md should be removed (duplicate context). `/init` incorporates `.cursor/rules/`, `.cursorrules`, `.github/copilot-instructions.md`, and with `CLAUDE_CODE_NEW_INIT=1` also `AGENTS.md`, `.devin/rules/`, `.windsurf/rules/`, `.windsurfrules`, `.clinerules`. `/import` copies a supported agent's config once (instruction files appended to CLAUDE.md, plus MCP servers, commands, subagents, skills).
