---
type: "Reference"
title: "Hint tag format and when the prompt appears"
description: "Required v, type and value attributes, and the conditions and frequency limits that must all pass for the prompt to show."
resource: "https://code.claude.com/docs/en/plugins/cli-hints"
tags: [plugins, hints, limits, telemetry]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "v"
  - "type"
  - "value"
  - "DISABLE_TELEMETRY"
  - "DO_NOT_TRACK"
  - "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC"
  - "--cloud"
  - "claude -p"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-cli-hints"
    resource: "https://code.claude.com/docs/en/plugins/cli-hints"
    title: "Recommend your plugin from your CLI"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The tag must occupy its own line; a tag embedded mid-line is ignored. Claude Code removes the line from output even when `v` or `type` is unrecognized.

# How to use it

| Attribute | Description |
| :- | :- |
| `v` | Protocol version; `1` is the only supported value |
| `type` | Hint kind; `plugin` is the only supported value |
| `value` | Plugin identifier as `name@marketplace` |

All three are required. Values may be double-quoted or unquoted; an unquoted value cannot contain whitespace.

# Limits and defaults

The prompt appears only in interactive terminal sessions. In `claude -p` runs, subagent runs and hook command output the tag is stripped and no prompt shows. All must also hold:
- Official and installable: `value` names a plugin found in Claude Code's local copy of an official marketplace, not already installed, not blocked by policy.
- Analytics on: never prompts when analytics are off, e.g. `DISABLE_TELEMETRY`, `DO_NOT_TRACK` or `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` is set, or a third-party provider such as Amazon Bedrock with automatic telemetry opt-out.
- Frequency: one prompt per session, one ever per plugin regardless of answer, none once 100 plugins have been prompted for on the machine.
- Not turned off: the user has not chosen "No, and don't show plugin installation hints again".
- Local, attended session: workspace is local (not cloud or remote) and the session is not unattended; sessions started with `--cloud`, serving Remote Control, or an agent-team teammate never prompt.
