---
type: "Feature"
title: "Emitting a claude-code-hint tag"
description: "A CLI or SDK writes a one-line claude-code-hint tag to stderr, gated on CLAUDECODE or CLAUDE_CODE_CHILD_SESSION, to prompt a plugin install."
resource: "https://code.claude.com/docs/en/plugins/cli-hints"
tags: [plugins, hints, environment, stderr]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.172"
surfaces: [cli]
requires: "Plugin listed in claude-plugins-official or another marketplace with an official name; CLAUDE_CODE_CHILD_SESSION needs v2.1.172 or later"
identifiers:
  - "<claude-code-hint />"
  - "CLAUDECODE"
  - "CLAUDE_CODE_CHILD_SESSION"
  - "claude-plugins-official"
  - "claude-community"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-cli-hints"
    resource: "https://code.claude.com/docs/en/plugins/cli-hints"
    title: "Recommend your plugin from your CLI"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A tool detects it runs inside Claude Code and writes `<claude-code-hint />` to stderr. Claude Code strips the line from Bash and PowerShell tool output before the model sees it, then shows the user a one-time install prompt. Applies only to plugins in `claude-plugins-official` or another marketplace with an official name; the community marketplace `claude-community` is not one.

# How to use it

Gate emission on an environment variable:
- `CLAUDECODE`: set to `1` by every Claude Code version in commands run via Bash and PowerShell tools and in hook commands. IDE extensions also set it in integrated terminals, so gating on it alone also emits when a person runs your CLI there.
- `CLAUDE_CODE_CHILD_SESSION`: `1` only in subprocesses Claude Code itself starts; v2.1.172 and later.

Node.js example: `if (process.env.CLAUDECODE) process.stderr.write('<claude-code-hint v="1" type="plugin" value="example-cli@claude-plugins-official" />\n')`. Equivalent patterns exist for Python, Go and shell. Emitting on every invocation is fine since each plugin is prompted once. Test: `CLAUDECODE=1 example-cli` shows the tag on stderr; without the variable nothing extra prints.

# Notes

See [hint format](./hint-format-and-prompt-conditions.md) and [the dialog](./plugin-recommendation-dialog.md).
