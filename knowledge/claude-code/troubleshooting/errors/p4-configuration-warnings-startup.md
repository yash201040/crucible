---
type: "Reference"
title: "Startup configuration warnings (skills, agents, trust, paths)"
description: "Startup notices: interface error exit, agent descriptions over 15.0k tokens, unquoted asyncRewake hook paths, unloaded instruction files, reserved or refused names, trust, network paths."
resource: "https://code.claude.com/docs/en/errors"
tags: [errors, warnings, startup, skills, subagents]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.305"
surfaces: [cli, headless]
requires: ""
identifiers:
  - "--debug-file"
  - "--debug"
  - "CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN"
  - "asyncRewake"
  - "anthropic-skills"
  - ".claude/commands/"
  - "permissions.allow"
  - "permissions.additionalDirectories"
  - "hasTrustDialogAccepted"
  - "permissions.blockReadsOutsideWorkingDirectories"
  - ".config.json"
  - "~/.claude.json"
  - "--add-dir"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Warnings Claude Code emits at startup. Where to find them: a row below the startup banner (some permission-rule warnings), the debug log (`claude --debug-file <path>`), or stderr in non-interactive `-p` text output outside background sessions. Before v2.1.305 interactive sessions printed them on stderr too.

# How to use it

| Warning | Cause | Fix |
|---|---|---|
| `Claude Code exited after an unrecoverable interface error` | Terminal UI error in either renderer; if during fullscreen start, the next launch uses the classic renderer (`CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN=1` forces it). Before v2.1.236 it exited silently | Restart; `claude --resume` |
| `Agent descriptions are over the 15.0k-token limit` | Combined name plus `description` of non-built-in subagents exceeds 15,000 tokens (estimated); every agent still loads | Shorten descriptions or remove agents |
| `<Event> hook needs quotes around a path with a space (check.py)` | Shell-form `asyncRewake` hook with an interpreter plus unquoted path placeholder whose path has a space; script did not run | Quote: `"command": "python3 \"${CLAUDE_PLUGIN_ROOT}/hooks/check.py\""` |
| `Instruction file not loaded (...)` | A memory file exists but a Read deny rule covers it, it is outside working directories with `permissions.blockReadsOutsideWorkingDirectories` on, or its link target could not be worked out; counts extras as `and N more instruction files not loaded` (before v2.1.292 the file was named at the end of the line) | Narrow the rule, move the file inside, or fix the link; start a new session |
| `Not loaded: rename ... "anthropic-skills"` | Skill, command or saved workflow named `anthropic-skills` or `anthropic-skills:*` (reserved for claude.ai synced skills); before v2.1.282 they loaded | Rename and restart |
| `N skill or command name refused` | Name has hidden, direction-changing or blank-like characters, `<` `>`, or exceeds 256 characters. Not loaded, or a frontmatter `name` ignored while the skill loads | `claude --debug`, search the log for `[names]`; rename |
| `Ignoring N permissions.allow entries from .claude/settings.local.json: this workspace has not been trusted` | Project allow rules and `permissions.additionalDirectories` need workspace trust; deny and ask are unaffected | Accept trust dialog; in `-p` set `projects["<path>"].hasTrustDialogAccepted: true` in `~/.claude.json`. Versions 2.1.196 to 2.1.199 mis-treated own `settings.local.json` as repo-supplied outside git or in home |
| `<path> is a network path, which cannot be added as a working directory` | UNC, `/net/<host>` automounts, links reaching network locations refused as working directories (`/add-dir`, `--add-dir`, `permissions.additionalDirectories`); startup omits it with the message only in the debug log. Before v2.1.257 accepted | Windows: `net use Z: \\server\share` then `claude --add-dir Z:\`; mount locally on macOS/Linux |
| `Two Claude Code config files exist` | `~/.claude/.config.json` (older name) and `~/.claude.json` both exist; the first is used | Find which holds `hasCompletedOnboarding` or `mcpServers`; update all hosts sharing the home to v2.1.319+; stop Claude on all hosts; move the unwanted file aside |
| `Make this change again later: ~/.claude.json could not be updated` | Stderr notice; change (sign-in, trust answer) applies to this session only | Repeat later |

# Limits and defaults

- Subagent description budget warning: 15,000 tokens. Skill and command name maximum: 256 characters.

# Notes

Related session-saving and managed settings warnings: [transcript warnings](./p4-rewind-and-transcript-saving.md), [managed settings errors](./p4-managed-settings-errors.md).
