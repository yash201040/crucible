---
type: "Concept"
title: "Critical-path rm protection"
description: "Which rm and rmdir targets count as critical paths, what no allow rule or hook can approve, and the controls that still apply."
resource: "https://code.claude.com/docs/en/permission-modes"
tags: [critical-paths, rm, safety, permissions, sandbox]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.292"
surfaces: [cli]
requires: ""
identifiers:
  - "CLAUDE_CODE_DISABLE_SUBSTITUTION_RM_PROMPT"
  - "CLAUDE_CODE_DISABLE_INLINE_SHELL_RM_PROMPT"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permission-modes"
    resource: "https://code.claude.com/docs/en/permission-modes"
    title: "Choose a permission mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Critical paths are directories Claude Code protects from `rm` and `rmdir`. A critical-path removal is such a command whose target is recognized as one. No allow rule and no `PreToolUse` hook returning `"allow"` approves it, even in modes that skip other prompts. The check can miss commands and does not replace OS controls. A command it misses gets no special handling, so an allow rule, `bypassPermissions` or sandbox auto-allow can approve it unprompted; other approved commands can delete critical paths too.

# How to use it

Always critical: the filesystem root; top-level directories (direct children of root, e.g. `/usr`, `/etc`, `/data`); the home directory (Windows 8.3 short name too, v2.1.292+); Windows drive roots and top-level dirs (`C:\`, `C:\Windows`; spellings `\\?\C:\`, `\\localhost\C$` count as `C:\`, v2.1.292+); the working directory and its parents; additional working directories and parents only for a glob under one (`rm -rf <dir>/*`, not the directory itself).

Also critical:

| Target | Example |
| :- | :- |
| Glob or trailing slash directly under a shell variable | `rm -rf "$DIR"/*` |
| Same under `$1` or `$@` with no value in the command | `rm -rf "$1"/*` |
| Variable plus one common top-level name (`mnt`, `tmp`, `usr`, `Users`) | `rm -rf "$TMPDIR/mnt"` |
| Variable assigned from a directory-printing substitution | `D=$(pwd); rm -rf "$D"` |
| Target only a command substitution, recursive | `rm -rf "$(pwd)"` |
| Trailing substitution after a critical path | `rm -rf ~/$(cmd)` |
| Only backslashes | `rm -rf "\\"` |
| Windows volume GUID path (v2.1.292+) | `rm -rf '\\?\Volume{GUID}\work\build'` |
| Some targets ending `/*` or `/*/` | `rm -rf logs/*/*` |

Looks inside: subshells `(...)`, brace groups, `$(...)`, backticks, `<(...)`, and `sh/bash/zsh -c` scripts (a double-quoted script has variables expanded first; a single-quoted script that binds `$1` to a real value is not flagged). The message `This shell -c script runs rm and could not be checked` counts as a critical-path removal.

Rewrites: guard variables as `rm -rf "${DIR:?}"/*` or use a literal path; use a literal path for always-set variables like `$HOME` and for directory-printing substitutions (a `${D:?}` guard does not help); for command-substitution targets run the substitution first, then remove the printed paths.

# Limits and defaults

Controls that apply whether or not the check recognizes a command: deny rules (an installed mod may still approve some), sandboxing (sandboxed commands can still delete the working directory), and strict sandbox mode (turns off the retry outside the sandbox that an allow rule or `bypassPermissions` could approve silently).

Env switches (read from the launching environment; not honored in a settings `env` block): `CLAUDE_CODE_DISABLE_SUBSTITUTION_RM_PROMPT=1` turns off the check for command-substitution-only targets; `CLAUDE_CODE_DISABLE_INLINE_SHELL_RM_PROMPT=1` turns off the check on a critical path typed directly in a `-c` script such as `~`.
