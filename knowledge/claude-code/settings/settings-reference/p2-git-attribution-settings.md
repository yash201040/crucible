---
type: "Reference"
title: "Commit and PR attribution settings"
description: "Settings that control the attribution trailer on commits, the text on pull requests and the claude.ai session link."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [settings, git, attribution, commits]
kind: "setting"
maturity: "unlabelled"
since: "2.1.281"
surfaces: []
requires: ""
identifiers:
  - "attribution"
  - "attribution.commit"
  - "attribution.pr"
  - "attribution.sessionUrl"
  - "includeCoAuthoredBy"
  - "prUrlTemplate"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Keys that customise or hide what Claude Code appends to git commits and pull requests. Scope is any file.

# How to use it

| Name | Type | Default | What it does |
| :- | :- | :- | :- |
| `attribution` | object `{commit, pr, sessionUrl}` or `false` | unset | `false` hides all attribution; needs v2.1.281+ (earlier versions reject it and skip the whole settings file). For older readers set `commit` and `pr` to `""` and `sessionUrl` to `false` |
| `attribution.commit` | string | `Co-Authored-By: <name> <noreply@anthropic.com>` | Commit text including trailers; `""` hides it. Name is the model making the commit (for a subagent commit, the subagent's model); `Claude` alone if version unconfirmed; `Claude Code` if the model is not a recognised Claude model (such as via custom `ANTHROPIC_BASE_URL`) |
| `attribution.pr` | string | `🤖 Generated with [Claude Code](https://claude.com/claude-code)` | PR description text; `""` hides it |
| `attribution.sessionUrl` | Boolean | `true` | Append claude.ai session link as a `Claude-Session` trailer on commits and a link in PR descriptions, from cloud or Remote Control sessions |
| `includeCoAuthoredBy` | Boolean | `true` | Deprecated since v2.0.62 (replaced by `attribution`). `false` omits trailer and PR text unless `attribution.commit` or `.pr` is set, which makes it ignored |
| `prUrlTemplate` | string with `{host}`, `{owner}`, `{repo}`, `{number}`, `{url}` | unset | Point rendered PR links (footer badge, tool-result summaries) at an internal review tool. GitLab merge request links keep their URL; links not shaped `/pull/<number>` unchanged; PR numbers Claude writes (`#123`) not rewritten |

# Notes

Once `commit` or `pr` is set, the unset one uses its default text. Claude Code tells Claude that the user's own instructions (CLAUDE.md, memory) about attribution take precedence over these lines, unless set in managed settings.
