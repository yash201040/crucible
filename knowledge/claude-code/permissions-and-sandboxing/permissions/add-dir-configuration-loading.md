---
type: "Reference"
title: "What --add-dir directories load"
description: "Additional directories grant file access only; flag-added ones also load skills, commands, subagents and a few settings keys."
resource: "https://code.claude.com/docs/en/permissions"
tags: [permissions, add-dir, skills, subagents, configuration]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.257"
surfaces: [cli, sdk]
requires: ""
identifiers:
  - "CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD"
  - "--add-dir"
  - "/add-dir"
  - "add_dirs"
  - "additionalDirectories"
  - "--setting-sources"
  - "settingSources"
  - ".claude/skills/"
  - ".claude/commands/"
  - ".claude/agents/"
  - "enabledPlugins"
  - "extraKnownMarketplaces"
  - "CLAUDE.local.md"
  - ".claude/rules/"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permissions"
    resource: "https://code.claude.com/docs/en/permissions"
    title: "Configure permissions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Adding a directory extends where Claude can read and edit; it does not make it a configuration root. The exceptions apply only to directories added with `--add-dir` or `/add-dir`, not to `permissions.additionalDirectories` entries in settings (file access only). The Agent SDK options `additionalDirectories` (TypeScript) and `add_dirs` (Python) pass each entry as `--add-dir`, so they get the exceptions too.

# How to use it

| Configuration | Loaded from `--add-dir` |
| :- | :- |
| Skills in `.claude/skills/` | Yes, with live reload |
| Command files in `.claude/commands/` | Yes, no live reload; same-name project command wins |
| Subagents in `.claude/agents/` | Yes, no live reload |
| `.claude/settings.json` and `.claude/settings.local.json` | Only `enabledPlugins` and `extraKnownMarketplaces` |
| `CLAUDE.md` files, `.claude/rules/`, `CLAUDE.local.md` | Only with `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1`; `CLAUDE.local.md` also needs the `local` setting source (on by default) |

Skills, commands and subagents load through the `project` setting source, so excluding it with `--setting-sources` or SDK `settingSources` stops them; bare mode skips the commands and subagents.

To load skills, commands and subagents from a subdirectory of the primary working directory mid-session, run `/add-dir` with its path; they load for the rest of the session without adding a working directory. Needs v2.1.257+.

# Notes

Where other config loads from: output styles from the cwd and parents, `~/.claude/` and managed settings. Hooks and other `.claude/settings.json` keys load from the cwd's `.claude/` only (no parent fallback), plus user and managed settings. `.claude/settings.local.json` loads from the git repository root (except where the repository root is not used, such as Windows). To share config across projects use `~/.claude/agents/`, `~/.claude/output-styles/`, `~/.claude/settings.json`, plugins, or launch from the config directory.
