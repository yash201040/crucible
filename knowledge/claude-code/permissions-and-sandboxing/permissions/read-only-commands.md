---
type: "Reference"
title: "Built-in read-only Bash commands"
description: "A fixed, non-configurable set of Bash commands runs without prompts, with listed cases that still prompt in Manual mode."
resource: "https://code.claude.com/docs/en/permissions"
tags: [permissions, bash, read-only, prompts]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.290"
surfaces: [cli]
requires: ""
identifiers:
  - "permissions.blockReadsOutsideWorkingDirectories"
  - "ls"
  - "cat"
  - "echo"
  - "pwd"
  - "head"
  - "tail"
  - "grep"
  - "find"
  - "wc"
  - "which"
  - "diff"
  - "stat"
  - "du"
  - "cd"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permissions"
    resource: "https://code.claude.com/docs/en/permissions"
    title: "Configure permissions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Code treats a built-in set as read-only and runs it without a prompt in every mode (except as `permissions.blockReadsOutsideWorkingDirectories` changes for paths outside working directories). The set includes `ls`, `cat`, `echo`, `pwd`, `head`, `tail`, `grep`, `find`, `wc`, `which`, `diff`, `stat`, `du`, `cd` and read-only forms of `git`. It is not configurable; add an `ask` or `deny` rule to require a prompt. In auto mode they can also wait for classifier review.

# How to use it

In Manual mode these still prompt:

| Case | Detail |
| :- | :- |
| Unquoted globs with write/exec-capable flags | `find`, `sort`, `sed`, `git` prompt with an unquoted glob. `ls *.ts` and `head src/*.py` do not |
| `docker` at another daemon | Flags such as `-H`, `--context`, Podman `--url`, `--connection` |
| `file` with `-m`/`--magic-file` or `-f`/`--files-from` | They open the paths named |
| `ps` that could print env | `ps auxe`, `ps aux -e` prompt; `ps aux`, `ps -ef` do not. Dashed-form check needs v2.1.290+ |
| `which` with flags beyond lookup | `-i`/`--read-alias`, `--read-functions` prompt; `which node`, `which -a node` do not |
| Windows network (UNC) paths | `\\server\share\file`; also PowerShell tool |
| Writes to special shell variables | `PATH`, `IFS` set, unset or looped |
| Unparseable commands | Commands over 10,000 characters always prompt |

`cd` into a working or additional directory is read-only, so `cd packages/api && ls` runs without a prompt. Still prompt: `cd` plus `git` when the `cd` changes directory (a no-op `cd` to the cwd does not), and `cd` plus a redirect whose target depends on the new directory (`/dev/null` does not).
