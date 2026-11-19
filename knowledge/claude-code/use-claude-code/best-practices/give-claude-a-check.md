---
type: "Feature"
title: "Give Claude a check: goal, review, Stop hook"
description: "Verification options from prompt to /goal to a Stop hook to /code-review, including the Stop-hook block cap of eight and its env var."
resource: "https://code.claude.com/docs/en/best-practices"
tags: [verification, stop-hook, goal, code-review, subagents]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "/goal"
  - "/code-review"
  - "/verify"
  - "Stop"
  - "CLAUDE_CODE_STOP_HOOK_BLOCK_CAP"
  - ".claude/settings.json"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "best-practices"
    resource: "https://code.claude.com/docs/en/best-practices"
    title: "Best practices for Claude Code"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude stops when work looks done. Give it a pass/fail check it can run (test file, build exit code, linter, fixture diff script, browser screenshot) so it closes the loop itself. Ask for evidence (command and output) rather than "all tests pass".

# How to use it

| Strictness | Mechanism |
| - | - |
| In the prompt | "run the auth tests after, and keep going until they pass" |
| Goal | `/goal all tests in tests/auth pass and lint is clean`: a separate model checks the conversation after every turn until met; matters for long background runs |
| Stop hook | Runs a script whenever Claude tries to end its turn; exit code 2 sends Claude back to work. Enforced by the harness |
| Independent review | `/code-review` in the terminal reviews the diff in a fresh subagent that never saw the conversation |
| Run the app | `/verify` has Claude build and run the app and look at the result |

Stop hook example in `.claude/settings.json`: event `Stop`, hook `{ "type": "command", "command": "pnpm tsc --noEmit 1>&2 || exit 2" }`. stderr goes back to Claude as the reason it cannot finish.

Spec review prompt: "use a subagent to review the rate limiter diff against SPEC.md ... report gaps that affect correctness and skip style". Keep `skip style`, since a reviewer asked to find problems always finds something.

# Limits and defaults

If a Stop hook blocks eight stops in a row with no tool call between them, Claude Code overrides the next block and ends the turn. Raise the cap with `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP`.
