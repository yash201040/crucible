---
type: "Feature"
title: "Organize, filter and resume in the list"
description: "Grouping, pinning, reordering, renaming, deleting, filter prefixes, and bringing back past sessions."
resource: "https://code.claude.com/docs/en/agent-view"
tags: [agent-view, filters, grouping, resume]
kind: "ui"
maturity: "research-preview"
since: "2.1.287"
surfaces: [cli]
requires: ""
identifiers:
  - "a:<name>"
  - "s:<state>"
  - "n:<text>"
  - "o:<text>"
  - "/resume"
  - "/continue"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-view"
    resource: "https://code.claude.com/docs/en/agent-view"
    title: "Manage multiple agents with agent view"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Default grouping is by state: `Ready for review` (open PR needing review or failing checks) and `Needs input` above `Working` and `Completed` (finished, failed and stopped together). `Ctrl+S` switches to grouping by directory (persists). `Ctrl+T` pins (and keeps the process running while idle), `Shift+↑/↓` reorders, `Ctrl+R` renames, `Enter` on a header collapses, `Ctrl+X` stops, twice within two seconds deletes (on a group header deletes the whole group after confirmation). Overflow of `Completed` folds into `… N more`.

# How to use it

Start the dispatch input with a filter:

| Filter | Shows |
| :- | :- |
| `a:<name>` | Sessions running the named agent |
| `s:<state>` | State or group, e.g. `s:working`, `s:ready`; `s:blocked` = everything waiting on you |
| `n:<text>` | Name or first prompt contains text (v2.1.287+) |
| `o:<text>` | Result contains text; bare `o:` lists all with a result |
| `#1234` or PR/MR URL | The session working on that request |
| Other URL | Session whose first prompt held that URL |

Combine `a:`, `s:`, `n:`, `o:` with spaces (all must match), e.g. `s:blocked a:reviewer`. Filters expand collapsed groups and select a match.

Bring back a session: typing a bare `/resume` (or `/continue`) in the dispatch input opens a picker of past sessions of the repository, newest first, including deleted ones; `Enter` resumes it as a background session. `/resume` fails with `isn't available in agent view` when it names an id/search term, the view uses `--cwd`, `--safe-mode`, or a flag such as `--permission-mode` or `--settings`.
