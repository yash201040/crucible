---
type: "Concept"
title: "Redirection and tee target checks"
description: "Redirect and tee targets are checked against Edit/Read rules, protected paths and working directories."
resource: "https://code.claude.com/docs/en/permissions"
tags: [permissions, bash, redirection, tee]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.257"
surfaces: [cli]
requires: ""
identifiers:
  - "tee"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permissions"
    resource: "https://code.claude.com/docs/en/permissions"
    title: "Configure permissions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Code checks a redirect target as if Claude read or wrote the file directly.

# How to use it

- Output (`> file`, `>> file`, `2> file`): checked against `Edit` allow/deny rules, protected paths and working directories. `Bash(git commit *)` allows the command, not the target. A target starting with `~` or containing a glob character needs approval.
- Input (`< file`): checked against `Read` allow/deny rules and working directories. A target outside working directories needs approval unless an allow rule covers it; a glob target, or a relative path after a `cd` in the same command, needs approval even if allowed. Input targets are checked from v2.1.257.
- Not checked: `/dev/null`, descriptor forms (`2>&1`, `<&3`), here-docs and here-strings.
- `tee` writes (including `make | tee build.log`) are checked against `Edit` rules, protected paths and working directories; `Bash(tee *)` does not cover a destination outside working directories. Checked from v2.1.269.
