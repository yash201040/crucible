---
type: "Reference"
title: "Bash wildcard patterns"
description: "How * works in Bash rules: position matters, trailing ' *' also matches the bare command, and :* is an equivalent suffix."
resource: "https://code.claude.com/docs/en/permissions"
tags: [permissions, bash, wildcards, patterns]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "Bash(npm run *)"
  - "Bash(git commit *)"
  - "Bash(git push *)"
  - "Bash(ls *)"
  - "Bash(ls:*)"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permissions"
    resource: "https://code.claude.com/docs/en/permissions"
    title: "Configure permissions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`*` in a Bash rule matches any text including spaces. A rule with no `*` matches one exact command. Claude Code matches everything before the first `*` as written, so put `*` after the subcommand (`Bash(git log *)` allows only `git log`; `Bash(git *)` allows every git command). A startup warning fires for an allow rule with `*` before the subcommand, such as `Bash(git * main)`.

# How to use it

Example: allow `Bash(npm run *)` and `Bash(git commit *)`, deny `Bash(git push *)` under `permissions`. A push written as `git -C . push` is not matched.

| You write | Matches | Does not match |
| :- | :- | :- |
| `Bash(npm run build)` | `npm run build` | `npm run build --watch` |
| `Bash(npm run *)` | `npm run build`, `npm run test --watch`, `npm run` | `npm install` |
| `Bash(git log * main)` | `git log --oneline main`, `git log -5 main` | `git log main`, `git push origin main` |
| `Bash(git * main)` | `git merge main`, `git push origin main`, `git -c core.fsmonitor=<script> diff main` | `git log` |
| `Bash(* --version)` | `node --version`, `bash -c 'echo hi' --version` | `node -v` |
| `Bash(ls *)` | `ls -la`, `ls` | `lsof` |
| `Bash(ls*)` | `ls -la`, `lsof` | |
| `Bash(* --help *)` | `npm --help x` | `npm --help` |

# Notes

- A trailing ` *` also matches the bare command only when it is the rule's only wildcard.
- The space before a trailing `*` is part of the rule.
- `Bash(ls:*)` equals `Bash(ls *)`. The `:*` form is recognized only at the end; in `Bash(git:* push)` the colon is literal. The dialog writes the space form.
