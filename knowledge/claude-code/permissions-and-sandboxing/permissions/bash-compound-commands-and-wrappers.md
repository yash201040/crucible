---
type: "Concept"
title: "Compound commands and stripped wrappers"
description: "Every subcommand of a compound Bash command must be allowed; a fixed wrapper list is stripped before matching."
resource: "https://code.claude.com/docs/en/permissions"
tags: [permissions, bash, compound-commands, wrappers]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "timeout"
  - "time"
  - "nice"
  - "nohup"
  - "stdbuf"
  - "command"
  - "builtin"
  - "noglob"
  - "xargs"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permissions"
    resource: "https://code.claude.com/docs/en/permissions"
    title: "Configure permissions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Code understands shell operators. Separators recognized: `&&`, `||`, `;`, `|`, `|&`, `&`, newlines. `Bash(safe-cmd *)` does not allow `safe-cmd && other-cmd`; each subcommand must be allowed (rule match or read-only command).

# How to use it

- Deny and ask rules apply if any subcommand matches, including inside subshells, command substitutions and control-flow bodies such as `for`. An ask rule `Bash(git clean *)` still prompts for `cd /tmp && git clean -f`, even in auto mode.
- A trailing `&&` or `||` with nothing after it makes the command unparseable: not split, so `Bash(npm *)` does not approve it.
- Approving a compound command with "Yes, and don't ask again" saves one rule per subcommand needing approval, up to 5 rules. `git status && npm test` saves `npm test`. A `cd` outside working directories gets its own Read rule.
- Stripped before matching (built in, not configurable): `timeout`, `time`, `nice`, `nohup`, `stdbuf`, shell builtins `command` and `builtin`, zsh `noglob`. Not stripped: `command -v` and zsh `nocorrect`.
- A leading assignment of certain known-safe environment variables is stripped, so `Bash(npm test *)` matches `NODE_ENV=test npm test`. Allow rules do not match past other variable assignments; deny and ask rules do (`Bash(rm *)` deny matches `FOO=bar rm -rf tmp/`).
- Bare `xargs` is stripped (`Bash(grep *)` matches `xargs grep pattern`); with flags (`xargs -n1 grep pattern`) it is matched as an `xargs` command.

# Limits and defaults

Environment runners (`direnv exec`, `devbox run`, `mise exec`, `npx`, `docker exec`) are not stripped. `Bash(devbox run *)` matches `devbox run rm -rf .`. Write one rule per inner command, such as `Bash(devbox run npm test)`.
