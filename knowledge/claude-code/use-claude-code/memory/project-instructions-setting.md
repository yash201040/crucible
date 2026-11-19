---
type: "Reference"
title: "Project instructions setting values"
description: "The /config Project instructions setting and its pluginConfigs form that chooses between CLAUDE.md and AGENTS.md loading."
resource: "https://code.claude.com/docs/en/memory"
tags: [agents-md, settings, pluginconfigs, instructions]
kind: "setting"
maturity: "unlabelled"
since: "2.1.285"
surfaces: []
requires: "Claude Code v2.1.277 or later"
identifiers:
  - "Project instructions"
  - "claude-md-or-agents-md"
  - "claude-md-and-agents-md"
  - "claude-md"
  - "managed-only"
  - "pluginConfigs"
  - "cc-plugin-agents-md@builtin"
  - "agents-md@builtin"
  - "instructionFiles"
  - "/config"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "memory"
    resource: "https://code.claude.com/docs/en/memory"
    title: "How Claude remembers your project"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The **Project instructions** setting (in `/config`) controls which instruction files Claude reads. It applies from the next message and in every new session.

# How to use it

| Value | What Claude reads |
| :- | :- |
| `claude-md-or-agents-md` (default) | CLAUDE.md files, or AGENTS.md when no CLAUDE.md or CLAUDE.local.md is in the working directory or above |
| `claude-md-and-agents-md` | Both, each directory's CLAUDE.md first then its AGENTS.md; an already-loaded AGENTS.md (imported or symlinked) is not read twice |
| `claude-md` | CLAUDE.md only |
| `managed-only` | Only the managed CLAUDE.md and auto memory at launch; project, local and user CLAUDE.md, `.claude/rules/` and every AGENTS.md are left out; subdirectory CLAUDE.md, `.claude/rules/` and path-scoped rules still load on demand |

Settings-file form:

```
{"pluginConfigs": {"cc-plugin-agents-md@builtin": {"options": {"instructionFiles": "claude-md-and-agents-md"}}}}
```

Read from `~/.claude/settings.json`, a `--settings` file, or managed settings; ignored in project and local settings files.

# Notes

Before v2.1.285 the built-in plugin ID was `agents-md@builtin` and an entry under `cc-plugin-agents-md@builtin` was ignored; v2.1.285+ reads either. Use `agents-md@builtin` if earlier versions also read the file. To share one file with other tools, put `@AGENTS.md` in a `CLAUDE.md` (Claude-specific text below it) or symlink (`ln -s AGENTS.md CLAUDE.md`). The symlink has constraints: Edit and Write refuse to write through it (they direct Claude to edit `AGENTS.md`), and on Windows it needs Administrator or Developer Mode and Git may check it out as a plain text file unless `core.symlinks` is enabled, so use the import there.
