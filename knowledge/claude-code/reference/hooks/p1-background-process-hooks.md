---
type: "Guide"
title: "Hooks that start a background process"
description: "How to launch long-running programs from a hook without hanging it or losing a deny decision."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, background, stdio, pretooluse]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "async"
  - "stdio went quiet"
  - "refusing to honor the suspect capture"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A hook can start a long-running program (such as a dev server) and leave it running.

# How to use it

- Run the program in the background and redirect its stdout and stderr, e.g. `npm run dev > dev-server.log 2>&1 &`. Without redirection, a non-async hook takes up to 10 seconds to finish after its own process exits.
- Print the decision before starting the background process, and redirect that process's output.
- Example: `"$CLAUDE_PROJECT_DIR"/.claude/hooks/policy-check.sh || exit $?` then `upload-metrics.sh >/dev/null 2>&1 &`. The `|| exit $?` makes a check that exits 2 still block.

# Limits and defaults

- A deny printed by a background process after Claude Code stopped reading (shortly after the hook's own process exits, non-async) does not block.
- If a script prints an allow and then starts a background process without redirecting its stdio, Claude Code blocks the tool call; the error includes `stdio went quiet` and `refusing to honor the suspect capture`.
