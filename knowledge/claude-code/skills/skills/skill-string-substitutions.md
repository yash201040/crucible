---
type: "Reference"
title: "Skill string substitutions"
description: "$ARGUMENTS, $N, $name and ${CLAUDE_*} placeholders available inside skill content and allowed-tools rules."
resource: "https://code.claude.com/docs/en/skills"
tags: [skills, arguments, substitution, variables]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "$ARGUMENTS"
  - "$ARGUMENTS[N]"
  - "$N"
  - "$name"
  - "${CLAUDE_SESSION_ID}"
  - "${CLAUDE_EFFORT}"
  - "${CLAUDE_SKILL_DIR}"
  - "${CLAUDE_PROJECT_DIR}"
  - "${CLAUDE_PLUGIN_ROOT}"
  - "${CLAUDE_PLUGIN_DATA}"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "skills"
    resource: "https://code.claude.com/docs/en/skills"
    title: "Extend Claude with skills"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Placeholders replaced in a skill's content before Claude sees it.

# How to use it

| Variable | Meaning |
| :- | :- |
| `$ARGUMENTS` | all arguments; if no placeholder receives one, `ARGUMENTS: <value>` is appended |
| `$ARGUMENTS[N]` | argument by 0-based index |
| `$N` | shorthand, `$0` first, `$1` second |
| `$name` | named argument from the `arguments` frontmatter list, by position |
| `${CLAUDE_SESSION_ID}` | current session ID |
| `${CLAUDE_EFFORT}` | current effort: `low`, `medium`, `high`, `xhigh`, `max` |
| `${CLAUDE_SKILL_DIR}` | directory of the skill's `SKILL.md` (for plugins, the skill subdirectory) |
| `${CLAUDE_PROJECT_DIR}` | project root, same as hooks and MCP servers receive |
| `${CLAUDE_PLUGIN_ROOT}` | plugin install directory; plugin skills only |
| `${CLAUDE_PLUGIN_DATA}` | plugin persistent data directory surviving updates; plugin skills only |

# Limits and defaults

- `${CLAUDE_SKILL_DIR}` and `${CLAUDE_PROJECT_DIR}` (and plugin variables in plugin skills) are substituted both in content and in Bash rules in `allowed-tools`, so a bundled script runs without a prompt, e.g. `allowed-tools: Bash(${CLAUDE_SKILL_DIR}/scripts/render.sh *)`.
- Indexed arguments use shell-style quoting: `/my-skill "hello world" second` gives `$0` = `hello world`, `$1` = `second`.
- An indexed placeholder with no argument (e.g. `$2`) stays literal; a missing named placeholder becomes an empty string.
- Argument values containing `$1` or `$ARGUMENTS` are inserted literally; `${CLAUDE_*}` variables are still replaced after insertion.
- Escape a literal `$` before a digit, `ARGUMENTS` or a declared name with one backslash (`\$1.00`); a doubled backslash does not escape.

# Notes

Stacking skills at the terminal prompt: see [arguments and stacking](./skill-arguments-and-stacking.md).
